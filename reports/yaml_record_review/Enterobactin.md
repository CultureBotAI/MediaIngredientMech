# `data/ingredients/mapped/Enterobactin.yaml`

## Verdict

Needs curation. The exact ChEBI identity, CAS chemistry, and final SSSOM row
pass, but the chelator role is still a provisional CHEBI-ancestry inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Enterobactin.yaml`.
- Identifier and grounding: `identifier: CHEBI:28855` with matching
  `ontology_mapping.ontology_id`, canonical label `enterobactin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- `runoak -i ols:chebi info` resolved `CHEBI:28855` to `enterobactin`.
- PubChem resolved CAS RN `28384-96-5` to CID 34231 with formula
  `C30H27N3O15` and the same InChI recorded under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Enrofloxacin.yaml data/ingredients/mapped/Enterobactin.yaml data/ingredients/mapped/Epiandrosterone.yaml data/ingredients/mapped/Epigallocatechin.yaml data/ingredients/mapped/Epigallocatechin_Gallate.yaml --out /tmp/mim_epi_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Enterobactin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CAS RN, formula, InChI, SMILES, exact synonym, zero
  occurrence count, and provisional `CHELATOR` role as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Enterobactin` to `CHEBI:28855` with `skos:exactMatch`, the canonical
  ChEBI object label, the curated long exact synonym, and `CAS:28384-96-5`;
  both `other` tokens denote enterobactin.
- `mappings/ingredient_mappings_row_review_manifest.tsv` records the OAK/OLS
  pass as `CONFIRMED_NO_ACTION`.
- A hidden/ignored-inclusive search over `data/ingredients`, `mappings`, and
  `reports/yaml_record_review` for `MIM:Enterobactin`, `CHEBI:28855`, and
  `28384-96-5` found the active YAML, aggregate copy, final SSSOM row, and
  expected row-review TSVs; it did not expose a contradictory active mapping.
- The only `CHELATOR` role evidence is
  `reference_type: COMPUTATIONAL_PREDICTION` from
  `infer_roles_from_chebi_ancestry`, with a curator note explicitly marking
  the role provisional.

## Completeness

- The exact identity, CAS RN, formula, InChI, SMILES, exact synonym, and final
  SSSOM payload are populated.

## Recommended Edits

- Major: in `data/ingredients/mapped/Enterobactin.yaml`, either replace the
  provisional `physicochemical_roles.CHELATOR` evidence with claim-level
  support for enterobactin in MIM media, or remove the role.
- After editing the per-record YAML, run `sync-curated`, then rerun
  `validate-all`, `qc-sssom`, and strict validation.
