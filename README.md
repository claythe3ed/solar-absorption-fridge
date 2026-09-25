# Solar Absorption Fridge

![Solar Absorption Fridge — Engineering Diagram](docs/images/solar-fridge-diagram.png)

Solar-powered NH₃-H₂O absorption refrigeration system for off-grid use.
Designed for household deployment in Sudan and similar climates.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![CoolProp](https://img.shields.io/badge/CoolProp-8.0-green.svg)](http://www.coolprop.org/)
[![teqp](https://img.shields.io/badge/teqp-0.23.2-purple.svg)](https://github.com/usnistgov/teqp)
[![Release](https://img.shields.io/badge/release-v0.1.0-blue.svg)](https://github.com/claythe3ed/solar-absorption-fridge/releases/tag/v0.1.0)
[![Status](https://img.shields.io/badge/status-design--complete-brightgreen)]()

---

## Overview

A complete, validated design for a solar-powered absorption refrigerator
that runs entirely on heat — no mechanical compressor, no moving parts.

| Parameter | Value |
|---|---|
| Cooling capacity | 200 W |
| Cold box | 150 L (2 to 8 °C) |
| Working pair | NH₃ (refrigerant) + H₂O (absorbent) |
| COP | 0.424 |
| Solar collector | CPC, 1.59 m² aperture |
| Generator temperature | 135 °C |
| Operating pressures | 2.36 bar (low) / 15.55 bar (high) |

Full design in [`docs/DESIGN_SUMMARY.md`](docs/DESIGN_SUMMARY.md).

---

## Why this exists

CoolProp's HEOS backend requires departure-function parameters
(β<sub>ij</sub>, γ<sub>ij</sub>) for every binary pair. For ammonia-water
(CAS 7664-41-7 + 7732-18-5), those parameters are not available.

This is a **deliberate design choice**, not an oversight. As clarified by
the CoolProp maintainer in
[CoolProp Issue #341](https://github.com/CoolProp/CoolProp/issues/341#issuecomment-5830089558):

> "I think this is a little bit out of scope to use non-reference-grade
> models in CoolProp for a system that wants a reference-grade
> implementation."

CoolProp's scope is limited to reference-grade formulations (Helmholtz
free energy, IAPWS-2001). The Gibbs-excess class of models — including
Ziegler-Trepp — is explicitly out of scope.

**This project provides a validated engineering alternative** for users
who need ammonia-water mixture properties without a REFPROP license.

---

## Three paths for NH₃-H₂O properties

| Path | Status | Accuracy | License |
|---|---|---|---|
| **CoolProp** (pure components) | Works today | NIST-traceable, < 0.1% | MIT |
| **teqp** `AmmoniaWaterTillnerRoth` | Works on x86_64 | IAPWS-2001 reference | MIT |
| **Ziegler-Trepp** (this repo) | Validated | ±0.63 °C vs CoolProp | MIT |

---

## Validation Results

The Ziegler-Trepp implementation was validated against CoolProp for pure
components and published literature for the mixture.

| Test | Computed | Reference | Error |
|---|---|---|---|
| Pure NH₃ at 15.5 bar | 39.70 °C | 40.0 °C (CoolProp) | 0.30 °C |
| Pure NH₃ at 10 bar | 24.65 °C | 24.9 °C (CoolProp) | 0.25 °C |
| Pure H₂O at 1 bar | 98.98 °C | 99.6 °C (NIST) | 0.62 °C |
| y_NH₃ at 15.5 bar, x=0.25 | 0.9059 | 0.90–0.92 (Herold) | in band |
| Cycle COP (T_gen = 135 °C) | 0.424 | 0.4–0.6 (published) | within band |
| Energy balance closure | 0.00 W | 0.00 W (ideal) | exact |

**Full numerical comparison against teqp (IAPWS-2001):** 12 points,
P = 1 to 25 bar, max error **0.63 °C**, mean error **0.32 °C**.

See [`src/thermo/comparison/teqp_vs_zt.py`](src/thermo/comparison/teqp_vs_zt.py)
and [`results/logs/`](results/logs/) for details.

---

## Testing Notes

Five independent approaches were tested. Full summary:

| Approach | Status | Notes |
|---|---|---|
| **CoolProp** (pure components) | ✅ Works | NIST-traceable, < 0.1% error |
| **Ziegler-Trepp** (this repo) | ✅ Validated | Max 0.63 °C error vs CoolProp |
| **teqp** `AmmoniaWaterTillnerRoth` | ✅ Loads | API functional, `get_Ar01()` verified |
| **teqp** VLE solvers | ⚠️ Unstable | 56 grid attempts, 0 physical results |
| **CoolProp** HEOS mixture | ❌ No data | No binary pair for NH₃-H₂O |

### Details

- **CoolProp** does not include binary interaction parameters for
  NH₃-H₂O. Documented at
  [Issue #341](https://github.com/CoolProp/CoolProp/issues/341).
- **teqp 0.23.2** loads `AmmoniaWaterTillnerRoth` and exposes the full
  API. However, the mixture VLE solvers (`mixture_VLE_px`, `mix_VLE_Tp`)
  fail to converge for NH₃-H₂O with physically plausible initial guesses.
  Documented at [teqp Issue #193](https://github.com/usnistgov/teqp/issues/193).
- **Ziegler-Trepp** (this repository) is the validated engineering
  alternative. It is a Gibbs-excess model, not a Helmholtz reference
  formulation, which is why it is not suitable for direct inclusion in
  CoolProp.

---

## Quick Start

```bash
git clone https://github.com/claythe3ed/solar-absorption-fridge.git
cd solar-absorption-fridge

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Thermodynamic validation
python src/thermo/ziegler_trepp_props.py

# Full cycle model
python src/thermo/cycle_model.py

# teqp vs Ziegler-Trepp comparison
python src/thermo/comparison/teqp_vs_zt.py

# Solar collector sizing
python src/geometry/solar_collector.py

# Mechanical components sizing
python src/geometry/components_sizing.py

# Bill of Materials
python src/geometry/bom_quantities.py
```

Requirements

· Python 3.12 or newer
· CoolProp 8.0
· numpy, scipy, matplotlib
· teqp 0.23.2 (optional, for validation)

---

Design Summary

Component Specification
Cooling capacity 200 W
Cold box 150 L, target 2–8 °C
COP 0.424
Working pair NH₃ (refrigerant) + H₂O (absorbent)
Generator / receiver 200 mm × 4 m carbon steel, 2.5 mm wall, 48.5 kg
Solar collector CPC, 400 mm aperture, 3.98 m length, 1.59 m²
Condenser 7.5 m × 15 mm finned steel, air-cooled
Evaporator 6.37 m × 10 mm finned steel, in cold box
Solution heat exchanger 70% effectiveness, 277 W duty
Solution tanks 3.0 L rich + 2.3 L poor
Operating pressures 2.36 bar (low) / 15.55 bar (high)

Full design in docs/DESIGN_SUMMARY.md.

---

Thermodynamic Model

· Pure components (NH₃, H₂O): CoolProp 8.0 (NIST-accurate)
· Mixture (NH₃-H₂O): Ziegler-Trepp (1984) Gibbs-excess model
  · Coefficients E1–E16 cross-validated between two independent
    sources (Kherris 2013, Sadhukhan et al.)
  · Bubble and dew points: Patek & Klomfar (1995)
· Reference validation: teqp 0.23.2 (AmmoniaWaterTillnerRoth)
  · 12 pure-component points, max error 0.63 °C
  · Full mixture VLE comparison: convergence issues documented

---

CAD Models

All models generated by Python scripts in FreeCAD 1.0 (headless).

Component Dimensions Script
Generator 200 mm OD × 4 m, 2.5 mm wall cad/scripts/generator.py
CPC Mirror 400 mm × 3980 mm parabolic cad/scripts/all_components.py
Condenser 15 mm × 7.5 m, 5 rings cad/scripts/all_components.py
Evaporator 10 mm × 6.37 m, 7 rings cad/scripts/all_components.py
Cold Box 700 × 700 × 800 mm hollow cad/scripts/all_components.py

Assembly renders in results/plots/.

---

Bill of Materials

35 items across 8 categories. Quantities only — no prices, since the
SDG/USD rate is not stable.

Full list in results/bom.csv. Generator script:
src/geometry/bom_quantities.py.

---

Project Structure

```text
solar-absorption-fridge/
├── src/
│   ├── thermo/              # Thermodynamic models
│   │   ├── ziegler_trepp_props.py
│   │   ├── cycle_model.py
│   │   ├── ammonia_properties.py
│   │   └── comparison/      # teqp vs ZT validation
│   ├── geometry/            # Solar, components, BOM, P&ID
│   └── main.py
├── cad/
│   ├── scripts/             # FreeCAD generator scripts
│   ├── step/                # STEP files
│   └── stl/                 # STL files
├── docs/
│   ├── DESIGN_SUMMARY.md
│   ├── SESSION_SUMMARY.md
│   ├── images/              # Engineering diagrams
│   ├── datasheets/          # Coefficient tables
│   ├── patents/             # Reference patents
│   └── report/              # PDF report + HTML source
├── results/
│   ├── plots/               # P&ID, assembly renders
│   ├── logs/                # Simulation logs
│   └── bom.csv              # Bill of Materials
└── notes/
    └── log.md               # Development journal
```

---

Documentation

· Design Report (PDF) — 6-page Swiss-design report
· Wiki — Detailed design notes
· CoolProp Issue #341 — NH₃-H₂O binary pair gap
· teqp Issue #193 — ARM64 build + VLE findings
· Design Summary — Components and cycle data
· Session Summary — Development log

---

References

· Ziegler & Trepp (1984), Int. J. Refrigeration 7(2):101–106
· Patek & Klomfar (1995), Int. J. Refrigeration 18(4):228–234
· Tillner-Roth & Friend (1998), J. Phys. Chem. Ref. Data 27(1):63–96
· Kherris et al. (2013), Thermal Science 17(3):891–902
· Herold, Radermacher, Klein — Absorption Chillers and Heat Pumps, CRC Press

---

Related Work

· teqp — Same author as CoolProp.
  Provides AmmoniaWaterTillnerRoth() as a direct implementation of
  Tillner-Roth & Friend (1998). Recommended by the CoolProp maintainer.
· CoolProp Issue #341 —
  The long-standing gap this project documents and works around.

---

License

MIT — see LICENSE.

---

Author

Muhammad Ali (@claythe3ed)