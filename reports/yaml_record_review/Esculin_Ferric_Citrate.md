# `data/ingredients/mapped/Esculin_Ferric_Citrate.yaml`

## Verdict

Pass with minor issues. The record correctly preserves `Esculin Ferric Citrate`
as a local two-component reagent with explicit esculin and iron(III) citrate
parts, but a top-level import note and one curation note still describe the
older unresolved review state.

## Identity

- Reviewed record: `data/ingredients/mapped/Esculin_Ferric_Citrate.yaml`.
- Identifier and grounding: `identifier:
  kgmicrobe.ingredient:esculin_ferric_citrate` with matching
  `ontology_mapping.ontology_id`, local source `kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`,
  164 MicrobeDecoder BacDive metabolite-production/utilization occurrences,
  and `ingredient_type: NAMED_MEDIUM`.
- `runoak -i ols:chebi info` resolved the external component IDs
  `CHEBI:4853` and `CHEBI:144421` to `esculin` and `iron(III) citrate`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Erythrose.yaml data/ingredients/mapped/Escin.yaml data/ingredients/mapped/Esculin_Ferric_Citrate.yaml data/ingredients/mapped/Esculin_Monohydrate.yaml data/ingredients/mapped/Estragole.yaml --out /tmp/mim_esc_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- Engine A term validation was skipped for this record because the ontology ID
  uses the local `kgmicrobe.ingredient` prefix rather than an OBO prefix.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  the full catalog had 83 decompositions, 505 components, and 0 violations.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  local identifier, source occurrence block, esculin plus iron(III) citrate
  component list, `LABEL_ENUMERATION` component assertion, and typed component
  migration history as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Esculin_Ferric_Citrate` to
  `kgmicrobe.ingredient:esculin_ferric_citrate` with `skos:exactMatch` and an
  empty `other` column.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for
  `MIM:Esculin_Ferric_Citrate`,
  `kgmicrobe.ingredient:esculin_ferric_citrate`, `CHEBI:4853`, and
  `CHEBI:144421` found the active YAML, aggregate copy, final SSSOM row, and
  expected component references; it did not expose a contradictory active
  mapping.

## Completeness

- The local identity, two named components, source-label evidence, occurrence
  source, and final kgmicrobe registry row are populated.
- Minor: the top-level `notes` still says "no CAS-RN or CHEBI/NCIT match.
  Curator review needed.", and the original decomposition evidence note still
  contains the retired spelling `ingredient_type=DEFINED_MEDIUM`. The later
  curation history shows the record is now mapped and has typed partonomy, so
  these are stale prose rather than identity or export defects.

## Recommended Edits

- Minor: in `data/ingredients/mapped/Esculin_Ferric_Citrate.yaml`, refresh the
  old top-level `notes` and stale decomposition evidence text to describe the
  current local fallback identity and `NAMED_MEDIUM` enum spelling; then sync
  `data/curated/mapped_ingredients.yaml` and rerun strict validation plus
  `scripts/validate_component_partonomy.py`.
