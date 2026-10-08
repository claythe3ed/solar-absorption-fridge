# PERPLEXITY-AI-01 — Independent COP Literature Audit

**Status:** EXTERNAL RESEARCH INPUT — NOT ACCEPTED VALIDATION
**Project status:** HOLD
**Related work package:** THERMO-AUDIT-01
**Purpose:** Preserve the Perplexity AI literature-search finding as an independent research input for Claude and Copilot review.

## 1. Executive finding from Perplexity

Perplexity concluded that the available literature does not validate COP = 0.424 for the specific design. It identified supporting context and experimental/model benchmarks, but no verified primary experiment matching all of the following simultaneously:

- mechanically circulated, two-fluid NH3-H2O cycle;
- approximately 135 °C generator;
- approximately 40 °C condenser;
- approximately -15 °C evaporator;
- approximately 200 W cooling capacity.

Perplexity therefore recommends:

**COP = 0.424 remains an unvalidated design estimate. D-007 remains OPEN.**

A numerically similar COP is not sufficient unless architecture, temperature lift, capacity scale, COP definition, and generator boundary are comparable.

## 2. COP-boundary findings

Perplexity states that the minimum thermal COP is COP = Q_evap / Q_gen. For a mechanically circulated system, pump power should also be reported, and complete system assessment should include auxiliary power.

It identifies generator-boundary questions including generator vessel heat, rectifier/dephlegmator heat, analyzer heat, external solution-preheater heat, separate distillation-section heat, startup/transient energy, generator and associated piping heat loss, and pump/auxiliary electricity.

## 3. Primary evidence identified

### Najjaran, Freeman & Ramos (2019)
Experimental investigation of an ammonia-water-hydrogen diffusion absorption refrigerator.
Perplexity reports approximately 100–120 W nominal cooling, three-fluid NH3-H2O-H2 architecture, approximately 23.8 bar charge and 30% ammonia by mass, approximately 79–104 W cooling, COP approximately 0.11–0.26, generator heat approximately 300–700 W, and generator temperatures approximately 150–200 °C.

This does NOT directly validate the present two-fluid mechanically circulated design. It is practical small-scale system evidence.

### 2023 small-scale NH3-H2O experimental study
Performance Evaluation of a Small Scale Ammonia-Water Absorption Cooling System.
DOI: 10.18280/ijht.420110.
Perplexity reports experimental COP approximately 0.63–0.64, evaporator around 7 °C, generator around 85–100 °C, COP uncertainty approximately ±5.61%, and cooling-capacity uncertainty approximately ±6.93%.

This is not directly comparable to -15 °C evaporation.

### Tao et al. (2022), Energies
Compact Ammonia/Water Absorption Chiller of Different Cycle Configurations: Parametric Analysis Based on Heat Transfer Performance.
Perplexity reports a model validated against experimental data, COP defined using cooling capacity divided by heating capacity and consumed power, pump power included for non-compression-assisted cycles, modeled COP approximately 0.51–0.58 at a 120 °C heat source for selected configurations, relevance to sub-zero refrigeration, and refrigerant impurity/concentration effects.

This is one of the more relevant sources because it addresses two-fluid NH3-H2O behavior and sub-zero operation, but it does not validate the present 200 W design.

### Lin et al. (2009)
Perplexity identifies an experimental NH3-H2O system with solution pump, generator/distillation section, condensers, evaporator, absorber, and solution heat exchangers. Evaporator temperature was approximately 4.6 °C, COP approximately 0.43, and heating power around 1700 W.

Numerical similarity to 0.424 is NOT validation because temperature lift, capacity, and application differ.

### Experimental ammonia/water exergy study (2023)
Perplexity identifies an experimental NH3-H2O cooling/exergy study but says the available result did not expose enough information to establish direct comparability. It should remain a candidate for full-text extraction rather than accepted benchmark evidence.

### NBS ammonia-water absorption chiller report
Perplexity identifies Laboratory Evaluation of the Steady-State and Part Load Performance of an Ammonia-Water Absorption Water Chiller as potentially important primary experimental literature. It recommends retrieval and extraction of operating-point data before quantitative use.

## 4. Evidence explicitly excluded from direct COP comparison

- Diffusion absorption refrigeration is not directly comparable because it uses an inert gas and generally thermosyphon/bubble-pump circulation.
- Generic simulation papers do not validate actual circulation, heat loss, rectification, mass transfer, heat-exchanger pinch, small-scale heat leaks, or measured cooling capacity.
- Solar Polar DAR COP must NOT be used as direct comparison to the current two-fluid COP.

## 5. Potential falsifiers of COP = 0.424

1. Generator-boundary error.
2. Cooling-load overestimation.
3. Refrigerant impurity/incomplete rectification.
4. Poor absorber performance.
5. Heat-exchanger degradation or incorrect effectiveness.
6. Low-temperature pressure/flow instability.
7. Unverified solution concentration.
8. Transient rather than steady-state operation.
9. Pump and auxiliary power.
10. Scale effects at approximately 200 W.

## 6. Required validation dataset proposed by Perplexity

Perplexity recommends an auditable dataset containing independently measured evaporator cooling load, generator thermal input, solution flow, refrigerant flow, NH3 concentration in rich and poor solutions, refrigerant purity/water carryover, generator/condenser/absorber/evaporator temperatures, relevant pressures, pump power, auxiliary power, uncertainty estimates, and steady-state criteria.

It recommends uncertainty propagation for COP rather than reporting a single unqualified number.

## 7. Perplexity final finding

Perplexity concludes that COP values around 0.4–0.6 are plausible for NH3-H2O absorption systems under favorable conditions. It also concludes that experimental systems have reported COP near 0.43 but not under the exact Clay operating point; small-scale systems have reported approximately 0.52–0.64 at warmer evaporator temperatures; validated models have reported approximately 0.51–0.58 for selected NH3-H2O configurations; and small three-fluid diffusion systems have reported approximately 0.11–0.26.

Therefore:

**COP = 0.424 is plausible but not validated.**

## 8. Required Claude/Copilot review

Treat this document as an external research input, not project truth.

Claude and Copilot should independently report:

1. Which Perplexity claims are confirmed by the cited primary sources.
2. Which claims are overstated, incomplete, or unsupported.
3. Whether any cited COP definitions are genuinely comparable to the Clay COP boundary.
4. Whether the reported temperature/capacity/architecture comparisons are valid.
5. Any missing primary literature that materially changes the conclusion.
6. Whether the Perplexity findings expose additional issues in src/thermo/cycle_model.py.
7. Whether D-007 should remain OPEN.
8. What evidence would be sufficient to move COP from MODEL OUTPUT/UNVERIFIED toward VALIDATED.
9. Exact source paths and reproducible calculations where applicable.

**Do not silently modify the cycle model based on this document.**

## 9. Relationship to THERMO-AUDIT-01

This document feeds into THERMO-AUDIT-01 — NH3-H2O Cycle Model Audit.

It specifically informs COP definition and boundary, independent two-fluid literature benchmarking, species/rectification audit, generator separation/water-carryover audit, pump/auxiliary-power accounting, and uncertainty analysis.

It does NOT close D-007 and does NOT change the project HOLD status.

## 10. Evidence classification

All Perplexity-derived findings should initially be treated as:

**PRELIMINARY / EXTERNAL RESEARCH INPUT**

They may be promoted only after source-level verification.

---
Generated from the Perplexity AI response supplied to the project review workflow on 2026-10-05.