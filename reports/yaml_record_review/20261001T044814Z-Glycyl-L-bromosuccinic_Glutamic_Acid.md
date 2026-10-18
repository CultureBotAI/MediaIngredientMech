# YAML Record Review: Glycyl-L-bromosuccinic Glutamic Acid

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/unmapped/Glycyl-L-bromosuccinic_Glutamic_Acid.yaml`
- Started UTC: 2026-10-01T04:48:14Z
- Finished UTC: 2026-10-01T04:48:15Z
- Verdict: pass

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/unmapped/Glycyl-L-bromosuccinic_Glutamic_Acid.yaml`
- Identifier: `UNMAPPED_0817`
- Preferred term: Glycyl-L-bromosuccinic Glutamic Acid
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

- Current record SHA-256: `d0921088e01118db4557a5da8ecf518abb4cbd65a656ef5661b21f68ef54f7b6`.
- Source occurrence traceability: 0 active occurrence(s) across 0 medium/media; source rows: microbedecoder: 1.
- Latest curation event: RETIRED_NOT_AN_INGREDIENT by retire_assay_labels at 2026-08-15T00:00:00+00:00: Retired as an ingredient record (#213/#308): a splice of TWO Biolog panel substrates run together by the #308 ingest: `glycyl-L-glutamic acid` and `bromosuccinic acid`. Both are already records — `Gly-Glu` (CHEBI:73801) and `Bromosuccinate` (CHEBI:73706) — so there is nothing left to ground once the splice is recognised. Not mapped, because every substrate CURIE it could be grounded to is already the primary key of a live record — in MIM the identifier IS the ontology CURIE, so a mapping here would mint a duplicate rather than add coverage. No synonym is folded onto those records either: this label names a reaction or a splice, not the substance, and asserting the synonymy would make label_index resolve it to something it does not denote.
- Active SSSOM state: No active row for `MIM:Glycyl-L-bromosuccinic_Glutamic_Acid`, as expected for `REJECTED`.
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

- Re-run strict schema validation on `data/ingredients/unmapped/Glycyl-L-bromosuccinic_Glutamic_Acid.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/unmapped/Glycyl-L-bromosuccinic_Glutamic_Acid.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
