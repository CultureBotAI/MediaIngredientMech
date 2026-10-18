# `data/ingredients/mapped/Pinene.yaml`

## Verdict

Needs curation; major. The primary CHEBI target is the generic `CHEBI:17187`
pinene class, but the CultureBotHT CAS and final SSSOM `other` synonym are
specific to alpha-pinene.

## Identity

- Reviewed record: `data/ingredients/mapped/Pinene.yaml`.
- Identifier and grounding: `identifier: CHEBI:17187` with
  `ontology_mapping.ontology_id: CHEBI:17187`, label `pinene`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 MediaRecipe occurrences; this row was created from the
  CultureBotHT CAS table.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `CHEBI:17187` resolves the generic CHEBI
  `pinene` class.
- A fresh OLS4 exact search for `alpha-Pinene` resolves the narrower
  `CHEBI:36740` `alpha-pinene` class, with separate CHEBI terms for its (+) and
  (-) enantiomers.
- A fresh PubChem lookup for CAS `80-56-8` resolves to CID 6654,
  `(+-)-alpha-Pinene`.
- The final SSSOM row was inspected directly and maps `MIM:Pinene` exactly to
  `CHEBI:17187`.

## Evidence

- Major: `CAS:80-56-8` identifies alpha-pinene, but the curated mapping target
  is the broader `CHEBI:17187` pinene class.
- Major: the final SSSOM row exports `alpha-Pinene|CAS:80-56-8` in `other`,
  so an exact row for generic pinene presents alpha-pinene-specific identifiers
  as exact synonyms.

## Completeness

- The CultureBotHT row needs a curator decision about whether the maintained
  record should map to `CHEBI:36740` alpha-pinene or keep generic
  `CHEBI:17187` and drop the alpha-pinene-specific CAS and synonym from final
  `other`.

## Recommended Edits

- Major: in `data/ingredients/mapped/Pinene.yaml`, either remap the CultureBotHT
  CAS import to `CHEBI:36740` if the source row truly denotes alpha-pinene, or
  remove/retype `alpha-Pinene` and `CAS:80-56-8` so final SSSOM no longer
  exports alpha-pinene-specific terms on the generic `CHEBI:17187` mapping.
