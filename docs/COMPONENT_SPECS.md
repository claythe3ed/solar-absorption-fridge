# Component Specifications — Manufacturing Data

Supplementary engineering specifications for V-101 through FRAME-01.
These values are the outcome of design decisions made during the
project. They complement `DESIGN_SUMMARY.md` (which lists principal
dimensions only).

---

## V-101 Generator / Solar Receiver

### Geometry (from `cad/scripts/generator.py`)

| Parameter | Value |
|---|---|
| Outer diameter | 200 mm |
| Wall thickness | 2.5 mm |
| Inner diameter | 195 mm (derived) |
| Total length | 4000 mm |
| End-cap thickness | 5 mm |
| End-cap material | ASTM A516 Gr.70 carbon steel plate |
| Port outer diameter | 25 mm |
| **Port wall thickness** | **2 mm** |
| **Port protrusion** | **40 mm** |
| **Port hole diameter** | **21 mm (drilled through shell)** |
| Mass (hollow steel) | 48.5 kg |

### Operating conditions

| Parameter | Value |
|---|---|
| Operating pressure (high side) | 15.55 bar |
| **Design pressure** | **25 bar** |
| Operating temperature | 135 °C |
| **Hydro test pressure** | **25 bar, duration 24 h** |
| **N₂ leak test** | **After hydro, hold 1 h, ΔP < 10 mbar** |
| **Minimum burst pressure** | **> 60 bar (calculated)** |

### Welding

| Joint | Type | Size | Process | Inspection |
|---|---|---|---|---|
| End cap → shell | Full-penetration butt weld, V-groove 60° | Full pen. | **TIG only** | **100% RT + 100% PT** |
| Port P1 → shell | Fillet weld | **3 mm leg** | TIG | **100% PT** |
| Port P2 → shell | Fillet weld | 3 mm leg | TIG | 100% PT |
| Port P3 → shell | Fillet weld | 3 mm leg | TIG | 100% PT |
| Port P4 → shell | Fillet weld | 3 mm leg | TIG | 100% PT |

**Notes:**
- TIG filler: ER70S-6, 2.4 mm diameter
- Shielding gas: Argon 99.99%, 8–12 L/min
- Interpass temperature: < 150 °C
- Backing gas: Argon purge inside shell during root pass

### Coating

| Surface | Coating | Spec |
|---|---|---|
| Outer cylindrical surface | Selective black | α/ε > 5 |
| Ports, end caps | Bare | For NDT and welding |
| Internal surfaces | None | Ammonia compatible |

### Tolerances

| Dimension | Tolerance |
|---|---|
| Overall length | ±1.0 mm |
| Outer diameter | ±0.5 mm |
| Wall thickness | ±0.2 mm |
| Port axial position | ±1.0 mm |
| Port angular position (clock) | ±2° |
| Straightness (over 4 m) | < 2 mm |
| Roundness (cross-section) | < 1 mm |

### Materials

| Item | Spec |
|---|---|
| Main pipe | ASTM A106 Gr.B seamless |
| End caps | ASTM A516 Gr.70 plate |
| Port stubs | ASTM A106 Gr.B seamless |
| **Mill test certificate** | **Required per ASTM A106 and A516** |
| Traceability | Heat number stamped on each piece |

### NDT requirements

| Method | Extent | Standard |
|---|---|---|
| Dye penetrant (PT) | 100% of all welds | ASME V, Art. 6 |
| Radiographic (RT) | 100% of end-cap welds | ASME V, Art. 2 |
| Hydrostatic | Full vessel, 25 bar, 24 h | ASME VIII Div.1 UG-99 |
| Leak (N₂) | After hydro, 1 h hold | ASME V, Art. 10 |

### Assembly notes

1. All dimensions in millimeters unless noted.
2. Pipe shall be seamless — no longitudinal seam welds.
3. TIG welding only for all pressure-boundary joints.
4. End-cap welds: full-penetration butt with V-groove 60°.
5. Port welds: 3 mm fillet, continuous, all around.
6. Hydro test at 25 bar for 24 h before coating.
7. Selective black coating on outer cylindrical surface only.
8. Ports and end cap edges left bare for NDT.
9. Mill test certificates required for all pressure parts.
10. Heat numbers stamped near each weld for traceability.

---

## V-102 Absorber

Integrated with the generator vessel. See V-101 dimensions.
Extra specifications: (to be added in future revision)

---

## E-101 CPC Mirror

| Parameter | Value |
|---|---|
| Aperture width | 400 mm |
| Length | 3980 mm |
| Depth | 80 mm |
| Wall thickness (mirror) | 3 mm |
| Aperture area | 1.59 m² |
| Acceptance half-angle | 30° |
| Concentration ratio | 2.0 |
| Mirror material | Polished aluminum (or acrylic) |
| Cover glass | Low-iron tempered, 4 mm |
| Frame | Galvanized steel angle 40×40×3 mm |
| Orientation | East–West horizontal |
| Tilt | 15° (local latitude) |

---

## E-102 Condenser

