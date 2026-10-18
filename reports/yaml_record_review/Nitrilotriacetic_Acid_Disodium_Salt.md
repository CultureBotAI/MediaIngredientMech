# `data/ingredients/mapped/Nitrilotriacetic_Acid_Disodium_Salt.yaml`

## Verdict

Needs curation - major. The `cas:15467-20-6` identity, `CHEBI:44557`
parent anchor, CAS and `kgmicrobe.compound` registry rows, and 7/7 occurrence
count pass, but the record still carries parent free-acid structure and
synonym data, and its `CHELATOR` role is only provisional.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Nitrilotriacetic_Acid_Disodium_Salt.yaml`.
- Identifier and grounding: `identifier: cas:15467-20-6` with
  `ontology_mapping.ontology_id: CHEBI:44557`, label
  `nitrilotriacetic acid`, source `CHEBI`, `mapping_quality: NARROW_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 7 CultureMech recipe occurrences across 7 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for the CHEBI parent
  mapping.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:44557` as active
  `nitrilotriacetic acid` with formula `C6H9NO6`, CAS `139-13-9`, InChI and
  SMILES for the parent free acid, and the free-acid synonym
  `N,N-bis(carboxymethyl)glycine`.
- A fresh PubChem lookup for CAS `15467-20-6` resolves to formula
  `C6H7NNa2O6` with two sodium counterions. The record's molecular formula
  matches that exact disodium identity.
- Major: `chemical_properties.inchi` and `chemical_properties.smiles` still
  describe the parent free acid rather than the disodium salt represented by
  CAS `15467-20-6` and molecular formula `C6H7NNa2O6`.
- Major: `N,N-bis(carboxymethyl)glycine` is an inherited synonym of the
  `CHEBI:44557` free-acid parent. It is exported in the final SSSOM `other`
  value on the `skos:narrowMatch` row, but it erases the disodium salt
  boundary.
- Major: `physicochemical_roles.CHELATOR` cites only the
  `infer_roles_from_name_lists` `COMPUTATIONAL_PREDICTION` evidence object.
  That name-pattern rule is explicitly provisional and does not independently
  support the role.
- The `skos:narrowMatch` parent row is accompanied by both expected identity
  rows: `cas:15467-20-6` and
  `kgmicrobe.compound:nitrilotriacetic_acid_disodium_salt`.

## Completeness

- The active parent ChEBI term, exact CAS RN, disodium formula, occurrence
  count, and local registry rows otherwise agree.
- The raw parenthetical disodium and trisodium fragments are filtered from the
  final SSSOM; the remaining consequential gaps are the stale structure block,
  the parent-free-acid synonym leaking into `other`, and unsupported chelator
  role evidence.

## Recommended Edits

- Major: in
  `data/ingredients/mapped/Nitrilotriacetic_Acid_Disodium_Salt.yaml`, replace
  the inherited parent InChI and SMILES with CAS `15467-20-6` disodium-salt
  structure values.
- Major: remove `N,N-bis(carboxymethyl)glycine` from this disodium record, or
  otherwise keep parent-only synonyms out of the final `other` value for parent
  mappings.
- Major: replace the `CHELATOR` role evidence with inspected source-backed
  chelation evidence, or remove the role until that evidence exists.
