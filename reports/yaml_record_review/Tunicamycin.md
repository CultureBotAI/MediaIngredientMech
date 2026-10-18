# `data/ingredients/mapped/Tunicamycin.yaml`

## Verdict

Needs curation, major. The exact CHEBI identity, CAS RN, variable-homologue
structure, aggregate row, and final SSSOM row pass, but `SELECTIVE_AGENT` is
still a provisional name-pattern prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Tunicamycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:29699` with matching
  `ontology_mapping.ontology_id`, label `tunicamycin`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `11089-65-9`.
- Synonyms: none.
- Occurrences: no CultureMech recipe occurrences.
- Roles: one `physicochemical_roles.SELECTIVE_AGENT` facet at confidence
  `0.8`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tuberactinomycin` through `Tween`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on this file with
  `--labels`: passed.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:29699` returns active label `tunicamycin`, CAS
  xref `11089-65-9`, formula `C25H38N4O16`, and the same wildcard SMILES as the
  YAML, matching the modeled mixture of homologues.
- The final SSSOM row correctly has
  `MIM:Tunicamycin skos:exactMatch CHEBI:29699` and exports only
  `CAS:11089-65-9` in `other`.

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

The exact CHEBI identity does not independently curate the selective-agent
role.

## Completeness

- The CHEBI identity, CAS RN, wildcard structure, aggregate copy, and final
  SSSOM row agree.
- The residual issue is limited to the unsupported role facet.

## Recommended Edits

- Replace the `SELECTIVE_AGENT` computational prediction with curated
  database/literature evidence, or remove `physicochemical_roles` until such
  support is added.
