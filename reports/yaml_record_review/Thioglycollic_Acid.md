# `data/ingredients/mapped/Thioglycollic_Acid.yaml`

## Verdict

Pass. The promoted exact spelling-variant match to `CHEBI:30065`, structure
fields, occurrence count, aggregate row, and final SSSOM row for thioglycolic
acid are synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Thioglycollic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:30065` with the same
  `ontology_mapping.ontology_id`, label `thioglycolic acid`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `C2H4O2S`, InChI, SMILES, and molecular weight
  from `ChEBI+PubChem`.
- Occurrences: three CultureMech recipe occurrences in three media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Thiamine_pyrophosphate` through `Thiolutin`: exited 0 and wrote zero ERROR
  rows.
- `uv run --frozen linkml-term-validator validate-data` on the same 5-file
  batch with `conf/term-validator.yaml`: all five CHEBI rows passed.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Local OAK resolves `CHEBI:30065` with canonical label `thioglycolic acid`,
  supporting the `Thioglycollic acid` spelling variant promoted from the
  mim-queue unmapped record.
- The stored `C2H4O2S` formula and neutral InChI/SMILES match thioglycolic
  acid rather than the separate thioglycolate anion or sodium thioglycolate
  salt records.
- The final SSSOM has exactly one exact row for `MIM:Thioglycollic_Acid`,
  points at `CHEBI:30065`, keeps the reviewed
  `OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07` validation token, and leaves
  `other` empty.

## Completeness

- The exact CHEBI identity, acid structure fields, aggregate copy, occurrence
  count, and final SSSOM row agree.
- No components, roles, synonyms, or environmental contexts are asserted.
- An ignored/hidden search of the active local curated, mapping, generated,
  source, and report paths found the expected mim-queue import, promotion,
  aggregate, and final SSSOM rows.

## Recommended Edits

- None.
