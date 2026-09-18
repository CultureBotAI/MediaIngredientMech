# `data/ingredients/mapped/Tetrathionate.yaml`

## Verdict

Pass. The promoted synonym match to `CHEBI:15226`, structure fields, occurrence
statistics, aggregate row, and final SSSOM row for tetrathionate are
synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Tetrathionate.yaml`.
- Identifier and grounding: `identifier: CHEBI:15226` with the same
  `ontology_mapping.ontology_id`, label `tetrathionate(2-)`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `O6S4`, InChI, SMILES, and molecular weight from
  `ChEBI+PubChem`.
- Occurrences: one CultureMech recipe occurrence in one medium, plus 23
  MicrobeDecoder `BacDive_Metabolite_utilization` source occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tetrandrine` through `Tetrazolium_Violet`: exited 0 and wrote zero ERROR
  rows.
- `uv run --frozen linkml-term-validator validate-data` on the same 5-file
  batch with `conf/term-validator.yaml`: all five CHEBI rows passed.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Local OAK aliases for `CHEBI:15226` include canonical label
  `tetrathionate(2-)` and related synonyms `Tetrathionate` and `tetrathionate`,
  supporting the promoted MicrobeDecoder source surface.
- The stored `O6S4` formula and anionic InChI/SMILES match tetrathionate(2-),
  not the sodium or potassium tetrathionate salts tracked in sibling records.
- The final SSSOM has exactly one exact row for `MIM:Tetrathionate`, points at
  `CHEBI:15226`, keeps the
  `manual:promote_resolved_unmapped|PROMOTED|2026-08-05` validation token, and
  leaves `other` empty.

## Completeness

- The CHEBI synonym match, raw MicrobeDecoder source synonym, aggregate copy,
  occurrence counts, and final SSSOM row agree.
- No components, roles, or environmental contexts are asserted.
- An ignored/hidden search of the active local curated, mapping, generated,
  source, and report paths found the expected MicrobeDecoder import, aggregate,
  and final SSSOM rows. The search also found the intentionally separate
  `Na-tetrathionate` unmapped sodium-salt record and the already reviewed
  `K2S4O6` potassium-salt record.

## Recommended Edits

- None.
