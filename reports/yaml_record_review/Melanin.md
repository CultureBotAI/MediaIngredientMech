# `data/ingredients/mapped/Melanin.yaml`

## Verdict

Pass. The exact ChEBI identity, structure, MicrobeDecoder occurrence, and final
SSSOM row all pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Melanin.yaml`.
- Identifier and grounding: `identifier: CHEBI:89634` with
  `ontology_mapping.ontology_id: CHEBI:89634`, label `Melanin`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 46 MicrobeDecoder `BacDive_Metabolite_production` occurrences
  and zero CultureMech recipe occurrences.
- Chemical identity: formula `C18H10N2O4`, InChI, and SMILES copied from
  ChEBI/PubChem.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Meat_peptone` through `Melezitose`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  CHEBI-primary record.

## Evidence

- EBI OLS4 resolves `CHEBI:89634` as active `Melanin` with CAS `8049-97-6`,
  formula `C18H10N2O4`, and the same InChI and SMILES carried in the YAML.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Melanin` to
  `CHEBI:89634` with empty `other`.

## Completeness

- The record does not publish unsupported roles or non-exact synonyms.

## Recommended Edits

- None.
