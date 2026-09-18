# `data/ingredients/mapped/Peptone-yeast_Extract-glucose.yaml`

## Verdict

Pass. The MicrobeDecoder residual is represented as a local undefined-mixture
registry record with a complete label-enumeration decomposition into peptone,
yeast extract, and glucose.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Peptone-yeast_Extract-glucose.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:peptone_yeast_extract_glucose` with the
  same local registry `ontology_mapping.ontology_id`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- Components: peptone / `MICRO:0000178`, yeast extract / `FOODON:03315426`,
  and glucose / `CHEBI:17234`, all with `reference_scope: MIM_CATALOG`.
- Occurrences: 1 MicrobeDecoder `bergey:substrates` occurrence and no
  CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- Fresh OLS4 lookups resolved all three component identifiers.
- A fresh OLS4 exact search found no term for the full
  `Peptone-yeast Extract-glucose` label.
- The final SSSOM row was inspected directly and maps
  `MIM:Peptone-yeast_Extract-glucose` exactly to the local kg-microbe
  registry identifier.

## Evidence

- The label explicitly enumerates all three retained top-level components.
- `mappings/microbedecoder_residual_research_decomposition.tsv` records a
  high-confidence `split` decision for the same three components and notes that
  this is the full spelling of PYG.
- `component_assertion.method: LABEL_ENUMERATION` and
  `component_assertion.completeness: COMPLETE` accurately describe the local
  mixture assertion.
- The final SSSOM row exports no `other` tokens.

## Completeness

- No concentrations are present in the source label, so they are correctly
  absent from the components.

## Recommended Edits

- None.
