# Solar Polar / Imperial Benchmark Report
## External engineering benchmark for the solar-powered NH3-H2O absorption refrigerator

**Project:** `claythe3ed/solar-absorption-fridge`  
**Benchmark ID:** BENCHMARK-01  
**Status:** INFORMATIONAL / VALIDATION INPUT — NOT DESIGN APPROVAL  
**Project release status:** **HOLD**

> **Safety boundary:** This report is an engineering-review artifact. It is not a fabrication, pressure-test, ammonia-charging, commissioning, or operating procedure. No value from this benchmark should silently become an approved design input.

---

## 1. Executive conclusion

Solar Polar and the Imperial College London research programme provide one of the strongest external benchmarks currently identified for the project's problem class: small-scale, solar-thermal, ammonia-based refrigeration for warm/off-grid applications.

The benchmark is valuable precisely because it does **not** simply validate the proposed refrigerator. The published work demonstrates experimentally that ammonia-water-hydrogen diffusion-absorption refrigeration (DAR) can provide useful cooling at roughly the relevant scale, while also exposing system-level limitations involving:

- bubble-pump activation and startup;
- high generator temperatures under some operating conditions;
- condenser/ambient heat rejection;
- off-design and part-load performance;
- coupling between charge pressure, generator heat input and heat rejection;
- transient solar operation;
- relatively modest experimentally demonstrated COP.

The proposed project is **not the same cycle**. The current design is an NH3-H2O continuous absorption system with a high-side/low-side pressure difference and, as presently documented, mechanical circulation. Solar Polar's benchmark is an NH3-H2O-H2 diffusion-absorption system using a thermally driven bubble pump and essentially single-pressure operation.

Therefore:

> **Solar Polar is a benchmark, not a design template and not a validation of the Clay cycle.**

The correct project response is to preserve the current architecture as a live candidate while making the architecture choice explicit and evidence-based.

---

## 2. Current project baseline being benchmarked

The current public design summary identifies:

| Parameter | Current Clay design |
|---|---:|
| Cycle | NH3-H2O continuous absorption |
| Cooling capacity | 200 W |
| Evaporator | -15 °C |
| Condenser | 40 °C |
| Generator | 135 °C |
| Absorber | 30 °C |
| COP | 0.424 |
| Solution circulation ratio | 4.37 |
| High-side pressure | 15.55 bar |
| Low-side pressure | 2.36 bar |
| Pressure ratio | 6.58 |
| Refrigerant flow | 0.68 kg/h NH3 |
| Rich solution | 2.99 kg/h, x_NH3 = 0.40 |
| Poor solution | 2.30 kg/h, x_NH3 = 0.25 |
| Generator vapour | y_NH3 = 0.906 |
| CPC aperture | 1.59 m² |
| CPC aperture width | 400 mm |
| CPC receiver | 200 mm OD × 4 m |
| Condenser rejection | 274.8 W |
| Condenser tube | 15 mm OD, 7.5 m |
| Absorber rejection | 396.7 W |
| Absorber area | 3.97 m² |

These values are **current project values, not independently approved design values**. The repository's engineering validation call explicitly states that repository values are preliminary, contain unresolved conflicts, and must not be used as work instructions. The project remains on HOLD.

---

## 3. What Solar Polar actually benchmarks

### 3.1 Architecture

The Solar Polar / Imperial system is a diffusion-absorption refrigerator using:

- ammonia as refrigerant;
- water as absorbent;
- hydrogen as inert gas;
- a thermally activated bubble pump for circulation;
- generator;
- rectifier;
- condenser;
- evaporator;
- absorber;
- reservoir;
- solar-thermal heat input.

The third fluid is fundamental to the DAR architecture. Hydrogen reduces the ammonia partial pressure in the evaporator and participates in gas circulation; it is not simply an additive to a conventional two-fluid NH3-H2O cycle.

**Implication:** adding hydrogen to the current project would constitute an architecture change, not a minor modification.

### 3.2 Experimental scale

