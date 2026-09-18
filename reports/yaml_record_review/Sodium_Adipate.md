# `data/ingredients/mapped/Sodium_Adipate.yaml`

**Verdict**: pass.

**Identity**: `Sodium adipate` is modeled as a distinct CAS-backed sodium salt
with primary identifier `cas:7486-38-6` and a narrower parent mapping to
`FOODON:03413240` / `sodium adipate`. Fresh FOODON OLS lookup resolved the
parent term by exact label, live ChEBI OLS search found no `sodium adipate`
term, and PubChem resolves CAS RN `7486-38-6` to CID `24073` with the same
formula, SMILES, and InChI stored in the record.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sodium_Acetate.yaml
data/ingredients/mapped/Sodium_Acetate3h2o.yaml
data/ingredients/mapped/Sodium_Acetate_Trihydrate.yaml
data/ingredients/mapped/Sodium_Adipate.yaml
data/ingredients/mapped/Sodium_Alginate.yaml` passed for the 5-file batch with
0 ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed for all 5 OBO-grounded files.

**Evidence**: The FOODON parent row is intentionally `skos:narrowMatch` because
the MIM subject keeps its own CAS primary identity. Final SSSOM rows 2614-2616
contain the FOODON parent row plus exact CAS and `kgmicrobe.ingredient`
registry rows, satisfying the registry-row pattern for a parent mapping.

**Completeness**: The CAS field, PubChem CID `24073`, formula, structure
fields, empty synonym list, and absence of asserted roles are consistent. The
per-record YAML agrees with the regenerated aggregate row when keyed by
`(preferred_term, mapping_status)`.

**Recommended Edits**: None.
