# `data/ingredients/mapped/Ristocetin_A.yaml`

**Verdict**: pass.

**Identity**: `Ristocetin A` maps exactly to active, defining `mesh:C016719` /
`ristocetin A`. Fresh OLS4 lookup resolved the MeSH CURIE with the same
canonical label.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Rifamycin_B.yaml
data/ingredients/mapped/Rifamycin_O.yaml
data/ingredients/mapped/Rifamycin_S.yaml
data/ingredients/mapped/Rifamycin_Sv.yaml
data/ingredients/mapped/Ristocetin_A.yaml` passed for the 5-file batch with 0
ERROR rows. Direct `linkml-term-validator validate-data` with `--labels` passed
for the same 5 files.

**Evidence**: The per-record YAML agrees with the regenerated aggregate row
when keyed by `(identifier, preferred_term)`. Final SSSOM row 2520 maps exactly
to `mesh:C016719` with an empty `other` field. The older status-conflict
proposal in `mappings/record_research_validation.tsv` was superseded by #213,
which promoted this row to the exact MeSH label match now present in the YAML
and in final SSSOM.

**Completeness**: The MicrobeDecoder occurrence provenance, exact MeSH identity,
and final SSSOM row agree. No roles or chemical properties are asserted.

**Recommended Edits**: None.
