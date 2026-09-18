# `data/ingredients/mapped/D-_-lyxose.yaml`

## Verdict

Pass with minor issues. This record is intentionally a rejected tombstone after
`D-(-)-lyxose` was merged into the live `CHEBI:62318` `D-lyxose` record. No
`MIM:D-_-lyxose` final SSSOM row remains, and the retained record owns the
folded `D-(-)-lyxose` and `D-lyxo-pentose` aliases. Stale chemistry,
provisional role data, and an unreviewed cross-record baseline row remain as
non-exported cleanup.

## Identity

- Reviewed record: `data/ingredients/mapped/D-_-lyxose.yaml`.
- Tombstone status: `mapping_status: REJECTED`.
- Current record state: `identifier: CHEBI:62318` with old
  `ontology_mapping.ontology_id: CHEBI:16789`,
  `ontology_label: aldehydo-D-lyxose`, and
  `mapping_quality: SYNONYM_MATCH`.
- Live OLS lookups confirm that `CHEBI:16789` is the active
  `aldehydo-D-lyxose` term for the open-chain aldehyde form with CAS xref
  `1114-34-7`, and that `CHEBI:62318` is active `D-lyxose`.
- A hidden/ignored-inclusive exact `^identifier:`/`ontology_id:` search under
  `data/ingredients` found this tombstone, the active
  `data/ingredients/mapped/(2)-D-lyxose.yaml` survivor, and no other primary
  `CHEBI:62318` records.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-Sucrose.yaml data/ingredients/mapped/D-_-galactosamine_Hydrochloride.yaml data/ingredients/mapped/D-_-gluconic_Acid_Gamma-lactone.yaml data/ingredients/mapped/D-_-lyxose.yaml data/ingredients/mapped/D-_-melezitose_Hydrate.yaml`:
  passed; 5 files scanned and 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-_-galactosamine_Hydrochloride.yaml data/ingredients/mapped/D-_-gluconic_Acid_Gamma-lactone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the two live CHEBI-primary exact records in this batch. This
  rejected tombstone was skipped because its intentionally stale
  aldehydo-form pointer is outside the simple active-record term check.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed before this read-only report batch; both curated collection files had
  0 data differences and only expected scratch `generation_date` metadata
  differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K before this read-only report
  batch. Rule B4 was skipped because the sibling kg-microbe ontology transforms
  were absent.

## Evidence

- The 2026-08-18 `MERGED_INTO` event says `D-(-)-lyxose` was merged into
  `CHEBI:62318` `D-lyxose` and SSSOM rows were dropped.
- The active `(2)-D-lyxose.yaml` record now publishes the
  `MIM:~282~29-D-lyxose skos:exactMatch CHEBI:62318` final SSSOM row and
  carries `D-(-)-lyxose`, `D-lyxo-pentose`, and `CAS:1114-34-7` in `other`.
- A hidden/ignored-inclusive search over `mappings`, `data`, `docs`,
  `reports`, `scripts`, and `tests` found no active
  `MIM:D-_-lyxose` final SSSOM row. It found only the historical
  row-review/enrichment rows, the `mim_curie_aliases` row, and the
  `mappings/other_cross_record_baseline.tsv` row that still marks the
  `MIM:~282~29-D-lyxose` to `MIM:D-_-lyxose` duplicate as `UNREVIEWED`.

## Completeness

- The tombstone is complete enough for rejected duplicate lookup: its
  occurrence count is 0/0, its merge event names the retained record, and it no
  longer publishes a final SSSOM row.
- Stale `chemical_properties`, `ingredient_type`, and the provisional
  `CARBON_SOURCE` facet remain on the tombstone YAML but are not exported as
  live claims.
- The aggregate record in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML for this reviewed entry.

## Recommended Edits

- Optionally refresh `mappings/other_cross_record_baseline.tsv` so the
  `MIM:~282~29-D-lyxose` to `MIM:D-_-lyxose` duplicate is no longer
  `UNREVIEWED`, and prune stale chemistry/role fields from the rejected
  tombstone if tombstones are no longer expected to retain inert pre-merge
  facts. No final SSSOM row change is required for this tombstone.
