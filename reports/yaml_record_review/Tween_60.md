# `data/ingredients/mapped/Tween_60.yaml`

## Verdict

Needs curation, major. The synonym match to polysorbate 60, polymer structure
fields, synonyms, aggregate row, and final SSSOM row pass, but `SURFACTANT` is
still a provisional in-session LLM role.

## Identity

- Reviewed record: `data/ingredients/mapped/Tween_60.yaml`.
- Identifier and grounding: `identifier: CHEBI:53425` with matching
  `ontology_mapping.ontology_id`, label `polysorbate 60`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Synonyms: raw CultureMech property strings plus PEG-60/polyoxyethylene
  sorbitan stearate labels.
- Occurrences: 5 CultureMech recipe occurrences.
- Roles: one `physicochemical_roles.SURFACTANT` facet at confidence `0.6`.
- KG-Microbe node: `CHEBI:53425`, matching the identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tween_20` through `Tyloxapol`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on this file with
  `--labels`: passed.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:53425` returns active label `polysorbate 60`,
  formula `(C2H4O)w.(C2H4O)x.(C2H4O)y.(C2H4O)z.C24H46O6`, the same InChI and
  SMILES as the YAML, and the exported SSSOM `other` labels as CHEBI synonyms.
- The final SSSOM row correctly has
  `MIM:Tween_60 skos:exactMatch CHEBI:53425` and exports only
  polysorbate-60 synonyms in `other`.

## Issues

### Major: `SURFACTANT` is provisional in-session LLM evidence

The only role assertion is:

```yaml
physicochemical_roles:
- role: SURFACTANT
  confidence: 0.6
  evidence:
  - reference_type: COMPUTATIONAL_PREDICTION
    reference_text: Assigned by in-session Claude reasoning (no external API)
    curator_note: Provisional in-session LLM role assignment; review recommended.
```

The CHEBI synonym match does not independently curate the surfactant role.

## Completeness

- The CHEBI identity, polymer structure fields, synonyms, KG-Microbe node,
  aggregate copy, and final SSSOM row agree.
- Raw `Properties:` CultureMech strings are kept out of final SSSOM `other`.
- The residual material gap is the unsupported role facet.

## Recommended Edits

- Replace the `SURFACTANT` computational prediction with curated
  database/literature evidence, or remove `physicochemical_roles` until such
  support is added.
