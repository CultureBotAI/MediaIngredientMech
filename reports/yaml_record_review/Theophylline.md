# `data/ingredients/mapped/Theophylline.yaml`

## Verdict

Pass. The exact CHEBI identity, exact synonym, CAS RN, PubChem structure,
aggregate row, and final SSSOM row for theophylline are synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Theophylline.yaml`.
- Identifier and grounding: `identifier: CHEBI:28177` with the same
  `ontology_mapping.ontology_id`, label `theophylline`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Synonyms: one exact ChEBI synonym,
  `1,3-dimethyl-3,7-dihydro-1H-purine-2,6-dione`.
- Chemical properties: CAS `58-55-9`, formula `C7H8N4O2`, and matching PubChem
  InChI/SMILES.
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

- Local OAK resolves `CHEBI:28177` with canonical label `theophylline` and the
  stored exact ChEBI synonym.
- Fresh PubChem lookup by CAS `58-55-9` resolves CID 2153, formula `C7H8N4O2`,
  and the same InChI as the curated record.
- The final SSSOM has exactly one exact row for `MIM:Theophylline`, points at
  `CHEBI:28177`, keeps the reviewed
  `OAK+OLS:chebi|CONFIRMED|2026-07-07` validation token, and publishes only
  the exact ChEBI synonym plus `CAS:58-55-9` in `other`.

## Completeness

- The exact CHEBI identity, exact synonym, CAS RN, structure fields, aggregate
  copy, and final SSSOM row agree.
- No components, roles, or environmental contexts are asserted.
- An ignored/hidden search of the active local curated, mapping, generated,
  source, and report paths found the expected CultureBotHT import, OAK/OLS
  row-review, aggregate, and final SSSOM rows.

## Recommended Edits

- None.
