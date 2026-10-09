# AI AGENT PROJECT INSTRUCTIONS

## Project

This repository is `solar-absorption-fridge`, a solar-powered NH3-H2O
absorption refrigerator project intended for off-grid use in Sudan.

## MANDATORY CROSS-CHAT HANDOFF PROTOCOL

Every AI assistant working on this repository, including every ChatGPT window/session, MUST read:

    docs/AI_CHAT_HANDOFF_PROTOCOL.md

A fresh ChatGPT window does not necessarily load repository instructions automatically. The user or a prior handoff must provide the protocol URL and explicitly ask the assistant to read it. Do not claim automatic enforcement. At the start of work, verify the current GitHub state; at the end of meaningful work, update the handoff protocol with verified changes, test results, limitations, and the next action. Baton Pass may transport context, but it does not replace verification against the canonical repository.

## FIRST READ — CANONICAL PROJECT STATE

Before analyzing, modifying, reviewing, testing, or describing this project,
AI agents MUST read:

    claude/PROJECT_GRAPH.json

This is the canonical structured project-state graph.

Do not treat another `PROJECT_GRAPH` file as the current state unless it has
been explicitly reconciled into the canonical graph.

## FORMAL ENGINEERING GOVERNANCE

For formal project status, unresolved engineering decisions, design-basis
requirements, and fabrication/release authorization, consult:

    docs/DECISION_REGISTER.md
    docs/DESIGN_BASIS.md
    docs/BUILD_RELEASE_GATE.md

These documents take precedence over assumptions, generated drawings,
unverified analysis, or AI recommendations.

## CURRENT RELEASE STATUS

The project is currently:

    HOLD

It is NOT approved for:

- fabrication
- pressure testing
- ammonia charging
- operational use

Do not silently change this status.

## ENGINEERING EVIDENCE RULE

Do not invent missing engineering values.

When a required value is unavailable or conflicting:

1. identify the missing/conflicting value;
2. identify its source(s);
3. preserve the uncertainty;
4. ask the engineering question needed to resolve it;
5. do not silently choose a value.

AI-generated calculations and recommendations are not engineering approval,
code compliance, certification, or sign-off.

## VALIDATION RULE

Distinguish clearly between:

- model calculation;
- software/input validation;
- property/VLE validation;
- CFD validation;
- literature comparison;
- experimental validation;
- engineering/code approval.

Passing software tests does not establish physical validation. Numerical solver convergence, internal phase-equilibrium consistency, or a closed model energy balance is not by itself independent validation against experimental measurements.

## SCIENTIFIC CITATIONS AND REPRODUCIBILITY

- Cite primary literature and authoritative technical sources for thermodynamic models, correlations, experimental data, and engineering claims.
- Include authors, year, title, publication, and DOI or stable publisher/institution URL where available.
- State which equation of state or correlation is actually implemented and which source supports it. Do not describe a correlation comparison as validation of a different EOS.
- Identify experimental dataset, units, composition basis (mole fraction versus mass fraction), measured conditions, solver settings, acceptance checks, residuals, and failed attempts.
- Preserve failed and rejected solver runs in the validation record; explain whether they indicate numerical failure, an invalid state, or a demonstrated model discrepancy. Do not silently discard failures or select roots merely because they match experimental data.
- Separate numerical/internal consistency checks from independent experimental validation. Report uncertainty and applicability limits, especially where measurements or correlations have known limitations.
- Do not claim the entire EOS or cycle model is validated from a small subset of points. Do not promote preliminary comparisons into approved design values without documented review and change control.

### Key ammonia-water thermodynamic references

1. Ziegler, B. & Trepp, C. (1984). “Equation of state for ammonia-water mixtures.” *International Journal of Refrigeration*. https://doi.org/10.1016/0140-7007(84)90022-7
2. Tillner-Roth, R. & Friend, D. G. (1998). “A Helmholtz Free Energy Formulation of the Thermodynamic Properties of the Mixture {Water + Ammonia}.” *Journal of Physical and Chemical Reference Data*, 27(1), 63–96. https://doi.org/10.1063/1.556015
3. Tillner-Roth, R. & Friend, D. G. (1998). “Survey and Assessment of Available Measurements on Thermodynamic Properties of the Mixture (Water + Ammonia).” *Journal of Physical and Chemical Reference Data*. https://doi.org/10.1063/1.556014
4. Pátek, J. & Klomfar, J. (1995). “Simple functions for fast calculations of selected thermodynamic properties of the ammonia-water system.” *International Journal of Refrigeration*. https://doi.org/10.1016/0140-7007(95)00006-W
5. Mirl, N. et al. (2020). “Comparison of ammonia/water equations of state under operating conditions of absorption systems.” *Fluid Phase Equilibria*. https://doi.org/10.1016/j.fluid.2020.112748
6. Rizvi, S. S. H. & Heidemann, R. A. (1987). “Vapor-Liquid Equilibria in the Ammonia-Water System.” *Journal of Chemical & Engineering Data*, 32, 183–191. Use the original paper/table when comparing experimental VLE data; keep its reported mole fractions distinct from mass fractions.
7. Field, R. W. & Combs, M. (2002). “Aqueous Ammonia Vapor-Liquid Equilibria: Entropy and Temperature Dependence of Wilson Coefficients.” *Journal of Solution Chemistry*, 31(9). This is a literature synthesis/model paper; do not misrepresent all collated measurements as newly measured by its authors.

