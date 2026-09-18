# `data/ingredients/mapped/2-methyl-1-butanol.yaml`

## Verdict

Pass with minor issues. The CAS-backed `CHEBI:48945` identity, chemistry, SSSOM
row, aggregate row, and docs pass; only stale advisory rows remain.

## Identity

- Reviewed record: `data/ingredients/mapped/2-methyl-1-butanol.yaml`.
- Identifier and grounding: `identifier: CHEBI:48945` with
  `ontology_mapping.ontology_id: CHEBI:48945`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:48945`
  resolves to `2-methylbutan-1-ol`, lists formula `C5H12O`, lists CAS RN
  `137-32-6`, and lists `2-methyl-1-butanol` as a synonym.
- Formula, InChI, and SMILES are populated and exactly match the ChEBI
  structure fields.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-methyl-1-butanol.yaml data/ingredients/mapped/2-methyl-4-isothizaolin-3-one.yaml data/ingredients/mapped/2-n-Heptyl-4-hydroxyquinoline_N-oxide.yaml data/ingredients/mapped/2-naphthyl_Dihydrogen_Phosphate.yaml data/ingredients/mapped/2-naphthyl_Tetradecanoate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/2-methyl-1-butanol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:2-methyl-1-butanol` to `CHEBI:48945` row, with `CAS:137-32-6`
  represented in the SSSOM `other` field.

## Evidence

- The active ChEBI term confirms the current CAS-backed identity and the source
  label as an exact synonym of `2-methylbutan-1-ol`.
- The July OAK/OLS row independently confirmed the same `CHEBI:48945` mapping.
- Stale: `mappings/record_research_validation.tsv` still contains an old P1 row
  that asked for direct ChEBI validation before exporting an exact SSSOM row;
  the current CAS-backed curation and live ChEBI page provide that validation.
- The hidden/ignored-inclusive search over `data/custom`, `data/curated`,
  `data/ingredients`, `mappings`, and `reports` found the active YAML,
  aggregate, SSSOM, OAK/OLS review row, and stale advisory rows.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- The core chemistry needed for the active neutral alcohol is populated.
- Empty occurrence counts are expected for this CultureBotHT CAS import.

## Recommended Edits

1. No curation edit is required for
   `data/ingredients/mapped/2-methyl-1-butanol.yaml`.
2. When stale advisory TSVs are next regenerated, confirm the obsolete
   `record_research_validation.tsv` row drops out for this record.
