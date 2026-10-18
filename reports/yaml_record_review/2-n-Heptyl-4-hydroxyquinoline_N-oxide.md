# `data/ingredients/mapped/2-n-Heptyl-4-hydroxyquinoline_N-oxide.yaml`

## Verdict

Pass with minor issues. The CAS-backed `CHEBI:28362` HQNO identity, synonym,
chemistry, SSSOM row, aggregate row, and docs pass; only stale advisory rows and
optional molecular-weight enrichment remain.

## Identity

- Reviewed record:
  `data/ingredients/mapped/2-n-Heptyl-4-hydroxyquinoline_N-oxide.yaml`.
- Identifier and grounding: `identifier: CHEBI:28362` with
  `ontology_mapping.ontology_id: CHEBI:28362`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:28362`
  resolves to `2-heptyl-4-hydroxyquinoline N-oxide`, lists CAS RN `341-88-8`,
  lists formula `C16H21NO2`, and lists `2-heptylquinolin-4-ol 1-oxide` as the
  IUPAC name.
- Formula, InChI, and SMILES are populated and exactly match the ChEBI
  structure fields.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-methyl-1-butanol.yaml data/ingredients/mapped/2-methyl-4-isothizaolin-3-one.yaml data/ingredients/mapped/2-n-Heptyl-4-hydroxyquinoline_N-oxide.yaml data/ingredients/mapped/2-naphthyl_Dihydrogen_Phosphate.yaml data/ingredients/mapped/2-naphthyl_Tetradecanoate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/2-n-Heptyl-4-hydroxyquinoline_N-oxide.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:2-n-Heptyl-4-hydroxyquinoline_N-oxide` to `CHEBI:28362` row, with the
  IUPAC synonym and `CAS:341-88-8` represented in the SSSOM `other` field.

## Evidence

- The active ChEBI term confirms the current CAS-backed identity, including the
  unsolvated and counterion-free HQNO structure that older research rows wanted
  checked.
- The July OAK/OLS row suggested synonym enrichment for the local source label;
  the active preferred term already represents it.
- Stale: `mappings/record_research_validation.tsv` still contains old P1/P2
  rows questioning `CHEBI:28362` and calling molecular weight absent. The
  current ChEBI page resolves the exact term, and the formula, InChI, and SMILES
  are now populated.
- The hidden/ignored-inclusive search over `data/custom`, `data/curated`,
  `data/ingredients`, `mappings`, and `reports` found the active YAML,
  aggregate, SSSOM, OAK/OLS review, synonym-review, and stale advisory rows.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- Core formula, InChI, and SMILES fields are complete.
- The only missing ChEBI-backed numeric chemistry is `molecular_weight`;
  populating it would be harmless but is optional for the current CAS import.

## Recommended Edits

1. No required curation edit was found for
   `data/ingredients/mapped/2-n-Heptyl-4-hydroxyquinoline_N-oxide.yaml`.
2. Optionally backfill `molecular_weight` from ChEBI in the next mechanical
   chemistry-enrichment pass.
3. When stale advisory TSVs are next regenerated, confirm the obsolete
   `record_research_validation.tsv` rows drop out for this record.
