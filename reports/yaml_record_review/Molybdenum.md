# `data/ingredients/mapped/Molybdenum.yaml`

## Verdict

Pass. The local molybdenum identity, #631 de-grounding from the ChEBI atom,
fallback registry mapping, occurrence count, and final registry row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Molybdenum.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.compound:molybdenum` with
  `ontology_mapping.ontology_id: kgmicrobe.compound:molybdenum`, source
  `kgmicrobe.compound`, `mapping_quality: FALLBACK_REGISTRY`, and
  `mapping_status: MAPPED`.
- Occurrences: two CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Modified_Wolfes_Minerals` through `Mono-_And_Disaccharides`: exited 0 and
  wrote zero ERROR rows.
- Direct Engine A term validation was skipped for this local registry record
  because its primary `kgmicrobe.compound` identifier is outside the OBO subset
  used for the batch.

## Evidence

- Fresh EBI OLS4 confirms `CHEBI:28685` is active `molybdenum atom` and has
  `Molybdenum` as an exact synonym; that is the candidate the #631 correction
  deliberately removed because the TAP trace-element source rows did not
  evidence a precise neutral atom, ion, salt, or counter-ion.
- A fresh PubChem lookup for `molybdenum` resolves elemental molybdenum rather
  than the unidentified TAP trace-element species, so it does not supply a
  narrower exact mapping for the current record.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Molybdenum` to
  the local `kgmicrobe.compound:molybdenum` identifier with the #631 comment and
  empty `other`.

## Completeness

- The local fallback identity, 2/2 occurrence count, ChEBI-atom rejection
  rationale, and final exact row agree.
- The record does not assert chemical properties, components, or media roles
  that would require stronger species-level evidence.

## Recommended Edits

- None.
