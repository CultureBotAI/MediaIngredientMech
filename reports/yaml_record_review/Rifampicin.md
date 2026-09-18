# `data/ingredients/mapped/Rifampicin.yaml`

**Verdict**: pass.

**Identity**: `Rifampicin` maps exactly to active, defining `CHEBI:28077` /
`rifampicin`. Fresh OLS4 lookup resolved the ChEBI term with CAS `13292-46-1`
and the same formula, SMILES, and InChI as the YAML; fresh PubChem lookup by the
stored CAS resolved CID 135398735 with the same formula and InChI.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Ribose.yaml data/ingredients/mapped/Rice_straw.yaml
data/ingredients/mapped/Rifabutin.yaml data/ingredients/mapped/Rifampicin.yaml
data/ingredients/mapped/Rifamycin.yaml` passed for the 5-file batch with 0 ERROR
rows. Direct `linkml-term-validator validate-data` with `--labels` passed for
the same 5 files.

**Evidence**: The per-record YAML agrees with the regenerated aggregate row
when keyed by `(identifier, preferred_term)`. Final SSSOM row 2514 maps exactly
to `CHEBI:28077`; the exported `other` field contains only ChEBI-backed
synonyms plus `CAS:13292-46-1`, and the raw `Role: Antimicrobial agent` synonym
is filtered out. The `SELECTIVE_AGENT` role is supported by the CultureMech
`DATABASE_ENTRY` evidence with original role text `Selective Agent`.

**Completeness**: The exact ChEBI identity, CAS, chemical properties, refreshed
3-occurrence count, CultureMech selective-agent role, and final SSSOM row agree.

**Recommended Edits**: None.
