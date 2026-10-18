# `data/ingredients/mapped/Kawain.yaml`

## Verdict

Needs curation. The CAS-specific regrounding from `CHEBI:6117` to racemic
`CHEBI:156288` is correct and the final SSSOM row is clean, but the InChI and
SMILES still describe the old stereospecific ChEBI form.

## Identity

- Reviewed record: `data/ingredients/mapped/Kawain.yaml`.
- Identifier and grounding: `identifier: CHEBI:156288` with
  `ontology_mapping.ontology_id: CHEBI:156288`, label `DL-kavain`, source
  `CHEBI`, `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `3155-48-4`, molecular formula `C14H14O3`, and
  stale InChI and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Kao_And_Michayluk_Vitamin_Solution.yaml data/ingredients/mapped/Karanjin.yaml data/ingredients/mapped/Kasugamycin.yaml data/ingredients/mapped/Kawain.yaml data/ingredients/mapped/Kbr.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for `Karanjin`, `Kasugamycin`,
  `Kawain`, and `Kbr`; `Kao_And_Michayluk_Vitamin_Solution` was skipped because
  MICRO is intentionally outside the OBO-safe Engine A adapter set.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_2200`:
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_2200`:
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- EBI OLS4 resolves `CHEBI:156288` as active ChEBI term `DL-kavain` and lists
  `D,L-kawain` and `DL-Kawain` as synonyms, supporting the CAS-specific
  regrounding from the old `CHEBI:6117` record.
- PubChem resolves CAS RN `3155-48-4` with formula `C14H14O3` and an InChI
  without the `/t12-/m0/s1` stereochemical layer retained in the current YAML,
  so the stored formula and CAS agree with the racemate but the stored InChI
  and SMILES still need to be refreshed.
- Major: the current InChI and SMILES were backfilled before #320 and still
  encode the old stereospecific `CHEBI:6117` form rather than `CHEBI:156288`
  `DL-kavain`.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Kawain` to
  `CHEBI:156288` with only `CAS:3155-48-4` in `other`.
- The hidden and ignored-inclusive search over `data/ingredients`, `mappings`,
  `reports/kg_microbe_node_id_mismatches.tsv`, `reports/hydrate_grounding.tsv`,
  `docs/data`, `src`, `tests`, `conf`, and `.claude` found the current YAML,
  final SSSOM row, docs projections, and old row-review references to the
  previous `CHEBI:6117` mapping; it found no hits in
  `reports/kg_microbe_node_id_mismatches.tsv`,
  `reports/hydrate_grounding.tsv`, or `mappings/needs_curator_review.tsv`.

## Completeness

- The active ChEBI racemate identity, CAS RN, aggregate copy, empty occurrence
  count, and final SSSOM row are present and consistent.
- The chemical structure block is incomplete until InChI and SMILES are
  regenerated for the racemate or intentionally cleared if no unambiguous
  registry structure should be attached.

## Recommended Edits

- Major: update or clear `chemical_properties.inchi` and
  `chemical_properties.smiles` in `data/ingredients/mapped/Kawain.yaml` so they
  no longer encode the old `CHEBI:6117` stereospecific form, then synchronize
  the aggregate and rerun strict, term, round-trip, component, and SSSOM
  validation.
