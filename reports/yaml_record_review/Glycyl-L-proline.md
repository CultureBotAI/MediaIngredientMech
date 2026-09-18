# `data/ingredients/mapped/Glycyl-L-proline.yaml`

## Verdict

Pass with minor issues. The promoted MicrobeDecoder synonym match to active
`CHEBI:70744` Gly-Pro, the absorbed `Glycine-proline` duplicate, the structure
fields, and the final SSSOM row pass, but the top-level note still says curator
review is needed after promotion.

## Identity

- Reviewed record: `data/ingredients/mapped/Glycyl-L-proline.yaml`.
- Identifier and grounding: `identifier: CHEBI:70744` with matching
  `ontology_mapping.ontology_id`, canonical label `Gly-Pro`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `C7H12N2O3`, molecular weight `172.184`, InChI
  `InChI=1S/C7H12N2O3/c8-4-6(10)9-3-1-2-5(9)7(11)12/h5H,1-4,8H2,(H,11,12)/t5-/m0/s1`,
  and SMILES `NCC(=O)N1CCC[C@H]1C(=O)O`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Glycolate.yaml data/ingredients/mapped/Glycolic_Acid.yaml data/ingredients/mapped/Glycyl-L-proline.yaml data/ingredients/mapped/Glycyl-glycine.yaml data/ingredients/mapped/Glycyl_L-aspartic_Acid.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Glycyl-L-proline.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry carries
  the same ChEBI synonym match, raw MicrobeDecoder labels, formula, InChI,
  SMILES, molecular weight, MicrobeDecoder source occurrence, and singleton
  type as the per-record YAML.
- OLS4 resolves `CHEBI:70744` as `Gly-Pro`, lists `glycyl-L-proline` as an
  exact synonym, and exposes the same formula, InChI, and SMILES as the record.
- The `Glycine-proline` duplicate was explicitly absorbed by #213 as the same
  Gly-Pro dipeptide under hyphenated residue naming.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Glycyl-L-proline` to `CHEBI:70744` by `skos:exactMatch` and keeps
  `Glycine-proline` in `other`.
- Minor: the top-level `notes` still preserve the old MicrobeDecoder import
  text saying no CAS-RN or CHEBI/NCIT match existed and curator review was
  needed. #201/#213 and the `PROMOTED_TO_MAPPED` event superseded that state.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, `conf`, `docs`, and `.claude` found the active YAML, matching
  aggregate copies, the residual-grounding row, generated products, the final
  SSSOM row, and ignored aggregate backups.

## Completeness

- The synonym-based ChEBI identity, formula, InChI, SMILES, molecular weight,
  MicrobeDecoder source occurrence, ingredient type, and final SSSOM row are
  populated.
- The stale top-level note needs cleanup.

## Recommended Edits

- Minor: refresh `notes` in
  `data/ingredients/mapped/Glycyl-L-proline.yaml` so they describe the promoted
  `CHEBI:70744` Gly-Pro synonym decision instead of the old unresolved import
  state.
