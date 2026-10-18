# `data/ingredients/mapped/Vitamin_K.yaml`

## Verdict

Pass. The restored CultureMech residual grounding to the ChEBI vitamin K
label, aggregate row, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Vitamin_K.yaml`.
- Identifier and grounding: `identifier: CHEBI:28384` with matching
  `ontology_mapping.ontology_id`, label `vitamin K`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `match_level: EXACT`, and
  `mapping_status: MAPPED`.
- Occurrences: one CultureMech recipe occurrence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Virginiamycin` through `Vitamin_K`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on this 5-file CHEBI
  batch exited 0.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:28384` returns active label `vitamin K`,
  supporting the exact label match restored from the CultureMech occurrence
  table.
- The final SSSOM row correctly has
  `MIM:Vitamin_K skos:exactMatch CHEBI:28384` with
  `MIM:culturemech:output/ingredient_occurrences.tsv` provenance.

## Issues

None.

## Completeness

- The exact CHEBI mapping, occurrence count, aggregate copy, and final SSSOM row
  agree.

## Recommended Edits

None.