The 2019 peer-reviewed study evaluated a nominal 100 W ammonia-water-hydrogen DAR unit specifically aimed at solar-cooling applications in warm climates. Generator heat input was varied from 150–700 W, producing measured generator temperatures of 175–215 °C. Measured steady-state cooling output was 24–108 W and measured COP was 0.11–0.26, with maximum COP at approximately 300 W generator heat input.

Source: Najjaran, Freeman, Ramos & Markides, *Applied Energy* 256 (2019), 113899, DOI 10.1016/j.apenergy.2019.113899.

### 3.3 2024 calibrated solar-DAR model

Freeman & Markides, *Renewable Energy* 230 (2024), 120718, developed a semi-empirical model including both steady-state and startup behaviour and calibrated it against experimental data.

Key reported results:

- maximum steady-state COP approximately 0.25 at 14 bar;
- at 100 W heat input, bubble-pump activation could take up to 2 hours or longer;
- before bubble-pump activation, no cooling was produced;
- experimentally calibrated model predicted steady-state COP within approximately ±20%;
- peak startup heat-source temperature was predicted within approximately ±10 K.

Source: DOI 10.1016/j.renene.2024.120718.

### 3.4 2024 solar-system simulation

Freeman & Markides, *Renewable Energy* 230 (2024), 120717, applied the calibrated model to variable solar operation for Ahmedabad, India.

Reported results include:

- nominal system around 70 W cooling;
- 1.5 m² collector area identified as appropriate for the nominal case;
- optimum charge pressure around 16 bar for the simulated October Ahmedabad conditions;
- predicted daily cooling output of 170 kJ/day in the nominal configuration;
- daily operating period below 5 hours because of the time required to reach the required collector temperature for bubble-pump activation;
- predicted overall solar-to-cooling efficiency below 1% for the studied configuration.

Source: DOI 10.1016/j.renene.2024.120717.

These are **Ahmedabad model results**, not Khartoum measurements and not direct predictions for the Clay refrigerator.

---

## 4. The most important architectural distinction

### Clay candidate

**NH3-H2O**

Two-fluid absorption cycle with a pressure difference between low and high sides and current project assumptions involving continuous circulation.

### Solar Polar benchmark

**NH3-H2O-H2**

Three-fluid diffusion-absorption cycle using hydrogen and a thermally driven bubble pump.

### Consequence

Solar Polar's bubble-pump startup limitation cannot simply be transferred to the Clay cycle.

Conversely, the Clay cycle cannot claim DAR's passive operation, because a mechanically circulated two-fluid system has different auxiliary-power, control, reliability and safety implications.

This distinction must remain explicit in all future documentation.

---

## 5. COP benchmark

The most useful numerical warning is the difference between the current modelled Clay COP and experimental DAR evidence.

### Clay

COP = **0.424**

At 200 W cooling, this corresponds to approximately:

**Q_gen ≈ 200 / 0.424 ≈ 472 W**

before considering any additional electrical/parasitic accounting that may or may not be included in the project COP definition.

### Solar Polar / Imperial DAR

Peer-reviewed 2019 experimental work:

- COP range: **0.11–0.26**
- maximum: approximately **0.26**

2024 calibrated solar-DAR model:

- maximum steady-state COP: approximately **0.25** at 14 bar.

Therefore the Clay modelled COP is approximately 1.63–1.70 times the 0.25–0.26 DAR experimental range.

This is **not evidence that COP = 0.424 is wrong**.

It is evidence that the model deserves an aggressive independent cross-check.

Questions to answer:

1. Is the Clay COP defined on the same heat-input boundary as the benchmark?
2. Is generator heat the complete thermal input?
3. Is pump electrical work excluded?
4. Are heat losses excluded?
5. Are solution heat-exchanger assumptions comparable?
6. Are the concentration and vapour-quality assumptions independently defensible?
7. Is rectification/water carryover treated consistently?
8. Are all state properties calculated with a validated NH3-H2O mixture model?
9. Is absorber and generator heat balance independently closed?
10. Does the model remain credible under off-design conditions?

