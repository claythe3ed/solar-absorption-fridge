# Architecture and flow-path reconstruction

## 1. High-level cycle

The paper describes a continuous pumped NH3/H2O absorption chiller with solar thermal generator heat.

Conceptual sequence:

**Generator → dephlegmator/rectification → condenser → refrigerant heat exchanger → expansion → evaporator → refrigerant heat exchanger → absorber → solution pump → solution heat exchanger/dephlegmator branch → generator**

The strong/weak solution loop is coupled to the refrigerant loop at the absorber and generator.

## 2. Generator / rectification concept

The paper's compact generator assembly is a critical architectural reference for the Clay audit.

Bottom:
- solar-heated water passes through concentric heating coils;
- heat is transferred into the NH3/H2O solution.

Middle:
- heat-recovery coils exchange heat between hot weak solution and incoming/preheated strong solution.

Top:
- strong-solution distributor;
- rectification zone with stainless-steel packing;
- rising NH3/H2O vapor contacts colder strong solution;
- water-rich condensate and some ammonia return;
- ammonia-rich vapor exits toward the condenser.

## 3. Why this matters to Clay

Clay's current cycle model calculates a generator vapor composition but does not yet demonstrate a physical rectifier/dephlegmator or a water-carryover model equivalent to the paper's architecture.

This creates a direct THERMO-AUDIT-01 question:

> Is Clay's predicted refrigerant stream composition and condenser duty physically consistent with the absence/presence of an explicit rectification stage?

This should be answered before treating COP = 0.424 as validated.

## 4. Refrigerant-side controls

The paper reports two alternating refrigerant expansion valves controlled to regulate ammonia mass flow and low pressure.

Clay should not copy this hardware arrangement automatically. Instead, it is evidence that the reference experimental system required active control of refrigerant flow/pressure to maintain its operating point.

## 5. Solution-side circulation

The reference system uses a diaphragm solution pump. The paper therefore supports the proposition that a continuous two-fluid architecture normally needs a defined solution-circulation mechanism and control strategy.

For Clay, this is especially important because the current project graph still contains an unresolved OQ-0 around continuous pumped operation versus intermittent/batch and other architectures.

## 6. Heat rejection

The paper deliberately varies the condenser/absorber inlet temperature using the heat-rejection fans. This is valuable for the Sudan/Khartoum audit because it demonstrates that heat rejection temperature is a direct performance variable rather than merely a fixed ambient input.

## 7. Storage architecture

The full solar installation uses both ice storage and cold-water storage. This is separate from the absorption cycle itself.

The paper's storage system should be treated as a benchmark for solar availability mismatch, not as a requirement for the Clay 200 W refrigerator.

## 8. Reconstructed architecture diagram

See `drawings/said2016_architecture.svg` and `drawings/said2016_generator_rectification.svg`.

These are original engineering schematics created from the textual description in the paper. They are not reproductions of the published figures.
