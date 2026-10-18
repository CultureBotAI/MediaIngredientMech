# `data/ingredients/mapped/Triton_X-100.yaml`

## Verdict

Needs curation, major. The exact CHEBI identity, CAS RN, structure fields,
aggregate row, and final SSSOM row pass, but `SURFACTANT` is still provisional
CHEBI-ancestry evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/Triton_X-100.yaml`.
- Identifier and grounding: `identifier: CHEBI:9750` with matching
  `ontology_mapping.ontology_id`, label `Triton X-100`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `9002-93-1`.
- Synonyms: none.
- Occurrences: 0 recipe occurrences in 0 media.
- Roles: one `physicochemical_roles.SURFACTANT` facet at confidence `0.7`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Triton_X-100` through `Tryptamine`: exited 0 and wrote zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh CHEBI-scoped OLS4 exact search for `Triton X-100` returns
  `CHEBI:9750` with label `Triton X-100`.
- The final SSSOM row has
  `MIM:Triton_X-100 skos:exactMatch CHEBI:9750` and exports only
  `CAS:9002-93-1` in `other`.

## Issues

### Major: `SURFACTANT` is provisional CHEBI-ancestry evidence

The only role assertion is:

```yaml
physicochemical_roles:
- role: SURFACTANT
  confidence: 0.7
  evidence:
  - reference_type: COMPUTATIONAL_PREDICTION
    reference_text: 'Inferred from CHEBI ancestry: subclass/has_role of CHEBI:35195
      (surfactant (role))'
    curator_note: Provisional role inferred from CHEBI is_a/has_role closure; review
      recommended.
```

The exact CHEBI and CAS identity do not independently curate the surfactant
role for this media ingredient record.

## Completeness

- The CHEBI identity, CAS RN, structure fields, aggregate copy, and final SSSOM
  row agree.
- The only residual issue is the provisional `SURFACTANT` role evidence.

## Recommended Edits

- Replace the `SURFACTANT` computational prediction with curated evidence, or
  remove `physicochemical_roles` until such support is added.
