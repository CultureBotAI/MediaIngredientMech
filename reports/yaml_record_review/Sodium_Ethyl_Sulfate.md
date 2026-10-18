# `data/ingredients/mapped/Sodium_Ethyl_Sulfate.yaml`

**Verdict**: pass.

**Identity**: `Sodium ethyl sulfate` maps to the CAS fallback
`cas:546-74-7`. Fresh PubChem lookup resolves CAS RN `546-74-7` to CID
`23680278` with formula `C2H5NaO4S`, SMILES `CCOS(=O)(=O)[O-].[Na+]`, and the
same InChI as the YAML. A fresh exact OLS4 search found no ChEBI term for
`sodium ethyl sulfate`, so the CAS registry identifier remains the appropriate
primary grounding.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sodium_Dodecyl_Sulfate.yaml
data/ingredients/mapped/Sodium_Ethyl_Sulfate.yaml
data/ingredients/mapped/Sodium_Ferric_EDTA.yaml
data/ingredients/mapped/Sodium_Ferulate.yaml
data/ingredients/mapped/Sodium_Fluoroacetate.yaml` passed for the 5-file batch
with 0 ERROR rows. Engine A term validation is intentionally skipped for this
record because `cas:` is a registry prefix, not an OBO ontology prefix.

**Evidence**: The CAS fallback identity, PubChem CID, formula, InChI, and
SMILES pass. Final SSSOM row 2638 maps `MIM:Sodium_Ethyl_Sulfate` to the same
`cas:546-74-7` object and exports only `CAS:546-74-7` in `other`. The
per-record YAML agrees with the regenerated aggregate row when keyed by
identifier and preferred term.

**Completeness**: The record has no roles or local synonyms needing evidence
review, and no unsafe synonyms are exported to final SSSOM.

**Recommended Edits**: None.
