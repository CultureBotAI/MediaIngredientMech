# `data/ingredients/mapped/Thymine.yaml`

## Verdict

Pass. The exact CHEBI identity, exact synonyms, CAS RN, PubChem structure,
source occurrence count, aggregate row, and final SSSOM row for thymine are
synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Thymine.yaml`.
- Identifier and grounding: `identifier: CHEBI:17821` with the same
  `ontology_mapping.ontology_id`, label `thymine`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS `65-71-4`, formula `C5H6N2O2`, and matching
  PubChem InChI/SMILES.
- Occurrences: 33 CultureMech recipe occurrences in 33 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Thymidine` through `Tiamulin`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on the CHEBI subset
  from this batch: `Thymidine`, `Thymine`, `Thymoquinone`, and `Tiamulin` all
  passed. The `TiCl3` MeSH row was skipped because `mesh:C039460` is outside
  the CHEBI-focused OBO term-validator subset.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Local OAK resolves `CHEBI:17821` with canonical label `thymine` and the exact
  and related synonyms stored on the record.
- Fresh PubChem lookup by CAS `65-71-4` resolves CID 1135, formula
  `C5H6N2O2`, and the same InChI as the curated record.
- The final SSSOM has exactly one exact row for `MIM:Thymine`, points at
  `CHEBI:17821`, keeps the reviewed
  `OAK+OLS:chebi|CONFIRMED|2026-07-07` validation token, and publishes only
  the stored real thymine synonyms plus `CAS:65-71-4` in `other`.

## Completeness

- The CHEBI identity, CAS RN, structure fields, occurrence count, aggregate
  copy, and final SSSOM row agree.
- No components, roles, or environmental contexts are asserted.
- An ignored/hidden search of the active local curated, mapping, generated,
  source, and report paths found the expected CultureMech import, OAK/OLS
  row-review, aggregate, and final SSSOM rows.

## Recommended Edits

- None.
