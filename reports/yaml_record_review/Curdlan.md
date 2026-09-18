# `data/ingredients/mapped/Curdlan.yaml`

## Verdict

Needs curation; major. The current CAS identity, MeSH parent, registry SSSOM
rows, and 0/0 CultureMech count are internally consistent, but a fresh CHEBI
search now returns a plausible `curdlan` synonym under `CHEBI:37671`, making
the old no-CHEBI provenance stale enough for curator review.

## Identity

- Reviewed record: `data/ingredients/mapped/Curdlan.yaml`.
- Identifier and grounding: `identifier: cas:54724-00-4`,
  `ontology_mapping.ontology_id: mesh:C038459`,
  `ontology_label: curdlan`, `ontology_source: MESH`,
  `mapping_quality: NARROW_MATCH`, and `mapping_status: MAPPED`.
- Live OLS lookup by `mesh:C038459` returns active MeSH `C038459` labelled
  `curdlan`.
- Live exact CHEBI search for `curdlan` now returns `CHEBI:37671`,
  `(1->3)-beta-D-glucan`, which did not exist in the original curation note and
  could be a closer CHEBI parent or replacement for the MeSH parent after
  identity review.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this active record using `cas:54724-00-4` as a
  primary identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Curcumin.yaml data/ingredients/mapped/Curdlan.yaml data/ingredients/mapped/Cuso4.yaml data/ingredients/mapped/Cuso4_X_2_H2o.yaml data/ingredients/mapped/Cuso4_X_4_H2o.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Curcumin.yaml data/ingredients/mapped/Cuso4.yaml data/ingredients/mapped/Cuso4_X_2_H2o.yaml data/ingredients/mapped/Cuso4_X_4_H2o.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four CHEBI records in this batch. `Curdlan` was intentionally
  skipped because its CAS primary identifier and MeSH parent are outside this
  CHEBI-focused exact-label validation pass.
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

- Hidden/ignored-inclusive searches over `data`, `mappings`, `docs/data`,
  `scripts`, `tests`, and `reports` found the `MIM:Curdlan` final SSSOM
  parent row, CAS registry row, and local kg-microbe registry row.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` already marks the
  MeSH `UNKNOWN_TERM` validation as prefix-dispatch coverage only, and marks
  the CAS and kg-microbe rows as expected registry identifiers.
- `mappings/culturemech_recipe_membership.tsv` has no `cas:54724-00-4` rows,
  which agrees with the CultureBotHT-only `0/0` `occurrence_statistics`.
- Major: the YAML still says no CHEBI entry exists for this compound, but live
  OLS now finds a plausible CHEBI result for `curdlan`; the MeSH parent and
  registry rows need a curation review against `CHEBI:37671`.
- The final SSSOM `other` tokens are empty on the MeSH parent row and
  `CAS:54724-00-4` on the registry rows.

## Completeness

- The CAS RN, MeSH parent row, registry identity rows, aggregate copy, and
  generated docs rows are populated and agree with the current CAS-primary
  modeling.
- The stale CHEBI-negative provenance is the only consequential gap.

## Recommended Edits

- Major: review `CHEBI:37671` against `cas:54724-00-4` in
  `data/ingredients/mapped/Curdlan.yaml`; either remap to CHEBI if it is exact
  or a better parent, or keep the MeSH parent and record why the CHEBI result
  is too broad.
- Regenerate synchronized products and rerun strict validation, SSSOM QC,
  aggregate roundtrip, and `git diff --check`.