| Parameter | Value |
|---|---|
| Heat load | 274.8 W |
| Tube outer diameter | 15 mm |
| Tube wall | 2 mm |
| Coil diameter | 300 mm |
| Total tube length | 7.5 m |
| Number of rings | 5 |
| Fin material | Aluminum 0.5 mm |
| Fin spacing | 6 fins per ring |
| Material | Carbon steel tube + Al fins |
| U-value (design) | 15 W/m²·K |
| U-value (CFD) | 21.23 W/m²·K |

---

## E-103 SHX (Solution Heat Exchanger)

| Parameter | Value |
|---|---|
| Type | Tube-in-tube counterflow |
| Hot side tube | 25 mm OD, 2 mm wall |
| Cold side tube | 12 mm OD, 1.5 mm wall |
| Length | 2 m |
| Effectiveness | 70% |
| Heat duty | 277 W |

---

## E-104 Evaporator

| Parameter | Value |
|---|---|
| Heat load | 200 W |
| Tube outer diameter | 10 mm |
| Tube wall | 1.5 mm |
| Coil diameter | 300 mm |
| Total tube length | 6.37 m |
| Number of rings | 7 |
| Fin material | Aluminum 0.5 mm |
| Fin spacing | 8 fins per ring |
| U-value (design) | 25 W/m²·K |
| Operating temperature | -15 °C |

---

## V-103 Rich Solution Tank

| Parameter | Value |
|---|---|
| Volume | 3.0 L |
| Solution | 40% NH₃ by mass |
| Material | Carbon steel, 3 mm wall |
| Shape | Vertical cylinder with rounded caps |
| Connection | 15 mm NPT outlet |

---

## V-104 Poor Solution Tank

| Parameter | Value |
|---|---|
| Volume | 2.3 L |
| Solution | 25% NH₃ by mass |
| Material | Carbon steel, 3 mm wall |
| Shape | Vertical cylinder with rounded caps |
| Connection | 15 mm NPT outlet |

---

## BOX-01 Cold Box

| Parameter | Value |
|---|---|
| External dimensions | 700 × 700 × 800 mm |
| Internal dimensions | 500 × 500 × 600 mm |
| Wall thickness | 100 mm PU foam |
| Internal volume | 150 L |
| Operating temperature | 2–8 °C |
| Door | Hinged, front-face |
| Material (cabinet) | Stainless 304 or painted carbon steel |
| Gasket | Magnetic, neoprene-free |

---

## VLV-SET Valves

| Tag | Type | Size | Spec |
|---|---|---|---|
| VLV-101 | Expansion capillary | 0.6 mm ID × 1.5 m | Coiled, stainless |
| VLV-102 | Needle valve | 1/4" NPT | Manual |
| — | Safety relief valve | 25 bar set | 1/4" NPT, stainless |
| — | Check valve | 1/4" NPT | Cracking 0.2 bar |
| — | Ball valve (×4) | 1/4" NPT | Isolation |
| — | Schrader charging | 1/4" SAE | For ammonia charge |

---

## INST-SET Instruments

| Tag | Type | Range | Location |
|---|---|---|---|
| TIC-101 | Type-K thermocouple | -50 to 200 °C | Generator |
| PI-102 | Pressure gauge | 0–25 bar | Condenser |
| — | Type-K (×3) | -50 to 200 °C | T_evap, T_cond, T_abs |
| — | Sight glass | — | Liquid line |

---

## PIPE-SET Piping

| Line | Size | Length | Material |
|---|---|---|---|
| Vapor + solution (main) | 15 mm OD, 2 mm wall | ~6 m | Carbon steel |
| Liquid NH₃ + instruments | 8 mm OD, 1.5 mm wall | ~4 m | Carbon steel |
| Elbows 90° | 15 mm | ×12 | Carbon steel |
| Tees | 15 mm | ×4 | Carbon steel |
| Reducers 15→8 mm | — | ×4 | Carbon steel |

---

## FRAME-01 Support Frame

| Parameter | Value |
|---|---|
| Profile | Galvanized steel angle 40×40×3 mm |
| Total length | 12 m |
| Fasteners | Stainless M8–M12 |
| Load capacity | > 200 kg |
| Orientation | Adjustable tilt 0–30° (for latitude) |

---

## General Notes (apply to all components)

1. All dimensions in millimeters unless noted.
2. **Copper, brass, and zinc fittings are FORBIDDEN** in the ammonia circuit.
3. Carbon steel or stainless 304/316 only for wetted parts.
4. Ammonia-compatible seals: PTFE, Viton. NOT neoprene.
5. All NPT threads: use PTFE tape or ammonia-compatible sealant.
6. Work in outdoor/ventilated space when handling ammonia.
7. Full-face respirator with ammonia cartridges required.
8. Eye-wash station within 10 m of any ammonia work.
9. Never heat generator above 180 °C.
10. Pressure test every subsystem before charging.

---

**Document version:** v0.2.0
**Date:** 28 September 2026
**Author:** Muhammad Ali (claythe3ed)
**Project:** Solar NH₃-H₂O Absorption Refrigerator
