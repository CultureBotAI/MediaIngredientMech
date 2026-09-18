# `data/ingredients/mapped/Tryptone.yaml`

## Verdict

Needs curation, major. The exact MICRO identity, occurrence count, aggregate
row, and own SSSOM row pass, but malformed and CAS-decorated raw labels leak
into final SSSOM `other`, and `PROTEIN_SOURCE` is still provisional
name-pattern evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/Tryptone.yaml`.
- Identifier and grounding: `identifier: MICRO:0000182` with matching
  `ontology_mapping.ontology_id`, label `tryptone`, source `MICRO`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- CAS RN: `84843-69-6`.
- Synonyms: raw CultureMech labels plus curated catalog variants for Bacto,
  BD, Difco, and VWR tryptone forms.
- Occurrences: 1600 CultureMech recipe occurrences in 1583 media.
- Roles: one `nutritional_roles.PROTEIN_SOURCE` facet at confidence `0.8`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Trypticase-glucose-yeast_Extract` through `Tryptone_Peptone`: exited 0 and
  wrote zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh MICRO-scoped OLS4 exact search for `tryptone` resolves `MICRO:0000182`
  with label `tryptone`.
- The final SSSOM row has `MIM:Tryptone skos:exactMatch MICRO:0000182` and
  exports curated catalog variants, a CAS token, `Tryptone(CAS: 91079-40-2)`,
  and the malformed `Tryptone(Sigma T 9410))` label in `other`.

## Issues

### Major: final `other` exports raw CAS-decorated and malformed labels

`Tryptone(CAS: 91079-40-2)` carries a CAS annotation inside the synonym text,
and `Tryptone(Sigma T 9410))` is a malformed catalog label with an extra
closing parenthesis. They should not be exported as final SSSOM synonyms.

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

- The MICRO identity, occurrence count, undefined-mixture classification,
  aggregate copy, and own SSSOM row agree.
- The residual issues are limited to noisy exported raw labels and the
  provisional role assertion.

## Recommended Edits

- Mark the CAS-decorated and malformed raw CultureMech labels as
  non-exportable so final SSSOM `other` keeps only real tryptone synonyms and
  curated catalog variants.
- Replace the `PROTEIN_SOURCE` computational prediction with curated
  database/literature evidence, or remove `nutritional_roles` until such
  support is added.
