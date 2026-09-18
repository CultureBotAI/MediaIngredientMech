# `data/ingredients/mapped/Rac-3-Hydroxypentanoic_Acid.yaml`

**Verdict**: pass.

**Identity**: `rac-3-Hydroxypentanoic Acid` now preserves the racemate as the
CAS-primary `cas:10237-77-1` identity and points to `CHEBI:139272` /
`3-hydroxypentanoic acid` only with `NARROW_MATCH`. Fresh OLS4 lookup resolved
`CHEBI:139272` as a defining ChEBI term, and PubChem lookup by CAS resolved CID
107802 with the same formula and achiral InChI as the YAML.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Rac-3-Hydroxypentanoic_Acid.yaml
data/ingredients/mapped/Racemomycin_E.yaml data/ingredients/mapped/Radicicol.yaml
data/ingredients/mapped/Raffinose.yaml data/ingredients/mapped/Ramoplanin.yaml`
passed for the 5-file batch with 0 ERROR rows. Direct
`linkml-term-validator validate-data` with `--labels` passed for the ChEBI
parent mapping.

**Evidence**: The per-record YAML agrees with the aggregate
`data/curated/mapped_ingredients.yaml` row. Final SSSOM rows 2485-2487 publish
the expected parent `skos:narrowMatch`, the exact CAS identity row, and the
exact `kgmicrobe.compound:rac-3-hydroxypentanoic_acid` Rule B1 sibling row. The
only `other` token is `CAS:10237-77-1`, matching the record's
`chemical_properties.cas_rn`.

**Completeness**: #456 superseded the old CAS-to-CHEBI exact match and kept the
specific racemate distinct from the stereo-unspecified ChEBI parent. No roles,
components, or extra synonyms are asserted.

**Recommended Edits**: None.