**Required action:** create an independent COP reconciliation before treating 0.424 as a mature design result.

---

## 6. Generator temperature: 135 °C needs architecture-specific justification

Solar Polar/DAR evidence includes generator temperatures around 175–215 °C in the 2019 experiment and difficult startup behaviour in the 2024 work.

However:

> This does not establish that an NH3-H2O mechanically circulated system requires 175–215 °C.

DAR needs sufficient heat/temperature to activate its bubble pump. The Clay architecture does not use that same circulation mechanism.

Therefore the correct question is:

> Can the complete proposed NH3-H2O cycle produce 200 W at -15 °C evaporator, 40 °C condenser, 30 °C absorber and 135 °C generator, at the stated concentrations, circulation ratio, heat-exchanger effectiveness and pressure levels, while satisfying material, pressure and stability constraints?

That question should be answered by the Clay model and independent thermodynamic validation, not by copying DAR temperature requirements.

---

## 7. Pressure benchmark

Solar Polar/Imperial work provides a useful external range:

- 2019 experimental unit: default charge pressure 22 bar;
- 2024 Part I: maximum steady-state COP reported at 14 bar;
- 2024 Part II: approximately 16 bar identified as optimum for the simulated Ahmedabad case.

The current Clay high-side pressure is:

**15.55 bar**

This numerical proximity is interesting but is **not validation**.

In particular:

- DAR charge pressure is not automatically equivalent to Clay high-side operating pressure;
- design pressure is not operating pressure;
- Solar Polar's pressure optimization cannot select the Clay vessel design pressure;
- hot-ambient condensation requirements can push pressure requirements in a different direction.

Therefore Solar Polar strengthens DB-04 (operating-pressure context) but does not close DB-05 (design pressure), D-001 (16 vs 25 bar conflict), or DB-09 (relief basis).

---

## 8. Heat rejection is now a high-priority validation area

Solar Polar's research makes the condenser/ambient coupling especially important.

A solar absorption refrigerator cannot be evaluated only by asking whether enough solar heat reaches the generator.

The system is coupled:

**solar collector → generator → cycle pressure → condenser → ambient heat rejection**

and also:

**absorber → ambient heat rejection → solution concentration/circulation → generator duty**

The 2019 Solar Polar-related experimental unit deliberately used larger condenser and absorber areas to promote heat rejection.

This directly supports aggressive validation of:

- E-102 condenser;
- V-102 absorber;
- their performance at high ambient temperature;
- the assumed U-values;
- natural-convection assumptions;
- hot-day operating envelope.

### Clay condenser

Current design basis:

- rejection: 274.8 W;
- 15 mm OD tube;
- 7.5 m total;
- natural convection;
- U = 15 W/m²K.

This is not obviously impossible, but the Solar Polar benchmark demonstrates why a generic U-value is insufficient evidence.

### Existing CFD limitation

The project's current CFD result of approximately 21.23 W/m²K should remain classified as preliminary.

The current extraction method is not yet a direct wall-heat-flux integration and the pressure variable did not fully converge. Therefore:

> **Do not describe current CFD as condenser validation.**

Recommended next CFD evidence:

1. fully converged thermal/flow solution;
2. direct wall heat-flux integration;
3. area-weighted heat-transfer coefficient;
4. explicit ambient boundary conditions;
5. sensitivity to ambient temperature and wind/natural-convection regime;
6. mesh and timestep/iteration independence as applicable;
7. comparison against analytical correlations or experimental data.

---

## 9. Absorber implications

The Solar Polar absorber performs coupled mass and heat transfer in a gas-liquid system. It is not merely a finned vessel.

The current Clay V-102 concept has:

- integrated physical relationship with V-101;
- approximately 3.97 m² total surface;
- approximately 1.5 m² added fin area;
- approximately 396.7 W absorber heat rejection target.

The Solar Polar benchmark does **not** validate this geometry.

Instead it raises a design question:

> Is the proposed V-102 architecture sufficient to achieve the required NH3 absorption rate and heat rejection simultaneously at the proposed concentration, pressure and absorber temperature?

