# `data/ingredients/mapped/N-acetylglucosamine.yaml`

## Verdict

Pass. The exact `CHEBI:59640` N-acetylglucosamine identity, source-backed
carbon-source role, CultureMech occurrence count, accepted catalog alias, and
final exact row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/N-acetylglucosamine.yaml`.
- Identifier and grounding: `identifier: CHEBI:59640` with
  `ontology_mapping.ontology_id: CHEBI:59640`, label
  `N-acetylglucosamine`, source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 57 CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `N-acetyl-lysine` through `N-acetylmuramic_Acid`: exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:59640` as active
  `N-acetylglucosamine` and exposes `N-acetylglucosamines` as a stored related
  synonym.
- CultureMech supplied original role text `Carbon Source`, which directly
  supports the migrated `CARBON_SOURCE` role.
- `mappings/culturemech_residual_triage.tsv` records the one
  `N-acetylglucosamine (Sigma)` alias that was backfilled as a same-record
  catalog variant.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:N-acetylglucosamine` to `CHEBI:59640` with the ChEBI plural synonym, the
  Sigma catalog variant, and `CAS:7512-17-6` in `other`.

## Completeness

- The active ChEBI target, PubChem CAS provenance, 57/57 occurrence count,
  source-backed role, accepted aliases, and final row agree.
- Raw `Role: Carbon source; Properties: ...` import strings remain only in YAML
  and are correctly filtered from final SSSOM `other`.

## Recommended Edits

- None.
