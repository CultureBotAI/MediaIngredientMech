# `data/ingredients/mapped/Mops.yaml`

## Verdict

Pass. The exact `CHEBI:39074` MOPS identity, CAS metadata, CultureMech buffer
role, occurrence count, and final exact row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Mops.yaml`.
- Identifier and grounding: `identifier: CHEBI:39074` with
  `ontology_mapping.ontology_id: CHEBI:39074`, label `MOPS`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 91 CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Monomethyl_Succinate` through `Moxifloxacin`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:39074` as active `MOPS`.
- A fresh PubChem lookup for CAS `1132-61-2` returns formula `C7H15NO4S` and
  the same InChI stored on the record.
- CultureMech supplied original role text `Buffer`, which directly supports
  the migrated `BUFFER` role.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Mops` to
  `CHEBI:39074` with only `CAS:1132-61-2` in `other`.

## Completeness

- The active ChEBI target, CAS RN, occurrence count, role evidence, and final
  exact row agree.
- The raw `Role: Buffer; Properties: ...` import strings remain only in YAML
  and are correctly filtered from final SSSOM `other`.

## Recommended Edits

- None.
