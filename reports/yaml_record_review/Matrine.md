# `data/ingredients/mapped/Matrine.yaml`

## Verdict

Pass. The exact ChEBI identity, CAS number, structure, and final SSSOM row all
pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Matrine.yaml`.
- Identifier and grounding: `identifier: CHEBI:6700` with
  `ontology_mapping.ontology_id: CHEBI:6700`, label `Matrine`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: zero CultureMech recipe occurrences.
- Chemical identity: `cas_rn: 519-02-8`, formula `C15H24N2O`, InChI and SMILES
  copied from ChEBI.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Marine_agar_2216` through `Mc_general_salts`: exited 0 and wrote zero ERROR
  rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  CHEBI-primary record.

## Evidence

- EBI OLS4 resolves `CHEBI:6700` as active `Matrine` with CAS `519-02-8`,
  formula `C15H24N2O`, and the same InChI and SMILES carried in the YAML.
- PubChem resolves CAS `519-02-8` to CID 91466 with formula `C15H24N2O`.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Matrine` to
  `CHEBI:6700` with `CAS:519-02-8` in `other`.

## Completeness

- The record does not publish unsupported roles or non-exact synonyms.

## Recommended Edits

- None.
