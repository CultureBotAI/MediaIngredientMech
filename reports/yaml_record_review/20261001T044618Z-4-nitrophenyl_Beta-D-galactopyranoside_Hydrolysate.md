# YAML Record Review: 4-nitrophenyl Beta-D-galactopyranoside Hydrolysate

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/unmapped/4-nitrophenyl_Beta-D-galactopyranoside_Hydrolysate.yaml`
- Started UTC: 2026-10-01T04:46:18Z
- Finished UTC: 2026-10-01T04:46:19Z
- Verdict: pass

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/unmapped/4-nitrophenyl_Beta-D-galactopyranoside_Hydrolysate.yaml`
- Identifier: `UNMAPPED_0651`
- Preferred term: 4-nitrophenyl Beta-D-galactopyranoside Hydrolysate
- Mapping status: `REJECTED`
- Ingredient type: `<missing>`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/unmapped data/ingredients/mapped/Na2-citrate.yaml data/ingredients/mapped/Nitrilotriacetic_Acid_Trisodium_Salt.yaml --out /tmp/mim_remaining_review_validation.tsv --workers 4 --quiet`; 275 files scanned and 0 ERROR rows.
- Not checked: this record has no `ontology_mapping.ontology_id`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `REJECTED`.
- Ontology ID: `None`.
- Ontology label: `None`.
- Mapping quality: `None`.
- Active SSSOM rows for this subject: 0.
- Identity judgement: Rejected tombstone is retained for provenance and is not an active mapping target.

## Evidence

- Current record SHA-256: `3433abdc800cc76ee5b5d546b03b1879f69d4147b8485970a3232cf377bb3fc9`.
- Source occurrence traceability: 0 active occurrence(s) across 0 medium/media; source rows: microbedecoder: 19.
- Latest curation event: RETIRED_NOT_AN_INGREDIENT by retire_assay_labels at 2026-08-15T00:00:00+00:00: Retired as an ingredient record (#213/#308): names the beta-galactosidase TEST outcome — 4-nitrophenol released, yellow — not a substance. MicrO models it as MICRO:0000724 'beta-galactosidase assay with PNPG'. The substrate is already a record: `4-nitrophenyl beta-D-galactopyranoside` (CHEBI:355715), and the product 4-nitrophenol is CHEBI:16836. Not mapped, because every substrate CURIE it could be grounded to is already the primary key of a live record — in MIM the identifier IS the ontology CURIE, so a mapping here would mint a duplicate rather than add coverage. No synonym is folded onto those records either: this label names a reaction or a splice, not the substance, and asserting the synonymy would make label_index resolve it to something it does not denote.
- Active SSSOM state: No active row for `MIM:4-nitrophenyl_Beta-D-galactopyranoside_Hydrolysate`, as expected for `REJECTED`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/unmapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/unmapped_ingredients.yaml`.
- Consequential unresolved item: None found.

## Findings

None found.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/unmapped/4-nitrophenyl_Beta-D-galactopyranoside_Hydrolysate.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/unmapped/4-nitrophenyl_Beta-D-galactopyranoside_Hydrolysate.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
