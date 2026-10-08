# Solar Polar Benchmark — Comprehensive Engineering Review for Claude

**Repository:** `claythe3ed/solar-absorption-fridge`  
**Report:** Solar Polar / Solar-DAR benchmark and implications for the proposed NH3-H2O refrigerator  
**Status:** RESEARCH / BENCHMARK ONLY — does not change release status  
**Current project disposition:** **HOLD**  
**Prepared:** 2026-10-05

---

## 0. Executive Summary

Solar Polar is one of the most relevant external benchmarks identified so far for this project because it combines:

- solar-thermal heat input;
- ammonia-based absorption refrigeration;
- small-scale/off-grid operation;
- warm-climate deployment;
- passive/thermally driven circulation;
- experimental hardware;
- academic modelling and calibration;
- field demonstrations;
- patents and system-development history.

However, Solar Polar is **not a direct validation of the present Clay design**.

The Solar Polar/Imperial work is primarily based on **three-fluid diffusion-absorption refrigeration (DAR): NH3-H2O-H2**, whereas the present Clay design is a **two-fluid NH3-H2O continuous absorption cycle**. The architectures have materially different circulation mechanisms, gas handling, component functions, startup behavior, and safety considerations.

The strongest external evidence is therefore a **benchmark**, not a design template.

The literature gives several important findings:

1. Small-scale NH3-H2O-H2 DAR refrigeration has been experimentally demonstrated.
2. Experimental COP values around **0.25-0.26** have been reported for relevant small DAR systems.
3. A 2024 experimentally calibrated solar-DAR model reported a maximum steady-state COP of about **0.25 at 14 bar** and found that, at 100 W heat input, bubble-pump activation could take **2 h or longer**, with no cooling before activation.
4. A companion 2024 solar-system study found an optimal charge pressure of about **16 bar** for the modeled Ahmedabad case and predicted less than **5 h/day** operation and less than **1% solar-to-cooling efficiency** for the nominal 70 W system/configuration studied.
5. Older experimental work on NH3-H2O-H2 DAR reported generator temperatures around **175-215 °C** and COP of **0.11-0.26** over 150-700 W heat input.
6. These DAR startup and high-temperature requirements **must not be transferred directly to the present two-fluid cycle**, because the Clay architecture does not depend on a thermally driven bubble pump for solution circulation.
7. Solar Polar nevertheless exposes system-level risks directly relevant to Clay: condenser rejection in hot ambient conditions, generator/rectifier coupling, startup/transient behavior, solar-collector/cycle matching, absorber sizing, and the danger of judging a solar refrigerator from steady-state COP alone.
8. The present **COP = 0.424** therefore deserves independent scrutiny. It is not disproven, but it is materially above the approximately 0.25-0.26 experimental DAR benchmark and must be explained by architectural/operating differences and independently validated.
9. The present **135 °C generator target should remain an explicit two-fluid-cycle hypothesis**, not be justified or rejected using DAR precedent alone.
10. Solar Polar strengthens the case for a formal architecture comparison rather than an immediate architecture change.

**Recommendation:** do not redesign or release the Clay refrigerator based on Solar Polar evidence alone. Add Solar Polar as a formal benchmark and execute a controlled comparison between:
- the present continuous NH3-H2O architecture;
- NH3-H2O-H2 DAR;
- an intermittent NH3-H2O architecture;
- and, only if evidence warrants, a hybrid architecture.

---

## 1. Scope and Evidence Discipline

This report is intended to give Claude and future reviewers a durable engineering brief.

It distinguishes:

- **Experimental evidence** — measured hardware results.
- **Model/calculation evidence** — simulation or calibrated model results.
- **Field/deployment evidence** — demonstrations or funded deployment activity.
- **Patent evidence** — architecture/design intent, not independent performance validation.
- **Company/marketing information** — useful for current product/technology description, but not equivalent to experimental validation.

No Solar Polar value in this report should automatically become a Clay design input.

A Solar Polar result can be used as:

- an external benchmark;
- a plausibility check;
- a source of failure modes;
- a source of validation methods;
- a candidate architecture for comparative analysis.

