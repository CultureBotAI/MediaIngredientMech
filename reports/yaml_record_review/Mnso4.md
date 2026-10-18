# `data/ingredients/mapped/Mnso4.yaml`

## Verdict

Pass. The exact `CHEBI:86360` anhydrous manganese sulfate identity, CAS,
source-backed trace-element role, hydrate-label filtering, occurrence count,
and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Mnso4.yaml`.
- Identifier and grounding: `identifier: CHEBI:86360` with
  `ontology_mapping.ontology_id: CHEBI:86360`, label
  `manganese(II) sulfate`, source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 399 CultureMech recipe occurrences.
- Chemical identity: CAS `7785-87-7`, formula `Mn.O4S`, SMILES, and InChI.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mncl2` through `Mnso4`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for all five
  CHEBI-primary records in the same batch.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:86360` as active
  `manganese(II) sulfate` and distinguishes the anhydrous term from the
  monohydrate, dihydrate, tetrahydrate, pentahydrate, and hexahydrate terms.
- The 2026-09-12 hidden-hydrate sweep marked wildcard and monohydrate-like
  sulfate strings `REJECTED_LABEL`.
- `TRACE_ELEMENT` is backed by an imported CultureMech role.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Mnso4` to
  `CHEBI:86360`.

## Completeness

- The anhydrous target, CAS, structure, 399/399 occurrence count, supported
  role, and final row agree.
- The raw `Role:`/`Properties:` imports and rejected hydrate labels are filtered
  from final SSSOM `other`.

## Recommended Edits

- None.
