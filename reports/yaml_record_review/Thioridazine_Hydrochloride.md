# `data/ingredients/mapped/Thioridazine_Hydrochloride.yaml`

## Verdict

Pass. The exact CHEBI identity, exact synonym, CAS RN, PubChem structure,
aggregate row, and final SSSOM row for thioridazine hydrochloride are
synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Thioridazine_Hydrochloride.yaml`.
- Identifier and grounding: `identifier: CHEBI:48566` with the same
  `ontology_mapping.ontology_id`, label `thioridazine hydrochloride`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Synonyms: one exact ChEBI synonym for thioridazine hydrochloride.
- Chemical properties: CAS `130-61-0`, formula `C21H26N2S2.HCl`, and matching
  PubChem InChI/SMILES.
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

- Local OAK resolves `CHEBI:48566` with canonical label
  `thioridazine hydrochloride` and the stored exact systematic synonym.
- Fresh PubChem lookup by CAS `130-61-0` resolves CID 66062, formula
  `C21H27ClN2S2`, and the same InChI as the curated record.
- The final SSSOM has exactly one exact row for
  `MIM:Thioridazine_Hydrochloride`, points at `CHEBI:48566`, keeps the
  reviewed `OAK+OLS:chebi|CONFIRMED|2026-07-07` validation token, and
  publishes only the exact ChEBI synonym plus `CAS:130-61-0` in `other`.

## Completeness

- The exact CHEBI identity, exact synonym, CAS RN, structure fields, aggregate
  copy, and final SSSOM row agree.
- No components, roles, or environmental contexts are asserted.
- An ignored/hidden search of the active local curated, mapping, generated,
  source, and report paths found the expected CultureBotHT import, OAK/OLS
  row-review, aggregate, and final SSSOM rows.

## Recommended Edits

- None.
