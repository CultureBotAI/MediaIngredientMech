# `data/ingredients/mapped/Sodium_Acetate_Trihydrate.yaml`

**Verdict**: pass.

**Identity**: `Sodium acetate trihydrate` maps exactly to active, defining
`CHEBI:32138` / `sodium acetate trihydrate`. Fresh OLS4 lookup confirmed the
ChEBI label, CAS RN `6131-90-4`, formula `C2H3O2.3H2O.Na`, and exact IUPAC
synonym `sodium acetate--water (1/3)`. PubChem resolves the same CAS RN to CID
`23665404` with the hydrate-specific formula and InChI.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sodium_Acetate.yaml
data/ingredients/mapped/Sodium_Acetate3h2o.yaml
data/ingredients/mapped/Sodium_Acetate_Trihydrate.yaml
data/ingredients/mapped/Sodium_Adipate.yaml
data/ingredients/mapped/Sodium_Alginate.yaml` passed for the 5-file batch with
0 ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed for all 5 OBO-grounded files.

**Evidence**: The exact CHEBI identity, hydrate CAS, formula, InChI, and
hydrate-form synonyms pass. The `BUFFER` role is a CultureMech `DATABASE_ENTRY`
derived from original role text, and the raw `Role:` strings remain filtered
from final SSSOM. The per-record YAML agrees with the regenerated aggregate
row when keyed by `(preferred_term, mapping_status)`.

**Completeness**: Final SSSOM row 2613 maps this subject exactly to
`CHEBI:32138` and publishes only same-hydrate aliases plus `CAS:6131-90-4` in
`other`. The dedicated hydrate reports record `CHEBI:32138` as the correct
trihydrate term.

**Recommended Edits**: None.
