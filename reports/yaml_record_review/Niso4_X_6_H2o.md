# `data/ingredients/mapped/Niso4_X_6_H2o.yaml`

## Verdict

Pass with minor issues. This duplicate hexahydrate record has been tombstoned
as `REJECTED` and merged into the active `CHEBI:53437` nickel sulfate
hexahydrate record, so it no longer publishes final SSSOM rows; stale role,
synonym, and structure fields remain only on the rejected tombstone.

## Identity

- Reviewed record: `data/ingredients/mapped/Niso4_X_6_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:53437` with
  `ontology_mapping.ontology_id: CHEBI:53437`, label
  `nickel sulfate hexahydrate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: REJECTED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 active occurrences; the previous hexahydrate occurrences were
  transferred to `Nickel_II_sulfate_hexahydrate.yaml`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Niso4_X_6_H2o` through `Nitrilotriacetic_Acid`: exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  rejected record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:53437` as active
  `nickel sulfate hexahydrate` with formula `6H2O.Ni.O4S` and CAS
  `10101-97-0`.
- The August 2026 merge history records that this row was merged into
  `CHEBI:53437` `Nickel (II) sulfate hexahydrate`; the later tombstone repair
  synchronized `ontology_id` to that same target.
- Filtering the final `mappings/ingredient_mappings.sssom.tsv` produced no
  active `MIM:Niso4_X_6_H2o` row, which is correct for the tombstone.
- Minor: stale anhydrous `chemical_properties` and stale hydrate/role synonyms
  remain on the rejected record even though the current identity points at the
  hexahydrate merge target.
- Minor: the provisional `TRACE_ELEMENT` role remains on the rejected
  tombstone.

## Completeness

- The rejected status, zero occurrence count, target CHEBI identifier, and
  absence from final SSSOM agree.
- The remaining cleanup is limited to stale tombstone-local fields that no
  longer publish to final SSSOM.

## Recommended Edits

- Minor: in `data/ingredients/mapped/Niso4_X_6_H2o.yaml`, clear or refresh the
  stale anhydrous structure, stale active hydrate synonyms, and stale
  `TRACE_ELEMENT` role so the rejected tombstone carries only merge-target
  provenance.
