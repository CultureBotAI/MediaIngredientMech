# `data/ingredients/mapped/Harmol.yaml`

## Verdict

Pass. The exact harmol ChEBI identity, CAS RN, structure fields, ChEBI synonym,
and final SSSOM row are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Harmol.yaml`.
- Identifier and grounding: `identifier: CHEBI:192558` with
  `ontology_mapping.ontology_id: CHEBI:192558`, label `harmol`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `487-03-6`, formula `C12H10N2O`, InChI
  `InChI=1S/C12H10N2O/c1-7-12-10(4-5-13-7)9-3-2-8(15)6-11(9)14-12/h2-6,14-15H,1H3`,
  and SMILES `Cc1nccc2c1nc1cc(O)ccc12`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Harmol.yaml data/ingredients/mapped/Harmol_Hydrochloride.yaml data/ingredients/mapped/Hcl.yaml data/ingredients/mapped/Heart_Infusion_Agar_BD_211065.yaml data/ingredients/mapped/Hecogenin.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `linkml-term-validator` passed for `CHEBI:192558` and the CAS registry CURIE.
- The matching aggregate `data/curated/mapped_ingredients.yaml` entry is
  identical to the split per-record YAML.

## Evidence

- OLS4 resolves `CHEBI:192558` as active `harmol` with CAS `487-03-6`,
  formula `C12H10N2O`, the same InChI, and the same SMILES.
- The final SSSOM synonym token `1-methyl-9H-beta-carbolin-7-ol` occurs as a
  ChEBI synonym for `CHEBI:192558`; the final `CAS:487-03-6` token matches
  `chemical_properties.cas_rn`.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Harmol` to
  `CHEBI:192558`.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, exact synonym,
  and final SSSOM row are present and consistent.

## Recommended Edits

- None.
