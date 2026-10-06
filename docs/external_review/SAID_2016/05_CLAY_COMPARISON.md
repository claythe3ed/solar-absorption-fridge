# Controlled comparison — Said et al. (2016) vs Clay baseline

## Comparison table

| Variable | Said et al. SP-02 | Clay nominal | Interpretation |
|---|---:|---:|---|
| Working pair | NH3/H2O | NH3/H2O | Strong architecture match |
| Heat source | Solar thermal | Solar thermal | Strong match |
| Generator inlet | 140 °C | ~135 °C | Close |
| Condenser/absorber inlet | 45 °C | ~40 °C | Close |
| Evaporator outlet | −4 °C | ~−15 °C | Clay is substantially colder |
| Cooling capacity | 4.5 kW | 0.2 kW | Different scale |
| COP | 0.42 | 0.424 | Numerically close, but not equivalent proof |
| Solution circulation | Diaphragm pump | Current implementation unresolved | Major architecture gap |
| Rectification | Explicit dephlegmator/rectification | Not explicitly modeled in current cycle model | Major thermodynamic gap |
| Water carryover | Addressed physically by rectification | Not explicitly modeled | Major validation gap |
| Heat rejection | Controlled condenser/absorber inlet | Design assumption under audit | Requires local validation |
| Storage | Ice + cold-water | Cold box | Different system boundary |

## The key comparison

The strongest evidence is:

**Said SP-02:** 140 °C / 45 °C / −4 °C → 4.5 kW, COP 0.42.

**Clay nominal:** approximately 135 °C / 40 °C / −15 °C → 0.2 kW, COP 0.424.

This is encouraging because the same working pair, solar thermal drive and hot-climate heat rejection are involved.

It is not a validation because the evaporator target is much colder, the scale is different, the component architecture differs, and the paper uses an explicit rectification/dephlegmation stage and mechanical solution pump.

## Most important new benchmark

The paper's 129/25/−7 °C point gives COP 0.30. The 140/45/−4 °C point gives COP 0.42.

These points cannot be reduced to a simple one-variable temperature correction because generator temperature, heat-rejection temperature and evaporator temperature all change simultaneously.

However, they are useful for sensitivity expectations:

- heat-rejection temperature materially affects COP;
- colder evaporation can reduce COP;
- higher generator temperature can help overcome larger temperature lifts;
- the complete thermodynamic/control architecture matters.

## What this changes in THERMO-AUDIT-01

The paper strengthens the external plausibility case for a COP around 0.4 in a solar NH3/H2O continuous system.

It also strengthens the requirement to resolve:

1. OQ-0 architecture;
2. generator vapor composition;
3. rectification/water carryover;
4. condenser duty boundary;
5. absorber performance;
6. solution circulation ratio and pump work;
7. exact COP definition;
8. hot-climate heat rejection;
9. sub-zero evaporator validation.

## Do not make these claims

Do not write:

- “Said et al. validated Clay COP 0.424.”
- “The paper proves the Clay refrigerator will achieve COP 0.424.”
- “140/45/−4 is equivalent to 135/40/−15.”
- “The paper validates the Clay pressure design.”
- “The paper validates Clay's vessel, materials, relief system or CAD.”

The evidence supports only the narrower benchmark statements.
