# `data/ingredients/mapped/Sodium_Phosphate_Dibasic.yaml`

## Verdict

Needs curation - blocker. The `Sodium phosphate dibasic` source label is exact
mapped to `CHEBI:37583` trisodium phosphate and carries a
`Sodium dihydrogen phosphate` synonym, so the record conflates disodium,
trisodium, and monosodium phosphate identities. Its `BUFFER` role is also
provisional.

## Identity

- Reviewed record: `data/ingredients/mapped/Sodium_Phosphate_Dibasic.yaml`.
- Current grounding: `identifier: CHEBI:37583` with
  `ontology_mapping.ontology_id: CHEBI:37583`, label `trisodium phosphate`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 33 source occurrences across 33 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sodium_Phosphate_Dibasic` through `Sodium_Pyrophosphate_Dibasic`: exited 0
  and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record; this confirms the stored label matches the stored wrong ChEBI ID.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh EBI OLS4 lookup resolves active `CHEBI:37583` as
  `trisodium phosphate`, with CAS `7601-54-9` and a `sodium phosphate,
  tribasic` synonym.
- Fresh PubChem lookup for `Sodium phosphate dibasic` resolves to
  `HNa2O4P`, the disodium salt, not the trisodium `3Na.O4P` structure stored
  here.
- Fresh PubChem lookup for `Sodium dihydrogen phosphate` resolves to
  monosodium phosphate, so the active synonym recovered in #520 is also not a
  synonym of `Sodium phosphate dibasic`.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports` found the wrong `Sodium dihydrogen phosphate` token
  in this active YAML, its aggregate copy, and the final SSSOM `other` column.
- Major: `physicochemical_roles.BUFFER` is backed only by an in-session
  `COMPUTATIONAL_PREDICTION` with no external evidence and a
  `review recommended` note.

## Completeness

- The final SSSOM exact row currently publishes the wrong trisodium ChEBI
  target and the wrong monosodium `other` synonym.
- The occurrence count is current, but the identity, formula, structure, final
  row, and role need to be rechecked after regrounding.

## Recommended Edits

- Blocker: reground `data/ingredients/mapped/Sodium_Phosphate_Dibasic.yaml` to
  a disodium phosphate identity, using an exact ontology term if one resolves
  and otherwise a CAS or kg-microbe registry identity.
- Blocker: remove the active `Sodium dihydrogen phosphate` synonym and rebuild
  final SSSOM so `MIM:Sodium_Phosphate_Dibasic` stops publishing it in `other`.
- Major: remove `physicochemical_roles.BUFFER` unless a checked source supports
  the buffer role for the regrounded record.
