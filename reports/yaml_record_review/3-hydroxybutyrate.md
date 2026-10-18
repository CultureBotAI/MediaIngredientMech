# `data/ingredients/mapped/3-hydroxybutyrate.yaml`

## Verdict

Pass with minor issues. The exact non-stereospecific `CHEBI:37054`
3-hydroxybutyrate identity, beta-hydroxybutyrate alias, MicrobeDecoder source
tracking, SSSOM row, and generated exports pass; only stale advisory rows still
refer to older pre-classification review state.

## Identity

- Reviewed record: `data/ingredients/mapped/3-hydroxybutyrate.yaml`.
- Identifier and grounding: `identifier: CHEBI:37054`,
  `ontology_mapping.ontology_id: CHEBI:37054`,
  `ontology_label: 3-hydroxybutyrate`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:37054` returns the active label
  `3-hydroxybutyrate` and formula `C4H7O3`, matching the local anion formula,
  InChI, SMILES, and 2026-08-13 ChEBI/PubChem backfill.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/3-hydroxybenzoic_Acid.yaml data/ingredients/mapped/3-hydroxybutyrate.yaml data/ingredients/mapped/Calcium_lactate.yaml data/ingredients/mapped/Calcium_malate.yaml data/ingredients/mapped/Calprotectin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/3-hydroxybenzoic_Acid.yaml data/ingredients/mapped/3-hydroxybutyrate.yaml data/ingredients/mapped/Calcium_lactate.yaml data/ingredients/mapped/Calcium_malate.yaml data/ingredients/mapped/Calprotectin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 files.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.GkFQqh`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.GkFQqh`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The original `kgmicrobe.trait:3_hydroxybutyrate` import mapped directly to
  the same ChEBI label, and the 2026-08-06 merge kept
  `Beta-hydroxybutyrate` as a raw alias after confirming the beta and 3-
  positional names refer to the same compound.
- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `docs/data`, and `reports`, excluding bulky backups and generated
  review-report directories, found the active `MIM:3-hydroxybutyrate` SSSOM row
  with `Beta-hydroxybutyrate` in `other` and matching aggregate/docs rows.
- The same search found stale generated advisory rows in
  `mappings/record_research_validation.tsv`: one still says the CURIE was
  refuted, and another says `ingredient_type` is unset. The current record is
  already set to `SINGLE_INGREDIENT` and its exact achiral anion identity is
  intact.

## Completeness

- Formula, InChI, SMILES, molecular weight, single-ingredient classification,
  MicrobeDecoder source occurrence count, SSSOM row, aggregate copy, and docs
  row are populated.
- The record is intentionally a non-media MicrobeDecoder trait import, so 0/0
  media occurrences plus the separate 391-row `source_occurrences` entry are
  coherent.

## Recommended Edits

- No curated-record edits are needed.
- If `mappings/record_research_validation.tsv` is still used as a live queue,
  clear the stale `3-hydroxybutyrate` P1/P3 rows or regenerate that advisory
  table from the current record.
