# `data/ingredients/mapped/Niso4_X_7_H2o.yaml`

## Verdict

Needs curation - major. The record now maps exactly to
`CHEBI:53504` nickel sulfate heptahydrate and rejects hexahydrate aliases, but
it still carries anhydrous structure, anhydrous final synonyms, and a
provisional `TRACE_ELEMENT` role.

## Identity

- Reviewed record: `data/ingredients/mapped/Niso4_X_7_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:53504` with
  `ontology_mapping.ontology_id: CHEBI:53504`, label
  `nickel sulfate heptahydrate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 9 CultureMech recipe occurrences across 9 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Niso4_X_6_H2o` through `Nitrilotriacetic_Acid`: exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:53504` as active
  `nickel sulfate heptahydrate` with formula `7H2O.Ni.O4S`, CAS
  `10101-98-1`, and heptahydrate-specific InChI and SMILES.
- A fresh PubChem CAS lookup for `10101-98-1` resolves to nickel sulfate
  heptahydrate with the same InChI, confirming the #374 promotion to the
  form-specific ChEBI term.
- Major: `chemical_properties` now has the corrected formula `Ni.O4S.7H2O`,
  but the InChI and SMILES still describe anhydrous nickel sulfate.
- Major: final SSSOM `other` still exports `nickel(2+) sulfate`, an anhydrous
  parent label; the heptahydrate row should keep only heptahydrate synonyms.
- Major: `nutritional_roles.TRACE_ELEMENT` has only
  `COMPUTATIONAL_PREDICTION` evidence from a curated name-pattern rule.

## Completeness

- The active ChEBI term, formula, specific-hydrate CAS, rejected hexahydrate
  labels, 9/9 occurrence count, and final exact target otherwise agree.
- The remaining consequential gaps are the stale anhydrous structure, parent
  synonym in final SSSOM, and unsupported provisional role.

## Recommended Edits

- Major: in `data/ingredients/mapped/Niso4_X_7_H2o.yaml`, either replace the
  stale anhydrous InChI/SMILES with ChEBI heptahydrate structure values or
  clear them until that evidence is synchronized.
- Major: reject or demote `nickel(2+) sulfate`, then rebuild final SSSOM so the
  heptahydrate row does not publish an anhydrous parent synonym.
- Major: replace the provisional `TRACE_ELEMENT` role with inspected
  claim-level evidence or remove it.
