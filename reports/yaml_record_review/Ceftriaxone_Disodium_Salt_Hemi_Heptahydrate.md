# `data/ingredients/mapped/Ceftriaxone_Disodium_Salt_Hemi_Heptahydrate.yaml`

## Verdict

Needs curation; major issue. The CAS-derived ceftriaxone disodium
hemiheptahydrate identity is correctly grounded to active `CHEBI:3514`, and
its formula, InChI, SMILES, SSSOM row, aggregate copy, and zero occurrence
count agree; the remaining `SELECTIVE_AGENT` role is supported only by a
provisional name-pattern prediction.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Ceftriaxone_Disodium_Salt_Hemi_Heptahydrate.yaml`.
- Identifier and grounding: `identifier: CHEBI:3514`,
  `ontology_mapping.ontology_id: CHEBI:3514`,
  `ontology_label: Ceftriaxone disodium salt hemiheptahydrate`,
  `ontology_source: CHEBI`, `mapping_quality: CAS_RN_LOOKUP`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:3514` returns one active ChEBI term labelled
  `Ceftriaxone disodium salt hemiheptahydrate` with formula
  `2C18H16N8O7S3.7H2O.4Na` and the same InChI and SMILES stored in
  `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cefsulodin_Sodium_Salt_Hydrate.yaml data/ingredients/mapped/Ceftazidime.yaml data/ingredients/mapped/Ceftazidime_Hydrate.yaml data/ingredients/mapped/Ceftriaxone.yaml data/ingredients/mapped/Ceftriaxone_Disodium_Salt_Hemi_Heptahydrate.yaml`:
  passed.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cefsulodin_Sodium_Salt_Hydrate.yaml data/ingredients/mapped/Ceftazidime.yaml data/ingredients/mapped/Ceftazidime_Hydrate.yaml data/ingredients/mapped/Ceftriaxone.yaml data/ingredients/mapped/Ceftriaxone_Disodium_Salt_Hemi_Heptahydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 external-ontology records in this batch.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `docs/data`, and `reports`, excluding generated review reports and curated
  backups, found the active exact
  `MIM:Ceftriaxone_Disodium_Salt_Hemi_Heptahydrate` SSSOM row, the
  `SYNONYM_ENRICH` row-review disposition, the synonym-enrichment
  `ALREADY_REPRESENTED` row, `mappings/hydrate_review.tsv`, and matching
  aggregate/docs rows for `CHEBI:3514`.
- `mappings/hydrate_review.tsv` marks this row `OK` with high confidence
  because the named hemiheptahydrate is an established 3.5-water form and the
  hydrate-specific ChEBI identity/formula agrees.
- Hidden/ignored-inclusive anchored search of
  `mappings/culturemech_recipe_membership.tsv` found no `CHEBI:3514` rows,
  which matches the explicit 0/0 `occurrence_statistics`.
- `SELECTIVE_AGENT` has only `COMPUTATIONAL_PREDICTION` evidence from
  `infer_roles_from_name_lists` and is explicitly marked "Provisional role from
  a curated name-pattern rule; review recommended."

## Completeness

- The CAS-derived exact ChEBI identifier, formula, InChI, SMILES, SSSOM row,
  aggregate copy, docs row, and zero occurrence count are populated and agree.
- The record has no component, environment, or mechanistic assertions that need
  additional evidence.

## Recommended Edits

- Major: either replace `physicochemical_roles.SELECTIVE_AGENT` with inspected
  evidence for ceftriaxone disodium hemiheptahydrate as a selective agent in
  this media scope, or remove the role, then rerun strict validation, SSSOM QC,
  aggregate roundtrip, and `git diff --check`.
