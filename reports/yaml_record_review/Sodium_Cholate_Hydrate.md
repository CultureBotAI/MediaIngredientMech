# `data/ingredients/mapped/Sodium_Cholate_Hydrate.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Sodium cholate hydrate` is correctly kept distinct from
anhydrous `CHEBI:26711` / `sodium cholate` with primary identifier
`cas:206986-87-0`. Fresh OLS4 lookup confirmed that `CHEBI:26711` is the
anhydrous sodium cholate term with CAS RN `361-09-1`, while PubChem resolves
hydrate CAS RN `206986-87-0` to CID `23679061` with the hydrate formula,
SMILES, and InChI stored in the record. A fresh ChEBI search for `sodium
cholate hydrate` found no specific hydrate term.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sodium_Carbonate_Solution.yaml
data/ingredients/mapped/Sodium_Chlorite.yaml
data/ingredients/mapped/Sodium_Cholate_Hydrate.yaml
data/ingredients/mapped/Sodium_Chromate.yaml
data/ingredients/mapped/Sodium_Citrate.yaml` passed for the 5-file batch with
0 ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed.

**Evidence**: The hydrate CAS identity, PubChem structure, and
`skos:closeMatch` to the anhydrous ChEBI term pass, and the per-record YAML
agrees with the regenerated aggregate row when keyed by `(preferred_term,
mapping_status)`.

The final SSSOM needs repair. `reports/hydrate_grounding.tsv` classifies this
record as `CAS_MISSING_ANCHOR_ROWS`: rows 2628-2629 preserve the exact CAS
identity but omit an exact `kgmicrobe.compound:sodium_cholate_hydrate` anchor.
Row 2628 also exports `sodium 3alpha,7alpha,12alpha-trihydroxy-5beta-cholan-24-oate`
in `other`, but live ChEBI confirms that string is the exact IUPAC synonym for
anhydrous `CHEBI:26711`, not the hydrate.

**Completeness**: No roles or components are asserted. The hydrate has enough
CAS and PubChem support for a distinct CAS-primary identity; the material gap
is the missing kg-microbe anchor and anhydrous synonym leakage in final SSSOM.

**Recommended Edits**: Add the missing exact
`kgmicrobe.compound:sodium_cholate_hydrate` anchor, remove anhydrous sodium
cholate labels from the hydrate's final `other`, rebuild final SSSOM, and
confirm the hydrate-grounding row no longer reports `CAS_MISSING_ANCHOR_ROWS`.
