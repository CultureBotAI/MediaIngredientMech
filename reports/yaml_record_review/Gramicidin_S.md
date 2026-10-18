# `data/ingredients/mapped/Gramicidin_S.yaml`

## Verdict

Pass. The MicrobeDecoder exact match to active `CHEBI:5530` gramicidin S, the
cyclic peptide structure fields, the source-occurrence accounting, and the
final SSSOM row agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Gramicidin_S.yaml`.
- Identifier and grounding: `identifier: CHEBI:5530` with matching
  `ontology_mapping.ontology_id`, canonical label `gramicidin S`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `C60H92N12O10`, molecular weight `1141.47`,
  the ChEBI/PubChem gramicidin S InChI, and the ChEBI/PubChem gramicidin S
  SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Gossypetin.yaml data/ingredients/mapped/Gossypol.yaml data/ingredients/mapped/Gramicidin.yaml data/ingredients/mapped/Gramicidin_S.yaml data/ingredients/mapped/Gramine.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Gramicidin_S.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry is
  identical to the split per-record YAML.
- OLS4 resolves `CHEBI:5530` as `gramicidin S`, lists CAS `113-73-5` as a
  database cross-reference, and reports formula `C60H92N12O10`, the same InChI,
  and the same SMILES as the record.
- The review-ingredients promotion correctly moved this record from
  `PENDING_REVIEW` to `MAPPED` after the imported OLS exact label match was
  checked locally.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Gramicidin_S` to `CHEBI:5530` by `skos:exactMatch` and has an empty
  `other` payload.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, `conf`, `docs`, and `.claude` found the active YAML, matching
  aggregate copies, the MicrobeDecoder auto-mapped review entry, generated
  products, the final SSSOM row, and ignored aggregate backups.

## Completeness

- The exact ChEBI identity, formula, InChI, SMILES, molecular weight,
  MicrobeDecoder source occurrence, singleton type, and final SSSOM row are
  populated.
- No role facet is asserted, which is acceptable for this record.

## Recommended Edits

- None.
