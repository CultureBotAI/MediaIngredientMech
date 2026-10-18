# `data/ingredients/mapped/Ethambutol.yaml`

## Verdict

Pass. The base ethambutol record maps exactly to active ChEBI, the CultureBotHT
CAS structure matches PubChem, and the final SSSOM `other` tokens are the
curated exact synonym and same-substance CAS token.

## Identity

- Reviewed record: `data/ingredients/mapped/Ethambutol.yaml`.
- Identifier and grounding: `identifier: CHEBI:4877` with matching
  `ontology_mapping.ontology_id`, canonical label `ethambutol`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- PubChem lookup by CAS RN `74-55-5` resolved to CID 14052 with formula
  `C10H24N2O2` and the same InChI recorded under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Etabetacin.yaml data/ingredients/mapped/Etamycin.yaml data/ingredients/mapped/Ethambutol.yaml data/ingredients/mapped/Ethambutol_Dihydrochloride.yaml data/ingredients/mapped/Ethanol.yaml --out /tmp/mim_eta_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Ethambutol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CAS RN, formula, InChI, SMILES, and exact synonym as the
  per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Ethambutol` to `CHEBI:4877` with `skos:exactMatch`; the
  `(2S,2'S)-2,2'-(ethane-1,2-diyldiimino)dibutan-1-ol` and `CAS:74-55-5`
  `other` tokens both denote the same base ethambutol identity.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for `MIM:Ethambutol`,
  `CHEBI:4877`, and `74-55-5` found the active YAML, aggregate copy, final
  SSSOM row, OAK/OLS row-review provenance, and expected generated indexes; it
  did not expose a contradictory active mapping.

## Completeness

- The exact identity, CAS RN, structure fields, exact synonym, and final SSSOM
  payload are populated.
- No unsupported roles, components, source occurrences, or environmental
  contexts are asserted.

## Recommended Edits

- None.
