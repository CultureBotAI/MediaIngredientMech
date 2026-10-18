# `data/ingredients/mapped/Thiostrepton.yaml`

## Verdict

Pass. The MicrobeDecoder exact match to `CHEBI:29693`, absorbed Bryamycin
alias, structure fields, aggregate row, and final SSSOM row for thiostrepton
are synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Thiostrepton.yaml`.
- Identifier and grounding: `identifier: CHEBI:29693` with the same
  `ontology_mapping.ontology_id`, label `thiostrepton`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Synonyms: raw MicrobeDecoder alias `Bryamycin`, merged from the unmapped
  duplicate because ChEBI lists `bryamycin` as a thiostrepton synonym.
- Chemical properties: formula `C72H85N19O18S5`, InChI, SMILES, and molecular
  weight from `ChEBI+PubChem`.
- Occurrences: zero CultureMech recipe occurrences, with 16 MicrobeDecoder
  BacDive source occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Thioridazine_Hydrochloride` through `Threonine`: exited 0 and wrote zero
  ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on the same 5-file
  batch with `conf/term-validator.yaml`: all five CHEBI rows passed.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Local OAK resolves `CHEBI:29693` with canonical label `thiostrepton` and
  related synonym `bryamycin`, supporting both the imported exact label and the
  absorbed Bryamycin duplicate.
- The stored formula and stereospecific InChI/SMILES are specific to the
  `CHEBI:29693` thiostrepton structure.
- The final SSSOM has exactly one exact row for `MIM:Thiostrepton`, points at
  `CHEBI:29693`, keeps the `manual:review-ingredients|APPROVED|2026-08-04`
  validation token, and publishes only `Bryamycin` in `other`.

## Completeness

- The exact CHEBI identity, Bryamycin alias, structure fields, aggregate copy,
  MicrobeDecoder source occurrences, and final SSSOM row agree.
- No components, roles, or environmental contexts are asserted.
- An ignored/hidden search of the active local curated, mapping, generated,
  source, and report paths found the expected MicrobeDecoder import, Bryamycin
  merge, aggregate, and final SSSOM rows.

## Recommended Edits

- None.
