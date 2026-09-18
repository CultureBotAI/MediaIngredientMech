# `data/ingredients/mapped/3-Methyl-2-oxobutanoic_Acid_Sodium_Salt.yaml`

## Verdict

Pass with minor issues, minor. The CAS-derived `CHEBI:189431`
`Sodium-3-methyl-2-oxobutyrate` identity, chemistry, SSSOM row, and aggregate
row pass; only stale advisory rows still ask for the direct ChEBI verification
that now passes.

## Identity

- Reviewed record:
  `data/ingredients/mapped/3-Methyl-2-oxobutanoic_Acid_Sodium_Salt.yaml`.
- Identifier and grounding: `identifier: CHEBI:189431` with
  `ontology_mapping.ontology_id: CHEBI:189431`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:189431`
  resolves to `Sodium-3-methyl-2-oxobutyrate`, lists formula `C5H7O3.Na`,
  carries CAS `3715-29-5`, and matches the record formula, InChI, and SMILES.
- The `sodium;3-methyl-2-oxobutanoate` synonym is already represented.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/3-Hydroxypropanal.yaml data/ingredients/mapped/3-Hydroxypropionate.yaml data/ingredients/mapped/3-Methyl-2-Oxobutanoic_Acid.yaml data/ingredients/mapped/3-Methyl-2-oxobutanoic_Acid_Sodium_Salt.yaml data/ingredients/mapped/3-Methylcatechol.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/3-Methyl-2-oxobutanoic_Acid_Sodium_Salt.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:3-Methyl-2-oxobutanoic_Acid_Sodium_Salt` to `CHEBI:189431` row, with the
  represented synonym and CAS `3715-29-5` in the SSSOM `other` field.

## Evidence

- The active ChEBI page and OAK/OLS synonym-enrichment review both confirm the
  exact 1:1 sodium-salt identity.
- `mappings/ingredient_mappings_synonym_enrich_review.tsv` already resolved the
  proposed synonym enrichment as `ALREADY_REPRESENTED`.
- `occurrence_statistics` reports `0/0`; the record came from CultureBotHT CAS
  input rather than a counted CultureMech recipe occurrence.
- Stale: `mappings/record_research_validation.tsv` still contains old P1/P2
  rows asking for direct `CHEBI:189431` verification before publishing an exact
  SSSOM row; the direct ChEBI check now verifies the active salt term.
- The hidden/ignored-inclusive search over `data/custom`, `data/curated`,
  `data/ingredients`, `mappings`, and `reports` found the active YAML,
  aggregate, SSSOM, synonym-enrichment review, OAK/OLS review, and advisory
  rows.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- Core chemistry is complete for the active ChEBI identity.
- No record-local curation defect remains.

## Recommended Edits

No YAML edit is required for this record. The stale advisory rows can be
ignored or refreshed when `mappings/record_research_validation.tsv` is rebuilt.
