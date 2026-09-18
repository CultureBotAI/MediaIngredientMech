# `data/ingredients/mapped/Methyl-B-D-galactopyranoside.yaml`

## Verdict

Pass. The CAS-grounded ChEBI identity, structure, exact synonym, and final
SSSOM row all pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Methyl-B-D-galactopyranoside.yaml`.
- Identifier and grounding: `identifier: CHEBI:17540` with
  `ontology_mapping.ontology_id: CHEBI:17540`, label
  `methyl beta-D-galactoside`, source `CHEBI`, `mapping_quality:
  CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and `ingredient_type:
  SINGLE_INGREDIENT`.
- Occurrences: zero CultureMech recipe occurrences.
- Chemical identity: `cas_rn: 1824-94-8`, formula `C7H14O6`, and InChI and
  SMILES copied from ChEBI.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Methanol` through `Methyl-B-D-galactopyranoside`: exited 0 and wrote zero
  ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  CHEBI-primary record.

## Evidence

- EBI OLS4 resolves `CHEBI:17540` as active `methyl beta-D-galactoside` with
  CAS `1824-94-8`, formula `C7H14O6`, the same InChI and SMILES carried in the
  YAML, and the curated `Methyl beta-D-galactopyranoside` synonym.
- PubChem resolves CAS `1824-94-8` to CID 94214 with formula `C7H14O6` and the
  same InChI carried in the YAML.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Methyl-B-D-galactopyranoside` to `CHEBI:17540`; the non-CAS `other`
  token is an exact ChEBI synonym and `CAS:1824-94-8` matches
  `chemical_properties.cas_rn`.

## Completeness

- The record does not publish unsupported roles or non-exact synonyms.

## Recommended Edits

- None.
