# `data/ingredients/mapped/Theaflavin.yaml`

## Verdict

Pass. The exact CHEBI identity, exact synonym, structure fields, aggregate row,
and final SSSOM row for theaflavin are synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Theaflavin.yaml`.
- Identifier and grounding: `identifier: CHEBI:136609` with the same
  `ontology_mapping.ontology_id`, label `theaflavin`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Synonyms: one exact ChEBI synonym for the structure represented by
  `CHEBI:136609`.
- Chemical properties: formula `C29H24O12`, InChI, and SMILES from the local
  ChEBI sqlite adapter.
- Occurrences: zero CultureMech recipe occurrences.

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

- Local OAK resolves `CHEBI:136609` with canonical label `theaflavin` and the
  stored exact systematic synonym.
- The stored `C29H24O12` formula and stereospecific InChI/SMILES match
  `CHEBI:136609`.
- The final SSSOM has exactly one exact row for `MIM:Theaflavin`, points at
  `CHEBI:136609`, keeps the reviewed
  `OAK+OLS:chebi|CONFIRMED|2026-07-07` validation token, and publishes only
  the exact ChEBI synonym in `other`.

## Completeness

- The exact CHEBI identity, exact synonym, structure fields, aggregate copy,
  and final SSSOM row agree.
- No components, roles, or environmental contexts are asserted.
- An ignored/hidden search of the active local curated, mapping, generated,
  source, and report paths found the expected CultureBotHT import, OAK/OLS
  row-review, aggregate, and final SSSOM rows.

## Recommended Edits

- None.
