# `data/ingredients/mapped/Rhamnogalacturonan_From_Soy_Bean_Pectic_Fibre.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Rhamnogalacturonan from soy bean pectic fibre` is a
CAS-primary fallback to `cas:39280-21-2`, and PubChem lookup by that CAS
returned no CID. The fallback itself is not enough to disambiguate this record:
the neighboring `Rhamnogalacturonan I from potato pectic fiber` record uses the
same exact CAS identifier for a different source-qualified preferred term.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Reducing_Agent.yaml data/ingredients/mapped/Resazurin.yaml
data/ingredients/mapped/Resistomycin.yaml data/ingredients/mapped/Resveratrol.yaml
data/ingredients/mapped/Rhamnogalacturonan_From_Soy_Bean_Pectic_Fibre.yaml` passed
for the 5-file batch with 0 ERROR rows. Engine A OBO label validation was
skipped because this is a CAS-only registry record, and the term-validator's OAK
adapters do not label `cas:` CURIEs.

**Evidence**: The per-record YAML agrees with its
`data/curated/mapped_ingredients.yaml` row when the aggregate entry is matched by
both `identifier` and `preferred_term`; an identifier-only lookup collides with
the potato rhamnogalacturonan record. Final SSSOM row 2497 publishes
`MIM:Rhamnogalacturonan_From_Soy_Bean_Pectic_Fibre skos:exactMatch
cas:39280-21-2`, duplicating the same registry identity used by the potato
record rather than preserving a source-specific identity.

**Completeness**: The old process-only `autoclaved` and `filtered` synonyms are
already removed, and `UNDEFINED_MIXTURE` is plausible for a pectic-fibre
material. The unresolved gap is the duplicate exact CAS identity shared by two
source-qualified records.

**Recommended Edits**: Review both rhamnogalacturonan CAS-fallback records
together. If the source labels are the same substance, merge them; if soy bean
and potato pectic-fibre sources are intentionally distinct, mint source-specific
`kgmicrobe.ingredient:` identifiers and keep `39280-21-2` only as shared CAS
provenance rather than as the exact primary identity.
