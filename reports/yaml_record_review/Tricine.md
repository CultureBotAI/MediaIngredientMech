# `data/ingredients/mapped/Tricine.yaml`

## Verdict

Needs curation, major. The exact CHEBI identity, CAS RN, occurrence count,
aggregate row, and final SSSOM row pass, but `BUFFER` is still provisional
name-pattern evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/Tricine.yaml`.
- Identifier and grounding: `identifier: CHEBI:46760` with matching
  `ontology_mapping.ontology_id`, label `tricine`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `5704-04-1`.
- Synonyms: none.
- Occurrences: 44 recipe occurrences in 44 media.
- Roles: one `physicochemical_roles.BUFFER` facet at confidence `0.8`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tribenuron-methyl` through `Tricine`: exited 0 and wrote zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh exact OLS4 search for `tricine` returns `CHEBI:46760` with label
  `tricine`.
- Fresh PubChem lookup for CAS `5704-04-1` returns formula `C6H13NO5`,
  verifying the CAS identity.
- The final SSSOM row has `MIM:Tricine skos:exactMatch CHEBI:46760` and
  exports only `CAS:5704-04-1` in `other`.

## Issues

### Major: `BUFFER` is provisional name-pattern evidence

The only role assertion is:

```yaml
physicochemical_roles:
- role: BUFFER
  confidence: 0.8
  evidence:
  - reference_type: COMPUTATIONAL_PREDICTION
    reference_text: Inferred from curated media-role name pattern
    curator_note: Provisional role from a curated name-pattern rule; review recommended.
```

The exact CHEBI and CAS identity do not independently curate the buffer role.

## Completeness

- The CHEBI identity, CAS RN, occurrence count, aggregate copy, and final SSSOM
  row agree.
- The only issue is the provisional `BUFFER` role evidence.

## Recommended Edits

- Replace the `COMPUTATIONAL_PREDICTION` role evidence with curated
  database/literature evidence, or remove `physicochemical_roles` until such
  support is added.
