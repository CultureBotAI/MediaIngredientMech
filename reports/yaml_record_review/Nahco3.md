# `data/ingredients/mapped/Nahco3.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:32139` sodium hydrogencarbonate
identity, CAS-backed structure, `BUFFER` role, occurrence count, and core ChEBI
aliases pass, but final SSSOM still publishes a malformed alias plus vendor and
concentration labels as synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Nahco3.yaml`.
- Identifier and grounding: `identifier: CHEBI:32139` with
  `ontology_mapping.ontology_id: CHEBI:32139`, label
  `sodium hydrogencarbonate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 3,168 source occurrences across 3,163 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Nah2po4_X_2_H2o` through `Nalidixic_Acid_Sodium_Salt`: exited 0 and left
  `reports/instance_validation_failures.tsv` header-only.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:32139` as active
  `sodium hydrogencarbonate` with formula `CHO3.Na`, CAS `144-55-8`, and the
  same InChI and SMILES as the record.
- A fresh PubChem CAS lookup for `144-55-8` resolves to sodium bicarbonate with
  the same InChI, confirming the chemical block.
- The `BUFFER` role is supported by imported CultureMech `Buffer` source role
  text.
- Major: `NaHCO` is a malformed formula, not an OLS synonym for
  `CHEBI:32139`, and still publishes in final SSSOM `other`.
- Major: `NaHCO3(Fisher S 233)` and the 10%, 1 M, 3%, 5%, and 7.5% solution
  labels are formulation or catalog strings; they should not publish as exact
  synonyms for the plain salt.
- Minor: the auto-proposed `pmid: 39954419` mapping evidence is redundant and
  weak as an identity source for the active CHEBI row.

## Completeness

- The active ChEBI term, CAS RN, formula, structure, 3,163/3,168 occurrence
  count, role evidence, and exact SSSOM row otherwise agree.
- Raw role/property strings and autoclaving notes are filtered from final
  SSSOM; the remaining consequential gaps are the active malformed,
  vendor-qualified, and concentration-qualified synonyms.

## Recommended Edits

- Major: in `data/ingredients/mapped/Nahco3.yaml`, reject or delete `NaHCO`,
  `NaHCO3(Fisher S 233)`, and the concentration-qualified `NaHCO3 (...)`
  synonyms from the CultureMech alias backfill.
- Minor: remove `pmid: 39954419` from
  `ontology_mapping.evidence` unless a curator finds it materially supports
  the identity decision better than the existing database evidence.
