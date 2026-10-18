# `data/ingredients/mapped/Porcine_Serum.yaml`

**Verdict**: pass.

**Identity**: `Porcine serum` maps exactly to `MICRO:0001238` / `porcine serum` and is classified as an `UNDEFINED_MIXTURE`. The MICRO identity, normalized source label, refreshed occurrence count, and final SSSOM row 2374 agree.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Porcine_Serum.yaml ...` passed for the 5-file batch with 0 ERROR rows. Direct `linkml-term-validator` label validation was unavailable because the local `sqlite:obo:micro` adapter is an empty sqlite database with no `rdfs_label_statement` table; a prefix-specific live OLS lookup resolved `MICRO:0001238` to `porcine serum`.

**Evidence**: The `resolve_unmapped` history and ontology evidence record the exact MICRO label match for the old unmapped queue entry. The row-review manifest classifies the older `UNKNOWN_TERM` stamp as missing-prefix validator coverage, not a mapping defect. Final SSSOM row 2374 has no `other` synonyms. An ignored/hidden local search over `data/ingredients`, `data/curated`, `mappings`, `reports`, `scripts`, `src`, `tests`, `docs`, and `UNIFIED_INGREDIENT_MAPPING.tsv` found the expected curated, generated, row-review, and final SSSOM references.

**Completeness**: The serum mixture has occurrence statistics and the exact MICRO term; no component decomposition or chemical properties are expected.

**Recommended Edits**: None.
