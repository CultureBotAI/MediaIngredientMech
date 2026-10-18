# `data/ingredients/mapped/Milk.yaml`

## Verdict

Pass. The exact `UBERON:0001913` milk identity, metatraits provenance,
undefined-mixture type, occurrence count, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Milk.yaml`.
- Identifier and grounding: `identifier: UBERON:0001913` with
  `ontology_mapping.ontology_id: UBERON:0001913`, label `milk`, source
  `UBERON`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- Occurrences: three CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Midecamycin` through `Mineral_3B_Solution_Minus_Nitrogen`: exited 0 and
  wrote zero ERROR rows.
- Direct CHEBI-focused LinkML term validation was skipped for this UBERON
  record in the mixed batch.

## Evidence

- `mappings/ingredient_mappings_oak_ols_review.tsv` and
  `mappings/ingredient_mappings_row_review_manifest.tsv` confirm `MIM:Milk` to
  `UBERON:0001913`.
- A fresh UBERON-scoped EBI OLS4 lookup resolves `UBERON:0001913` as active
  `milk`.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Milk` to
  `UBERON:0001913` with empty `other`.

## Completeness

- The UBERON bodily-product target, metatraits source, undefined-mixture type,
  3/3 occurrence count, and final row agree.
- The record does not publish raw synonyms or unsupported roles.

## Recommended Edits

- None.
