# `data/ingredients/mapped/2-undecanol.yaml`

## Verdict

Pass with minor issues. The CAS-backed `CHEBI:77930` identity, chemistry, SSSOM
row, aggregate row, and docs pass; only stale advisory rows remain.

## Identity

- Reviewed record: `data/ingredients/mapped/2-undecanol.yaml`.
- Identifier and grounding: `identifier: CHEBI:77930` with
  `ontology_mapping.ontology_id: CHEBI:77930`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:77930`
  resolves to `undecan-2-ol`, lists formula `C11H24O`, and contains the same
  structure represented in the YAML.
- Formula, InChI, and SMILES are populated and exactly match the ChEBI
  structure fields.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-undecanol.yaml data/ingredients/mapped/20AA_mix.yaml data/ingredients/mapped/22-Dipyridyl.yaml data/ingredients/mapped/22-dibromo-2-cyanoacetamide.yaml data/ingredients/mapped/2244688-heptamethylnonane.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/2-undecanol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:2-undecanol` to `CHEBI:77930` row, with `CAS:1653-30-1` represented in
  the SSSOM `other` field.

## Evidence

- The active ChEBI term confirms the current CAS-backed identity.
- The July OAK/OLS row independently confirmed the same `CHEBI:77930` mapping.
- Stale: `mappings/record_research_validation.tsv` still contains an old P1 row
  asking to inspect `CHEBI:77930` directly before exporting the exact SSSOM row;
  direct ChEBI verification now passes.
- Stale/minor: the same TSV suggests adding `undecan-2-ol` as a synonym, but
  that is already the stored `ontology_label`.
- The hidden/ignored-inclusive search over `data/custom`, `data/curated`,
  `data/ingredients`, `mappings`, and `reports` found the active YAML,
  aggregate, SSSOM, OAK/OLS review, row-review manifest, and stale advisory
  rows.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- Core chemistry is complete for the active ChEBI identity.
- Empty occurrence counts are expected for this CultureBotHT CAS import.

## Recommended Edits

1. No curation edit is required for
   `data/ingredients/mapped/2-undecanol.yaml`.
2. When stale advisory TSVs are next regenerated, confirm the obsolete
   `record_research_validation.tsv` row drops out for this record.
