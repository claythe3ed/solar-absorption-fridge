#!/usr/bin/env python3
"""Acquire versioned Sudan boundary and weather-source data for later review.

This script downloads source data only. It does not run refrigerator
simulations, correct weather data, or make engineering design decisions.
"""

from __future__ import annotations

import argparse
import calendar
import gzip
import hashlib
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
GEOGRAPHY_DIR = ROOT / "data/raw/sudan/geography"
WEATHER_DIR = ROOT / "data/raw/sudan/weather"
METADATA_DIR = ROOT / "data/metadata/sudan"

SOURCES = {
    "ocha_boundaries": {
        "url": (
            "https://data.humdata.org/dataset/a66a4b6c-92de-4507-9546-aa1900474180/"
            "resource/018af991-4aa7-4043-a0d5-e429a55851fb/download/"
            "sdn_admin_boundaries.geojson.zip"
        ),
        "file": "ocha_cod_ab_sdn_geojson_2026.zip",
        "sha256": "75330d4e12e53f966df0e5683e04f0919e9964952fbbf827f3729038e603c95e",
        "license": "CC BY-IGO",
        "dataset": "OCHA/HDX Sudan COD-AB v03; resource updated 2026-01-26",
    },
    "ocha_settlements": {
        "url": (
            "https://data.humdata.org/dataset/1862de60-eb45-4373-ad8a-efb2facc44f5/"
            "resource/b068b383-34c9-43b2-9b32-213509f78e34/download/"
            "sudan_settlement_26july20.zip"
        ),
        "file": "ocha_sudan_settlements_2020.zip",
        "sha256": "3799ad439abc09a2a26668475d9826c61b0528f3bffa470e256fa32a24fd400b",
        "license": "CC BY",
        "dataset": "OCHA/HDX Sudan: Settlements; layer date 2020-07-26",
    },
    "hotosm_places": {
        "url": (
            "https://production-raw-data-api.s3.amazonaws.com/ISO3/SDN/"
            "populated_places/hotosm_sdn_populated_places_osm_geojson.zip"
        ),
        "file": "hotosm_sudan_populated_places_2026_geojson.zip",
        "sha256": "dfed550283539f93163a69ee655130f907e5db7ce3bd4e06f2e4415a1f55859b",
        "license": "ODC-ODbL",
        "dataset": "HOTOSM populated places from OpenStreetMap; snapshot 2026-09-06",
    },
    "hotosm_metadata": {
        "url": (
            "https://production-raw-data-api.s3.amazonaws.com/ISO3/SDN/"
            "populated_places/hotosm_sdn_populated_places_osm_metadata.json"
        ),
        "file": "hotosm_sudan_populated_places_2026_metadata.json",
        "sha256": None,
        "license": "ODC-ODbL",
        "dataset": "HOTOSM source snapshot metadata; 2026-09-06",
    },
}

POWER_PARAMETERS = (
    "ALLSKY_SFC_SW_DWN",
    "ALLSKY_SFC_SW_DNI",
    "ALLSKY_SFC_SW_DIFF",
    "T2M",
    "T2M_MAX",
    "T2M_MIN",
    "RH2M",
    "WS10M",
    "PRECTOTCORR",
)

# Every NASA POWER regional tile is <=10 degrees in either coordinate.
POWER_TILES = (
    {"name": "southwest", "lat_min": 8.5, "lat_max": 18.5,
     "lon_min": 21.5, "lon_max": 31.5},
    {"name": "southeast", "lat_min": 8.5, "lat_max": 18.5,
     "lon_min": 31.5, "lon_max": 38.75},
    {"name": "northwest", "lat_min": 18.5, "lat_max": 23.5,
     "lon_min": 21.5, "lon_max": 31.5},
    {"name": "northeast", "lat_min": 18.5, "lat_max": 23.5,
     "lon_min": 31.5, "lon_max": 38.75},
)

ERA5_DATASET = "reanalysis-era5-land"
ERA5_VARIABLES = [
    "2m_temperature",
    "2m_dewpoint_temperature",
    "10m_u_component_of_wind",
    "10m_v_component_of_wind",
    "surface_solar_radiation_downwards",
    "surface_thermal_radiation_downwards",
    "total_precipitation",
    "surface_pressure",
]
ERA5_VARIABLE_CODES = {"t2m", "d2m", "u10", "v10", "ssrd", "strd", "tp", "sp"}
ERA5_AREA = [23.25, 21.75, 8.5, 38.75]  # north, west, south, east


