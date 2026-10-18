# `data/ingredients/mapped/Ethyl_Methyl_Sulfide.yaml`

## Verdict

Pass. The CultureBotHT CAS-derived ethyl methyl sulfide identity agrees with
active ChEBI, PubChem confirms the recorded structure, and the final SSSOM
`other` tokens are safe.

## Identity

- Reviewed record: `data/ingredients/mapped/Ethyl_Methyl_Sulfide.yaml`.
- Identifier and grounding: `identifier: CHEBI:231886` with matching
  `ontology_mapping.ontology_id`, canonical label `ethyl methyl sulfide`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  and `ingredient_type: SINGLE_INGREDIENT`.
- PubChem lookup by CAS RN `624-89-5` resolved to CID 12230 with formula
  `C3H8S` and the same InChI recorded under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ethyl_Decanoate.yaml data/ingredients/mapped/Ethyl_Methyl_Sulfide.yaml data/ingredients/mapped/Ethyl_octanoate.yaml data/ingredients/mapped/Ethylene_Glycol.yaml data/ingredients/mapped/Ethylenediamine-NN-disuccinic_Acid.yaml --out /tmp/mim_ethyl_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Ethyl_Methyl_Sulfide.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CAS RN, formula, InChI, SMILES, and exact synonym as the
  per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Ethyl_Methyl_Sulfide` to `CHEBI:231886` with `skos:exactMatch`;
  `(methylsulfanyl)ethane` is the curated exact synonym and `CAS:624-89-5`
  belongs to the same subject.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for
  `MIM:Ethyl_Methyl_Sulfide`, `CHEBI:231886`, and `624-89-5` found the active
  YAML, aggregate copy, final SSSOM row, OAK/OLS row-review provenance, and
  expected generated indexes; it did not expose a contradictory active mapping.

## Completeness

- The exact identity, CAS RN, structure fields, exact synonym, and final SSSOM
  payload are populated.
- No unsupported roles, components, source occurrences, or environmental
  contexts are asserted.

## Recommended Edits

- None.
