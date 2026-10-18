# `data/ingredients/mapped/N-acetylgalactosamine.yaml`

## Verdict

Pass. The exact `CHEBI:28800` N-acetylgalactosamine identity, MicrobeDecoder
source provenance, review promotion, structural properties, and final exact row
pass.

## Identity

- Reviewed record: `data/ingredients/mapped/N-acetylgalactosamine.yaml`.
- Identifier and grounding: `identifier: CHEBI:28800` with
  `ontology_mapping.ontology_id: CHEBI:28800`, label
  `N-acetylgalactosamine`, source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: five MicrobeDecoder BacDive metabolite-utilization source
  occurrences and no CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `N-acetyl-lysine` through `N-acetylmuramic_Acid`: exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:28800` as active
  `N-acetylgalactosamine`, with formula `C8H15NO6` and no label drift.
- The MicrobeDecoder source row records
  `kgmicrobe.trait:n_acetylgalactosamine`, raw label
  `N-acetylgalactosamine`, source column `BacDive_Metabolite_utilization`, and
  count 5; `mappings/microbedecoder_auto_mapped_review.tsv` records the
  later `APPROVED` promotion.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:N-acetylgalactosamine` to `CHEBI:28800` with empty `other`.

## Completeness

- The active ChEBI target, MicrobeDecoder occurrence count, source provenance,
  review promotion, and final row agree.
- The record does not assert components, roles, or unsupported synonyms.

## Recommended Edits

- None.
