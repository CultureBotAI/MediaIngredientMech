# `data/ingredients/mapped/Macrolide_Antibiotic.yaml`

## Verdict

Pass. The MicrobeDecoder exact CHEBI:25105 identity, source occurrence count,
aggregate copy, and final SSSOM row are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Macrolide_Antibiotic.yaml`.
- Identifier and grounding: `identifier: CHEBI:25105` with
  `ontology_mapping.ontology_id: CHEBI:25105`, label `macrolide antibiotic`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, and `mapping_status:
  MAPPED`.
- Occurrences: four MicrobeDecoder source occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Macro_Component_2_For_J_Medium` through `Magnesium`: exited 0 and wrote zero
  ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for the
  CHEBI-primary subset `Macrolide_Antibiotic`, `Magainin_I`, `Magnesium(2)`,
  and `Magnesium`; `Macro_Component_2_For_J_Medium` was skipped because its
  primary identifier uses a local prefix outside the CHEBI/OBO term adapter
  scope.

## Evidence

- EBI OLS4 resolves `CHEBI:25105` as active `macrolide antibiotic`.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:25105`; its
  `other` field is empty.

## Completeness

- The active CHEBI identity, MicrobeDecoder source occurrence count, aggregate
  copy, and final SSSOM row are present and consistent.
- No unsupported role or synonym is asserted.

## Recommended Edits

- None.
