# Khartoum Solar-Heat Screening (2021–2025)

**Status: preliminary resource-to-load screening only.** This is not a validated
refrigerator-performance simulation, an approved design basis, or a prediction
of delivered cooling. The project remains **HOLD** under
[`BUILD_RELEASE_GATE.md`](BUILD_RELEASE_GATE.md).

## Initial result

Using the nominal cycle and CPC assumptions currently in the repository, the
Khartoum daily solar-resource screen estimates:

| Quantity | Screening result |
|---|---:|
| NASA POWER nearest grid point | 15.501° N, 32.560° E; reported elevation 407.76 m |
| Weather period | 2021-01-01 to 2025-12-31, 1,826 daily records |
| Mean daily horizontal solar irradiation | 6.47 kWh/m²/day |
| CPC aperture area calculated from current sizing inputs | 1.593 m² |
| Assumed optical × thermal efficiency | 0.75 × 0.65 = 0.4875 |
| Estimated mean useful solar heat | 5.02 kWh/day |
| Nominal cycle generator duty / COP | 471.5 W / 0.424 |
| Mean-energy equivalent at nominal generator duty | 10.65 generator-hours/day |
| Cooling-energy equivalent at nominal COP | 2.13 kWh/day |
| Equivalent fraction of a 200 W, 24 h/day load | 44.4% |
| Days with daily maximum air temperature above 40 °C | 467 of 1,826 |
| Days with daily maximum air temperature above 45 °C | 18 of 1,826 |

Across the weather period, the 5th–95th percentile estimated useful heat is
approximately 4.02–6.06 kWh/day. August has the lowest monthly mean estimate
(4.51 kWh/day), and 78.1% of August days meet the idealized 8-hour generator
heat budget. April and May have mean daily maximum temperatures of 40.9 °C
and 42.2 °C, respectively. The mean daily maximum air temperature is
36.6 °C; the highest reported daily maximum is 45.8 °C. These are gridded
NASA POWER values, not Khartoum station observations.

The “generator-hours” and cooling-energy values are arithmetic energy
equivalents, not runtime predictions. The cycle model assumes fixed
temperatures/compositions, including a 40 °C condenser, and the calculation
assumes the nominal COP stays constant. It does not establish that either
assumption holds through Khartoum’s hot periods.

## Method and reproducibility

The script [`scripts/simulation/khartoum_screening.py`](../scripts/simulation/khartoum_screening.py)
uses NASA POWER's daily point API at Khartoum city coordinates
(15.5007° N, 32.5599° E), explicitly requesting local solar time (LST). NASA
POWER snaps the location to the reported grid point. The two requested
variables are daily all-sky surface shortwave irradiation
(`ALLSKY_SFC_SW_DWN`, kWh/m²/day) and daily maximum 2 m temperature
(`T2M_MAX`, °C). The raw response is stored locally under the ignored
`data/raw/` directory.

From the existing cycle model, the script obtains nominal generator duty and
COP. It calculates aperture area using the existing collector sizing
assumptions (850 W/m² design irradiance, 0.75 optical efficiency, 0.65 thermal
efficiency, and 1.40 sizing margin). Daily heat is then estimated as:

```text
daily useful heat = daily horizontal irradiation × aperture area × 0.75 × 0.65
```

Run from the repository root:

```sh
./venv/bin/python -m scripts.simulation.khartoum_screening
```

To reacquire the source data before analysis:

```sh
./venv/bin/python -m scripts.simulation.khartoum_screening --download
```

Source: [NASA POWER Daily API](https://power.larc.nasa.gov/docs/services/api/temporal/daily/).

## What this does not model

- The actual CPC optical acceptance, incidence-angle modifier, orientation,
  shading, diffuse-sky capture, reflector/cover losses, or measured efficiency.
- Hourly solar variability, startup and shutdown, thermal storage, or the
  unresolved batch/continuous cycle architecture.
- Heat losses as a function of receiver temperature, ambient temperature, and
  wind; nor generator control or useful heat delivered to the working solution.
- Hot-weather performance of the condenser, absorber, or ammonia-water cycle.
- Site station bias/uncertainty, a design weather year, or climate extremes.

Daily horizontal irradiation applied to a fixed aperture efficiency is an
optimistic screening simplification. In particular, the 44.4% figure is **not**
a validated capacity or service-level estimate. DB-02, DB-03, DB-12, DB-13,
cycle validation, and the project release gates remain open. A defensible
performance simulation needs approved site/weather inputs, a measured or
validated collector thermal model, defined storage/operating strategy, and
independent cycle validation.
