# `data/ingredients/mapped/Harmane.yaml`

## Verdict

Pass. The harman ChEBI identity, CAS-RN lookup grade, CAS RN, structure fields,
ChEBI synonym, and final SSSOM row are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Harmane.yaml`.
- Identifier and grounding: `identifier: CHEBI:5623` with
  `ontology_mapping.ontology_id: CHEBI:5623`, label `harman`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `486-84-0`, formula `C12H10N2`, InChI
  `InChI=1S/C12H10N2/c1-8-12-10(6-7-13-8)9-4-2-3-5-11(9)14-12/h2-7,14H,1H3`,
  and SMILES `Cc1nccc2c1nc1ccccc12`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Hans_100x_Vitamins.yaml data/ingredients/mapped/Harmaline.yaml data/ingredients/mapped/Harmalol.yaml data/ingredients/mapped/Harmane.yaml data/ingredients/mapped/Harmine.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `linkml-term-validator` passed for `CHEBI:5623` and the CAS registry CURIE.
- The matching aggregate `data/curated/mapped_ingredients.yaml` entry is
  identical to the split per-record YAML.

## Evidence

- OLS4 resolves `CHEBI:5623` as active `harman` with CAS `486-84-0`, formula
  `C12H10N2`, the same InChI, and the same SMILES.
- OLS4 lists `harmane` as a synonym for `CHEBI:5623`, and the final SSSOM
  synonym token `1-methyl-9H-pyrido[3,4-b]indole` also occurs as a ChEBI
  synonym for the target.
- The final `CAS:486-84-0` token matches `chemical_properties.cas_rn`.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Harmane` to
  `CHEBI:5623`.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, exact synonym,
  and final SSSOM row are present and consistent.

## Recommended Edits

- None.
