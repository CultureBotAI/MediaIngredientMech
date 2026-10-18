# `data/ingredients/mapped/Soil_Extract.yaml`

## Verdict

Needs curation - major. The exact `MICRO:0000457` soil extract identity,
undefined-mixture type, environmental context, and occurrence count pass, but
final SSSOM publishes recipe-specific parenthetical text as exact synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Soil_Extract.yaml`.
- Identifier and grounding: `identifier: MICRO:0000457` with
  `ontology_mapping.ontology_id: MICRO:0000457`, label `soil extract`, source
  `MICRO`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- Occurrences: 17 source occurrences across 17 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Soil_Extract` through `Sorbose`: exited 0 and wrote zero ERROR rows.
- Direct Engine A term validation was skipped for this record because `MICRO`
  is outside the OBO allowlist for `linkml-term-validator`; fresh
  prefix-specific EBI OLS4 lookup resolved `MICRO:0000457`.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh EBI OLS4 lookup resolves active `MICRO:0000457` with label
  `soil extract`, matching the exact MICRO grounding.
- The environmental context links the extract to `ENVO:00001998` soil with
  `NATURAL_SOURCE`, which matches the source material named by the ingredient.
- Major: final SSSOM publishes `Soil extract (see below)` and
  `Soil extract (SE1)` in `other`. The first is an instruction pointer and the
  second is a recipe-local variant label, not a general exact synonym of soil
  extract.

## Completeness

- The MICRO ID, label, mixture type, soil environmental context, exact row, and
  occurrence count agree.
- The only consequential gap is demoting the two CultureMech occurrence labels
  so they remain searchable locally without publishing as exact final synonyms.

## Recommended Edits

- Major: in `data/ingredients/mapped/Soil_Extract.yaml`, retype or suppress the
  `Soil extract (see below)` and `Soil extract (SE1)` occurrence labels so final
  SSSOM no longer emits them in `other`.
