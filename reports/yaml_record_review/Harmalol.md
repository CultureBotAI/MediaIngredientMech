# `data/ingredients/mapped/Harmalol.yaml`

## Verdict

Pass. The exact harmalol ChEBI identity, CAS RN, structure fields, ChEBI
synonym, and final SSSOM row are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Harmalol.yaml`.
- Identifier and grounding: `identifier: CHEBI:27943` with
  `ontology_mapping.ontology_id: CHEBI:27943`, label `harmalol`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `525-57-5`, formula `C12H12N2O`, InChI
  `InChI=1S/C12H12N2O/c1-7-12-10(4-5-13-7)9-3-2-8(15)6-11(9)14-12/h2-3,6,14-15H,4-5H2,1H3`,
  and SMILES `CC1=NCCc2c1nc1cc(O)ccc21`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Hans_100x_Vitamins.yaml data/ingredients/mapped/Harmaline.yaml data/ingredients/mapped/Harmalol.yaml data/ingredients/mapped/Harmane.yaml data/ingredients/mapped/Harmine.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `linkml-term-validator` passed for `CHEBI:27943` and the CAS registry CURIE.
- The matching aggregate `data/curated/mapped_ingredients.yaml` entry is
  identical to the split per-record YAML.

## Evidence

- OLS4 resolves `CHEBI:27943` as active `harmalol` with CAS `525-57-5`,
  formula `C12H12N2O`, the same InChI, and the same SMILES.
- The final SSSOM synonym token
  `1-methyl-4,9-dihydro-3H-pyrido[3,4-b]indol-7-ol` occurs as a ChEBI synonym
  for `CHEBI:27943`; the final `CAS:525-57-5` token matches
  `chemical_properties.cas_rn`.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Harmalol` to
  `CHEBI:27943`.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, exact synonym,
  and final SSSOM row are present and consistent.

## Recommended Edits

- None.
