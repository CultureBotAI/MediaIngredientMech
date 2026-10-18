# `data/ingredients/mapped/K2so4_X_7_H2o.yaml`

## Verdict

Needs curation. The #344 local malformed-hydrate identity, close anhydrous
parent mapping, exact registry row, CAS removal, empty chemistry block,
occurrence count, and final SSSOM rows pass, but the carried nutritional roles
are still unsupported.

## Identity

- Reviewed record: `data/ingredients/mapped/K2so4_X_7_H2o.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.compound:k2so4_x_7_h2o` with
  `ontology_mapping.ontology_id: CHEBI:32036`, label `potassium sulfate`,
  source `CHEBI`, `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: intentionally empty after #344 cleared the unverified
  CAS RN and anhydrous structure strings from this unresolved `K2SO4 x 7 H2O`
  MediaDive source identity.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/K2so4_X_7_H2o.yaml data/ingredients/mapped/KH2PO3.yaml data/ingredients/mapped/Kanamycin.yaml data/ingredients/mapped/Kanamycin_Sulfate.yaml data/ingredients/mapped/Kanchanomycin.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 records.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_2150`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_2150`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- Fresh exact OLS4 ChEBI search for `K2SO4 x 7 H2O` returned zero hits, matching
  the #344 local identity decision. `CHEBI:32036` remains only the anhydrous
  potassium sulfate parent.
- The final SSSOM publishes the intended pair of rows: a `skos:closeMatch` from
  `MIM:K2so4_X_7_H2o` to anhydrous `CHEBI:32036` and a `skos:exactMatch` to
  `kgmicrobe.compound:k2so4_x_7_h2o`, with only hydrate-form labels in `other`.
- `mappings/hydrate_review.tsv`, `reports/hydrate_grounding.tsv`, and
  `tests/test_malformed_hydrate_identities.py` all retain this record as a
  local unresolved source identity rather than collapsing it into anhydrous
  potassium sulfate.
- Major: `nutritional_roles.SULFUR_SOURCE` has only
  `COMPUTATIONAL_PREDICTION` evidence from a curated name-pattern rule, and
  `nutritional_roles.MINERAL_SOURCE` has an empty `evidence` list.
- The hidden and ignored-inclusive search over `data/ingredients`, `mappings`,
  `reports/kg_microbe_node_id_mismatches.tsv`, `reports/hydrate_grounding.tsv`,
  `docs/data`, `src`, `tests`, `conf`, and `.claude` found the current
  per-record YAML, final SSSOM rows, docs projections, hydrate review rows, and
  the expected four CultureMech membership rows.

## Completeness

- The local identity, anhydrous close parent, exact registry row, missing CAS
  and chemical structure fields, occurrence count, and final SSSOM rows are
  present and consistent.
- The record is incomplete until both active nutritional roles carry inspected,
  role-specific evidence or are removed.

## Recommended Edits

- Major: remove `nutritional_roles.SULFUR_SOURCE` and
  `nutritional_roles.MINERAL_SOURCE` unless inspected database or literature
  evidence supports those roles for this local unresolved hydrate label, then
  rerun strict, term, round-trip, component, and SSSOM validation.
