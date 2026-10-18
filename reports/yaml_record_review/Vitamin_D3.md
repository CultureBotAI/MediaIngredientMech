# `data/ingredients/mapped/Vitamin_D3.yaml`

## Verdict

Pass. The restored CultureMech residual grounding to the ChEBI vitamin D3
synonym, aggregate row, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Vitamin_D3.yaml`.
- Identifier and grounding: `identifier: CHEBI:28940` with matching
  `ontology_mapping.ontology_id`, label `calciol`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `match_level: NORMALIZED`, and
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

- Fresh OLS4 lookup for `CHEBI:28940` returns active label `calciol` and lists
  `Vitamin D3` / `vitamin D3` as synonyms, supporting the normalized synonym
  match restored from the CultureMech occurrence table.
- The final SSSOM row correctly has
  `MIM:Vitamin_D3 skos:exactMatch CHEBI:28940` with
  `MIM:culturemech:output/ingredient_occurrences.tsv` provenance.

## Issues

None.

## Completeness

- The ChEBI synonym match, occurrence count, aggregate copy, and final SSSOM row
  agree.

## Recommended Edits

None.
