# `data/ingredients/mapped/Enoxacin.yaml`

## Verdict

Pass. Enoxacin maps to the exact ChEBI term, its PubChem-backed structure
matches the reviewed ChEBI identity, the MicrobeDecoder BacDive source
occurrences are preserved, and the final SSSOM row has no unsafe synonym
payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Enoxacin.yaml`.
- Identifier and grounding: `identifier: CHEBI:157175` with matching
  `ontology_mapping.ontology_id`, canonical label `enoxacin`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, four
  MicrobeDecoder source occurrences, and `ingredient_type: SINGLE_INGREDIENT`.
- `runoak -i ols:chebi info` resolved `CHEBI:157175` to `enoxacin`.
- PubChem name lookup for `Enoxacin` resolved to CID 3229 with formula
  `C15H17FN4O3` and the same InChI recorded under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Egg_Yolk.yaml data/ingredients/mapped/Elastin.yaml data/ingredients/mapped/Emodin.yaml data/ingredients/mapped/Enoxacin.yaml data/ingredients/mapped/Enrichment_Solution_For_Seawater_Medium.yaml --out /tmp/mim_e2_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Enoxacin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, structure, MicrobeDecoder source occurrence block, and
  review history as the per-record YAML.
- `mappings/microbedecoder_auto_mapped_review.tsv` records the
  `CHEBI:157175` Enoxacin row as `APPROVED` after the local OAK id resolved
  and its canonical label exact-matched the imported ontology label
  case-insensitively.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Enoxacin`
  to `CHEBI:157175` with `skos:exactMatch`, the canonical ChEBI object label,
  and an empty `other` column.
- A hidden/ignored-inclusive search over `data/ingredients`, `mappings`, and
  `reports/yaml_record_review` for `MIM:Enoxacin` and `CHEBI:157175` found
  the active YAML, aggregate copy, MicrobeDecoder review row, and final SSSOM
  row; it did not expose a contradictory active mapping.

## Completeness

- The exact identity, structure, molecular weight, MicrobeDecoder provenance,
  source occurrence count, and final SSSOM row are populated.
- CAS RN, nutritional roles, physicochemical roles, biological roles,
  components, and environmental contexts are correctly empty.

## Recommended Edits

- None.
