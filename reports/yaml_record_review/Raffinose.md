# `data/ingredients/mapped/Raffinose.yaml`

**Verdict**: pass.

**Identity**: `Raffinose` maps exactly to defining `CHEBI:16634` / `raffinose`.
Fresh OLS4 lookup resolved the ChEBI CURIE, and PubChem lookup by the stored CAS
`512-69-6` resolved CID 439242 with the same formula and InChI as the YAML.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Rac-3-Hydroxypentanoic_Acid.yaml
data/ingredients/mapped/Racemomycin_E.yaml data/ingredients/mapped/Radicicol.yaml
data/ingredients/mapped/Raffinose.yaml data/ingredients/mapped/Ramoplanin.yaml`
passed for the 5-file batch with 0 ERROR rows. Direct
`linkml-term-validator validate-data` with `--labels` passed for this CHEBI
record.

**Evidence**: The per-record YAML agrees with the aggregate
`data/curated/mapped_ingredients.yaml` row. Final SSSOM row 2491 maps exactly to
`CHEBI:16634`; the raw CultureMech `Role: Carbon source` synonym is filtered
out, and `other` contains only curated exact synonyms plus `CAS:512-69-6`. The
carbon-source role is supported by the imported CultureMech `DATABASE_ENTRY`
evidence and original role text, not by a provisional name-list rule.

**Completeness**: Occurrence statistics were refreshed to 8 media and 8 total
occurrences. The exact ChEBI identity, kg-microbe node id, chemical properties,
CultureMech role, and final SSSOM row agree.

**Recommended Edits**: None.