This strengthens the need to resolve the absorber architecture and mass-transfer model.

---

## 10. Startup and daily-energy implications

A steady-state COP is not enough for solar refrigeration.

The 2024 Solar-DAR work explicitly models startup because the system can spend a significant portion of the solar day reaching the conditions needed for operation.

The Ahmedabad simulation predicted:

- less than 5 h/day operating period in the studied configuration;
- below 1% overall solar-to-cooling efficiency.

This does **not** mean the Clay system will behave the same way.

The Clay cycle may avoid the DAR bubble-pump activation bottleneck.

But it establishes a broader requirement:

> The Clay project needs a dynamic solar-to-cooling analysis, not only a steady-state thermodynamic cycle calculation.

For the Sudan application, that analysis should eventually include:

- hourly solar resource;
- collector thermal efficiency;
- generator heat requirement;
- cycle startup;
- thermal inertia;
- condenser/absorber ambient limits;
- cooling-load profile;
- storage strategy if any;
- daily useful cooling;
- seasonal sensitivity.

Current NASA POWER daily screening is not sufficient to close this requirement.

---

## 11. Collector benchmark

The Solar Polar programme also demonstrates that collector/cycle integration matters.

The 2024 work used evacuated-tube collectors and explicitly coupled collector temperature to DAR startup.

The Clay project uses a CPC:

- 400 mm aperture;
- 1.59 m² aperture area;
- 4 m receiver;
- 30° acceptance half-angle;
- nominal concentration ratio 2.0;
- East-West horizontal orientation.

The appropriate comparison is not simply collector temperature.

The relevant metric is:

> **Useful generator heat delivered at the required generator temperature over the actual Sudan solar resource, including optical and thermal losses.**

A future collector benchmark should compare at least:

- useful thermal power;
- outlet/receiver temperature;
- optical efficiency;
- thermal loss;
- stagnation behaviour;
- daily useful heat;
- manufacturing complexity;
- dust sensitivity;
- maintenance;
- cost;
- local manufacturability.

Do not copy Solar Polar collector geometry into the Clay design.

---

## 12. Thermal storage

Solar Polar's historical patent literature contains thermal-storage concepts associated with its architecture.

These should be treated as evidence that thermal storage was considered as a system-level solution, **not** as approved Clay design inputs.

Do not copy a patent's PCM material, temperature or geometry into the Clay design without an independent engineering basis.

The correct Clay research question is:

> Would thermal storage materially improve daily useful cooling, startup reliability or overnight cooling enough to justify its mass, thermal losses, cost, pressure/interface complexity and safety implications?

---

## 13. Materials and safety

Solar Polar does not resolve the Clay project's materials and pressure-safety gaps.

It does not close:

- DB-01 governing code/jurisdiction;
- DB-07 permitted wetted materials;
- DB-08 prohibited wetted materials;
- DB-09 relief-device basis;
- DB-10 inspection/acceptance;
- DB-11 pressure/leak test basis;
- D-005 brazing/material conflict;
- D-006 relief/check valve quantity.

The benchmark should therefore **not** be used to justify any material choice, pressure-vessel thickness, valve count, relief setting or test pressure.

Those remain controlled engineering decisions requiring appropriate code/jurisdiction review and qualified responsibility.

---

## 14. Formal gap impact

The formal tracker remains:

**13 Design Basis items + 7 Decision Register items = 20 numbered entries.**

Solar Polar changes the evidence state as follows:

