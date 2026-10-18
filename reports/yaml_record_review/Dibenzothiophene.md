# `data/ingredients/mapped/Dibenzothiophene.yaml`

## Verdict

Pass. The CultureBotHT CAS-derived record exact-matches active `CHEBI:23681`
dibenzothiophene, its formula, InChI, SMILES, and CAS RN agree with ChEBI, and
the final SSSOM row publishes only true same-compound aliases.

## Identity

- Reviewed record: `data/ingredients/mapped/Dibenzothiophene.yaml`.
- Identifier and grounding: `identifier: CHEBI:23681` with
  `ontology_mapping.ontology_id: CHEBI:23681`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `ingredient_type: SINGLE_INGREDIENT`, and 0/0 CultureMech occurrences.
- Local OAK resolves `CHEBI:23681` to active `dibenzothiophene`, formula
  `C12H8S`, InChI, SMILES, CAS xref `132-65-0`, exact synonym
  `dibenzo[b,d]thiophene`, and related synonyms for the same compound.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Diammonium_tartrate.yaml data/ingredients/mapped/Dibenzofuran.yaml data/ingredients/mapped/Dibenzothiophene.yaml data/ingredients/mapped/Dibucaine.yaml data/ingredients/mapped/Dichloran_02_in_ethanol.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Diammonium_tartrate.yaml data/ingredients/mapped/Dibenzofuran.yaml data/ingredients/mapped/Dibenzothiophene.yaml data/ingredients/mapped/Dibucaine.yaml data/ingredients/mapped/Dichloran_02_in_ethanol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 records.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:63075 CHEBI:28145 CHEBI:23681 CHEBI:247956 CHEBI:27864`:
  returned the canonical ChEBI label, definition, synonyms, CAS xref,
  formula, InChI, SMILES, charge, and mass for `CHEBI:23681`.
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
  `CHEBI:23681` found only
  `data/ingredients/mapped/Dibenzothiophene.yaml`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` and
  `mappings/ingredient_mappings_row_review_manifest.tsv` both record the
  `CHEBI:23681` mapping as confirmed with no row-review action required.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Dibenzothiophene` to `CHEBI:23681` with `skos:exactMatch`, canonical
  object label `dibenzothiophene`, CHEBI object source,
  `dibenzo[b,d]thiophene`, and `CAS:132-65-0`.

## Completeness

- CAS RN, formula, InChI, SMILES, the CultureBotHT provenance, and no-action
  row-review provenance are populated.
- The 0/0 occurrence count is acceptable for a CultureBotHT panel record with
  no tracked CultureMech recipe memberships; ingredient roles, supplied forms,
  mixture components, and environmental contexts are correctly empty.

## Recommended Edits

- None.
