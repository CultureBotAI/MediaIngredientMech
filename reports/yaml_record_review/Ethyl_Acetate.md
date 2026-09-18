# `data/ingredients/mapped/Ethyl_Acetate.yaml`

## Verdict

Pass. The record maps exactly to active ChEBI ethyl acetate, the CAS-derived
structure matches PubChem, and the final SSSOM row carries only the same CAS RN
in `other`.

## Identity

- Reviewed record: `data/ingredients/mapped/Ethyl_Acetate.yaml`.
- Identifier and grounding: `identifier: CHEBI:27750` with matching
  `ontology_mapping.ontology_id`, canonical label `ethyl acetate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- PubChem lookup by CAS RN `141-78-6` resolved to CID 8857 with formula
  `C4H8O2` and the same InChI recorded under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ethanolamine.yaml data/ingredients/mapped/Ethidium_Bromide.yaml data/ingredients/mapped/Ethionamide.yaml data/ingredients/mapped/Ethyl_Acetate.yaml data/ingredients/mapped/Ethyl_Benzoate.yaml --out /tmp/mim_eth_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Ethyl_Acetate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CAS RN, formula, InChI, and SMILES as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Ethyl_Acetate` to `CHEBI:27750` with `skos:exactMatch` and
  `CAS:141-78-6`, which belongs to ethyl acetate, as its only `other` token.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for `MIM:Ethyl_Acetate`,
  `CHEBI:27750`, and `141-78-6` found the active YAML, aggregate copy, final
  SSSOM row, OAK/OLS row-review provenance, and expected generated indexes; it
  did not expose a contradictory active mapping.

## Completeness

- The exact identity, CAS RN, structure fields, and final SSSOM payload are
  populated.
- No unsupported synonyms, roles, components, source occurrences, or
  environmental contexts are asserted.

## Recommended Edits

- None.
