# `data/ingredients/mapped/Sodium_Isethionate.yaml`

**Verdict**: pass.

**Identity**: `sodium isethionate` maps to the CAS fallback `cas:1562-00-1`.
Fresh PubChem lookup resolves CAS RN `1562-00-1` to CID `517063`, formula
`C2H5NaO4S`, SMILES `C(CS(=O)(=O)[O-])O.[Na+]`, and the sodium
2-hydroxyethanesulfonate IUPAC label. A fresh exact OLS4 search found no ChEBI
term for `sodium isethionate`, so the CAS registry identifier remains the
appropriate primary grounding.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sodium_Iodate.yaml
data/ingredients/mapped/Sodium_Iodide.yaml
data/ingredients/mapped/Sodium_Iodoacetate.yaml
data/ingredients/mapped/Sodium_Isethionate.yaml
data/ingredients/mapped/Sodium_L-glutamate.yaml` passed for the 5-file batch
with 0 ERROR rows. Engine A term validation is intentionally skipped for this
record because `cas:` is a registry prefix, not an OBO ontology prefix.

**Evidence**: The CAS fallback identity and final SSSOM row pass. Row 2651
maps `MIM:Sodium_Isethionate` to the same `cas:1562-00-1` object and exports
only `CAS:1562-00-1` in `other`. The per-record YAML agrees with the
regenerated aggregate row when keyed by identifier and preferred term.

**Completeness**: The record has no roles or local synonyms needing evidence
review, and no unsafe synonyms are exported to final SSSOM.

**Recommended Edits**: None.
