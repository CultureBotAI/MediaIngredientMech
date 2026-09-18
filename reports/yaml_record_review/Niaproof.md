# `data/ingredients/mapped/Niaproof.yaml`

## Verdict

Pass. The `Niaproof` MicrobeDecoder trait is mapped to `CHEBI:75273` sodium
tetradecyl sulfate through the accepted Niaproof 4 trade-name synonym, and its
ChEBI/PubChem structure and final SSSOM row agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Niaproof.yaml`.
- Identifier and grounding: `identifier: CHEBI:75273` with
  `ontology_mapping.ontology_id: CHEBI:75273`, label
  `sodium tetradecyl sulfate`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 24 MicrobeDecoder source occurrences and no CultureMech media
  occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Niaproof` through `Nicl2`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:75273` as active
  `sodium tetradecyl sulfate`; its synonyms include `niaproof 4`, and its
  formula, InChI, and SMILES match the record.
- A fresh PubChem lookup for the CHEBI CAS `139-88-8` and for `Niaproof 4`
  returns the same sodium tetradecyl sulfate InChI, confirming the trade-name
  interpretation made in #213.
- The final SSSOM row maps `MIM:Niaproof` exactly to `CHEBI:75273` and emits no
  `other` synonym noise.

## Completeness

- The active ChEBI term, trade-name evidence, formula, structure, MicrobeDecoder
  occurrence count, ingredient type, and final exact row agree.
- No role, component, or environment assertions are present; those optional
  slots are appropriately empty.

## Recommended Edits

- None.
