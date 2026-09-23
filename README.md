# Solar Absorption Fridge

![Solar Absorption Fridge — Engineering Diagram](docs/images/solar-fridge-diagram.png)

Solar-powered NH3-H2O absorption refrigeration system for off-grid use.
Designed for household deployment in Sudan and similar climates.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![CoolProp](https://img.shields.io/badge/CoolProp-8.0-green.svg)](http://www.coolprop.org/)
[![Release](https://img.shields.io/badge/release-v0.1.0-blue.svg)](https://github.com/claythe3ed/solar-absorption-fridge/releases/tag/v0.1.0)
[![Status](https://img.shields.io/badge/status-design--complete-brightgreen)]()

---

## Why this exists

CoolProp does not include a binary interaction pair for ammonia-water (CAS 7664-41-7, 7732-18-5). This blocks any NH3-H2O absorption refrigeration, power, or Kalina cycle simulation using CoolProp HEOS backend.

This gap has been open since 2014 ([CoolProp#341](https://github.com/CoolProp/CoolProp/issues/341)).

This project provides a validated standalone alternative using the Ziegler-Trepp (1984) Gibbs-excess formulation.

[CoolProp Issue comment](https://github.com/CoolProp/CoolProp/issues/341#issuecomment-5782035587)

---

## Quick Start

pip install CoolProp numpy scipy matplotlib
python src/thermo/ziegler_trepp_props.py
python src/thermo/cycle_model.py

---

## Validation Results

| Test | Computed | Reference | Error |
|---|---|---|---|
| Pure NH3 at 15.5 bar | 39.70 C | 40.0 C (CoolProp) | 0.30 C |
| Pure NH3 at 10 bar | 24.65 C | 24.9 C (CoolProp) | 0.25 C |
| Pure H2O at 1 bar | 98.98 C | 99.6 C (NIST) | 0.62 C |
| y_NH3 at 15.5 bar, x=0.25 | 0.9059 | 0.90-0.92 (Herold) | in band |
| Cycle COP | 0.424 | 0.4-0.6 (published) | within band |

---

## Design Summary

| Component | Specification |
|---|---|
| Cooling capacity | 200 W |
| Cold box | 150 L, target 2-8 C |
| COP | 0.424 |
| Generator | 200 mm x 4 m carbon steel, 48.5 kg |
| Solar collector | CPC, 1.59 m2 aperture |
| Condenser | 7.5 m x 15 mm finned |
| Evaporator | 6.37 m x 10 mm finned |
| Operating pressures | 2.36 / 15.55 bar |

---

## Documentation

- [Design Report PDF](docs/report/solar-fridge-report.pdf)
- [Wiki](https://github.com/claythe3ed/solar-absorption-fridge/wiki)
- [CoolProp Issue 341](https://github.com/CoolProp/CoolProp/issues/341#issuecomment-5782035587)
- [Design Summary](docs/DESIGN_SUMMARY.md)

---

## References

- Ziegler & Trepp (1984), Int. J. Refrigeration 7(2):101-106
- Patek & Klomfar (1995), Int. J. Refrigeration 18(4):228-234
- Tillner-Roth & Friend (1998), J. Phys. Chem. Ref. Data 27(1):63-96
- Kherris et al. (2013), Thermal Science 17(3):891-902
- Herold, Radermacher, Klein — Absorption Chillers and Heat Pumps

---

## License

MIT

## Author

Muhammad Ali ([@claythe3ed](https://github.com/claythe3ed))
