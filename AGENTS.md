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

Passing software tests does not establish physical validation.

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
