# `data/ingredients/mapped/Eugenol.yaml`

## Verdict

Pass. The CultureBotHT CAS-derived eugenol identity agrees with active ChEBI,
PubChem confirms the recorded structure, and the final SSSOM `other` tokens
are safe.

## Identity

- Reviewed record: `data/ingredients/mapped/Eugenol.yaml`.
- Identifier and grounding: `identifier: CHEBI:4917` with matching
  `ontology_mapping.ontology_id`, canonical label `eugenol`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- PubChem lookup by CAS RN `97-53-0` resolved to CID 3314 with formula
  `C10H12O2` and the same InChI recorded under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ethylenediamine-NN-disuccinic_acid_EDDS.yaml data/ingredients/mapped/Ethylenediamine_N_N_Prime_Disuccinic_Acid.yaml data/ingredients/mapped/Ethylmalonic_Acid.yaml data/ingredients/mapped/Eudesmic_Acid.yaml data/ingredients/mapped/Eugenol.yaml --out /tmp/mim_edds_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Eugenol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CAS RN, formula, InChI, SMILES, and exact synonym as the
  per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Eugenol`
  to `CHEBI:4917` with `skos:exactMatch`; the
  `2-methoxy-4-(prop-2-en-1-yl)phenol` and `CAS:97-53-0` `other` tokens both
  denote eugenol.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for `MIM:Eugenol`,
  `CHEBI:4917`, and `97-53-0` found the active YAML, aggregate copy, final
  SSSOM row, OAK/OLS row-review provenance, and expected generated indexes; it
  did not expose a contradictory active mapping.

## Completeness

- The exact identity, CAS RN, structure fields, exact synonym, and final SSSOM
  payload are populated.
- No unsupported roles, components, source occurrences, or environmental
  contexts are asserted.

## Recommended Edits

- None.
