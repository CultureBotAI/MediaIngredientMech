# `data/ingredients/mapped/Lysostaphin.yaml`

## Verdict

Pass. The MicrobeDecoder import now maps exactly to active NCIT:C166895 by a
final curator ruling, and the final SSSOM row is internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Lysostaphin.yaml`.
- Identifier and grounding: `identifier: NCIT:C166895` with
  `ontology_mapping.ontology_id: NCIT:C166895`, label `Lysostaphin`, source
  `NCIT`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: none asserted.
- Occurrences: four MicrobeDecoder source occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Lydimycin` through `Lysozyme`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for all five
  records in the batch.

## Evidence

- EBI OLS4 resolves `NCIT:C166895` as active `Lysostaphin` and lists CAS RN
  `9011-93-2`.
- The record keeps the 2026-08-07 curator ruling that `NCIT:C166895` is the
  final exact grounding and that `CHEBI:753395` must not be restored without a
  new curator decision.
- The final SSSOM publishes one `skos:exactMatch` row to `NCIT:C166895`; its
  `other` field is empty.

## Completeness

- The active NCIT identity, MicrobeDecoder source occurrence count, aggregate
  copy, and final SSSOM row are present and consistent.
- No nutritional, physicochemical, cellular, or environmental role is asserted.

## Recommended Edits

- None.