def annual_date_ranges(start: str, end: str) -> list[tuple[str, str]]:
    from datetime import date

    try:
        first = date.fromisoformat(f"{start[:4]}-{start[4:6]}-{start[6:8]}")
        last = date.fromisoformat(f"{end[:4]}-{end[4:6]}-{end[6:8]}")
    except (ValueError, IndexError) as exc:
        raise ValueError("Dates must be valid calendar dates in YYYYMMDD format") from exc
    if len(start) != 8 or len(end) != 8 or not start.isdigit() or not end.isdigit():
        raise ValueError("Dates must use YYYYMMDD")
    if first > last:
        raise ValueError("Start date must not be after end date")

    chunks = []
    for year in range(first.year, last.year + 1):
        chunk_start = max(first, date(year, 1, 1))
        chunk_end = min(last, date(year, 12, 31))
        chunks.append((chunk_start.strftime("%Y%m%d"), chunk_end.strftime("%Y%m%d")))
    return chunks


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_power_chunk_filename(filename: str) -> tuple[str, str, str, str] | None:
    parts = Path(filename).name.removesuffix(".json.gz").split("_")
    if len(parts) < 4:
        return None
    return parts[0], "_".join(parts[1:-2]), parts[-2], parts[-1]


def download(url: str, target: Path, expected_sha256: str | None = None) -> str:
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        actual = sha256_file(target)
        if expected_sha256 is None or actual == expected_sha256:
            return actual
        raise RuntimeError(
            f"Existing file has unexpected checksum: {target} "
            f"(expected {expected_sha256}, got {actual}); move it aside before retrying"
        )

    request = urllib.request.Request(
        url,
        headers={"User-Agent": "solar-absorption-fridge-data-preparation/1.0"},
    )
    temporary = target.with_suffix(target.suffix + ".part")
    try:
        with urllib.request.urlopen(request, timeout=120) as response, temporary.open("wb") as out:
            while True:
                chunk = response.read(1024 * 1024)
                if not chunk:
                    break
                out.write(chunk)
    except Exception:
        temporary.unlink(missing_ok=True)
        raise

    actual = sha256_file(temporary)
    if expected_sha256 is not None and actual != expected_sha256:
        temporary.unlink(missing_ok=True)
        raise RuntimeError(
            f"Checksum mismatch for {target.name}: expected {expected_sha256}, got {actual}"
        )
    temporary.replace(target)
    return actual


