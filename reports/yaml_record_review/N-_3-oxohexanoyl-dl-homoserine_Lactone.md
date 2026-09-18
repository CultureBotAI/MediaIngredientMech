# `data/ingredients/mapped/N-_3-oxohexanoyl-dl-homoserine_Lactone.yaml`

## Verdict

Pass. The local CAS identity for the DL homoserine lactone, curated ChEBI
parent narrow match, rejected inherited synonym, structure, and three final
SSSOM rows pass.

## Identity

- Reviewed record:
  `data/ingredients/mapped/N-_3-oxohexanoyl-dl-homoserine_Lactone.yaml`.
- Identifier and grounding: `identifier: cas:76924-95-3` with
  `ontology_mapping.ontology_id: CHEBI:29640`, label
  `N-(3-oxohexanoyl)homoserine lactone`, source `CHEBI`,
  `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no direct CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `N-_3-oxohexanoyl-dl-homoserine_Lactone` through
  `N-acetyl-glutamine`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:29640` as active
  `N-(3-oxohexanoyl)homoserine lactone`, the nearest ChEBI parent retained by
  the #456 stereochemistry fix.
- A fresh PubChem lookup for CID `119133` returns formula `C10H15NO4` and the
  same InChI stored for the CAS identity.
- The inherited parent synonym is typed `REJECTED_LABEL` in YAML and is absent
  from final SSSOM `other`.
- The final SSSOM publishes the intended `skos:narrowMatch` row to
  `CHEBI:29640`, a CAS identity row for `cas:76924-95-3`, and the required
  kg-microbe registry exact row.

## Completeness

- The local CAS identity, parent ChEBI anchor, CAS RN, structure, rejected
  parent synonym, and final multi-row SSSOM pattern agree.
- The record does not assert components, roles, or non-synonym final `other`
  text.

## Recommended Edits

- None.