It should not be silently copied into:
- design pressure;
- design temperature;
- material selection;
- ammonia charge;
- relief settings;
- vessel geometry;
- collector dimensions;
- COP target;
- operating envelope.

---

## 2. Solar Polar Architecture

Solar Polar's cooling technology is based on **diffusion-absorption refrigeration (DAR)**.

The key working-fluid system is:

**NH3 + H2O + H2**

The third component, hydrogen, is an inert/auxiliary gas that establishes partial-pressure conditions in the evaporator and gas circuit.

The principal functional sequence is:

**Solar thermal input -> generator/bubble pump -> rectifier -> condenser -> evaporator -> NH3/H2 gas -> absorber -> reservoir -> generator**

Important functional elements include:

- solar collectors;
- generator;
- thermally driven bubble pump;
- rectifier;
- condenser;
- evaporator;
- absorber;
- reservoir;
- hydrogen gas return path;
- heat exchangers.

This is fundamentally different from the present Clay cycle:

**NH3-H2O continuous absorption cycle**

where the current design uses defined high/low pressure sides and a solution circulation ratio rather than a DAR hydrogen diffusion loop.

### Engineering consequence

The apparent mechanical simplicity of DAR does not imply thermodynamic simplicity.

DAR removes conventional mechanical circulation hardware but adds coupled:

- bubble-pump behavior;
- gas circulation;
- partial-pressure evaporation;
- rectification;
- gas-liquid mass transfer;
- absorber hydrogen return;
- transient startup behavior.

Therefore:

> **DAR should be treated as a different system architecture, not a simplified version of the Clay two-fluid cycle.**

---

## 3. Primary Experimental Evidence

### 3.1 2019 experimental NH3-H2O-H2 DAR study

Najjaran Kheirabadi, Freeman, Ramos Cabal and Markides reported a detailed experimental evaluation of a nominal 100 W DAR refrigerator.

The experimental system used:

- NH3-H2O-H2;
- nominal 100 W cooling capacity;
- electrical cartridge heaters as the thermal input;
- 150-700 W heat input;
- measured generator temperatures of approximately 175-215 °C;
- default manufacturer settings of 22 bar charge pressure and 30% ammonia concentration.

Measured cooling output was approximately:

**24-108 W**

and measured COP was:

**0.11-0.26**

with maximum COP around:

**0.26 at approximately 300 W heat input**.

This is direct experimental evidence, not a marketing claim.

Source:
https://spiral.imperial.ac.uk/entities/publication/bfb53c4f-4b15-45bf-9ae8-68740aa104d4

DOI:
https://doi.org/10.1016/j.apenergy.2019.113899

### Interpretation for Clay

This does **not** invalidate COP = 0.424.

It does establish a useful external scale:

> A small NH3-based DAR system has experimentally achieved roughly 0.25-0.26 COP under tested conditions.

The Clay cycle differs in:
- architecture;
- circulation;
- pressure levels;
- evaporator temperature;
- absorber configuration;
- solution concentrations;
- generator temperature;
- heat exchanger assumptions.

Therefore the correct question is:

> **What physical features of the Clay two-fluid cycle allow COP = 0.424, and are all of those gains supported by independent property, mass/energy balance, component and loss calculations?**

---

## 4. 2024 Part I — Solar-DAR Model + Experimental Calibration

Freeman and Markides, Renewable Energy 230 (2024), 120718, developed a semi-empirical model covering both steady-state and dynamic startup behavior.

The model was calibrated using laboratory DAR experiments with adjustable:
- heat input;
- system charge pressure.

The paper reports:

- maximum steady-state COP about **0.25 at 14 bar**;
- at 100 W heat input, bubble-pump activation could take **2 h or longer**;
- no cooling was produced before bubble-pump activation;
- experimentally calibrated steady-state COP prediction within approximately **±20%**;
- peak startup heat-source temperature prediction within approximately **±10 K**.

Source:
https://www.sciencedirect.com/science/article/pii/S0960148124007869

DOI:
https://doi.org/10.1016/j.renene.2024.120718

### Critical lesson

For solar refrigeration:

**steady-state COP != daily useful cooling**