def safe_extract(zip_path: Path, destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    root = destination.resolve()
    with zipfile.ZipFile(zip_path) as archive:
        for entry in archive.infolist():
            relative = PurePosixPath(entry.filename)
            if relative.is_absolute() or ".." in relative.parts:
                raise ValueError(f"Unsafe path in archive {zip_path}: {entry.filename}")
            output = (destination / Path(*relative.parts)).resolve()
            if root not in output.parents and output != root:
                raise ValueError(f"Archive member escapes destination: {entry.filename}")
        archive.extractall(destination)


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def acquire_geography() -> None:
    manifest: dict[str, Any] = {
        "acquired_utc": datetime.now(timezone.utc).isoformat(),
        "sources": {},
    }
    for key, source in SOURCES.items():
        target = GEOGRAPHY_DIR / source["file"]
        checksum = download(source["url"], target, source["sha256"])
        manifest["sources"][key] = {
            "url": source["url"],
            "dataset": source["dataset"],
            "license": source["license"],
            "file": str(target.relative_to(ROOT)),
            "sha256": checksum,
        }
        print(f"{key}: {target.relative_to(ROOT)} sha256={checksum}")

    boundary_extract = GEOGRAPHY_DIR / "ocha_cod_ab_sdn_geojson_2026"
    places_extract = GEOGRAPHY_DIR / "hotosm_sudan_populated_places_2026"
    safe_extract(GEOGRAPHY_DIR / SOURCES["ocha_boundaries"]["file"], boundary_extract)
    safe_extract(GEOGRAPHY_DIR / SOURCES["ocha_settlements"]["file"], GEOGRAPHY_DIR / "ocha_settlements_2020")
    safe_extract(GEOGRAPHY_DIR / SOURCES["hotosm_places"]["file"], places_extract)
    write_json(METADATA_DIR / "geography_acquisition.json", manifest)
    validate_geography()


def validate_geography() -> None:
    import geopandas as gpd

    admin_dir = GEOGRAPHY_DIR / "ocha_cod_ab_sdn_geojson_2026"
    expected = {
        "sdn_admin0.geojson": 1,
        "sdn_admin1.geojson": 19,
        "sdn_admin2.geojson": 189,
    }
    for filename, count in expected.items():
        path = admin_dir / filename
        if not path.exists():
            raise FileNotFoundError(f"Missing OCHA boundary source: {path}")
        layer = gpd.read_file(path)
        if len(layer) != count:
            raise ValueError(f"{filename}: expected {count} records, found {len(layer)}")
        if layer.crs is None or layer.crs.to_epsg() != 4326:
            raise ValueError(f"{filename}: expected WGS84 coordinates, got {layer.crs}")
        if not layer.geometry.is_valid.all():
            raise ValueError(f"{filename}: invalid geometry found")
        print(f"{filename}: {len(layer)} records; CRS={layer.crs}; geometries valid")

    admin1 = gpd.read_file(admin_dir / "sdn_admin1.geojson")
    if "adm1_name" not in admin1:
        raise ValueError("OCHA ADM1 layer has no adm1_name field")
    special = admin1[admin1["adm1_name"].astype(str).str.contains("Abyei", case=False)]
    print(f"ADM1 features: {len(admin1)} (includes {len(special)} Abyei special-area feature(s))")

    ocha_places = (
        GEOGRAPHY_DIR / "ocha_settlements_2020" / "Sudan_Settlement_26July20.shp"
    )
    if ocha_places.exists():
        places = gpd.read_file(ocha_places)
        print(f"OCHA settlement records: {len(places)}; CRS={places.crs}; "
              f"geometry types={sorted(places.geometry.geom_type.unique())}")

    osm_metadata = GEOGRAPHY_DIR / "hotosm_sudan_populated_places_2026/metadata.json"
    if osm_metadata.exists():
        details = json.loads(osm_metadata.read_text(encoding="utf-8"))
        data = details.get("metadata", details)
        feature_count = data.get("feature_count")
        if feature_count is not None:
            print(f"HOTOSM metadata feature count: {feature_count}; "
                  "features are mixed geometries and not all are named settlements")


def validate_nasa_power(start: str = "20210101", end: str = "20251231") -> int:
    import datetime

    expected: set[tuple[str, str, str, str]] = set()
    for tile in POWER_TILES:
        for parameter in POWER_PARAMETERS:
            for year_start, year_end in annual_date_ranges(start, end):
                expected.add((tile["name"], parameter, year_start, year_end))

    seen: set[tuple[str, str, str, str]] = set()
    for path in sorted((WEATHER_DIR / "nasa_power").glob("*.json.gz")):
        key = parse_power_chunk_filename(path.name)
        if key is None:
            continue
        _, parameter, file_start, file_end = key
        if key not in expected:
            continue
        with gzip.open(path, "rt", encoding="utf-8") as stream:
            payload = json.load(stream)
        header = payload.get("header", {})
        if header.get("start") != file_start or header.get("end") != file_end:
            raise ValueError(f"Date header mismatch in {path}")
        if header.get("time_standard") != "UTC":
            raise ValueError(f"NASA POWER timestamps are not UTC in {path}")
        features = payload.get("features")
        if not isinstance(features, list) or not features:
            raise ValueError(f"No grid features in {path}")
        date_start = datetime.datetime.strptime(file_start, "%Y%m%d").date()
        date_end = datetime.datetime.strptime(file_end, "%Y%m%d").date()
        expected_days = (date_end - date_start).days + 1
        for feature in features:
            values = feature.get("properties", {}).get("parameter", {}).get(parameter)
            if not isinstance(values, dict) or len(values) != expected_days:
                raise ValueError(
                    f"{path}: expected {expected_days} daily values for {parameter}"
                )
            if any(not isinstance(value, (int, float)) for value in values.values()):
                raise ValueError(f"Non-numeric daily value found in {path}")
        seen.add(key)

    absent = expected - seen
    print(f"NASA POWER daily chunks verified: {len(seen)}/{len(expected)}; "
          f"expected interval {start}-{end} in UTC.")
    if absent:
        print(f"NASA POWER incomplete: {len(absent)} tile/parameter/year chunks missing.")
        for item in sorted(absent)[:8]:
            print("  missing:", " / ".join(item))
    return len(absent)


def validate_era5_land(start_year: int = 2021, end_year: int = 2025) -> int:
    import calendar as calendar_module
    import xarray as xr

    out_dir = WEATHER_DIR / "era5_land"
    expected_count = (end_year - start_year + 1) * 12
    present = 0
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            path = out_dir / f"era5_land_hourly_{year}_{month:02d}.nc"
            if not path.exists():
                continue
            with xr.open_dataset(path) as dataset:
                time_name = next(
                    (name for name in ("valid_time", "time") if name in dataset.coords),
                    None,
                )
                if time_name is None:
                    raise ValueError(f"No recognized time coordinate in {path}")
                expected_hours = calendar_module.monthrange(year, month)[1] * 24
                actual_hours = dataset.sizes.get(time_name, 0)
                if actual_hours != expected_hours:
                    raise ValueError(
                        f"{path}: expected {expected_hours} hourly samples, found {actual_hours}"
                    )
                missing_vars = ERA5_VARIABLE_CODES - set(dataset.data_vars)
                if missing_vars:
                    raise ValueError(f"{path}: missing ERA5 variables {sorted(missing_vars)}")
                present += 1
    print(f"ERA5-Land monthly files verified: {present}/{expected_count} "
          f"for {start_year}-{end_year}.")
    if present < expected_count:
        print(f"ERA5-Land incomplete: {expected_count - present} monthly files missing.")
    return expected_count - present


def fetch_url_json(url: str, retries: int = 4) -> dict[str, Any]:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "solar-absorption-fridge-data-preparation/1.0"},
    )
    last_error: Exception | None = None
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(request, timeout=180) as response:
                payload = json.load(response)
            if payload.get("messages"):
                errors = [str(message) for message in payload["messages"]]
                if any("failed" in message.lower() or "error" in message.lower() for message in errors):
                    raise RuntimeError("; ".join(errors))
            return payload
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            try:
                body = json.loads(detail)
                messages = body.get("messages", [])
                explanation = "; ".join(str(message) for message in messages) or detail[:500]
            except json.JSONDecodeError:
                explanation = detail[:500]
            if 400 <= exc.code < 500 and exc.code != 429:
                raise RuntimeError(f"NASA POWER returned HTTP {exc.code}: {explanation}") from exc
            last_error = RuntimeError(f"HTTP {exc.code}: {explanation}")
            if attempt + 1 < retries:
                time.sleep(2 ** attempt)
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, RuntimeError) as exc:
            last_error = exc
            if attempt + 1 < retries:
                time.sleep(2 ** attempt)
    assert last_error is not None
    raise RuntimeError(f"NASA POWER request failed after {retries} attempts: {last_error}")


