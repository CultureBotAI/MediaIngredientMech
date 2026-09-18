# `data/ingredients/mapped/Trypticase_Peptone.yaml`

## Verdict

Needs curation, major. The exact MICRO identity, catalog variants, occurrence
count, aggregate row, and final SSSOM row pass, but `PROTEIN_SOURCE` is still
provisional name-pattern evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/Trypticase_Peptone.yaml`.
- Identifier and grounding: `identifier: MICRO:0000175` with matching
  `ontology_mapping.ontology_id`, label `Trypticase peptone`, source `MICRO`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- Synonyms: exact spelling variant plus curated BD/BBL catalog variants.
- Occurrences: 785 CultureMech recipe occurrences in 785 media.
- Roles: one `nutritional_roles.PROTEIN_SOURCE` facet at confidence `0.8`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Trypticase-glucose-yeast_Extract` through `Tryptone_Peptone`: exited 0 and
  wrote zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh MICRO-scoped OLS4 exact search for `Trypticase peptone` resolves
  `MICRO:0000175` with label `Trypticase peptone`.
- The final SSSOM row has
  `MIM:Trypticase_Peptone skos:exactMatch MICRO:0000175` and exports only the
  curated catalog variants and the `Tripticase peptone` spelling variant in
  `other`.
- The final `none|UNKNOWN_TERM` validation stamp is stale prefix coverage
  noise: the prefix-specific OLS search resolves the exact MICRO CURIE.

## Issues

### Major: `PROTEIN_SOURCE` is provisional name-pattern evidence

The only role assertion is:

```yaml
nutritional_roles:
- role: PROTEIN_SOURCE
  confidence: 0.8
  evidence:
  - reference_type: COMPUTATIONAL_PREDICTION
    reference_text: Inferred from curated media-role name pattern
    curator_note: Provisional role from a curated name-pattern rule; review recommended.
```

The exact MICRO identity does not independently curate the protein-source
role.

## Completeness

- The MICRO identity, occurrence count, catalog variants, aggregate copy, and
  final SSSOM row agree.
- The only residual issue is the provisional `PROTEIN_SOURCE` role evidence.

## Recommended Edits

- Replace the `PROTEIN_SOURCE` computational prediction with curated
  database/literature evidence, or remove `nutritional_roles` until such
  support is added.
