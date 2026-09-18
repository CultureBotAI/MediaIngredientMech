# `data/ingredients/mapped/Sodium_Beta-glycerophosphate.yaml`

**Verdict**: pass.

**Identity**: `Sodium beta-glycerophosphate` maps exactly to active, defining
`CHEBI:132089` / `sodium glycerol 2-phosphate`. Fresh OLS4 lookup confirmed
the ChEBI term, CAS RN `819-83-0`, formula `C3H7O6P.2Na`, and the same InChI
stored in the record. PubChem resolves the CAS RN to an anhydrous disodium
glycerol 2-phosphate CID whose InChI also matches the YAML.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sodium_Antimonate.yaml
data/ingredients/mapped/Sodium_Azide.yaml
data/ingredients/mapped/Sodium_Beta-glycerophosphate.yaml
data/ingredients/mapped/Sodium_Bromate.yaml
data/ingredients/mapped/Sodium_Carbonate_Monohydrate.yaml` passed for the
5-file batch with 0 ERROR rows. Direct `linkml-term-validator validate-data`
with `--labels` passed.

**Evidence**: The exact CHEBI identity, structure fields, eight kg-microbe
synonyms, and merged raw beta-glycerophosphate surface forms all denote the
same anhydrous disodium glycerol 2-phosphate identity. Final SSSOM row 2622
exports those same same-substance labels plus `CAS:819-83-0`; it does not
collapse the neighboring pentahydrate record. The per-record YAML agrees with
the regenerated aggregate row when keyed by `(preferred_term, mapping_status)`.

**Completeness**: The record has no asserted roles or components. The
occurrence refresh and CultureMech alias backfill explain why raw beta-glyph
surface forms are retained as synonyms.

**Recommended Edits**: None.
