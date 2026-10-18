# `data/ingredients/mapped/Thiourea.yaml`

## Verdict

Pass. The exact CHEBI identity, CAS RN, PubChem structure, aggregate row, and
final SSSOM row for thiourea are synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Thiourea.yaml`.
- Identifier and grounding: `identifier: CHEBI:36946` with the same
  `ontology_mapping.ontology_id`, label `thiourea`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS `62-56-6`, formula `CH4N2S`, and matching PubChem
  InChI/SMILES.
- Occurrences: zero CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Thioridazine_Hydrochloride` through `Threonine`: exited 0 and wrote zero
  ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on the same 5-file
  batch with `conf/term-validator.yaml`: all five CHEBI rows passed.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Local OAK resolves `CHEBI:36946` with canonical label `thiourea` and exact
  `Thiourea` synonyms.
- Fresh PubChem lookup by CAS `62-56-6` resolves CID 2723790, formula
  `CH4N2S`, and the same InChI as the curated record.
- The final SSSOM has exactly one exact row for `MIM:Thiourea`, points at
  `CHEBI:36946`, keeps the reviewed
  `OAK+OLS:chebi|CONFIRMED|2026-07-07` validation token, and publishes only
  `CAS:62-56-6` in `other`.

## Completeness

- The exact CHEBI identity, CAS RN, structure fields, aggregate copy, and final
  SSSOM row agree.
- No components, roles, synonyms, or environmental contexts are asserted.
- An ignored/hidden search of the active local curated, mapping, generated,
  source, and report paths found the expected CultureBotHT import, OAK/OLS
  row-review, aggregate, and final SSSOM rows.

## Recommended Edits

- None.
