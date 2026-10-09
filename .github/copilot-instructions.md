# GitHub Copilot Project Instructions

## Mandatory first read

Before analyzing, modifying, reviewing, testing, or describing this project,
read:

    claude/PROJECT_GRAPH.json

This is the canonical structured project-state graph.

Do not use alternate PROJECT_GRAPH files as current state.

## Formal engineering governance

For formal status and unresolved engineering requirements, consult:

    docs/DECISION_REGISTER.md
    docs/DESIGN_BASIS.md
    docs/BUILD_RELEASE_GATE.md

Current project status is:

    HOLD

The project is not approved for fabrication, pressure testing, ammonia
charging, or operation.

## Engineering evidence rules

Do not invent missing engineering values.

For conflicting or missing values:

- identify the conflict;
- identify the source of each value;
- preserve uncertainty;
- ask the question needed to resolve it;
- never silently choose a value.

Distinguish calculations, software/input validation, property/VLE validation,
CFD validation, literature comparison, experimental validation, and
engineering/code approval.

Passing automated tests does not establish physical validation.

## Change control

Before changing engineering-critical values, inspect the relevant decision
register, design basis, component specification, calculation/model, CAD
source, and validation evidence.

Never close an OPEN engineering decision merely by editing code or
documentation.

## Repository discipline

Before modifying files, inspect:

    git status
    git log -1

Prefer minimal, traceable changes.

Run relevant tests after modifications.

Preserve unresolved engineering conflicts and historical evidence.

## AI limitation

Copilot-generated code, analysis, or recommendations are not engineering
approval, certification, code compliance, or professional sign-off.

When evidence is insufficient, record the gap rather than manufacturing
certainty.

## Cross-chat continuity

Before each work session, read `docs/AI_CHAT_HANDOFF_PROTOCOL.md` as well as the canonical project graph and formal governance files. At the end of meaningful work, update the handoff with verified repository revision, actual commands/results, limitations, open blockers, and next action. Baton Pass is only a context-transfer aid; verify claims against GitHub. A new ChatGPT window is not guaranteed to read repository instructions automatically, so provide the handoff URL explicitly.
