# `data/ingredients/mapped/PYG-002_Tween_80.yaml`

## Verdict

Pass. The record correctly models `PYG-0.02% Tween 80` as a local
peptone/yeast/glucose/polysorbate 80 mixture rather than as polysorbate 80
alone, and the final SSSOM preserves only that local mixture identity.

## Identity

- Reviewed record: `data/ingredients/mapped/PYG-002_Tween_80.yaml`.
- Identifier and grounding: `identifier:
  kgmicrobe.ingredient:pyg_0_02_tween_80` with
  `ontology_mapping.ontology_id: kgmicrobe.ingredient:pyg_0_02_tween_80`,
  label `PYG-0.02% Tween 80`, source `kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- Occurrences: 1 MicrobeDecoder `bergey:substrates` occurrence and no
  CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- CHEBI/OBO term validation was skipped for this local
  `kgmicrobe.ingredient` primary record.
- A fresh exact OLS4 search for `PYG-0.02% Tween 80` returned zero class
  documents.
- The final SSSOM row was inspected directly and maps
  `MIM:PYG-002_Tween_80` exactly to
  `kgmicrobe.ingredient:pyg_0_02_tween_80` with no `other` tokens.

## Evidence

- The checked-in `scripts/decompose_py_media_and_ground_categories.py` curation
  input explicitly decomposes `PYG-0.02% Tween 80` into peptone
  `MICRO:0000178`, yeast extract `FOODON:03315426`, glucose `CHEBI:17234`,
  and polysorbate 80 `CHEBI:53426`.
- Fresh OLS4 exact component-label lookups resolved those same component IDs
  for peptone, yeast extract, glucose, and polysorbate 80.
- The component assertion correctly uses `ABBREVIATION_EXPANSION`,
  `completeness: UNKNOWN`, and `MIM_CATALOG` component scope, so the components
  are a best local mixture expansion rather than a complete quantitative
  recipe.
- The record does not map exactly to `CHEBI:53426`; polysorbate 80 is a
  component of the PYG/Tween mixture, not the whole subject.
- The final SSSOM emits a single exact local ingredient row and no unsafe
  synonyms.

## Completeness

- The exact OLS4 miss supports the local fallback registry row for this
  MicrobeDecoder shorthand.
- The label-level `0.02%` Tween qualifier is preserved in the mixture identity
  and is not exported as stray SSSOM `other` text.

## Recommended Edits

- None.
