# `data/ingredients/mapped/Gossypol.yaml`

## Verdict

Pass. The CultureBotHT exact match to active `CHEBI:28584` gossypol, CAS RN,
structure fields, curated IUPAC synonym, and final SSSOM row agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Gossypol.yaml`.
- Identifier and grounding: `identifier: CHEBI:28584` with matching
  `ontology_mapping.ontology_id`, canonical label `gossypol`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS-RN `303-45-7`, formula `C30H30O8`, the ChEBI
  gossypol InChI, and the ChEBI gossypol SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Gossypetin.yaml data/ingredients/mapped/Gossypol.yaml data/ingredients/mapped/Gramicidin.yaml data/ingredients/mapped/Gramicidin_S.yaml data/ingredients/mapped/Gramine.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Gossypol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry is
  identical to the split per-record YAML.
- OLS4 resolves `CHEBI:28584` as `gossypol`, lists CAS `303-45-7` as a
  database cross-reference, lists
  `1,1',6,6',7,7'-hexahydroxy-3,3'-dimethyl-5,5'-di(propan-2-yl)[2,2'-binaphthalene]-8,8'-dicarbaldehyde`
  as an exact synonym, and reports formula `C30H30O8`, the same InChI, and the
  same SMILES as the record.
- The active unmapped `Gossypol-Acetic_Acid_Complex` record is a distinct
  complex and does not conflict with this exact gossypol mapping.
- `mappings/ingredient_mappings_row_review_manifest.tsv` marks the
  `CHEBI:28584` OAK/OLS review as `CONFIRMED_NO_ACTION`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Gossypol`
  to `CHEBI:28584` by `skos:exactMatch`; its `other` payload contains only the
  curated IUPAC synonym and `CAS:303-45-7`.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, `conf`, `docs`, and `.claude` found the active YAML, the separate
  unmapped acetic-acid-complex YAML, matching aggregate copies, generated
  products, the final SSSOM row, row-review TSVs, and ignored aggregate
  backups.

## Completeness

- The exact ChEBI identity, CAS RN, formula, InChI, SMILES, curated ChEBI
  synonym, ingredient type, and final SSSOM row are populated.
- No role facet is asserted, which is acceptable for this record.

## Recommended Edits

- None.
