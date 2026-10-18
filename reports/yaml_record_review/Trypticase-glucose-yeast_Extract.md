# `data/ingredients/mapped/Trypticase-glucose-yeast_Extract.yaml`

## Verdict

Pass. The fallback registry identity, three-component decomposition, source
occurrence count, aggregate row, and final SSSOM row pass.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Trypticase-glucose-yeast_Extract.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:trypticase_glucose_yeast_extract` with
  matching `ontology_mapping.ontology_id`, label
  `Trypticase-glucose-yeast Extract`, source `kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- Synonyms: one raw MicrobeDecoder label identical to the preferred term.
- Occurrences: 11 MicrobeDecoder source occurrences; no CultureMech recipe
  occurrences.
- Components: `MICRO:0000175` Trypticase peptone, `CHEBI:17234` glucose, and
  `FOODON:03315426` yeast extract.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Trypticase-glucose-yeast_Extract` through `Tryptone_Peptone`: exited 0 and
  wrote zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Hidden/ignored-inclusive search found the maintained decomposition row in
  `mappings/microbedecoder_residual_research_decomposition.tsv`: the row splits
  `Trypticase-glucose-yeast Extract` into Trypticase peptone, glucose, and
  yeast extract with high confidence.
- The record's `component_assertion` cites the MicrobeDecoder source label and
  the curated decomposition row, uses `LABEL_ENUMERATION`, and marks the
  three top-level components complete.
- The final SSSOM row has
  `MIM:Trypticase-glucose-yeast_Extract skos:exactMatch
  kgmicrobe.ingredient:trypticase_glucose_yeast_extract` and exports no
  `other` tokens.

## Issues

None.

## Completeness

- The fallback identity, component list, component assertion metadata, source
  occurrence count, aggregate copy, and final SSSOM row agree.

## Recommended Edits

None.