A solar system may have an acceptable steady-state COP but poor daily performance if:
- startup is slow;
- the collector spends much of the morning below activation temperature;
- heat storage is inadequate;
- condenser rejection is poor;
- operating pressure is mismatched to ambient temperature.

This is directly relevant to the Clay project.

---

## 5. 2024 Part II — Solar System Simulation

The companion Renewable Energy paper simulated the solar-DAR system for rural Ahmedabad.

Reported findings include:

- nominal cooling system around 70 W;
- collector area around 1.5 m² identified as appropriate for the modeled nominal system;
- approximately 16 bar identified as an optimal charge pressure for the modeled October Ahmedabad case;
- daily operating period less than 5 h;
- predicted overall solar-to-cooling efficiency less than 1%.

Source:
https://www.sciencedirect.com/science/article/pii/S0960148124007857

DOI:
https://doi.org/10.1016/j.renene.2024.120717

### Interpretation

This is not a universal DAR performance limit.

It is the outcome of a specific:
- architecture;
- component set;
- collector;
- climate;
- pressure;
- control/startup model;
- nominal cooling capacity.

But it demonstrates why Clay's project should eventually model:

**hourly solar input -> collector outlet temperature -> generator heat input -> cycle state -> condenser/absorber rejection -> instantaneous cooling -> startup/shutdown/storage**

rather than relying only on nominal steady-state COP.

---

## 6. 2017 Solar Polar / Imperial Study

The 2017 Solar Polar/Imperial work investigated a laboratory DAR system and solar-cooling application for India.

Source:
https://spiral.imperial.ac.uk/entities/publication/efdb60ca-e9f6-4355-b125-84ca5b15857a

The work is particularly valuable because it connects:
- DAR hardware;
- pressure;
- heat input;
- solar collector behavior;
- startup;
- condenser limitations;
- field-demonstration thinking.

It should be treated as an important benchmark document for Clay's design review.

---

## 7. The 135 °C Question

This is the most important architectural distinction.

### Solar Polar / conventional NH3-H2O-H2 DAR

The published Solar Polar-related experimental evidence includes generator temperatures around 175-215 °C, and the solar-DAR research emphasizes the difficulty of activating the bubble pump under insufficient thermal input.

Therefore:

> **135 °C should be regarded as potentially problematic for this particular NH3-H2O-H2 DAR architecture unless a low-temperature bubble-pump design is specifically demonstrated.**

### Clay two-fluid NH3-H2O cycle

The Clay design does not use the same bubble-pump mechanism.

Therefore:

> **The DAR high-temperature requirement cannot be used as proof that a 135 °C two-fluid NH3-H2O cycle is impossible.**

The correct Clay question is:

> Can the complete two-fluid cycle produce 200 W at -15 °C evaporator / 40 °C condenser / 30 °C absorber using a 135 °C generator, at the stated solution concentrations, circulation ratio, heat exchanger effectiveness, and pressure levels, with all required parasitic and heat-loss terms included?

This question should be answered independently.

---

## 8. Lower-Temperature DAR Literature — Important Counterpoint

The broader DAR literature shows that low-source-temperature DAR is possible in specially redesigned systems.

Rattner and Garimella investigated NH3-NaSCN-He DAR architectures intended for source temperatures at or below approximately 130 °C.

Their work shows that low-temperature DAR requires:
- alternate working fluids;
- redesigned bubble-pump generator;
- enhanced absorber;
- detailed component-level heat/mass-transfer design.

Source:
https://www.sciencedirect.com/science/article/pii/S0140700715003059

A companion experimental study reports operation of a demonstration-scale low-source-temperature DAR system over source/operating conditions including the 110-130 °C range, with refrigeration-grade cooling but relatively low COP.

Source:
https://www.sciencedirect.com/science/article/abs/pii/S0140700715003801

### Why this matters

It prevents an overstatement:

> “DAR always needs 180-230 °C.”

That statement is too broad.

The more defensible statement is:

> **Conventional NH3-H2O-H2 DAR has demanding source-temperature/startup behavior, while low-source-temperature DAR has been demonstrated using different working fluids and substantially redesigned components.**

This distinction should be preserved in future project documentation.

---

## 9. Pressure Benchmark

Solar Polar-related research provides a useful pressure benchmark in the approximate range:

