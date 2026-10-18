# `data/ingredients/mapped/PY-glucose-rumen_Fluid.yaml`

## Verdict

Pass. The record correctly models `PY-glucose-rumen Fluid` as a local
peptone/yeast/glucose/clarified-rumen-fluid mixture rather than as glucose or
rumen fluid alone, and the final SSSOM preserves only that local mixture
identity.

## Identity

- Reviewed record: `data/ingredients/mapped/PY-glucose-rumen_Fluid.yaml`.
- Identifier and grounding: `identifier:
  kgmicrobe.ingredient:py_glucose_rumen_fluid` with
  `ontology_mapping.ontology_id:
  kgmicrobe.ingredient:py_glucose_rumen_fluid`, label
  `PY-glucose-rumen Fluid`, source `kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- Occurrences: 1 MicrobeDecoder `bergey:substrates` occurrence and no
  CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- CHEBI/OBO term validation was skipped for this local
  `kgmicrobe.ingredient` primary record.
- A fresh exact OLS4 search for `PY-glucose-rumen Fluid` returned zero class
  documents.
- The final SSSOM row was inspected directly and maps
  `MIM:PY-glucose-rumen_Fluid` exactly to
  `kgmicrobe.ingredient:py_glucose_rumen_fluid` with no `other` tokens.

## Evidence

- `mappings/microbedecoder_residual_research_decomposition.tsv` explicitly
  decomposes `PY-glucose-rumen Fluid` into peptone `MICRO:0000178`, yeast
  extract `FOODON:03315426`, glucose `CHEBI:17234`, and clarified rumen fluid
  `MICRO:0000520` with a high-confidence curated split.
- Fresh OLS4 exact component-label lookups resolved those same component IDs
  for peptone, yeast extract, glucose, and clarified rumen fluid.
- The component assertion correctly uses `ABBREVIATION_EXPANSION`,
  `completeness: UNKNOWN`, and `MIM_CATALOG` component scope, so the components
  are a best local mixture expansion rather than a complete quantitative
  recipe.
- The final SSSOM emits a single exact local ingredient row and no unsafe
  synonyms.

## Completeness

- The exact OLS4 miss supports the local fallback registry row for this
  MicrobeDecoder shorthand.
- The missing concentrations are explicitly documented: the curated
  decomposition row states none.

## Recommended Edits

- None.
