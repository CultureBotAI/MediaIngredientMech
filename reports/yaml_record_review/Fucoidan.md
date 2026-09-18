# `data/ingredients/mapped/Fucoidan.yaml`

## Verdict

Pass. The MicrobeDecoder import maps fucoidan to the exact ChEBI polysaccharide
class, the MicrobeDecoder source occurrence is retained, and the final SSSOM row
publishes no unsafe synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Fucoidan.yaml`.
- Identifier and grounding: `identifier: CHEBI:5181` with matching
  `ontology_mapping.ontology_id`, canonical label `fucoidan`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local ChEBI metadata for `CHEBI:5181` defines fucoidan as a
  fucose-rich sulfated polysaccharide type and has no fixed small-molecule
  formula to backfill.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Fructose-asparagine.yaml data/ingredients/mapped/Fructose.yaml data/ingredients/mapped/Fucoidan.yaml data/ingredients/mapped/Fucose.yaml data/ingredients/mapped/Fumarate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Fructose.yaml data/ingredients/mapped/Fucoidan.yaml data/ingredients/mapped/Fucose.yaml data/ingredients/mapped/Fumarate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four CHEBI-primary records in the batch.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:28757 CHEBI:5181 CHEBI:33984 CHEBI:29806`:
  returned the active ChEBI label, xrefs, synonyms, and definition for
  `CHEBI:5181`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, MicrobeDecoder source occurrence, empty synonym list, 0/0
  CultureMech occurrence counts, and absence of structure fields as the
  per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Fucoidan`
  to `CHEBI:5181` with `skos:exactMatch` and an empty `other` column.
- `mappings/microbedecoder_auto_mapped_review.tsv` approved the row by exact
  local OAK label review, and the record has no inferred nutritional,
  physicochemical, component, or environment claim that would need independent
  support.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports`, excluding prior per-record review reports and
  historical aggregate backups, found the active YAML, aggregate copy, final
  SSSOM row, MicrobeDecoder source row, and MicrobeDecoder approval row.

## Completeness

- The exact fucoidan ChEBI class, MicrobeDecoder source occurrence, and final
  SSSOM row are populated.
- Fixed chemical structure fields are correctly absent because the grounded
  ChEBI identity is a polysaccharide class.

## Recommended Edits

- None.