def acquire_nasa_power(start: str, end: str) -> None:
    date_ranges = annual_date_ranges(start, end)

    out_dir = WEATHER_DIR / "nasa_power"
    manifest: dict[str, Any] = {
        "source": "NASA POWER Daily API, regional spatial option",
        "api": "https://power.larc.nasa.gov/api/temporal/daily/regional",
        "start": start,
        "end": end,
        "time_standard": "UTC",
        "community": "RE",
        "parameters": list(POWER_PARAMETERS),
        "tiles": list(POWER_TILES),
        "note": "Bounding-box grid includes non-Sudan points; clip only in a logged downstream step.",
        "responses": [],
        "acquired_utc": datetime.now(timezone.utc).isoformat(),
    }
    for tile in POWER_TILES:
        if tile["lat_max"] - tile["lat_min"] > 10.0 or tile["lon_max"] - tile["lon_min"] > 10.0:
            raise ValueError(f"NASA POWER regional tile exceeds its 10-degree API limit: {tile}")
        for parameter in POWER_PARAMETERS:
            for year_start, year_end in date_ranges:
                query = {
                    "latitude-min": tile["lat_min"],
                    "latitude-max": tile["lat_max"],
                    "longitude-min": tile["lon_min"],
                    "longitude-max": tile["lon_max"],
                    "parameters": parameter,
                    "community": "RE",
                    "start": year_start,
                    "end": year_end,
                    "format": "JSON",
                    "time-standard": "UTC",
                }
                url = (
                    "https://power.larc.nasa.gov/api/temporal/daily/regional?"
                    + urllib.parse.urlencode(query)
                )
                payload = fetch_url_json(url)
                features = payload.get("features")
                if not isinstance(features, list) or not features:
                    raise ValueError(
                        f"NASA POWER returned no grid features for "
                        f"{tile['name']} {parameter} {year_start}-{year_end}"
                    )
                path = out_dir / (
                    f"{tile['name']}_{parameter}_{year_start}_{year_end}.json.gz"
                )
                path.parent.mkdir(parents=True, exist_ok=True)
                temporary = path.with_suffix(path.suffix + ".part")
                with gzip.open(temporary, "wt", encoding="utf-8") as stream:
                    json.dump(payload, stream, separators=(",", ":"))
                temporary.replace(path)
                checksum = sha256_file(path)
                manifest["responses"].append({
                    "tile": tile["name"],
                    "parameter": parameter,
                    "start": year_start,
                    "end": year_end,
                    "feature_count": len(features),
                    "file": str(path.relative_to(ROOT)),
                    "sha256": checksum,
                })
                print(f"NASA POWER {tile['name']} {parameter} "
                      f"{year_start}-{year_end}: {len(features)} points "
                      f"-> {path.relative_to(ROOT)}")
                time.sleep(0.25)

    write_json(METADATA_DIR / f"nasa_power_{start}_{end}.json", manifest)


