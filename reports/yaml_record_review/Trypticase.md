# `data/ingredients/mapped/Trypticase.yaml`

## Verdict

Needs curation, major. The curated MICRO target, undefined-mixture
classification, occurrence count, aggregate row, and final SSSOM row pass, but
`PROTEIN_SOURCE` is still provisional name-pattern evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/Trypticase.yaml`.
- Identifier and grounding: `identifier: MICRO:0000175` with matching
  `ontology_mapping.ontology_id`, label `Trypticase peptone`, source `MICRO`,
  `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- Synonyms: raw CultureMech properties text plus one manual `trypticase`
  synonym.
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
  `MICRO:0000175` with label `Trypticase peptone` and `Trypticase` as a broad
  synonym.
- The final SSSOM row has
  `MIM:Trypticase skos:exactMatch MICRO:0000175`; this is an own-identifier
  identity row, so exact SSSOM predicate placement is correct despite the
  curated `CLOSE_MATCH` quality.
- The raw `Properties:` label is filtered out of final SSSOM `other`.

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

- The MICRO target, occurrence count, undefined-mixture classification,
  aggregate copy, and final SSSOM row agree.
- The only residual issue is the provisional `PROTEIN_SOURCE` role evidence.

## Recommended Edits

- Replace the `PROTEIN_SOURCE` computational prediction with curated
  database/literature evidence, or remove `nutritional_roles` until such
  support is added.
