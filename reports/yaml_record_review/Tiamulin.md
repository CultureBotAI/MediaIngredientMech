# `data/ingredients/mapped/Tiamulin.yaml`

## Verdict

Pass. The exact CHEBI identity, exact synonym, CAS RN, PubChem structure,
aggregate row, and final SSSOM row for tiamulin are synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Tiamulin.yaml`.
- Identifier and grounding: `identifier: CHEBI:44137` with the same
  `ontology_mapping.ontology_id`, label `tiamulin`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Synonyms: one exact ChEBI synonym for tiamulin.
- Chemical properties: CAS `55297-95-5`, formula `C28H47NO4S`, and matching
  PubChem InChI/SMILES.
- Occurrences: zero CultureMech recipe occurrences.

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

- Local OAK resolves `CHEBI:44137` with canonical label `tiamulin` and the
  stored exact ChEBI synonym.
- Fresh PubChem lookup by CAS `55297-95-5` resolves CID 656958, formula
  `C28H47NO4S`, and the same InChI as the curated record.
- The final SSSOM has exactly one exact row for `MIM:Tiamulin`, points at
  `CHEBI:44137`, keeps the reviewed
  `OAK+OLS:chebi|CONFIRMED|2026-07-07` validation token, and publishes only
  the exact ChEBI synonym plus `CAS:55297-95-5` in `other`.

## Completeness

- The exact CHEBI identity, exact synonym, CAS RN, structure fields, aggregate
  copy, and final SSSOM row agree.
- No components, roles, or environmental contexts are asserted.
- An ignored/hidden search of the active local curated, mapping, generated,
  source, and report paths found the expected CultureBotHT import, OAK/OLS
  row-review, aggregate, and final SSSOM rows.

## Recommended Edits

- None.
