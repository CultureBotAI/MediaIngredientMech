# `data/ingredients/mapped/Sodium_succinate_dibasic_hexahydrate.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:63686` sodium succinate hexahydrate
identity, CAS-backed structure, hydrate synonyms, occurrence count, and final
SSSOM row pass, but the carbon and energy roles are provisional.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Sodium_succinate_dibasic_hexahydrate.yaml`.
- Identifier and grounding: `identifier: CHEBI:63686` with
  `ontology_mapping.ontology_id: CHEBI:63686`, label
  `sodium succinate hexahydrate`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 20 source occurrences across 20 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sodium_Thiosulfate_Pentahydrate` through `Soil`: exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh EBI OLS4 lookup resolves active `CHEBI:63686` with label
  `sodium succinate hexahydrate`, CAS `6106-21-4`, and the curated hexahydrate
  synonyms.
- Fresh PubChem lookup for CAS `6106-21-4` resolves to sodium succinate
  hexahydrate with the same hydrate formula, InChI, and SMILES as the record.
- Final SSSOM publishes same-substance hexahydrate aliases, the `x 6 H2O` and
  middle-dot raw labels, and `CAS:6106-21-4`.
- Major: `nutritional_roles.CARBON_SOURCE` and
  `nutritional_roles.ENERGY_SOURCE` are still provisional
  `COMPUTATIONAL_PREDICTION` facets with `review recommended` notes.

## Completeness

- The ChEBI ID, CAS RN, hydrate formula, structure, 20/20 occurrence count,
  active synonyms, and final exact row agree.
- The only consequential gap is replacing or dropping the provisional
  nutritional roles.

## Recommended Edits

- Major: in
  `data/ingredients/mapped/Sodium_succinate_dibasic_hexahydrate.yaml`, replace
  the provisional carbon and energy role evidence with checked source evidence
  or remove those roles.
