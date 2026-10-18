# `data/ingredients/mapped/D-tryptophan.yaml`

## Verdict

Needs curation. The `CHEBI:16296` D-tryptophan identity, CAS, formula,
structure, 0/0 CultureMech count, and final SSSOM CAS payload pass, but the
`AMINO_ACID_SOURCE` role is still a provisional ChEBI-ancestry prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/D-tryptophan.yaml`.
- Identifier and grounding: `identifier: CHEBI:16296` with
  `ontology_mapping.ontology_id: CHEBI:16296`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:16296` to `D-tryptophan` with formula
  `C11H12N2O2`, charge `0`, InChI, SMILES, CAS `153-94-6`, and exact
  D-tryptophan synonyms.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-tagatose.yaml data/ingredients/mapped/D-threonine.yaml data/ingredients/mapped/D-trehalose_Dihydrate.yaml data/ingredients/mapped/D-tryptophan.yaml data/ingredients/mapped/D-valine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-tagatose.yaml data/ingredients/mapped/D-threonine.yaml data/ingredients/mapped/D-trehalose_Dihydrate.yaml data/ingredients/mapped/D-tryptophan.yaml data/ingredients/mapped/D-valine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all 5 files.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:16443 CHEBI:16398 CHEBI:232797 CHEBI:16296 CHEBI:27477`:
  returned formula, charge, CAS, InChI, SMILES, mass, synonyms, and xrefs for
  `CHEBI:16296`.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with full-corpus plausibility
  warnings only.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/culturemech_recipe_membership.tsv` has no rows for `CHEBI:16296`,
  matching `occurrence_statistics.media_count: 0` and
  `total_occurrences: 0`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:D-tryptophan` to `CHEBI:16296` with `skos:exactMatch`, canonical object
  label `D-tryptophan`, CHEBI object source, and `CAS:153-94-6` in `other`.
- The `AMINO_ACID_SOURCE` role is supported only by a
  `COMPUTATIONAL_PREDICTION` evidence object whose curator note says the role
  was inferred from ChEBI ancestry and recommends review.
- The record does not assert synonyms, environmental contexts, or mixture
  components, so there are no other claim-specific evidence objects to resolve.

## Completeness

- The hidden/ignored-inclusive exact-identifier search over active `data`
  surfaces found no second primary record or parent-mapping record for
  `CHEBI:16296`.
- CAS, formula, InChI, SMILES, and ingredient type are populated.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` and the
  per-record YAML agree.

## Recommended Edits

- In `data/ingredients/mapped/D-tryptophan.yaml`, remove the provisional
  `AMINO_ACID_SOURCE` role or replace its `COMPUTATIONAL_PREDICTION` evidence
  with inspected claim-level evidence.
- Regenerate synchronized curated and SSSOM products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-tryptophan.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
