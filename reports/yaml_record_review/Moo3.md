# `data/ingredients/mapped/Moo3.yaml`

## Verdict

Pass. The exact `CHEBI:30627` molybdenum trioxide identity, CAS-backed
structure, source-backed trace-element role, occurrence count, and final exact
row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Moo3.yaml`.
- Identifier and grounding: `identifier: CHEBI:30627` with
  `ontology_mapping.ontology_id: CHEBI:30627`, label `molybdenum trioxide`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 32 CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Monomethyl_Succinate` through `Moxifloxacin`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:30627` as active `molybdenum
  trioxide`; the final `other` tokens `[MoO3]`, `molybdenum(6+) oxide`, and
  `molybdenum(VI) oxide` are ontology aliases for this same term.
- A fresh PubChem lookup for CAS `1313-27-5` returns formula `MoO3` and the
  same InChI stored on the record.
- CultureMech supplied original role text `Mineral`, which supports the
  migrated `TRACE_ELEMENT` role for this molybdenum compound.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Moo3` to
  `CHEBI:30627` with same-substance synonyms and `CAS:1313-27-5` in `other`.

## Completeness

- The active ChEBI target, CAS RN, structure, occurrence count, role evidence,
  and final row agree.
- The raw `Role: Mineral source; Properties: ...` import strings remain only in
  YAML and are correctly filtered from final SSSOM `other`.

## Recommended Edits

- None.
