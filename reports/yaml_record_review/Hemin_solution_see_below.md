# `data/ingredients/mapped/Hemin_solution_see_below.yaml`

## Verdict

Needs curation. `MICRO:0001598` is an active `hemin solution` term, but the
record preserved `(see below)` recipe prose as part of the preferred identity
without checking the downstream formulation.

## Identity

- Reviewed record: `data/ingredients/mapped/Hemin_solution_see_below.yaml`.
- Identifier and grounding: `identifier: MICRO:0001598` with
  `ontology_mapping.ontology_id: MICRO:0001598`, label `hemin solution`, source
  `MICRO`, `mapping_quality: SYNONYM_MATCH`, `match_level: NORMALIZED`, and
  `mapping_status: MAPPED`.
- Occurrence statistics: `total_occurrences: 1` and `media_count: 1`.
- Supplied form and components: absent, so the record does not capture any
  hemin concentration, solvent, NaOH amount, filter sterilization, or other
  recipe-level "see below" details.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Helenine.yaml data/ingredients/mapped/Hemin_solution_see_below.yaml data/ingredients/mapped/Hemoglobin.yaml data/ingredients/mapped/Henicosane.yaml data/ingredients/mapped/Heparin_Sodium_Salt_From_Porcine_Intestinal_Mucosa.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation was skipped for this record because
  `MICRO` is intentionally omitted from the justfile's OBO-prefix adapter list
  and covered by the product/id-label validators.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1418`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1418`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `MICRO:0001598` as active `hemin solution`.
- The maintained residual row shows the raw CultureMech surface
  `Hemin solution (see below)` was normalized to `hemin solution` before the
  new `MICRO:0001598` record was minted.
- Major: `(see below)` is not a synonym of a stock hemin solution; it points to
  recipe-local preparation text that must be inspected before an exact
  formulation claim is published.
- The direct `culturemech:output/ingredient_occurrences.tsv` source file is
  not present in this checkout; a hidden and ignored-inclusive `find` over this
  worktree found no `ingredient_occurrences.tsv` copy.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Hemin_solution_see_below` to `MICRO:0001598` and does not export noisy
  `other` tokens.

## Completeness

- The active MICRO target and final SSSOM row are present.
- The record is incomplete until the original CultureMech recipe is inspected:
  either the preferred term should drop `(see below)` if the ingredient is
  truly the generic MICRO hemin solution, or the recipe-specific solution
  should be modeled as a local formulation with supported components.

## Recommended Edits

- Major: inspect the CultureMech source occurrence behind
  `culturemech:output/ingredient_occurrences.tsv`, record the actual "see
  below" formulation, and either remap this record to plain `hemin solution` or
  mint a local formulation with hemin and solvent/base components.
