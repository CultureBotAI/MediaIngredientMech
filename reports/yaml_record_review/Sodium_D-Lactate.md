# `data/ingredients/mapped/Sodium_D-Lactate.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Sodium D-Lactate` is a CAS-primary D-lactate salt with fallback
identifier `cas:920-49-0`. Fresh PubChem lookup resolved CAS RN `920-49-0` to
CID `23666457`, formula `C3H5NaO3`, and the same stereospecific InChI stored
in the record. Fresh ChEBI OLS search found no specific sodium D-lactate term.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sodium_Cyanide.yaml
data/ingredients/mapped/Sodium_D-Lactate.yaml
data/ingredients/mapped/Sodium_Deoxycholate.yaml
data/ingredients/mapped/Sodium_Deoxycholate_Monohydrate.yaml
data/ingredients/mapped/Sodium_Dithionite.yaml` passed for the 5-file batch
with 0 ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed for the four CHEBI-grounded records; this CAS fallback row was skipped
because `cas` is outside the Engine A OBO subset.

**Evidence**: The CAS fallback identity, CAS field, formula, structure fields,
occurrence count, and final exact CAS SSSOM row pass. The per-record YAML
agrees with the regenerated aggregate row when keyed by `(preferred_term,
mapping_status)`.

The nutritional roles need real evidence. `CARBON_SOURCE` and `ENERGY_SOURCE`
are still `COMPUTATIONAL_PREDICTION` claims from provisional name-pattern
rules, and no source in this record ties sodium D-lactate to a medium or
organism context that supports those roles.

**Completeness**: No curated synonyms, components, or environmental contexts
are asserted. The exact CAS identity is complete enough; only the roles are
over-scoped.

**Recommended Edits**: Either attach source-backed medium evidence to the
`CARBON_SOURCE` and `ENERGY_SOURCE` roles or remove those two provisional
roles from `data/ingredients/mapped/Sodium_D-Lactate.yaml`, then validate the
record and rebuild final SSSOM.
