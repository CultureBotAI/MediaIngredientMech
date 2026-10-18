# `data/ingredients/mapped/Rna.yaml`

**Verdict**: pass.

**Identity**: `Rna` maps exactly to active, defining `mesh:D012313` / `RNA`.
Fresh OLS4 lookup resolved the MeSH CURIE with the same canonical label and a
generic RNA definition, matching the #213 split that gave generic RNA its own
identifier instead of merging it into the Torula-yeast RNA product record.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Ristocetin_B.yaml data/ingredients/mapped/Rna.yaml
data/ingredients/mapped/Robustic_Acid.yaml
data/ingredients/mapped/Roccellic_Acid.yaml
data/ingredients/mapped/Rolled_Oats.yaml` passed for the 5-file batch with 0
ERROR rows. Direct `linkml-term-validator validate-data` with `--labels` passed
for the same 5 files.

**Evidence**: The per-record YAML agrees with the regenerated aggregate row
when keyed by `(identifier, preferred_term)`. Final SSSOM row 2523 maps exactly
to `mesh:D012313` and exports an empty `other` field. The old
CHEBI:33697 proposal in
`mappings/microbedecoder_residual_research_proposed.sssom.tsv` explicitly
warned not to merge this generic RNA record onto the Torula-yeast product; the
current #213 MeSH promotion implements that split.

**Completeness**: The MicrobeDecoder occurrence provenance, exact MeSH identity,
and final SSSOM row agree. No roles or chemical properties are asserted.

**Recommended Edits**: None.
