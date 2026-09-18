# `data/ingredients/mapped/D-Sucrose.yaml`

## Verdict

Pass with minor issues. This record is intentionally a rejected tombstone after
`D-Sucrose` was merged into the live `Sucrose` record at `CHEBI:17992`; no
`MIM:D-Sucrose` row remains in final SSSOM, and the retained record owns the
merged `D-Sucrose` synonym. Stale chemistry, provisional nutritional roles,
and an unreviewed cross-record baseline row remain as non-exported cleanup.

## Identity

- Reviewed record: `data/ingredients/mapped/D-Sucrose.yaml`.
- Tombstone status: `mapping_status: REJECTED`.
- Current pointer: `identifier: CHEBI:17992` with
  `ontology_mapping.ontology_id: CHEBI:17992`, source `CHEBI`, and
  `mapping_quality: EXACT_MATCH`.
- Live OLS lookup by `CHEBI:17992` returns active `CHEBI:17992` labelled
  `sucrose` with formula `C12H22O11`; the stored IUPAC synonym
  `beta-D-fructofuranosyl alpha-D-glucopyranoside` is an exact
  `CHEBI:17992` synonym.
- A hidden/ignored-inclusive exact `^identifier:`/`ontology_id:` search under
  `data/ingredients` found this tombstone and the active
  `data/ingredients/mapped/Sucrose.yaml` record for `CHEBI:17992`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-Sucrose.yaml data/ingredients/mapped/D-_-galactosamine_Hydrochloride.yaml data/ingredients/mapped/D-_-gluconic_Acid_Gamma-lactone.yaml data/ingredients/mapped/D-_-lyxose.yaml data/ingredients/mapped/D-_-melezitose_Hydrate.yaml`:
  passed; 5 files scanned and 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-_-galactosamine_Hydrochloride.yaml data/ingredients/mapped/D-_-gluconic_Acid_Gamma-lactone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the two live CHEBI-primary exact records in this batch. This
  rejected tombstone was skipped because its status and old merge state, not
  simple CHEBI primary resolution, are the review surface.
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

- The 2026-08-05 `MERGED_INTO` event says `D-Sucrose` was merged into
  `CHEBI:17992` `Sucrose`, 0/0 occurrences were transferred, and SSSOM rows
  were dropped.
- The active `Sucrose.yaml` record now owns 233/233 occurrences and carries
  `D-Sucrose` as a merged raw synonym.
- A hidden/ignored-inclusive search over `mappings`, `data`, `docs`,
  `reports`, `scripts`, and `tests` found no active
  `MIM:D-Sucrose` final SSSOM row. It found only the historical
  row-review/enrichment rows and the `mappings/other_cross_record_baseline.tsv`
  row that still marks the `MIM:Sucrose` to `MIM:D-Sucrose` duplicate as
  `UNREVIEWED`.
- The final `MIM:Sucrose` SSSOM row carries `D-Sucrose` in `other`, preserving
  the alias on the retained identity.

## Completeness

- The tombstone is complete enough for rejected duplicate lookup: its
  occurrence count is 0/0, its merge event names the retained record, and it no
  longer publishes a final SSSOM row.
- Stale `chemical_properties`, `ingredient_type`, and provisional
  `CARBON_SOURCE`/`ENERGY_SOURCE` facets remain on the tombstone YAML but are
  not exported as live claims.
- The aggregate record in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML for this reviewed entry.

## Recommended Edits

- Optionally refresh `mappings/other_cross_record_baseline.tsv` so the
  `MIM:Sucrose` to `MIM:D-Sucrose` duplicate is no longer `UNREVIEWED`, and
  prune stale chemistry/role fields from the rejected tombstone if tombstones
  are no longer expected to retain inert pre-merge facts. No final SSSOM row
  change is required.
