# `data/ingredients/mapped/Dipicolinic_Acid.yaml`

## Verdict

Pass. The CultureBotHT record exact-matches active `CHEBI:46837`, the stored
CAS RN, formula, InChI, and SMILES agree with PubChem, OLS resolves the
published ChEBI label and synonym, and final SSSOM exports only the exact
synonym plus `CAS:499-83-2`.

## Identity

- Reviewed record: `data/ingredients/mapped/Dipicolinic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:46837` with
  `ontology_mapping.ontology_id: CHEBI:46837`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `ingredient_type: SINGLE_INGREDIENT`, and 0/0 CultureMech occurrences.
- PubChem resolves CAS `499-83-2` to CID `10367` with formula `C7H5NO4`, the
  stored InChI, and InChIKey `WJJMNDUMQPNECX-UHFFFAOYSA-N`.
- EBI OLS exact search for `dipicolinic acid` resolves `CHEBI:46837` with
  canonical label `dipicolinic acid` and exact synonym
  `PYRIDINE-2,6-DICARBOXYLIC ACID`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Diosgenin.yaml data/ingredients/mapped/Dioxygen.yaml data/ingredients/mapped/Dipicolinic_Acid.yaml data/ingredients/mapped/Disodium_Glutarate.yaml data/ingredients/mapped/Disodium_Malate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Diosgenin.yaml data/ingredients/mapped/Dioxygen.yaml data/ingredients/mapped/Dipicolinic_Acid.yaml data/ingredients/mapped/Disodium_Malate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the 4 CHEBI-label records in the batch; the lowercase MeSH parent
  in `Disodium_Glutarate.yaml` was left to Engine B/product validation.
- `curl -L -sS --max-time 20 "https://www.ebi.ac.uk/ols/api/search?q=dipicolinic%20acid&ontology=chebi&exact=true"`:
  returned live `CHEBI:46837` with label `dipicolinic acid`.
- `curl -L -sS --max-time 20 "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/499-83-2/property/MolecularFormula,InChI,CanonicalSMILES,IsomericSMILES,InChIKey/JSON"`:
  returned PubChem CID `10367` with matching formula, InChI, and InChIKey.
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
  found the expected active record, aggregate copy, generated products,
  row-review confirmations, and ignored aggregate backups.
- A focused hidden/ignored-inclusive search of `data/ingredients` for
  `CHEBI:46837` and `499-83-2` found only
  `data/ingredients/mapped/Dipicolinic_Acid.yaml`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` and
  `mappings/ingredient_mappings_row_review_manifest.tsv` both record the
  `CHEBI:46837` mapping as confirmed with no row-review action required.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Dipicolinic_Acid` to `CHEBI:46837` with `skos:exactMatch`, canonical
  object label `dipicolinic acid`, CHEBI object source, exact synonym
  `PYRIDINE-2,6-DICARBOXYLIC ACID`, and `CAS:499-83-2`.

## Completeness

- CAS RN, formula, InChI, SMILES, CultureBotHT provenance, synonym review
  provenance, and ingredient type are populated.
- The 0/0 occurrence count is acceptable for a CultureBotHT panel record with
  no tracked CultureMech recipe memberships; ingredient roles, supplied forms,
  mixture components, and environmental contexts are correctly empty.

## Recommended Edits

- None.
