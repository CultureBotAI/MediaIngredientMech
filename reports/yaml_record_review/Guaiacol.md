# `data/ingredients/mapped/Guaiacol.yaml`

## Verdict

Pass. The CultureBotHT exact match to active `CHEBI:28591` guaiacol, CAS RN,
structure fields, curated IUPAC synonym, refreshed occurrence count, and final
SSSOM row agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Guaiacol.yaml`.
- Identifier and grounding: `identifier: CHEBI:28591` with matching
  `ontology_mapping.ontology_id`, canonical label `guaiacol`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS-RN `90-05-1`, formula `C7H8O2`, InChI
  `InChI=1S/C7H8O2/c1-9-7-5-3-2-4-6(7)8/h2-5,8H,1H3`, and SMILES
  `COc1ccccc1O`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Griseolutein_B.yaml data/ingredients/mapped/Ground_Beef.yaml data/ingredients/mapped/Guaiacol.yaml data/ingredients/mapped/Guaiazulene.yaml data/ingredients/mapped/Guanidine_Hydrochloride.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Guaiacol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry is
  identical to the split per-record YAML.
- OLS4 resolves `CHEBI:28591` as `guaiacol`, lists CAS `90-05-1` as a database
  cross-reference, lists `2-methoxyphenol` as an exact synonym, and reports
  formula `C7H8O2`, the same InChI, and the same SMILES as the record.
- `mappings/ingredient_mappings_row_review_manifest.tsv` marks the
  `CHEBI:28591` OAK/OLS review as `CONFIRMED_NO_ACTION`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Guaiacol`
  to `CHEBI:28591` by `skos:exactMatch`; its `other` payload contains only the
  curated IUPAC synonym and `CAS:90-05-1`.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, `conf`, `docs`, and `.claude` found the active YAML, matching
  aggregate copies, generated products, the final SSSOM row, row-review TSVs,
  and ignored aggregate backups.

## Completeness

- The exact ChEBI identity, CAS RN, formula, InChI, SMILES, curated ChEBI
  synonym, ingredient type, occurrence count, and final SSSOM row are populated.
- No role facet is asserted, which is acceptable for this record.

## Recommended Edits

- None.