**14-21 bar**

with the 2024 modeled Ahmedabad case identifying approximately:

**16 bar**

as an optimum for its specific system.

Clay's present model:

**high side = 15.55 bar**

This is interesting because the values are of the same order.

But it is **not validation**.

Pressure is coupled to:
- ammonia saturation temperature;
- condenser ambient approach;
- generator temperature;
- rectification;
- absorber operation;
- system charge;
- component pressure drop;
- safety margin.

### Required Clay conclusion

Do not write:

> “Solar Polar validates our 15.55 bar pressure.”

Write:

> “Solar Polar/DAR literature provides an external pressure-scale benchmark near the present modeled high-side pressure, but does not establish the Clay design pressure or its pressure-boundary basis.”

---

## 10. Hot-Climate Condenser Risk

This is one of the most useful lessons from the benchmark.

DAR studies show that lower pressure can reduce required source temperature, but lower pressure also reduces refrigerant condensation temperature.

In a hot ambient environment this can become a serious limitation.

For Clay, the relevant coupled system is:

**ambient temperature -> condenser temperature -> high-side pressure -> generator requirement -> solar collector requirement**

Therefore high-side pressure cannot be optimized in isolation.

### Clay design point

- high side: 15.55 bar
- condenser: 40 °C
- ambient environment: Sudan / Khartoum screening
- condenser heat rejection: 274.8 W
- natural convection
- preliminary U basis: 15 W/m²K

This makes E-102 a high-priority validation component.

---

## 11. Consequence for E-102 Condenser CFD

Current Clay CFD work provides preliminary evidence:

- single 15 mm cylinder;
- OpenFOAM v1912;
- calculated heat-transfer coefficient approximately 21.23 W/m²K;
- design U = 15 W/m²K.

However, the current extraction method has a known limitation: the reported HTC was inferred using an assumed thermal boundary-layer thickness rather than directly integrating wall heat flux, and pressure-field convergence was incomplete.

Therefore:

**Do not call the CFD a validated condenser model.**

Recommended next CFD validation:

1. Use wall heat flux directly.
2. Integrate total wall heat rejection.
3. Calculate HTC from a clearly defined bulk-to-wall temperature difference.
4. Demonstrate mesh sensitivity.
5. Demonstrate residual/convergence criteria.
6. Run the actual proposed condenser geometry.
7. Test relevant ambient temperatures.
8. Test realistic air velocity/natural-convection conditions.
9. Compare against an independent analytical correlation.
10. Document uncertainty.

Solar Polar makes this work more important, not less.

---

## 12. Absorber Benchmark

Solar Polar-related experimental work used substantial absorber/condenser heat-transfer capacity.

The DAR absorber has multiple simultaneous functions:
- ammonia absorption;
- hydrogen return;
- gas-liquid contact;
- heat rejection;
- circulation/mass-transfer management.

Clay V-102 is physically integrated with V-101 and currently has:
- approximately 3.97 m² stated total available surface;
- approximately 1.5 m² additional fin area;
- approximately 396.7 W absorber heat load.

The benchmark does not establish that 3.97 m² is sufficient.

### Required validation question

> Can the proposed V-102 geometry achieve the required NH3 absorption rate and heat rejection at the stated solution concentration, pressure, temperature and flow regime?

This is a coupled **heat + mass transfer** problem.

A finned surface-area calculation alone is not enough.

---

## 13. Generator / Rectifier Coupling

Solar Polar's DAR research highlights an important system lesson:

The generator is not simply a device that adds heat.

Generator heat input affects:
- bubble-pump circulation;
- refrigerant generation;
- rectification;
- water carryover;
- condenser composition;
- refrigerant flow;
- COP.

Therefore the Clay generator should similarly be evaluated as part of a coupled subsystem:

**generator + desorption + rectification + solution circulation + SHX + condenser**

rather than as a standalone heat input boundary.

---

## 14. Solar Collector Benchmark

Clay E-101:

- CPC;
- 400 mm aperture;
- 1.59 m² aperture area;
- 4 m nominal receiver;
- 200 mm OD receiver;
- 2.5 mm wall;
- acceptance half-angle 30°;
- concentration ratio 2.0;
- East-West horizontal;
- nominal 15° tilt basis.

