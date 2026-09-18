# `data/ingredients/mapped/Deoxycholic_Acid.yaml`

## Verdict

Pass. The CultureBotHT CAS-derived record exact-matches active `CHEBI:28834`
deoxycholic acid, the stored CAS, formula, InChI, and SMILES agree with local
ChEBI, and final SSSOM exports only the exact ChEBI synonym plus the same
CAS RN.

## Identity

- Reviewed record: `data/ingredients/mapped/Deoxycholic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:28834` with
  `ontology_mapping.ontology_id: CHEBI:28834`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Local OAK resolves `CHEBI:28834` to active `deoxycholic acid`, a neutral bile
  acid with formula `C24H40O4`, charge `0`, InChI, SMILES, exact synonym
  `3alpha,12alpha-dihydroxy-5beta-cholan-24-oic acid`, and CAS xref
  `83-44-3`.
- The record's formula, InChI, and SMILES agree with the local ChEBI term
  metadata.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Delta-Undecalactone.yaml data/ingredients/mapped/Deoxycholic_Acid.yaml data/ingredients/mapped/Deoxyribonucleic_Acid_From_Herring_Sperm.yaml data/ingredients/mapped/Dermcidin.yaml data/ingredients/mapped/Desferrioxamine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Delta-Undecalactone.yaml data/ingredients/mapped/Deoxycholic_Acid.yaml data/ingredients/mapped/Deoxyribonucleic_Acid_From_Herring_Sperm.yaml data/ingredients/mapped/Dermcidin.yaml data/ingredients/mapped/Desferrioxamine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 records.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:171846 CHEBI:28834 CHEBI:50453`:
  returned formula, charge, InChI, InChIKey, SMILES, mass, synonyms, and xrefs
  for `CHEBI:28834`.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/ingredient_mappings_oak_ols_review.tsv` and
  `mappings/ingredient_mappings_row_review_manifest.tsv` both record the
  `CHEBI:28834` mapping as confirmed with no row-review action required.
- The hidden/ignored-inclusive exact search over active `data/ingredients`,
  `data/curated`, `mappings`, `docs/data`, `src`, `scripts`, and `tests`
  found no second active per-record YAML or stale parent-mapping row for
  `CHEBI:28834`.
- The same hidden/ignored-inclusive search found no
  `mappings/culturemech_recipe_membership.tsv` row for `CHEBI:28834`,
  matching `occurrence_statistics.total_occurrences: 0` and `media_count: 0`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Deoxycholic_Acid` to `CHEBI:28834` with `skos:exactMatch`, canonical
  object label `deoxycholic acid`, CHEBI object source, the exact synonym
  `3alpha,12alpha-dihydroxy-5beta-cholan-24-oic acid` and `CAS:83-44-3` in
  `other`, and an OAK/OLS confirmed validation stamp.

## Completeness

- CAS RN, formula, InChI, SMILES, exact ChEBI synonym, curation history, and
  ChEBI exact identity are populated.
- Mixture components, ingredient roles, supplied forms, and environmental
  contexts are correctly empty for this pure CultureBotHT chemical import.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` and the
  per-record YAML agree.

## Recommended Edits

- None.
