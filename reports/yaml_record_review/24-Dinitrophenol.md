# `data/ingredients/mapped/24-Dinitrophenol.yaml`

## Verdict

Pass with minor issues, minor. The exact `CHEBI:42017`
`2,4-dinitrophenol` identity, chemistry, SSSOM row, and aggregate row pass; only
stale advisory rows still ask for the direct ChEBI verification that now passes.

## Identity

- Reviewed record: `data/ingredients/mapped/24-Dinitrophenol.yaml`.
- Identifier and grounding: `identifier: CHEBI:42017` with
  `ontology_mapping.ontology_id: CHEBI:42017`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:42017`
  resolves to `2,4-dinitrophenol`, lists formula `C6H4N2O5`, carries CAS
  `51-28-5`, and matches the record formula, InChI, and SMILES.
- The record was seeded from CultureBotHT CAS `51-28-5` and has
  `ingredient_type: SINGLE_INGREDIENT`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/24-Dinitrophenol.yaml data/ingredients/mapped/24-diamino-67-di-iso-propylpteridine_phosphate.yaml data/ingredients/mapped/25-Dihydroxy-4-Methoxychalcone.yaml data/ingredients/mapped/3-Aminophenol.yaml data/ingredients/mapped/3-Aminopropionitrile_Fumarate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/24-Dinitrophenol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:24-Dinitrophenol` to `CHEBI:42017` row, with CAS `51-28-5` represented
  in the SSSOM `other` field.

## Evidence

- The active ChEBI page and OAK/OLS review both confirm the exact identity.
- `occurrence_statistics` reports `0/0`; the record came from a CultureBotHT
  FEBA/Hans80 panel CAS source rather than a counted CultureMech recipe
  occurrence.
- Stale: `mappings/record_research_validation.tsv` still contains old P1/P2
  rows asking for direct `CHEBI:42017` verification before exporting an exact
  row; the refreshed ChEBI page now verifies the active term and exact neutral
  molecule identity.
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
