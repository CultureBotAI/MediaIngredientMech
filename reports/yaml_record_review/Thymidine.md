# `data/ingredients/mapped/Thymidine.yaml`

## Verdict

Pass. The exact CHEBI identity, exact synonyms, CAS RN, PubChem structure,
source occurrence count, aggregate row, and final SSSOM row for thymidine are
synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Thymidine.yaml`.
- Identifier and grounding: `identifier: CHEBI:17748` with the same
  `ontology_mapping.ontology_id`, label `thymidine`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS `50-89-5`, formula `C10H14N2O5`, and matching
  PubChem InChI/SMILES.
- Occurrences: 13 CultureMech recipe occurrences in 13 media.

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

- Local OAK resolves `CHEBI:17748` with canonical label `thymidine` and the
  exact and related synonyms stored on the record.
- Fresh PubChem lookup by CAS `50-89-5` resolves CID 5789, formula
  `C10H14N2O5`, and the same InChI as the curated record.
- The final SSSOM has exactly one exact row for `MIM:Thymidine`, points at
  `CHEBI:17748`, keeps the reviewed
  `OAK+OLS:chebi|CONFIRMED|2026-07-07` validation token, and publishes only
  the stored real thymidine synonyms plus `CAS:50-89-5` in `other`.

## Completeness

- The CHEBI identity, CAS RN, structure fields, occurrence count, aggregate
  copy, and final SSSOM row agree.
- No components, roles, or environmental contexts are asserted.
- An ignored/hidden search of the active local curated, mapping, generated,
  source, and report paths found the expected CultureMech import, OAK/OLS
  row-review, aggregate, and final SSSOM rows.

## Recommended Edits

- None.