def acquire_era5_land(start_year: int, end_year: int) -> None:
    if start_year > end_year:
        raise ValueError("Start year must not be after end year")
    if start_year < 1950 or end_year > datetime.now(timezone.utc).year:
        raise ValueError("ERA5-Land years must be from 1950 through the current year")
    try:
        import cdsapi
    except ImportError as exc:
        raise RuntimeError(
            "ERA5-Land retrieval needs optional dependencies: "
            "python3 -m pip install -r requirements-data.txt"
        ) from exc

    # Client construction will report missing CDS credentials/configuration.
    client = cdsapi.Client()
    out_dir = WEATHER_DIR / "era5_land"
    manifest: dict[str, Any] = {
        "dataset": ERA5_DATASET,
        "variables": ERA5_VARIABLES,
        "area_north_west_south_east": ERA5_AREA,
        "years": [start_year, end_year],
        "time_utc": [f"{hour:02d}:00" for hour in range(24)],
        "format": "netcdf",
        "requests": [],
        "acquired_utc": datetime.now(timezone.utc).isoformat(),
        "note": "Rectangular subset includes neighboring territory; apply reviewed Sudan polygon downstream.",
    }
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            target = out_dir / f"era5_land_hourly_{year}_{month:02d}.nc"
            if target.exists():
                manifest["requests"].append({
                    "year": year,
                    "month": month,
                    "file": str(target.relative_to(ROOT)),
                    "sha256": sha256_file(target),
                    "status": "already-present",
                })
                print(f"Skip existing {target.relative_to(ROOT)}")
                continue
            request = {
                "variable": ERA5_VARIABLES,
                "year": f"{year:04d}",
                "month": f"{month:02d}",
                "day": [
                    f"{day:02d}"
                    for day in range(1, calendar.monthrange(year, month)[1] + 1)
                ],
                "time": [f"{hour:02d}:00" for hour in range(24)],
                "area": ERA5_AREA,
                "data_format": "netcdf",
                "download_format": "unarchived",
            }
            target.parent.mkdir(parents=True, exist_ok=True)
            temporary = target.with_suffix(".nc.part")
            print(f"Request ERA5-Land {year}-{month:02d}")
            client.retrieve(ERA5_DATASET, request, str(temporary))
            if not temporary.exists() or temporary.stat().st_size == 0:
                raise RuntimeError(f"CDS returned an empty file for {year}-{month:02d}")
            temporary.replace(target)
            checksum = sha256_file(target)
            manifest["requests"].append({
                "year": year,
                "month": month,
                "file": str(target.relative_to(ROOT)),
                "sha256": checksum,
                "status": "downloaded",
            })
            write_json(METADATA_DIR / f"era5_land_{start_year}_{end_year}.json", manifest)

    write_json(METADATA_DIR / f"era5_land_{start_year}_{end_year}.json", manifest)


