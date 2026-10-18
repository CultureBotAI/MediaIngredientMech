# `data/ingredients/mapped/Tyloxapol.yaml`

## Verdict

Needs curation, major. The exact CHEBI identity, CAS RN, polymer structure,
aggregate row, and final SSSOM row pass, but `SURFACTANT` is still a
provisional in-session LLM role.

## Identity

- Reviewed record: `data/ingredients/mapped/Tyloxapol.yaml`.
- Identifier and grounding: `identifier: CHEBI:141517` with matching
  `ontology_mapping.ontology_id`, label `tyloxapol`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `25301-02-4`.
- Synonyms: none.
- Occurrences: 2 CultureBotHT media occurrences.
- Roles: one `physicochemical_roles.SURFACTANT` facet at confidence `0.6`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tween_20` through `Tyloxapol`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on this file with
  `--labels`: passed.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:141517` returns active label `tyloxapol`, CAS
  xref `25301-02-4`, formula `(C17H26O2)m.2(C2H4O)n.C29H44O2`, and the same
  InChI and SMILES as the YAML.
- The final SSSOM row correctly has
  `MIM:Tyloxapol skos:exactMatch CHEBI:141517` and exports only
  `CAS:25301-02-4` in `other`.

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

The exact CHEBI identity does not independently curate the surfactant role or
put evidence on that facet.

## Completeness

- The CHEBI identity, CAS RN, polymer structure fields, aggregate copy, and
  final SSSOM row agree.
- The residual material gap is the unsupported role facet.

## Recommended Edits

- Replace the `SURFACTANT` computational prediction with curated
  database/literature evidence, or remove `physicochemical_roles` until such
  support is added.
