# `data/ingredients/mapped/Na-acetate.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:32954` sodium acetate identity, CAS
provenance, source-backed buffer role, occurrence count, duplicate merge, and
structure pass, but the final SSSOM publishes non-synonyms in `other`.

## Identity

- Reviewed record: `data/ingredients/mapped/Na-acetate.yaml`.
- Identifier and grounding: `identifier: CHEBI:32954` with
  `ontology_mapping.ontology_id: CHEBI:32954`, label `sodium acetate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 1,166 CultureMech recipe occurrences across 1,165 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na-3-hydroxybutyrate` through `Na-ascorbate`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:32954` as active `sodium acetate`,
  with `cas:127-09-3`, formula `C2H3O2.Na`, the stored InChI/SMILES, and the
  accepted same-substance ChEBI synonyms.
- The `BUFFER` role is source-backed by CultureMech original role text that
  explicitly says `Role: Buffer`.
- The #414 merge correctly folded the duplicate live `Sodium acetate` record
  into this record.
- Major: final SSSOM row `MIM:Na-acetate` publishes `Optional ingredient`,
  `1 M Sodium acetate`, and `Sodium acetate(Fisher BP 333)` in `other`. These
  are a role/procurement flag, a concentration-qualified solution label, and a
  catalog surface, not unconstrained synonyms for sodium acetate itself.

## Completeness

- The active ChEBI target, CAS RN, structure, 1166/1165 occurrence count,
  duplicate merge, source-backed `BUFFER` role, and core sodium acetate
  synonyms agree.
- The raw `Role: Buffer; Properties: ...` strings are correctly filtered from
  final SSSOM `other`; the problem is the three remaining non-synonym tokens
  listed above.

## Recommended Edits

- Major: in `data/ingredients/mapped/Na-acetate.yaml`, keep role/procurement
  and concentration text as provenance only, and only publish true
  same-substance labels in final SSSOM `other`. Rebuild the final SSSOM and
  re-run final SSSOM validation plus product label validation after the
  synonym cleanup.