def prepare_settlement_layers() -> None:
    import geopandas as gpd

    ocha_path = GEOGRAPHY_DIR / "ocha_settlements_2020/Sudan_Settlement_26July20.shp"
    osm_path = GEOGRAPHY_DIR / "hotosm_sudan_populated_places_2026/populated_places.geojson"
    if not ocha_path.exists() or not osm_path.exists():
        raise FileNotFoundError(
            "Download/extract both settlement sources first with the geography command"
        )

    output_dir = ROOT / "data/processed/sudan"
    output_dir.mkdir(parents=True, exist_ok=True)
    ocha = gpd.read_file(ocha_path)
    if ocha.crs is None or ocha.crs.to_epsg() != 4326:
        raise ValueError(f"Unexpected OCHA settlement CRS: {ocha.crs}")
    ocha_columns = {
        "featureRef": "source_reference",
        "featureNam": "name",
        "feature_AR": "name_ar_source",
        "Type_Text": "place_type",
        "feature_pc": "source_id",
        "ADM1_PCODE": "adm1_code_source",
        "ADM1_EN": "adm1_name_source",
        "ADM2_PCODE": "adm2_code_source",
        "ADM2_EN": "adm2_name_source",
        "date": "feature_date",
        "validOn_1": "valid_on_source",
    }
    missing_ocha = set(ocha_columns) - set(ocha.columns)
    if missing_ocha:
        raise ValueError(f"OCHA settlement layer is missing fields: {sorted(missing_ocha)}")
    ocha_out = ocha[list(ocha_columns)].rename(columns=ocha_columns).copy()
    if ocha_out["source_id"].isna().any() or not ocha_out["source_id"].is_unique:
        raise ValueError("OCHA source place codes must be present and unique")
    ocha_out.insert(0, "source", "OCHA/HDX Sudan Settlements 2020")
    ocha_gdf = gpd.GeoDataFrame(ocha_out, geometry=ocha.geometry, crs=ocha.crs)
    ocha_out_path = output_dir / "ocha_sudan_settlements_2020.geojson"
    ocha_gdf.to_file(ocha_out_path, driver="GeoJSON", index=False)

    osm = gpd.read_file(osm_path)
    if osm.crs is None or osm.crs.to_epsg() != 4326:
        raise ValueError(f"Unexpected HOTOSM populated places CRS: {osm.crs}")
    settlement_types = {"city", "town", "village", "hamlet", "isolated_dwelling"}
    osm_points = osm[
        osm.geometry.geom_type.eq("Point") & osm["place"].isin(settlement_types)
    ].copy()
    osm_columns = {
        "id": "source_id",
        "name": "name",
        "name_en": "name_en",
        "name_ar": "name_ar",
        "place": "place_type",
        "population": "population_source",
        "adm1_pcode": "adm1_code_source",
        "adm1_name": "adm1_name_source",
        "adm2_pcode": "adm2_code_source",
        "adm2_name": "adm2_name_source",
    }
    missing_osm = set(osm_columns) - set(osm_points.columns)
    if missing_osm:
        raise ValueError(f"HOTOSM places layer is missing fields: {sorted(missing_osm)}")
    osm_out = osm_points[list(osm_columns)].rename(columns=osm_columns).copy()
    if osm_out["source_id"].isna().any() or not osm_out["source_id"].is_unique:
        raise ValueError("HOTOSM source IDs must be present and unique")
    osm_out.insert(0, "source", "HOTOSM/OSM snapshot 2026-09-06")
    osm_gdf = gpd.GeoDataFrame(osm_out, geometry=osm_points.geometry, crs=osm.crs)
    osm_out_path = output_dir / "hotosm_sudan_settlement_points_2026.geojson"
    osm_gdf.to_file(osm_out_path, driver="GeoJSON", index=False)

    report = {
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "coordinate_reference_system": "EPSG:4326",
        "deduplication": "none; source-specific IDs and records retained",
        "ocha": {
            "source_layer": "OCHA Sudan Settlements, 2020-07-26",
            "features": len(ocha_gdf),
            "geometry_types": ocha_gdf.geometry.geom_type.value_counts().to_dict(),
            "output": str(ocha_out_path.relative_to(ROOT)),
            "arabic_source_note": (
                "Original Arabic attribute text retained as read; inspect encoding "
                "against the source before using Arabic labels."
            ),
        },
        "hotosm": {
            "source_layer": "HOTOSM/OSM snapshot 2026-09-06",
            "selected_point_features": len(osm_gdf),
            "place_types": osm_gdf["place_type"].value_counts(dropna=False).to_dict(),
            "missing_name": int(
                osm_gdf["name"].fillna("").astype(str).str.strip().eq("").sum()
            ),
            "unique_source_ids": int(osm_gdf["source_id"].nunique()),
            "output": str(osm_out_path.relative_to(ROOT)),
        },
        "warning": (
            "These source layers are separate inventories, not a complete official "
            "gazetteer; no automated deduplication or completeness claim is made."
        ),
    }
    write_json(output_dir / "settlement_inventory_audit.json", report)
    print(f"OCHA settlements: {len(ocha_gdf)} -> {ocha_out_path.relative_to(ROOT)}")
    print(f"HOTOSM point features in selected settlement classes: {len(osm_gdf)}; "
          f"missing names={report['hotosm']['missing_name']} -> "
          f"{osm_out_path.relative_to(ROOT)}")
    print("Source layers remain separate; no duplicate matching was attempted.")


