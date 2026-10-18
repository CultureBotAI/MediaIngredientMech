# YAML Record Review: 2',2'-Bisepigallocatechin Digallate

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/unmapped/22-Bisepigallocatechin_Digallate.yaml`
- Started UTC: 2026-10-01T04:46:13Z
- Finished UTC: 2026-10-01T04:46:14Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/unmapped/22-Bisepigallocatechin_Digallate.yaml`
- Identifier: `UNMAPPED_0190`
- Preferred term: 2',2'-Bisepigallocatechin Digallate
- Mapping status: `UNMAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
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
- Identity judgement: Specific single-ingredient residual remains unresolved: current evidence does not support an exact ontology or stable-registry identity.

## Evidence

- Current record SHA-256: `138c9b44c7bd58e48a1a0bc24e1b53c902f0854c2e9ad79a3f931bd037f16f39`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: ANNOTATED by edison_literature_identity at 2026-08-06T00:00:00+00:00: Edison LITERATURE (PaperQA3) identity research; report at research/ingredients/22-bisepigallocatechin_Digallate-edison-literature.md (local artifact — research/ is gitignored, so the findings are quoted here rather than linked). Report verdict: ## Executive recommendation — **Retain `UNMAPPED`.** The literature supports that this label was intended to denote a **discrete polyphenolic small molecule**, rather than a buffer, extract, medium formulation, salt mixture, or commercial blend. Nevertheless, the recovered sources do not supply a CAS Registry Number, molecular formula, molecular weight, full stereochemical description, salt/hydrat No ontology CURIE was proposed. Recorded as provenance only — no grounding applied from this run. Edison's recommendations are deliberately conservative, and a plausible identifier promoted by a mechanism that never decided anything is what #203 and #263 exist to undo. Any CURIE above is a curator's to accept or reject.
- Active SSSOM state: No active row for `MIM:22-Bisepigallocatechin_Digallate`, as expected for `UNMAPPED`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/unmapped_ingredients.yaml`.
- The 2026-09-01 unmapped review explains the residual unmapped policy: named media, undefined mixtures, and exact single-ingredient residuals must stay unmapped until exact same-form evidence is available.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/unmapped_ingredients.yaml`.
- Consequential unresolved item: Specific single-ingredient residual remains unresolved: current evidence does not support an exact ontology or stable-registry identity.

## Findings

- **major**: `data/ingredients/unmapped/22-Bisepigallocatechin_Digallate.yaml` remains `UNMAPPED`; no exact ontology term or independently supported registry identity is recorded. Do not exact-match it to a broader parent, component, hydrate, salt, or lookalike label.

## Recommended Edits

- Curate an exact same-form identity or decomposition for `data/ingredients/unmapped/22-Bisepigallocatechin_Digallate.yaml` before mapping it.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/unmapped/22-Bisepigallocatechin_Digallate.yaml`, `just validate-terms data/ingredients/unmapped/22-Bisepigallocatechin_Digallate.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/unmapped/22-Bisepigallocatechin_Digallate.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/unmapped/22-Bisepigallocatechin_Digallate.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
