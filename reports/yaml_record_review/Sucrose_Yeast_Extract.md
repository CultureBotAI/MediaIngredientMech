# `data/ingredients/mapped/Sucrose_Yeast_Extract.yaml`

## Verdict

Pass. The local registry identity, undefined-mixture classification, curated
two-component partonomy, MicrobeDecoder source occurrence, and final SSSOM row
all agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Sucrose_Yeast_Extract.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:sucrose_yeast_extract` with
  `ontology_mapping.ontology_id: kgmicrobe.ingredient:sucrose_yeast_extract`,
  label `Sucrose + Yeast Extract`, source `kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- Components: `sucrose` as `CHEBI:17992` and `yeast extract` as
  `FOODON:03315426`, both scoped to the MIM catalog.
- Occurrences: 0 CultureMech media occurrences plus 3 MicrobeDecoder source
  occurrences from `bergey:substrates`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sucrose` through `Sugars`: exited 0 and wrote zero ERROR rows.
- Engine A term validation was skipped for this local registry record because
  `kgmicrobe.ingredient:` is not an OBO prefix; the shared component partonomy
  gate covers the component references.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- `mappings/microbedecoder_residual_research_decomposition.tsv` records a
  high-confidence split of `Sucrose + Yeast Extract` into
  `CHEBI:17992:sucrose` and `FOODON:03315426:yeast extract`, matching the
  current `components`.
- `component_assertion` uses `LABEL_ENUMERATION` with complete `SOURCE_LABEL`
  and `CURATED_DATASET` evidence, which fits a source label that explicitly
  names both retained top-level parts.
- The final SSSOM row exact-matches
  `kgmicrobe.ingredient:sucrose_yeast_extract` and leaves `other` empty.

## Completeness

- The local identity, aggregate row, components, component assertion, source
  occurrence, and final SSSOM row agree.
- No unsupported active synonym, role, component, or final SSSOM payload was
  found.

## Recommended Edits

- None.
