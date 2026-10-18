# `data/ingredients/mapped/2-pentyl-furan.yaml`

## Verdict

Pass with minor issues. The CAS-backed `CHEBI:89197` identity, chemistry, SSSOM
row, aggregate row, and docs pass; only stale advisory rows remain.

## Identity

- Reviewed record: `data/ingredients/mapped/2-pentyl-furan.yaml`.
- Identifier and grounding: `identifier: CHEBI:89197` with
  `ontology_mapping.ontology_id: CHEBI:89197`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:89197`
  resolves to `2-pentylfuran`, lists formula `C9H14O`, and contains the same
  structure represented in the YAML.
- Formula, InChI, and SMILES are populated and exactly match the ChEBI
  structure fields.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-oxobutanoate.yaml data/ingredients/mapped/2-oxobutyric_Acid_Sodium_Salt.yaml data/ingredients/mapped/2-oxopentanoate.yaml data/ingredients/mapped/2-pentyl-furan.yaml data/ingredients/mapped/2-propanolCO2.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/2-pentyl-furan.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:2-pentyl-furan` to `CHEBI:89197` row, with `CAS:3777-69-3` represented
  in the SSSOM `other` field.

## Evidence

- The active ChEBI term confirms the current CAS-backed identity.
- The July OAK/OLS row independently confirmed the same `CHEBI:89197` mapping.
- Stale: generated batch-review rows still treat the hyphenation difference
  between source `2-pentyl-furan` and ChEBI `2-pentylfuran` as suspicious, but
  the record was already regraded to `CAS_RN_LOOKUP` to preserve the CAS
  provenance that established the mapping.
- The hidden/ignored-inclusive search over `data/custom`, `data/curated`,
  `data/ingredients`, `mappings`, and `reports` found the active YAML,
  aggregate, SSSOM, OAK/OLS review, and stale advisory rows.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- Core chemistry is complete for the active ChEBI identity.
- Empty occurrence counts are expected for this CultureBotHT CAS import.

## Recommended Edits

1. No curation edit is required for
   `data/ingredients/mapped/2-pentyl-furan.yaml`.
2. When stale advisory artifacts are next regenerated, confirm the obsolete
   hyphenation-only batch findings drop out for this record.
