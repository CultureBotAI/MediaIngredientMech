# `data/ingredients/mapped/Tryptose.yaml`

## Verdict

Needs curation, major. The exact MICRO identity, catalog variant, occurrence
count, aggregate row, and final SSSOM row pass, but `PROTEIN_SOURCE` is still a
provisional name-pattern prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Tryptose.yaml`.
- Identifier and grounding: `identifier: MICRO:0000183` with matching
  `ontology_mapping.ontology_id`, label `tryptose`, source `MICRO`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Synonyms: the raw `Tryptose` label and one `Tryptose (BD-Difco)` catalog
  variant.
- Occurrences: 12 CultureMech recipe occurrences.
- Roles: one `nutritional_roles.PROTEIN_SOURCE` facet at confidence `0.8`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tryptoneyeastbeef_(tyb)` through `Tuberactinamine_A`: exited 0 and wrote
  zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- Engine A label validation was limited to the CHEBI records in this batch.
  `MICRO:0000183` is covered by the prefix-specific OLS lookup below and by the
  existing unknown-term triage row that classifies its stale final validation
  stamp as missing-prefix-validator coverage.

## Evidence

- Fresh OLS4 lookup for `MICRO:0000183` returns an active `tryptose` term.
  The term definition describes tryptose as a mixed enzymatic hydrolysate of
  protein for cultivating microorganisms, which agrees with keeping the record
  mapped to MICRO rather than forcing a single CHEBI compound.
- The final SSSOM row correctly has
  `MIM:Tryptose skos:exactMatch MICRO:0000183` and exports only
  `Tryptose (BD-Difco)` in `other`.
- The hidden/ignored-inclusive search across `mappings`, `data/curated`, and
  `reports` also found `Tryptose-phosphate` and `Tryptose-phosphate broth` as
  separate explicit unmapped records, so the MICRO tryptose row is not
  conflating those broader broth labels.

## Issues

### Major: `PROTEIN_SOURCE` is provisional name-pattern evidence

The only role assertion is:

```yaml
nutritional_roles:
- role: PROTEIN_SOURCE
  confidence: 0.8
  evidence:
  - reference_type: COMPUTATIONAL_PREDICTION
    reference_text: Inferred from curated media-role name pattern
    curator_note: Provisional role from a curated name-pattern rule; review recommended.
```

The exact MICRO identity does not independently curate the protein-source
role.

## Completeness

- The exact MICRO mapping, BD-Difco catalog alias, occurrence count, aggregate
  copy, and final SSSOM row agree.
- The remaining consequential gap is the unsupported role facet.

## Recommended Edits

- Replace the `PROTEIN_SOURCE` computational prediction with curated
  database/literature evidence, or remove `nutritional_roles` until such
  support is added.
