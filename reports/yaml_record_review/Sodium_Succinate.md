# `data/ingredients/mapped/Sodium_Succinate.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:63675` anhydrous sodium succinate
identity, CAS-backed structure, final synonyms, rejected hydrate label, and
occurrence count pass, but the carbon and energy roles are provisional.

## Identity

- Reviewed record: `data/ingredients/mapped/Sodium_Succinate.yaml`.
- Identifier and grounding: `identifier: CHEBI:63675` with
  `ontology_mapping.ontology_id: CHEBI:63675`, label
  `sodium succinate (anhydrous)`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 195 source occurrences across 195 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sodium_Salicylate` through `Sodium_Thiophosphate_Tribasic_Hydrate`: exited 0
  and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh EBI OLS4 lookup resolves active `CHEBI:63675` with label
  `sodium succinate (anhydrous)`, CAS `150-90-3`, and the curated anhydrous
  disodium succinate aliases.
- Fresh PubChem lookup for CAS `150-90-3` resolves to sodium succinate with the
  same disodium succinate InChI and SMILES as the record.
- Final SSSOM keeps the same-substance succinate aliases plus `CAS:150-90-3`;
  the raw `Role: Growth factor` strings and rejected hexahydrate label are
  correctly filtered out of final `other`.
- Major: `nutritional_roles.CARBON_SOURCE` and
  `nutritional_roles.ENERGY_SOURCE` are still provisional
  `COMPUTATIONAL_PREDICTION` facets with `review recommended` notes.

## Completeness

- The active anhydrous ChEBI term, CAS RN, formula, structure, 195/195
  occurrence count, final exact row, and rejected hidden hydrate synonym state
  agree.
- The only consequential gap on this record is replacing or dropping the
  provisional nutritional roles.

## Recommended Edits

- Major: in `data/ingredients/mapped/Sodium_Succinate.yaml`, replace the
  provisional carbon and energy role evidence with checked source evidence or
  remove those roles.
