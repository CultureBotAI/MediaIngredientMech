# `data/ingredients/mapped/Gossypetin.yaml`

## Verdict

Pass. The CultureBotHT exact match to active `CHEBI:16400` gossypetin, CAS RN,
structure fields, curated IUPAC synonym, and final SSSOM row agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Gossypetin.yaml`.
- Identifier and grounding: `identifier: CHEBI:16400` with matching
  `ontology_mapping.ontology_id`, canonical label `gossypetin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS-RN `489-35-0`, formula `C15H10O8`, InChI
  `InChI=1S/C15H10O8/c16-6-2-1-5(3-7(6)17)14-13(22)12(21)10-8(18)4-9(19)11(20)15(10)23-14/h1-4,16-20,22H`,
  and SMILES `O=c1c(O)c(-c2ccc(O)c(O)c2)oc2c(O)c(O)cc(O)c12`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Gossypetin.yaml data/ingredients/mapped/Gossypol.yaml data/ingredients/mapped/Gramicidin.yaml data/ingredients/mapped/Gramicidin_S.yaml data/ingredients/mapped/Gramine.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Gossypetin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry is
  identical to the split per-record YAML.
- OLS4 resolves `CHEBI:16400` as `gossypetin`, lists CAS `489-35-0` as a
  database cross-reference, lists
  `2-(3,4-dihydroxyphenyl)-3,5,7,8-tetrahydroxy-4H-chromen-4-one` as an exact
  synonym, and reports formula `C15H10O8`, the same InChI, and the same SMILES
  as the record.
- `mappings/ingredient_mappings_row_review_manifest.tsv` marks the
  `CHEBI:16400` OAK/OLS review as `CONFIRMED_NO_ACTION`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Gossypetin` to `CHEBI:16400` by `skos:exactMatch`; its `other` payload
  contains only the curated IUPAC synonym and `CAS:489-35-0`.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, `conf`, `docs`, and `.claude` found the active YAML, matching
  aggregate copies, generated products, the final SSSOM row, row-review TSVs,
  and ignored aggregate backups.

## Completeness

- The exact ChEBI identity, CAS RN, formula, InChI, SMILES, curated ChEBI
  synonym, ingredient type, and final SSSOM row are populated.
- No role facet is asserted, which is acceptable for this record.

## Recommended Edits

- None.
