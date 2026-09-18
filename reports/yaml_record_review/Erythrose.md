# `data/ingredients/mapped/Erythrose.yaml`

## Verdict

Pass. The MicrobeDecoder exact-label ChEBI grounding resolves to the generic
erythrose term, the per-record and aggregate YAML agree, and the final SSSOM
row has no unsafe synonym payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Erythrose.yaml`.
- Identifier and grounding: `identifier: CHEBI:33946` with matching
  `ontology_mapping.ontology_id`, canonical label `erythrose`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, one
  MicrobeDecoder BacDive metabolite-utilization occurrence, and
  `ingredient_type: SINGLE_INGREDIENT`.
- `runoak -i ols:chebi info` resolved `CHEBI:33946` to active `erythrose`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Erythrose.yaml data/ingredients/mapped/Escin.yaml data/ingredients/mapped/Esculin_Ferric_Citrate.yaml data/ingredients/mapped/Esculin_Monohydrate.yaml data/ingredients/mapped/Estragole.yaml --out /tmp/mim_esc_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Erythrose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, MicrobeDecoder occurrence block, ingredient type, and
  reviewed promotion history as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Erythrose`
  to `CHEBI:33946` with `skos:exactMatch`, the canonical ChEBI object label,
  and an empty `other` column.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for `MIM:Erythrose`,
  `CHEBI:33946`, and `kgmicrobe.trait:erythrose` found the active YAML,
  aggregate copy, final SSSOM row, and MicrobeDecoder review provenance; it did
  not expose a contradictory active mapping.

## Completeness

- The exact identity, source occurrence, and final SSSOM row are populated.
- CAS RN, roles, components, environmental contexts, and final SSSOM synonyms
  are correctly empty.

## Recommended Edits

- None.