| Gap | Status after benchmark | Interpretation |
|---|---|---|
| DB-01 | OPEN | Governing code/jurisdiction unresolved |
| DB-02 | BETTER INFORMED | Hot-climate heat rejection risk strengthened |
| DB-03 | BETTER INFORMED | External generator-temperature evidence exists, but not direct Clay validation |
| DB-04 | BETTER INFORMED | 14–22 bar DAR evidence gives context |
| DB-05 | OPEN | Vessel design pressure remains unresolved |
| DB-06 | BETTER INFORMED | Wider thermal/startup evidence available |
| DB-07 | OPEN | Materials unresolved |
| DB-08 | OPEN | Prohibited materials unresolved |
| DB-09 | OPEN | Relief basis unresolved |
| DB-10 | OPEN | Inspection/acceptance unresolved |
| DB-11 | OPEN | Pressure/leak test basis unresolved |
| DB-12 | BETTER INFORMED | Solar-thermal collector benchmark strengthened |
| DB-13 | BETTER INFORMED | External small-scale cooling benchmark strengthened |
| D-001 | OPEN | 16 vs 25 bar conflict remains |
| D-002 | OPEN | 40 vs 60 mm port conflict unaffected |
| D-003 | OPEN | 3980 vs 4000 mm CPC conflict unaffected |
| D-004 | OPEN | 3 vs 2 mm reflector conflict unaffected |
| D-005 | OPEN | Silver-brazing/material conflict remains |
| D-006 | OPEN | Valve quantity conflict remains |
| D-007 | BETTER INFORMED / NOT CLOSED | External DAR evidence strengthens validation context but does not validate the Clay NH3-H2O mixture model |

### Numerical status

**0 / 20 formal gaps closed.**

Approximately **7 / 20 materially better informed**:

- DB-02
- DB-03
- DB-04
- DB-06
- DB-12
- DB-13
- D-007

The formal count must not be reduced merely because the external evidence is strong.

---

## 15. Architecture decision that should now be formalized

Create/maintain:

### OQ-0 — Cycle Architecture Selection

At minimum compare:

**A. Continuous two-fluid NH3-H2O**
- current Clay direction;
- mechanical circulation;
- pressure-separated cycle;
- potentially lower heat-source-temperature requirement than DAR;
- introduces pump/electrical/mechanical dependencies.

**B. Three-fluid NH3-H2O-H2 DAR**
- Solar Polar benchmark;
- thermally driven bubble pump;
- no conventional compressor/pump;
- experimental evidence exists;
- startup and heat-rejection limitations are significant.

**C. Intermittent/batch NH3-H2O**
- potentially lower mechanical complexity;
- requires explicit duty-cycle and thermal-storage analysis;
- must be evaluated against required daily cooling.

**D. Hybrid**
- only if a specific evidence-based architecture emerges;
- no hybridization should be assumed merely because individual technologies are attractive.

### Decision rule

Do not select an architecture based on:

- marketing;
- one COP value;
- one patent;
- one Reddit comment;
- nominal collector temperature;
- steady-state calculations alone.

Select it after comparing:

1. daily useful cooling;
2. startup behaviour;
3. COP under consistent boundaries;
4. heat-source temperature;
5. condenser/absorber performance;
6. climate sensitivity;
7. electrical demand;
8. pressure/safety burden;
9. materials compatibility;
10. manufacturability;
11. maintainability;
12. evidence maturity.

---

## 16. Required Solar Polar benchmark simulation

A formal simulation study should be added rather than treating the literature as a narrative comparison.

### SP-01 — Literature-consistent DAR reference case

Reconstruct, as far as the published data permit:

- NH3-H2O-H2;
- representative charge pressures such as 14, 16, 21/22 bar;
- published ammonia concentration assumptions where applicable;
- generator heat input;
- startup behaviour;
- condenser/ambient conditions;
- published DAR correlations/assumptions;
- steady-state COP;
- dynamic daily cooling.

The reconstruction must clearly label:

- measured input;
- measured output;
- fitted/modelled quantity;
- assumption;
- unavailable parameter.

### CLAY-01 — Current cycle

Evaluate:

- 15.55 bar high side;
- 2.36 bar low side;
- -15 °C evaporator;
- 40 °C condenser;
- 30 °C absorber;
- 135 °C generator;
- 200 W cooling;
- COP 0.424.

### Comparison metrics

At minimum:

