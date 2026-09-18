# `data/ingredients/mapped/Sodium_Alginate.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Sodium alginate` maps exactly to active, defining
`CHEBI:53311` / `sodium alginate`. Fresh OLS4 lookup confirmed the ChEBI term,
CAS RN `9005-38-3`, formula `(C6H7O6)n.H2NaO`, and structure fields, and the
KEGG `D03336` record resolves back to the same CAS and ChEBI identifiers.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sodium_Acetate.yaml
data/ingredients/mapped/Sodium_Acetate3h2o.yaml
data/ingredients/mapped/Sodium_Acetate_Trihydrate.yaml
data/ingredients/mapped/Sodium_Adipate.yaml
data/ingredients/mapped/Sodium_Alginate.yaml` passed for the 5-file batch with
0 ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed for all 5 OBO-grounded files.

**Evidence**: The exact CHEBI identity, CAS, formula, InChI, and
CultureMech-backed `SOLIDIFYING_AGENT` role pass. The per-record YAML agrees
with the regenerated aggregate row when keyed by `(preferred_term,
mapping_status)`.

The kg-microbe P4.4 synonym sweep needs review. The five kg-microbe aliases in
the YAML are only bulk-promoted `EXACT_SYNONYM` claims; live ChEBI lists them
as related synonyms sourced from ChEMIDplus or KEGG rather than exact ChEBI
synonyms. Final SSSOM row 2617 exports all five in `other`, so any related,
trade-name, or source-organism alias that is not a true same-substance label
would publish as a plain synonym for the MIM subject.

**Completeness**: No components are needed for the ChEBI sodium alginate
polymer identity. The record is complete for exact identity, CAS, chemistry,
and role evidence; the only material gap is claim-level synonym evidence for
the kg-microbe alias block.

**Recommended Edits**: Review `Algiline`, `Algin`, `Arcrane`, `Ascophyllum`,
and `Sodium polymannuronate` in `data/ingredients/mapped/Sodium_Alginate.yaml`.
Keep only true same-substance labels as active synonyms, demote related or
non-substance names to provenance-only entries, rebuild final SSSOM, and
confirm row 2617 no longer exports any non-exact alias in `other`.
