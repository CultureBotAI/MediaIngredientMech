# `data/ingredients/mapped/3-O-methyl-glucose.yaml`

## Verdict

Needs curation, major. The CAS-derived `CHEBI:73918`
`3-O-methyl-D-glucose` identity, chemistry, absorbed raw label, SSSOM row, and
aggregate row pass, but the active `CARBON_SOURCE` role is only provisional and
contradicts the repository's own exclusion of `3-O-methyl-glucose` as a
nonmetabolizable transport tracer.

## Identity

- Reviewed record: `data/ingredients/mapped/3-O-methyl-glucose.yaml`.
- Identifier and grounding: `identifier: CHEBI:73918` with
  `ontology_mapping.ontology_id: CHEBI:73918`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:73918`
  resolves to `3-O-methyl-D-glucose`, lists formula `C7H14O6`, carries CAS
  `146-72-5`, and matches the record InChI and SMILES.
- The absorbed `3-methylglucose` microbedecoder label is intentionally retained
  as `RAW_TEXT` by the `issue_213_grounding` event.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/3-Methylglutaric_Acid.yaml data/ingredients/mapped/3-O-Methyl-D-glucopyranose.yaml data/ingredients/mapped/3-O-methyl-glucose.yaml data/ingredients/mapped/3-O-methyl_Alpha-D-glucopyranoside.yaml data/ingredients/mapped/3-O-methylgallate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/3-O-methyl-glucose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:3-O-methyl-glucose` to `CHEBI:73918` row with
  `3-methylglucose|CAS:146-72-5` in `other`.

## Evidence

- The ChEBI page confirms the CAS-to-ChEBI grounding and structure.
- The OAK/OLS row-review candidate for `3-O-methyl-glucose` is already
  represented by the record's preferred term.
- Unsupported: `nutritional_roles.CARBON_SOURCE` has only `reference_type:
  COMPUTATIONAL_PREDICTION` from a curated media-role name pattern. The
  repository's focused role-inference tests explicitly exclude
  `3-O-methyl-glucose` as a nonmetabolizable transport tracer, and
  `mappings/record_research_validation.tsv` has a P2 row recommending removal
  of the generic carbon-source annotation.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `scripts`, `conf`, `src`, and `tests` found the active YAML,
  aggregate, SSSOM, synonym-enrichment review, generated docs, role-inference
  test, and stale advisory rows.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- Core ChEBI chemistry is complete.
- The active nutritional role still needs direct exact-form evidence or removal.

## Recommended Edits

1. In `data/ingredients/mapped/3-O-methyl-glucose.yaml`, remove
   `nutritional_roles.CARBON_SOURCE` or replace it with direct medium-use
   evidence scoped to organisms and conditions where this compound is actually
   a usable carbon source.
2. Run the per-record strict validator, compare the record against
   `data/curated/mapped_ingredients.yaml`, rebuild the SSSOM/docs with the
   maintained generators, and then rerun the whole-corpus SSSOM and flat-export
   checks.
