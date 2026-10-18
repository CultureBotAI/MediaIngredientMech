# `data/ingredients/mapped/Ceftazidime_Hydrate.yaml`

## Verdict

Needs curation; major issue. The CAS-primary local identity and Section 3
SSSOM rows are internally consistent, but the original source or supplier is
still needed to verify the intended water stoichiometry for the label
`Ceftazidime hydrate`; the only remaining role claim is also a provisional
`SELECTIVE_AGENT` name-pattern prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Ceftazidime_Hydrate.yaml`.
- Identifier and grounding: `identifier: cas:120618-65-7`,
  `ontology_mapping.ontology_id: CHEBI:3508`,
  `ontology_label: ceftazidime`, `ontology_source: CHEBI`,
  `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:3508` returns one active ChEBI term labelled
  `ceftazidime` with formula `C22H22N6O7S2`; exact OLS search did not find an
  active ChEBI term for the source label `Ceftazidime hydrate`.

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
  backups, found both active `MIM:Ceftazidime_Hydrate` SSSOM rows, the
  `UNKNOWN_TERM` row-review disposition, the unknown-term triage row accepting
  the CAS registry identity, the `mappings/cas_hydrate_anchor_plan.tsv` row,
  `mappings/hydrate_review.tsv`, and matching aggregate/docs rows for
  `cas:120618-65-7`.
- The active SSSOM surface publishes a `skos:closeMatch` to the anhydrous
  ceftazidime parent `CHEBI:3508` and a `skos:exactMatch` registry row to
  `cas:120618-65-7`. `reports/hydrate_grounding.tsv` still reports
  `CAS_MISSING_ANCHOR_ROWS`, but that report is stale: the current SSSOM file
  contains the exact CAS registry row.
- `mappings/cas_hydrate_anchor_plan.tsv` anchors the record to `CHEBI:3508`
  because `CHEBI:3509` is specifically the pentahydrate, while the local label
  says only `Ceftazidime hydrate`.
- `mappings/hydrate_review.tsv` marks this record `NEEDS_SOURCE`, with the
  rationale that the label says only "hydrate" and the CAS/formula metadata
  does not securely establish a unique water stoichiometry without the original
  recipe or supplier.
- Hidden/ignored-inclusive anchored search of
  `mappings/culturemech_recipe_membership.tsv` found no `cas:120618-65-7`
  rows, which matches the explicit 0/0 `occurrence_statistics`.
- `SELECTIVE_AGENT` has only `COMPUTATIONAL_PREDICTION` evidence from
  `infer_roles_from_name_lists` and is explicitly marked "Provisional role from
  a curated name-pattern rule; review recommended."

## Completeness

- The CAS primary identifier, anhydrous-parent closeMatch, CAS registry
  identity row, zero occurrence count, SSSOM rows, aggregate copy, and docs row
  are populated.
- The record intentionally omits exact formula, InChI, and SMILES fields while
  the source water stoichiometry remains unresolved.

## Recommended Edits

- Major: inspect the original CultureBotHT source or supplier record for the
  intended ceftazidime hydrate and either keep the CAS identity as explicitly
  verified, or retarget to a more specific hydrate if the source names one.
- Major: either replace `physicochemical_roles.SELECTIVE_AGENT` with inspected
  evidence for ceftazidime hydrate as a selective agent in this media scope, or
  remove the role, then rerun strict validation, SSSOM QC, aggregate roundtrip,
  hydrate audits, and `git diff --check`.
