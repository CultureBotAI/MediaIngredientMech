# `data/ingredients/mapped/Carotenoid.yaml`

## Verdict

Pass. The MicrobeDecoder class label is exactly grounded to active
`CHEBI:23044` carotenoid, and its source provenance, SSSOM row, and aggregate
copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Carotenoid.yaml`.
- Identifier and grounding: `identifier: CHEBI:23044`,
  `ontology_mapping.ontology_id: CHEBI:23044`,
  `ontology_label: carotenoid`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Direct OLS lookup for `CHEBI:23044` returns the active ChEBI carotenoid class
  term.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Carnitine_Hydrochloride.yaml data/ingredients/mapped/Carnosic_Acid.yaml data/ingredients/mapped/Carotenoid.yaml data/ingredients/mapped/Carrageenan.yaml data/ingredients/mapped/Carrot.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Carnitine_Hydrochloride.yaml data/ingredients/mapped/Carnosic_Acid.yaml data/ingredients/mapped/Carotenoid.yaml data/ingredients/mapped/Carrageenan.yaml data/ingredients/mapped/Carrot.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 files.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.GkFQqh`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.GkFQqh`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `docs/data`, and `reports`, excluding bulky backups and generated
  review-report directories, found the active `MIM:Carotenoid` SSSOM row with
  the exact ChEBI target and matching aggregate/docs rows.
- The current `mappings/culturemech_recipe_membership.tsv` table has 0 rows
  for `CHEBI:23044`, matching `occurrence_statistics` `0/0`.
- The MicrobeDecoder import source is retained as
  `kgmicrobe.trait:carotenoid`; no synonym, role, component, or environment
  claims are present.

## Completeness

- The exact ChEBI class identifier, MicrobeDecoder source occurrence, SSSOM
  row, aggregate copy, and docs row are populated.
- Chemical structure slots are appropriately empty because `CHEBI:23044`
  denotes a chemical class, not one exact molecular graph.

## Recommended Edits

- None for this record.
