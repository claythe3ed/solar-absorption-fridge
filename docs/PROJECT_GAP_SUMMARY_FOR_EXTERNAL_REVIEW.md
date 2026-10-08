# Solar Absorption Refrigerator — Open-Gap Summary for External Review

**Prepared:** 2026-10-05
**Repository:** <https://github.com/claythe3ed/solar-absorption-fridge>
**Disposition:** **HOLD — not approved for fabrication, pressure testing,
ammonia charging, or operation.**

## Purpose and gap count

This document is a concise, source-linked brief for requesting independent
technical feedback. It separates the project's **formal register count** from
the larger set of individual missing data and calculations:

- **13 open Design Basis items:** DB-01 through DB-13.
- **7 open Decision Register items:** D-001 through D-007.
- **20 numbered register entries in total**, before overlap is consolidated.
- The Build Release Gate separately lists **16 broad evidence categories**.
  These overlap with the DB/D entries and **must not be added as 16 more
  independent gaps**.

Therefore, **20 is the formal count of numbered open entries, not a count of
every missing measurement, calculation, drawing, certificate, approval, or
subtask**. Some entries overlap (for example, design pressure appears in both
DB-05 and D-001 and the release gate). A fully deduplicated count of atomic
engineering tasks has not yet been made.

These are repository-recorded gaps, not an independent engineering audit.
An external comment, social-media response, AI answer, or apparent lack of
objection does not close any item or constitute engineering approval.

## Project snapshot

The project is a preliminary solar-heated ammonia-water absorption refrigerator
for off-grid cooling in Sudan. The tracked specification describes a nominal
200 W cooling target and a 150 L cold box. The current steady-state model gives
approximately 0.424 COP at its selected inputs, but that is an unvalidated
model result, not demonstrated product performance.

The model's nominal inputs include evaporator −15 °C, condenser 40 °C,
generator 135 °C, absorber 30 °C, rich/poor solution ammonia mass fractions
0.40/0.25, and 200 W cooling. The pressure basis is unresolved: one artifact
states 25 bar and another 16 bar; the cycle model gives about 15.55 bar
absolute at its nominal condenser condition. **None of these is a signed,
approved design basis.**

## Formal Design Basis gaps (13)

All DB items are marked **OPEN** in the local draft `docs/DESIGN_BASIS.md`.

| ID | Open item | Needed to close |
|---|---|---|
| DB-01 | Governing code and jurisdiction | Identify the authority having jurisdiction and approved pressure-system/refrigeration code basis. |
| DB-02 | Site maximum/minimum ambient conditions | Approve a verified site design envelope, not only a gridded historical series. |
| DB-03 | Maximum generator temperature | Establish normal and credible upset temperatures, controls, and thermal limits. |
| DB-04 | Maximum high-side operating pressure | Independently validate the cycle across the operating and upset envelope. |
| DB-05 | High-side design pressure | Resolve the 16/25 bar conflict and establish a signed code-based basis. |
| DB-06 | Design temperature range | Establish minimum, normal, maximum, and upset metal/process temperatures. |
| DB-07 | Permitted wetted materials | Approve materials for ammonia-water composition, contaminants, stress, temperature, and joining method. |
| DB-08 | Prohibited wetted materials | Verify and control copper, brass, zinc/galvanizing, and any other exclusions. |
| DB-09 | Relief-device basis | Define scenarios, required capacity, device selection, discharge destination, and backpressure basis. |
| DB-10 | Inspection and acceptance criteria | Approve applicable code, inspection scope, acceptance criteria, and inspection authority. |
| DB-11 | Pressure/leak test basis | Approve a code-compliant test plan, limits, safeguards, and records; draft values are not instructions. |
| DB-12 | Solar resource and collector design envelope | Approve site resource, weather conditions, collector assumptions, and structural/thermal loads. |
| DB-13 | Cooling load and performance criteria | Verify the application load profile, required product/cabinet temperatures, and acceptance method. |

## Formal Decision Register conflicts/gaps (7)

All D items are marked **OPEN** in the local draft `docs/DECISION_REGISTER.md`.

| ID | Open decision | Conflict / missing evidence |
|---|---|---|
| D-001 | V-101 high-side design pressure | 25 bar in component specification versus 16 bar in BOM; operating/upset envelope and code basis not approved. |
| D-002 | V-101 port projection | 40 mm in component specification versus 60 mm in drawing/CAD artifacts. |
| D-003 | CPC length | 3980 mm in component specification versus 4000 mm in BOM. |
| D-004 | Reflector thickness | 3 mm in component specification versus 2 mm in BOM; material and structural basis unresolved. |
| D-005 | Silver-brazing consumable | BOM language describes copper-steel brazing despite copper prohibition; register says removed pending review, while artifact consistency and joint scope require reconciliation. |
| D-006 | Relief/check-valve quantities | Component specification lists one of each; BOM lists two; location, capacity, and device basis unresolved. |
| D-007 | Thermodynamic mixture validation | Saved teqp comparison failed to converge at all 12 points; no independent comparison against traceable mixture measurements is recorded. |

