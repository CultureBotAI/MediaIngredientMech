# `data/ingredients/mapped/Texazone.yaml`

## Verdict

Pass. The MicrobeDecoder exact match to `CHEBI:197442`, ChEBI/PubChem
structure fields, aggregate row, and final SSSOM row for texazone are
synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Texazone.yaml`.
- Identifier and grounding: `identifier: CHEBI:197442` with the same
  `ontology_mapping.ontology_id`, label `texazone`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `C14H10N2O4`, InChI, SMILES, and molecular
  weight from `ChEBI+PubChem`.
- Occurrences: zero CultureMech recipe occurrences, with one MicrobeDecoder
  `BacDive_Metabolite_production` source occurrence.

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

- Local OAK resolves `CHEBI:197442` with canonical label `texazone`, supporting
  the imported MicrobeDecoder exact-label match.
- The stored `C14H10N2O4` formula and phenoxazine carboxylic-acid
  InChI/SMILES are specific to the texazone record.
- The final SSSOM has exactly one exact row for `MIM:Texazone`, points at
  `CHEBI:197442`, keeps the `manual:review-ingredients|APPROVED|2026-08-04`
  validation token, and leaves `other` empty.

## Completeness

- The exact CHEBI identity, structure fields, aggregate copy, MicrobeDecoder
  source occurrence, and final SSSOM row agree.
- No components, roles, synonyms, or environmental contexts are asserted.
- An ignored/hidden search of the active local curated, mapping, generated,
  source, and report paths found the expected MicrobeDecoder review, aggregate,
  and final SSSOM rows.

## Recommended Edits

- None.
