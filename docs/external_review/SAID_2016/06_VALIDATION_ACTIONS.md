# Validation actions derived from Said et al. (2016)

## Priority P0 — thermodynamic model

### SAID-A01 — COP boundary extraction
Locate and document the paper's exact COP definition and the measured heat-input boundary.

**Required output:** equation, measurement points, units, uncertainty treatment, and exact meaning of generator inlet temperature.

### SAID-A02 — Rectification representation
Determine whether Clay needs an explicit rectifier/dephlegmator model or a validated equivalent separation assumption.

**Required output:** water carryover relation and refrigerant vapor composition sensitivity.

### SAID-A03 — Refrigerant-side mass flow
Extract the reference system's method of controlling/measuring refrigerant mass flow.

**Required output:** reproducible measurement/control description.

### SAID-A04 — Solution circulation
Compare the paper's pumped continuous architecture with Clay's current architecture decision.

**Required output:** resolved OQ-0 decision and mass-flow path.

## Priority P1 — component/performance validation

### SAID-B01 — Heat rejection
Use the paper's 23/25/30/45 °C condenser/absorber inlet points as external evidence for performance sensitivity.

Do not substitute them for Khartoum-specific hourly heat-rejection analysis.

### SAID-B02 — Sub-zero performance
Use the −2, −4, −5 and −7 °C operating points as benchmarks for a controlled model sensitivity sweep.

Clay's −15 °C target remains outside these demonstrated operating points and requires independent evidence.

### SAID-B03 — Solar thermal integration
Compare Clay's CPC concept against the paper's evacuated tubular CPC field in terms of generator temperature, available thermal power, heat-transfer loop and control.

Do not assume collector equivalence.

## Priority P2 — experimental planning

If a prototype is eventually authorized, mirror the reference paper's useful measurement categories where practical:

- generator inlet temperature;
- condenser/absorber inlet temperature;
- evaporator outlet temperature;
- cooling capacity;
- generator heat input;
- solution flow;
- refrigerant flow;
- relevant pressures;
- component inlet/outlet temperatures;
- ambient/solar irradiance;
- pump and auxiliary electrical power;
- stable-operation duration;
- uncertainty.

## Evidence classification

Until independently reproduced:

- Paper COP values = **EXTERNAL EXPERIMENTAL EVIDENCE**
- Clay COP = 0.424 = **MODEL OUTPUT / PLAUSIBLE / UNVALIDATED**
- Any direct correction of Clay COP using Said data = **INFERENCE**, not validation.
- Pressure/material/relief conclusions from Said = **NOT ESTABLISHED**.

## Release impact

This paper does not remove the project's HOLD.

It should instead raise the quality of the validation plan and tighten the architecture audit.
