# Technical Reference Library

**Purpose:** maintain source-traceable, copyright-conscious technical notes for the solar-powered NH3–H2O absorption refrigerator project.

This directory contains original summaries and evidence records, not replacement copies of copyrighted publications. The original PDFs currently reside in the project owner's local `Documents/` directory and are **not included in this repository**.

## Rules for contributors and AI assistants

1. Write summaries in your own words; do not reproduce entire papers, chapters, or substantial tables.
2. Record bibliographic details and a stable publisher, DOI, or institutional URL when verified. Mark missing details `NOT YET VERIFIED`.
3. For technical claims, record the source page and equation/table/figure where possible.
4. Keep units and composition basis explicit (mole fraction versus mass fraction).
5. Distinguish measured data, authors' correlations, literature values, our calculations, and inference.
6. Preserve limitations, uncertainty, failed numerical attempts, and contradictory evidence.
7. Do not treat model consistency or agreement at a few points as independent physical validation.
8. Check each publication's license/permissions before redistributing figures, tables, or substantial text. Possessing a PDF does not establish redistribution rights.
9. Do not include local PDF copies, OCR dumps, or full-paper Markdown conversions in this public repository unless redistribution is explicitly authorized.
10. This reference library does not change the project's engineering release status: **HOLD**.

## Reference notes

| Note | Source | Current status |
|---|---|---|
| [Rizvi & Heidemann (1987)](rizvi-heidemann-1987-ammonia-water-vle.md) | *Vapor-Liquid Equilibria in the Ammonia-Water System* | Identity confirmed from extracted pages 1–3; full source/table review pending |
| [Field & Combs (2002)](field-combs-2002-aqueous-ammonia-vle.md) | *Aqueous Ammonia Vapor-Liquid Equilibria: Entropy and Temperature Dependence of Wilson Coefficients* | Identity and abstract confirmed from extracted pages 1–3; detailed review pending |
| [IAPWS G4-01 (2001)](iapws-g4-01-ammonia-water-guideline.md) | *Guideline on the IAPWS Formulation 2001 for the Thermodynamic Properties of Ammonia-Water Mixtures* | Identity and attribution permission confirmed from extracted pages 1–2; formulation review pending |

## Local source inventory

The following filenames and SHA-256 hashes were reported from the owner's local machine on 2026-10-18. The hashes identify those local files; they do not prove authenticity, publication status, or that any file is authorized for redistribution. These PDFs have not been uploaded here.

| Local PDF filename | SHA-256 |
|---|---|
| `[6] Thermophysical Properties of Ammonia-Water Mixtures.pdf` | `377b33e9d34803dcdb3cbc3d75ade53399869099bbb0c470080c8d4515b8b9af` |
| `ammonia-water-system_compress.pdf` | `bebb63b1f022bb859b0a15d1b3d00d7cc29f2e95380df9f6302f64f844782511` |
| `API-520-I.pdf` | `e82098191b24d6de47be3c76477e3481afb9738b313a091e8f9e15aa80183522` |
| `Aqueous_Ammonia_Vapor_Liquid_Equilibria.pdf` | `be172385ef4edea3e7bc395c695f424c026d4110e89c9fb4881eb0d8c1ea0a47` |
| `A simple explicit thermodynamic closure for multi-fluid simulations including complex vapor–liquid equilibria: Application to NH3 single bondH2O mixtures.pdf` | `830492909e2f561205ecce65a179b06bcc0a56550bdd384893d4d474ff0f92c4` |
| `ASME-BPVC-Section-VIII.pdf` | `65b8082031ebf72d921a95fd2a89a6a5a05823caceb1d37fa46cc8aec5fdcf07` |
| `Asme-IX-2019-www.fouladline.com.pdf` | `a64e6759d70e3e32d586b8a61d894cb6a8b02995c2efb8b06311d6be91ab7b0d` |
| `fundamentals-of-heat-and-mass-transfer-incropera.pdf` | `8b004226b346fb8f867f543c2418985d22518ba5fb5baa3ef6b6569f2cce5933` |
| `G4-01: Guideline on the IAPWS Formulation 2001 for the Thermodynamic Properties of Ammonia-Water Mixtures.pdf` | `d26207452b834ad39c6be5e7f467baa2a526118a8fcf2c446b730a05e5a66a65` |
| `Heat integration of ammonia-water absorption refrigeration system through heat-exchanger network analysis.pdf` | `9cb36d72b7d07efa3bb2c85c9b276e0c14fa266b34174576502828604d088813` |
| `m112content.pdf` | `440eb31d71c7de6adca9e1a2bccc7652c8ad183fc831d8becd2cfc3a4865ba48` |
| `ModelingandAnalysisofanAmmonia-waterAbsorptionRefrigerationSystemUtilizingWasteHeatwithLargeTemperatureSpan.pdf` | `ded435a3b17b6b78a227e449a961680b79c077d2331f64fb535c24fbb4b60037` |
| `Simulation of an ammonia-water absorption cycle using exchanger effectiveness.pdf` | `6f442e7c1530cac880b2823bea43b2edc30105385c04972c7a44e50546127978` |
| `sustainability-11-03346.pdf` | `45608ddb3888c7f3189ae0288d12ea233294511e0e3b0d32ae4ecac0ab87542f` |

## Next review sequence

1. Verify full bibliographic identities and publisher/DOI links for the three priority VLE sources.
2. Inspect the exact experimental points and data tables used by the existing teqp comparison.
3. Record composition basis, temperature, pressure, reported uncertainties, solver settings, residuals, and failed attempts.
4. Review the remaining sources one by one and create notes only where their actual contents have been inspected.
5. Update the canonical project graph and handoff protocol after the notes have been checked against the local PDFs.

**Important:** these initial notes are based only on the opening pages extracted in the current review. They are deliberately marked incomplete and must not be cited as a completed full-paper review.
