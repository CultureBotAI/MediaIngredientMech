# `data/ingredients/mapped/Primocarcin.yaml`

**Verdict**: pass.

**Identity**: `Primocarcin` is intentionally retained as local `kgmicrobe.compound:primocarcin`. The record documents the placeholder origin and the 2026-05-10 review that kept the KG-Microbe primary because no exact external ontology term or normalized local duplicate supported promotion.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Primocarcin.yaml ...` passed for the 5-file batch with 0 ERROR rows. Engine A term validation is intentionally skipped for this record because `kgmicrobe.compound` is a local non-OBO prefix; the final SSSOM row-review triage classifies the row as a placeholder to keep pending curator promotion.

**Evidence**: Fresh exact OLS4 search across CHEBI and NCIT returned zero hits for `Primocarcin`, which agrees with the May placeholder review. Final SSSOM row 2420 preserves the exact local registry row and publishes no non-synonym `other` payload.

**Completeness**: The record has no active synonyms, roles, components, or structure fields. Its zero occurrence count is consistent with a KG-Microbe placeholder retained until an external ontology identifier appears.

**Recommended Edits**: None.
