# `data/ingredients/mapped/Fastidious_Anaerobe_Broth_With_Meat_Granules.yaml`

## Verdict

Pass with minor issues. The MicrobeDecoder residual was promoted to a local
complex-medium identity with curated partial component partonomy and a clean
final registry SSSOM row, but its top-level `notes` still describe the old
unmapped review state.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Fastidious_Anaerobe_Broth_With_Meat_Granules.yaml`.
- Identifier and grounding: `identifier:
  kgmicrobe.ingredient:fastidious_anaerobe_broth_with_meat_granules` with
  matching `ontology_mapping.ontology_id`, source `kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- The record has one MicrobeDecoder `bergey:substrates` source occurrence and
  four curated `MIM_CATALOG` components under a `CURATED_INTERPRETATION` /
  `PARTIAL` component assertion.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Fastidious_Anaerobe_Broth_With_Meat_Granules.yaml data/ingredients/mapped/Fatty_Acid_Mixture_See_Medium_No_266.yaml data/ingredients/mapped/Fe2_So43_X_N_H2o.yaml data/ingredients/mapped/Fe4_Po42.yaml data/ingredients/mapped/Fe_Iii-edta.yaml --out /tmp/mim_fe_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- Engine A term validation was skipped for this record because the ontology ID
  uses the local `kgmicrobe.ingredient` prefix rather than an OBO prefix.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  local identifier, MicrobeDecoder occurrence, four curated components,
  component-assertion block, `UNDEFINED_MIXTURE` type, and fallback registry
  row as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Fastidious_Anaerobe_Broth_With_Meat_Granules` to
  `kgmicrobe.ingredient:fastidious_anaerobe_broth_with_meat_granules` with
  `skos:exactMatch` and an empty `other` column.
- `mappings/microbedecoder_residual_research_decomposition.tsv` records the
  medium-level strategy and four component identifiers that are now carried in
  the record.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for
  `MIM:Fastidious_Anaerobe_Broth_With_Meat_Granules`,
  `kgmicrobe.ingredient:fastidious_anaerobe_broth_with_meat_granules`, and
  `Fastidious Anaerobe Broth With Meat Granules` found the active YAML,
  aggregate copy, final SSSOM row, residual-decomposition provenance, and
  ignored aggregate backups; it did not expose a contradictory active mapping.

## Completeness

- The local mixture identity, partial component list, component evidence, type,
  source occurrence, and final SSSOM row are populated.
- Minor: the top-level `notes` field still says "Curator review needed" from
  the original unmapped import even though the record was decomposed, promoted,
  and moved to `data/ingredients/mapped`.

## Recommended Edits

- Minor: replace the stale top-level `notes` with a short summary of the local
  fallback identity and partial curated decomposition, sync
  `data/curated/mapped_ingredients.yaml`, and rerun strict validation.
