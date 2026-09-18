# `data/ingredients/mapped/Ginkgolide_A.yaml`

## Verdict

Pass. The exact `CHEBI:5355` Ginkgolide A identity, CAS RN, structure fields,
and final SSSOM row are consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Ginkgolide_A.yaml`.
- Identifier and grounding: `identifier: CHEBI:5355` with matching
  `ontology_mapping.ontology_id`, canonical label `Ginkgolide A`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- OLS4 resolved `CHEBI:5355` as active Ginkgolide A with CAS xref
  `15291-75-5`, formula `C20H24O9`, and InChI/SMILES matching the YAML.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ginkgolide_A.yaml data/ingredients/mapped/Ginkgotoxin.yaml data/ingredients/mapped/Glebomycin.yaml data/ingredients/mapped/Glucomannan_Konjac.yaml data/ingredients/mapped/Gluconate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Ginkgolide_A.yaml data/ingredients/mapped/Ginkgotoxin.yaml data/ingredients/mapped/Glebomycin.yaml data/ingredients/mapped/Gluconate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four CHEBI/NCIT-primary records in the batch.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry carries
  the same ChEBI exact mapping, CAS RN, structure fields, single-ingredient
  type, and empty synonym set as the per-record YAML.
- `mappings/ingredient_mappings_row_review_manifest.tsv` marks the current
  `Ginkgolide A` to `CHEBI:5355` row as `CONFIRMED_NO_ACTION`.
- The final SSSOM row maps `MIM:Ginkgolide_A` to `CHEBI:5355` by
  `skos:exactMatch` and exports only `CAS:15291-75-5` in `other`.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports` found the active YAML, aggregate copies, the final
  SSSOM and row-review rows, generated indexes, and ignored aggregate backups.

## Completeness

- The exact Ginkgolide A identity, CAS RN, structure fields, ingredient type,
  and final SSSOM row are populated.

## Recommended Edits

- None.
