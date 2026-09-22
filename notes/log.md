# Project Log

## 2026-09-21
- Project structure created.
- Cycle selected: ammonia-water absorption.
- Available books: University Physics Vol 2, Vol 3, Calculus Vol 1.

## Session 3 - CoolProp Installed
- Ubuntu 25.10 with Python 3.13.7
- CoolProp 8.0.0 installed successfully (manylinux wheel)
- numpy 2.5.3, scipy 1.18.1, matplotlib 3.11.2, pandas 3.0.6
- Bind mount: Termux ~/solar-absorption-fridge <-> Ubuntu /root/fridge
- Created test_coolprop.py and test_solution.py

## Session 6 - Cross-Validation Complete
- Extracted tables from 3 papers successfully
- Kherris and Sadhukhan A,B,C,D coefficients MATCH exactly
- E1-E16 coefficients MATCH exactly between both papers
- Patek-Klomfar bubble/dew point coefficients obtained
- Saved master reference file: docs/datasheets/ziegler_trepp_coefficients.md
- Next: write ziegler_trepp_props.py

## Session 7 - Cycle Validated & Components Sized
- COP = 0.424 (realistic for NH3-H2O)
- Q_gen = 471.5 W
- Solar collector: 400mm aperture x 3.98m = 1.593 m^2
- Receiver pipe: 200mm OD steel, 4m long (= generator)
- Next: FreeCAD drawings and mechanical assembly

## Session 7 Final - Design Locked
- All component sizes calculated
- Generator: 200mm × 4m, 48.5 kg steel
- Condenser: 7.5m of 15mm finned
- Evaporator: 6.37m of 10mm finned
- DESIGN_SUMMARY.md created

## Session 8 - CAD Complete
- All 5 components modeled in FreeCAD 1.0 (freecadcmd headless)
- Generator: 200mm × 4m, 6.57 L steel, 48.5 kg
- CPC Mirror: parabolic trough, 400×4000mm
- Condenser Coil: 5 tori, 15mm tube
- Evaporator Coil: 7 tori, 10mm tube
- Cold Box: 700×700×800mm hollow, 242 L
- Assembly rendered (3 views)
- FreeCAD 1.0 API notes: exportStl has no kwargs; use shape.tessellate + Mesh.Mesh
- All files: cad/step/*.step, cad/stl/*.stl, results/plots/*.png

## Session 10 - BOM Complete
- Generated BOM: 35 items, $2,184 USD (1.31M SDG)
- Categories: steel pipes (24%), fabrication (18%), solar (14%), valves (13%)
- CSV exported: results/bom.csv
- Procurement notes for Sudan included

## Session 11 - Final Report PDF
- Report generated with WeasyPrint 69
- Swiss design, cream + red-brown palette
- 6 pages: cover, design, thermodynamics, components, BOM, status
- Files: report.html (source), style.css (styles), solar-fridge-report.pdf
Tue Sep 22 22:36:53 CAT 2026