def validate_sources() -> None:
    missing: list[str] = []
    for key, source in SOURCES.items():
        path = GEOGRAPHY_DIR / source["file"]
        if not path.exists():
            missing.append(f"{key}: {path.relative_to(ROOT)}")
        elif source["sha256"] and sha256_file(path) != source["sha256"]:
            raise ValueError(f"Checksum mismatch: {path}")
    for expected in ("sdn_admin0.geojson", "sdn_admin1.geojson", "sdn_admin2.geojson"):
        path = GEOGRAPHY_DIR / "ocha_cod_ab_sdn_geojson_2026" / expected
        if not path.exists():
            missing.append(str(path.relative_to(ROOT)))
    if missing:
        print("Missing geography inputs:")
        for item in missing:
            print(f"  - {item}")
        print("Acquire them with: python3 scripts/data/acquire_sudan_data.py geography")
        raise RuntimeError("Geography source coverage is incomplete")
    validate_geography()
    missing_power = validate_nasa_power()
    missing_era5 = validate_era5_land()
    if missing_power or missing_era5:
        raise RuntimeError(
            "Weather coverage is incomplete: "
            f"{missing_power} NASA POWER chunks and {missing_era5} ERA5-Land months missing"
        )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("geography", help="Download OCHA boundaries and settlement sources")
    power = subparsers.add_parser("nasa-power", help="Download tiled NASA POWER daily grid")
    power.add_argument("--start", default="20210101", help="Start date, YYYYMMDD")
    power.add_argument("--end", default="20251231", help="End date, YYYYMMDD")
    era5 = subparsers.add_parser("era5-land", help="Retrieve hourly ERA5-Land files through CDS")
    era5.add_argument("--start-year", type=int, default=2021)
    era5.add_argument("--end-year", type=int, default=2025)
    subparsers.add_parser(
        "prepare-settlements",
        help="Create separate normalized OCHA and HOTOSM point inventories",
    )
    subparsers.add_parser("validate", help="Check source archives and acquisition coverage")
    args = parser.parse_args()

    try:
        if args.command == "geography":
            acquire_geography()
        elif args.command == "nasa-power":
            acquire_nasa_power(args.start, args.end)
        elif args.command == "era5-land":
            acquire_era5_land(args.start_year, args.end_year)
        elif args.command == "prepare-settlements":
            prepare_settlement_layers()
        elif args.command == "validate":
            validate_sources()
    except (RuntimeError, ValueError, FileNotFoundError, zipfile.BadZipFile) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
