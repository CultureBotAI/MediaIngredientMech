# `data/ingredients/mapped/Ertapenem.yaml`

## Verdict

Pass. The restored high-accession ChEBI term resolves to ertapenem, the
PubChem-backed structure matches the current record, MicrobeDecoder source
occurrences are preserved, and the final SSSOM row has no unsafe synonym
payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Ertapenem.yaml`.
- Identifier and grounding: `identifier: CHEBI:404903` with matching
  `ontology_mapping.ontology_id`, canonical label `ertapenem`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, six
  MicrobeDecoder BacDive sensitivity occurrences, and
  `ingredient_type: SINGLE_INGREDIENT`.
- `runoak -i ols:chebi info` resolved `CHEBI:404903` to `ertapenem`,
  confirming that the earlier ID ceiling demotion was a false positive.
- PubChem name lookup for `Ertapenem` resolved to CID 150610 with formula
  `C22H25N3O7S` and the same InChI recorded under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Epinephrine.yaml data/ingredients/mapped/Ertapenem.yaml data/ingredients/mapped/Erythromycin.yaml data/ingredients/mapped/Erythromycin_A.yaml data/ingredients/mapped/Erythromycin_B.yaml --out /tmp/mim_ery_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Ertapenem.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  restored ChEBI identifier, exact ontology mapping, MicrobeDecoder source
  occurrence block, structure, and append-only correction history as the
  per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Ertapenem`
  to `CHEBI:404903` with `skos:exactMatch`, the canonical ChEBI object label,
  and an empty `other` column.
- A hidden/ignored-inclusive search over `data/ingredients`, `mappings`, and
  `reports/yaml_record_review` for `MIM:Ertapenem` and `CHEBI:404903` found
  the active YAML, aggregate copy, and final SSSOM row; it did not expose a
  contradictory active mapping.

## Completeness

- The exact identity, structure, molecular weight, MicrobeDecoder provenance,
  source occurrence count, and final SSSOM row are populated.
- CAS RN, nutritional roles, physicochemical roles, biological roles,
  components, and environmental contexts are correctly empty.

## Recommended Edits

- None.
