# YAML Record Review: N'-disuccinic Acid (EDDS)

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/unmapped/N-disuccinic_Acid_(EDDS).yaml`
- Started UTC: 2026-10-01T04:49:09Z
- Finished UTC: 2026-10-01T04:49:10Z
- Verdict: pass

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/unmapped/N-disuccinic_Acid_(EDDS).yaml`
- Identifier: `kgmicrobe.compound:ethylenediamine_n_n_disuccinic_acid`
- Preferred term: N'-disuccinic Acid (EDDS)
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

- Current record SHA-256: `7ceb8de7188c719b7112cf3c6e4708a10149876ded8728c1f7218a26291eca70`.
- Source occurrence traceability: 0 active occurrence(s) across 0 medium/media; source rows: microbedecoder: 1.
- Latest curation event: MERGED_INTO by repair_comma_split_labels at 2026-08-14T00:00:00+00:00: Merged into kgmicrobe.compound:ethylenediamine_n_n_disuccinic_acid "Ethylenediamine-N,N'-disuccinic acid (EDDS)": this record is the other half of a comma-split label, not an ingredient. Repaired a comma-split label (#308/#313): `Ethylenediamine-N` and `N'-disuccinic Acid (EDDS)` are the two halves of `ethylenediamine-N,N'-disuccinic acid` split at its only comma — the surviving `(EDDS)` on the second fragment confirms the reading. ChEBI has no term for EDDS (searched the local build and live at OLS4), so MAPPING_SEMANTICS §3 step 3 applies and the rejoined record takes a registry mint. The ingest strips commas from every chemical label, so a name containing one arrives as separate fragment records — the same mechanism that produced the `D` record resolved in #346.
- Active SSSOM state: No active row for `MIM:N-disuccinic_Acid_(EDDS)`, as expected for `REJECTED`.
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

- Re-run strict schema validation on `data/ingredients/unmapped/N-disuccinic_Acid_(EDDS).yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/unmapped/N-disuccinic_Acid_(EDDS).yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
