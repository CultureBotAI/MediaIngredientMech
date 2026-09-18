# `data/ingredients/mapped/Meat_Extract.yaml`

## Verdict

Needs curation. The exact FoodOn identity, occurrence count, mixture
classification, and final SSSOM row pass, but `PROTEIN_SOURCE` is only a
provisional name-pattern inference.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Meat_Extract.yaml`.
- Identifier and grounding: `identifier: FOODON:03315424` with
  `ontology_mapping.ontology_id: FOODON:03315424`, label `meat extract`,
  source `FOODON`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  and `ingredient_type: UNDEFINED_MIXTURE`.
- Occurrences: 777 CultureMech recipes.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mc_general_salts_SO4free` through `Meat_Extract`: exited 0 and wrote zero
  ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  FoodOn-primary record.

## Evidence

- EBI OLS4 resolves `FOODON:03315424` as active `meat extract`.
- The mapping history deliberately distinguishes this broader `meat extract`
  term from the sibling `MIM:Beef_Extract` record on `FOODON:03302088`.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Meat_Extract`
  to `FOODON:03315424` with empty `other`.

## Completeness

- The `UNDEFINED_MIXTURE` classification fits a variable biological extract.
- `PROTEIN_SOURCE` is only backed by a `COMPUTATIONAL_PREDICTION` inferred from
  a media-role name pattern. No source attached to the role verifies that this
  meat-extract record was supplied as a protein source.

## Recommended Edits

- Curate recipe or literature evidence for `PROTEIN_SOURCE`, or remove the
  provisional nutritional role.