| Metric | SP-01 | CLAY-01 |
|---|---|---|
| Cycle architecture | | |
| Working fluids | | |
| Circulation mechanism | | |
| Operating pressure | | |
| Generator temperature | | |
| Startup time | | |
| Steady-state COP | | |
| Daily cooling | | |
| Solar heat required | | |
| Condenser rejection | | |
| Absorber rejection | | |
| Evaporator temperature | | |
| Collector area | | |
| Collector operating temperature | | |
| Electrical input | | |
| Fluid inventory | | |
| Materials basis | | |
| Pressure-safety burden | | |
| Climate sensitivity | | |
| Evidence class | | |

The comparison should never imply that different cycle definitions are directly equivalent without harmonizing system boundaries.

---

## 17. Validation priorities produced by this benchmark

### Priority 1 — Independent thermodynamic audit

Attack COP = 0.424.

Recalculate the complete NH3-H2O cycle independently and document:

- property method;
- state equations;
- mass balances;
- energy balances;
- solution concentrations;
- vapour composition;
- heat exchanger assumptions;
- pump work;
- heat losses;
- COP boundary.

### Priority 2 — Generator feasibility

Demonstrate, by validated NH3-H2O thermodynamics, that 135 °C is sufficient for the complete proposed cycle.

Do not use DAR temperature data as proof either way.

### Priority 3 — Hot-climate condenser

Validate E-102 at realistic Sudan ambient conditions.

The required evidence should include direct heat-transfer calculation/measurement or validated correlations, not a generic U-value alone.

### Priority 4 — Absorber

Resolve V-102's actual absorption/mass-transfer architecture.

A finned surface-area number alone is not a sufficient absorption validation.

### Priority 5 — Dynamic solar simulation

Move from daily solar screening to hourly system simulation.

### Priority 6 — Architecture comparison

Complete OQ-0 using SP-01 vs CLAY-01 vs intermittent NH3-H2O.

---

## 18. What this benchmark does NOT establish

Solar Polar does **not** establish that:

- the Clay cycle is valid;
- COP = 0.424 is correct;
- 135 °C is sufficient for the Clay cycle;
- 15.55 bar is the correct Clay operating pressure;
- 16 bar or 25 bar is the correct Clay design pressure;
- the V-101 vessel geometry is safe;
- the V-102 absorber is adequate;
- E-102 is adequate;
- the CPC is adequate;
- any material is ammonia-compatible;
- any relief setting is correct;
- any pressure-test value is correct;
- the system is ready for fabrication;
- the system is ready for ammonia charging;
- the system is ready for operation.

---

## 19. Evidence hierarchy

### Tier 1 — peer-reviewed experimental evidence

**Najjaran, Freeman, Ramos & Markides (2019)**  
“Experimental investigation of an ammonia-water-hydrogen diffusion absorption refrigerator.”  
*Applied Energy*, 256, 113899. DOI: 10.1016/j.apenergy.2019.113899.

Primary evidence for measured DAR cooling/COP and heat-source conditions.

### Tier 1 — experimentally calibrated dynamic model

**Freeman & Markides (2024), Part I**  
*Renewable Energy*, 230, 120718.  
DOI: 10.1016/j.renene.2024.120718.

Primary evidence for calibrated steady-state and startup modelling.

### Tier 1 — solar-system simulation

**Freeman & Markides (2024), Part II**  
*Renewable Energy*, 230, 120717.  
DOI: 10.1016/j.renene.2024.120717.

Primary evidence for variable-solar operation, collector area/pressure tradeoffs and daily performance of the studied DAR system.

### Tier 2 — earlier Solar Polar/Imperial demonstration work

2017 Solar Polar/Imperial/ISES work provides useful system-level experimental context and a documented field-demonstration lineage.

### Tier 2 — patents

Solar Polar patent families are useful for architecture/history/design intent, but patent embodiments are not independent performance validation.

### Tier 3 — government/project case studies

UKRI / Energy Catalyst material supports the existence of funded development and field-demonstration activity, but should not be treated as a substitute for peer-reviewed performance data.

### Tier 4 — company marketing

Useful for current product positioning and architecture descriptions, but not sufficient as independent experimental evidence.

---

## 20. Recommended repository disposition

