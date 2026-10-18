# `data/ingredients/mapped/Koh.yaml`

## Verdict

Pass. The exact potassium hydroxide identity, CAS value, structure fields,
occurrence count, synonym set, absence of nutritional roles, and final SSSOM row
are consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Koh.yaml`.
- Identifier and grounding: `identifier: CHEBI:32035` with
  `ontology_mapping.ontology_id: CHEBI:32035`, label `potassium hydroxide`,
  source `CHEBI`, `mapping_quality: SYNONYM_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `1310-58-3`, molecular formula `HO.K`, InChI, and
  SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Koh.yaml data/ingredients/mapped/Kscn.yaml data/ingredients/mapped/L-2-Aminobutyric_Acid.yaml data/ingredients/mapped/L-Arabinose.yaml data/ingredients/mapped/L-Asparagine_Monohydrate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 records.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_2315`:
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_2315`:
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- EBI OLS4 resolves `CHEBI:32035` as active ChEBI term `potassium hydroxide`
  and lists `KOH`, `Aetzkali`, `Kaliumhydroxid`, `caustic potash`,
  `hydroxyde de potassium`, `potash lye`, and `potasse caustique` as
  same-substance aliases.
- PubChem resolves CAS RN `1310-58-3` with the same InChI and equivalent formula
  `HKO`, supporting the stored CAS and structure fields.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Koh` to
  `CHEBI:32035` with only same-substance aliases and `CAS:1310-58-3` in
  `other`.
- The raw CultureMech role/property pseudo-synonyms are filtered out of the
  final SSSOM and do not create a published synonym defect.
- The #128 migration deliberately dropped the legacy mineral role because
  potassium hydroxide is a pH adjuster rather than a mineral nutrient; the
  current record correctly has no nutritional role.
- The hidden and ignored-inclusive search over `data/ingredients`, `mappings`,
  `reports/kg_microbe_node_id_mismatches.tsv`, `reports/hydrate_grounding.tsv`,
  `docs/data`, `src`, `tests`, `conf`, and `.claude` found the current YAML,
  final SSSOM row, docs projections, and row-review dispositions; it found no
  hits in `reports/kg_microbe_node_id_mismatches.tsv`,
  `reports/hydrate_grounding.tsv`, or `mappings/needs_curator_review.tsv`.

## Completeness

- The exact ChEBI identity, CAS value, structure fields, aggregate copy,
  occurrence count, empty role set, and final SSSOM row are present and
  consistent.

## Recommended Edits

- None.
