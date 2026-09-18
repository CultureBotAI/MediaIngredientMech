# `data/ingredients/mapped/3-acetylpyridine.yaml`

## Verdict

Pass with minor issues, minor. The exact `CHEBI:166501`
`3-Acetylpyridine` identity, CAS, IUPAC synonym, ChEBI chemistry, SSSOM row, and
aggregate row pass; only stale research-validation rows still ask for the direct
ChEBI verification that now passes.

## Identity

- Reviewed record: `data/ingredients/mapped/3-acetylpyridine.yaml`.
- Identifier and grounding: `identifier: CHEBI:166501` with
  `ontology_mapping.ontology_id: CHEBI:166501`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:166501`
  resolves to `3-Acetylpyridine`, lists formula `C7H7NO`, carries CAS
  `350-03-8`, and matches the record InChI and SMILES.
- The `1-pyridin-3-ylethanone` synonym is represented as an `EXACT_SYNONYM`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/3-Pyridinesulfonic_Acid.yaml data/ingredients/mapped/3-_N-morpholinopropanesulfonic_Acid.yaml data/ingredients/mapped/3-acetylpyridine.yaml data/ingredients/mapped/3-aminobenzoate.yaml data/ingredients/mapped/3-aminobutyrate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/3-acetylpyridine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:3-acetylpyridine` to `CHEBI:166501` row with
  `1-pyridin-3-ylethanone|CAS:350-03-8` in `other`.

## Evidence

- The active ChEBI page confirms the current ontology label, formula, structure,
  and CAS RN.
- The OAK/OLS row-review surface already records this row as `CONFIRMED`.
- Stale: `mappings/record_research_validation.tsv` and its Markdown summary
  still contain old rows asking for direct `CHEBI:166501` verification. The
  direct ChEBI check now verifies the active term, formula, and structure.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `scripts`, `conf`, `src`, and `tests` found the active YAML,
  aggregate, SSSOM, OAK/OLS review, generated docs, and stale advisory rows.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- Core ChEBI chemistry is complete.
- No record-local curation defect remains.

## Recommended Edits

No YAML edit is required for this record. The stale advisory rows can be
ignored or refreshed when `mappings/record_research_validation.tsv` is rebuilt.
