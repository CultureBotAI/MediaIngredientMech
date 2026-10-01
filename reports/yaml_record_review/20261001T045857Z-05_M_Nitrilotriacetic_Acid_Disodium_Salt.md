# YAML Record Review: 0.5 M Nitrilotriacetic acid, disodium salt

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/05_M_Nitrilotriacetic_Acid_Disodium_Salt.yaml`
- Started UTC: 2026-10-01T04:58:57Z
- Finished UTC: 2026-10-01T04:58:58Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/05_M_Nitrilotriacetic_Acid_Disodium_Salt.yaml`
- Identifier: `kgmicrobe.ingredient:05_m_nitrilotriacetic_acid_disodium_salt`
- Preferred term: 0.5 M Nitrilotriacetic acid, disodium salt
- Mapping status: `MAPPED`
- Ingredient type: `STOCK_SOLUTION`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/05_M_Nitrilotriacetic_Acid_Disodium_Salt.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `kgmicrobe.ingredient:05_m_nitrilotriacetic_acid_disodium_salt`.
- Ontology label: `0.5 M Nitrilotriacetic acid, disodium salt`.
- Mapping quality: `FALLBACK_REGISTRY`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/05_M_Nitrilotriacetic_Acid_Disodium_Salt.md` after the record changed from 9534e4229546828c3f4f2dd48ae759dd32aa9e6f7b8a084cd929699a98b08790 to 91eae6a773cf1630a143147a314e29f37f430a33f885e0340d08978cb58ea74f; preserved the previous blocker finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `91eae6a773cf1630a143147a314e29f37f430a33f885e0340d08978cb58ea74f`.
- Previous review: `reports/yaml_record_review/05_M_Nitrilotriacetic_Acid_Disodium_Salt.md`.
- Previous record SHA-256: `9534e4229546828c3f4f2dd48ae759dd32aa9e6f7b8a084cd929699a98b08790`.
- Source occurrence traceability: 1 occurrence(s) across 1 medium/media.
- Latest curation event: CORRECTED by mim_semantic_review_20260921 at 2026-09-21T21:33:25.379198+00:00: Separate the 0.5 M disodium stock from trisodium nitrilotriacetate. Source occurrence rows explicitly name one of each. Restore the trisodium substance as its own record, carrying its chemistry and valid synonyms; withdraw those synonyms on the stock. The stock is a local preparation with a named disodium solute, no pure-substance formula or CAS. Solvent and complete recipe are not established. Evidence: https://www.ebi.ac.uk/chebi/CHEBI:132766 ; https://www.ncbi.nlm.nih.gov/books/NBK519184/ ; ../CultureMech/output/ingredient_occurrences.tsv
- Active SSSOM state: 1 active row(s) for `MIM:05_M_Nitrilotriacetic_Acid_Disodium_Salt`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/05_M_Nitrilotriacetic_Acid_Disodium_Salt.md` after the record changed from 9534e4229546828c3f4f2dd48ae759dd32aa9e6f7b8a084cd929699a98b08790 to 91eae6a773cf1630a143147a314e29f37f430a33f885e0340d08978cb58ea74f; preserved the previous blocker finding floor pending targeted retirement.

## Findings

- **blocker**: The previous finding set in `reports/yaml_record_review/05_M_Nitrilotriacetic_Acid_Disodium_Salt.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: 0.5 M disodium stock label is exactly mapped to a trisodium ChEBI salt and publishes trisodium synonyms/chemistry.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/05_M_Nitrilotriacetic_Acid_Disodium_Salt.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/05_M_Nitrilotriacetic_Acid_Disodium_Salt.yaml`, `just validate-terms data/ingredients/mapped/05_M_Nitrilotriacetic_Acid_Disodium_Salt.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/05_M_Nitrilotriacetic_Acid_Disodium_Salt.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/05_M_Nitrilotriacetic_Acid_Disodium_Salt.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
