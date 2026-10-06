# Said et al. (2016) — Solar NH3/H2O Absorption Chiller Evidence Package

**Source:** S.A.M. Said, K. Spindler, M.A. El-Shaarawi, M.U. Siddiqui, F. Schmid, B. Bierling, M.M.A. Khan, *Design, construction and operation of a solar powered ammonia–water absorption refrigeration system in Saudi Arabia*, International Journal of Refrigeration 62 (2016) 222–231. DOI: 10.1016/j.ijrefrig.2015.10.026.

## Purpose

This directory captures the uploaded primary paper as a structured engineering evidence package for the Solar Absorption Refrigerator project. It is intended for **Claude, Copilot, ChatGPT, and human engineering reviewers**.

The paper itself is not republished here verbatim. The repository contains source metadata, page-level research notes, extracted numerical evidence, architecture/flow-path representations, comparison tables, validation implications, and original diagrams derived from the paper.

## Files

- `01_SOURCE_RECORD.md` — bibliographic and provenance record.
- `02_PAPER_CONTENT_MAP.md` — page-by-page content map.
- `03_EXTRACTED_DATA.md` — numerical operating points and design evidence.
- `04_ARCHITECTURE_FLOWPATH.md` — reconstructed architecture and process-flow notes.
- `05_CLAY_COMPARISON.md` — controlled comparison with the current Clay design.
- `06_VALIDATION_ACTIONS.md` — actions required before using the paper as validation evidence.
- `07_FULL_ENGINEERING_REPORT.md` — full external-review report.
- `data/said2016_operating_points.csv` — machine-readable operating-point dataset.
- `data/said2016_system_features.csv` — machine-readable architecture/features dataset.
- `drawings/said2016_architecture.svg` — original simplified system architecture drawing.
- `drawings/said2016_generator_rectification.svg` — original generator/rectification concept drawing.
- `drawings/said2016_cop_benchmark.svg` — original COP/operating-point benchmark plot.

## Evidence status

**The paper is Tier-1 external experimental evidence for a solar-driven, continuous, pumped NH3/H2O absorption system. It is NOT direct validation of the Clay design.**

Current Clay status remains:

> **HOLD — NOT RELEASED FOR FABRICATION, PRESSURE TESTING, AMMONIA CHARGING, OR OPERATION.**

## Important comparison boundary

The strongest comparable point reported by Said et al. is:

- generator inlet: 140 °C
- condenser/absorber inlet: 45 °C
- evaporator outlet: −4 °C
- cooling capacity: 4.5 kW
- COP: 0.42

This is highly relevant to the Clay hot-climate solar NH3/H2O concept, but Clay currently targets approximately 135/40/−15 °C and 200 W. The colder evaporator and different scale/architecture mean the paper must be used as a benchmark, not as proof that COP = 0.424 is achieved.

Source basis: uploaded primary paper `turn91file0`.
