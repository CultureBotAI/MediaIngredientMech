# `data/ingredients/mapped/Pasteurized_Seawater.yaml`

## Verdict

Pass. The record preserves `Pasteurized Seawater` as a local ingredient and
uses a close parent edge to generic `ENVO:00002149` sea water without flattening
the heat-treated preparation into environmental sea water.

## Identity

- Reviewed record: `data/ingredients/mapped/Pasteurized_Seawater.yaml`.
- Identifier and grounding: `identifier:
  kgmicrobe.ingredient:pasteurized_seawater` with
  `ontology_mapping.ontology_id: ENVO:00002149`, label `sea water`, source
  `ENVO`, `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- Occurrences: 19 CultureMech occurrences across 19 recipes.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- CHEBI/OBO term validation was skipped for this mixed ENVO plus local
  `kgmicrobe.ingredient` record.
- A fresh exact OLS4 search for `Pasteurized Seawater` returned zero class
  documents.
- The final SSSOM rows were inspected directly: the record publishes the close
  `ENVO:00002149` parent row and the exact
  `kgmicrobe.ingredient:pasteurized_seawater` registry row.

## Evidence

- The curated mapping note explicitly records pasteurized seawater as a
  preparation variant and not an identity-equivalent label for generic sea
  water.
- The environmental context correctly uses `ENVO:00002149` as a natural source
  for the heat-treated marine water rather than as the ingredient identity.
- The final SSSOM emits no unsafe `other` tokens.

## Completeness

- The close ENVO row and exact local identity row together preserve the
  preparation boundary.
- No component decomposition is expected for a variable natural water
  preparation.

## Recommended Edits

- None.
