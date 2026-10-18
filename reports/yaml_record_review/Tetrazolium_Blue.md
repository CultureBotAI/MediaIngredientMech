# `data/ingredients/mapped/Tetrazolium_Blue.yaml`

## Verdict

Pass. The MicrobeDecoder exact match to `CHEBI:75198`, structure fields,
aggregate row, and final SSSOM row for tetrazolium blue are synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Tetrazolium_Blue.yaml`.
- Identifier and grounding: `identifier: CHEBI:75198` with the same
  `ontology_mapping.ontology_id`, label `tetrazolium blue`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `C40H32N8O2.2Cl`, InChI, SMILES, and molecular
  weight from `ChEBI+PubChem`.
- Occurrences: zero CultureMech recipe occurrences, with 17 MicrobeDecoder
  BacDive antibiotic source occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tetrandrine` through `Tetrazolium_Violet`: exited 0 and wrote zero ERROR
  rows.
- `uv run --frozen linkml-term-validator validate-data` on the same 5-file
  batch with `conf/term-validator.yaml`: all five CHEBI rows passed.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Local OAK resolves `CHEBI:75198` with canonical label `tetrazolium blue` and
  exact systematic synonym
  `3,3'-(3,3'-dimethoxybiphenyl-4,4'-diyl)bis(2,5-diphenyl-2H-tetrazol-3-ium) dichloride`,
  supporting the imported exact label.
- The stored formula and two-chloride InChI/SMILES are specific to the
  ditetrazolium chloride salt represented by `CHEBI:75198`.
- The final SSSOM has exactly one exact row for `MIM:Tetrazolium_Blue`, points
  at `CHEBI:75198`, keeps the
  `manual:review-ingredients|APPROVED|2026-08-04` validation token, and leaves
  `other` empty.

## Completeness

- The exact CHEBI identity, structure fields, aggregate copy, MicrobeDecoder
  occurrence, and final SSSOM row agree.
- No components, roles, synonyms, or environmental contexts are asserted.
- An ignored/hidden search of the active local curated, mapping, generated,
  source, and report paths found the expected MicrobeDecoder review, aggregate,
  and final SSSOM rows.

## Recommended Edits

- None.
