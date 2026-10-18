# `data/ingredients/mapped/S-adenosyl_Homocysteine.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `S-adenosyl Homocysteine` is currently represented as a CAS
fallback, `cas:9789-92-0`, but that CAS did not resolve in fresh OLS4 or
PubChem lookups.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Rutilantinone.yaml
data/ingredients/mapped/Rutin.yaml data/ingredients/mapped/Rye-bran.yaml
data/ingredients/mapped/S-3-hydroxybutyrate.yaml
data/ingredients/mapped/S-adenosyl_Homocysteine.yaml` passed for the 5-file
batch with 0 ERROR rows. Direct `linkml-term-validator validate-data` with
`--labels` crashed on the first CAS-primary fallback because the OBO SQLite
adapter cannot label `cas:` registry IDs; rerunning it on the CHEBI/FOODON
subset, Rutin, Rye-bran, and S-3-hydroxybutyrate, passed.

**Evidence**: The per-record YAML agrees with the regenerated aggregate row
when keyed by `(identifier, preferred_term)`. Final SSSOM row 2543 maps exactly
to `cas:9789-92-0` and publishes both the adenosyl-L-homocysteine synonym and
`CAS:9789-92-0` in `other`.

The CAS fallback appears stale or incorrect. Fresh OLS4 exact search for
`9789-92-0` returned no ChEBI hit, PubChem had no CID for `9789-92-0`, and
searching OLS4 by `S-adenosyl-L-homocysteine` resolved active `CHEBI:16680`.
CHEBI:16680 also lists the same adenosyl-L-homocysteine synonym family that the
YAML already carries, so the current CAS fallback should not remain primary
without a source-backed explanation of what `9789-92-0` denotes.

**Completeness**: The unknown-term triage table correctly recorded that CAS
registry CURIEs are outside OAK/OLS coverage, but the fresh CAS lookup shows
this row is not just an expected local-registry case. No roles, components, or
structure fields are asserted locally.

**Recommended Edits**: Revisit
`data/ingredients/mapped/S-adenosyl_Homocysteine.yaml` against the original
CultureBotHT CAS source. If the source intended S-adenosyl-L-homocysteine,
promote the record to CHEBI:16680, populate exact CHEBI-derived structure
fields, remove `9789-92-0`, and regenerate final SSSOM so row 2543 no longer
publishes the non-resolving CAS.
