# `data/ingredients/mapped/Epiandrosterone.yaml`

## Verdict

Pass. Epiandrosterone is grounded to the exact ChEBI term, the CAS-derived
structure matches PubChem, and the final SSSOM row publishes only a
same-substance ChEBI synonym plus the matching CAS token.

## Identity

- Reviewed record: `data/ingredients/mapped/Epiandrosterone.yaml`.
- Identifier and grounding: `identifier: CHEBI:541975` with matching
  `ontology_mapping.ontology_id`, canonical label `epiandrosterone`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- `runoak -i ols:chebi info` resolved `CHEBI:541975` to
  `epiandrosterone`.
- PubChem resolved CAS RN `481-29-8` to CID 441302 with formula `C19H30O2`
  and the same InChI recorded under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Enrofloxacin.yaml data/ingredients/mapped/Enterobactin.yaml data/ingredients/mapped/Epiandrosterone.yaml data/ingredients/mapped/Epigallocatechin.yaml data/ingredients/mapped/Epigallocatechin_Gallate.yaml --out /tmp/mim_epi_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Epiandrosterone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CAS RN, formula, InChI, SMILES, exact synonym, and zero
  occurrence count as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Epiandrosterone` to `CHEBI:541975` with `skos:exactMatch`, the
  canonical ChEBI object label, and
  `3beta-hydroxy-5alpha-androstan-17-one|CAS:481-29-8`; both `other` tokens
  denote epiandrosterone.
- `mappings/ingredient_mappings_row_review_manifest.tsv` records the OAK/OLS
  pass as `CONFIRMED_NO_ACTION`.
- A hidden/ignored-inclusive search over `data/ingredients`, `mappings`, and
  `reports/yaml_record_review` for `MIM:Epiandrosterone`, `CHEBI:541975`, and
  `481-29-8` found the active YAML, aggregate copy, final SSSOM row, and
  expected row-review TSVs; it did not expose a contradictory active mapping.

## Completeness

- The exact identity, CAS RN, formula, InChI, SMILES, exact synonym, and final
  SSSOM payload are populated.
- No unsupported nutritional, physicochemical, biological, component, or
  environmental claims are asserted.

## Recommended Edits

- None.
