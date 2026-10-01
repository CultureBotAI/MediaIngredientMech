# YAML Record Review: Deoxysappanone B 7,3'-Dimethyl Ether

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/unmapped/Deoxysappanone_B_73-Dimethyl_Ether.yaml`
- Started UTC: 2026-10-01T04:47:36Z
- Finished UTC: 2026-10-01T04:47:37Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/unmapped/Deoxysappanone_B_73-Dimethyl_Ether.yaml`
- Identifier: `UNMAPPED_0200`
- Preferred term: Deoxysappanone B 7,3'-Dimethyl Ether
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

- Current record SHA-256: `1b268dbb3d9e92e0395759c81497f9f9b41179a31ac98640b2c8bfc785dfebb1`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: ANNOTATED by edison_literature_identity at 2026-08-06T00:00:00+00:00: Edison LITERATURE (PaperQA3) identity research; report at research/ingredients/Deoxysappanone_B_73-Dimethyl_Ether-edison-literature.md (local artifact — research/ is gitignored, so the findings are quoted here rather than linked). Report verdict: **Recommended interpretation:** a **discrete single small molecule**, not a medium formulation, extract, buffer, mixture, salt family, or generic ether. The strongest direct source names “deoxysappanone (B) 7,3′-dimethyl ether” as a selected deoxysappanone compound and elsewhere writes “deoxysappanone (deoxysappanone b 7,3′-dimethyl ether).” This supports retaining `ingredient_type: SINGLE_INGREDI CURIEs discussed: NCIT:C1645. Recorded as provenance only — no grounding applied from this run. Edison's recommendations are deliberately conservative, and a plausible identifier promoted by a mechanism that never decided anything is what #203 and #263 exist to undo. Any CURIE above is a curator's to accept or reject.
- Active SSSOM state: No active row for `MIM:Deoxysappanone_B_73-Dimethyl_Ether`, as expected for `UNMAPPED`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/unmapped_ingredients.yaml`.
- The 2026-09-01 unmapped review explains the residual unmapped policy: named media, undefined mixtures, and exact single-ingredient residuals must stay unmapped until exact same-form evidence is available.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/unmapped_ingredients.yaml`.
- Consequential unresolved item: Specific single-ingredient residual remains unresolved: current evidence does not support an exact ontology or stable-registry identity.

## Findings

- **major**: `data/ingredients/unmapped/Deoxysappanone_B_73-Dimethyl_Ether.yaml` remains `UNMAPPED`; no exact ontology term or independently supported registry identity is recorded. Do not exact-match it to a broader parent, component, hydrate, salt, or lookalike label.

## Recommended Edits

- Curate an exact same-form identity or decomposition for `data/ingredients/unmapped/Deoxysappanone_B_73-Dimethyl_Ether.yaml` before mapping it.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/unmapped/Deoxysappanone_B_73-Dimethyl_Ether.yaml`, `just validate-terms data/ingredients/unmapped/Deoxysappanone_B_73-Dimethyl_Ether.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/unmapped/Deoxysappanone_B_73-Dimethyl_Ether.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/unmapped/Deoxysappanone_B_73-Dimethyl_Ether.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
