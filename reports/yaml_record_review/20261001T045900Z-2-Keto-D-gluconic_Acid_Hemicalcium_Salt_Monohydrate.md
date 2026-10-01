# YAML Record Review: 2-Keto-D-gluconic acid hemicalcium salt monohydrate

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Monohydrate.yaml`
- Started UTC: 2026-10-01T04:59:00Z
- Finished UTC: 2026-10-01T04:59:01Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Monohydrate.yaml`
- Identifier: `kgmicrobe.compound:2-keto-d-gluconic_acid_hemicalcium_salt_monohydrate`
- Preferred term: 2-Keto-D-gluconic acid hemicalcium salt monohydrate
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Monohydrate.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:27469`.
- Ontology label: `2-dehydro-D-gluconic acid`.
- Mapping quality: `CLOSE_MATCH`.
- Active SSSOM rows for this subject: 2.
- Identity judgement: Refreshed `reports/yaml_record_review/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Monohydrate.md` after the record changed from c723754f95dc6bcb53fdbafe6912a8545fe82b86a78989d19bdacae67e337bae to 35ffa2d129a9e674a6a9fe7a08665e15e18a7c4c570a5ce30105802e3a7df048; preserved the previous blocker finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `35ffa2d129a9e674a6a9fe7a08665e15e18a7c4c570a5ce30105802e3a7df048`.
- Previous review: `reports/yaml_record_review/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Monohydrate.md`.
- Previous record SHA-256: `c723754f95dc6bcb53fdbafe6912a8545fe82b86a78989d19bdacae67e337bae`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: CORRECTED by mim_semantic_review_20260921 at 2026-09-21T21:33:25.379198+00:00: Refine the prior blocker: MP Biomedicals explicitly uses CAS 3470-37-9 for the monohydrate, while the same CAS is used for unhydrated calcium salt. Use a distinct local hydrate identity and preserve the supplier CAS as procurement metadata rather than exact global identity. Withdraw anhydrous CID/SMILES/InChI. Formula follows the certificate hemicalcium unit plus one water, doubled to whole calcium stoichiometry. Existing close match to free acid retained as reviewed in #342, not promoted to subsumption. Evidence: https://www.mpbio.com/media/document/infor/S/1/1/1/0/100365-S1110.PDF ; https://www.caymanchem.com/product/35622/2-keto-d-gluconic-acid-calcium-salt
- Active SSSOM state: 2 active row(s) for `MIM:2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Monohydrate`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Monohydrate.md` after the record changed from c723754f95dc6bcb53fdbafe6912a8545fe82b86a78989d19bdacae67e337bae to 35ffa2d129a9e674a6a9fe7a08665e15e18a7c4c570a5ce30105802e3a7df048; preserved the previous blocker finding floor pending targeted retirement.

## Findings

- **blocker**: The previous finding set in `reports/yaml_record_review/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Monohydrate.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The record says monohydrate, but the active CAS/formula/structure/PubChem values resolve to an anhydrous calcium 2-ketogluconate.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Monohydrate.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Monohydrate.yaml`, `just validate-terms data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Monohydrate.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Monohydrate.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Monohydrate.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
