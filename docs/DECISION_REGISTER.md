# Decision Register

**Status: HOLD.** These conflicts are unresolved. No row below authorizes fabrication or selects a design value.

| ID | Item | Source A | Source B / missing evidence | Decision | Basis / evidence required | Approver | Date | Status |
|---|---|---|---|---|---|---|---|---|
| D-001 | V-101 high-side design pressure | 25 bar in `COMPONENT_SPECS.md` | 16 bar in `results/bom.csv`; maximum operating/upset envelope and code basis not approved | OPEN | Approved DB-01 through DB-06 and code-based pressure design review | TBD | TBD | OPEN |
| D-002 | V-101 port projection | 40 mm in `COMPONENT_SPECS.md` | 60 mm in original drawing brief/local drawing artifacts | OPEN | Approved nozzle/port interface drawing, datum, clocking and stress review | TBD | TBD | OPEN |
| D-003 | CPC length | 3980 mm in `COMPONENT_SPECS.md` | 4000 mm in `results/bom.csv` | OPEN | Approved collector assembly envelope and released profile drawing | TBD | TBD | OPEN |
| D-004 | Reflector thickness | 3 mm in `COMPONENT_SPECS.md` | 2 mm in `results/bom.csv` | OPEN | Approved material selection, structural/load basis and drawing | TBD | TBD | OPEN |
| D-005 | Silver-brazing consumable | BOM generator described rods for copper-steel joints | Project rule prohibits copper/brass in ammonia service; joint scope/material compatibility not approved | Removed from ammonia-system BOM pending qualified joining/material review | Approved wetted-material list and joint procedures; do not substitute an unapproved joining method | TBD | 2026-09-30 | OPEN |
| D-006 | Relief and check valve quantities | Component spec lists one of each | BOM lists two of each; location/capacity basis unresolved | OPEN | Approved P&ID, relief sizing, device selection and instrument/valve index | TBD | TBD | OPEN |
| D-007 | Thermodynamic mixture validation | Ziegler-Trepp coefficient sets were compared across sources | Saved teqp mixture-VLE comparison failed at all 12 points; no independent experimental dataset comparison is recorded | OPEN | Reproducible independent comparison to traceable mixture data with uncertainty | TBD | TBD | OPEN |

## Change Control

When a decision is approved, replace `OPEN` only after attaching or linking the evidence, recording the responsible approver and date, and updating every affected specification, BOM, model, drawing, test document, and public summary. If a decision changes the approved design basis, increment the applicable document revisions and repeat impact review. The repository remains **HOLD** until all release-gate items are closed.