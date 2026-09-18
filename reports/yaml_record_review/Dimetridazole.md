# `data/ingredients/mapped/Dimetridazole.yaml`

## Verdict

Pass. The CultureBotHT record exact-matches active `CHEBI:141155`
dimetridazole, its CAS RN and structure fields agree with PubChem/ChEBI, and
the final SSSOM row exports only exact/related synonyms plus `CAS:551-92-8`.

## Identity

- Reviewed record: `data/ingredients/mapped/Dimetridazole.yaml`.
- Identifier and grounding: `identifier: CHEBI:141155` with
  `ontology_mapping.ontology_id: CHEBI:141155`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `ingredient_type: SINGLE_INGREDIENT`, and 0/0 CultureMech occurrences.
- Local OAK resolves `CHEBI:141155` to active `dimetridazole`, formula
  `C5H7N3O2`, the stored InChI, the stored SMILES, exact synonym
  `1,2-dimethyl-5-nitro-1H-imidazole`, and related synonyms for the same
  compound.
- PubChem resolves CAS `551-92-8` to CID `3090` with the same formula, InChI,
  and InChIKey `IBXPYPUJPLLOIN-UHFFFAOYSA-N`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Dimethyl_Sulfoxide.yaml data/ingredients/mapped/Dimethylamine.yaml data/ingredients/mapped/Dimethylfraxetin.yaml data/ingredients/mapped/Dimethylsulfoniopropionate_Hydrochloride.yaml data/ingredients/mapped/Dimetridazole.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dimethyl_Sulfoxide.yaml data/ingredients/mapped/Dimethylamine.yaml data/ingredients/mapped/Dimethylfraxetin.yaml data/ingredients/mapped/Dimethylsulfoniopropionate_Hydrochloride.yaml data/ingredients/mapped/Dimetridazole.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 records.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:28262 CHEBI:17170 CHEBI:93172 CHEBI:16457 CHEBI:141155`:
  returned the active ChEBI label, formula, InChI, SMILES, charge, and synonym
  metadata for `CHEBI:141155`.
- `curl -L -sS --max-time 20 "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/551-92-8/property/MolecularFormula,InChI,CanonicalSMILES,IsomericSMILES,InChIKey/JSON"`:
  returned PubChem CID `3090` with matching formula, InChI, and InChIKey.
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
  found the expected active record, aggregate copy, SSSOM row, row-review
  confirmations, generated products, and ignored aggregate backups.
- A focused hidden/ignored-inclusive search of `data/ingredients` for
  `CHEBI:141155` and `551-92-8` found only
  `data/ingredients/mapped/Dimetridazole.yaml`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` and
  `mappings/ingredient_mappings_row_review_manifest.tsv` both record the
  `CHEBI:141155` mapping as confirmed with no row-review action required.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Dimetridazole` to `CHEBI:141155` with `skos:exactMatch`, canonical
  object label `dimetridazole`, CHEBI object source, the exact/related ChEBI
  same-compound synonyms, and `CAS:551-92-8`.

## Completeness

- CAS RN, formula, InChI, SMILES, CultureBotHT provenance, synonym review
  provenance, and ingredient type are populated.
- The 0/0 occurrence count is acceptable for a CultureBotHT panel record with
  no tracked CultureMech recipe memberships; ingredient roles, supplied forms,
  mixture components, and environmental contexts are correctly empty.

## Recommended Edits

- None.
