# Rizvi & Heidemann (1987) — Ammonia–Water VLE

**Review status:** PARTIAL — opening pages inspected only; complete paper and relevant tables not yet reviewed.  
**Use status:** candidate primary experimental source; do not use this note alone to validate the project's model.

## Bibliographic record

- **Title:** “Vapor-Liquid Equilibria in the Ammonia-Water System”
- **Authors:** Syed S. H. Rizvi and Robert A. Heidemann
- **Publication:** *Journal of Chemical and Engineering Data*
- **Year / volume / pages:** 1987, volume 32, pages 183–191
- **DOI / stable publisher URL:** NOT YET VERIFIED
- **Local source filename:** `Documents/ammonia-water-system_compress.pdf`
- **Local SHA-256 reported by owner:** `bebb63b1f022bb859b0a15d1b3d00d7cc29f2e95380df9f6302f64f844782511`
- **Public PDF:** not included in this repository.

## What the inspected opening pages establish

The abstract describes isothermal vapor–liquid equilibrium measurements for the ammonia–water system from 306 K to 618 K and pressures up to 22 MPa. The authors state that equilibrium temperature, pressure, and liquid- and vapor-phase compositions were measured, with measurements extending into critical regions of phase envelopes.

The methods discussion describes high-purity ammonia and distilled, degassed water, stainless-steel equilibrium cells, and chromatographic composition measurements. The authors also discuss known difficulties in older literature, including uncertainty in measuring the water content of vapor and potential sampling/condensation errors.

These are descriptions from the opening pages only. The actual point-by-point tables, units, uncertainty entries, and data selection criteria have not yet been reviewed in this project note.

## Relevance to this project

This paper is a candidate experimental source for checking NH3–H2O vapor–liquid equilibrium predictions. The project must use the paper's actual reported data and keep the following explicit:

- measured temperature and pressure;
- liquid composition and vapor composition;
- whether each composition is mole fraction or mass fraction;
- point identifiers and table/page location;
- reported experimental uncertainty, if provided;
- model inputs, initial guesses, convergence criteria, solver status, and residual definitions.

The existing project's preliminary seven-point teqp comparison is reported in `AGENTS.md` as five accepted results and two `notfinite_step` failures. Those preliminary figures are not independently reproduced by this note. They must not be presented as complete EOS validation.

## Evidence still required

- Inspect the full paper's relevant experimental tables and table notes.
- Confirm the exact seven points used in the current comparison against the original source.
- Verify whether the comparison's input values and composition basis were transcribed correctly.
- Record all seven attempts, including failed solver runs, settings, and residuals.
- Verify the DOI or publisher record before adding a permanent external citation.

## Copyright and reuse

This file is an original summary and bibliographic record, not a transcription of the paper. Do not add a full OCR dump, reproduce substantial tables, or upload the source PDF without confirming redistribution rights. Short factual references to individual measurements may be recorded when necessary for reproducibility, with precise attribution and context.

## Source inspection log

- **2026-10-18:** Owner-provided extraction of PDF pages 1–3 reviewed in the conversation. Full paper not reviewed.
