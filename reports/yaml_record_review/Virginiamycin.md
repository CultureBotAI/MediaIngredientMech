# `data/ingredients/mapped/Virginiamycin.yaml`

## Verdict

Pass. The MicrobeDecoder exact CHEBI identity, aggregate row, and final SSSOM
row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Virginiamycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:87209` with matching
  `ontology_mapping.ontology_id`, label `virginiamycin`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Occurrences: one MicrobeDecoder antibiotic-resistance occurrence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Virginiamycin` through `Vitamin_K`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on this 5-file CHEBI
  batch exited 0.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:87209` returns active label `virginiamycin`,
  supporting the MicrobeDecoder exact label match to the ChEBI antibiotic
  mixture term.
- The final SSSOM row correctly has
  `MIM:Virginiamycin skos:exactMatch CHEBI:87209`, with review provenance and
  no unsupported labels in `other`.

## Issues

None.

## Completeness

- The exact CHEBI mapping, MicrobeDecoder occurrence count, aggregate copy, and
  final SSSOM row agree.

## Recommended Edits

None.
