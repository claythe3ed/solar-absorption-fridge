# THERMO-AUDIT-01 — NH3-H2O Cycle Model Audit & Multi-Agent Re-Plan

**Status:** OPEN — P0 / CRITICAL  
**Project disposition:** HOLD — NOT RELEASED FOR FABRICATION, PRESSURE TESTING, AMMONIA CHARGING, OR OPERATION  
**Purpose:** Establish a controlled, evidence-driven work package for auditing the thermodynamic cycle before further design commitment.

## 1. Why the project plan was reset

Independent reviews by ChatGPT, Claude, and Copilot converged on the need to change the order of engineering work.

The project should no longer progress primarily by closing the 20 governance entries one-by-one. The work must instead follow technical dependencies: first establish whether the cycle model is internally consistent and whether the architecture itself has been adequately selected; then proceed to pressure/material safety, thermal hardware, solar-system simulation, and CAD reconciliation.

The 20 formal DB-/D- entries remain the governance register. They are not replaced by this work package.

## 2. Current baseline

The current nominal model reports:

- Cooling capacity: 200 W
- Evaporator: -15 °C
- Condenser: 40 °C
- Generator: 135 °C
- Absorber: 30 °C
- COP: 0.424
- High side: 15.55 bar
- Low side: 2.36 bar
- Refrigerant flow: approximately 0.68 kg/h
- Solution circulation ratio: 4.37

These remain model/design-point values, not validated system performance or approved fabrication inputs.

## 3. Critical finding: species-consistency audit

Copilot identified a potentially material limitation in `src/thermo/cycle_model.py::solve_cycle()`:

- generator vapor composition `y_3` is used in the solution ammonia balance;
- refrigerant flow is obtained from a pure-ammonia evaporator balance;
- condenser duty combines mixed-vapor enthalpy with pure-ammonia liquid enthalpy;
- the P&ID labels the generator stream `y=0.906` but shows liquid ammonia downstream without an explicit rectification/water-carryover balance;
- vapor composition is calculated at the solution bubble point while vapor enthalpy is evaluated at a separate fixed generator temperature.

Therefore the present model does not yet establish a species-by-species NH3/H2O mass and energy balance.

**Important:** this is an audit finding, not a proposed correction. Do not alter the model until the existing equations and assumptions have been fully traced.

## 4. THERMO-AUDIT-01 objectives

Audit the complete cycle implementation component-by-component.

### A. State and stream audit

For every state and stream:

- identify phase;
- identify pressure and temperature basis;
- identify NH3 mass fraction/composition;
- identify H2O composition;
- identify enthalpy source;
- identify whether the stream is treated as pure NH3, pure H2O, or NH3-H2O mixture;
- identify any implicit phase-equilibrium assumption.

### B. Species balances

Explicitly formulate:

- NH3 balance around generator;
- H2O balance around generator;
- NH3 balance around absorber;
- H2O balance around absorber;
- solution heat exchanger consistency;
- condenser species balance;
- evaporator species balance;
- total-cycle NH3 and H2O closure.

Identify any missing rectification, dephlegmation, water carryover, or separation assumption.

### C. Energy balances

Audit:

- generator;
- condenser;
- evaporator;
- absorber;
- solution heat exchanger;
- circulation/pump work if applicable;
- total cycle.

The existing 0.00 W closure must be treated as an internal model accounting check until independent consistency is demonstrated.

### D. COP definition

Document exactly:

- numerator;
- denominator;
- whether generator heat includes losses;
- whether solution-pump work is included;
- whether other parasitic energy is included;
- whether solar collector losses are outside the COP boundary;
- how the definition compares with literature COP definitions.

### E. Property-model audit

Trace every NH3-H2O property call.

Verify:

- formulation;
- state range;
- bubble/dew treatment;
- mixture enthalpy;
- phase identification;
- applicability at the intended temperatures and pressures;
- independent validation points;
- uncertainty.

D-007 remains OPEN.

## 5. Architecture decision remains open

OQ-0 must compare, using common metrics:

A. Continuous two-fluid NH3-H2O absorption  
B. Three-fluid NH3-H2O-H2 diffusion absorption refrigeration  
C. Intermittent NH3-H2O absorption  
D. Hybrid only if evidence supports it

Compare:

- cooling capacity;
- daily useful cooling;
- COP using a common boundary;
- generator temperature;
- startup;
- circulation mechanism;
- electrical/parasitic demand;
- condenser and absorber requirements;
- pressure;
- safety burden;
- materials;
- complexity;
- Sudan climate suitability;
- evidence maturity.

Solar Polar is a benchmark for solar-DAR behavior and system integration. Its approximately 0.25–0.26 DAR COP is **not a direct performance comparison** to the current two-fluid COP of 0.424.

## 6. Multi-agent engineering roles

### ChatGPT
Scientific/system reviewer:
- thermodynamics;
- primary literature;
- architecture;
- system integration;
- evidence and release-gate review.

