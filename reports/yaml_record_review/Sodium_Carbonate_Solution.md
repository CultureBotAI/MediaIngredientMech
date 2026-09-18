# `data/ingredients/mapped/Sodium_Carbonate_Solution.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Sodium carbonate solution` is a stock-solution ingredient
grounded to active, defining `CHEBI:29377` / `sodium carbonate`. Fresh OLS4
lookup confirmed that the ChEBI term denotes anhydrous sodium carbonate with
formula `CO3.2Na`, matching the solute structure stored on the record.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sodium_Carbonate_Solution.yaml
data/ingredients/mapped/Sodium_Chlorite.yaml
data/ingredients/mapped/Sodium_Cholate_Hydrate.yaml
data/ingredients/mapped/Sodium_Chromate.yaml
data/ingredients/mapped/Sodium_Citrate.yaml` passed for the 5-file batch with
0 ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed for all 5 files.

**Evidence**: The stock-solution classification and sodium-carbonate solute
grounding pass. The `BUFFER` role has a DSMZ MediaDive technical-report
evidence object, and the per-record YAML agrees with the regenerated aggregate
row when keyed by `(preferred_term, mapping_status)`.

The final SSSOM row needs synonym cleanup. Row 2626 publishes `Na CO`,
`Na2CO`, `NaCO3`, `Na2CO3 anhydrous`, `Na2CO3(Baker 3604)`, and
`Na2CO3-CO2 buffer` in `other`; those are malformed formula fragments, a
hydrate-state note, a supplier-specific label, or a buffer system label rather
than same-substance sodium carbonate solution synonyms.

**Completeness**: The large occurrence count, source raw label, stock-solution
classification, and buffer role are enough for the active ingredient. The stale
`(adjust if required)` raw label remains contained in YAML and does not export.

**Recommended Edits**: Remove the malformed formula fragments,
supplier-specific label, and buffer-system label from
`data/ingredients/mapped/Sodium_Carbonate_Solution.yaml` or teach the SSSOM
builder to suppress them, then rebuild final SSSOM and confirm row 2626 exports
only true aliases.
