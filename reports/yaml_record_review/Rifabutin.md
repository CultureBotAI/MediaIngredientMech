# `data/ingredients/mapped/Rifabutin.yaml`

**Verdict**: pass.

**Identity**: `Rifabutin` maps exactly to active, defining `CHEBI:45367` /
`rifabutin`. Fresh OLS4 lookup resolved the ChEBI term, listed Rifabutin as a
registered synonym, and matched the YAML formula, SMILES, and InChI.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Ribose.yaml data/ingredients/mapped/Rice_straw.yaml
data/ingredients/mapped/Rifabutin.yaml data/ingredients/mapped/Rifampicin.yaml
data/ingredients/mapped/Rifamycin.yaml` passed for the 5-file batch with 0 ERROR
rows. Direct `linkml-term-validator validate-data` with `--labels` passed for
the same 5 files.

**Evidence**: The per-record YAML agrees with the regenerated aggregate row
when keyed by `(identifier, preferred_term)`. Final SSSOM row 2513 maps exactly
to `CHEBI:45367` and exports an empty `other` field. The old MicrobeDecoder
`PENDING_REVIEW` hold was already promoted after canonical-label review, and no
unsupported role assertions remain.

**Completeness**: The MicrobeDecoder occurrence provenance, reviewed ChEBI
identity, ingredient type, ChEBI structure fields, and final SSSOM row agree.

**Recommended Edits**: None.
