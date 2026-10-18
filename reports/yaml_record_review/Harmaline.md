# `data/ingredients/mapped/Harmaline.yaml`

## Verdict

Pass. The exact harmaline ChEBI identity, CAS RN, structure fields, ChEBI
synonym, and final SSSOM row are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Harmaline.yaml`.
- Identifier and grounding: `identifier: CHEBI:28172` with
  `ontology_mapping.ontology_id: CHEBI:28172`, label `harmaline`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `304-21-2`, formula `C13H14N2O`, InChI
  `InChI=1S/C13H14N2O/c1-8-13-11(5-6-14-8)10-4-3-9(16-2)7-12(10)15-13/h3-4,7,15H,5-6H2,1-2H3`,
  and SMILES `COc1ccc2c3c(nc2c1)C(C)=NCC3`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Hans_100x_Vitamins.yaml data/ingredients/mapped/Harmaline.yaml data/ingredients/mapped/Harmalol.yaml data/ingredients/mapped/Harmane.yaml data/ingredients/mapped/Harmine.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `linkml-term-validator` passed for `CHEBI:28172` and the CAS registry CURIE.
- The matching aggregate `data/curated/mapped_ingredients.yaml` entry is
  identical to the split per-record YAML.

## Evidence

- OLS4 resolves `CHEBI:28172` as active `harmaline` with CAS `304-21-2`,
  formula `C13H14N2O`, the same InChI, and the same SMILES.
- The final SSSOM synonym token
  `7-methoxy-1-methyl-4,9-dihydro-3H-pyrido[3,4-b]indole` occurs as a ChEBI
  synonym for `CHEBI:28172`; the final `CAS:304-21-2` token matches
  `chemical_properties.cas_rn`.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Harmaline` to
  `CHEBI:28172`.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, exact synonym,
  and final SSSOM row are present and consistent.

## Recommended Edits

- None.
