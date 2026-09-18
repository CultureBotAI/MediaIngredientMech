# `data/ingredients/mapped/Succinate.yaml`

## Verdict

Needs curation - major. The bare `Succinate` grounding to broad
`CHEBI:26806` follows the documented protonation rule, but salt-specific
`Na Succinate` labels publish as synonyms and the carbon/energy roles remain
provisional.

## Identity

- Reviewed record: `data/ingredients/mapped/Succinate.yaml`.
- Identifier and grounding: `identifier: CHEBI:26806` with
  `ontology_mapping.ontology_id: CHEBI:26806`, label `succinate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 20 occurrences across 20 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Substrate` through `Sucrose-6-monophosphate_Dipotassium_Salt`: exited 0 and
  wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:26806` with label `succinate` and a
  definition broad enough for a bare anion label, so the exact match to the
  generic succinate anion term is sound under `MAPPING_SEMANTICS.md`.
- `mappings/culturemech_recipe_membership.tsv` has the 20 expected
  `CHEBI:26806` recipe rows, agreeing with `total_occurrences: 20` and
  `media_count: 20`.
- Major: the final SSSOM row publishes `Na Succinate` and `Na-succinate` in
  `other` even though those tokens name sodium succinate salts, not the generic
  `CHEBI:26806` succinate subject. The separate
  `data/ingredients/mapped/Sodium_Succinate.yaml` record carries the sodium salt
  identity.
- Major: `nutritional_roles.CARBON_SOURCE` and
  `nutritional_roles.ENERGY_SOURCE` are supported only by
  `COMPUTATIONAL_PREDICTION` evidence from the name-list inference passes.

## Completeness

- The ontology target, aggregate row, occurrence count, and non-salt SSSOM
  synonyms agree.
- An ignored/hidden search of local curated, mapping, generated, report, source,
  and documentation paths found the expected active succinate rows plus the
  separate sodium-succinate record that owns the exported `Na Succinate` text.

## Recommended Edits

- Major: in `data/ingredients/mapped/Succinate.yaml`, retype or remove the
  `Na Succinate` and `Na-succinate` synonyms so the final SSSOM `other` column
  only exports names for the `CHEBI:26806` subject.
- Major: either replace the provisional `CARBON_SOURCE` and `ENERGY_SOURCE`
  assertions with inspected CultureMech or literature evidence, or remove
  those role facets.