**Recommended status: add BENCHMARK-01 as an external-evidence document while retaining project HOLD.**

Do not:

- alter the cycle architecture solely because of Solar Polar;
- change the 135 °C generator value solely because DAR uses higher temperatures;
- change pressure solely because Solar Polar studied 14–22 bar;
- change condenser/absorber geometry solely from Solar Polar;
- add hydrogen;
- copy patent materials or thermal-storage values;
- treat Solar Polar performance as direct validation.

Do:

- add the benchmark to the evidence/traceability layer;
- make OQ-0 explicit;
- independently audit COP = 0.424;
- validate condenser/absorber performance;
- perform dynamic solar simulation;
- retain the HOLD gate until the existing pressure, materials, safety, thermodynamic and quality gaps are resolved.

---

## 21. Primary references

1. Najjaran, A., Freeman, J., Ramos, A., Markides, C.N. (2019). *Experimental investigation of an ammonia-water-hydrogen diffusion absorption refrigerator*. Applied Energy 256, 113899. https://doi.org/10.1016/j.apenergy.2019.113899
2. Freeman, J., Markides, C.N. (2024). *A solar diffusion-absorption refrigeration system for off-grid cold-chain provision. Part I: Model development and experimental calibration*. Renewable Energy 230, 120718. https://doi.org/10.1016/j.renene.2024.120718
3. Freeman, J., Markides, C.N. (2024). *A solar diffusion-absorption refrigeration system for off-grid cold-chain provision, Part II: System simulation and assessment of performance*. Renewable Energy 230, 120717. https://doi.org/10.1016/j.renene.2024.120717
4. Solar Polar official technology information: https://www.solar-polar.co.uk/solar-cooling
5. Solar Polar official concentrator information: https://www.solar-polar.co.uk/solar-concentrator
6. Solar Polar modular cooling patent: https://patents.google.com/patent/US9032755B2/en
7. Solar Polar solar thermal collector patent family: https://patents.google.com/patent/WO2023017273A1/en
8. UKRI Energy Catalyst Solar Polar case study: https://energycatalyst.ukri.org/casestudies/solar-polar-low-cost-cooling-improves-health-and-economic-outcomes-for-off-grid-communities-in-developing-nations/

---

## 22. Claude handoff — implementation instructions

Claude should treat this document as an **external benchmark and validation workstream**, not as an approval record.

Recommended implementation sequence:

1. Read this document.
2. Read `docs/DESIGN_SUMMARY.md`.
3. Read `docs/ENGINEERING_VALIDATION_CALL.md`.
4. Read `BUILD_RELEASE_GATE.md`.
5. Read the canonical open-gap/decision documents when available in the working tree.
6. Create/update BENCHMARK-01 in the project's traceability system.
7. Create/update OQ-0 — Cycle Architecture Selection.
8. Add explicit links from D-007 and the relevant thermal/performance gaps to BENCHMARK-01.
9. Do not close any gap merely because this benchmark exists.
10. Do not modify approved design values without a controlled engineering decision.
11. Preserve **HOLD** status.

### Suggested acceptance criterion for BENCHMARK-01

The benchmark is complete when every important comparison row has:

- source;
- year;
- evidence class;
- experimental/modelled/assumed classification;
- units;
- applicability statement;
- known uncertainty/limitation.

### Suggested acceptance criterion for the next thermodynamic task

An independent reviewer should be able to reproduce the Clay COP calculation from the repository without relying on undocumented assumptions.

---

## Final engineering position

The Solar Polar investigation did **not** close the project's formal gaps.

It did something more useful:

> It converted a vague external example into a strong, traceable benchmark and exposed several system-level failure modes that the Clay design must explicitly survive.

The project should therefore remain:

**HOLD — NOT RELEASED FOR FABRICATION, PRESSURE TESTING, AMMONIA CHARGING, OR OPERATION.**

The next high-value technical task is the **Solar Polar vs Clay architecture benchmark**, followed by an independent audit of the Clay COP = 0.424 and a hot-climate condenser/absorber validation.
