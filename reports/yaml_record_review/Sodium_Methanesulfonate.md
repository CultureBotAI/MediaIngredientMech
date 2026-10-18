# `data/ingredients/mapped/Sodium_Methanesulfonate.yaml`

**Verdict**: pass.

**Identity**: `Sodium methanesulfonate` maps to the CAS fallback
`cas:2386-57-4`. Fresh PubChem lookup resolves CAS RN `2386-57-4` to CID
`638112` with formula `CH3NaO3S`, SMILES `CS(=O)(=O)[O-].[Na+]`, the same
InChI and PubChem CID stored in YAML, and the sodium methanesulfonate IUPAC
label.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sodium_Malonate.yaml
data/ingredients/mapped/Sodium_Metasilicate.yaml
data/ingredients/mapped/Sodium_Metasilicate_Silicate_For_Diatom_Frustules.yaml
data/ingredients/mapped/Sodium_Methanesulfonate.yaml
data/ingredients/mapped/Sodium_Nitrate_070_M_Stock.yaml` passed for the
5-file batch with 0 ERROR rows. Engine A term validation is intentionally
skipped for this record because `cas:` is a registry prefix, not an OBO
ontology prefix.

**Evidence**: The CAS fallback identity, PubChem CID, formula, InChI, and
SMILES pass. Final SSSOM row 2659 maps `MIM:Sodium_Methanesulfonate` to the
same `cas:2386-57-4` object and exports only `CAS:2386-57-4` in `other`. The
per-record YAML agrees with the regenerated aggregate row when keyed by
identifier and preferred term.

**Completeness**: The record has no roles or local synonyms needing evidence
review, and no unsafe synonyms are exported to final SSSOM.

**Recommended Edits**: None.
