# `data/ingredients/mapped/Zinc_Acetate.yaml`

## Verdict

Needs curation, minor. The CultureMech residual label maps exactly to active
`CHEBI:62984` zinc acetate and the final SSSOM row has restored CultureMech
provenance, but this late residual record still lacks
`ingredient_type: SINGLE_INGREDIENT` and ChEBI-derived structure fields.

## Identity

- Reviewed record: `data/ingredients/mapped/Zinc_Acetate.yaml`.
- Identifier and grounding: `identifier: CHEBI:62984` with matching
  `ontology_mapping.ontology_id`, canonical label `zinc acetate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `match_level: EXACT`, and
  `mapping_status: MAPPED`.
- Occurrences: seven CultureMech occurrences across seven media.
- No synonyms, roles, components, environmental contexts, or discussion
  entries are asserted.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on this 5-file batch:
  exited 0 and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data` passed for this CHEBI-primary
  record with `--labels`.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- Fresh OLS4 exact search for `zinc acetate` in CHEBI returned the active
  `CHEBI:62984` label `zinc acetate`.

## Evidence

- The record's structured evidence cites the CultureMech occurrence table exact
  label match.
- The final SSSOM correctly exports
  `MIM:Zinc_Acetate skos:exactMatch CHEBI:62984`, with restored
  `MIM:culturemech:output/ingredient_occurrences.tsv` source provenance.
- The final SSSOM `other` field is empty.
- Minor: this exact CHEBI chemical is missing
  `ingredient_type: SINGLE_INGREDIENT`.
- Minor: ChEBI structure fields have not been copied into
  `chemical_properties`.

## Completeness

- The exact CHEBI identity, CultureMech occurrence evidence, occurrence count,
  aggregate copy, and empty final SSSOM synonym payload are populated.
- The missing single-ingredient type and structure fields are the only
  consequential field gaps.

## Recommended Edits

- Add `ingredient_type: SINGLE_INGREDIENT`.
- Backfill `chemical_properties` from `CHEBI:62984`.
- Sync `data/curated/mapped_ingredients.yaml`, rebuild SSSOM, and rerun strict
  validation plus SSSOM invariant validation.
