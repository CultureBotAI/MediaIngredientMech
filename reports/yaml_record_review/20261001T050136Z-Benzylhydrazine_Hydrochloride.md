# YAML Record Review: Benzylhydrazine Hydrochloride

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Benzylhydrazine_Hydrochloride.yaml`
- Started UTC: 2026-10-01T05:01:36Z
- Finished UTC: 2026-10-01T05:01:37Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Benzylhydrazine_Hydrochloride.yaml`
- Identifier: `cas:1073-62-7`
- Preferred term: Benzylhydrazine Hydrochloride
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Benzylhydrazine_Hydrochloride.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `cas:1073-62-7`.
- Ontology label: `Benzylhydrazine Hydrochloride`.
- Mapping quality: `FALLBACK_REGISTRY`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/Benzylhydrazine_Hydrochloride.md` after the record changed from d04e663d2f1cd497e2ff07d39d2b41302bc7a256794288bc04fe89290c1e1b0f to 67593573945a67c2ee27d401b9c4e11456045df4c7773db14515c34a1761c7bc; preserved the previous blocker finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `67593573945a67c2ee27d401b9c4e11456045df4c7773db14515c34a1761c7bc`.
- Previous review: `reports/yaml_record_review/Benzylhydrazine_Hydrochloride.md`.
- Previous record SHA-256: `d04e663d2f1cd497e2ff07d39d2b41302bc7a256794288bc04fe89290c1e1b0f`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: CORRECTED by mim_semantic_review_20260921 at 2026-09-21T21:33:25.379198+00:00: Curate the stated benzylhydrazine hydrochloride identity using the manufacturer certificate: CAS 1073-62-7, C7H10N2.ClH. Withdraw benzylamine hydrochloride CAS 3287-99-8, CID 2724127 and one-nitrogen structure. No unverified replacement structure or PubChem CID is asserted. Evidence: https://store.apolloscientific.co.uk/storage/coas/OR5636_TypicalCofA.pdf
- Active SSSOM state: 1 active row(s) for `MIM:Benzylhydrazine_Hydrochloride`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/Benzylhydrazine_Hydrochloride.md` after the record changed from d04e663d2f1cd497e2ff07d39d2b41302bc7a256794288bc04fe89290c1e1b0f to 67593573945a67c2ee27d401b9c4e11456045df4c7773db14515c34a1761c7bc; preserved the previous blocker finding floor pending targeted retirement.

## Findings

- **blocker**: The previous finding set in `reports/yaml_record_review/Benzylhydrazine_Hydrochloride.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The stored CAS 3287-99-8 and PubChem CID 2724127 denote benzylamine hydrochloride, not the labeled two-nitrogen Benzylhydrazine Hydrochloride identity.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/Benzylhydrazine_Hydrochloride.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Benzylhydrazine_Hydrochloride.yaml`, `just validate-terms data/ingredients/mapped/Benzylhydrazine_Hydrochloride.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Benzylhydrazine_Hydrochloride.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Benzylhydrazine_Hydrochloride.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
