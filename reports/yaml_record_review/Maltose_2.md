# `data/ingredients/mapped/Maltose_2.yaml`

## Verdict

Pass with minor cleanup. This rejected duplicate is absent from final SSSOM
after the lower-case maltose row was merged into the active anomer-agnostic
`Maltose` record; only stale rejected-record role and alpha-anomer payloads
remain in YAML.

Severity: minor.

## Identity

- Reviewed record: `data/ingredients/mapped/Maltose_2.yaml`.
- Identifier and grounding: `identifier: CHEBI:17306` with
  `ontology_mapping.ontology_id: CHEBI:17306`, label `maltose`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: REJECTED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: zero occurrences after transfer to the active `Maltose` record.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Maltose_2` through `Maltotriose_Hydrate`: exited 0 and wrote zero ERROR
  rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  CHEBI-primary record.

## Evidence

- The 2026-08-13 duplicate merge tombstoned this record as `REJECTED` and
  transferred its occurrences to active `Maltose`.
- The 2026-08-15 and 2026-09-09 repairs refreshed the tombstone's
  `ontology_mapping.ontology_id` and `kg_microbe_node_id` to agree with the
  surviving `CHEBI:17306` identifier.
- A gitignored-inclusive search found no `MIM:Maltose_2` row in final SSSOM.

## Completeness

- No rows or synonyms publish from this rejected duplicate.
- The raw CultureMech role text, old role facets, and alpha-anomer-specific
  structure are stale relative to the surviving anomer-agnostic maltose record,
  but they are inert while the tombstone remains rejected.

## Recommended Edits

- Optionally prune the stale roles, alpha-specific synonym, and alpha-specific
  chemistry from the rejected tombstone.
