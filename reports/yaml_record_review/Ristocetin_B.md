# `data/ingredients/mapped/Ristocetin_B.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Ristocetin B` correctly keeps the local
`kgmicrobe.compound:ristocetin_b` identity and maps narrowly to active
`CHEBI:85129` / `ristocetin`. Fresh OLS4 lookup resolved the broader ChEBI
parent, and a fresh ChEBI OLS exact search found no exact Ristocetin B ChEBI
term, so the local identity plus `skos:narrowMatch` remains appropriate.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Ristocetin_B.yaml data/ingredients/mapped/Rna.yaml
data/ingredients/mapped/Robustic_Acid.yaml
data/ingredients/mapped/Roccellic_Acid.yaml
data/ingredients/mapped/Rolled_Oats.yaml` passed for the 5-file batch with 0
ERROR rows. Direct `linkml-term-validator validate-data` with `--labels` passed
for the same 5 files.

**Evidence**: The per-record YAML agrees with the regenerated aggregate row
when keyed by `(identifier, preferred_term)`. Final SSSOM rows 2521 and 2522
publish the broad ChEBI row and the expected local exact registry row.

Two fields still blur the local Ristocetin B identity with broader or raw data.
First, `chemical_properties` are copied from `CHEBI:85129` `ristocetin`
(`C95H110N8O44`), while fresh PubChem lookup for Ristocetin B resolved CID
90478637 with formula `C84H92N8O35`. Second, final SSSOM row 2521 exports
`produces: ristocetin B` in `other`; that is process-qualified source text, not
an alternate name for this compound.

**Completeness**: The conservative broad ChEBI grounding and local exact
identity rows are complete enough for publication. The unsafe payloads are the
parent-derived structure fields and the process-qualified backfilled synonym.

**Recommended Edits**: Remove the CHEBI-parent `chemical_properties` from
`data/ingredients/mapped/Ristocetin_B.yaml` unless they can be replaced with
source-backed Ristocetin B-specific values, and remove the
`sssom_other_backfill` synonym `produces: ristocetin B`. Regenerate final SSSOM
and confirm row 2521 no longer exports the process text in `other`.
