# `data/ingredients/mapped/3-Methyl-2-Oxobutanoic_Acid.yaml`

## Verdict

Pass with minor issues, minor. The exact `CHEBI:16530`
`3-methyl-2-oxobutanoic acid` identity, chemistry, SSSOM row, and aggregate row
pass; only stale advisory rows still ask for the direct ChEBI verification that
now passes.

## Identity

- Reviewed record:
  `data/ingredients/mapped/3-Methyl-2-Oxobutanoic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:16530` with
  `ontology_mapping.ontology_id: CHEBI:16530`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:16530`
  resolves to `3-methyl-2-oxobutanoic acid`, lists formula `C5H8O3`, carries
  CAS `759-05-7`, and matches the record formula, InChI, and SMILES.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/3-Hydroxypropanal.yaml data/ingredients/mapped/3-Hydroxypropionate.yaml data/ingredients/mapped/3-Methyl-2-Oxobutanoic_Acid.yaml data/ingredients/mapped/3-Methyl-2-oxobutanoic_Acid_Sodium_Salt.yaml data/ingredients/mapped/3-Methylcatechol.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/3-Methyl-2-Oxobutanoic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:3-Methyl-2-Oxobutanoic_Acid` to `CHEBI:16530` row, with CAS `759-05-7`
  represented in the SSSOM `other` field.

## Evidence

- The active ChEBI page and OAK/OLS review both confirm the exact neutral-acid
  identity.
- `occurrence_statistics` reports `0/0`; the record came from CultureBotHT CAS
  input rather than a counted CultureMech recipe occurrence.
- Stale: `mappings/record_research_validation.tsv` still contains a P1 row
  asking for direct `CHEBI:16530` verification; the direct ChEBI check now
  verifies the active neutral-acid term.
- The hidden/ignored-inclusive search over `data/custom`, `data/curated`,
  `data/ingredients`, `mappings`, and `reports` found the active YAML,
  aggregate, SSSOM, OAK/OLS review, and advisory rows.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- Core chemistry is complete for the active ChEBI identity.
- No record-local curation defect remains.

## Recommended Edits

No YAML edit is required for this record. The stale advisory rows can be
ignored or refreshed when `mappings/record_research_validation.tsv` is rebuilt.
