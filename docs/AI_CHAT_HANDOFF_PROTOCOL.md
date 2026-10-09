# AI Chat Handoff Protocol

Purpose: maintain accurate project continuity across ChatGPT windows and other assistants. This file is a protocol; it does not automatically inject instructions into every new chat.

## Mandatory startup checklist

Every AI assistant/window must, before project-specific analysis or edits:

1. Read [AGENTS.md](../AGENTS.md).
2. Read [canonical project graph](../claude/PROJECT_GRAPH.json).
3. Read [Decision Register](DECISION_REGISTER.md), [Design Basis](DESIGN_BASIS.md), and [Build Release Gate](BUILD_RELEASE_GATE.md) for formal status and open engineering items.
4. Read this handoff protocol.
5. Verify current branch, commit, and working tree when local access exists. State what was actually read; disclose inaccessible sources.

For a fresh ChatGPT window, Clay should provide this file URL and explicitly ask it to read the protocol and canonical graph. A repository note cannot guarantee that every chat automatically reads it. Baton Pass may transport the note/context, but the receiver must verify against GitHub.

## Authority and engineering rules

- GitHub is the canonical technical record.
- `claude/PROJECT_GRAPH.json` is the canonical structured project-state graph. Alternate copies are historical only unless reconciled.
- Formal release status and open items are governed by the Decision Register, Design Basis, and Build Release Gate.
- Current status: **HOLD** — not approved for fabrication, pressure testing, ammonia charging, or operation.
- Do not invent values or silently resolve conflicts. Label evidence as model output, software test, property/VLE validation, CFD validation, literature comparison, experimental validation, or engineering/code approval as applicable.
- Zero energy-balance residuals and passing software tests do not prove physical validity.
- Do not overwrite untracked work or use destructive cleanup/reset commands without explicit review and permission.

## Required end-of-session handoff

Update the **Current handoff** or add a dated entry to the **Handoff log** after meaningful work. Record:
- date and assistant/tool, if known;
- repository, branch, exact commit and working-tree state;
- files changed and commit/PR;
- commands actually run and results;
- evidence classification and limitations;
- open blockers;
- exact next action;
- what the next assistant must verify.

Never claim a change is committed or a test passed without checking the commit or actual output.

## Baton Pass experiment

Status: **NOT TESTED**. This chat has not invoked or verified the connector.

1. In a sending ChatGPT window, use Baton Pass to pass this document URL, the canonical graph URL, the current handoff below, and a request to verify each claim against GitHub.
2. In the receiving window, ask it to report files actually read, commit, release status, A0/A1 results, one open limitation, and the next action.
3. Compare its response with this document and GitHub; record missing/stale/invented facts and access failures.
4. Mark PASS only if the receiver accurately transfers the required context and verifies current repository state. Otherwise record PARTIAL/FAIL and why.
5. Baton Pass is a transport aid, not the canonical record.

## Current handoff — 2026-10-09

Repository: https://github.com/claythe3ed/solar-absorption-fridge  
Local path: `~/projects/solar-absorption-fridge`  
Branch: `main`. At the time of the A0/A1 terminal runs, Clay reported it synchronized with `origin/main` at `28fd206`. Subsequent governance documentation commits were made directly on GitHub, latest verified here: `54b771a3700bfe0273103f44715dfccff28a3d7b`. Re-check live `main` before acting.

The local working tree contains many untracked CAD/FreeCAD files, duplicate root-level Python files, notes and OpenFOAM files. They have not been audited or committed. Preserve them; do not use `git clean`, `git reset --hard`, or blanket `git add .`.

### A0/A1 checkpoint

- Environment: `./venv`, Python 3.12.3, CoolProp 8.0.0, NumPy 2.5.3, SciPy 1.18.1, pandas 3.0.6.
- A0 ran successfully with `./venv/bin/python src/thermo/cycle_model.py`: 200 W cooling, Q_gen 471.5 W, COP 0.424, internal closure +0.00 W. Classification: **MODEL OUTPUT / UNVALIDATED**.
- A1 ran successfully with `./venv/bin/python scripts/validation/run_a1_shx_sensitivity.py`.
- eta_shx sweep 0.16, 0.30, 0.50, 0.70, 0.83 yielded COP 0.2909, 0.3157, 0.3605, 0.4242, 0.4860; Q_gen 687.47, 633.59, 554.83, 471.50, 411.56 W.
- `git diff --ignore-space-at-eol -- results/a1_shx_sensitivity/results.csv` returned no output after rerun. Earlier diff appeared to be CRLF/LF line-ending differences, not numerical changes.
- A1 classification: **SENSITIVITY STUDY / UNVALIDATED**. Internal closure is not independent physical validation.
- Open technical review: check whether the simplified SHX effectiveness formulation enforces physically appropriate heat-capacity/pinch constraints; review input provenance and the missing human-readable evidence report before calling A1 complete.
- No CSV normalization/commit was made.

### Next actions

1. Run the Baton Pass test between two ChatGPT windows and record the receiver's response.
2. Inspect the canonical SHX equations and document assumptions/limitations.
3. Audit untracked local files separately before deciding what belongs in GitHub.

### Handoff log

- **2026-10-09 — ChatGPT:** A0 and A1 reproduced in the project virtual environment. The A1 CSV diff is empty when ignoring end-of-line differences. Added this protocol and linked it from `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`, and the canonical graph. Baton Pass has not been invoked or verified.
