# `data/ingredients/mapped/Ribonucleic_Acid_From_Torula_Yeast_Type_VI.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Ribonucleic acid from torula yeast type VI` correctly uses a
local `kgmicrobe.ingredient:ribonucleic_acid_from_torula_yeast_type_vi`
identifier and maps narrowly to active, defining `CHEBI:33697` / `ribonucleic
acid`. Fresh OLS4 lookup resolved `CHEBI:33697` as the generic ribonucleic-acid
class and carried the same CAS `63231-63-0`; fresh PubChem lookup by that CAS
returned no CID, consistent with the parent term having no concrete structure.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Rhodomycin_A.yaml
data/ingredients/mapped/Rhodomycin_B.yaml data/ingredients/mapped/Ribitol.yaml
data/ingredients/mapped/Riboflavin.yaml
data/ingredients/mapped/Ribonucleic_Acid_From_Torula_Yeast_Type_VI.yaml` passed
for the 5-file batch with 0 ERROR rows. Direct
`linkml-term-validator validate-data` with `--labels` passed for the same 5
files.

**Evidence**: The per-record YAML agrees with the regenerated aggregate row
when keyed by `(identifier, preferred_term)`. Final SSSOM rows 2508-2510 publish
the expected broad ChEBI row plus the exact local registry rows required for a
source-specific `skos:narrowMatch` subject.

The `chebi_synonym_review` backfilled `ribonucleic acids` synonym belongs to
the broader ChEBI parent, not to the source-qualified Torula-yeast type VI
record. Final SSSOM row 2508 currently exports that broader label in `other`,
erasing the source-specific boundary that issue #322 introduced.

**Completeness**: The conservative broad ChEBI grounding and local exact
identity rows are complete enough for the current model. The only unsafe
payload is the parent synonym copied onto this narrower MIM record.

**Recommended Edits**: Remove the `ribonucleic acids` `chebi_synonym_review`
synonym from
`data/ingredients/mapped/Ribonucleic_Acid_From_Torula_Yeast_Type_VI.yaml` and
regenerate final SSSOM; row 2508 should keep the `skos:narrowMatch` to
`CHEBI:33697` without exporting a generic RNA synonym in `other`.
