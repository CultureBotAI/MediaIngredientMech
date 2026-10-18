# `data/ingredients/mapped/Trans-cinnamic_Acid.yaml`

## Verdict

Needs curation, major. The exact CHEBI identity, CAS RN, PubChem structure,
real synonyms, occurrence count, aggregate row, and final SSSOM row pass, but
`CARBON_SOURCE` is still provisional in-session LLM evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/Trans-cinnamic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:35697` with matching
  `ontology_mapping.ontology_id`, label `trans-cinnamic acid`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `kg_microbe_node_id: CHEBI:35697`, and `ingredient_type:
  SINGLE_INGREDIENT`.
- CAS RN: `621-82-9`.
- Synonyms: ten exact kg-microbe labels for the trans cinnamic-acid isomer.
- Occurrences: 3 CultureMech recipe occurrences in 3 media.
- Roles: one `nutritional_roles.CARBON_SOURCE` facet at confidence `0.6`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Trans-cinnamic_Acid` through `Trehalose`: exited 0 and wrote zero ERROR
  rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 search for `trans-cinnamic acid` returns `CHEBI:35697` with label
  `trans-cinnamic acid`.
- Fresh PubChem lookup for CAS `621-82-9` returns formula `C9H8O2` and the
  same E isomer InChI as the YAML.
- The final SSSOM row has
  `MIM:Trans-cinnamic_Acid skos:exactMatch CHEBI:35697` and exports only real
  trans-cinnamic-acid synonyms plus `CAS:621-82-9` in `other`.

## Issues

### Major: `CARBON_SOURCE` is provisional in-session LLM evidence

The only role assertion is still the June in-session Claude prediction with the
curator note `Provisional in-session LLM role assignment; review recommended.`
The exact CHEBI identity and occurrence count do not independently establish a
carbon-source role.

## Completeness

- The CHEBI identity, CAS RN, structure fields, exact synonyms, occurrence
  count, aggregate copy, and final SSSOM row agree.
- The only residual issue is the provisional `CARBON_SOURCE` role.

## Recommended Edits

- Replace the `COMPUTATIONAL_PREDICTION` role evidence with curated
  database/literature evidence, or remove `nutritional_roles` until such
  support is added.