Solar Polar's technology history is relevant because its development evolved toward high-temperature solar concentration.

The current Solar Polar site presents a solar concentrator technology intended for high-temperature thermal applications, while its earlier DAR work used solar-thermal collector systems.

Official technology page:
https://www.solar-polar.co.uk/solar-cooling

Current concentrator page:
https://www.solar-polar.co.uk/solar-concentrator

### Correct benchmark question

Do not ask:

> “Should Clay copy Solar Polar's collector?”

Ask:

> **At the same aperture area and the same Khartoum solar resource, which collector can deliver the required useful generator heat at the required temperature, with acceptable optical/thermal efficiency, manufacturability, dust tolerance and maintenance burden?**

This is the correct collector-level comparison.

---

## 15. Thermal Storage

Solar Polar's development history includes thermal-storage concepts.

This is highly relevant because the major weakness of solar thermal refrigeration is not necessarily steady-state operation; it is the mismatch between:
- solar availability;
- startup;
- generator requirements;
- cooling demand.

For Clay, thermal storage should therefore be considered as an **architecture option**, not an automatic requirement.

Potential storage functions:
- smooth cloud transients;
- reduce morning startup penalty;
- extend evening operation;
- decouple collector temperature from generator temperature;
- protect the refrigeration cycle from rapid solar fluctuations.

But no Solar Polar storage material or temperature should be adopted directly.

---

## 16. 200 W Benchmark

The project target is:

**200 W cooling**

Solar Polar literature contains systems and development targets in the same general small-scale range, including 100 W-class experimental DAR hardware and reported 200 W-class modular concepts.

The most defensible use of this evidence is:

> **The 200 W target is within the demonstrated scale of small ammonia absorption/DAR technology.**

It is not evidence that the Clay architecture can produce 200 W.

The Clay target still requires:
- full cycle balance;
- component sizing;
- heat/mass transfer validation;
- transient solar simulation;
- pressure/safety review.

---

## 17. COP Comparison

Current Clay design point:

**COP = 0.424**

Solar Polar-related experimental DAR:

**approximately 0.25-0.26 maximum in cited studies**

This creates an important benchmark gap:

**0.424 / 0.26 ≈ 1.63**

The Clay predicted COP is therefore roughly 1.6x the upper end of the cited DAR experimental range.

Again, this is not a proof of error because the systems are not identical.

But it is enough to require an explicit reconciliation.

### COP reconciliation checklist

Claude should independently audit:

1. definition of COP;
2. generator heat boundary;
3. cooling-load boundary;
4. pump/electrical parasitic treatment;
5. solution-pump heat;
6. heat loss from generator;
7. heat loss from piping;
8. solution heat exchanger effectiveness;
9. absorber heat rejection;
10. condenser heat rejection;
11. rectifier assumptions;
12. refrigerant purity;
13. ammonia-water property formulation;
14. bubble/dew calculations;
15. concentration basis (mass vs mole fraction);
16. state-point temperatures;
17. pressure assumptions;
18. enthalpy reference consistency;
19. mass balance closure;
20. uncertainty.

The objective is not to force the COP downward.

The objective is to determine whether **0.424 is a physically traceable result**.

---

## 18. What Solar Polar Does NOT Validate

Solar Polar does not validate:

- Clay's 15.55 bar design pressure;
- Clay's 16 vs 25 bar design-pressure decision;
- Clay's vessel wall thickness;
- Clay's end-cap thickness;
- Clay's nozzle dimensions;
- Clay's port projection;
- Clay's material compatibility;
- Clay's relief-device basis;
- Clay's pressure testing;
- Clay's silver-brazing decision;
- Clay's 0.424 COP;
- Clay's 135 °C generator;
- Clay's 3.97 m² absorber area;
- Clay's 274.8 W condenser design;
- Clay's 1.59 m² CPC;
- Clay's 150 L cold-box design;
- Clay's ammonia charge;
- Clay's fabrication readiness.

This list should be preserved to prevent benchmark evidence from becoming accidental design approval.

---

## 19. What Solar Polar DOES Strengthen

