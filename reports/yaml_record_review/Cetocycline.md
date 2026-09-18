# `data/ingredients/mapped/Cetocycline.yaml`

## Verdict

Needs curation; major issue. `Cetocycline` is exactly grounded to the active
`NCIT:C98044` term, and its zero occurrence count, SSSOM row, and aggregate copy
agree. The only material gap is that `SELECTIVE_AGENT` is supported solely by a
provisional name-pattern prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Cetocycline.yaml`.
- Identifier and grounding: `identifier: NCIT:C98044`,
  `ontology_mapping.ontology_id: NCIT:C98044`,
  `ontology_label: Cetocycline`, `ontology_source: NCIT`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `NCIT:C98044` returns one active NCI Thesaurus term
  labelled `Cetocycline` with formula `C22H21NO7`, CAS `29144-42-1`, and exact
  synonyms including `Cetocycline`, `Beta-Chelocardin`, and `Chelocardin`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cetocycline.yaml data/ingredients/mapped/Cetomacrogol_1000.yaml data/ingredients/mapped/Cetrimonium_Bromide.yaml data/ingredients/mapped/Chalcopyrite.yaml data/ingredients/mapped/Champamycin_B.yaml`:
  passed.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cetocycline.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed. The same focused validator also passed for `Cetomacrogol_1000`,
  `Cetrimonium_Bromide`, and `Chalcopyrite`; `Champamycin_B` was skipped
  because its `kgmicrobe.compound` placeholder CURIE is a local registry ID
  outside Engine A's OBO prefix scope.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `reports` found the active exact `MIM:Cetocycline` SSSOM row, the aggregate
  and docs rows for `NCIT:C98044`, and the row-review disposition that keeps
  the mapping because a prefix-specific EBI OLS query resolves the exact NCIT
  CURIE.
- Hidden/ignored-inclusive anchored search of
  `mappings/culturemech_recipe_membership.tsv` found no `NCIT:C98044` rows,
  matching the explicit 0/0 `occurrence_statistics`.
- `SELECTIVE_AGENT` has only `COMPUTATIONAL_PREDICTION` evidence from
  `infer_roles_from_name_lists` and is explicitly marked "Provisional role from
  a curated name-pattern rule; review recommended."

## Completeness

- The exact NCIT identifier, SSSOM row, aggregate copy, docs row, and zero
  occurrence count are populated and agree.
- The record has no synonym, component, chemical property, or environment
  claims that need additional evidence.
- The only consequential gap is the unsupported provisional role.

## Recommended Edits

- Major: in `data/ingredients/mapped/Cetocycline.yaml`, either replace
  `physicochemical_roles.SELECTIVE_AGENT` with inspected evidence for
  cetocycline as a selective agent in this media scope, or remove the role.
- Regenerate synchronized outputs and rerun strict validation, Engine A term
  validation, SSSOM QC, aggregate roundtrip, and `git diff --check`.
