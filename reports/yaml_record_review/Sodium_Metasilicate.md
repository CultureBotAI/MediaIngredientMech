# `data/ingredients/mapped/Sodium_Metasilicate.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Sodium Metasilicate` maps exactly to `mesh:C025349` /
`sodium metasilicate`. Fresh prefix-specific OLS4 lookup confirmed the MeSH
term, and PubChem resolves CAS RN `6834-92-0` to CID `23266` with formula
`Na2O3Si`, InChI, InChIKey, and a disodium metasilicate structure.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sodium_Malonate.yaml
data/ingredients/mapped/Sodium_Metasilicate.yaml
data/ingredients/mapped/Sodium_Metasilicate_Silicate_For_Diatom_Frustules.yaml
data/ingredients/mapped/Sodium_Methanesulfonate.yaml
data/ingredients/mapped/Sodium_Nitrate_070_M_Stock.yaml` passed for the
5-file batch with 0 ERROR rows. Engine A term validation is skipped for this
record because `mesh:` is outside the OBO prefixes handled by the direct
LinkML term-validator recipe.

**Evidence**: The exact MeSH identity, CAS RN, and final own-identifier SSSOM
row pass. `mappings/ingredient_mappings_unknown_term_triage.tsv` already
records that prefix-specific OLS resolves `mesh:C025349`; the old
`UNKNOWN_TERM` flag came from missing prefix coverage in the synonym-review
dispatcher, not a dead mapping. The per-record YAML agrees with the regenerated
aggregate row when keyed by identifier and preferred term.

Final SSSOM row 2658 still exports `Sodium metasilicate (silicate for diatom
frustules)` in `other`. That string carries a CultureMech use-context
parenthetical, not a same-substance synonym for sodium metasilicate.

**Completeness**: The live identity is sound, but the final synonym set still
needs to drop the diatom-frustule context label. The bare `Sodium Metasilicate`
raw synonym duplicates the preferred term and is harmless.

**Recommended Edits**: Remove the `Sodium metasilicate (silicate for diatom
frustules)` synonym from the live metasilicate record or mark it so final
SSSOM excludes it, then rebuild final SSSOM and confirm row 2658 exports only
true sodium metasilicate identifiers such as `CAS:6834-92-0`.
