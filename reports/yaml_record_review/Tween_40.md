# `data/ingredients/mapped/Tween_40.yaml`

## Verdict

Needs curation, major. The CHEBI polysorbate 40 identity, structure fields,
synonyms, occurrence count, aggregate row, and final SSSOM row pass, but
`SURFACTANT` is still a provisional in-session LLM role.

## Identity

- Reviewed record: `data/ingredients/mapped/Tween_40.yaml`.
- Identifier and grounding: `identifier: CHEBI:53423` with matching
  `ontology_mapping.ontology_id`, label `polysorbate 40`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Synonyms: polysorbate 40 and polyoxyethylene sorbitan monopalmitate labels.
- Occurrences: 6 CultureMech recipe occurrences.
- Roles: one `physicochemical_roles.SURFACTANT` facet at confidence `0.6`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tween_20` through `Tyloxapol`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on this file with
  `--labels`: passed.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:53423` returns active label `polysorbate 40`,
  formula `(C2H4O)w.(C2H4O)x.(C2H4O)y.(C2H4O)z.C22H42O6`, the same InChI and
  SMILES as the YAML, and both `Tween 40` and the exported SSSOM `other` label
  as CHEBI synonyms.
- The final SSSOM row correctly has
  `MIM:Tween_40 skos:exactMatch CHEBI:53423` and exports only
  `Polyoxyethylene (20) sorbitan monopalmitate` in `other`.

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

The exact CHEBI identity does not independently curate the surfactant role.

### Minor: `mapping_quality` overstates the lexical match

`Tween 40` is a CHEBI synonym of canonical `polysorbate 40`, not the canonical
label itself. This mirrors the already-fixed Tween 20 and Tween 60 records and
should be `SYNONYM_MATCH`; the final SSSOM predicate remains `skos:exactMatch`
either way.

## Completeness

- The CHEBI identity, structure fields, synonyms, occurrence count, aggregate
  copy, and final SSSOM row agree.
- The residual material gap is the unsupported role facet.

## Recommended Edits

- Replace the `SURFACTANT` computational prediction with curated
  database/literature evidence, or remove `physicochemical_roles` until such
  support is added.
- Regrade `ontology_mapping.mapping_quality` from `EXACT_MATCH` to
  `SYNONYM_MATCH` so it records that the source label matched a CHEBI synonym.
