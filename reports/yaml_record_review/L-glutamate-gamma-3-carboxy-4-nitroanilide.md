# `data/ingredients/mapped/L-glutamate-gamma-3-carboxy-4-nitroanilide.yaml`

## Verdict

Pass with minor issues. The MicrobeDecoder label is intentionally preserved as
a local `kgmicrobe.compound` fallback registry record, its source occurrence
and final SSSOM row are consistent, and only stale importer notes still say
curator review is needed.

## Identity

- Reviewed record:
  `data/ingredients/mapped/L-glutamate-gamma-3-carboxy-4-nitroanilide.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.compound:l-glutamate-gamma-3-carboxy-4-nitroanilide`
  with the same `ontology_mapping.ontology_id`, label
  `L-glutamate-gamma-3-carboxy-4-nitroanilide`, source
  `kgmicrobe.compound`, `mapping_quality: FALLBACK_REGISTRY`, and
  `mapping_status: MAPPED`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-glutamate-gamma-3-carboxy-4-nitroanilide.yaml data/ingredients/mapped/L-glutamic_Acid.yaml data/ingredients/mapped/L-glutamine.yaml data/ingredients/mapped/L-histidine.yaml data/ingredients/mapped/L-histidine_2-naphthylamide.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/L-glutamic_Acid.yaml data/ingredients/mapped/L-glutamine.yaml data/ingredients/mapped/L-histidine.yaml data/ingredients/mapped/L-histidine_2-naphthylamide.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the four OBO-backed ChEBI records. Engine A term validation was
  skipped for this non-OBO `kgmicrobe.compound` registry record, matching the
  justfile prefilter.

## Evidence

- The promotion history records the #213 decision to keep
  `L-glutamate-gamma-3-carboxy-4-nitroanilide` as a chromogenic enzyme
  substrate that was absent from available namespaces.
- Fresh OLS4 exact ChEBI search for
  `L-glutamate-gamma-3-carboxy-4-nitroanilide` found no term, and PubChem name
  lookup found no CID, so the local registry fallback remains plausible.
- The MicrobeDecoder import records one `BacDive_Metabolite_utilization`
  source occurrence for
  `kgmicrobe.trait:l_glutamate_gamma_3_carboxy_4_nitroanilide`.
- The final SSSOM publishes one `skos:exactMatch` row to the local
  `kgmicrobe.compound` identifier with an empty `other` field.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy, final
  SSSOM row, docs projections, and older batch-validation warnings that only
  reflect the local non-OBO CURIE.
- Minor: the top-level `notes` still say curator review was needed. The absent
  CHEBI/NCIT wording is still accurate, but #213 resolved the mapping by
  creating the local fallback registry identifier.

## Completeness

- The local registry identity, source occurrence count, aggregate copy, and
  final SSSOM row are present and consistent.

## Recommended Edits

- Minor: update the stale top-level `notes` in
  `data/ingredients/mapped/L-glutamate-gamma-3-carboxy-4-nitroanilide.yaml`
  and the aggregate copy the next time the record is touched so the current
  review text does not imply that #213 is still unresolved.
