# Build Release Gate

**Current disposition: HOLD - NOT RELEASED FOR FABRICATION, PRESSURE TESTING, AMMONIA CHARGING, OR OPERATION.**

This repository is a preliminary research/design record. Its model outputs and drawings are not an approved pressure-system design. A qualified refrigeration and pressure-vessel engineer, the responsible safety professional, and the authority having jurisdiction must determine whether and how the system can be built. This register tracks evidence still required; it does not provide design values or work instructions.

If physical fabrication has started, stop work on the pressure boundary. Do not pressurize or charge any component based on repository values. For any suspected ammonia release or exposure, move away and follow the site emergency plan; contact local emergency response. Do not approach or attempt a repair unless trained and authorized.

## Unresolved Design Baseline

| Issue | Conflicting or missing repository evidence | Required disposition before release | Status |
|---|---|---|---|
| V-101 design pressure | `COMPONENT_SPECS.md` says 25 bar; `results/bom.csv` says 16 bar. | Engineer establishes and signs the design conditions and basis; update every affected artifact from that controlled decision. | OPEN |
| V-101 port projection | Component spec says 40 mm; earlier drawing brief and local CAD/drawing artifacts use 60 mm. | Approve port geometry, datum, orientation and connection schedule. | OPEN |
| V-101 port opening | Component spec gives 21 mm bore; legacy FreeCAD generator uses the port OD for the opening. | Reconcile model, detail drawing and approved nozzle design. | OPEN |
| V-101 pressure-boundary design | Current wall, caps, nozzles, weld details and stated burst/test claims are not a documented code calculation package. | Complete, independently reviewed calculations and code/jurisdiction determination; replace unsupported claims with approved evidence. | OPEN |
| Test requirements | Repository states hydro/leak values and duration without a released test plan or signed acceptance basis. | Qualified engineer and inspection authority approve test method, limits, safeguards and records; do not use wiki values as instructions. | OPEN |
| Relief protection | Valve schedule gives a set pressure, but no documented capacity calculation, discharge routing, backpressure review or approved device selection. | Complete the relief-system engineering and obtain required approvals. | OPEN |
| CPC dimensions/material | Component spec and BOM conflict on reflector length and thickness; substrate is presented as alternatives. | Freeze material, profile coordinates, dimensions, supports and environmental loads in a controlled drawing. | OPEN |
| Heat exchanger geometry | Condenser/evaporator pitch, headers, end connections and fin geometry are incomplete; legacy CAD uses disconnected rings. | Release manufacturable coil geometry and reconciled cut lists, connection details and inspection criteria. | OPEN |
| Solution tanks | Volume, wall thickness and a general shape are given, but vessel dimensions, head/nozzle details, design conditions and support details are missing. | Complete and approve vessel designs and interfaces; do not infer geometry from volume. | OPEN |
| V-102 integration | Absorber is described as integrated with V-101, but its interface, internals and flow distribution are not defined. | Approve a single consistent vessel/absorber architecture and detailed connections. | OPEN |
| Piping and instruments | Piping lengths are approximate; no controlled isometrics/nozzle schedule. Gauge, sight-glass and relief quantities differ between spec and BOM. | Release P&ID, line list, isometrics, instrument index and reconciled quantities. | OPEN |
| Material compatibility | BOM includes silver-brazing consumables described for copper-steel joints, while project notes prohibit copper/brass in the ammonia circuit. | Review every wetted metal, filler, seal, lubricant and instrument against authoritative compatibility data; remove prohibited options. | OPEN |
| Frame / installation | Total profile length and nominal section exist, but cut list, joints, anchors, wind loads and structural substantiation are absent. | Complete structural calculations and a controlled fabrication/installation drawing. | OPEN |
| Thermal performance | CFD record is a single-cylinder study; its heat-transfer extraction uses an assumed boundary-layer thickness. No prototype test data is tracked. | Validate heat-exchanger design with defensible methods and documented, instrumented prototype testing before claiming performance. | OPEN |
| Thermodynamic validation | Cycle regression checks selected outputs and internal energy closure; mixture VLE comparison is recorded as failed/nonconverged. | Complete independent property/cycle validation, uncertainty and operating-envelope review. | OPEN |
| Build and safety controls | No approved WPS/PQR package, qualified-welder evidence, inspection/acceptance plan, site-specific ammonia risk assessment, or emergency/operating plan is released here. | Responsible engineering, quality and safety authorities approve the complete controlled package for the intended jurisdiction and site. | OPEN |

## Release Evidence Checklist

Do not change the disposition from HOLD until the project has a controlled, revisioned package with all applicable evidence below approved by qualified responsible people:

- Signed design basis, applicable codes/standards, jurisdiction, design conditions and independent design review.
- Reconciled P&ID, equipment list, nozzle schedule, line list/isometrics, interface control and final BOM.
- Code-based calculations for every pressure boundary, support and overpressure-protection function.
- Released drawings and CAD that agree with each other and identify tolerances, materials, welds, inspection and acceptance requirements.
- Material certificates and traceability requirements; approved joining procedures and personnel qualifications.
- Quality/inspection plan, nonconformance process, test plan and controlled records approved by the responsible engineer and authority.
- Site-specific hazard analysis, ammonia compatibility review, emergency response plan and approved operating/maintenance documentation.
- Independent thermodynamic/thermal review and reproducible performance validation with uncertainty documented.
- Final sign-off and release authorization recorded in the project's document-control system.

## Change Control

Do not resolve conflicts by choosing the more conservative-looking value, copying a drawing, or editing one file in isolation. Record the engineering decision, approver, evidence, revision and affected artifacts, then update and review the complete set together. Until then, conflicting items remain **OPEN** and the disposition remains **HOLD**.