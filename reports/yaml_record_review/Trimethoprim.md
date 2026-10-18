# `data/ingredients/mapped/Trimethoprim.yaml`

## Verdict

Needs curation, major. The exact CHEBI identity, CAS RN, structure fields,
occurrence count, aggregate row, and own SSSOM row pass, but a
vendor-qualified label leaks into final SSSOM `other` and `SELECTIVE_AGENT` is
still provisional name-pattern evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/Trimethoprim.yaml`.
- Identifier and grounding: `identifier: CHEBI:45924` with matching
  `ontology_mapping.ontology_id`, label `trimethoprim`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `738-70-5`.
- Synonyms: one exact ChEBI synonym plus one raw CultureMech
  vendor-qualified label.
- Occurrences: 1 CultureMech recipe occurrence in 1 medium.
- Roles: one `physicochemical_roles.SELECTIVE_AGENT` facet at confidence
  `0.8`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Triethanolamine` through `Trimethylamine-N-oxide`: exited 0 and wrote zero
  ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh exact OLS4 search for `trimethoprim` returns `CHEBI:45924` with label
  `trimethoprim` and the exported
  `5-(3,4,5-trimethoxybenzyl)pyrimidine-2,4-diamine` synonym.
- The final SSSOM row has `MIM:Trimethoprim skos:exactMatch CHEBI:45924` and
  exports `5-(3,4,5-trimethoxybenzyl)pyrimidine-2,4-diamine`,
  `trimethoprim (GlaxoSmithKline)`, and `CAS:738-70-5` in `other`.

## Issues

### Major: final `other` exports a vendor-qualified label

`trimethoprim (GlaxoSmithKline)` is a recipe/source surface carrying supplier
context, not an exact synonym for the pure `CHEBI:45924` molecule. It should
remain traceable as a CultureMech occurrence label without being published in
the final SSSOM synonym surface.

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

The exact CHEBI and CAS identity do not independently curate the selective
agent role.

## Completeness

- The CHEBI identity, CAS RN, structure fields, occurrence count, aggregate
  copy, and own SSSOM row agree.
- Residual curation is needed for the exported vendor label and provisional
  role.

## Recommended Edits

- Mark `trimethoprim (GlaxoSmithKline)` as non-exportable raw source text so
  the final SSSOM row keeps only true synonyms.
- Replace the `SELECTIVE_AGENT` computational prediction with curated
  database/literature evidence, or remove `physicochemical_roles` until such
  support is added.
