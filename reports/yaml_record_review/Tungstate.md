# `data/ingredients/mapped/Tungstate.yaml`

## Verdict

Needs curation, major. The exact CHEBI identity, CAS RN, structure fields,
CHEBI synonyms, aggregate row, and final SSSOM row pass, but `TRACE_ELEMENT` is
still a provisional in-session LLM role.

## Identity

- Reviewed record: `data/ingredients/mapped/Tungstate.yaml`.
- Identifier and grounding: `identifier: CHEBI:46502` with matching
  `ontology_mapping.ontology_id`, label `tungstate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `14311-52-5`.
- Synonyms: exact CHEBI/kg-microbe synonyms for tungstate.
- Occurrences: 3 CultureMech recipe occurrences.
- Roles: one `nutritional_roles.TRACE_ELEMENT` facet at confidence `0.6`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tuberactinomycin` through `Tween`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on this file with
  `--labels`: passed.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:46502` returns active label `tungstate`, CAS
  xref `14311-52-5`, formula `O4W`, the same InChI and SMILES as the YAML, and
  the exported SSSOM `other` labels as CHEBI synonyms.
- The final SSSOM row correctly has
  `MIM:Tungstate skos:exactMatch CHEBI:46502`, with only curated synonyms and
  `CAS:14311-52-5` in `other`.

## Issues

### Major: `TRACE_ELEMENT` is provisional in-session LLM evidence

The only role assertion is:

```yaml
nutritional_roles:
- role: TRACE_ELEMENT
  confidence: 0.6
  evidence:
  - reference_type: COMPUTATIONAL_PREDICTION
    reference_text: Assigned by in-session Claude reasoning (no external API)
    curator_note: Provisional in-session LLM role assignment; review recommended.
```

The exact CHEBI identity does not independently curate the trace-element role.

## Completeness

- The CHEBI identity, CAS RN, structure fields, CHEBI synonyms, aggregate copy,
  and final SSSOM row agree.
- The residual issue is limited to the unsupported role facet.

## Recommended Edits

- Replace the `TRACE_ELEMENT` computational prediction with curated
  database/literature evidence for tungstate in this ingredient context, or
  remove `nutritional_roles` until such support is added.
