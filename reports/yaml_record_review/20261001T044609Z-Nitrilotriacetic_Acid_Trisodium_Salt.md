# YAML Record Review: Nitrilotriacetic acid, trisodium salt

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Nitrilotriacetic_Acid_Trisodium_Salt.yaml`
- Started UTC: 2026-10-01T04:46:09Z
- Finished UTC: 2026-10-01T04:46:10Z
- Verdict: pass

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Nitrilotriacetic_Acid_Trisodium_Salt.yaml`
- Identifier: `CHEBI:132766`
- Preferred term: Nitrilotriacetic acid, trisodium salt
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/unmapped data/ingredients/mapped/Na2-citrate.yaml data/ingredients/mapped/Nitrilotriacetic_Acid_Trisodium_Salt.yaml --out /tmp/mim_remaining_review_validation.tsv --workers 4 --quiet`; 275 files scanned and 0 ERROR rows.
- Passed: `just validate-terms data/ingredients/mapped/Nitrilotriacetic_Acid_Trisodium_Salt.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:132766`.
- Ontology label: `sodium nitrilotriacetate`.
- Mapping quality: `EXACT_MATCH`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Restored trisodium nitrilotriacetate identity, CHEBI exact mapping, chemistry, synonyms, and singleton occurrence pass.

## Evidence

- Current record SHA-256: `c68bf8109946d2a5ccd474860657d19663520960f962b9845de82b269940a137`.
- Source occurrence traceability: 1 occurrence(s) across 1 medium/media.
- Latest curation event: RESTORED_DISTINCT_SUBSTANCE by mim_semantic_review_20260921 at 2026-09-21T21:33:25.379198+00:00: Separate the 0.5 M disodium stock from trisodium nitrilotriacetate. Source occurrence rows explicitly name one of each. Restore the trisodium substance as its own record, carrying its chemistry and valid synonyms; withdraw those synonyms on the stock. The stock is a local preparation with a named disodium solute, no pure-substance formula or CAS. Solvent and complete recipe are not established. Evidence: https://www.ebi.ac.uk/chebi/CHEBI:132766 ; https://www.ncbi.nlm.nih.gov/books/NBK519184/ ; ../CultureMech/output/ingredient_occurrences.tsv
- Active SSSOM state: 1 active row(s) for `MIM:Nitrilotriacetic_Acid_Trisodium_Salt`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- `reports/sssom_completion_20260921/mapping_review/issue-intersections.json` records why the trisodium salt had to be restored as a distinct CHEBI identity instead of sharing the 0.5 M disodium-stock record.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: None found.

## Findings

None found.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Nitrilotriacetic_Acid_Trisodium_Salt.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Nitrilotriacetic_Acid_Trisodium_Salt.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
