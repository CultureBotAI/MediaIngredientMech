# `data/ingredients/mapped/Potassium_Polysulfide.yaml`

**Verdict**: pass.

**Identity**: `potassium (poly)sulfide` is a CAS-only exact fallback for `cas:37199-66-9`. PubChem resolves that CAS RN to CID 5362529 and lists `Potassium (Poly)Sulfide` as a synonym, while fresh OLS4 CHEBI searches for the exact label and CAS returned zero hits.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Potassium_Polysulfide.yaml ...` passed for the 5-file batch with 0 ERROR rows. Engine A term validation is intentionally skipped for this record because `cas` is a non-OBO registry prefix; the final SSSOM row-review triage classifies `cas:37199-66-9` as an expected registry identifier.

**Evidence**: The YAML exact identity and final SSSOM row 2406 agree on `cas:37199-66-9`, and the final `CAS:37199-66-9` token is allowed because it matches `chemical_properties.cas_rn`. The record has no active synonyms, roles, components, or structure fields that could overstate the CAS fallback.

**Completeness**: The zero occurrence counts, empty role slots, and absent structure fields are acceptable for a registry fallback with no current exact CHEBI replacement. No local component or final synonym surface needs a repair.

**Recommended Edits**: None.
