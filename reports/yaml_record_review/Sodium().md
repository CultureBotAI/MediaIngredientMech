# `data/ingredients/mapped/Sodium().yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Sodium(+)` maps exactly to active, defining `CHEBI:29101` /
`sodium(1+)`. Fresh OLS4 lookup resolved the ChEBI term and agrees with the
documented MicrobeDecoder parse-artifact repair that promoted `Sodium(+)` to
the monoatomic sodium cation.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sncl2_X_2_H2o.yaml
data/ingredients/mapped/Sodium().yaml
data/ingredients/mapped/Sodium_2-bromoethanesulfonate.yaml
data/ingredients/mapped/Sodium_2-mercaptoethanesulfonate.yaml
data/ingredients/mapped/Sodium_4-Hydroxybenzoate.yaml` passed for the 5-file
batch with 0 ERROR rows. Direct `linkml-term-validator validate-data` with
`--labels` passed for the 4 CHEBI files; `Sodium_2-bromoethanesulfonate` was
skipped because `cas` is outside the Engine A OBO term-validation subset.

**Evidence**: The repaired MicrobeDecoder `Sodium(+)` identity and structure
fields pass. The per-record YAML agrees with the regenerated aggregate row when
keyed by `(identifier, preferred_term)`.

The final SSSOM row needs synonym cleanup. Row 2609 exports raw CultureMech
surface form `Sodium` as `other`, but fresh OLS4 lookup on `CHEBI:29101` lists
only cation-specific exact synonyms and does not list plain elemental `Sodium`.

**Completeness**: The exact sodium-cation identity and structure fields agree.
The ambiguous raw `Sodium` alias should not publish as a synonym for
`sodium(1+)`.

**Recommended Edits**: Remove `Sodium` from
`data/ingredients/mapped/Sodium().yaml` or update the SSSOM synonym policy to
exclude ambiguous element aliases for ion records, then rebuild final SSSOM and
confirm row 2609 has an empty `other` field.
