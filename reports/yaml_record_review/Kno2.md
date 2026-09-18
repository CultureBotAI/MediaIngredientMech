# `data/ingredients/mapped/Kno2.yaml`

## Verdict

Pass with minor issues. The promoted exact ChEBI potassium nitrite identity,
structure fields, occurrence count, aggregate copy, and final SSSOM row are
consistent, but the import-era notes still say the record was left unmapped
pending exact ontology evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/Kno2.yaml`.
- Identifier and grounding: `identifier: CHEBI:232610` with
  `ontology_mapping.ontology_id: CHEBI:232610`, label `potassium nitrite`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: molecular formula `K.NO2`, molecular weight `85.103`,
  InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Khco3.yaml data/ingredients/mapped/Ki.yaml data/ingredients/mapped/Kijanimicin.yaml data/ingredients/mapped/Kno2.yaml data/ingredients/mapped/Kno3.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 records.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_2300`:
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_2300`:
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- EBI OLS4 resolves `CHEBI:232610` as active ChEBI term `potassium nitrite`,
  with the same formula, mass, InChI, and SMILES as the YAML
  `chemical_properties`.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Kno2` to
  `CHEBI:232610` with no `other` synonyms.
- Minor: `notes` still repeats the May review result saying the KNO2 formula
  shorthand was left unmapped pending exact ontology evidence, even though the
  June `promote_resolved_unmapped` pass mapped it exactly to `CHEBI:232610`.
- The hidden and ignored-inclusive search over `data/ingredients`, `mappings`,
  `reports/kg_microbe_node_id_mismatches.tsv`, `reports/hydrate_grounding.tsv`,
  `docs/data`, `src`, `tests`, `conf`, and `.claude` found the current YAML,
  final SSSOM row, docs projections, and CultureMech membership rows; it found
  no hits in `reports/kg_microbe_node_id_mismatches.tsv`,
  `reports/hydrate_grounding.tsv`, or `mappings/needs_curator_review.tsv`.

## Completeness

- The exact ChEBI identity, structure fields, aggregate copy, occurrence count,
  and final SSSOM row are present and consistent.
- Only stale explanatory `notes` text is left from the pre-promotion state.

## Recommended Edits

- Minor: refresh or remove the stale `notes` text in
  `data/ingredients/mapped/Kno2.yaml`, then synchronize the aggregate and rerun
  strict, term, round-trip, component, and SSSOM validation.
