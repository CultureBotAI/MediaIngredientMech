# `data/ingredients/mapped/Trimethylamine.yaml`

## Verdict

Needs curation, major. The exact CHEBI identity, CAS RN, kg-microbe synonyms,
occurrence count, aggregate row, and final SSSOM row pass, but
`CARBON_SOURCE` is still provisional in-session LLM evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/Trimethylamine.yaml`.
- Identifier and grounding: `identifier: CHEBI:18139` with matching
  `ontology_mapping.ontology_id`, label `trimethylamine`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `75-50-3`.
- Synonyms: seven kg-microbe exact synonyms.
- Occurrences: 4 CultureMech recipe occurrences in 4 media.
- Roles: one `nutritional_roles.CARBON_SOURCE` facet at confidence `0.6`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Trimethylamine-hcl` through `Tris_Acetate_Stock_Solution`: exited 0 and
  wrote zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 term lookup for `CHEBI:18139` returns `trimethylamine`, CAS xref
  `cas:75-50-3`, formula `C3H9N`, the same InChI and SMILES as the YAML, and
  all seven exported kg-microbe synonyms.
- The final SSSOM row has `MIM:Trimethylamine skos:exactMatch CHEBI:18139` and
  exports only the kg-microbe synonyms plus `CAS:75-50-3` in `other`.

## Issues

### Major: `CARBON_SOURCE` is provisional in-session LLM evidence

The only role assertion is:

```yaml
nutritional_roles:
- role: CARBON_SOURCE
  confidence: 0.6
  evidence:
  - reference_type: COMPUTATIONAL_PREDICTION
    reference_text: Assigned by in-session Claude reasoning (no external API)
    curator_note: Provisional in-session LLM role assignment; review recommended.
```

The exact CHEBI and CAS identity do not independently curate the carbon-source
role.

## Completeness

- The CHEBI identity, CAS RN, structure fields, occurrence count, aggregate
  copy, and final SSSOM row agree.
- The only residual issue is the provisional `CARBON_SOURCE` role evidence.

## Recommended Edits

- Replace the `CARBON_SOURCE` computational prediction with curated
  database/literature evidence, or remove `nutritional_roles` until such
  support is added.