## Consolidated work areas

The following groups summarize the release-gate evidence. They are **not extra
numbered gaps** on top of DB-01–DB-13 and D-001–D-007.

### 1. Pressure boundary, vessels, and piping

- Reconcile design pressure, design temperatures, material grades, and
  applicable code/jurisdiction.
- Produce reviewed code calculations for shell, heads/caps, nozzles, welds,
  tanks, and all pressure-retaining components. Current stated wall/head,
  burst, and test claims are not a released calculation package.
- Reconcile port projection and opening dimensions between specification,
  CAD, drawings, and BOM.
- Complete vessel geometry, head/nozzle details, supports, piping isometrics,
  line list, and connection schedule.
- Define an approved fabrication, inspection, nonconformance, and test plan.
  Values in preliminary repository material are not instructions to pressurize
  or test equipment.

### 2. Overpressure protection and process safety

- Identify and document credible overpressure scenarios for the actual
  ammonia-water system and solar input.
- Calculate required relief capacity and select devices against the approved
  design basis; review inlet losses, discharge piping, backpressure, and
  disposal/absorption destination.
- Reconcile valve quantities, locations, set pressure, and discharge routing.
- Complete site-specific ammonia hazard analysis, leak detection/ventilation,
  emergency response, operating, and maintenance plans.

### 3. Materials and chemical compatibility

- Establish a tag-by-tag wetted-material list, including piping, fittings,
  valve internals, relief trim, instruments, weld metal, brazes, coatings,
  plating, seals, lubricants, and charging connections.
- Exact installed heats/lots, mill test reports, actual grades, and component
  manufacturer wetted-material declarations are absent or unspecified in the
  project records. “Carbon steel” and “stainless” are not sufficient
  material identities.
- Resolve the A106 Grade B, A516 Grade 70, unspecified carbon steel, proposed
  304/316 stainless, ER70S-6 filler, silver-brazing, PTFE, and “Viton”
  compound questions against the exact service and controlled sources.
- Evaluate actual ammonia phase/composition, water/oil/oxygen/chloride
  contamination, temperatures, pressures, cyclic stress, stagnant/wet
  conditions, and relevant corrosion or cracking mechanisms.
- Obtain code allowables at design temperature and traceable temperature-
  dependent thermal properties for actual alloys before using them in
  pressure or transient thermal calculations.
- NIOSH identifies copper and galvanized surfaces as incompatible/corroded by
  ammonia. That is a warning, **not** qualification of the other alloys or
  a complete compatibility matrix.

### 4. Thermodynamic and cycle-model validation

- The nominal cycle solver is steady-state and uses a simplified Ziegler–Trepp
  mixture-property implementation plus pure-fluid CoolProp calls.
- Internal energy balance closure and input checks do not validate mixture
  properties, cycle architecture, or hardware performance.
- The ammonia-water mixture comparison to teqp did not converge; an independent
  validation against traceable measurements and uncertainty is still required.
- Verify the IAPWS ammonia-water implementation against published check points,
  units, composition conventions, and range-of-validity limits before treating
  it as an independent model.
- The selected 135 °C generator condition is above pure-ammonia critical
  temperature. This does not determine the mixture critical point, but it
  makes validation and property-method applicability at generator conditions
  especially important.
- Resolve the intermittent batch versus continuous pumped versus other
  architecture, component interfaces, solution circulation, rectification/
  dephlegmation needs, and operating/control sequence.

### 5. Collector, heat exchangers, and performance

- The CPC size is an algebraic estimate using assumed irradiance and
  efficiencies; it is not an optical/thermal or hourly collector simulation.
- Collector profile, materials, support/wind loads, orientation, incidence-angle
  response, shading, receiver/cover properties, and thermal losses need a
  controlled design and validation.
- Condenser/evaporator geometry and exchanger UA/heat rejection are incomplete;
  a single-cylinder CFD study is not prototype performance validation.
- Reconcile manufacturable exchanger geometry, headers, connections, fins,
  lengths, and cut lists.
- Verify the 200 W load from a cabinet/application heat balance and define
  operating/product-temperature service criteria.
- Cold-side storage capacity, losses, charge power, temperature range, and
  required service duration are not specified/validated.

### 6. Khartoum climate/resource and simulation readiness

- NASA POWER data have been used in a **local, preliminary daily solar-energy
  screen** only. It is not a coupled full refrigerator simulation or
  station-validated site design weather basis.
- A local hourly NASA POWER file was obtained, but the hourly cycle + storage
  simulation was not completed. There are no verified results for service
  fraction, storage sizing, runtime, or unmet load.
