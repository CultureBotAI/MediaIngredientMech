# `data/ingredients/mapped/Ethylmalonic_Acid.yaml`

## Verdict

Pass. The CultureBotHT CAS-derived ethylmalonic acid identity agrees with
active ChEBI, PubChem confirms the recorded structure, and the final SSSOM
`other` tokens are safe.

## Identity

- Reviewed record: `data/ingredients/mapped/Ethylmalonic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:741548` with matching
  `ontology_mapping.ontology_id`, canonical label `ethylmalonic acid`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- PubChem lookup by CAS RN `601-75-2` resolved to CID 11756 with formula
  `C5H8O4` and the same InChI recorded under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ethylenediamine-NN-disuccinic_acid_EDDS.yaml data/ingredients/mapped/Ethylenediamine_N_N_Prime_Disuccinic_Acid.yaml data/ingredients/mapped/Ethylmalonic_Acid.yaml data/ingredients/mapped/Eudesmic_Acid.yaml data/ingredients/mapped/Eugenol.yaml --out /tmp/mim_edds_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Ethylmalonic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CAS RN, formula, InChI, SMILES, and exact synonym as the
  per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Ethylmalonic_Acid` to `CHEBI:741548` with `skos:exactMatch`;
  `ethylpropanedioic acid` and `CAS:601-75-2` are safe `other` tokens for the
  same ethylmalonic acid identity.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for `MIM:Ethylmalonic_Acid`,
  `CHEBI:741548`, and `601-75-2` found the active YAML, aggregate copy, final
  SSSOM row, OAK/OLS row-review provenance, and expected generated indexes; it
  did not expose a contradictory active mapping.

## Completeness

- The exact identity, CAS RN, structure fields, exact synonym, and final SSSOM
  payload are populated.
- No unsupported roles, components, source occurrences, or environmental
  contexts are asserted.

## Recommended Edits

- None.
