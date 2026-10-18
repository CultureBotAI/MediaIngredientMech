# `data/ingredients/mapped/PYEG.yaml`

## Verdict

Pass. The record correctly models `PYEG` as a local peptone/yeast/glucose
mixture, keeps the abbreviation out of a single-compound mapping, and publishes
a clean exact local SSSOM row.

## Identity

- Reviewed record: `data/ingredients/mapped/PYEG.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.ingredient:pyeg` with
  `ontology_mapping.ontology_id: kgmicrobe.ingredient:pyeg`, label `PYEG`,
  source `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`,
  `mapping_status: MAPPED`, and `ingredient_type: UNDEFINED_MIXTURE`.
- Occurrences: 1 MicrobeDecoder `bergey:substrates` occurrence and no
  CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- CHEBI/OBO term validation was skipped for this local
  `kgmicrobe.ingredient` primary record.
- A fresh exact OLS4 search for `PYEG` returned one unrelated NCBI Taxonomy
  class for an expression vector and no medium or ingredient class.
- The final SSSOM row was inspected directly and maps `MIM:PYEG` exactly to
  `kgmicrobe.ingredient:pyeg` with no `other` tokens.

## Evidence

- `mappings/microbedecoder_residual_research_decomposition.tsv` explicitly
  decomposes `PYEG` into peptone `MICRO:0000178`, yeast extract
  `FOODON:03315426`, and glucose `CHEBI:17234` with a high-confidence curated
  split.
- Fresh OLS4 exact component-label lookups resolved those same component IDs
  for peptone, yeast extract, and glucose.
- The component assertion correctly uses `ABBREVIATION_EXPANSION`,
  `completeness: UNKNOWN`, and `MIM_CATALOG` component scope, so the components
  are a best local mixture expansion rather than a complete quantitative
  recipe.
- The final SSSOM emits a single exact local ingredient row and no unsafe
  synonyms.

## Completeness

- The exact OLS4 search supports the local fallback registry row for this
  MicrobeDecoder shorthand: it found no exact ingredient or medium class to
  promote to.
- The missing concentrations are explicitly documented: the curated
  decomposition row states none.

## Recommended Edits

- None.
