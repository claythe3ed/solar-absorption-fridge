# HOLD Blocker Evidence Map

**Purpose:** Identify why the project remains on HOLD and define evidence required to reconsider the disposition. This is a tracking document, not an engineering approval.

**Current disposition:** HOLD — not released for fabrication, pressure testing, ammonia charging, or operation.

**Basis reviewed:** `docs/BUILD_RELEASE_GATE.md`, `docs/DESIGN_BASIS.md`, `docs/DECISION_REGISTER.md`, and `docs/THERMO-AUDIT-01_REPLAN_AND_MULTI_AGENT_TRACKING.md`, plus the corresponding Release Gate and THERMO-AUDIT-01 pages in Solar Absorption Refrigerator Project HQ (Notion, last edited 2026-10-05). Evidence map created from repository/record review; it does not claim independent physical validation or inspection of the complete local worktree.

## Blockers and closure evidence

| Priority | Blocker | Existing evidence / record | Evidence needed to reconsider closure | Status |
|---|---|---|---|---|
| P0 | V-101 design pressure conflict | Component specification: 25 bar; BOM: 16 bar. Decision D-001 and DB-05 open. Model reports about 15.55 bar high side at its nominal point. | Approved design conditions and credible operating/upset envelope; code/jurisdiction basis; qualified pressure-equipment review; all affected specification, BOM, CAD and calculation records reconciled to the approved decision. | OPEN |
| P0 | V-101 pressure boundary not demonstrated | Build Release Gate records 5 mm flat end caps as failing the project's own UG-34 screening at candidate pressures; wall, heads/caps, nozzles and joints lack a complete approved code-calculation package. | Applicable code-based design calculations and independent qualified review; approved drawings, materials, joints, inspection criteria and acceptance records. Screening estimates are not approved dimensions. | OPEN |
| P0 | Overpressure protection / testing / ammonia safety | Relief capacity, discharge routing and backpressure review are not documented as approved; repository test values lack a released, signed test plan. | Scenario-based relief sizing and approved device/discharge design; code-compliant test and inspection plan; site-specific ammonia hazard and emergency plans; responsible approvals. | OPEN |
| P0 | Cycle model species/property consistency | THERMO-AUDIT-01 identifies mixed pure-ammonia and NH3–H2O stream treatment, unquantified water carryover, differing composition/enthalpy bases, and an internal-only global energy closure. | Reproducible state/stream ledger; independent total-mass, NH3, H2O and component-energy balances; explicit separation/rectification assumptions; independently checked mixture-property implementation and uncertainty; documented COP boundary. | OPEN |
| P0 | Property-model validation | D-007 open. LibHub contains IAPWS G4-01, Rizvi–Heidemann experimental VLE, Field–Combs VLE, and other candidate sources. Existing notes warn that equations/tables/applicability require checking against originals; recorded mixture-VLE comparison has unresolved failures/discrepancy. | Check the original sources and data; select points within documented validity ranges; match composition bases/units; reproduce residuals and convergence; record uncertainty and code/tests. A citation alone does not close this item. | OPEN |
| P0 | Cycle architecture OQ-0 unresolved | Audit plan requires comparison of continuous two-fluid, three-fluid diffusion, and intermittent alternatives. Existing model assumes a continuous two-fluid cycle while pump work defaults to zero and rectification is not modeled. | Documented architecture decision using common metrics, explicit circulation/separation mechanism, and matching model/P&ID/BOM assumptions. | OPEN |
| P0 | Wetted materials and joining | Build Release Gate and D-005 identify unresolved copper/brass restrictions and copper–steel joining/brazing conflict. | Traceable compatibility review for all wetted materials, fillers, seals and instruments; approved joining procedures and qualified personnel; BOM/drawings reconciled. | OPEN |
| P1 | V-101 ports and interfaces | D-002: 40 mm versus 60 mm port projection; 21 mm specified bore versus 25 mm in legacy CAD path. | Controlled interface/nozzle drawing with datum, orientation, connection details and qualified review; reconcile all generated and released artifacts. | OPEN |
| P1 | V-102 absorber and flow path | Absorber architecture/internals/flow distribution and integration remain unresolved. | Selected architecture, detailed design, interface/flow distribution basis, and evidence of thermal and hydraulic performance. | OPEN |
| P1 | Heat-exchanger geometry and performance | Release Gate identifies incomplete coil pitch, headers, connections and fin geometry; CFD is preliminary and not prototype validation. | Manufacturable geometry/cut lists; defensible heat-transfer analysis; boundary conditions and assumptions documented; validation plan and measured results with uncertainty before performance claims. | OPEN |
| P1 | Solar resource and cooling-load basis | DB-02, DB-12 and DB-13 remain open; site inputs and acceptance criteria are incomplete. | Traceable site weather/solar data and design envelope; verified load profile; coupled transient/solar model and defined measurement-based acceptance criteria. | OPEN |
| P1 | CAD/spec/BOM/P&ID conflicts | D-003 CPC length 3980/4000 mm; D-004 reflector thickness 3/2 mm; valve/instrument quantities conflict; CAD manufacturability issues are recorded. | Approved controlled design baseline; reconcile drawings, CAD, P&ID, BOM, line/instrument lists and calculations; documented review of affected changes. | OPEN |
| P1 | Quality, structural, inspection and installation package | Gate records missing approved welding/joining, structural supports/anchors/wind-load basis, inspection/acceptance plan and site operating/maintenance package. | Approved structural calculations, qualified procedures/personnel, material traceability, inspection/quality plan, site-specific safety/operating documentation and required approvals. | OPEN |

## Research-source handling rules

1. Use LibHub to identify candidate primary sources and keep citations traceable to exact editions/pages/equations/data.
2. Check original documents for equations, tables, units, uncertainty and applicability before using extracted Markdown/OCR in calculations.
3. Record the calculation or test that used the source, the expected acceptance criterion, the actual result, and a reproducible test/script.
4. Label each claim `VALIDATED`, `MODEL OUTPUT`, `ASSUMPTION`, `PRELIMINARY`, `CONFLICT`, `UNVERIFIED`, or `OPEN`; do not upgrade status because a source was cited.
5. Keep software/research publication status separate from permission to fabricate, pressure-test, charge or operate the physical system.

## Recommended dependency order

1. Close the P0 cycle/property audit sufficiently to establish the architecture and credible pressure/temperature envelope.
2. In parallel, establish the governing code/jurisdiction, design conditions, pressure-boundary basis, relief basis and material compatibility through qualified review.
3. Decide OQ-0 and reconcile the cycle model, P&ID and equipment interfaces to that architecture.
4. Complete absorber/condenser/collector validation and site/load analysis.
5. Reconcile CAD, specifications, BOM, piping/instrumentation and quality/test records.
6. Obtain independent qualified review and explicit approvals before any physical-release decision.

**Disposition rule:** This map does not close any gate. The project remains on HOLD until all applicable release evidence is complete and approved by the responsible qualified people and authority where required.
