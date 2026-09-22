# CAD Models

## Files

### STEP (editable, high precision)
- generator.step        — Steel receiver tube, 200 mm OD × 4 m
- cpc_mirror.step       — Compound parabolic concentrator
- condenser_coil.step   — 5-turn coil, 15 mm OD
- evaporator_coil.step  — 7-turn coil, 10 mm OD
- cold_box.step         — 150 L insulated box

### STL (for 3D printing / viewing)
Same names as above, mesh format.

### Scripts
- scripts/generator.py       — Build generator
- scripts/all_components.py  — Build CPC + coils + box
- scripts/assembly.py        — Position all components + render
- scripts/render_stl.py      — Convert STL to PNG

## Coordinate System
- X: width (mm)
- Y: height (mm)
- Z: length along 4 m axis (mm)

## Render Views
- assembly_iso.png   — Isometric
- assembly_side.png  — Side profile (shows 15° tilt)
- assembly_top.png   — Top-down layout

## Regenerate
```bash
cd /root/fridge
freecadcmd cad/scripts/generator.py
freecadcmd cad/scripts/all_components.py
python cad/scripts/assembly.py
