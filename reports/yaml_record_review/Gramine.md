# `data/ingredients/mapped/Gramine.yaml`

## Verdict

Pass. The CultureBotHT exact match to active `CHEBI:28948` gramine, CAS RN,
structure fields, curated IUPAC synonym, and final SSSOM row agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Gramine.yaml`.
- Identifier and grounding: `identifier: CHEBI:28948` with matching
  `ontology_mapping.ontology_id`, canonical label `gramine`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS-RN `87-52-5`, formula `C11H14N2`, InChI
  `InChI=1S/C11H14N2/c1-13(2)8-9-7-12-11-6-4-3-5-10(9)11/h3-7,12H,8H2,1-2H3`,
  and SMILES `CN(C)Cc1cnc2ccccc12`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Gossypetin.yaml data/ingredients/mapped/Gossypol.yaml data/ingredients/mapped/Gramicidin.yaml data/ingredients/mapped/Gramicidin_S.yaml data/ingredients/mapped/Gramine.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Gramine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry is
  identical to the split per-record YAML.
- OLS4 resolves `CHEBI:28948` as `gramine`, lists CAS `87-52-5` as a database
  cross-reference, lists `1-(1H-indol-3-yl)-N,N-dimethylmethanamine` as an
  exact synonym, and reports formula `C11H14N2`, the same InChI, and the same
  SMILES as the record.
- `mappings/ingredient_mappings_row_review_manifest.tsv` marks the
  `CHEBI:28948` OAK/OLS review as `CONFIRMED_NO_ACTION`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Gramine` to
  `CHEBI:28948` by `skos:exactMatch`; its `other` payload contains only the
  curated IUPAC synonym and `CAS:87-52-5`.
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
