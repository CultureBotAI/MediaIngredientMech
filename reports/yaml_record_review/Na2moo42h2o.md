# `data/ingredients/mapped/Na2moo42h2o.yaml`

## Verdict

Pass with minor issues. This duplicate sodium molybdate dihydrate record is
correctly tombstoned as `REJECTED` after merging into
`data/ingredients/mapped/Na2moo4_X_2_H2o.yaml`, and an ignored-inclusive exact
subject search found no `MIM:Na2moo42h2o` row in final SSSOM.

## Identity

- Reviewed record: `data/ingredients/mapped/Na2moo42h2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:75213` with
  `ontology_mapping.ontology_id: CHEBI:75213`, label
  `sodium molybdate dihydrate`, source `CHEBI`,
  `mapping_quality: NARROW_MATCH`, `mapping_status: REJECTED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 CultureMech recipe occurrences across 0 media after the merge.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na2moo42h2o` through `Na2s2o3`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:75213` as active
  `sodium molybdate dihydrate`, confirming that the tombstone points at the same
  target as its active merge winner.
- The 2026-08-13 `MERGED_INTO` event explains that this record was minted as a
  local hydrate unnecessarily because `CHEBI:75213` already denotes the
  dihydrate; the 2026-08-15 event then refreshed the tombstone ontology ID to
  the merge target so stale ontology-index lookups no longer route through
  anhydrous `CHEBI:75215`.
- An ignored-inclusive exact subject search of
  `mappings/ingredient_mappings.sssom.tsv` found no final `MIM:Na2moo42h2o`
  row, so the rejected tombstone does not publish a duplicate mapping.
- Minor: the rejected tombstone still carries active-looking
  `chemical_properties`, `nutritional_roles`, and synonym payloads inherited
  from its pre-merge state. They are stale, but they do not reach the final
  SSSOM.

## Completeness

- The rejected status, merge target, zero occurrence count, fixed node ID, and
  absence from final SSSOM agree.
- Remaining stale fields are tombstone cleanup only.

## Recommended Edits

- Minor: in `data/ingredients/mapped/Na2moo42h2o.yaml`, clear stale live-shape
  chemistry and role payloads or mark them explicitly historical if a tombstone
  cleanup pass is desired. The active fix belongs on
  `data/ingredients/mapped/Na2moo4_X_2_H2o.yaml`.
