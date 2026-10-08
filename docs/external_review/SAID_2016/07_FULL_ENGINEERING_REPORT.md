# Full Engineering Review Report
## Said et al. (2016) as an external benchmark for the Clay solar NH3/H2O refrigerator

**Project:** Solar Absorption Refrigerator — off-grid solar NH3/H2O concept for Sudan  
**External source:** Said et al. (2016), International Journal of Refrigeration 62, 222–231  
**DOI:** 10.1016/j.ijrefrig.2015.10.026  
**Review status:** External evidence integrated for audit; not design approval  
**Clay release status:** **HOLD**

---

## 1. Executive conclusion

The uploaded Said et al. paper is one of the strongest external references currently available for the Clay project.

It is unusually close to the intended system in five important ways:

1. NH3/H2O working pair.
2. Solar thermal generator.
3. Continuous mechanically pumped absorption cycle.
4. Sub-zero evaporator operation.
5. High heat-rejection-temperature testing in Saudi Arabia.

The most relevant measured point is 140 °C generator inlet, 45 °C condenser/absorber inlet, −4 °C evaporator outlet, 4.5 kW cooling and COP 0.42.

That result makes a Clay COP around 0.4 **credible enough to remain a serious engineering hypothesis**. It does not validate Clay's current COP = 0.424.

The main reason is not simply the 11 °C colder Clay evaporator. The more important issue is architecture and model fidelity: Said et al. explicitly use rectification/dephlegmation and a mechanically driven solution pump, while the current Clay model does not yet demonstrate an equivalent rectification/water-carryover model or a demonstrated circulation implementation.

Therefore:

> **The paper strengthens the plausibility case but does not close THERMO-AUDIT-01, D-007, OQ-0, or the overall release HOLD.**

---

## 2. Source identity

Said et al. report a laboratory-developed NH3/H2O absorption chiller and a Saudi Arabian demonstration plant. The article was received in 2015 and published in International Journal of Refrigeration volume 62 in 2016.

The uploaded source is the complete 10-page paper.

This repository package deliberately avoids reproducing the article verbatim. It preserves the engineering evidence needed for reproducible review and links the evidence to the primary source record.

---

## 3. Reference-system architecture

The reference chiller contains:

- generator;
- dephlegmator;
- condenser;
- evaporator;
- absorber;
- internal/external heat exchangers;
- refrigerant expansion valves;
- solution expansion valves;
- solution pump.

The paper describes continuous operation: desorption and absorption occur simultaneously, with the solution loop replacing the mechanical compressor function.

### Refrigerant path

The reference process is:

1. generator creates ammonia-rich vapor;
2. dephlegmator removes water and some ammonia;
3. nearly pure ammonia vapor enters condenser;
4. liquid ammonia passes through a refrigerant heat exchanger;
5. expansion valves regulate low-side flow/pressure;
6. evaporator produces cooling;
7. ammonia vapor returns through the refrigerant heat exchanger;
8. vapor enters absorber.

### Solution path

1. weak NH3/H2O solution leaves generator;
2. it is cooled in the solution heat exchanger;
3. it is further cooled in the absorber-pre-cooler;
4. it is expanded to low pressure;
5. it absorbs ammonia vapor;
6. strong solution leaves absorber;
7. diaphragm pump raises pressure;
8. flow is divided through heat-exchanger/dephlegmator paths;
9. preheated strong solution returns to generator.

---

## 4. Generator assembly

The generator assembly is particularly important for Clay.

The paper reports a compact integrated assembly with:

- bottom heating coils;
- middle heat-recovery coils;
- top rectification zone;
- strong-solution distributor.

Four concentric heating coils receive hot water from the solar collectors.

The rectification zone contains stainless-steel packing. The paper explains that this supports heat and mass transfer between hot ammonia/water vapor and colder strong solution.

This arrangement explicitly addresses water contamination of the ammonia refrigerant.

### Engineering implication for Clay

Clay currently computes a generator vapor ammonia fraction but does not yet demonstrate a physical rectifier/dephlegmator or a validated equivalent separation model.

