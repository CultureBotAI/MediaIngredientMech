# `data/ingredients/mapped/Egg_Yolk.yaml`

## Verdict

Pass. Egg yolk maps to the FOODON chicken egg yolk food-product term with the
correct FOODON source, no unsafe SSSOM `other` tokens, and no unsupported
single-chemical assertions.

## Identity

- Reviewed record: `data/ingredients/mapped/Egg_Yolk.yaml`.
- Identifier and grounding: `identifier: FOODON:03315772` with matching
  `ontology_mapping.ontology_id`, canonical label
  `chicken egg yolk food product`, source `FOODON`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- `runoak -i ols:foodon info` resolved `FOODON:03315772` to
  `chicken egg yolk food product`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Egg_Yolk.yaml data/ingredients/mapped/Elastin.yaml data/ingredients/mapped/Emodin.yaml data/ingredients/mapped/Enoxacin.yaml data/ingredients/mapped/Enrichment_Solution_For_Seawater_Medium.yaml --out /tmp/mim_e2_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Egg_Yolk.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  FOODON identifier, ontology source, mixture type, zero occurrence count, and
  curation history as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Egg_Yolk` to `FOODON:03315772` with `skos:exactMatch`, the canonical
  FOODON object label, and an empty `other` column.
- `mappings/ingredient_mappings_synonym_enrich_review.tsv` records that the
  Egg yolk synonym-enrichment text was already represented.
- A hidden/ignored-inclusive search over `data/ingredients`, `mappings`, and
  `reports/yaml_record_review` for `MIM:Egg_Yolk` and `FOODON:03315772` found
  the active YAML, aggregate copy, final SSSOM row, and expected row-review
  TSVs; it did not expose a contradictory active mapping.

## Completeness

- The FOODON identity, mixture classification, and source provenance are
  populated.
- CAS RN, chemical structure, component, nutritional-role, physicochemical-role,
  biological-role, and environmental-context fields are correctly empty.

## Recommended Edits

- None.
