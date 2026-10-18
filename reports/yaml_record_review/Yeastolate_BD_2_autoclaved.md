# `data/ingredients/mapped/Yeastolate_BD_2_autoclaved.yaml`

## Verdict

Needs curation. The source-backed CultureMech grounding to the generic MicrO
Yeastolate class is structurally present in the aggregate row, but the reviewed
label carries BD, concentration, and autoclave qualifiers that should not be
exact-mapped to generic `MICRO:0000522`; the final SSSOM also exports a Difco
catalog variant as `other`.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Yeastolate_BD_2_autoclaved.yaml`.
- Identifier and grounding: `identifier: MICRO:0000522` with matching
  `ontology_mapping.ontology_id`, label `Yeastolate`, source `MICRO`,
  `mapping_quality: SYNONYM_MATCH`, `match_level: NORMALIZED`, and
  `mapping_status: MAPPED`.
- Preferred term: `Yeastolate (BD; 2%, autoclaved)`.
- Synonyms: one CultureMech catalog variant, `Yeastolate (Difco)`.
- Occurrences: four CultureMech occurrences across four media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on this 5-file batch:
  exited 0 and wrote zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- Fresh OLS4 exact search for `Yeastolate` in MicrO found active
  `MICRO:0000522` with label `Yeastolate` and Yeastolate-specific narrow
  synonyms.
- Focused Engine A label validation was skipped for this MicrO row because it
  has no CHEBI/OBO adapter.

## Evidence

- The final SSSOM exports
  `MIM:Yeastolate_BD_2_autoclaved skos:exactMatch MICRO:0000522`.
- The final SSSOM exports `Yeastolate (Difco)` as `other`.
- The record's structured evidence cites the CultureMech occurrence table exact
  match that folded the source label onto the MicrO Yeastolate class.

## Issues

- Major: `Yeastolate (BD; 2%, autoclaved)` has vendor, two-percent
  concentration, and heat-treatment qualifiers, so it is a narrower processed
  catalog ingredient rather than an exact synonym of generic MicrO Yeastolate.
- Major: final SSSOM exports `Yeastolate (Difco)` as an `other` synonym on the
  generic Yeastolate exact-match row, even though that label is catalog
  qualified.

## Completeness

- The aggregate copy and occurrence count agree.
- The mapping should preserve Yeastolate as a parent or component rather than
  as the exact identity of the BD, two-percent, autoclaved source label.

## Recommended Edits

- Reground this record to a local MIM identifier for the BD, two-percent,
  autoclaved preparation.
- Move `MICRO:0000522` to an appropriate parent or component assertion if the
  source label is known to be Yeastolate-based.
- Suppress `Yeastolate (Difco)` from final SSSOM `other` on the generic MicrO
  exact row.
- Rebuild SSSOM, then rerun strict validation, SSSOM invariant validation, and
  the cross-record `other` synonym audit.
