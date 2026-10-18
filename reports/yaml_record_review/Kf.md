# `data/ingredients/mapped/Kf.yaml`

## Verdict

Pass with minor issues. The false-friend `KF` record is a rejected tombstone for
the potassium fluoride merge, no final SSSOM row publishes from it, and its
identifier now points at the active potassium fluoride target, but stale
Lys-Phe synonyms from the pre-rejection state remain on the tombstone.

## Identity

- Reviewed record: `data/ingredients/mapped/Kf.yaml`.
- Tombstone state: `identifier: CHEBI:66872`, `mapping_status: REJECTED`,
  `kg_microbe_node_id: CHEBI:66872`, and no final SSSOM row.
- Merge target: `data/ingredients/mapped/Potassium_Fluoride.yaml`, which holds
  the active `CHEBI:66872` potassium fluoride identity.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Kcl.yaml data/ingredients/mapped/Keratin.yaml data/ingredients/mapped/Ketomycin.yaml data/ingredients/mapped/Kf.yaml data/ingredients/mapped/Kh2po4.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 records.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_2245`:
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_2245`:
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- EBI OLS4 resolves `CHEBI:66872` as active ChEBI term `potassium fluoride`.
- The #346 and #360 curation history records document the false-friend repair:
  the old `KF` mapping to `CHEBI:73605` `Lys-Phe` was rejected and merged into
  the active potassium fluoride record.
- `mappings/ingredient_mappings.sssom.tsv` has no `MIM:Kf` row, so the
  rejected tombstone no longer contributes published SSSOM synonyms or
  predicates.
- Minor: the tombstone still carries active `EXACT_SYNONYM` strings for the old
  dipeptide interpretation: `L-Lys-L-Phe`, `L-lysyl-L-phenylalanine`,
  `Lys-Phe`, and `Lysylphenylalanine`. These no longer publish because the
  record is rejected, but they are stale leftovers from the superseded identity.
- The hidden and ignored-inclusive search over `data/ingredients`, `mappings`,
  `reports/kg_microbe_node_id_mismatches.tsv`, `reports/hydrate_grounding.tsv`,
  `docs/data`, `src`, `tests`, `conf`, and `.claude` found the current
  tombstone, active potassium fluoride target, docs projections, and the stale
  pre-rejection row-review disposition; it found no hits in
  `reports/kg_microbe_node_id_mismatches.tsv`,
  `reports/hydrate_grounding.tsv`, or `mappings/needs_curator_review.tsv`.

## Completeness

- The tombstone status, active merge target, corrected target identifier,
  corrected `kg_microbe_node_id`, and absence of a final SSSOM row are
  consistent.
- Cleanup is limited to stale, non-publishing tombstone fields.

## Recommended Edits

- Minor: remove or demote the stale Lys-Phe synonyms from
  `data/ingredients/mapped/Kf.yaml` if tombstones are expected to carry only
  current-target provenance, then rerun strict, term, round-trip, component, and
  SSSOM validation.
