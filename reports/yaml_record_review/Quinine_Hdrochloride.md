# `data/ingredients/mapped/Quinine_Hdrochloride.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Quinine Hdrochloride` is a CAS-primary fallback for `cas:6119-47-7`. PubChem lookup by CAS confirms the stored CID `16211283`, formula, SMILES, and InChI for quinine hydrochloride dihydrate, and the final SSSOM row preserves `CAS:6119-47-7`.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Quinine_Hdrochloride.yaml ...` passed for the 5-file batch with 0 ERROR rows. Direct Engine A term validation was skipped for this CAS-only registry record because the term-validator's local OAK adapter cannot label `cas:6119-47-7`.

**Evidence**: The CAS exact row is the right registry fallback, but final SSSOM row 2478 emits `Quinine Hdrochloride` as both the subject label and CAS object label. That label misspells hydrochloride and hides the two waters represented in the stored PubChem formula/InChI.

**Completeness**: The record has no roles, components, or extra synonyms. The active issue is that the fallback registry label in YAML and final SSSOM does not reflect the exact CAS hydrate.

**Recommended Edits**: Correct `preferred_term`, `ontology_mapping.ontology_label`, and the filename/subject slug to a hydrate-preserving spelling such as `Quinine_Hydrochloride_Dihydrate`; keep `cas:6119-47-7` as the exact registry identifier unless a same-identity CHEBI term appears. Then regenerate final SSSOM and rerun the CAS registry row checks.
