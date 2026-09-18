# `data/ingredients/mapped/Proteose.yaml`

**Verdict**: pass.

**Identity**: `Proteose` is preserved as local `kgmicrobe.compound:proteose` after promotion from the MicrobeDecoder unresolved queue. A fresh exact OLS4 search for `Proteose` found `proteose peptone` and related peptone assay hits, but no exact standalone Proteose class that should replace the local fallback.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Proteose.yaml ...` passed for the 5-file batch with 0 ERROR rows. Engine A term validation is intentionally skipped because `kgmicrobe.compound` is a local non-OBO prefix.

**Evidence**: The #213 promotion kept the record in the fallback registry after an exact search across the repo's supported ontologies, and final SSSOM row 2430 publishes only `kgmicrobe.compound:proteose` with no noisy `other` tokens.

**Completeness**: The record has no active roles, components, CAS, or structure fields that could overstate the local placeholder identity.

**Recommended Edits**: None.
