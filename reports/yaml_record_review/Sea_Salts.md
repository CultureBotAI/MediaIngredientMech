# `data/ingredients/mapped/Sea_Salts.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Sea salts` represents a commercial sea-salts mixture whose best
external anchor is generic `NCIT:C75874` / `Sea Salt`. Fresh OLS4 lookup
resolved the NCIT term, but the YAML's `mapping_quality: CLOSE_MATCH` correctly
records that the NCIT class is only a close parent, not an exact commercial
mixture identity.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sarcidin.yaml data/ingredients/mapped/Sarcosine.yaml
data/ingredients/mapped/Sclareolide.yaml
data/ingredients/mapped/Scopoletin.yaml
data/ingredients/mapped/Sea_Salts.yaml` passed for the 5-file batch with 0
ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed for the OBO-resolvable subset, `Sarcosine`, `Sclareolide`,
`Scopoletin`, and `Sea_Salts`; the `kgmicrobe.compound` placeholder is outside
Engine A coverage.

**Evidence**: The per-record YAML agrees with the regenerated aggregate row
when keyed by `(identifier, preferred_term)`. The row needs curation because
final SSSOM row 2565 publishes `MIM:Sea_Salts skos:exactMatch NCIT:C75874`,
even though the #114 curation and current YAML record only support a
`CLOSE_MATCH`. The same SSSOM row also exports `sea salts (Sigma)` and
`Sea salts (Sigma-Aldrich)` in `other`; those vendor-qualified strings are
catalog variants, not real synonyms of the generic NCIT class.

**Completeness**: The occurrence count is current and the undefined-mixture
type fits, but the SSSOM export erases the close-match semantics and leaks
catalog strings into synonym payloads.

**Recommended Edits**: Preserve a local exact identity for the commercial
sea-salts preparation, keep `NCIT:C75874` only as a close parent, and prevent
vendor-qualified catalog labels from reaching final SSSOM `other`.