The benchmark strengthens the following project statements:

### Strongly strengthened

- Small solar-thermal ammonia refrigeration is technically credible.
- DAR is a serious alternative architecture for off-grid cooling.
- 100 W-class experimental DAR systems exist.
- Solar-DAR has been studied experimentally and dynamically.
- Hot-climate heat rejection is a critical system-level issue.
- Startup/transient behavior matters.
- Collector/cycle integration matters.
- Pressure and source temperature are strongly coupled.

### Moderately strengthened

- 200 W is a plausible target scale.
- High-side pressures in the mid-teens of bar are plausible in related systems.
- Large condenser/absorber heat-transfer surfaces can be important.
- Thermal storage deserves explicit investigation.

### Not strengthened

- The present Clay design is correct.
- The present Clay design is safe.
- The present Clay design is ready to fabricate.
- The present Clay COP is validated.
- The present Clay pressure basis is acceptable.

---

## 20. Architecture Decision: Two-Fluid vs DAR

### Candidate A — Current Clay architecture

**NH3-H2O continuous absorption**

Potential advantages:
- no hydrogen inventory;
- no bubble-pump startup dependency;
- explicit high/low pressure architecture;
- potentially lower generator temperature;
- conventional circulation can be controlled;
- easier conceptual separation of refrigeration and solar thermal subsystems.

Potential disadvantages:
- solution pump/mechanical circulation;
- electrical dependence unless another circulation method is adopted;
- pressure-vessel requirements;
- seals and pump compatibility;
- parasitic electrical consumption;
- more active components.

### Candidate B — Solar Polar-type DAR

**NH3-H2O-H2 diffusion absorption**

Potential advantages:
- thermally driven circulation;
- very low electrical requirement;
- no conventional solution pump;
- demonstrated off-grid architecture;
- simple mechanical concept.

Potential disadvantages:
- bubble-pump startup;
- strong generator-temperature sensitivity;
- hydrogen handling;
- coupled gas/liquid mass transfer;
- condenser sensitivity;
- transient performance;
- relatively modest experimental COP;
- difficult optimization at low source temperature.

### Candidate C — Intermittent NH3-H2O solar cycle

Potential advantages:
- potentially simpler mechanics;
- potentially no continuous pump;
- easier solar/thermal-storage integration.

Potential disadvantages:
- intermittent cooling;
- storage requirement;
- different duty-cycle definition;
- different food/cold-chain usability;
- need for a completely different control/storage analysis.

### Decision status

**OPEN**

No architecture should be silently selected from this benchmark.

---

## 21. Recommended Formal Benchmark Record

Add:

### BENCHMARK-01 — Solar Polar / Imperial Solar-DAR

**Purpose:** External benchmark for small-scale solar-thermal ammonia refrigeration.

**Compare:**
1. cycle architecture;
2. working fluids;
3. circulation mechanism;
4. operating pressure;
5. generator temperature;
6. startup behavior;
7. collector technology;
8. collector area;
9. steady-state COP;
10. daily cooling;
11. solar-to-cooling efficiency;
12. condenser requirements;
13. absorber requirements;
14. evaporator conditions;
15. thermal storage;
16. working-fluid inventory;
17. materials;
18. safety architecture;
19. field evidence;
20. manufacturability.

Every imported value must carry:
- source;
- publication year;
- experimental/modelled/field classification;
- applicability;
- uncertainty/limitations.

---

## 22. Recommended Formal Architecture Question

### OQ-0 — Cycle Architecture Selection

Compare:

**A. Continuous two-fluid NH3-H2O**

**B. Three-fluid NH3-H2O-H2 DAR**

**C. Intermittent NH3-H2O**

**D. Hybrid architecture — only if justified by evidence**

Decision criteria:
- required cooling duty;
- daily cooling energy;
- generator temperature;
- solar collector area;
- startup time;
- hot-ambient condenser performance;
- absorber performance;
- pressure safety;
- materials;
- electrical consumption;
- maintenance;
- manufacturability in Sudan;
- water/ammonia handling;
- control complexity;
- thermal storage requirements;
- lifecycle reliability.

---

## 23. Recommended Next Validation Work

