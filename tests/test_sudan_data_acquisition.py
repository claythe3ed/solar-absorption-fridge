from datetime import date

import pytest

from scripts.data.acquire_sudan_data import (
    ERA5_VARIABLES,
    POWER_PARAMETERS,
    POWER_TILES,
    SOURCES,
    annual_date_ranges,
    parse_power_chunk_filename,
)


def test_five_complete_year_chunks_include_leap_day():
    chunks = annual_date_ranges("20210101", "20251231")
    assert chunks == [
        ("20210101", "20211231"),
        ("20220101", "20221231"),
        ("20230101", "20231231"),
        ("20240101", "20241231"),
        ("20250101", "20251231"),
    ]
    assert sum(
        (date.fromisoformat(f"{end[:4]}-{end[4:6]}-{end[6:8]}")
         - date.fromisoformat(f"{start[:4]}-{start[4:6]}-{start[6:8]}")).days + 1
        for start, end in chunks
    ) == 1826


@pytest.mark.parametrize(
    ("start", "end"),
    [
        ("20210229", "20210301"),
        ("20210102", "20210101"),
        ("2021011", "20210102"),
    ],
)
def test_annual_date_ranges_reject_invalid_intervals(start, end):
    with pytest.raises(ValueError):
        annual_date_ranges(start, end)


def test_nasa_power_tiles_obey_api_limits_and_cover_sudan_bounds():
    assert all(tile["lat_max"] - tile["lat_min"] <= 10 for tile in POWER_TILES)
    assert all(tile["lon_max"] - tile["lon_min"] <= 10 for tile in POWER_TILES)
    assert min(tile["lat_min"] for tile in POWER_TILES) <= 8.641
    assert max(tile["lat_max"] for tile in POWER_TILES) >= 23.143
    assert min(tile["lon_min"] for tile in POWER_TILES) <= 21.814
    assert max(tile["lon_max"] for tile in POWER_TILES) >= 38.582


def test_nasa_power_filename_parser_handles_short_and_compound_parameters():
    assert parse_power_chunk_filename(
        "northeast_PRECTOTCORR_20210101_20211231.json.gz"
    ) == ("northeast", "PRECTOTCORR", "20210101", "20211231")
    assert parse_power_chunk_filename(
        "northwest_ALLSKY_SFC_SW_DWN_20210101_20211231.json.gz"
    ) == ("northwest", "ALLSKY_SFC_SW_DWN", "20210101", "20211231")
    assert parse_power_chunk_filename("not-a-data-chunk.gz") is None


def test_weather_parameters_include_solar_and_thermal_drivers():
    assert {"ALLSKY_SFC_SW_DWN", "ALLSKY_SFC_SW_DNI", "ALLSKY_SFC_SW_DIFF"} <= set(
        POWER_PARAMETERS
    )
    assert {"T2M", "RH2M", "WS10M", "PRECTOTCORR"} <= set(POWER_PARAMETERS)
    assert {
        "2m_temperature",
        "2m_dewpoint_temperature",
        "10m_u_component_of_wind",
        "10m_v_component_of_wind",
        "surface_solar_radiation_downwards",
    } <= set(ERA5_VARIABLES)


def test_sources_retain_licenses_and_pinned_geographic_snapshots():
    assert SOURCES["ocha_boundaries"]["license"] == "CC BY-IGO"
    assert SOURCES["ocha_settlements"]["license"] == "CC BY"
    assert SOURCES["hotosm_places"]["license"] == "ODC-ODbL"
    assert len(SOURCES["ocha_boundaries"]["sha256"]) == 64
