# YAML Record Review: 4-Methyl-2-oxopentanoic acid sodium salt

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/4-Methyl-2-oxopentanoic_Acid_Sodium_Salt.yaml`
- Started UTC: 2026-10-01T05:01:06Z
- Finished UTC: 2026-10-01T05:01:07Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/4-Methyl-2-oxopentanoic_Acid_Sodium_Salt.yaml`
- Identifier: `cas:4502-00-5`
- Preferred term: 4-Methyl-2-oxopentanoic acid sodium salt
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/4-Methyl-2-oxopentanoic_Acid_Sodium_Salt.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:48430`.
- Ontology label: `4-methyl-2-oxopentanoic acid`.
- Mapping quality: `NARROW_MATCH`.
- Active SSSOM rows for this subject: 3.
- Identity judgement: Refreshed `reports/yaml_record_review/4-Methyl-2-oxopentanoic_Acid_Sodium_Salt.md` after the record changed from 92f14fe20e0800055755f55293278dcf53f0b241726501d65235ed8e12d192a6 to 8d5da3b1c891a79adf823a2ea778b04ef2658cc6bc175469631251c3874a314b; preserved the previous major finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `8d5da3b1c891a79adf823a2ea778b04ef2658cc6bc175469631251c3874a314b`.
- Previous review: `reports/yaml_record_review/4-Methyl-2-oxopentanoic_Acid_Sodium_Salt.md`.
- Previous record SHA-256: `92f14fe20e0800055755f55293278dcf53f0b241726501d65235ed8e12d192a6`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: REJECTED_PARENT_NAME_SYNONYMS by claude at 2026-09-22T20:41:14.285965+00:00: Retyped names of the parent compound or of a different hydrate as provenance-only REJECTED_LABEL, because this record is a distinct salt, hydrate or tombstone form and the label index resolved the parent's name here (#232): '4-Methyl-2-oxopentanoate'. Preserved original text and source metadata. No identity, mapping, role, or remaining-synonym claim was adjudicated.
- Active SSSOM state: 3 active row(s) for `MIM:4-Methyl-2-oxopentanoic_Acid_Sodium_Salt`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/4-Methyl-2-oxopentanoic_Acid_Sodium_Salt.md` after the record changed from 92f14fe20e0800055755f55293278dcf53f0b241726501d65235ed8e12d192a6 to 8d5da3b1c891a79adf823a2ea778b04ef2658cc6bc175469631251c3874a314b; preserved the previous major finding floor pending targeted retirement.

## Findings

- **major**: The previous finding set in `reports/yaml_record_review/4-Methyl-2-oxopentanoic_Acid_Sodium_Salt.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The sodium-salt identity and registry rows are coherent, but the record exports neutral-acid and anion labels as labels of the sodium salt.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/4-Methyl-2-oxopentanoic_Acid_Sodium_Salt.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/4-Methyl-2-oxopentanoic_Acid_Sodium_Salt.yaml`, `just validate-terms data/ingredients/mapped/4-Methyl-2-oxopentanoic_Acid_Sodium_Salt.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/4-Methyl-2-oxopentanoic_Acid_Sodium_Salt.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/4-Methyl-2-oxopentanoic_Acid_Sodium_Salt.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
