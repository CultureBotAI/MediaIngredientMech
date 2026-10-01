# YAML Record Review: Acridine orange

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Acridine_Orange.yaml`
- Started UTC: 2026-10-01T05:01:13Z
- Finished UTC: 2026-10-01T05:01:14Z
- Verdict: pass_with_minor_issues

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Acridine_Orange.yaml`
- Identifier: `CHEBI:87346`
- Preferred term: Acridine orange
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Acridine_Orange.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:87346`.
- Ontology label: `acridine orange free base`.
- Mapping quality: `CAS_RN_LOOKUP`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/Acridine_Orange.md` after the record changed from 2eacc84c8f7b1c5058d124252b98bac124af26421609bad887cb7b768ef85bc2 to 1a40274cae73f569d471bd910c4ef4d1e91f98e7a2651377e1bd707422581777; preserved the previous minor finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `1a40274cae73f569d471bd910c4ef4d1e91f98e7a2651377e1bd707422581777`.
- Previous review: `reports/yaml_record_review/Acridine_Orange.md`.
- Previous record SHA-256: `2eacc84c8f7b1c5058d124252b98bac124af26421609bad887cb7b768ef85bc2`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: REGROUNDED_IDENTITY by claude at 2026-09-23T00:44:54.408844+00:00: identifier CHEBI:51739 -> CHEBI:87346; ontology CHEBI:51739 ('acridine orange') -> CHEBI:87346 ('acridine orange free base'); mapping_quality EXACT_MATCH -> CAS_RN_LOOKUP. CHEBI:51739 'acridine orange' is the hydrochloride (formula H.C17H19N3.Cl, is_a hydrochloride); its formula, InChI, SMILES and the 'tetramethylacridine-3,6-diamine hydrochloride' synonym were copied onto the record from the term. The record's only source-supplied identity evidence is CAS 494-38-2, which PubChem resolves to CID 62344, C17H19N3, InChIKey DPKHZNPWBDQZCN-UHFFFAOYSA-N: CHEBI:87346 'acridine orange free base' (synonyms 'Acridine Orange', 'Acridine Orange Base'). ChEBI xrefs 494-38-2 on both terms, so the PubChem InChIKey decides. The CAS governs the form (#320). Structure fields refreshed from the term; the hydrochloride alias is REJECTED_LABEL. (#312) REJECTED_LABEL: N,N,N',N'-tetramethylacridine-3,6-diamine hydrochloride (names the hydrochloride CHEBI:51739, not the free base).
- Active SSSOM state: 1 active row(s) for `MIM:Acridine_Orange`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: None found.

## Findings

- **minor**: The previous finding set in `reports/yaml_record_review/Acridine_Orange.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The exact CHEBI identity, exact synonym, CAS, chemistry, SSSOM row, and aggregate pass; one history auto-backfill change string has a truncated InChI.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/Acridine_Orange.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Acridine_Orange.yaml`, `just validate-terms data/ingredients/mapped/Acridine_Orange.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Acridine_Orange.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Acridine_Orange.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
