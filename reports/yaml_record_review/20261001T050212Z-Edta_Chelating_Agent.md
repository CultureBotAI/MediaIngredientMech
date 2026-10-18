# YAML Record Review: EDTA (chelating agent)

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Edta_Chelating_Agent.yaml`
- Started UTC: 2026-10-01T05:02:12Z
- Finished UTC: 2026-10-01T05:02:13Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Edta_Chelating_Agent.yaml`
- Identifier: `NCIT:C360`
- Preferred term: EDTA (chelating agent)
- Mapping status: `REJECTED`
- Ingredient type: `<missing>`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Edta_Chelating_Agent.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `REJECTED`.
- Ontology ID: `NCIT:C360`.
- Ontology label: `Chelating Agent`.
- Mapping quality: `LEXICAL_MATCH`.
- Active SSSOM rows for this subject: 0.
- Identity judgement: Refreshed `reports/yaml_record_review/Edta_Chelating_Agent.md` after the record changed from 7fe6440002acca66be63af7bccb2a4e1c955511e5da0b044de2238097004d1c0 to 85c00a1b83b9f31e8bd04b3ee56ee4b487aab3c0e18a5c0302b46b04bfee175f; preserved the previous blocker finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `85c00a1b83b9f31e8bd04b3ee56ee4b487aab3c0e18a5c0302b46b04bfee175f`.
- Previous review: `reports/yaml_record_review/Edta_Chelating_Agent.md`.
- Previous record SHA-256: `7fe6440002acca66be63af7bccb2a4e1c955511e5da0b044de2238097004d1c0`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: MERGED_INTO by mim_semantic_review_20260921 at 2026-09-21T21:33:25.379198+00:00: Merged into CHEBI:4735 (EDTA). The source explicitly names EDTA; the parenthetical function does not turn the substance into the generic class of chelators. Original fields remain only on this excluded tombstone. Evidence: https://www.ebi.ac.uk/chebi/CHEBI:4735
- Active SSSOM state: No active row for `MIM:Edta_Chelating_Agent`, as expected for `REJECTED`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/Edta_Chelating_Agent.md` after the record changed from 7fe6440002acca66be63af7bccb2a4e1c955511e5da0b044de2238097004d1c0 to 85c00a1b83b9f31e8bd04b3ee56ee4b487aab3c0e18a5c0302b46b04bfee175f; preserved the previous blocker finding floor pending targeted retirement.

## Findings

- **blocker**: The previous finding set in `reports/yaml_record_review/Edta_Chelating_Agent.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The record exact-maps an EDTA-specific label to generic NCIT:C360 Chelating Agent.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/Edta_Chelating_Agent.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Edta_Chelating_Agent.yaml`, `just validate-terms data/ingredients/mapped/Edta_Chelating_Agent.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Edta_Chelating_Agent.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Edta_Chelating_Agent.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
