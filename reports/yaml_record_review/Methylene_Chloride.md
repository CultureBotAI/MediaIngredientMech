# `data/ingredients/mapped/Methylene_Chloride.yaml`

## Verdict

Pass. The CAS-grounded `CHEBI:15767` dichloromethane identity, methylene
chloride synonym label, ChEBI/PubChem structure, CAS_RN_LOOKUP grade, and final
SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Methylene_Chloride.yaml`.
- Identifier and grounding: `identifier: CHEBI:15767` with
  `ontology_mapping.ontology_id: CHEBI:15767`, label `dichloromethane`, source
  `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: zero CultureMech recipe occurrences.
- Chemical identity: CAS `75-09-2`, formula `CH2Cl2`, SMILES, and InChI for
  dichloromethane, also known as methylene chloride.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Methylene_Blue` through `Methylxanthoxylin`: exited 0 and wrote zero ERROR
  rows.
- `uv run linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- EBI OLS4 resolves `CHEBI:15767` as active `dichloromethane` with CAS
  `75-09-2`, formula `CH2Cl2`, the same SMILES and InChI carried in the YAML,
  and `Methylene chloride` as a synonym.
- PubChem resolves CAS `75-09-2` to CID 6344 with the same formula and InChI
  carried in the YAML.
- The OAK/OLS row-review manifest confirmed this row with no curation action,
  and the #317/#438 regrade retained the CAS lookup provenance without changing
  the exact chemical identity.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Methylene_Chloride` to `CHEBI:15767` with only `CAS:75-09-2` in
  `other`.

## Completeness

- The record does not publish unsupported roles or non-exact synonyms.

## Recommended Edits

- None.
