# `data/ingredients/mapped/Glycyl_L-aspartic_Acid.yaml`

## Verdict

Pass with minor issues. The promoted MicrobeDecoder synonym match to active
`CHEBI:73804` Gly-Asp, the structure fields, and the final SSSOM row pass, but
the top-level note still says curator review is needed after promotion.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Glycyl_L-aspartic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:73804` with matching
  `ontology_mapping.ontology_id`, canonical label `Gly-Asp`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `C6H10N2O5`, molecular weight `190.155`, InChI
  `InChI=1S/C6H10N2O5/c7-2-4(9)8-3(6(12)13)1-5(10)11/h3H,1-2,7H2,(H,8,9)(H,10,11)(H,12,13)/t3-/m0/s1`,
  and SMILES `NCC(=O)N[C@@H](CC(=O)O)C(=O)O`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Glycolate.yaml data/ingredients/mapped/Glycolic_Acid.yaml data/ingredients/mapped/Glycyl-L-proline.yaml data/ingredients/mapped/Glycyl-glycine.yaml data/ingredients/mapped/Glycyl_L-aspartic_Acid.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Glycyl_L-aspartic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry carries
  the same ChEBI synonym match, raw MicrobeDecoder label, formula, InChI,
  SMILES, molecular weight, MicrobeDecoder source occurrence, and singleton
  type as the per-record YAML.
- OLS4 resolves `CHEBI:73804` as `Gly-Asp`, lists
  `glycyl-L-aspartic acid` as an exact synonym, and exposes the same formula,
  InChI, and SMILES as the record.
- The #213 evidence explicitly records that `Glycyl-L-aspartic acid` is the
  Gly-Asp dipeptide.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Glycyl_L-aspartic_Acid` to `CHEBI:73804` by `skos:exactMatch` and has an
  empty `other` payload.
- Minor: the top-level `notes` still preserve the old MicrobeDecoder import
  text saying no CAS-RN or CHEBI/NCIT match existed and curator review was
  needed. #213 and the `PROMOTED_TO_MAPPED` event superseded that state.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, `conf`, `docs`, and `.claude` found the active YAML, matching
  aggregate copies, the manual #213 promotion listed in
  `mappings/record_research_validation.md`, generated products, the final SSSOM
  row, and ignored aggregate backups.

## Completeness

- The synonym-based ChEBI identity, formula, InChI, SMILES, molecular weight,
  MicrobeDecoder source occurrence, ingredient type, and final SSSOM row are
  populated.
- The stale top-level note needs cleanup.

## Recommended Edits

- Minor: refresh `notes` in
  `data/ingredients/mapped/Glycyl_L-aspartic_Acid.yaml` so they describe the
  promoted `CHEBI:73804` Gly-Asp synonym decision instead of the old unresolved
  import state.
