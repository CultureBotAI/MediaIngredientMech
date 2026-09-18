# `data/ingredients/mapped/Kscn.yaml`

## Verdict

Pass. The exact ChEBI potassium thiocyanate identity, CAS value, structure
fields, occurrence count, ChEBI synonym set, and final SSSOM row are
consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Kscn.yaml`.
- Identifier and grounding: `identifier: CHEBI:30951` with
  `ontology_mapping.ontology_id: CHEBI:30951`, label `potassium thiocyanate`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `333-20-0`, molecular formula `CNS.K`, InChI, and
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

- EBI OLS4 resolves `CHEBI:30951` as active ChEBI term
  `potassium thiocyanate` and lists `KSCN`, `Rhocya`,
  `potassium rhodanate`, `potassium rhodanide`, and
  `potassium sulfocyanate` as same-substance aliases.
- PubChem resolves CAS RN `333-20-0` with the same InChI and equivalent formula
  `CKNS`, supporting the stored CAS and structure fields.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Kscn` to
  `CHEBI:30951` with only same-substance aliases and `CAS:333-20-0` in
  `other`.
- The raw CultureMech property pseudo-synonym is filtered out of the final
  SSSOM and does not create a published synonym defect.
- The hidden and ignored-inclusive search over `data/ingredients`, `mappings`,
  `reports/kg_microbe_node_id_mismatches.tsv`, `reports/hydrate_grounding.tsv`,
  `docs/data`, `src`, `tests`, `conf`, and `.claude` found the current YAML,
  final SSSOM row, docs projections, and row-review dispositions; it found no
  hits in `reports/kg_microbe_node_id_mismatches.tsv`,
  `reports/hydrate_grounding.tsv`, or `mappings/needs_curator_review.tsv`.

## Completeness

- The exact ChEBI identity, CAS value, structure fields, aggregate copy,
  occurrence count, and final SSSOM row are present and consistent.

## Recommended Edits

- None.