### Priority 1 — Independent Clay COP audit

Recalculate the complete cycle independently.

Deliver:
- state table;
- mass balance;
- energy balance;
- property-source traceability;
- uncertainty;
- comparison with 0.424.

### Priority 2 — Hot-ambient condenser model

Use:
- actual E-102 geometry;
- wall heat flux;
- validated natural-convection correlations;
- relevant Khartoum ambient envelope;
- sensitivity to air velocity;
- sensitivity to condenser temperature.

### Priority 3 — Absorber heat + mass transfer

Establish whether V-102 can actually absorb the required ammonia rate, not merely reject 396.7 W.

### Priority 4 — Hourly solar-cycle model

Simulate:
- solar irradiance;
- collector temperature;
- generator heat;
- cycle state;
- condenser/absorber rejection;
- startup;
- shutdown;
- storage if applicable.

### Priority 5 — Architecture comparison

Build a controlled comparison of A/B/C above.

### Priority 6 — D-007 thermodynamic validation

Use independent ammonia-water reference calculations and/or experimental datasets.

Do not treat a related DAR dataset as direct validation of the Clay Ziegler-Trepp implementation.

### Priority 7 — Pressure/material/safety basis

Continue independently of Solar Polar.

Solar Polar cannot close these gates.

---

## 24. Impact on the Existing 20 Formal Gaps

Solar Polar does **not close any of the 20 formal DB/D entries**.

It materially improves the evidence base for approximately seven areas:

| Gap | Effect |
|---|---|
| DB-02 Site ambient envelope | Better external evidence for hot-climate rejection sensitivity |
| DB-03 Maximum generator temperature | Better informed by source-temperature/startup evidence |
| DB-04 Maximum high-side operating pressure | Related-system pressure benchmark |
| DB-06 Design temperature range | Better informed by experimental/modelled DAR behavior |
| DB-12 Solar resource/collector envelope | Stronger collector/cycle benchmark |
| DB-13 Cooling/performance criteria | External small-scale cooling benchmark |
| D-007 Thermodynamic mixture validation | Stronger independent comparison context, but not direct validation |

Therefore:

**Formal gaps closed: 0 / 20**

**Materially better informed: approximately 7 / 20**

**Release disposition: HOLD**

The benchmark also substantially improves the definition of **OQ-0 architecture selection**.

---

## 25. New Risks Exposed by the Benchmark

Solar Polar adds or strengthens the following risk register items:

### SP-R01 — Startup/transient risk

A solar thermal refrigerator can lose a significant portion of the useful solar day before reaching operating conditions.

### SP-R02 — High-source-temperature requirement

DAR startup can require much higher temperatures than steady-state intuition suggests.

### SP-R03 — Condenser/ambient coupling

Lower pressure can make heat rejection difficult in hot ambient conditions.

### SP-R04 — COP optimism

A high modeled COP must be reconciled against experimental benchmarks and all heat/parasitic boundaries.

### SP-R05 — Absorber mass-transfer limitation

Surface area alone does not establish ammonia absorption capacity.

### SP-R06 — Solar/cycle mismatch

Collector design cannot be separated from generator and refrigeration-cycle operating requirements.

### SP-R07 — Daily-vs-steady-state confusion

A steady-state COP is insufficient as a project-level performance metric.

### SP-R08 — Benchmark transfer error

DAR evidence must not be silently transferred to the two-fluid cycle.

---

## 26. Source Hierarchy

Recommended evidence hierarchy for this benchmark:

### Tier 1 — Experimental / peer-reviewed

**2019**
Najjaran Kheirabadi et al., experimental NH3-H2O-H2 DAR.

https://spiral.imperial.ac.uk/entities/publication/bfb53c4f-4b15-45bf-9ae8-68740aa104d4

DOI: https://doi.org/10.1016/j.apenergy.2019.113899

### Tier 1 — Experimentally calibrated model

**2024 Part I**
Freeman & Markides, Renewable Energy 230, 120718.

https://www.sciencedirect.com/science/article/pii/S0960148124007869

DOI: https://doi.org/10.1016/j.renene.2024.120718

### Tier 1 — Solar system simulation

**2024 Part II**
Renewable Energy 230, 120717.

