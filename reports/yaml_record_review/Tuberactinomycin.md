# `data/ingredients/mapped/Tuberactinomycin.yaml`

## Verdict

Needs curation, major. The exact MeSH fallback identity, aggregate row, and
final SSSOM row pass, but `SELECTIVE_AGENT` is still a provisional
name-pattern prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Tuberactinomycin.yaml`.
- Identifier and grounding: `identifier: mesh:C015563` with matching
  `ontology_mapping.ontology_id`, label `tuberactinomycin`, source `MESH`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Synonyms: none.
- Occurrences: no CultureMech recipe occurrences.
- Roles: one `physicochemical_roles.SELECTIVE_AGENT` facet at confidence
  `0.8`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tuberactinomycin` through `Tween`: exited 0 and wrote zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- Engine A label validation was limited to the CHEBI records in this batch.
  The lower-case `mesh:C015563` CURIE is covered by the exact OLS search below
  and by the existing unknown-term triage row that classifies its stale final
  validation stamp as missing-prefix-validator coverage.

## Evidence

- Fresh exact OLS4 search for `Tuberactinomycin` returns active `mesh:C015563`
  as an exact label match. The import note's old low-confidence CHEBI hits are
  Tuberactinomycin O and enviomycin, not exact matches for this record.
- The final SSSOM row correctly has
  `MIM:Tuberactinomycin skos:exactMatch mesh:C015563` and no `other`
  synonyms.

## Issues

### Major: `SELECTIVE_AGENT` is provisional name-pattern evidence

The only role assertion is:

```yaml
physicochemical_roles:
- role: SELECTIVE_AGENT
  confidence: 0.8
  evidence:
  - reference_type: COMPUTATIONAL_PREDICTION
    reference_text: Inferred from curated media-role name pattern
    curator_note: Provisional role from a curated name-pattern rule; review recommended.
```

The MeSH fallback mapping does not independently curate the selective-agent
role.

## Completeness

- The MeSH fallback identity, aggregate copy, and final SSSOM row agree.
- The residual issue is limited to the unsupported role facet.

## Recommended Edits

- Replace the `SELECTIVE_AGENT` computational prediction with curated
  database/literature evidence, or remove `physicochemical_roles` until such
  support is added.
