# `data/ingredients/mapped/Trisodium_Citrate_X_2_H2o.yaml`

## Verdict

Pass with minor issues. This rejected duplicate points at the live
`CHEBI:32142` sodium citrate dihydrate target and emits no final SSSOM row,
but stale trihydrate and parent-salt labels remain in the tombstone.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Trisodium_Citrate_X_2_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:32142` with matching
  `ontology_mapping.ontology_id`, label `sodium citrate dihydrate`, source
  `CHEBI`, `mapping_quality: NARROW_MATCH`, and `mapping_status: REJECTED`.
- CAS RN: `6132-04-3`.
- Synonyms: 2-water hydrate labels, one stale 3-water hydrate label, raw
  CultureMech role text, and an anhydrous parent-salt label.
- Occurrences: 0 recipe occurrences in 0 media after merge.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tris_Base` through `Trithionate`: exited 0 and wrote zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 term lookup for `CHEBI:32142` returns `sodium citrate dihydrate`,
  CAS xref `cas:6132-04-3`, and formula `C6H5O7.2H2O.3Na`.
- A hidden/ignored-inclusive search of `mappings/ingredient_mappings.sssom.tsv`
  found no `MIM:Trisodium_Citrate_X_2_H2o` subject row, so the stale
  tombstone-only synonyms are not published in final SSSOM.

## Issues

### Minor: stale synonyms remain in a rejected tombstone

The tombstone still carries a trihydrate label and an anhydrous ChEBI parent
label. They do not reach final SSSOM, but they are cleanup candidates for a
future tombstone-normalization pass.

## Completeness

- The rejected record points at its live dihydrate merge target and emits no
  published SSSOM row.
- Stale synonym cleanup is the only residual work.

## Recommended Edits

- Optionally remove or reclassify the stale trihydrate and parent-salt
  synonyms during a tombstone cleanup pass; no immediate final SSSOM repair is
  needed.
