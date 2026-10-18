# `data/ingredients/mapped/Harmine.yaml`

## Verdict

Pass. The exact harmine ChEBI identity, CAS RN, structure fields, ChEBI
synonym, and final SSSOM row are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Harmine.yaml`.
- Identifier and grounding: `identifier: CHEBI:28121` with
  `ontology_mapping.ontology_id: CHEBI:28121`, label `harmine`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `442-51-3`, formula `C13H12N2O`, InChI
  `InChI=1S/C13H12N2O/c1-8-13-11(5-6-14-8)10-4-3-9(16-2)7-12(10)15-13/h3-7,15H,1-2H3`,
  and SMILES `COc1ccc2c(c1)nc1c(C)nccc12`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Hans_100x_Vitamins.yaml data/ingredients/mapped/Harmaline.yaml data/ingredients/mapped/Harmalol.yaml data/ingredients/mapped/Harmane.yaml data/ingredients/mapped/Harmine.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `linkml-term-validator` passed for `CHEBI:28121` and the CAS registry CURIE.
- The matching aggregate `data/curated/mapped_ingredients.yaml` entry is
  identical to the split per-record YAML.

## Evidence

- OLS4 resolves `CHEBI:28121` as active `harmine` with CAS `442-51-3`,
  formula `C13H12N2O`, the same InChI, and the same SMILES.
- The final SSSOM synonym token
  `7-methoxy-1-methyl-9H-pyrido[3,4-b]indole` occurs as a ChEBI synonym for
  `CHEBI:28121`; the final `CAS:442-51-3` token matches
  `chemical_properties.cas_rn`.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Harmine` to
  `CHEBI:28121`.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, exact synonym,
  and final SSSOM row are present and consistent.

## Recommended Edits

- None.
