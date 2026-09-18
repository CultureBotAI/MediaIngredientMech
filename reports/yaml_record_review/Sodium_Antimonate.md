# `data/ingredients/mapped/Sodium_Antimonate.yaml`

**Verdict**: pass.

**Identity**: `Sodium antimonate` is modeled as a CAS-primary antimonate salt
with a narrower parent mapping to `mesh:C034426` / `sodium antimonate`. Fresh
OLS4 lookup resolved `mesh:C034426` exactly, ChEBI OLS search found related
antimony/sodium terms but no exact sodium antimonate term, and PubChem resolves
CAS RN `15432-85-6` to CID `25469`.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sodium_Antimonate.yaml
data/ingredients/mapped/Sodium_Azide.yaml
data/ingredients/mapped/Sodium_Beta-glycerophosphate.yaml
data/ingredients/mapped/Sodium_Bromate.yaml
data/ingredients/mapped/Sodium_Carbonate_Monohydrate.yaml` passed for the
5-file batch with 0 ERROR rows. Direct `linkml-term-validator validate-data`
with `--labels` passed for the four CHEBI files. `Sodium_Antimonate` uses
lowercase `mesh:`, outside the Engine A OBO term-validation subset, and was
checked with direct OLS instead.

**Evidence**: The CAS fallback identity, exact MeSH parent, and empty synonym
list pass. Final SSSOM rows 2618-2620 carry the MeSH parent plus exact CAS and
`kgmicrobe.compound` registry rows, which preserves the distinct CAS identity
beside the parent mapping. The per-record YAML agrees with the regenerated
aggregate row when keyed by `(preferred_term, mapping_status)`.

**Completeness**: No roles, components, or curated synonyms are asserted. The
record is complete enough for a CAS-primary salt whose exact ChEBI equivalent
is still absent.

**Recommended Edits**: None.
