# `data/ingredients/mapped/Guaiazulene.yaml`

## Verdict

Pass. The CultureBotHT exact match to active `CHEBI:5550` guaiazulene, CAS RN,
structure fields, curated IUPAC synonym, and final SSSOM row agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Guaiazulene.yaml`.
- Identifier and grounding: `identifier: CHEBI:5550` with matching
  `ontology_mapping.ontology_id`, canonical label `guaiazulene`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS-RN `489-84-9`, formula `C15H18`, InChI
  `InChI=1S/C15H18/c1-10(2)13-7-5-11(3)14-8-6-12(4)15(14)9-13/h5-10H,1-4H3`,
  and SMILES `Cc1ccc(C(C)C)cc2c(C)ccc1-2`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Griseolutein_B.yaml data/ingredients/mapped/Ground_Beef.yaml data/ingredients/mapped/Guaiacol.yaml data/ingredients/mapped/Guaiazulene.yaml data/ingredients/mapped/Guanidine_Hydrochloride.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Guaiazulene.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry is
  identical to the split per-record YAML.
- OLS4 resolves `CHEBI:5550` as `guaiazulene`, lists CAS `489-84-9` as a
  database cross-reference, lists `1,4-dimethyl-7-(propan-2-yl)azulene` as an
  exact synonym, and reports formula `C15H18`, the same InChI, and the same
  SMILES as the record.
- `mappings/ingredient_mappings_row_review_manifest.tsv` marks the
  `CHEBI:5550` OAK/OLS review as `CONFIRMED_NO_ACTION`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Guaiazulene` to `CHEBI:5550` by `skos:exactMatch`; its `other` payload
  contains only the curated IUPAC synonym and `CAS:489-84-9`.
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
