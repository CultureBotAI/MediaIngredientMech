# `data/ingredients/mapped/PY-fructose.yaml`

## Verdict

Pass. The record correctly models `PY-fructose` as a local undefined
peptone/yeast/fructose mixture rather than as the fructose compound alone, and
the final SSSOM preserves only that local mixture identity.

## Identity

- Reviewed record: `data/ingredients/mapped/PY-fructose.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.ingredient:py_fructose`
  with `ontology_mapping.ontology_id: kgmicrobe.ingredient:py_fructose`, label
  `PY-fructose`, source `kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- Occurrences: 1 MicrobeDecoder `bergey:substrates` occurrence and no
  CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- CHEBI/OBO term validation was skipped for this local
  `kgmicrobe.ingredient` primary record.
- A fresh exact OLS4 search for `PY-fructose` returned zero class documents.
- The final SSSOM row was inspected directly and maps `MIM:PY-fructose`
  exactly to `kgmicrobe.ingredient:py_fructose` with no `other` tokens.

## Evidence

- The checked-in `scripts/decompose_py_media_and_ground_categories.py` curation
  input explicitly decomposes `PY-fructose` into peptone `MICRO:0000178`, yeast
  extract `FOODON:03315426`, and fructose `CHEBI:28757`.
- The component assertion correctly uses `ABBREVIATION_EXPANSION`,
  `completeness: UNKNOWN`, and `MIM_CATALOG` component scope, so the components
  are a best local mixture expansion rather than a complete quantitative
  recipe.
- The record does not map exactly to `CHEBI:28757`; fructose is a component of
  the PY mixture, not the whole subject.
- The final SSSOM emits a single exact local ingredient row and no unsafe
  synonyms.

## Completeness

- A gitignore-independent local search over `data/ingredients`, `data/curated`,
  `mappings`, `reports`, `scripts`, `src`, `tests`, `docs`, and
  `UNIFIED_INGREDIENT_MAPPING.tsv` found the expected local references for
  this fallback identity.
- The missing concentrations are explicitly documented: the source label gives
  none.

## Recommended Edits

- None.
