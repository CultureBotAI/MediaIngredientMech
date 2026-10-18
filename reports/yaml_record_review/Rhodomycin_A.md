# `data/ingredients/mapped/Rhodomycin_A.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Rhodomycin A` intentionally keeps the local
`kgmicrobe.compound:rhodomycin_a` identity and maps narrowly to the broader
`mesh:C004977` / `rhodomycin` parent. Fresh OLS4 lookup resolved the MeSH CURIE
as a defining, active `rhodomycin` term. A fresh PubChem name lookup for
Rhodomycin A resolved a distinct Rhodomycin A compound at CID 9896436, while
Rhodomycin B resolves to a different formula and structure, supporting the
current local exact row rather than an exact collapse to `CHEBI:81879`.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Rhodomycin_A.yaml
data/ingredients/mapped/Rhodomycin_B.yaml data/ingredients/mapped/Ribitol.yaml
data/ingredients/mapped/Riboflavin.yaml
data/ingredients/mapped/Ribonucleic_Acid_From_Torula_Yeast_Type_VI.yaml` passed
for the 5-file batch with 0 ERROR rows. Direct
`linkml-term-validator validate-data` with `--labels` passed for the same 5
files.

**Evidence**: The per-record YAML agrees with the regenerated aggregate row
when keyed by `(identifier, preferred_term)`. Final SSSOM rows 2503 and 2504
publish the MeSH `skos:narrowMatch` and the required local exact registry row,
with both `other` fields empty. The old `UNKNOWN_TERM` review result is already
triaged in `mappings/ingredient_mappings_unknown_term_triage.tsv` as missing
MeSH prefix coverage plus an expected local registry identifier.

The `physicochemical_roles.SELECTIVE_AGENT` assertion is unsupported. Its only
evidence is a `COMPUTATIONAL_PREDICTION` from `infer_roles_from_name_lists`
with the standard provisional curator note.

**Completeness**: The broader MeSH parent is adequate for publication because
no exact CHEBI or NCIT parent is curated here. PubChem CID 9896436 is a useful
future source for structure completion, but this record currently asserts no
chemical-properties fields.

**Recommended Edits**: Either remove `physicochemical_roles.SELECTIVE_AGENT` or
replace the name-list prediction with source-backed evidence for Rhodomycin A
as a selective agent. Optionally add PubChem-backed structure fields for CID
9896436 in the same future curation pass.