https://www.sciencedirect.com/science/article/pii/S0960148124007857

DOI: https://doi.org/10.1016/j.renene.2024.120717

### Tier 2 — Solar Polar / Imperial conference work

**2017**
Testing and simulation of a solar diffusion-absorption refrigeration system for low-cost solar cooling in India.

https://spiral.imperial.ac.uk/entities/publication/efdb60ca-e9f6-4355-b125-84ca5b15857a

### Tier 2 — Broader low-temperature DAR research

Rattner & Garimella, low-source-temperature DAR modelling and experiments.

https://www.sciencedirect.com/science/article/pii/S0140700715003059

https://www.sciencedirect.com/science/article/abs/pii/S0140700715003801

### Tier 3 — Patents

Useful for architecture/history/design intent; not independent performance validation.

### Tier 4 — Company/marketing material

Useful for current Solar Polar technology descriptions and product direction.

Official:
https://www.solar-polar.co.uk/solar-cooling

---

## 27. Claude Handoff Instructions

Claude should treat this report as a **benchmark/research document**, not as an approved design update.

When continuing the project:

1. Preserve the project **HOLD** status.
2. Do not replace Clay design values with Solar Polar values.
3. Do not infer pressure, temperature, material, relief or fabrication requirements from Solar Polar.
4. Add Solar Polar as an external benchmark.
5. Keep OQ-0 architecture selection explicitly OPEN.
6. Independently audit COP = 0.424.
7. Prioritize E-102 condenser validation.
8. Prioritize V-102 absorber heat/mass-transfer validation.
9. Continue D-007 independent NH3-H2O property validation.
10. Build a daily/hourly solar performance model before claiming solar-duty performance.
11. Distinguish experimental data from model outputs and company claims.
12. Record source year, DOI/URL, evidence class, applicability and uncertainty for every imported benchmark value.
13. Do not use social-media comments as engineering evidence.
14. Do not treat a benchmark as design approval.

---

## 28. Final Engineering Judgment

The Solar Polar investigation does **not** tell us to abandon the Clay refrigerator.

It gives us something more useful:

**an external, experimentally grounded architecture against which the Clay design can be challenged.**

The strongest current conclusions are:

- **200 W-class solar absorption refrigeration is credible at the technology scale.**
- **DAR is a legitimate alternative architecture.**
- **DAR's experimental COP is materially below the current Clay modeled COP.**
- **DAR startup is a major problem.**
- **DAR source temperature can become a major constraint.**
- **Hot-ambient condenser rejection is a major risk.**
- **The Clay two-fluid architecture may avoid the DAR bubble-pump startup bottleneck.**
- **The Clay COP = 0.424 therefore deserves a hard independent audit.**
- **The Clay 135 °C generator target must be justified by the two-fluid cycle itself.**
- **E-102 and V-102 should receive increased validation priority.**
- **Daily solar performance matters more than steady-state COP alone.**
- **Solar Polar is a benchmark, not a blueprint.**

### Current status

**HOLD — NOT RELEASED FOR FABRICATION, PRESSURE TESTING, AMMONIA CHARGING, OR OPERATION.**

No conclusion in this report changes that status.

---

## 29. Short Claude Summary

> Solar Polar is now a formal external benchmark for the Clay solar absorption refrigerator. Its strongest evidence comes from Imperial/Solar Polar experimental and 2024 modelling work on NH3-H2O-H2 diffusion-absorption refrigeration. The benchmark demonstrates small-scale solar/DAR feasibility but also exposes startup delays, high source-temperature requirements, condenser/ambient coupling, transient losses and modest experimental COP (~0.25-0.26). These findings do not invalidate the Clay two-fluid NH3-H2O architecture or its 135 °C generator target because the Clay system does not use a DAR bubble pump. They do require a rigorous independent audit of COP=0.424, stronger E-102 condenser validation, stronger V-102 absorber heat/mass-transfer validation, and an explicit A/B/C architecture comparison. Solar Polar does not close any of the 20 formal DB/D gaps. Approximately seven gaps are materially better informed. OQ-0 architecture selection is now a major benchmarkable engineering decision. Project remains HOLD.
