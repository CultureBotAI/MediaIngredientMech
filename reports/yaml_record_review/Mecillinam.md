# `data/ingredients/mapped/Mecillinam.yaml`

## Verdict

Pass. The exact ChEBI identity, CAS number, structure, exact synonym, and final
SSSOM row all pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Mecillinam.yaml`.
- Identifier and grounding: `identifier: CHEBI:51208` with
  `ontology_mapping.ontology_id: CHEBI:51208`, label `mecillinam`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: zero CultureMech recipe occurrences.
- Chemical identity: `cas_rn: 32887-01-7`, formula `C15H23N3O3S`, and InChI
  and SMILES copied from ChEBI.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Meat_peptone` through `Melezitose`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  CHEBI-primary record.

## Evidence

- EBI OLS4 resolves `CHEBI:51208` as active `mecillinam` with CAS
  `32887-01-7`, formula `C15H23N3O3S`, the same InChI carried in the YAML, and
  the exact IUPAC synonym curated in the record.
- PubChem resolves CAS `32887-01-7` to CID 36273 with formula `C15H23N3O3S` and
  the same InChI carried in the YAML.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Mecillinam` to
  `CHEBI:51208` with the curated IUPAC synonym and `CAS:32887-01-7` in `other`;
  both `other` tokens are same-substance synonyms.

## Completeness

- The record does not publish unsupported roles or non-exact synonyms.

## Recommended Edits

- None.
