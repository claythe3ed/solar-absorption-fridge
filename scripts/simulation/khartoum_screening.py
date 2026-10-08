"""Best-case daily solar-heat screening for the preliminary Khartoum design.

This is not a transient collector or refrigerator performance model. It applies
the existing assumed collector efficiencies to NASA POWER daily horizontal
irradiation and compares that heat budget with the nominal cycle model duty.
"""

import argparse
import datetime as dt
import json
import math
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from src.geometry.solar_collector import DESIGN as COLLECTOR_DESIGN
from src.geometry.solar_collector import required_aperture_area
from src.thermo.cycle_model import DESIGN as CYCLE_DESIGN
from src.thermo.cycle_model import solve_cycle


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_DATA = (
    ROOT
    / "data/raw/sudan/weather/nasa_power/khartoum_daily_2021_2025.json"
)
START = dt.date(2021, 1, 1)
END = dt.date(2025, 12, 31)
LATITUDE = 15.5007
LONGITUDE = 32.5599
PARAMETERS = "ALLSKY_SFC_SW_DWN,T2M_MAX"


def request_url():
    query = urlencode(
        {
            "parameters": PARAMETERS,
            "community": "RE",
            "longitude": LONGITUDE,
            "latitude": LATITUDE,
            "start": START.strftime("%Y%m%d"),
            "end": END.strftime("%Y%m%d"),
            "time-standard": "LST",
            "format": "JSON",
        }
    )
    return f"https://power.larc.nasa.gov/api/temporal/daily/point?{query}"


def load_daily_series(payload):
    parameters = payload["properties"]["parameter"]
    expected_dates = []
    day = START
    while day <= END:
        expected_dates.append(day.strftime("%Y%m%d"))
        day += dt.timedelta(days=1)

    series = {}
    for name in ("ALLSKY_SFC_SW_DWN", "T2M_MAX"):
        values = parameters[name]
        if set(values) != set(expected_dates):
            raise ValueError(
                f"{name} must contain each date from {START} through {END}"
            )
        series[name] = {}
        for date in expected_dates:
            value = values[date]
            if not isinstance(value, (int, float)) or not math.isfinite(value):
                raise ValueError(f"{name} has an invalid value on {date}")
            if value == -999:
                raise ValueError(f"{name} has a missing-value sentinel on {date}")
            if name == "ALLSKY_SFC_SW_DWN" and value < 0:
                raise ValueError(f"Negative solar irradiation on {date}")
            series[name][date] = float(value)

    coordinates = payload["geometry"]["coordinates"]
    if (
        abs(coordinates[0] - LONGITUDE) > 0.1
        or abs(coordinates[1] - LATITUDE) > 0.1
    ):
        raise ValueError(
            f"NASA POWER returned an unexpected grid point: {coordinates}"
        )
    return series, coordinates


def percentile(values, fraction):
    ordered = sorted(values)
    position = (len(ordered) - 1) * fraction
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return ordered[lower]
    return ordered[lower] + (ordered[upper] - ordered[lower]) * (
        position - lower
    )


def build_report(series, coordinates):
    cycle = solve_cycle(CYCLE_DESIGN)
    q_gen_kw = cycle["Q_gen_W"] / 1000.0
    area = required_aperture_area(
        cycle["Q_gen_W"],
        COLLECTOR_DESIGN["irradiance_Wm2"],
        COLLECTOR_DESIGN["optical_eff"],
        COLLECTOR_DESIGN["thermal_eff"],
        COLLECTOR_DESIGN["design_margin"],
    )
    efficiency = (
        COLLECTOR_DESIGN["optical_eff"]
        * COLLECTOR_DESIGN["thermal_eff"]
    )
    cop = cycle["COP"]

    records = []
    for date, irradiation in series["ALLSKY_SFC_SW_DWN"].items():
        heat_kwh = irradiation * area * efficiency
        records.append(
            {
                "date": dt.datetime.strptime(date, "%Y%m%d").date(),
                "ghi_kwh_m2": irradiation,
                "tmax_c": series["T2M_MAX"][date],
                "heat_kwh": heat_kwh,
            }
        )

    by_month = defaultdict(list)
    by_year = defaultdict(list)
    for record in records:
        by_month[record["date"].month].append(record)
        by_year[record["date"].year].append(record)

    heat = [row["heat_kwh"] for row in records]
    ghi = [row["ghi_kwh_m2"] for row in records]
    tmax = [row["tmax_c"] for row in records]
    mean_heat = sum(heat) / len(heat)
    target_cooling_kwh_day = CYCLE_DESIGN["Q_evap_W"] * 24 / 1000.0
    thresholds = {
        hours: 100.0
        * sum(energy >= q_gen_kw * hours for energy in heat)
        / len(heat)
        for hours in (4, 8, 12, 24)
    }

    return {
        "coordinates": coordinates,
        "days": len(records),
        "area_m2": area,
        "efficiency": efficiency,
        "q_gen_kw": q_gen_kw,
        "cop": cop,
        "target_cooling_kwh_day": target_cooling_kwh_day,
        "mean_ghi": sum(ghi) / len(ghi),
        "ghi_p05": percentile(ghi, 0.05),
        "ghi_p95": percentile(ghi, 0.95),
        "mean_heat": mean_heat,
        "heat_p05": percentile(heat, 0.05),
        "heat_p95": percentile(heat, 0.95),
        "heat_min": min(heat),
        "heat_max": max(heat),
        "equivalent_cycle_hours": mean_heat / q_gen_kw,
        "cooling_equivalent": mean_heat * cop,
        "continuous_cooling_fraction": (
            mean_heat * cop / target_cooling_kwh_day
        ),
        "tmax_mean": sum(tmax) / len(tmax),
        "tmax_max": max(tmax),
        "days_tmax_over_40": sum(value > 40 for value in tmax),
        "days_tmax_over_45": sum(value > 45 for value in tmax),
        "thresholds": thresholds,
        "monthly": {
            month: {
                "ghi": sum(row["ghi_kwh_m2"] for row in rows) / len(rows),
                "heat": sum(row["heat_kwh"] for row in rows) / len(rows),
                "tmax": sum(row["tmax_c"] for row in rows) / len(rows),
                "days_8h": 100.0
                * sum(
                    row["heat_kwh"] >= q_gen_kw * 8 for row in rows
                )
                / len(rows),
            }
            for month, rows in sorted(by_month.items())
        },
        "yearly": {
            year: {
                "ghi": sum(row["ghi_kwh_m2"] for row in rows) / len(rows),
                "heat": sum(row["heat_kwh"] for row in rows) / len(rows),
                "tmax": sum(row["tmax_c"] for row in rows) / len(rows),
            }
            for year, rows in sorted(by_year.items())
        },
    }


