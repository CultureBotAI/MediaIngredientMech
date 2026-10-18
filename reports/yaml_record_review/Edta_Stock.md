# `data/ingredients/mapped/Edta_Stock.yaml`

## Verdict

Pass. `EDTA Stock` is modeled as a named local stock solution rather than a
single EDTA compound, and a fresh exact OLS search still found no external term
for this lab preparation.

## Identity

- Reviewed record: `data/ingredients/mapped/Edta_Stock.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:edta_stock` with matching
  `ontology_mapping.ontology_id`, source `kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`,
  `ingredient_type: STOCK_SOLUTION`, `solution_type: OTHER`, and one
  CultureMech occurrence.
- A fresh exact OLS query for `EDTA Stock` across ChEBI, NCIT, MeSH, FOODON,
  and ENVO returned zero documents.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ectoine.yaml data/ingredients/mapped/Edta.yaml data/ingredients/mapped/Edta_Acid_Form.yaml data/ingredients/mapped/Edta_Chelating_Agent.yaml data/ingredients/mapped/Edta_Stock.yaml --out /tmp/mim_edta_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- The LinkML term-label gate was skipped for this file because its identifier
  uses the local `kgmicrobe.ingredient` prefix that the justfile excludes from
  Engine A.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  local identifier, stock-solution type, occurrence count, exact local mapping,
  and curation history as the per-record YAML.
- `mappings/unmapped_ingredients_ols_exact_audit.tsv` found no exact OLS hit
  for the precursor `UNMAPPED_0073` EDTA Stock label.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Edta_Stock` to `kgmicrobe.ingredient:edta_stock` with
  `skos:exactMatch`, local object source, and no `other` tokens.
- A hidden/ignored-inclusive search over `data/ingredients`, `mappings`, and
  `reports/yaml_record_review` found the active YAML, aggregate copy, alias
  records for the historical capitalized MIM CURIE, the OLS audit row, and the
  final SSSOM row; it did not expose an exact external ontology term for this
  named preparation.

## Completeness

- The local identity, stock-solution classification, fallback registry mapping,
  and occurrence count are populated.
- CAS RN, chemical structure, nutritional roles, physicochemical roles,
  biological roles, environmental contexts, and single-ontology parent mappings
  are correctly empty.

## Recommended Edits

- None.
