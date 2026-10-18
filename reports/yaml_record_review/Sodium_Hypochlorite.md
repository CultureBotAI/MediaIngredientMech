# `data/ingredients/mapped/Sodium_Hypochlorite.yaml`

**Verdict**: pass.

**Identity**: `Sodium hypochlorite` maps exactly to active, defining
`CHEBI:32146` / `sodium hypochlorite`. Fresh OLS4 lookup confirmed the ChEBI
label, CAS RN `7681-52-9`, formula `ClO.Na`, InChI, InChIKey, SMILES, and
same-substance synonyms. PubChem resolves the CAS RN to CID `23665760` with
the same formula, InChI, InChIKey, and structure.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sodium_Fluorophosphate.yaml
data/ingredients/mapped/Sodium_Gluconate.yaml
data/ingredients/mapped/Sodium_Glutamate_Monohydrate.yaml
data/ingredients/mapped/Sodium_Hypochlorite.yaml
data/ingredients/mapped/Sodium_Hypophosphite_Monohydrate.yaml` passed for the
5-file batch with 0 ERROR rows. Direct `linkml-term-validator validate-data`
with `--labels` passed.

**Evidence**: The exact CHEBI identity, CAS RN, formula, InChI, and SMILES
pass. Final SSSOM row 2645 exports only `CAS:7681-52-9` in `other`, matching
the local CAS RN and ChEBI xref. The per-record YAML agrees with the
regenerated aggregate row when keyed by identifier and preferred term.

**Completeness**: The record has no roles or local synonyms needing evidence
review, and no unsafe synonyms are exported to final SSSOM.

**Recommended Edits**: None.
