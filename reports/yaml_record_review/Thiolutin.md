# `data/ingredients/mapped/Thiolutin.yaml`

## Verdict

Pass. The MicrobeDecoder exact match to `CHEBI:156450`, structure fields,
aggregate row, and final SSSOM row for thiolutin are synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Thiolutin.yaml`.
- Identifier and grounding: `identifier: CHEBI:156450` with the same
  `ontology_mapping.ontology_id`, label `thiolutin`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `C8H8N2O2S2`, InChI, SMILES, and molecular
  weight from `ChEBI+PubChem`.
- Occurrences: zero CultureMech recipe occurrences, with two MicrobeDecoder
  `BacDive_Metabolite_production` source occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Thiamine_pyrophosphate` through `Thiolutin`: exited 0 and wrote zero ERROR
  rows.
- `uv run --frozen linkml-term-validator validate-data` on the same 5-file
  batch with `conf/term-validator.yaml`: all five CHEBI rows passed.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Local OAK resolves `CHEBI:156450` with canonical label `thiolutin`,
  supporting the imported MicrobeDecoder exact-label match.
- The stored `C8H8N2O2S2` formula and InChI/SMILES are specific to the
  thiolutin record.
- The final SSSOM has exactly one exact row for `MIM:Thiolutin`, points at
  `CHEBI:156450`, keeps the
  `manual:review-ingredients|APPROVED|2026-08-04` validation token, and leaves
  `other` empty.

## Completeness

- The exact CHEBI identity, structure fields, aggregate copy, MicrobeDecoder
  source occurrence, and final SSSOM row agree.
- No components, roles, synonyms, or environmental contexts are asserted.
- An ignored/hidden search of the active local curated, mapping, generated,
  source, and report paths found the expected MicrobeDecoder review, aggregate,
  and final SSSOM rows.

## Recommended Edits

- None.
