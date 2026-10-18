# YAML Record Review: MEM alpha Modification

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/unmapped/MEM_Alpha_Modification.yaml`
- Started UTC: 2026-10-01T04:48:48Z
- Finished UTC: 2026-10-01T04:48:49Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/unmapped/MEM_Alpha_Modification.yaml`
- Identifier: `UNMAPPED_0437`
- Preferred term: MEM alpha Modification
- Mapping status: `UNMAPPED`
- Ingredient type: `NAMED_MEDIUM`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/unmapped data/ingredients/mapped/Na2-citrate.yaml data/ingredients/mapped/Nitrilotriacetic_Acid_Trisodium_Salt.yaml --out /tmp/mim_remaining_review_validation.tsv --workers 4 --quiet`; 275 files scanned and 0 ERROR rows.
- Not checked: this record has no `ontology_mapping.ontology_id`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `UNMAPPED`.
- Ontology ID: `None`.
- Ontology label: `None`.
- Mapping quality: `None`.
- Active SSSOM rows for this subject: 0.
- Identity judgement: Named medium/formulation is intentionally left unmapped until a recipe-level CultureMech representation owns the formulation.

## Evidence

- Current record SHA-256: `53bef2ebf4a08858099277f59554eb8d7563fc00ccc4415399f2b68294ed5008`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: ADDED_SYNONYMS by claude_culturemech_alias_backfill at 2026-08-30T06:20:04.233651+00:00: Added 1 CultureMech recipe surface form(s) that folded onto this record's published label but were absent from MIM's label index, so CultureMech could not resolve them: 'MEM alpha Modification (BioWest)' (x1 CultureMech mentions). Source: culturemech:output/ingredient_occurrences.tsv.
- Active SSSOM state: No active row for `MIM:MEM_Alpha_Modification`, as expected for `UNMAPPED`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/unmapped_ingredients.yaml`.
- The 2026-09-01 unmapped review explains the residual unmapped policy: named media, undefined mixtures, and exact single-ingredient residuals must stay unmapped until exact same-form evidence is available.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/unmapped_ingredients.yaml`.
- Consequential unresolved item: Named medium/formulation is intentionally left unmapped until a recipe-level CultureMech representation owns the formulation.

## Findings

- **major**: `data/ingredients/unmapped/MEM_Alpha_Modification.yaml` remains `UNMAPPED`; the label denotes a named medium or formulation rather than one exact chemical substance. Do not exact-match it to a broader parent, component, hydrate, salt, or lookalike label.

## Recommended Edits

- Curate an exact same-form identity or decomposition for `data/ingredients/unmapped/MEM_Alpha_Modification.yaml` before mapping it.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/unmapped/MEM_Alpha_Modification.yaml`, `just validate-terms data/ingredients/unmapped/MEM_Alpha_Modification.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/unmapped/MEM_Alpha_Modification.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/unmapped/MEM_Alpha_Modification.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
