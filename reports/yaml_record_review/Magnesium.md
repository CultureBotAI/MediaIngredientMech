# `data/ingredients/mapped/Magnesium.yaml`

## Verdict

Pass. This record is intentionally rejected after its neutral magnesium-atom
grounding was merged into the active `Magnesium(2+)` record, and the rejected
subject is absent from final SSSOM.

## Identity

- Reviewed record: `data/ingredients/mapped/Magnesium.yaml`.
- Identifier and grounding: `identifier: CHEBI:18420` with
  `ontology_mapping.ontology_id: CHEBI:18420`, label `magnesium(2+)`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: REJECTED`, and
  `representative: CHEBI:18420`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Macro_Component_2_For_J_Medium` through `Magnesium`: exited 0 and wrote zero
  ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for the
  CHEBI-primary subset `Macrolide_Antibiotic`, `Magainin_I`, `Magnesium(2)`,
  and `Magnesium`; `Macro_Component_2_For_J_Medium` was skipped because its
  primary identifier uses a local prefix outside the CHEBI/OBO term adapter
  scope.

## Evidence

- EBI OLS4 resolves `CHEBI:18420` as active `magnesium(2+)`.
- The 2026-09-11 `fix_element_atom_overclaims` merge moved this record's three
  CultureMech occurrences into `Magnesium(2+)` and dropped the old
  atom-grounded SSSOM row.
- The final SSSOM has no `MIM:Magnesium` row and no `CHEBI:25107` row.

## Completeness

- The duplicate/tombstone state is intentional and keeps the magnesium surface
  routed to the active Mg2+ record.
- No stale synonym, role, or chemistry payload publishes from this rejected
  record.

## Recommended Edits

- None.
