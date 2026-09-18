# `data/ingredients/mapped/Isopropionate.yaml`

## Verdict

Pass with minor issues. `Isopropionate` is represented as a local fallback
registry term after `#213` found no public ontology class that denotes the
source label, and the final SSSOM row points at that fallback CURIE; only the
old top-level import note remains stale.

## Identity

- Reviewed record: `data/ingredients/mapped/Isopropionate.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.compound:isopropionate`
  with `ontology_mapping.ontology_id: kgmicrobe.compound:isopropionate`, label
  `Isopropionate`, source `kgmicrobe.compound`,
  `mapping_quality: FALLBACK_REGISTRY`, and `mapping_status: MAPPED`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Isomaltose.yaml data/ingredients/mapped/Isoniazid.yaml data/ingredients/mapped/Isoorientin.yaml data/ingredients/mapped/Isophthalate.yaml data/ingredients/mapped/Isopropionate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for the 4 CHEBI records.
  `Isopropionate` was outside adapter scope because its primary identifier is a
  local `kgmicrobe.compound` CURIE.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_2100`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_2100`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- The `#213` curator evidence records a search across the ontologies available
  to the repo and a live exact OLS4 query that found no term denoting
  isopropionate.
- A fresh exact live OLS4 search for `Isopropionate` returned zero hits,
  supporting continued use of the local fallback registry term.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Isopropionate` to `kgmicrobe.compound:isopropionate` with empty
  `other`.
- Minor: top-level `notes` still describe the original MicrobeDecoder miss and
  say curator review is needed even though the `#213` review promoted the
  fallback CURIE.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, the `UNMAPPED_0761`
  promotion, and prior research-validation rows agreeing that the
  kg-microbe-primary fallback encodes "no ontology term denotes this".

## Completeness

- The local fallback identifier, aggregate copy, and final SSSOM row are
  present and consistent.
- The record intentionally has no public ontology parent or ChEBI structure
  fields.

## Recommended Edits

- Minor: refresh top-level `notes` to stop saying that curator review is still
  needed, then rerun strict, round-trip, component, id-label, and SSSOM
  validation.
