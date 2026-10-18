# `data/ingredients/mapped/Transvalencin_A.yaml`

## Verdict

Pass. The exact MeSH label upgrade, aggregate row, and final SSSOM row for
Transvalencin A are synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Transvalencin_A.yaml`.
- Identifier and grounding: `identifier: mesh:C498222` with matching
  `ontology_mapping.ontology_id`, label `transvalencin A`, source `MESH`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Synonyms: none.
- Occurrences: no MediaDive/media occurrence count.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Trans-cinnamic_Acid` through `Trehalose`: exited 0 and wrote zero ERROR
  rows.
- Direct old Engine A/OBO term validation was skipped for this MeSH row because
  `mesh:C498222` is intentionally outside the CHEBI-focused OBO term subset.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh exact OLS4 search for `Transvalencin A` returns MeSH `mesh:C498222`
  `transvalencin A`; the nearest ChEBI candidate in the old kg-microbe
  placeholder note was Transvalencin Z, a different named molecule.
- The final SSSOM row has
  `MIM:Transvalencin_A skos:exactMatch mesh:C498222`, uses `registry:mesh`,
  and leaves `other` empty.

## Completeness

- The MeSH identity, aggregate copy, and final SSSOM row agree.
- No synonyms, roles, components, chemical properties, environmental contexts,
  or final `other` tokens are asserted.

## Recommended Edits

- None.
