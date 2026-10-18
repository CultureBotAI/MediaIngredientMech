# `data/ingredients/mapped/Potassium_4-aminobenzoate.yaml`

**Verdict**: pass.

**Identity**: `Potassium 4-aminobenzoate` is preserved as the CAS-registry identity `cas:138-84-1`. PubChem CID 23663628 confirms the stored formula `C7H6KNO2`, SMILES `C1=CC(=CC=C1C(=O)[O-])N.[K+]`, InChI, and CAS synonym `138-84-1`; final SSSOM row 2383 exports the same CAS in `other`.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Potassium_4-aminobenzoate.yaml ...` passed for the 5-file batch with 0 ERROR rows. Engine A term validation was skipped intentionally because `cas` is a non-OBO registry prefix covered by product validation rather than `linkml-term-validator` OAK lookup.

**Evidence**: Fresh exact CHEBI OLS lookup found no `Potassium 4-aminobenzoate` document, consistent with the CAS fallback decision. The row-review manifest classifies the final CAS object as an expected registry identifier. The final SSSOM `CAS:138-84-1` token is allowed because it matches `chemical_properties.cas_rn`. An ignored/hidden local search over `data/ingredients`, `data/curated`, `mappings`, `reports`, `scripts`, `src`, `tests`, `docs`, and `UNIFIED_INGREDIENT_MAPPING.tsv` found the expected curated, generated, row-review, and final SSSOM references.

**Completeness**: The CAS RN, PubChem CID, formula, SMILES, and InChI are present; no roles, components, or unsupported synonyms are asserted.

**Recommended Edits**: None.
