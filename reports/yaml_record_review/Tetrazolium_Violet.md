# `data/ingredients/mapped/Tetrazolium_Violet.yaml`

## Verdict

Pass. The exact CHEBI identity, exact synonym, CAS RN, PubChem structure,
aggregate row, and final SSSOM row for tetrazolium violet are synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Tetrazolium_Violet.yaml`.
- Identifier and grounding: `identifier: CHEBI:75193` with the same
  `ontology_mapping.ontology_id`, label `tetrazolium violet`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Synonyms: one exact ChEBI synonym,
  `3-(1-naphthyl)-2,5-diphenyl-2H-tetrazol-3-ium chloride`.
- Chemical properties: CAS `1719-71-7`, formula `C23H17N4.Cl`, and matching
  PubChem InChI/SMILES for tetrazolium violet chloride.
- Occurrences: zero CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tetrandrine` through `Tetrazolium_Violet`: exited 0 and wrote zero ERROR
  rows.
- `uv run --frozen linkml-term-validator validate-data` on the same 5-file
  batch with `conf/term-validator.yaml`: all five CHEBI rows passed.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Local OAK resolves `CHEBI:75193` with canonical label `tetrazolium violet`
  and exact synonym
  `3-(1-naphthyl)-2,5-diphenyl-2H-tetrazol-3-ium chloride`.
- Fresh exact OLS4 search for `Tetrazolium violet` returns active
  `CHEBI:75193` and the narrower sibling cation `CHEBI:75197`; the record maps
  to the chloride salt, which matches the CAS-bearing MIM subject.
- Fresh PubChem lookup by CAS `1719-71-7` resolves CID 74395, formula
  `C23H17ClN4`, and the same InChI as the curated record.
- The final SSSOM has exactly one exact row for `MIM:Tetrazolium_Violet`,
  points at `CHEBI:75193`, keeps the reviewed
  `OAK+OLS:chebi|CONFIRMED|2026-07-07` validation token, and publishes only
  the exact ChEBI synonym plus `CAS:1719-71-7` in `other`.

## Completeness

- The exact CHEBI identity, exact synonym, CAS RN, structure fields, aggregate
  copy, and final SSSOM row agree.
- No components, roles, or environmental contexts are asserted.
- An ignored/hidden search of the active local curated, mapping, generated,
  source, and report paths found the expected CultureBotHT, OAK/OLS row-review,
  aggregate, and final SSSOM rows.

## Recommended Edits

- None.
