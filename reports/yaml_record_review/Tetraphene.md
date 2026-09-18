# `data/ingredients/mapped/Tetraphene.yaml`

## Verdict

Pass. The MicrobeDecoder exact match to `CHEBI:51348`, ChEBI structure fields,
aggregate row, and final SSSOM row for tetraphene are synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Tetraphene.yaml`.
- Identifier and grounding: `identifier: CHEBI:51348` with the same
  `ontology_mapping.ontology_id`, label `tetraphene`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `C18H12`, InChI, SMILES, and molecular weight
  from `ChEBI+PubChem`.
- Occurrences: zero CultureMech recipe occurrences, with one MicrobeDecoder
  `BacDive_Metabolite_utilization` source occurrence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tetrandrine` through `Tetrazolium_Violet`: exited 0 and wrote zero ERROR
  rows.
- `uv run --frozen linkml-term-validator validate-data` on the same 5-file
  batch with `conf/term-validator.yaml`: all five CHEBI rows passed.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Local OAK aliases for `CHEBI:51348` include the canonical label and exact
  synonym `tetraphene`, supporting the MicrobeDecoder
  `ols-label-exact-chebi` import and review-ingredients promotion.
- The stored `C18H12` formula and aromatic InChI/SMILES are specific to
  `CHEBI:51348`.
- The final SSSOM has exactly one exact row for `MIM:Tetraphene`, points at
  `CHEBI:51348`, keeps the `manual:review-ingredients|APPROVED|2026-08-04`
  validation token, and leaves `other` empty.

## Completeness

- The exact CHEBI identity, structure fields, aggregate copy, MicrobeDecoder
  occurrence, and final SSSOM row agree.
- No components, roles, synonyms, or environmental contexts are asserted.
- An ignored/hidden search of the active local curated, mapping, generated,
  source, and report paths found the expected MicrobeDecoder review, aggregate,
  and final SSSOM rows.

## Recommended Edits

- None.
