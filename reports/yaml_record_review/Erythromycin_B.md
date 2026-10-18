# `data/ingredients/mapped/Erythromycin_B.yaml`

## Verdict

Pass. Erythromycin B maps to the exact ChEBI term, its PubChem-backed structure
matches the record, the MicrobeDecoder source occurrence is preserved, and the
final SSSOM row has no unsafe synonym payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Erythromycin_B.yaml`.
- Identifier and grounding: `identifier: CHEBI:28196` with matching
  `ontology_mapping.ontology_id`, canonical label `erythromycin B`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, one
  MicrobeDecoder BacDive metabolite-production occurrence, and
  `ingredient_type: SINGLE_INGREDIENT`.
- `runoak -i ols:chebi info` resolved `CHEBI:28196` to `erythromycin B`.
- PubChem name lookup for `Erythromycin B` resolved to CID 9918244 with formula
  `C37H67NO12` and the same InChI recorded under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Epinephrine.yaml data/ingredients/mapped/Ertapenem.yaml data/ingredients/mapped/Erythromycin.yaml data/ingredients/mapped/Erythromycin_A.yaml data/ingredients/mapped/Erythromycin_B.yaml --out /tmp/mim_ery_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Erythromycin_B.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, structure, MicrobeDecoder source occurrence block, and
  review history as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Erythromycin_B` to `CHEBI:28196` with `skos:exactMatch`, the canonical
  ChEBI object label, and an empty `other` column.
- A hidden/ignored-inclusive search over `data/ingredients`, `mappings`, and
  `reports/yaml_record_review` for `MIM:Erythromycin_B` and `CHEBI:28196`
  found the active YAML, aggregate copy, and final SSSOM row; it did not expose
  a contradictory active mapping.

## Completeness

- The exact identity, structure, molecular weight, MicrobeDecoder provenance,
  source occurrence count, and final SSSOM row are populated.
- CAS RN, nutritional roles, physicochemical roles, biological roles,
  components, and environmental contexts are correctly empty.

## Recommended Edits

- None.
