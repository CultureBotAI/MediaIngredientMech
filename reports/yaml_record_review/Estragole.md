# `data/ingredients/mapped/Estragole.yaml`

## Verdict

Pass. The CultureBotHT CAS-derived estragole identity agrees with active ChEBI,
its structure matches PubChem for the same CAS RN, and the final SSSOM `other`
tokens are safe synonyms for the subject.

## Identity

- Reviewed record: `data/ingredients/mapped/Estragole.yaml`.
- Identifier and grounding: `identifier: CHEBI:4867` with matching
  `ontology_mapping.ontology_id`, canonical label `estragole`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- `runoak -i ols:chebi info` resolved `CHEBI:4867` to active `estragole`.
- PubChem lookup by CAS RN `140-67-0` resolved to CID 8815 with formula
  `C10H12O` and the same InChI recorded under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Erythrose.yaml data/ingredients/mapped/Escin.yaml data/ingredients/mapped/Esculin_Ferric_Citrate.yaml data/ingredients/mapped/Esculin_Monohydrate.yaml data/ingredients/mapped/Estragole.yaml --out /tmp/mim_esc_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Estragole.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CAS RN, formula, InChI, SMILES, and exact synonym as the
  per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Estragole`
  to `CHEBI:4867` with `skos:exactMatch`; `CAS:140-67-0` belongs to the same
  estragole identity, and
  `1-methoxy-4-(prop-2-en-1-yl)benzene` is the curated exact ChEBI synonym.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for `MIM:Estragole`,
  `CHEBI:4867`, and `140-67-0` found the active YAML, aggregate copy, final
  SSSOM row, OAK/OLS row-review provenance, and expected generated indexes; it
  did not expose a contradictory active mapping.

## Completeness

- The exact identity, CAS RN, structure fields, exact synonym, and final SSSOM
  payload are populated.
- No unsupported roles, components, source occurrences, or environmental
  contexts are asserted.

## Recommended Edits

- None.