def print_report(report):
    print("KHARTOUM DAILY SOLAR-HEAT SCREENING — NOT A DESIGN VALIDATION")
    print(f"NASA POWER nearest grid: {report['coordinates']}")
    print(f"Period: {START} through {END} ({report['days']} daily records)")
    print(
        "Solar-heat assumptions: "
        f"{report['area_m2']:.3f} m² aperture × "
        f"{report['efficiency']:.4f} constant optical/thermal efficiency"
    )
    print(
        f"Cycle model: Q_gen={report['q_gen_kw']:.4f} kW, "
        f"COP={report['cop']:.3f}; "
        f"cooling target={report['target_cooling_kwh_day']:.2f} kWh/day"
    )
    print()
    print(
        "Daily irradiation (kWh/m²/day): "
        f"mean {report['mean_ghi']:.2f}, "
        f"P05 {report['ghi_p05']:.2f}, P95 {report['ghi_p95']:.2f}"
    )
    print(
        "Estimated useful heat (kWh/day): "
        f"mean {report['mean_heat']:.2f}, "
        f"P05 {report['heat_p05']:.2f}, P95 {report['heat_p95']:.2f}, "
        f"range {report['heat_min']:.2f}–{report['heat_max']:.2f}"
    )
    print(
        "Mean-energy equivalent: "
        f"{report['equivalent_cycle_hours']:.2f} rated generator-hours/day; "
        f"{report['cooling_equivalent']:.2f} cooling-kWh/day"
    )
    print(
        "That cooling-energy equivalent is "
        f"{100 * report['continuous_cooling_fraction']:.1f}% of a "
        "200 W × 24 h/day target (before storage and all other losses)."
    )
    print(
        "Days whose estimated heat budget reaches rated cycle duty for: "
        + ", ".join(
            f"{hours} h/day {report['thresholds'][hours]:.1f}%"
            for hours in (4, 8, 12, 24)
        )
    )
    print(
        "Daily maximum air temperature: "
        f"mean {report['tmax_mean']:.1f} °C, maximum "
        f"{report['tmax_max']:.1f} °C; "
        f"{report['days_tmax_over_40']} days >40 °C, "
        f"{report['days_tmax_over_45']} days >45 °C."
    )
    print()
    print("Month  GHI mean  Useful heat  Mean daily Tmax  Days with >=8h heat")
    for month, values in report["monthly"].items():
        name = dt.date(2000, month, 1).strftime("%b")
        print(
            f"{name:>3}    {values['ghi']:>5.2f}      "
            f"{values['heat']:>5.2f} kWh       "
            f"{values['tmax']:>5.1f} °C          "
            f"{values['days_8h']:>5.1f}%"
        )
    print()
    print(
        "Caution: daily horizontal irradiation is treated as fully intercepted; "
        "the fixed-efficiency estimate omits CPC incidence-angle response, "
        "collector thermal losses versus ambient/wind, storage, controls, "
        "condenser/absorber derating, and cycle transients."
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_DATA)
    parser.add_argument(
        "--download",
        action="store_true",
        help="download the specified NASA POWER daily series before analysis",
    )
    args = parser.parse_args()

    if args.download:
        args.input.parent.mkdir(parents=True, exist_ok=True)
        request = Request(
            request_url(),
            headers={"User-Agent": "solar-absorption-fridge-screening/1.0"},
        )
        with urlopen(request, timeout=90) as response:
            payload = json.load(response)
        load_daily_series(payload)
        args.input.write_text(json.dumps(payload, separators=(",", ":")))
    else:
        with args.input.open(encoding="utf-8") as data_file:
            payload = json.load(data_file)

    series, coordinates = load_daily_series(payload)
    print_report(build_report(series, coordinates))


if __name__ == "__main__":
    main()
