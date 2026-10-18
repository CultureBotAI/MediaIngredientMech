# `data/ingredients/mapped/Methicillin.yaml`

## Verdict

Pass. The exact ChEBI identity, structure, MicrobeDecoder occurrence,
CultureMech spelling variant, and final SSSOM row all pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Methicillin.yaml`.
- Identifier and grounding: `identifier: CHEBI:6827` with
  `ontology_mapping.ontology_id: CHEBI:6827`, label `methicillin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: six MicrobeDecoder BacDive antibiotic occurrences and zero
  CultureMech recipe occurrences.
- Chemical identity: formula `C17H20N2O6S`, InChI, and SMILES copied from
  ChEBI/PubChem.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Methanol` through `Methyl-B-D-galactopyranoside`: exited 0 and wrote zero
  ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  CHEBI-primary record.

## Evidence

- EBI OLS4 resolves `CHEBI:6827` as active `methicillin` with CAS `61-32-5`,
  formula `C17H20N2O6S`, the same InChI and SMILES carried in the YAML, and the
  `meticillin` spelling variant.
- `mappings/culturemech_residual_groundings.tsv` records `Meticillin` as a
  synonym of the existing `CHEBI:6827` record.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Methicillin`
  to `CHEBI:6827` with `Meticillin` as the only `other` token.

## Completeness

- The record does not publish unsupported roles or non-exact synonyms.

## Recommended Edits

- None.
