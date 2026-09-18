# `data/ingredients/mapped/Elastin.yaml`

## Verdict

Needs curation. The ChEBI identity itself is valid, but
`degradation: elastin` is an assay/action label rather than an elastin synonym
and is still exported through the final SSSOM `other` column.

## Identity

- Reviewed record: `data/ingredients/mapped/Elastin.yaml`.
- Identifier and grounding: `identifier: CHEBI:4767` with matching
  `ontology_mapping.ontology_id`, canonical label `Elastin`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- `runoak -i ols:chebi info` resolved `CHEBI:4767` to `Elastin`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Egg_Yolk.yaml data/ingredients/mapped/Elastin.yaml data/ingredients/mapped/Emodin.yaml data/ingredients/mapped/Enoxacin.yaml data/ingredients/mapped/Enrichment_Solution_For_Seawater_Medium.yaml --out /tmp/mim_e2_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Elastin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, backfilled raw synonym, zero occurrence count, and curation
  history as the per-record YAML.
- `mappings/ingredient_mappings_row_review_manifest.tsv` records the
  `CHEBI:4767` mapping as `CONFIRMED_NO_ACTION`, supporting the object id and
  label.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Elastin`
  to `CHEBI:4767` with `skos:exactMatch`, but its `other` column is
  `degradation: elastin`. That token describes a degradation capability rather
  than the elastin ingredient.
- A hidden/ignored-inclusive search over `data/ingredients`, `mappings`, and
  `reports/yaml_record_review` found the `degradation: elastin` token in the
  active YAML, aggregate copy, and final SSSOM row; it is not filtered out of
  the published synonym surface.

## Completeness

- The ontology identity and mapping provenance are populated.
- No CAS RN, chemical structure, component, nutritional-role,
  physicochemical-role, biological-role, or environmental-context claims are
  asserted.

## Recommended Edits

- Major: remove `degradation: elastin` from the active synonym surface in
  `data/ingredients/mapped/Elastin.yaml`, or reclassify it as
  rejected/provenance-only so it cannot be exported in final SSSOM `other`.
- After editing the per-record YAML, run `sync-curated`, rebuild SSSOM, and
  rerun `validate-all`, `qc-sssom`, and strict validation.
