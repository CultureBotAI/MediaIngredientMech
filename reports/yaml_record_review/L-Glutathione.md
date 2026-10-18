# `data/ingredients/mapped/L-Glutathione.yaml`

## Verdict

Pass with minor issues. The record is a rejected tombstone for the active
`Glutathione` record on the same ChEBI identifier, and the final SSSOM
correctly omits `MIM:L-Glutathione`, but stale notes still say the old
unmapped import needed curator review.

## Identity

- Reviewed record: `data/ingredients/mapped/L-Glutathione.yaml`.
- Identifier and grounding: `identifier: CHEBI:16856` with
  `ontology_mapping.ontology_id: CHEBI:16856`, label `glutathione`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: REJECTED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Rejection state: this is a tombstone merged into
  `data/ingredients/mapped/Glutathione.yaml`, which also uses `CHEBI:16856`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-Cysteine_X_HCl_X_H2O_Solution.yaml data/ingredients/mapped/L-Deoxyalliin.yaml data/ingredients/mapped/L-Galactose.yaml data/ingredients/mapped/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.yaml data/ingredients/mapped/L-Glutathione.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 records.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_yjzjKv`:
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_yjzjKv`:
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- EBI OLS4 resolves `CHEBI:16856` as active `glutathione` and lists
  `L-gamma-glutamyl-L-cysteinylglycine` as a synonym, matching the tombstoned
  ontology mapping.
- The active `Glutathione` record contains the same `CHEBI:16856` identifier
  and records that it absorbed `CHEBI:16856` `L-Glutathione`; the duplicate
  tombstone records `MERGED_INTO` with `new_status: REJECTED`.
- Hidden and ignored-inclusive search found no `MIM:L-Glutathione` row in
  `mappings/ingredient_mappings.sssom.tsv`. The final SSSOM instead publishes
  `MIM:Glutathione` to `CHEBI:16856` with `L-Glutathione` retained as an
  active-record synonym.
- Minor: `notes` still carries the original import text claiming there was no
  CAS RN or CHEBI/NCIT match and that curator review was needed, which no
  longer describes this rejected same-substance tombstone.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current tombstone, its active merge
  target, and the active target's final SSSOM row.

## Completeness

- The rejection status, merge history, zero occurrence count, duplicate active
  target, and final SSSOM omission are present and consistent.
- The tombstone is complete enough for publication because it no longer
  contributes a final SSSOM row.

## Recommended Edits

- Minor: refresh `notes` in `data/ingredients/mapped/L-Glutathione.yaml` to
  state that this duplicate was merged into `Glutathione`.
- Rerun strict and round-trip validation after the note cleanup.