This is a direct reason to keep generator vapor composition and water carryover as an open thermodynamic issue.

---

## 5. Experimental operating evidence

The paper reports four representative points:

| Point | T_gen,in | T_cond/abs,in | T_evap,out | Cooling | COP |
|---|---:|---:|---:|---:|---:|
| SP-01 | 114 °C | 23 °C | −2 °C | 10.1 kW | 0.69 |
| SP-02 | 140 °C | 45 °C | −4 °C | 4.5 kW | 0.42 |
| SP-03 | 121 °C | 30 °C | −5 °C | 4.8 kW | 0.46 |
| SP-04 | 129 °C | 25 °C | −7 °C | 4.8 kW | 0.30 |

The paper also reports a summary point around 115/23/−2 °C with 10.5 kW and COP 0.71.

The 140/45/−4 point is especially relevant because the heat-rejection temperature is high and the system still produces ice.

---

## 6. Comparison with Clay

Clay nominally targets approximately:

- generator: 135 °C;
- condenser: 40 °C;
- evaporator: −15 °C;
- cooling: 200 W;
- COP: 0.424.

### Similarities

- same NH3/H2O working pair;
- same solar-thermal concept;
- similar generator temperature;
- similar high-side heat-rejection environment;
- same general continuous absorption concept if OQ-0 resolves in favor of pumping.

### Differences

- Clay evaporator is substantially colder;
- Clay is approximately 22.5 times smaller in cooling capacity than the 4.5 kW reference point;
- reference uses explicit rectification/dephlegmation;
- reference uses a diaphragm solution pump;
- reference includes active refrigerant flow/pressure regulation;
- reference uses a different solar collector field and storage architecture;
- Clay's heat rejection is still under local environmental validation;
- Clay's pressure/material/relief basis remains open.

---

## 7. Why COP = 0.424 remains unvalidated

A numerical coincidence between Clay's 0.424 and the paper's 0.42 is not a validation.

For validation, the following must be made consistent:

1. COP numerator.
2. COP denominator.
3. Generator heat boundary.
4. Pump/auxiliary power treatment.
5. Refrigerant composition.
6. Solution concentrations.
7. Heat rejection temperature.
8. Evaporator temperature definition.
9. Steady-state criteria.
10. Measurement uncertainty.

The reference paper provides valuable experimental evidence, but the Clay model must still reproduce a controlled benchmark under comparable boundary conditions.

---

## 8. Important warning about the −15 °C target

The reference paper demonstrates −7 °C at a reported COP of 0.30 under 129/25 °C generator/heat-rejection conditions.

That does not mean COP must be 0.30 at Clay's −15 °C.

It does show that colder evaporation is not a free extrapolation.

Clay's −15 °C point should therefore be treated as an explicit extrapolation requiring model validation and sensitivity analysis.

---

## 9. Heat rejection is a first-class design variable

The reference system deliberately changes heat-rejection conditions using fan control.

Reported points show strong performance variation as condenser/absorber inlet temperature changes.

For Clay, this supports a design rule:

> Do not treat condenser/absorber temperature as a fixed secondary assumption.

For Sudan/Khartoum, hourly heat rejection should be modeled with actual ambient conditions, solar interaction, natural/forced convection assumptions, fouling/dust effects where relevant, and the final geometry.

---

## 10. Solar thermal integration

The reference plant used 14 evacuated tubular CPC-18 collectors, 42 m² total collector area and a stated maximum heating power of 20 kW at 140 °C.

This is not a direct sizing benchmark for Clay's 1.59 m² CPC.

It is useful instead as evidence that:

- solar thermal NH3/H2O absorption can operate at approximately 140 °C;
- high-temperature solar heat collection and a hydraulic heat-transfer loop are practical system-level requirements;
- storage can decouple solar availability from cooling demand.

---

## 11. Storage and operating modes

The reference installation uses ice storage and cold-water storage, each reported as 0.41 m³, with 40 kWh cold storage per tank.

Five operating modes coordinate:

- chiller ON/OFF;
- cooling demand;
- ice charging/discharging;
- cold-water charging/discharging;
- fan-coil temperature protection.

