# `data/ingredients/mapped/Ethidium_Bromide.yaml`

## Verdict

Pass. The supplied salt maps exactly to active ChEBI ethidium bromide, the CAS
structure matches PubChem, and the final SSSOM `other` tokens are valid for the
same salt identity.

## Identity

- Reviewed record: `data/ingredients/mapped/Ethidium_Bromide.yaml`.
- Identifier and grounding: `identifier: CHEBI:4883` with matching
  `ontology_mapping.ontology_id`, canonical label `ethidium bromide`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- PubChem lookup by CAS RN `1239-45-8` resolved to CID 14710 with formula
  `C21H20BrN3` and the same InChI recorded under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ethanolamine.yaml data/ingredients/mapped/Ethidium_Bromide.yaml data/ingredients/mapped/Ethionamide.yaml data/ingredients/mapped/Ethyl_Acetate.yaml data/ingredients/mapped/Ethyl_Benzoate.yaml --out /tmp/mim_eth_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Ethidium_Bromide.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CAS RN, formula, InChI, SMILES, and exact synonym as the
  per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Ethidium_Bromide` to `CHEBI:4883` with `skos:exactMatch`; the
  `3,8-diamino-5-ethyl-6-phenylphenanthridinium bromide` and
  `CAS:1239-45-8` `other` tokens both denote ethidium bromide.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for
  `MIM:Ethidium_Bromide`, `CHEBI:4883`, and `1239-45-8` found the active YAML,
  aggregate copy, final SSSOM row, OAK/OLS row-review provenance, and expected
  generated indexes; it did not expose a contradictory active mapping.

## Completeness

- The exact salt identity, CAS RN, structure fields, exact synonym, and final
  SSSOM payload are populated.
- No unsupported roles, components, source occurrences, or environmental
  contexts are asserted.

## Recommended Edits

- None.
