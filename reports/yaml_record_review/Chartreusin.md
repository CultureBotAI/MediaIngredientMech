# `data/ingredients/mapped/Chartreusin.yaml`

## Verdict

Pass. The MicrobeDecoder chartreusin import is exactly grounded to active
`CHEBI:3580`, and its formula, InChI, SMILES, MicrobeDecoder source occurrence,
SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Chartreusin.yaml`.
- Identifier and grounding: `identifier: CHEBI:3580`,
  `ontology_mapping.ontology_id: CHEBI:3580`,
  `ontology_label: Chartreusin`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:3580` returns one active ChEBI term labelled
  `Chartreusin` with formula `C32H32O14`, molecular mass `640.594`, and the
  same InChI and SMILES stored in `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Chaninin.yaml data/ingredients/mapped/Charcoal.yaml data/ingredients/mapped/Chartreusin.yaml data/ingredients/mapped/Chaulmoogric_Acid.yaml data/ingredients/mapped/Chelated_Iron_Solution.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Chartreusin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed. The same focused validator also passed for `Charcoal` and
  `Chaulmoogric_Acid`; `Chaninin` and `Chelated_Iron_Solution` were skipped
  because their kg-microbe CURIEs are local registry IDs outside Engine A's OBO
  prefix scope.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `reports` found the active exact `MIM:Chartreusin` SSSOM row, the
  MicrobeDecoder import-review approval, and matching aggregate and docs rows
  for `CHEBI:3580`.
- Hidden/ignored-inclusive search of `data/custom/microbedecoder` found
  `kgmicrobe.trait:chartreusin` in `BacDive_Metabolite_production` with count
  1, matching the explicit `source_occurrences` entry.
- Hidden/ignored-inclusive anchored search of
  `mappings/culturemech_recipe_membership.tsv` found no `CHEBI:3580` rows,
  matching the explicit 0/0 media-recipe `occurrence_statistics`.
- The record carries no role, component, or environment claims.

## Completeness

- The exact ChEBI identifier, formula, InChI, SMILES, MicrobeDecoder source
  occurrence, SSSOM row, aggregate copy, and docs row are populated and agree.
- `synonyms` is empty, but no local alternate label, rejected label, or
  additional lookup key is required for this exact ChEBI identity.

## Recommended Edits

- None for this record.