This is relevant to Clay's off-grid objective but should not be copied mechanically.

The Clay 200 W cold box can have a much smaller storage requirement, and the correct sizing should come from the actual load profile and solar resource.

---

## 12. What the paper supports

### Strongly supported

- Solar thermal NH3/H2O absorption is experimentally demonstrated.
- Continuous pumped NH3/H2O operation is experimentally demonstrated.
- Sub-zero evaporation is experimentally demonstrated.
- High heat-rejection operation is experimentally demonstrated.
- COP around 0.4 is experimentally demonstrated at 140/45/−4 °C.
- Rectification/dephlegmation is an important physical part of the reference design.
- Heat rejection materially influences performance.

### Not supported

- Clay COP = 0.424.
- Clay operation at −15 °C.
- Clay pressure-vessel design.
- Clay relief-device sizing.
- Clay wetted-material selection.
- Clay CPC geometry.
- Clay absorber area.
- Clay condenser U-value.
- Clay safety or fabrication release.

---

## 13. Required next calculations

### P0

**P0-1:** extract the exact COP equation and generator heat boundary from the paper.

**P0-2:** reproduce SP-02 in the Clay model using 140/45/−4 °C boundary conditions as closely as the source permits.

**P0-3:** determine whether Clay's current generator vapor composition can reproduce a physically plausible post-rectification refrigerant stream.

**P0-4:** add a water-carryover/rectification sensitivity model.

**P0-5:** explicitly include or bound solution-pump work.

### P1

**P1-1:** compare model predictions against SP-01 through SP-04.

**P1-2:** perform controlled sweeps in generator, heat-rejection and evaporator temperature.

**P1-3:** compare Clay's condenser/absorber heat rejection against the reference system's high-temperature tests.

**P1-4:** develop a separate −15 °C evidence case.

---

## 14. Proposed validation matrix

| Test | Reference | Clay status | Required action |
|---|---|---|---|
| 114/23/−2 | COP 0.69 | OPEN | reproduce model boundary |
| 140/45/−4 | COP 0.42 | OPEN | highest priority |
| 121/30/−5 | COP 0.46 | OPEN | controlled check |
| 129/25/−7 | COP 0.30 | OPEN | cold-evap sensitivity |
| −15 °C | no direct paper point | OPEN | independent validation |
| rectification | explicit reference architecture | OPEN | model/architecture decision |
| solution pump | explicit reference hardware | OPEN | OQ-0 decision |
| water carryover | explicitly addressed | OPEN | quantitative model |
| Khartoum heat rejection | not covered | OPEN | local hourly analysis |

---

## 15. Release and safety status

This external paper does not authorize:

- fabrication;
- pressure testing;
- ammonia charging;
- operation.

The project remains **HOLD**.

Pressure boundary, relief basis, materials compatibility, inspection, testing and jurisdictional code basis remain independent engineering tasks.

---

## 16. Recommended evidence classification

Use these labels in future model/review work:

- **SOURCE-EVIDENCE:** directly reported by Said et al.
- **MODEL-REPRODUCTION:** Clay model attempting to reproduce the paper.
- **INFERENCE:** interpretation derived from the paper.
- **UNVERIFIED:** plausible but not independently demonstrated.
- **CONFLICT:** source or project records disagree.
- **OPEN:** engineering decision or validation task not closed.

Do not convert SOURCE-EVIDENCE into VALIDATED-CLAY merely because a number is similar.

---

## 17. Final assessment

Said et al. (2016) materially improves the scientific basis of the Clay project.

The most important finding is not simply that “COP 0.42 exists.”

The important finding is that a real experimental solar NH3/H2O system in a hot Saudi environment achieved COP 0.42 at 140/45/−4 °C while using an architecture that explicitly includes rectification and mechanical solution circulation.

That gives Clay a credible external benchmark and exposes exactly where the present model needs deeper work.

**Recommendation: keep COP = 0.424 as PLAUSIBLE / UNVALIDATED; make SP-02 the first external benchmark for THERMO-AUDIT-01; resolve OQ-0 and D-007 before treating the cycle as technically mature.**
