# `data/ingredients/mapped/3-aminobutyric_Acid.yaml`

## Verdict

Needs curation, major. The CAS-derived `CHEBI:37081`
`3-aminobutanoic acid` identity, CAS, ChEBI chemistry, SSSOM row, and aggregate
row pass, but the active `AMINO_ACID_SOURCE` role is only backed by a
provisional ChEBI-ancestry inference.

## Identity

- Reviewed record: `data/ingredients/mapped/3-aminobutyric_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:37081` with
  `ontology_mapping.ontology_id: CHEBI:37081`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:37081`
  resolves to `3-aminobutanoic acid`, lists formula `C4H9NO2`, carries CAS
  `541-48-0`, and matches the record InChI and SMILES.
- The `3-aminobutyric acid` preferred term is a synonym for this same neutral
  acid, while the neighboring `3-aminobutyrate` record denotes the deprotonated
  `CHEBI:87997` anion.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/3-aminobutyric_Acid.yaml data/ingredients/mapped/3-beta-d-glucan.yaml data/ingredients/mapped/3-dehydro-D-gluconate.yaml data/ingredients/mapped/3-fucosyllactose.yaml data/ingredients/mapped/3-hydroxybenzoate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/3-aminobutyric_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:3-aminobutyric_Acid` to `CHEBI:37081` row with `CAS:541-48-0` in
  `other`.

## Evidence

- The active ChEBI page confirms the CAS-to-ChEBI grounding and structure.
- The OAK/OLS row-review surface already records this row as `CONFIRMED`.
- Unsupported: `nutritional_roles.AMINO_ACID_SOURCE` has only `reference_type:
  COMPUTATIONAL_PREDICTION` from ChEBI is_a/has_role closure. That proves class
  membership, not culture-medium use as an amino-acid source.
- Stale/advisory: `mappings/record_research_validation.tsv` still asks for
  direct live-ChEBI inspection and optional BABA synonym enrichment. The ChEBI
  identity check now passes; the synonym enrichment can be handled separately.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `scripts`, `conf`, `src`, and `tests` found the active YAML,
  aggregate, SSSOM, OAK/OLS review, generated docs, and advisory research rows.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- CAS, formula, InChI, and SMILES are populated.
- The active nutritional role still needs direct exact-form evidence or removal.

## Recommended Edits

1. In `data/ingredients/mapped/3-aminobutyric_Acid.yaml`, remove
   `nutritional_roles.AMINO_ACID_SOURCE` or replace it with direct evidence that
   the neutral acid is used as a culture-medium amino-acid source.
2. Optionally add directly supported synonyms such as `beta-aminobutyric acid`
   and `BABA` while keeping racemate-specific labels off this neutral generic
   acid unless exact-form evidence supports them.
3. Run the per-record strict validator, compare the record against
   `data/curated/mapped_ingredients.yaml`, rebuild the SSSOM/docs with the
   maintained generators, and then rerun the whole-corpus SSSOM and flat-export
   checks.
