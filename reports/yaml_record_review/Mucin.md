# `data/ingredients/mapped/Mucin.yaml`

## Verdict

Pass. The exact `NCIT:C16883` Mucin identity, MicrobeDecoder provenance, and
final exact row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Mucin.yaml`.
- Identifier and grounding: `identifier: NCIT:C16883` with
  `ontology_mapping.ontology_id: NCIT:C16883`, label `Mucin`, source `NCIT`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Occurrences: two MicrobeDecoder source occurrences from `bergey:substrates`
  and `literature:substrates`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `MreB_Perturbing_Compound_A22` through
  `Mucin_From_Porcine_StomachType_II`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this NCIT-primary
  record.

## Evidence

- A fresh NCIT-scoped EBI OLS4 lookup resolves `NCIT:C16883` as active `Mucin`
  with `Mucin` as an exact synonym.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Mucin` to
  `NCIT:C16883` with empty `other`.

## Completeness

- The NCIT target, exact label, MicrobeDecoder provenance, source occurrence
  count, and final row agree.
- The record does not assert chemical properties, components, roles, or
  non-synonym final `other` text.

## Recommended Edits

- None.
