# YAML Record Review: 4-nitrophenyl beta-D-galactopyranoside

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/4-nitrophenyl_Beta-D-galactopyranoside.yaml`
- Started UTC: 2026-10-01T05:01:08Z
- Finished UTC: 2026-10-01T05:01:09Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/4-nitrophenyl_Beta-D-galactopyranoside.yaml`
- Identifier: `CHEBI:355715`
- Preferred term: 4-nitrophenyl beta-D-galactopyranoside
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/4-nitrophenyl_Beta-D-galactopyranoside.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:355715`.
- Ontology label: `4-nitrophenyl-beta-D-galactoside`.
- Mapping quality: `SYNONYM_MATCH`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/4-nitrophenyl_Beta-D-galactopyranoside.md` after the record changed from 6e2f802d56a9def864513a62f247213e10edd48445162a48a077e75441a65d77 to c2a90016b3ee718811986e5ade2e11025f2e7e3eb4ada5be9022c730842907ba; preserved the previous major finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `c2a90016b3ee718811986e5ade2e11025f2e7e3eb4ada5be9022c730842907ba`.
- Previous review: `reports/yaml_record_review/4-nitrophenyl_Beta-D-galactopyranoside.md`.
- Previous record SHA-256: `6e2f802d56a9def864513a62f247213e10edd48445162a48a077e75441a65d77`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: REJECTED_TRAIT_SYNONYMS by claude at 2026-09-22T06:14:49.563933+00:00: Retyped activity/assay phrases as provenance-only REJECTED_LABEL because they describe a process or organism trait, not an ingredient name (#703): 'degradation: 4-nitrophenyl beta-D-galactopyranoside'; 'hydrolysis: 4-nitrophenyl beta-D-galactopyranoside'. Preserved original text and source metadata. No identity, mapping, role, or remaining-synonym claim was adjudicated.
- Active SSSOM state: 1 active row(s) for `MIM:4-nitrophenyl_Beta-D-galactopyranoside`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/4-nitrophenyl_Beta-D-galactopyranoside.md` after the record changed from 6e2f802d56a9def864513a62f247213e10edd48445162a48a077e75441a65d77 to c2a90016b3ee718811986e5ade2e11025f2e7e3eb4ada5be9022c730842907ba; preserved the previous major finding floor pending targeted retirement.

## Findings

- **major**: The previous finding set in `reports/yaml_record_review/4-nitrophenyl_Beta-D-galactopyranoside.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The CHEBI beta-D-galactoside identity passes, but two action-prefixed labels are stored and exported as exact synonyms of the chemical.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/4-nitrophenyl_Beta-D-galactopyranoside.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/4-nitrophenyl_Beta-D-galactopyranoside.yaml`, `just validate-terms data/ingredients/mapped/4-nitrophenyl_Beta-D-galactopyranoside.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/4-nitrophenyl_Beta-D-galactopyranoside.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/4-nitrophenyl_Beta-D-galactopyranoside.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
