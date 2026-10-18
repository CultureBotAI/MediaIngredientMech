# `data/ingredients/mapped/M-inositol.yaml`

## Verdict

Pass with minor issues. This record is intentionally rejected after its
scyllo-inositol grounding was merged into the active `Myo-inositol` record, and
the rejected subject is absent from final SSSOM.

Severity: minor.

## Identity

- Reviewed record: `data/ingredients/mapped/M-inositol.yaml`.
- Identifier and grounding: `identifier: CHEBI:17268` with
  `ontology_mapping.ontology_id: CHEBI:17268`, label `myo-inositol`, source
  `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: REJECTED`.
- Chemical properties: CAS RN `87-89-8`, formula `C6H12O6`, InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `M-inositol` through `MES_sodium_salt`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for the
  CHEBI-primary subset `M-inositol`, `M-xylene`, and `MES_sodium_salt`;
  `MES_Buffer` and `MES_Hydrat` were skipped because their primary identifiers
  use local and CAS prefixes outside the CHEBI/OBO term adapter scope.

## Evidence

- EBI OLS4 resolves `CHEBI:17268` as active `myo-inositol`, lists CAS RN
  `87-89-8`, and records formula `C6H12O6`.
- PubChem resolves CAS RN `87-89-8` to CID `892` with formula `C6H12O6`.
- The final SSSOM has no `MIM:M-inositol` row. It preserves `m-Inositol` only
  as a synonym on the active `MIM:Myo-inositol` exact row to `CHEBI:17268`.
- A gitignored-inclusive text search found the historical `MIM:m_Inositol`
  surfaces only in review TSVs, alias TSVs, and the active `Myo-inositol`
  final SSSOM row.

## Completeness

- The duplicate/tombstone state is intentional: `m-Inositol` was merged into
  `CHEBI:17268` `myo-Inositol` on 2026-08-13 because its previous
  `CHEBI:10642` scyllo-inositol grounding conflicted with CAS RN `87-89-8`.
- The stale scyllo-oriented synonym and structure payloads, plus the
  provisional `VITAMIN_SOURCE` role, remain in a rejected record and do not
  publish to final SSSOM.

## Recommended Edits

- Optionally strip stale synonyms, structure, and role facets from this rejected
  tombstone if the project starts normalizing tombstoned records.
