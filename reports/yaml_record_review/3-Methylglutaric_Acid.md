# `data/ingredients/mapped/3-Methylglutaric_Acid.yaml`

## Verdict

Pass, none. The exact `CHEBI:68566` `3-methylglutaric acid` identity, CAS
cross-reference, ChEBI chemistry, SSSOM row, aggregate row, and exported docs
all agree.

## Identity

- Reviewed record: `data/ingredients/mapped/3-Methylglutaric_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:68566` with
  `ontology_mapping.ontology_id: CHEBI:68566`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:68566`
  resolves to `3-methylglutaric acid`, lists formula `C6H10O4`, SMILES
  `CC(CC(=O)O)CC(=O)O`, the same standard InChI recorded in the YAML, and CAS
  `626-51-7`.
- The `3-methylpentanedioic acid` synonym is the ChEBI IUPAC name and is
  represented as an `EXACT_SYNONYM`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/3-Methylglutaric_Acid.yaml data/ingredients/mapped/3-O-Methyl-D-glucopyranose.yaml data/ingredients/mapped/3-O-methyl-glucose.yaml data/ingredients/mapped/3-O-methyl_Alpha-D-glucopyranoside.yaml data/ingredients/mapped/3-O-methylgallate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/3-Methylglutaric_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:3-Methylglutaric_Acid` to `CHEBI:68566` row with
  `3-methylpentanedioic acid|CAS:626-51-7` in the SSSOM `other` field.

## Evidence

- The active ChEBI page confirms the current ontology label, formula, structure,
  and CAS RN.
- `occurrence_statistics` reports `0/0`; the record came from CultureBotHT CAS
  input rather than a counted CultureMech recipe occurrence.
- The OAK/OLS row-review surface already records this row as `CONFIRMED`.
- A hidden/ignored-inclusive search over `data`, `mappings`, `reports`, `docs`,
  `scripts`, `conf`, `src`, and `tests` found the active YAML, aggregate, SSSOM,
  OAK/OLS review, and generated docs rows. A narrower hidden/ignored-inclusive
  search of `mappings/record_research_validation.tsv` and
  `reports/yaml_record_review_batch` found no stale advisory rows for
  `3-Methylglutaric_Acid`/`CHEBI:68566`.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- Core ChEBI chemistry is complete.
- No record-local curation defect remains.

## Recommended Edits

No YAML edit is required for this record.
