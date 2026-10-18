# `data/ingredients/mapped/Dibenzofuran.yaml`

## Verdict

Pass. The record exact-matches active `CHEBI:28145` dibenzofuran, its
structure fields match ChEBI, its final SSSOM row exports only true ChEBI
synonyms, and the refreshed CultureMech occurrence count is represented.

## Identity

- Reviewed record: `data/ingredients/mapped/Dibenzofuran.yaml`.
- Identifier and grounding: `identifier: CHEBI:28145` with
  `ontology_mapping.ontology_id: CHEBI:28145`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `ingredient_type: SINGLE_INGREDIENT`, and 159 CultureMech occurrences.
- Local OAK resolves `CHEBI:28145` to active `dibenzofuran`, formula
  `C12H8O`, InChI, SMILES, CAS xref `132-64-9`, exact synonym
  `dibenzo[b,d]furan`, and related synonyms including `DBF`,
  `Dibenzofuran`, and `Diphenylene oxide`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Diammonium_tartrate.yaml data/ingredients/mapped/Dibenzofuran.yaml data/ingredients/mapped/Dibenzothiophene.yaml data/ingredients/mapped/Dibucaine.yaml data/ingredients/mapped/Dichloran_02_in_ethanol.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Diammonium_tartrate.yaml data/ingredients/mapped/Dibenzofuran.yaml data/ingredients/mapped/Dibenzothiophene.yaml data/ingredients/mapped/Dibucaine.yaml data/ingredients/mapped/Dichloran_02_in_ethanol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 records.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:63075 CHEBI:28145 CHEBI:23681 CHEBI:247956 CHEBI:27864`:
  returned the canonical ChEBI label, definition, synonyms, CAS xref,
  formula, InChI, SMILES, charge, and mass for `CHEBI:28145`.
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
  found the expected active record, generated/indexed copies, membership rows,
  and row-review rows.
- A focused hidden/ignored-inclusive search of `data/ingredients` for
  `CHEBI:28145` found only `data/ingredients/mapped/Dibenzofuran.yaml`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` and
  `mappings/ingredient_mappings_row_review_manifest.tsv` both record the
  `CHEBI:28145` mapping as confirmed with no row-review action required.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Dibenzofuran` to `CHEBI:28145` with `skos:exactMatch`, canonical
  object label `dibenzofuran`, CHEBI object source, and only `DBF`,
  `dibenzo[b,d]furan`, and `Diphenylene oxide` in `other`.

## Completeness

- Formula, InChI, SMILES, curated synonyms, occurrence statistics, and
  no-action row-review provenance are populated.
- CAS RN is available only as a ChEBI xref, and ingredient roles, supplied
  forms, mixture components, and environmental contexts are correctly empty.

## Recommended Edits

- None.
