# `data/ingredients/mapped/Enrofloxacin.yaml`

## Verdict

Pass. Enrofloxacin maps to the exact ChEBI term, its PubChem-backed structure
matches the reviewed ChEBI identity, the MicrobeDecoder BacDive source
occurrences are preserved, and the final SSSOM row has no unsafe synonym
payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Enrofloxacin.yaml`.
- Identifier and grounding: `identifier: CHEBI:35720` with matching
  `ontology_mapping.ontology_id`, canonical label `enrofloxacin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, three
  MicrobeDecoder source occurrences, and `ingredient_type: SINGLE_INGREDIENT`.
- `runoak -i ols:chebi info` resolved `CHEBI:35720` to `enrofloxacin`.
- PubChem name lookup for `Enrofloxacin` resolved to CID 71188 with formula
  `C19H22FN3O3` and the same InChI recorded under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Enrofloxacin.yaml data/ingredients/mapped/Enterobactin.yaml data/ingredients/mapped/Epiandrosterone.yaml data/ingredients/mapped/Epigallocatechin.yaml data/ingredients/mapped/Epigallocatechin_Gallate.yaml --out /tmp/mim_epi_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Enrofloxacin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, PubChem-backed structure, MicrobeDecoder source occurrence
  block, and review history as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Enrofloxacin` to `CHEBI:35720` with `skos:exactMatch`, the canonical
  ChEBI object label, and an empty `other` column.
- A hidden/ignored-inclusive search over `data/ingredients`, `mappings`, and
  `reports/yaml_record_review` for `MIM:Enrofloxacin` and `CHEBI:35720` found
  the active YAML, aggregate copy, final SSSOM row, and related MicrobeDecoder
  review/provenance rows; it did not expose a contradictory active mapping.

## Completeness

- The exact identity, structure, molecular weight, MicrobeDecoder provenance,
  source occurrence count, and final SSSOM row are populated.
- CAS RN, nutritional roles, physicochemical roles, biological roles,
  components, and environmental contexts are correctly empty.

## Recommended Edits

- None.
