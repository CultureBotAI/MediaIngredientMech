# `data/ingredients/mapped/3-aminobenzoate.yaml`

## Verdict

Pass, none. The exact `CHEBI:30761` `3-aminobenzoate` identity, CAS, ChEBI
chemistry, SSSOM row, aggregate row, and generated docs all agree.

## Identity

- Reviewed record: `data/ingredients/mapped/3-aminobenzoate.yaml`.
- Identifier and grounding: `identifier: CHEBI:30761` with
  `ontology_mapping.ontology_id: CHEBI:30761`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:30761`
  resolves to `3-aminobenzoate`, lists formula `C7H6NO2`, carries CAS
  `2906-33-4`, and matches the record InChI and SMILES.
- Empty `synonyms: []` is acceptable for this anion record.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/3-Pyridinesulfonic_Acid.yaml data/ingredients/mapped/3-_N-morpholinopropanesulfonic_Acid.yaml data/ingredients/mapped/3-acetylpyridine.yaml data/ingredients/mapped/3-aminobenzoate.yaml data/ingredients/mapped/3-aminobutyrate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/3-aminobenzoate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:3-aminobenzoate` to `CHEBI:30761` row with `CAS:2906-33-4` in `other`.

## Evidence

- The active ChEBI page confirms the anion identity, formula, structure, and CAS
  RN.
- The OAK/OLS row-review surface already records this row as `CONFIRMED`.
- `occurrence_statistics` reports `0/0`; the record came from CultureBotHT CAS
  input rather than a counted CultureMech recipe occurrence.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `scripts`, `conf`, `src`, and `tests` found the active YAML,
  aggregate, SSSOM, OAK/OLS review, and generated docs rows.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- Core ChEBI chemistry is complete.
- No record-local curation defect remains.

## Recommended Edits

No YAML edit is required for this record.
