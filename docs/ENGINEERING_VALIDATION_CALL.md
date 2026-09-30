# Call for Independent Engineering Validation

We invite qualified engineers, researchers and technical reviewers worldwide to help independently assess this solar-powered ammonia-water absorption refrigeration design.

**Current status: HOLD. This is not an invitation to fabricate, pressure-test, charge or operate the system.** Repository values are preliminary and contain unresolved conflicts. Participation, discussion, calculations or a merged code change do not constitute design approval or authorization to build.

## Review Areas

- **Pressure systems:** design basis, pressure-boundary calculations, vessel/nozzle design, relief-system basis, code and jurisdiction review.
- **Ammonia refrigeration:** cycle states, mixture-property validity, operating envelope, material and seal compatibility.
- **Thermal engineering:** generator, absorber, condenser, evaporator, solution heat exchanger and solar collector performance.
- **Mechanical design:** geometry, interfaces, piping, supports, tolerances, manufacturability and CAD-to-drawing consistency.
- **Quality and safety:** inspection requirements, material traceability, hazard analysis, test governance and documentation gaps.
- **Model and data validation:** reproducibility, unit handling, independent reference data, uncertainty and CFD limitations.

## How to Contribute

Open a GitHub issue using the **Engineering validation review** form, or submit a focused pull request linked to an issue. For each finding or proposed correction, include as applicable:

- The exact repository file, revision or calculation being reviewed.
- The question, finding or proposed change, with assumptions and units.
- Primary references, including edition/date and relevant section or clause where available.
- A reproducible calculation, script, test case or evidence trail; distinguish measured results from estimates and model outputs.
- The applicable code jurisdiction and limits of the review.
- Conflicts of interest or relevant vendor relationships, if any.

Reviewers may identify an issue without proposing a replacement value. Do not guess missing dimensions or select pressure/test limits from incomplete data. Do not post private, export-controlled, employer-confidential or personal information.

## Review and Acceptance

Issues and pull requests are evidence for the project review process, not approval. Engineering decisions that affect pressure containment, ammonia safety, materials, test limits or operating conditions must be resolved and documented by appropriately qualified responsible professionals for the intended jurisdiction and site. The release disposition remains **HOLD** until every applicable gate in [Build Release Gate](BUILD_RELEASE_GATE.md) is closed and signed through controlled project document review.

## Safety Boundary

Do not use repository drawings, scripts, comments, model outputs or this call as work instructions. Do not fabricate, pressurize, ammonia-charge or operate equipment based on this repository. See the [Build Release Gate](BUILD_RELEASE_GATE.md).