# `data/ingredients/mapped/Thallium_I_Acetate.yaml`

## Verdict

Pass. The exact CHEBI identity, exact and raw CultureMech synonyms, CAS RN,
PubChem structure, aggregate row, and final SSSOM row for thallium(I) acetate
are synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Thallium_I_Acetate.yaml`.
- Identifier and grounding: `identifier: CHEBI:75192` with the same
  `ontology_mapping.ontology_id`, label `thallium(I) acetate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Synonyms: exact ChEBI synonym `thallium(1+) acetate` plus the CultureMech raw
  surface form `Thallium acetate`.
- Chemical properties: CAS `563-68-8`, formula `C2H3O2.Tl`, and matching
  PubChem InChI/SMILES for thallium(I) acetate.
- Occurrences: zero CultureMech recipe occurrences after the CultureMech raw
  synonym was folded into this mapped record.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tetrodotoxin` through `Thauers_Vitamin_Mix_No_Biotin`: exited 0 and wrote
  zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on the CHEBI subset
  from this batch: `Tetrodotoxin`, `Texazone`, and `Thallium_I_Acetate` all
  passed. The two local `kgmicrobe.ingredient` stock rows were skipped because
  their exact local registry CURIEs are intentionally outside the OBO
  term-validator subset.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Local OAK resolves `CHEBI:75192` with canonical label
  `thallium(I) acetate`, exact synonym `thallium(1+) acetate`, and related
  synonym `Thallium acetate`.
- Fresh PubChem lookup by CAS `563-68-8` resolves CID 11247, formula
  `C2H3O2Tl`, and the same InChI/SMILES as the curated record.
- The final SSSOM has exactly one exact row for `MIM:Thallium_I_Acetate`,
  points at `CHEBI:75192`, keeps the reviewed
  `OAK+OLS:chebi|CONFIRMED|2026-07-07` validation token, and publishes only
  `thallium(1+) acetate`, `Thallium acetate`, and `CAS:563-68-8` in `other`.

## Completeness

- The exact CHEBI identity, CAS RN, exact synonym, CultureMech surface alias,
  aggregate copy, and final SSSOM row agree.
- No components, roles, or environmental contexts are asserted.
- An ignored/hidden search of the active local curated, mapping, generated,
  source, and report paths found the expected CultureBotHT import,
  CultureMech alias backfill, aggregate, and final SSSOM rows.

## Recommended Edits

- None.