Additional technical documentation:
- teqp VLE algorithms: https://teqp.readthedocs.io/en/stable/algorithms/VLE.html
- NIST record for Tillner-Roth & Friend (1998) Helmholtz formulation: https://www.nist.gov/publications/helmholtz-free-energy-formulation-thermodynamic-properties-mixture-water-ammonia
- NIST record for the survey of available measurements: https://www.nist.gov/publications/survey-and-assessment-available-measurements-thermodynamic-properties-mixture-water

### Current preliminary teqp VLE comparison — not a validation claim

A preliminary comparison using `teqp.AmmoniaWaterTillnerRoth()` and seven isothermal
Rizvi & Heidemann (1987) Table IV points has so far accepted five solver results
and failed to obtain accepted solutions for two points (points 21 and 22,
`notfinite_step`). For the five accepted points, calculated temperatures were
about +2.95 to +6.91 K above the tabulated temperatures; mean temperature
residual was +4.60 K. Mean vapour NH3 mole-fraction residual was −0.00573 and
its mean absolute residual was 0.00608. The two failed attempts are numerical
failures for the tested initial guesses, not proof that the EOS is invalid.
These results are preliminary, dataset-specific, and not a complete EOS
validation. Re-run and preserve all settings/results before drawing conclusions.

The solver's pressure reproduction and equality of phase chemical potentials
are internal consistency checks using the same model, not independent evidence
of experimental accuracy. Experimental high-vapour-ammonia compositions also
require careful uncertainty interpretation. Do not use this preliminary result
to change design inputs or release status without further review.

## LOCAL WORKING LOCATIONS AND REFERENCE FILES

The current local repository path recorded in
`docs/AI_CHAT_HANDOFF_PROTOCOL.md` is:

    ~/projects/solar-absorption-fridge

On the user's Ubuntu system this has also been expressed as:

    /home/clay/projects/solar-absorption-fridge

These are two spellings of the same repository root, not two distinct
locations. Verify local filesystem state when shell access is available; a
GitHub read does not prove that the local tree is synchronized.

The canonical `claude/PROJECT_GRAPH.json` records the Revision B 13-sheet
FreeCAD TechDraw pack in two local locations:

    private/Copilot/revB-freecad/
    copilot_drowings/

Treat both as local-workspace locations documented by the project graph.
They are not present as directories in the current public GitHub tree, so do
not claim their contents were inspected from GitHub. When local access exists,
inspect both locations and reconcile their contents without overwriting or
deleting either copy. Do not assume they are identical.

Two local research PDF filenames used in the ongoing ammonia-water VLE work
are:

    ammonia-water-system_compress.pdf
    Aqueous_Ammonia_Vapor_Liquid_Equilibria.pdf

These PDFs are not tracked in the current public repository tree. Their exact
local absolute paths have not been established from GitHub; locate and verify
them in the local working tree before using or citing the files. Do not invent
paths or claim the files were inspected if they were inaccessible.

Do not overwrite, delete, stage, commit, stash, or otherwise modify local files
unless the user explicitly authorizes the relevant operation. A direct GitHub
edit does not update the user's local working tree.

## CHANGE CONTROL

Before modifying an engineering-critical value, check the relevant:

- Decision Register entry;
- Design Basis entry;
- component specification;
- calculation/model;
- drawing/CAD source;
- validation evidence.

Do not resolve an OPEN decision merely by editing one file.

## CANONICAL PATHS

Canonical structured project state:

    claude/PROJECT_GRAPH.json

Formal engineering governance:

    docs/DECISION_REGISTER.md
    docs/DESIGN_BASIS.md
    docs/BUILD_RELEASE_GATE.md

Claude-specific guidance:

    CLAUDE.md

GitHub Copilot guidance:

    .github/copilot-instructions.md

## ALTERNATE PROJECT GRAPH

`PROJECT_GRAPH(1).json` is a retained historical/non-canonical copy.

It may contain useful historical evidence, but it MUST NOT override:

    claude/PROJECT_GRAPH.json

## PROJECT PRINCIPLE

Prefer evidence over assumptions.

When evidence is insufficient, record the gap rather than manufacturing
certainty.
