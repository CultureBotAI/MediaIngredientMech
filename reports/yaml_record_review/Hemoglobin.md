# `data/ingredients/mapped/Hemoglobin.yaml`

## Verdict

Needs curation. The ChEBI ID is active and carries `Hemoglobin` as a synonym,
but the generic CultureMech ingredient surface should not exact-match the
oxygenation-specific `deoxyhemoglobin` class without source support for that
state.

## Identity

- Reviewed record: `data/ingredients/mapped/Hemoglobin.yaml`.
- Identifier and grounding: `identifier: CHEBI:5656` with
  `ontology_mapping.ontology_id: CHEBI:5656`, label `deoxyhemoglobin`, source
  `CHEBI`, `mapping_quality: SYNONYM_MATCH`, `match_level: NORMALIZED`, and
  `mapping_status: MAPPED`.
- Occurrence statistics: `total_occurrences: 1` and `media_count: 1`.
- The adjacent CultureMech residual record
  `data/ingredients/mapped/Dried_Bovine_Hemoglobin_BD_212392.yaml` separately
  preserves a BD catalog product at active `MICRO:0001599` `dried bovine
  hemoglobin`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Helenine.yaml data/ingredients/mapped/Hemin_solution_see_below.yaml data/ingredients/mapped/Hemoglobin.yaml data/ingredients/mapped/Henicosane.yaml data/ingredients/mapped/Heparin_Sodium_Salt_From_Porcine_Intestinal_Mucosa.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `linkml-term-validator` passed for `CHEBI:5656`.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1418`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1418`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:5656` as active `deoxyhemoglobin` and includes
  `Hemoglobin` as a synonym.
- Major: the source occurrence was only the generic surface `Hemoglobin`; the
  residual grounding table does not establish that the recipe meant
  deoxygenated hemoglobin rather than hemoglobin as a generic growth-medium
  material.
- The direct `culturemech:output/ingredient_occurrences.tsv` source file is
  not present in this checkout; a hidden and ignored-inclusive `find` over this
  worktree found no `ingredient_occurrences.tsv` copy.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Hemoglobin` to
  `CHEBI:5656` and does not export noisy `other` tokens.

## Completeness

- The active ChEBI target and synchronized final SSSOM row are present.
- The record is incomplete until the original CultureMech recipe is inspected
  and the term is either regrounded to a generic hemoglobin material or retained
  with evidence that the supplied ingredient specifically denotes
  deoxyhemoglobin.

## Recommended Edits

- Major: inspect the CultureMech source occurrence behind
  `culturemech:output/ingredient_occurrences.tsv`; if it only says
  `Hemoglobin`, replace the exact `CHEBI:5656` identity with a generic
  external hemoglobin material or a local registry identity.
