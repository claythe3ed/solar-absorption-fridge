# Owner Requirement and Architecture Options — Provisional

**Recorded:** 2026-10-22
**Status:** Owner requirement captured; architecture selection **OPEN**. This record is not engineering approval.
**Project disposition:** **HOLD** — not approved for fabrication, pressure testing, ammonia charging, or operation.

## 1. Owner's stated need

The project is intended to provide useful refrigeration in Sudan, where power outages are a normal condition. The owner has clarified that reducing or eliminating dependence on electricity is a central design goal and has agreed that the project should first define what the cooling service must provide and what “without electricity” means in operation.

This is an owner-stated goal, not yet a complete, measurable design requirement. In particular, it is not yet clear whether it means:

- **No grid dependence:** electrical loads are permitted if supplied independently by dedicated solar-electric generation and storage; or
- **No operational electricity:** the refrigerator must provide its required service with no electrically powered pump, fan, control, or other operating load.

Until the owner clarifies this boundary, do not describe either interpretation as the finalized requirement.

## 2. Provisional architecture study order

**Study Plan B first:** three-fluid ammonia–water–hydrogen diffusion-absorption refrigeration (DAR), because its thermally driven bubble-pump circulation is the repository's closest candidate for reducing reliance on conventional electrically driven solution circulation.

Keep the other options as separate alternatives for comparison:

- **Plan A:** continuous two-fluid ammonia–water absorption with a solution pump.
- **Plan C:** intermittent/batch two-fluid ammonia–water absorption, potentially paired with cold or ice storage.

This is a prioritization for further research, not a selected architecture. Plan B must not be called fully passive, electricity-free in all configurations, safe, or suitable for the required Sudan service without evidence. It introduces a different three-fluid cycle and different component, operating, and safety questions. Do not combine assumptions from A, B, and C into a hybrid unless later evidence justifies that design.

## 3. Evidence and limitations

The repository's [Solar Polar / Imperial benchmark review](BENCHMARK-01_SOLAR_POLAR_EXTERNAL_REVIEW.md) describes experimental NH₃–H₂O–H₂ DAR evidence and explicitly distinguishes it from the current two-fluid model. The cited 2019 experiment reports a nominal 100 W unit, measured cooling output of 24–108 W, and COP of 0.11–0.26. A 2024 calibrated solar-DAR study reports a potentially long bubble-pump startup period under a studied low-heat-input condition. These results are evidence that DAR has been studied experimentally; they do not demonstrate that Plan B can meet this project's nominal 200 W target, cold-box service, hot-ambient conditions, or required autonomy in Sudan.

The 2019 source is Najjaran Kheirabadi, Freeman, Ramos Cabal & Markides, “Experimental evaluation of a diffusion absorption refrigeration cycle at variable heat input conditions,” *Applied Energy* 256 (2019), 113899, DOI: [10.1016/j.apenergy.2019.113899](https://doi.org/10.1016/j.apenergy.2019.113899). The 2024 calibrated-model source is Freeman & Markides, *Renewable Energy* 230 (2024), 120718, DOI: [10.1016/j.renene.2024.120718](https://doi.org/10.1016/j.renene.2024.120718). Consult the full cited papers and their exact system boundaries before using numerical results.

## 4. Requirements to clarify before the architecture comparison

1. **Use and contents:** What will be refrigerated (medicine, food, other), and what are the actual product/storage requirements?
2. **Temperature service:** Required operating temperature range, allowable excursions, and measurement/acceptance method.
3. **Cooling load:** Heat-load profile, loading/recovery events, and whether the existing 200 W target is required or only preliminary.
4. **Autonomy:** How many hours or days must the cold space remain within limits without useful solar heat or other input? What storage is acceptable?
5. **Electricity boundary:** Is dedicated PV/battery-powered operation acceptable, or must all operational electrical loads be zero? Explicitly count pumps, fans, controls, sensors, monitoring, lighting, and any other load.
6. **Operating context:** Site/location, ambient design conditions, installation constraints, maintenance capability, and seasonal expectations.

The comparison should use common service criteria and report daily useful cooling, startup/recovery, parasitic electricity, thermal input, storage behavior, heat rejection in Sudan conditions, architecture-specific pressures and materials, safety burden, complexity, and evidence maturity—not steady-state COP alone.

## 5. Governance and next action

OQ-0 remains **OPEN**. The next action is to clarify the cooling service and electricity boundary with the owner, then compare Plan B against Plans A and C using the same requirements and traceable evidence. No architecture choice or design pressure/material value is approved by this note. The repository's design basis and [Build Release Gate](BUILD_RELEASE_GATE.md) remain controlling; project HOLD status is unchanged.
