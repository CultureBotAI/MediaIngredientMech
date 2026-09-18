# `data/ingredients/mapped/Ground_Beef.yaml`

## Verdict

Needs curation. The FoodOn exact mapping, undefined-mixture type, occurrence
count, and final SSSOM row pass, but the `PROTEIN_SOURCE` role is still an
unsupported computational name-pattern inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Ground_Beef.yaml`.
- Identifier and grounding: `identifier: FOODON:00001282` with matching
  `ontology_mapping.ontology_id`, canonical label `beef (ground)`, source
  `FOODON`, `mapping_quality: LEXICAL_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- Occurrence statistics: `total_occurrences: 92` and `media_count: 92`, derived
  from the refreshed CultureMech occurrence table.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Griseolutein_B.yaml data/ingredients/mapped/Ground_Beef.yaml data/ingredients/mapped/Guaiacol.yaml data/ingredients/mapped/Guaiazulene.yaml data/ingredients/mapped/Guanidine_Hydrochloride.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Ground_Beef.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry is
  identical to the split per-record YAML.
- OLS4 resolves `FOODON:00001282` as active `beef (ground)`, lists
  `ground beef` as a synonym, and defines the class as beef that has been
  ground.
- `mappings/ingredient_mappings_row_review_manifest.tsv` marks the
  `FOODON:00001282` OAK/OLS review as `CONFIRMED_NO_ACTION`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Ground_Beef` to `FOODON:00001282` by `skos:exactMatch` and has an empty
  `other` payload.
- Major: `nutritional_roles.PROTEIN_SOURCE` is supported only by
  `COMPUTATIONAL_PREDICTION` from `infer_roles_from_name_lists`; no inspected
  source demonstrates the nutritional role for this FoodOn ingredient.
- Minor: the top-level `notes` value is the original import note and still says
  no CHEBI or NCIT match was found and curator review is needed, even though
  the record now has a reviewed FoodOn mapping and refreshed occurrence counts.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, `conf`, `docs`, and `.claude` found the active YAML, matching
  aggregate copies, residual fat-free ground-beef labels that are distinct from
  this record, generated products, the final SSSOM row, row-review TSVs, and
  ignored aggregate backups.

## Completeness

- The exact FoodOn identity, undefined-mixture type, occurrence counts,
  CultureMech raw label, and final SSSOM row are populated.
- The protein-source role needs source-backed evidence or removal.

## Recommended Edits

- Major: remove `nutritional_roles.PROTEIN_SOURCE` from
  `data/ingredients/mapped/Ground_Beef.yaml` unless a curated source can be
  attached at the role facet proving that this ingredient was used as a protein
  source in a medium.
- Minor: replace the stale top-level note with current FoodOn grounding and
  occurrence-provenance text.
