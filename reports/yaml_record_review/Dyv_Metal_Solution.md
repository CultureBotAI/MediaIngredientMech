# `data/ingredients/mapped/Dyv_Metal_Solution.yaml`

## Verdict

Pass. DYV Metal Solution is a named CultureMech trace-metal preparation without
an exact external ontology term, and the record correctly uses a local
`kgmicrobe.ingredient` identity with no misleading single-compound parent.

## Identity

- Reviewed record: `data/ingredients/mapped/Dyv_Metal_Solution.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:dyv_metal_solution` with matching
  `ontology_mapping.ontology_id`, source `kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`,
  `ingredient_type: STOCK_SOLUTION`, `solution_type: TRACE_METAL_MIX`, and 2
  CultureMech source occurrences.
- A fresh OLS search across ChEBI, NCIT, MeSH, FOODON, and ENVO for `DYV Metal
  Solution` found no exact external ontology term.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Dry_Cow-manure.yaml data/ingredients/mapped/Duartin.yaml data/ingredients/mapped/Durhamycin.yaml data/ingredients/mapped/Dynemicin.yaml data/ingredients/mapped/Dyv_Metal_Solution.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dry_Cow-manure.yaml data/ingredients/mapped/Dynemicin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed the ENVO and NCIT files. Duartin, Durhamycin, and DYV Metal Solution
  were skipped because they use `mesh:`, `cas:`, or local `kgmicrobe.*`
  identifiers outside this subset.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.

## Evidence

- `data/curated/mapped_ingredients.yaml` contains the same maintained record
  body as the per-record YAML.
- A hidden/ignored-inclusive exact search over `data/ingredients` and
  `mappings` for `kgmicrobe.ingredient:dyv_metal_solution` found only the
  active DYV Metal Solution YAML and its final local SSSOM row.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Dyv_Metal_Solution` to local
  `kgmicrobe.ingredient:dyv_metal_solution` with `skos:exactMatch`, local
  object source, and no `other` tokens.

## Completeness

- The local identity, named stock-solution type, trace-metal mix type, and
  CultureMech occurrence count are populated.
- CAS RN, chemical structure, supplied forms, nutritional roles,
  physicochemical roles, biological roles, environmental contexts, and
  single-ontology parent mappings are correctly empty.

## Recommended Edits

- None.
