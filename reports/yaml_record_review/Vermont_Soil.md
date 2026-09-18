# `data/ingredients/mapped/Vermont_Soil.yaml`

## Verdict

Pass. The local Vermont Soil identity, ENVO soil parent, aggregate row, and
paired final SSSOM rows pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Vermont_Soil.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.ingredient:vermont_soil`
  with parent `ENVO:00001998` `soil`, source `ENVO`,
  `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- The local identifier preserves the ingredient-level Vermont-sourced soil
  sample while ENVO supplies only the generic soil parent.
- Occurrences: one CultureMech recipe occurrence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Veratrine_Hydrochloride` through `Viomycin`: exited 0 and wrote zero ERROR
  rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- Engine A label validation was limited to the CHEBI records in this batch;
  this local `kgmicrobe.ingredient` row has no OBO adapter for that focused
  check.

## Evidence

- Fresh OLS4 lookup for `ENVO:00001998` returns active label `soil`, supporting
  the broader parent while leaving Vermont provenance on the local exact
  identity.
- The final SSSOM exports both
  `MIM:Vermont_Soil skos:narrowMatch ENVO:00001998` and
  `MIM:Vermont_Soil skos:exactMatch kgmicrobe.ingredient:vermont_soil`.
- The duplicate raw `Vermont Soil` synonym is filtered from final SSSOM
  `other`.

## Issues

None.

## Completeness

- The local exact identity, ENVO parent, occurrence count, aggregate copy, and
  paired final SSSOM rows agree.

## Recommended Edits

None.
