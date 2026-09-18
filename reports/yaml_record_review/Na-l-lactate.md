# `data/ingredients/mapped/Na-l-lactate.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:232798` sodium L-lactate identity,
CAS-backed structure, source-backed carbon role, duplicate/dead-ID repairs, and
occurrence count pass, but the `ENERGY_SOURCE` facet is provisional and the
final SSSOM still publishes a racemate label for this L-specific salt.

## Identity

- Reviewed record: `data/ingredients/mapped/Na-l-lactate.yaml`.
- Identifier and grounding: `identifier: CHEBI:232798` with
  `ontology_mapping.ontology_id: CHEBI:232798`, label `sodium L-lactate`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 162 CultureMech recipe occurrences across 162 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na-formate` through `Na-laurate`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- Fresh OLS4 and OAK lookups resolve `CHEBI:232798` as active
  `sodium L-lactate`, with `cas:867-56-1`, formula `C3H5O3.Na`, the stored
  structure, and the submitted IUPAC synonym that is also present in YAML.
- The `CARBON_SOURCE` facet is source-backed by CultureMech original role text
  that explicitly says `Carbon Source`; the raw `Role: Carbon source` strings
  and `(after autoclaving)` recipe note are correctly absent from final SSSOM
  `other`.
- Major: `nutritional_roles.ENERGY_SOURCE` is backed only by automatic
  `COMPUTATIONAL_PREDICTION` evidence, and its curator note explicitly marks it
  provisional.
- Major: the final SSSOM row `MIM:Na-l-lactate` publishes
  `Sodium D,L-Lactate` in `other`. A D,L lactate label denotes racemic sodium
  lactate, not the L-specific salt asserted by `CHEBI:232798`.

## Completeness

- The active ChEBI target, CAS RN, formula, structure, 162/162 occurrence count,
  duplicate merge, dead-ID repair, source-backed `CARBON_SOURCE` role, and final
  exact mapping row agree.
- The remaining gaps are the unsupported inferred energy role and the
  stereochemically overbroad `Sodium D,L-Lactate` final synonym.

## Recommended Edits

- Major: in `data/ingredients/mapped/Na-l-lactate.yaml`, either remove
  `nutritional_roles.ENERGY_SOURCE` or replace its computational placeholder
  with source-backed evidence from maintained occurrence, role-text, or
  literature inputs. Rerun strict validation after the role facet change.
- Major: demote `Sodium D,L-Lactate` so it is not published as a synonym for
  the L-specific `CHEBI:232798` record, then rebuild final SSSOM and re-run
  final SSSOM validation plus product label validation.
