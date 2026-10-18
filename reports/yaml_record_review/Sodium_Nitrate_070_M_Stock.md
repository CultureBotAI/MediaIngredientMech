# `data/ingredients/mapped/Sodium_Nitrate_070_M_Stock.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Sodium nitrate (0.70 M stock)` keeps a local
`kgmicrobe.ingredient` identity and maps by `NARROW_MATCH` to active, defining
`CHEBI:63005` / `sodium nitrate`. Fresh OLS4 lookup confirmed the ChEBI parent
label, CAS RN `7631-99-4`, formula `NO3.Na`, InChI, InChIKey, SMILES, `NaNO3`,
and the exact IUPAC synonym.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sodium_Malonate.yaml
data/ingredients/mapped/Sodium_Metasilicate.yaml
data/ingredients/mapped/Sodium_Metasilicate_Silicate_For_Diatom_Frustules.yaml
data/ingredients/mapped/Sodium_Methanesulfonate.yaml
data/ingredients/mapped/Sodium_Nitrate_070_M_Stock.yaml` passed for the
5-file batch with 0 ERROR rows. Direct `linkml-term-validator validate-data`
with `--labels` passed for the ChEBI parent.

**Evidence**: The stock-solution identity, close sodium-nitrate parent, and
paired exact local registry rows all pass. Final SSSOM rows 2660-2662 preserve
the parent row, `kgmicrobe.ingredient` identity row, and
`kgmicrobe.compound` compatibility row. The per-record YAML agrees with the
regenerated aggregate row when keyed by identifier and preferred term.

The final parent row still exports `NaNO3` and `sodium trioxidonitrate(1-)` in
`other`. Those are exact synonyms for the sodium nitrate solute, not for the
0.70 M stock solution subject, so they cross the stock/solute boundary.

**Completeness**: The record correctly uses `ingredient_type: STOCK_SOLUTION`
and carries the exact local rows required for a parent mapping. It needs the
broader solute's synonyms kept out of final SSSOM for the stock subject.

**Recommended Edits**: Remove the bare sodium-nitrate solute synonyms from this
stock-solution record or mark them so final SSSOM excludes them, then rebuild
final SSSOM and confirm rows 2660-2662 keep only the parent and exact local
identity relationships.