- A quick probe found the current cycle solver rejects some higher sink
  temperatures at fixed generator conditions. This is a model guard outcome,
  not a confirmed hardware shutdown threshold.
- Hourly operation requires validated heat rejection, collector thermal
  performance, cycle controls/transients, storage physics, load profile, and
  data uncertainty—not simply applying a steady COP to weather.
- Sudan-wide data readiness also has unresolved source-quality, station
  comparison, boundary/settlement validation, and ERA5-Land coverage issues.

### 7. Structural/CAD, quality, and release controls

- Approve CPC/frame dimensions, materials, joints, anchors, wind loads, and
  structural calculations.
- Reconcile CAD, drawings, BOM, materials, and released specifications under
  revision/document control.
- Complete qualified welding procedures and personnel qualifications,
  material traceability, inspection plan, test records, safety review, and
  final sign-offs.
- Independent reviewers and the authority having jurisdiction must approve
  the controlled package before any release. Project status remains HOLD.

## GitHub sources and availability

**Verified public on GitHub at the time this document was prepared:**

- [Repository README](https://github.com/claythe3ed/solar-absorption-fridge/blob/main/README.md)
- [Build Release Gate](https://github.com/claythe3ed/solar-absorption-fridge/blob/main/docs/BUILD_RELEASE_GATE.md)
- [Component Specifications](https://github.com/claythe3ed/solar-absorption-fridge/blob/main/docs/COMPONENT_SPECS.md)
- [Canonical project graph (published commit 29e19f2)](https://github.com/claythe3ed/solar-absorption-fridge/blob/29e19f2/claude/PROJECT_GRAPH.json)
- [Cycle model](https://github.com/claythe3ed/solar-absorption-fridge/blob/main/src/thermo/cycle_model.py)
- [Validation issue template](https://github.com/claythe3ed/solar-absorption-fridge/tree/main/.github/ISSUE_TEMPLATE)

**Local-only drafts/reports as checked 2026-10-05 (not yet linkable as public
GitHub source):**

- `docs/DESIGN_BASIS.md`
- `docs/DECISION_REGISTER.md`
- `docs/AMMONIA_AND_MATERIAL_PROPERTY_REGISTER.md`
- `docs/KHARTOUM_SCREENING.md`
- `scripts/simulation/khartoum_screening.py`
- Local NASA POWER source data under ignored `data/raw/`

Those links should be updated only after the relevant files are reviewed and
actually committed/pushed. Do not cite a guessed `main` URL as though a local
draft were already public. The public GitHub version may not include the
latest local edits.

## Independent-review request

The project owner would like ChatGPT's help preparing a neutral request for
technical opinions from Reddit and LinkedIn. Any post should:

1. Ask for **specific, evidence-based critique** of the open design questions,
   not a general endorsement or fabrication instruction.
2. State the HOLD status prominently and clarify that preliminary pressures,
   temperatures, materials, drawings, and model outputs are not approved.
3. Ask responders to identify relevant experience/qualification and cite
   accessible, authoritative sources (standards clauses by reference, journal
   papers, agency/supplier technical documents); request edition/date and
   applicability.
4. Ask for red flags, missing inputs, and validation methods—especially for
   ammonia-water thermodynamics, actual wetted-material compatibility,
   pressure-vessel/relief basis, and Khartoum hot-weather heat rejection.
5. Explicitly distinguish professional engineering review from Reddit or
   LinkedIn comments. Do not treat social consensus or AI output as approval.
6. Avoid posting copyrighted book/standard scans or large verbatim excerpts.
   Share only public repository links and brief factual summaries.
7. Avoid publishing personal contact details, credentials, private files,
   access tokens, or unreviewed raw datasets.

### Copy-ready instruction for ChatGPT

> Help me prepare a neutral technical-review package for this preliminary
> solar ammonia-water refrigerator project. Start by reading the public
> repository sources linked in the gap summary and clearly distinguish what
> is public from what is described only as local draft material. Do not assume
> local drafts are on GitHub. Summarize the open questions without inventing
> answers or turning preliminary values into approved inputs. Draft separate,
> concise Reddit and LinkedIn posts asking qualified people for evidence-based
> critique, with the project HOLD status prominent. Ask reviewers to state
> relevant experience, cite authoritative sources with editions/dates, point
> out missing data and validation approaches, and refrain from giving
> build/pressure-test/ammonia-charging instructions. Do not reproduce
> copyrighted standards or claim that social-media feedback is engineering
> approval. Before finalizing, identify any statements in the draft that are
> unsupported by the linked public sources.

## Current boundary

This document organizes gaps; it does not close them. No number of online
opinions replaces certificates, calculations, test data, licensed/qualified
review, or jurisdictional approval. Do not fabricate, pressure-test, charge,
or operate the system based on the repository or social-media feedback.
