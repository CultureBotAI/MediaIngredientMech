# `data/ingredients/mapped/Potassium_Hexahydroxoantimonate.yaml`

**Verdict**: pass.

**Identity**: `potassium hexahydroxoantimonate` is preserved as the CAS-registry identity `cas:12208-13-8`. PubChem CID 25524 confirms the stored formula, SMILES, InChI, and CAS synonym `12208-13-8`; final SSSOM row 2397 exports the same CAS in `other`.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Potassium_Hexahydroxoantimonate.yaml ...` passed for the 5-file batch with 0 ERROR rows. Engine A term validation was skipped intentionally because `cas` is a non-OBO registry prefix covered by product validation rather than `linkml-term-validator` OAK lookup.

**Evidence**: The CultureBotHT CAS fallback is consistent with the PubChem record for CID 25524, and the row-review manifest classifies the final CAS object as an expected registry identifier. The final SSSOM `CAS:12208-13-8` token is allowed because it matches `chemical_properties.cas_rn`. An ignored/hidden local search over `data/ingredients`, `data/curated`, `mappings`, `reports`, `scripts`, `src`, `tests`, `docs`, and `UNIFIED_INGREDIENT_MAPPING.tsv` found the expected curated, generated, row-review, and final SSSOM references.

**Completeness**: The CAS RN, PubChem CID, formula, SMILES, and InChI are present; no active roles, components, or unsupported synonyms are asserted.

**Recommended Edits**: None.
