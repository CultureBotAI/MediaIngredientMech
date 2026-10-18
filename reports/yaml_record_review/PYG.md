# `data/ingredients/mapped/PYG.yaml`

## Verdict

Needs curation; major. The local PYG mixture fallback is internally consistent,
but a fresh OLS4 search now finds `MICRO:0001573` `PYG medium`, so the fallback
identity may be promotable to a public MICRO term.

## Identity

- Reviewed record: `data/ingredients/mapped/PYG.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.ingredient:pyg` with
  `ontology_mapping.ontology_id: kgmicrobe.ingredient:pyg`, label `PYG`,
  source `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`,
  `mapping_status: MAPPED`, and `ingredient_type: UNDEFINED_MIXTURE`.
- Occurrences: 114 MicrobeDecoder `bergey:substrates` occurrences and no
  CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- CHEBI/OBO term validation was skipped for this local
  `kgmicrobe.ingredient` primary record.
- The final SSSOM row was inspected directly and maps `MIM:PYG` exactly to
  `kgmicrobe.ingredient:pyg` with no `other` tokens.

## Evidence

- `mappings/microbedecoder_residual_research_decomposition.tsv` explicitly
  decomposes `PYG` into peptone `MICRO:0000178`, yeast extract
  `FOODON:03315426`, and glucose `CHEBI:17234` with a high-confidence curated
  split.
- Fresh OLS4 exact component-label lookups resolved those same component IDs
  for peptone, yeast extract, and glucose.
- The component assertion correctly uses `ABBREVIATION_EXPANSION`,
  `completeness: UNKNOWN`, and `MIM_CATALOG` component scope, so the components
  are a best local mixture expansion rather than a complete quantitative
  recipe.
- Major: a fresh OLS4 search for `PYG` returned `MICRO:0001573` `PYG medium`,
  which is a plausible public term for this local fallback subject and was not
  reflected in the 2026-08 decomposition.
- The final SSSOM emits a single exact local ingredient row and no unsafe
  synonyms.

## Completeness

- The local fallback identity was reasonable when curated from the older
  residual pass, but the newly visible MICRO candidate needs a curator decision.
- The missing concentrations are explicitly documented: the curated
  decomposition row states none.

## Recommended Edits

- Major: evaluate `MICRO:0001573` as a replacement grounding for
  `data/ingredients/mapped/PYG.yaml`. If it denotes the same PYG formulation,
  promote the record from `kgmicrobe.ingredient:pyg` to a MICRO mapping, rebuild
  `mappings/ingredient_mappings.sssom.tsv`, and rerun
  `scripts/validate_sssom_invariants.py` plus
  `scripts/validate_component_partonomy.py`.
