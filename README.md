# Solar Absorption Fridge

Solar-powered NH₃-H₂O absorption refrigeration system for off-grid use.
Designed for household deployment in Sudan and similar climates.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![CoolProp](https://img.shields.io/badge/CoolProp-8.0-green.svg)](http://www.coolprop.org/)
[![Status](https://img.shields.io/badge/status-design--complete-blue)]()

---

## Why this exists

CoolProp — the reference open-source library for thermodynamic properties —
**does not include a binary interaction pair for ammonia-water**
(CAS [7664-41-7, 7732-18-5]). This blocks any NH₃-H₂O absorption refrigeration,
power, or Kalina cycle simulation using CoolProp's HEOS backend.

This gap has been open since 2014
([CoolProp#341](https://github.com/CoolProp/CoolProp/issues/341)).

This project provides a **validated standalone alternative** using the
Ziegler-Trepp (1984) Gibbs-excess formulation, and documents the situation
for maintainers and users.

- **CoolProp Issue comment (2026-09-22):**
  [Link to comment](https://github.com/CoolProp/CoolProp/issues/341#issuecomment-5782035587)

---

## What it solves

| Problem | Solution in this repo |
|---|---|
| CoolProp cannot mix NH₃ + H₂O | Custom Gibbs-excess model in `src/thermo/ziegler_trepp_props.py` |
| No validated NH₃-H₂O code for Termux/ARM64 | Pure Python + CoolProp pure-component backend |
| No reference design for off-grid solar absorption | Full cycle model + CAD + P&ID + BOM |
| No mixture coefficient traceability | Cross-validated coefficients in `docs/datasheets/` |

---

## Quick Start

```bash
# Clone
git clone https://github.com/claythe3ed/solar-absorption-fridge.git
cd solar-absorption-fridge

# Install dependencies
pip install CoolProp numpy scipy matplotlib

# Run thermodynamic validation
python src/thermo/ziegler_trepp_props.py

# Run full cycle model
python src/thermo/cycle_model.py

# Size solar collector
python src/geometry/solar_collector.py

# Size all mechanical components
python src/geometry/components_sizing.py
```

---

Validation Results

The Ziegler-Trepp implementation was validated against CoolProp
(pure components) and published literature:

Test Computed Reference Error
Pure NH₃ at 15.5 bar 39.70 °C 40.0 °C (CoolProp) 0.30 °C
Pure NH₃ at 10 bar 24.65 °C 24.9 °C (CoolProp) 0.25 °C
Pure H₂O at 1 bar 98.98 °C 99.6 °C (NIST) 0.62 °C
y_NH₃ at 15.5 bar, x=0.25 0.9059 0.90–0.92 (Herold et al.) within band
Cycle COP (T_gen=135°C) 0.424 0.4–0.6 (published) within band
Energy balance closure 0.00 W 0.00 W (ideal) exact

Coefficients cross-validated 100% between Kherris et al. (2013) and
Sadhukhan et al. (see docs/datasheets/).

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
Solution tanks 3.0 L rich + 2.3 L poor
Operating pressures 2.36 bar (low) / 15.55 bar (high)

Full design in docs/DESIGN_SUMMARY.md.

---

Project Structure

```
solar-absorption-fridge/
├── src/
│   ├── thermo/         # Thermodynamic models (Ziegler-Trepp + CoolProp)
│   ├── geometry/       # Solar collector, components, BOM, P&ID
│   └── main.py         # Entry point
├── cad/
│   ├── scripts/        # FreeCAD scripts (generator, coils, assembly)
│   ├── step/           # STEP files (regenerate via scripts)
│   └── stl/            # STL files (regenerate via scripts)
├── docs/
│   ├── DESIGN_SUMMARY.md
│   ├── datasheets/     # Coefficient tables (Kherris, Sadhukhan, ZT)
│   └── patents/        # US1781541, EP0374179 concept CSVs
├── results/
│   ├── plots/          # P&ID, assembly renders, validation plots
│   └── logs/           # Simulation logs
└── notes/
    └── log.md          # Development journal
```

---

Thermodynamic Model

· Pure components (NH₃, H₂O): CoolProp 8.0 (NIST-accurate)
· Mixture (NH₃-H₂O): Ziegler-Trepp (1984) Gibbs-excess model
  · Coefficients E1–E16 cross-validated between two independent sources
  · Bubble/dew points: Patek & Klomfar (1995)
· Reference: Tillner-Roth & Friend (1998) — IAPWS-2001 formulation
  (not implementable in CoolProp without β_ij/γ_ij data)

---

References

· Ziegler & Trepp (1984), Int. J. Refrigeration 7(2):101–106
  DOI: 10.1016/0140-7007(84)90022-7
· Patek & Klomfar (1995), Int. J. Refrigeration 18(4):228–234
  DOI: 10.1016/0140-7007(95)00006-W
· Tillner-Roth & Friend (1998), J. Phys. Chem. Ref. Data 27(1):63–96
  DOI: 10.1063/1.556015
· Kherris et al. (2013), Thermal Science 17(3):891–902
  DOI: 10.2298/TSCI110206083K
· Herold, Radermacher, Klein — Absorption Chillers and Heat Pumps, CRC Press

---

Related Work

· teqp (usnistgov/teqp) — same author as CoolProp, provides
  AmmoniaWaterTillnerRoth() as a direct implementation of Tillner-Roth &
  Friend (1998). Recommended by the CoolProp maintainer.
· CoolProp Issue #341 — the long-standing gap this project documents
  and works around.

---

License

MIT — see LICENSE.

---

Author

Muhammad Ali (claythe3ed) — @claythe3ed
