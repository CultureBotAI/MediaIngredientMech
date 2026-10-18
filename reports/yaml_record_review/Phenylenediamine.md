# `data/ingredients/mapped/Phenylenediamine.yaml`

## Verdict

Needs curation; major. The current `CHEBI:51402` mapping is the generic
phenylenediamine class, but the CultureBotHT source CAS `106-50-3` denotes the
specific para isomer and is exported in final SSSOM `other`.

## Identity

- Reviewed record: `data/ingredients/mapped/Phenylenediamine.yaml`.
- Identifier and grounding: `identifier: CHEBI:51402` with
  `ontology_mapping.ontology_id: CHEBI:51402`, label `phenylenediamine`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 MediaRecipe occurrences; this row was created from the
  CultureBotHT CAS table.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `CHEBI:51402` resolves `CHEBI:51402`
  `phenylenediamine`.
- A fresh OLS4 exact search for `p-phenylenediamine` resolves `CHEBI:51403`
  `1,4-phenylenediamine`.
- A fresh PubChem lookup for CAS `106-50-3` resolves p-Phenylenediamine, CID
  7814.
- The final SSSOM row was inspected directly and maps `MIM:Phenylenediamine`
  exactly to `CHEBI:51402`.

## Evidence

- `CHEBI:51402` is the broader phenylenediamine class, and its formula
  `C6H8N2` covers the ortho, meta, and para isomers.
- Major: CAS `106-50-3` identifies p-Phenylenediamine rather than the broader
  phenylenediamine class currently used as the primary mapping.
- Major: the final SSSOM row exports `CAS:106-50-3` in `other`, which turns the
  broad `CHEBI:51402` row into a synonym surface for the para isomer.

## Completeness

- The CultureBotHT row needs a curator decision about whether the maintained
  record should map to the para isomer `CHEBI:51403` or keep `CHEBI:51402` and
  drop the isomer-specific CAS provenance from exported synonyms.

## Recommended Edits

- Major: in `data/ingredients/mapped/Phenylenediamine.yaml`, either remap the
  CultureBotHT CAS import to `CHEBI:51403` if the source row truly denotes
  p-Phenylenediamine, or remove/retype `CAS:106-50-3` so final SSSOM no longer
  exports the para-isomer CAS on the generic `CHEBI:51402` mapping.
