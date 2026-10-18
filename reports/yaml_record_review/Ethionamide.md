# `data/ingredients/mapped/Ethionamide.yaml`

## Verdict

Pass. The CultureBotHT CAS-derived ethionamide identity agrees with active
ChEBI, PubChem confirms the recorded structure, and the final SSSOM payload
contains only same-substance synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Ethionamide.yaml`.
- Identifier and grounding: `identifier: CHEBI:4885` with matching
  `ontology_mapping.ontology_id`, canonical label `ethionamide`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- PubChem lookup by CAS RN `536-33-4` resolved to CID 2761171 with formula
  `C8H10N2S` and the same InChI recorded under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ethanolamine.yaml data/ingredients/mapped/Ethidium_Bromide.yaml data/ingredients/mapped/Ethionamide.yaml data/ingredients/mapped/Ethyl_Acetate.yaml data/ingredients/mapped/Ethyl_Benzoate.yaml --out /tmp/mim_eth_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Ethionamide.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CAS RN, formula, InChI, SMILES, and exact synonym as the
  per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Ethionamide` to `CHEBI:4885` with `skos:exactMatch`;
  `2-ethylpyridine-4-carbothioamide` and `CAS:536-33-4` are safe `other`
  tokens for the same ethionamide identity.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for `MIM:Ethionamide`,
  `CHEBI:4885`, and `536-33-4` found the active YAML, aggregate copy, final
  SSSOM row, OAK/OLS row-review provenance, and expected generated indexes; it
  did not expose a contradictory active mapping.

## Completeness

- The exact identity, CAS RN, structure fields, exact synonym, and final SSSOM
  payload are populated.
- No unsupported roles, components, source occurrences, or environmental
  contexts are asserted.

## Recommended Edits

- None.
