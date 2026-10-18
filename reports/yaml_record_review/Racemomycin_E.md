# `data/ingredients/mapped/Racemomycin_E.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Racemomycin E` keeps a local
`kgmicrobe.compound:racemomycin_e` identity and uses `mesh:C019594` /
`racemomycin` as a broader parent. Fresh OLS4 lookup resolved the MeSH parent as
a defining term, and an exact PubChem name lookup found a distinct Racemomycin E
structure at CID 198907, supporting the current local-specific identity rather
than an exact collapse to the generic MeSH parent.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Rac-3-Hydroxypentanoic_Acid.yaml
data/ingredients/mapped/Racemomycin_E.yaml data/ingredients/mapped/Radicicol.yaml
data/ingredients/mapped/Raffinose.yaml data/ingredients/mapped/Ramoplanin.yaml`
passed for the 5-file batch with 0 ERROR rows. Direct
`linkml-term-validator validate-data` with `--labels` passed for the MeSH parent
mapping.

**Evidence**: The per-record YAML agrees with the aggregate
`data/curated/mapped_ingredients.yaml` row. Final SSSOM rows 2488 and 2489
publish the MeSH `skos:narrowMatch` and the required local exact registry row,
and both `other` fields are empty. The old `UNKNOWN_TERM` SSSOM review result
is already triaged in `mappings/ingredient_mappings_unknown_term_triage.tsv` as
missing-prefix coverage for the MeSH parent and an expected local registry
identifier for the `kgmicrobe.compound:` row.

The `physicochemical_roles.SELECTIVE_AGENT` assertion is unsupported: its only
evidence is a `COMPUTATIONAL_PREDICTION` from
`infer_roles_from_name_lists` with the standard provisional curator note.

**Completeness**: The broader MeSH parent is sufficient for publication because
no exact CHEBI or NCIT parent is curated here. PubChem CID 198907 is a useful
future source for structure completion, but no current chemical-properties field
is asserted.

**Recommended Edits**: Either remove `physicochemical_roles.SELECTIVE_AGENT` or
replace the name-list prediction with source-backed evidence for Racemomycin E
as a selective agent. Optionally add PubChem-backed structure fields for CID
198907 in the same future curation pass.
