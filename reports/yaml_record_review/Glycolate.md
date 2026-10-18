# `data/ingredients/mapped/Glycolate.yaml`

## Verdict

Pass. The reviewed MicrobeDecoder exact match to active `CHEBI:29805`
glycolate, the anion structure fields, the source-occurrence accounting, and
the final SSSOM row agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Glycolate.yaml`.
- Identifier and grounding: `identifier: CHEBI:29805` with matching
  `ontology_mapping.ontology_id`, canonical label `glycolate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `C2H3O3`, molecular weight `75.043`, InChI
  `InChI=1S/C2H4O3/c3-1-2(4)5/h3H,1H2,(H,4,5)/p-1`, and SMILES
  `O=C([O-])CO`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Glycolate.yaml data/ingredients/mapped/Glycolic_Acid.yaml data/ingredients/mapped/Glycyl-L-proline.yaml data/ingredients/mapped/Glycyl-glycine.yaml data/ingredients/mapped/Glycyl_L-aspartic_Acid.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Glycolate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry carries
  the same ChEBI exact match, anion formula, InChI, SMILES, molecular weight,
  CultureMech occurrence count, MicrobeDecoder source occurrence, and singleton
  type as the per-record YAML.
- OLS4 resolves `CHEBI:29805` as `glycolate` with formula `C2H3O3`, charge `-1`,
  the same InChI, and the same SMILES as the record.
- The review-ingredients promotion correctly moved this record from
  `PENDING_REVIEW` to `MAPPED` after the imported OLS exact label match was
  checked locally.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Glycolate`
  to `CHEBI:29805` by `skos:exactMatch` and has an empty `other` payload.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, `conf`, `docs`, and `.claude` found the active YAML, matching
  aggregate copies, the MicrobeDecoder auto-mapped review entry, generated
  products, the final SSSOM row, and ignored aggregate backups.

## Completeness

- The exact ChEBI identity, anion formula, InChI, SMILES, molecular weight,
  ingredient type, source occurrence, CultureMech occurrence count, and final
  SSSOM row are populated.

## Recommended Edits

- None.
