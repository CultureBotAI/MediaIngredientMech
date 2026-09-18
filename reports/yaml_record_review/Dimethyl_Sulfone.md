# `data/ingredients/mapped/Dimethyl_Sulfone.yaml`

## Verdict

Pass. The CultureBotHT CAS lookup resolves to live `CHEBI:9349`
sulfonyldimethane, the stored CAS RN, formula, InChI, and SMILES are
internally consistent, and the final SSSOM row exports only `CAS:67-71-0`.

## Identity

- Reviewed record: `data/ingredients/mapped/Dimethyl_Sulfone.yaml`.
- Identifier and grounding: `identifier: CHEBI:9349` with
  `ontology_mapping.ontology_id: CHEBI:9349`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`,
  `ingredient_type: SINGLE_INGREDIENT`, and 0/0 CultureMech occurrences.
- EBI OLS resolves the exact ChEBI label `sulfonyldimethane` to
  `CHEBI:9349` and lists `dimethyl sulfone` as a related synonym.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Dihydrostreptomycin.yaml data/ingredients/mapped/Dihydroxyacetone.yaml data/ingredients/mapped/Dimethyl_Disulfide.yaml data/ingredients/mapped/Dimethyl_Sulfide.yaml data/ingredients/mapped/Dimethyl_Sulfone.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dihydrostreptomycin.yaml data/ingredients/mapped/Dihydroxyacetone.yaml data/ingredients/mapped/Dimethyl_Disulfide.yaml data/ingredients/mapped/Dimethyl_Sulfide.yaml data/ingredients/mapped/Dimethyl_Sulfone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 records.
- `curl -L -sS --max-time 20 "https://www.ebi.ac.uk/ols/api/search?q=sulfonyldimethane&ontology=chebi&exact=true"`:
  returned live `CHEBI:9349` with label `sulfonyldimethane`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus
  plausibility warnings.

## Evidence

- `data/curated/mapped_ingredients.yaml` contains the same maintained record
  body as the per-record YAML.
- The hidden/ignored-inclusive exact search over `data/ingredients`,
  `data/curated`, `mappings`, `docs/data`, `src`, `scripts`, and `tests`
  found the expected active record, generated/indexed copies, and row-review
  rows.
- A focused hidden/ignored-inclusive search of `data/ingredients` for
  `CHEBI:9349` found only `data/ingredients/mapped/Dimethyl_Sulfone.yaml`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` and
  `mappings/ingredient_mappings_row_review_manifest.tsv` both record the
  `CHEBI:9349` mapping as confirmed with no row-review action required.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Dimethyl_Sulfone` to `CHEBI:9349` with `skos:exactMatch`, canonical
  object label `sulfonyldimethane`, CHEBI object source, and `CAS:67-71-0`.

## Completeness

- CAS RN, formula, InChI, SMILES, CultureBotHT provenance, CAS lookup regrade
  history, and row-review provenance are populated.
- The 0/0 occurrence count is acceptable for a CultureBotHT panel record with
  no tracked CultureMech recipe memberships; ingredient roles, supplied forms,
  mixture components, and environmental contexts are correctly empty.

## Recommended Edits

- None.
