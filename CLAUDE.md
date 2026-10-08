# CLAUDE PROJECT INSTRUCTIONS

## Mandatory first read

Before analyzing, modifying, reviewing, testing, or describing this project,
read:

    claude/PROJECT_GRAPH.json

This is the canonical structured project-state graph.

## Engineering authority

For formal engineering status and unresolved items, consult:

    docs/DECISION_REGISTER.md
    docs/DESIGN_BASIS.md
    docs/BUILD_RELEASE_GATE.md

The project is currently HOLD.

Do not approve fabrication, pressure testing, ammonia charging, or operation.

## Evidence discipline

Do not invent missing engineering values.

When values conflict or are missing:

1. identify the conflict or gap;
2. identify the source of each value;
3. preserve the uncertainty;
4. ask the engineering question required to resolve it;
5. do not silently select a value.

Clearly distinguish calculations, software tests, property/VLE validation,
CFD validation, literature comparison, experimental validation, and
engineering/code approval.

Passing software tests does not prove physical validation.

## Change control

Before changing engineering-critical values, inspect the relevant decision,
design-basis entry, specification, calculation, CAD source, and validation
evidence.

Do not close an OPEN decision by editing a single file.

## Repository discipline

Treat GitHub/main and the canonical project graph as the current project
record.

Before making changes:

    git status
    git log -1

Prefer small, traceable commits.

Run relevant tests and validation checks after changes.

Do not overwrite or delete historical evidence merely to make files agree.

## AI limitation

Claude analysis is not engineering approval, certification, code compliance,
or professional sign-off.

When evidence is insufficient, report the gap rather than manufacturing
certainty.
