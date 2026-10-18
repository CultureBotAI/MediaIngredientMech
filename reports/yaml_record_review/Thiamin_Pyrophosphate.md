# `data/ingredients/mapped/Thiamin_Pyrophosphate.yaml`

## Verdict

Needs curation. The synonym match to `CHEBI:45931`, CAS RN, structure fields,
occurrence counts, aggregate row, and final SSSOM row pass, but the
`VITAMIN_SOURCE` role is still only a provisional ChEBI-ancestry computational
prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Thiamin_Pyrophosphate.yaml`.
- Identifier and grounding: `identifier: CHEBI:45931` with the same
  `ontology_mapping.ontology_id`, label `thiamine(1+) diphosphate(1-)`, source
  `CHEBI`, `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Synonyms: one exact ChEBI synonym for thiamine(1+) diphosphate(1-).
- Chemical properties: CAS `136-09-4`, formula `C12H18N4O7P2S`, and matching
  PubChem InChI/SMILES.
- Occurrences: two CultureMech recipe occurrences in two media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Theaflavin` through `Thiamin_Pyrophosphate`: exited 0 and wrote zero ERROR
  rows.
- `uv run --frozen linkml-term-validator validate-data` on the CHEBI-primary
  subset from this batch: `Theaflavin`, `Theobromine`, `Theophylline`, and
  `Thiamin_Pyrophosphate` all passed. The CAS-primary
  `Theaflavin_Digallate` row was skipped because its registry identifier is
  intentionally outside the OBO term-validator subset.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Local OAK resolves `CHEBI:45931` with canonical label
  `thiamine(1+) diphosphate(1-)` and related synonym
  `thiamin pyrophosphate`, supporting the current synonym-match grade.
- Fresh PubChem lookup by CAS `136-09-4` resolves CID 5431, formula
  `C12H18N4O7P2S`, and the same InChI as the curated record.
- The final SSSOM has exactly one exact row for `MIM:Thiamin_Pyrophosphate`,
  points at `CHEBI:45931`, keeps the reviewed
  `OAK+OLS:chebi|CONFIRMED|2026-07-07` validation token, and publishes only
  the exact ChEBI synonym plus `CAS:136-09-4` in `other`.
- Major: `nutritional_roles.VITAMIN_SOURCE` has only
  `reference_type: COMPUTATIONAL_PREDICTION` evidence inferred from ChEBI
  ancestry and the curator note explicitly marks the role as provisional.

## Completeness

- The CHEBI identity, CAS RN, structure fields, aggregate copy, occurrence
  count, and final SSSOM row agree.
- No components or environmental contexts are asserted.
- An ignored/hidden search of the active local curated, mapping, generated,
  source, and report paths found the expected CultureMech import, OAK/OLS
  row-review, aggregate, and final SSSOM rows. It also found the intentionally
  separate `Thiamine_pyrophosphate` record, whose final row points at a
  different ChEBI subject and does not shadow this active record.

## Recommended Edits

- Major: in `data/ingredients/mapped/Thiamin_Pyrophosphate.yaml`, either verify
  `VITAMIN_SOURCE` against an inspected database or literature source and
  replace the provisional `COMPUTATIONAL_PREDICTION`, or remove the role. Then
  rerun strict validation, term validation, SSSOM publication, and
  `scripts/validate_sssom_invariants.py`.
