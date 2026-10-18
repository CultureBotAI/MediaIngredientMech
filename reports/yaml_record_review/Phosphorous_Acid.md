# `data/ingredients/mapped/Phosphorous_Acid.yaml`

## Verdict

Needs curation; major. The CultureBotHT identity maps exactly to active
`CHEBI:36361` phosphorous acid and the local CHEBI synonyms are valid, but
final SSSOM `other` also exports a sodium-phosphite hydrate/salt label from a
separate CAS record.

## Identity

- Reviewed record: `data/ingredients/mapped/Phosphorous_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:36361` with
  `ontology_mapping.ontology_id: CHEBI:36361`, label `phosphorous acid`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 MediaRecipe occurrences; this row was created from the
  CultureBotHT CAS table.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `phosphorous acid` returns active
  `CHEBI:36361` `phosphorous acid` with the three exported CHEBI exact
  synonyms on the same term.
- A fresh PubChem lookup for CAS `13598-36-2` resolves to a compound CID.
- The final SSSOM row was inspected directly and maps `MIM:Phosphorous_Acid`
  exactly to `CHEBI:36361`.

## Evidence

- The CHEBI primary identifier, mapping target, CAS `13598-36-2`, structured
  formula, SMILES, and InChI all describe phosphorous acid.
- The local exact synonyms `trihydrogen trioxophosphate(3-)`,
  `trihydroxidophosphorus`, and `trioxophosphoric(3-) acid` are exact synonyms
  on the current CHEBI term.
- Major: the final SSSOM row exports `Sodium phosphite dibasic pentahydrate`
  in `other`, but `data/ingredients/mapped/Sodium_Phosphite_Dibasic_Pentahydrate.yaml`
  is a separate `cas:13517-23-2` hydrate/salt record that only close-maps to
  `CHEBI:36361`.

## Completeness

- The record-level identity and CHEBI synonyms are complete enough.
- The final synonym surface remains incomplete while an exact row for
  phosphorous acid exports a sibling CAS record's hydrate/salt preferred term.

## Recommended Edits

- Major: prevent final SSSOM generation from folding
  `Sodium phosphite dibasic pentahydrate` into
  `MIM:Phosphorous_Acid` `other`; labels from a sibling CAS hydrate/salt record
  should stay on that exact CAS registry row, not the broader CHEBI parent.
