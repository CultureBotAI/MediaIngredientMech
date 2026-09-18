# `data/ingredients/mapped/Hecogenin.yaml`

## Verdict

Pass. The exact hecogenin ChEBI identity, CAS RN, structure fields, and final
SSSOM row are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Hecogenin.yaml`.
- Identifier and grounding: `identifier: CHEBI:5633` with
  `ontology_mapping.ontology_id: CHEBI:5633`, label `Hecogenin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `467-55-0`, formula `C27H42O4`, InChI
  `InChI=1S/C27H42O4/c1-15-7-10-27(30-14-15)16(2)24-22(31-27)12-21-19-6-5-17-11-18(28)8-9-25(17,3)20(19)13-23(29)26(21,24)4/h15-22,24,28H,5-14H2,1-4H3/t15-,16+,17+,18+,19-,20+,21+,22+,24+,25+,26-,27-/m1/s1`,
  and SMILES
  `[H][C@@]12CC[C@]3([H])[C@]([H])(CC(=O)[C@@]4(C)[C@@]3([H])C[C@]3([H])O[C@]5(CC[C@@H](C)CO5)[C@@H](C)[C@]43[H])[C@@]1(C)CC[C@H](O)C2`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Harmol.yaml data/ingredients/mapped/Harmol_Hydrochloride.yaml data/ingredients/mapped/Hcl.yaml data/ingredients/mapped/Heart_Infusion_Agar_BD_211065.yaml data/ingredients/mapped/Hecogenin.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `linkml-term-validator` passed for `CHEBI:5633` and the CAS registry CURIE.
- The matching aggregate `data/curated/mapped_ingredients.yaml` entry is
  identical to the split per-record YAML.

## Evidence

- OLS4 resolves `CHEBI:5633` as active `Hecogenin` with CAS `467-55-0`,
  formula `C27H42O4`, the same InChI, and the same SMILES.
- The final `CAS:467-55-0` token matches `chemical_properties.cas_rn`.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Hecogenin` to
  `CHEBI:5633`.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, and final SSSOM
  row are present and consistent.

## Recommended Edits

- None.
