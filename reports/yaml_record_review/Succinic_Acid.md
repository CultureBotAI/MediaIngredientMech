# `data/ingredients/mapped/Succinic_Acid.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:15741` identity, CAS, structural
fields, curated synonyms, and final SSSOM row pass, but the carbon/energy role
facets are still provisional.

## Identity

- Reviewed record: `data/ingredients/mapped/Succinic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:15741` with
  `ontology_mapping.ontology_id: CHEBI:15741`, label `succinic acid`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS `110-15-6`, formula `C4H6O4`, and ChEBI/PubChem
  structure fields for the neutral diacid.
- Occurrences: 36 occurrences across 36 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Substrate` through `Sucrose-6-monophosphate_Dipotassium_Salt`: exited 0 and
  wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:15741` with label `succinic acid`,
  CAS xref `110-15-6`, formula `C4H6O4`, and all exported kg-microbe synonyms
  as exact or related synonyms of the acid.
- PubChem resolves CAS `110-15-6` to `Succinic Acid` with the same molecular
  formula and InChI.
- `mappings/culturemech_recipe_membership.tsv` has the 36 expected
  `CHEBI:15741` recipe rows, agreeing with `total_occurrences: 36` and
  `media_count: 36`.
- The final SSSOM row exact-matches `CHEBI:15741`; its `other` tokens are
  ChEBI synonyms of succinic acid plus `CAS:110-15-6`.
- Major: `nutritional_roles.CARBON_SOURCE` and
  `nutritional_roles.ENERGY_SOURCE` are supported only by
  `COMPUTATIONAL_PREDICTION` evidence from the name-list inference passes.

## Completeness

- The exact acid identity, CAS, chemical properties, aggregate row, occurrence
  count, and final SSSOM row agree.
- No unsupported active synonym, component, or final SSSOM payload was found;
  the only unsupported claims are the provisional role facets.

## Recommended Edits

- Major: either replace the provisional `CARBON_SOURCE` and `ENERGY_SOURCE`
  assertions in `data/ingredients/mapped/Succinic_Acid.yaml` with inspected
  CultureMech or literature evidence, or remove those role facets.