### Claude
Independent engineering critic:
- repository-wide consistency;
- architecture/model review;
- assumptions;
- documentation/governance;
- challenge conclusions.

### Copilot
Implementation auditor:
- source-code implementation;
- tests;
- CAD/BOM/spec consistency;
- reproducibility;
- code-to-engineering-document traceability.

All three provide evidence and criticism. None constitutes fabrication approval.

## 7. Re-planned engineering sequence

### P0 — Critical

1. THERMO-AUDIT-01: species, mass, energy, property, and COP audit.
2. Resolve OQ-0 architecture.
3. Independently benchmark the resulting two-fluid COP against appropriate NH3-H2O literature where applicable.
4. Establish pressure/design-code/material/relief basis.
5. Resolve materials compatibility and joining basis.

### P1 — High

6. Engineer and validate V-102 absorber.
7. Validate E-102 condenser under hot-ambient conditions.
8. Audit generator separation/rectification and water carryover.
9. Build coupled hourly solar/transient model.

### P2 — Engineering reconciliation

10. Reconcile CAD/spec/BOM conflicts.
11. Reconcile P&ID and actual flow paths.
12. Replace disconnected/simple coil geometry with reviewed flow-path geometry.
13. Reconcile drawings, BOM, component specifications, and source code.

### P3 — Release preparation

14. Prototype test plan.
15. Instrumentation plan.
16. Measurement uncertainty.
17. Independent technical review.
18. Final release-gate evidence.

## 8. Known additional findings to track

- No pump or circulation hardware is currently established despite descriptions of mechanical circulation.
- Pump shaft work is omitted from the present model.
- V-102 absorber area is calculated from assumed U and temperature approach rather than demonstrated heat/mass transfer.
- Solution tank sizing uses an implicit 1 kg/L proxy and is not a validated inventory/vessel design.
- Older Solar Polar benchmark wording conflicts with the newer benchmark's corrected COP-comparability statement.
- Repository artifacts contain actionable-looking hydrotest and relief values despite HOLD status; these must not be treated as approved instructions.
- Local BOM edits removing silver-brazing rods are not yet reconciled with the checked-in BOM snapshot.
- Component/CAD conflicts include 40 vs 60 mm port projection and 21 vs 25 mm port bore.
- CPC records contain 3980 vs 4000 mm length and 3 vs 2 mm reflector thickness.
- Existing V-101 5 mm flat end caps remain unresolved and fail the repository's existing UG-34 screening at both candidate pressures.
- Simplified coil geometry does not establish continuous manufacturable tubing.
- Khartoum daily solar screening is preliminary resource evidence, not coupled refrigerator performance.

## 9. Acceptance criteria for THERMO-AUDIT-01

Do not mark the audit complete until:

- every cycle state/stream has a documented composition and property basis;
- NH3 and H2O balances close independently;
- total mass balance closes;
- component energy balances close with a documented boundary;
- generator vapor composition and water carryover are explicitly accounted for;
- any rectification/separation assumption is explicit;
- COP definition is unambiguous and reproducible;
- property methods are independently checked over the intended state range;
- uncertainty/sensitivity is reported;
- all material discrepancies are documented rather than silently corrected;
- independent reviewers can reproduce the audit from the repository.

## 10. Evidence classes

Use these labels throughout the work:

- **VALIDATED** — independently supported by reproducible evidence.
- **MODEL OUTPUT** — produced by the current model but not independently validated.
- **ASSUMPTION** — explicit engineering assumption.
- **PRELIMINARY** — useful evidence that is not sufficient for release.
- **CONFLICT** — incompatible project records.
- **UNVERIFIED** — insufficient evidence.
- **OPEN** — engineering decision not yet resolved.

Do not convert MODEL OUTPUT, PRELIMINARY, ASSUMPTION, CONFLICT, or UNVERIFIED into VALIDATED merely by repetition.

## 11. Current disposition

**HOLD remains unchanged.**

No fabrication, pressure testing, ammonia charging, or operation is authorized by this report.

## 12. Required follow-up from Claude and Copilot

Read this report together with:

1. `docs/ENGINEERING_VALIDATION_CALL.md`
2. `docs/DESIGN_SUMMARY.md`
3. `BUILD_RELEASE_GATE.md`
4. `COMPONENT_SPECS.md`
5. `claude/PROJECT_GRAPH.json`
6. `docs/BENCHMARK-01_SOLAR_POLAR_EXTERNAL_REVIEW.md`
7. `src/thermo/cycle_model.py`
8. relevant CAD/P&ID/BOM implementation

Then report:

- findings confirmed;
- findings rejected, with evidence;
- additional hidden gaps;
- exact source paths;
- proposed validation method;
- dependencies;
- status recommendation.

Do not silently implement a correction. First document the discrepancy and its engineering significance.

## 13. Tracking rule

Every future THERMO-AUDIT-01 update should use:

**ID → finding → evidence → status → owner/agent → next action → acceptance evidence → Git commit**

This report is the shared baseline for ChatGPT, Claude, and Copilot.
