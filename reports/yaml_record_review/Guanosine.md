# `data/ingredients/mapped/Guanosine.yaml`

## Verdict

Pass. The exact ChEBI identity, CAS RN, chemical structure, occurrence count,
exported synonyms, and final SSSOM row are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Guanosine.yaml`.
- Identifier and grounding: `identifier: CHEBI:16750` with
  `ontology_mapping.ontology_id: CHEBI:16750`, label `guanosine`, source
  `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `118-00-3`, formula `C10H13N5O5`, InChI
  `InChI=1S/C10H13N5O5/c11-10-13-7-4(8(19)14-10)12-2-15(7)9-6(18)5(17)3(1-16)20-9/h2-3,5-6,9,16-18H,1H2,(H3,11,13,14,19)/t3-,5-,6-,9-/m1/s1`,
  and SMILES
  `Nc1nc(=O)c2ncn([C@@H]3O[C@H](CO)[C@@H](O)[C@H]3O)c2n1`.
- Occurrence statistics: `total_occurrences: 10` and `media_count: 10`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Guanidinium_Chloride.yaml data/ingredients/mapped/Guanine.yaml data/ingredients/mapped/Guanosine.yaml data/ingredients/mapped/Gum_Arabic_From_Acacia_Tree.yaml data/ingredients/mapped/H23-methyl_Mercaptopropionate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `linkml-term-validator` passed for `CHEBI:16750`.
- The matching aggregate `data/curated/mapped_ingredients.yaml` entry is
  identical to the split per-record YAML.

## Evidence

- OLS4 resolves `CHEBI:16750` as active `guanosine` with CAS `118-00-3`.
- The formula, stereochemical InChI, and stereochemical SMILES describe the
  exact guanosine identity.
- The eight exported final-SSSOM synonym tokens are real guanosine synonyms,
  and the final `CAS:118-00-3` token matches `chemical_properties.cas_rn`.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Guanosine` to
  `CHEBI:16750`.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, `conf`, `docs`, and `.claude` found no adjacent duplicate active
  identity.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, exact synonyms,
  occurrence statistics, and final SSSOM row are present and consistent.

## Recommended Edits

- None.
