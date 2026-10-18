# `data/ingredients/mapped/Tomato_Juice.yaml`

## Verdict

Needs curation, major. The FOODON identity, undefined-mixture classification,
occurrence count, and aggregate row are synchronized, but the final SSSOM row
exports a brand-qualified raw label as a synonym.

## Identity

- Reviewed record: `data/ingredients/mapped/Tomato_Juice.yaml`.
- Identifier and grounding: `identifier: FOODON:03301454` with matching
  `ontology_mapping.ontology_id`, label `tomato juice`, source `FOODON`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- Synonyms: raw mim-queue source form `Tomato juice` plus raw CultureMech
  source form `Tomato juice (Del Monte)`.
- Occurrences: 21 CultureMech recipe occurrences in 21 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tomato_Juice` through `Trace_Element_Solution`: exited 0 and wrote zero
  ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh exact OLS4 search for `tomato juice` returns `FOODON:03301454` with
  label `tomato juice`.
- The final SSSOM row has
  `MIM:Tomato_Juice skos:exactMatch FOODON:03301454`, uses `obo:foodon.owl`,
  and carries `Tomato juice (Del Monte)` in `other`.

## Issues

### Major: final `other` exports a brand-qualified source label

`Tomato juice (Del Monte)` is a CultureMech recipe surface that folded onto
the FOODON tomato-juice record. It is useful as occurrence provenance, but it
is not a synonym of the general FOODON class because the parenthetical text is
brand-specific. Exporting it in final SSSOM `other` violates the rule that
final synonym tokens must be true synonyms of the mapped subject.

## Completeness

- The FOODON identity, occurrence count, `UNDEFINED_MIXTURE` classification,
  and aggregate copy agree.
- No CAS RN, chemical properties, components, or roles are asserted.
- The only issue is the brand-qualified synonym leaking to final SSSOM.

## Recommended Edits

- Keep `Tomato juice (Del Monte)` as provenance or a raw source alias, but mark
  it so the final SSSOM `other` exporter filters it out.
