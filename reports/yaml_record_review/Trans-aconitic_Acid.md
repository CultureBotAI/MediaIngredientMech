# `data/ingredients/mapped/Trans-aconitic_Acid.yaml`

## Verdict

Needs curation, major. The exact CHEBI identity, exact synonym, CAS RN,
PubChem structure, aggregate row, and final SSSOM row pass, but
`CARBON_SOURCE` is still provisional name-pattern evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/Trans-aconitic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:32806` with matching
  `ontology_mapping.ontology_id`, label `trans-aconitic acid`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `4023-65-8`.
- Synonyms: exact ChEBI synonym
  `(1E)-prop-1-ene-1,2,3-tricarboxylic acid`.
- Roles: one `nutritional_roles.CARBON_SOURCE` facet at confidence `0.8`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Trace_Mineral_Solution` through `Trans-aconitic_Acid`: exited 0 and wrote
  zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh exact OLS4 search for `trans-aconitic acid` returns `CHEBI:32806` with
  label `trans-aconitic acid`.
- Fresh PubChem lookup for CAS `4023-65-8` returns formula `C6H6O6` and the
  same E isomer InChI as the YAML.
- The final SSSOM row has
  `MIM:Trans-aconitic_Acid skos:exactMatch CHEBI:32806` and exports only the
  exact synonym plus `CAS:4023-65-8` in `other`.

## Issues

### Major: `CARBON_SOURCE` is provisional name-pattern evidence

The only role assertion comes from `infer_roles_from_name_lists`:

```yaml
nutritional_roles:
- role: CARBON_SOURCE
  confidence: 0.8
  evidence:
  - reference_type: COMPUTATIONAL_PREDICTION
    reference_text: Inferred from curated media-role name pattern
    curator_note: Provisional role from a curated name-pattern rule; review recommended.
```

The exact CHEBI and CAS identity do not establish that this ingredient is used
as a curated carbon source.

## Completeness

- The CHEBI identity, CAS RN, structure fields, exact synonym, aggregate copy,
  and final SSSOM row agree.
- The only residual problem is the provisional `CARBON_SOURCE` role evidence.

## Recommended Edits

- Replace the `COMPUTATIONAL_PREDICTION` role evidence with curated
  database/literature evidence, or remove `nutritional_roles` until such
  support is added.
