# YAML Record Review: Apigenin Dimethyl Ether

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Apigenin_Dimethyl_Ether.yaml`
- Started UTC: 2026-10-01T05:01:23Z
- Finished UTC: 2026-10-01T05:01:24Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Apigenin_Dimethyl_Ether.yaml`
- Identifier: `CHEBI:2769`
- Preferred term: Apigenin Dimethyl Ether
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Apigenin_Dimethyl_Ether.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:2769`.
- Ontology label: `apigenin 7,4'-dimethyl ether`.
- Mapping quality: `EXACT_MATCH`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/Apigenin_Dimethyl_Ether.md` after the record changed from fe19720fc98248fc7c7920ebcd4967cde33a788001c276faf4ed2a3e4c735a20 to 688e89dc9a35a85c841cdb462c11b2b89874de379263a486d77feb74e7b4d2f8; preserved the previous blocker finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `688e89dc9a35a85c841cdb462c11b2b89874de379263a486d77feb74e7b4d2f8`.
- Previous review: `reports/yaml_record_review/Apigenin_Dimethyl_Ether.md`.
- Previous record SHA-256: `fe19720fc98248fc7c7920ebcd4967cde33a788001c276faf4ed2a3e4c735a20`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: CORRECTED by mim_semantic_review_20260921 at 2026-09-21T21:33:25.379198+00:00: Resolve the stated Apigenin Dimethyl Ether name to the explicit ChEBI/KEGG synonym of apigenin 7,4-prime-dimethyl ether. Correct CAS 5128-44-9 differs from imported 5728-44-9, which produced unrelated benzoic-acid chemistry. Withdraw methoxymethane CHEBI:28887 and reject its synonym; replace the wrong molecular formula, structure and CID from ChEBI and PubChem. Evidence: https://www.ebi.ac.uk/chebi/CHEBI:2769 ; https://pubchem.ncbi.nlm.nih.gov/compound/5281601
- Active SSSOM state: 1 active row(s) for `MIM:Apigenin_Dimethyl_Ether`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/Apigenin_Dimethyl_Ether.md` after the record changed from fe19720fc98248fc7c7920ebcd4967cde33a788001c276faf4ed2a3e4c735a20 to 688e89dc9a35a85c841cdb462c11b2b89874de379263a486d77feb74e7b4d2f8; preserved the previous blocker finding floor pending targeted retirement.

## Findings

- **blocker**: The previous finding set in `reports/yaml_record_review/Apigenin_Dimethyl_Ether.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The record conflates the Apigenin Dimethyl Ether surface with methoxymethane and a PubChem CID for 4-(2-cyanophenyl)benzoic Acid.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/Apigenin_Dimethyl_Ether.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Apigenin_Dimethyl_Ether.yaml`, `just validate-terms data/ingredients/mapped/Apigenin_Dimethyl_Ether.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Apigenin_Dimethyl_Ether.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Apigenin_Dimethyl_Ether.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
