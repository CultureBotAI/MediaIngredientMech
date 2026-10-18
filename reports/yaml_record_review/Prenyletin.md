# `data/ingredients/mapped/Prenyletin.yaml`

**Verdict**: pass.

**Identity**: `Prenyletin` is preserved as CAS `15870-91-4`. PubChem resolves the CAS RN to CID 3873459 and lists `PRENYLETIN` as a synonym; fresh OLS4 CHEBI searches found no exact `Prenyletin` or CAS hit to promote over the fallback.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Prenyletin.yaml ...` passed for the 5-file batch with 0 ERROR rows. Engine A term validation is intentionally skipped for this record because `cas` is a non-OBO registry prefix; the final SSSOM row-review triage classifies `cas:15870-91-4` as an expected registry identifier.

**Evidence**: The YAML identifier, `chemical_properties.cas_rn`, and final SSSOM row 2416 agree on CAS `15870-91-4`, and the final `CAS:15870-91-4` token is allowed because it matches the structured CAS field.

**Completeness**: The CAS fallback has no active synonyms, roles, components, or structure fields to overstate. The absent occurrence count is consistent with its imported CultureBotHT fallback shape.

**Recommended Edits**: None.
