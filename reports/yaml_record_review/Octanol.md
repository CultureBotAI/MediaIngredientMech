# `data/ingredients/mapped/Octanol.yaml`

## Verdict

Needs curation, major. The record carries CAS `111-87-5`, which denotes
1-octanol, but exact-maps to the generic ChEBI `octanol` positional-isomer
class.

## Identity

- Reviewed record: `data/ingredients/mapped/Octanol.yaml`.
- Current grounding: `identifier: CHEBI:37868` with
  `ontology_mapping.ontology_id: CHEBI:37868`, label `octanol`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Structure: CultureBotHT supplied CAS `111-87-5` and formula `C8H18O`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:37868` as active `octanol`, defined
  as a fatty alcohol with the hydroxy function at any position of an
  unbranched saturated C8 chain, and reports CAS xref `29063-28-3`.
- A fresh exact EBI OLS4 search for `1-octanol` returns active
  `CHEBI:16188` `octan-1-ol`, defined as an octanol with the hydroxy group at
  position 1.
- The final SSSOM row maps `MIM:Octanol` exactly to the generic parent
  `CHEBI:37868` and exports `CAS:111-87-5` in `other`, which combines a
  position-specific registry number with the parent positional-isomer class.
- No unsupported roles, components, supplied forms, or environmental contexts
  are asserted.

## Completeness

- The current formula is compatible with both 1-octanol and the broader
  octanol class, so the record needs a CAS-aware identity repair rather than
  only formula backfill.
- The row-review tables confirm only the current generic ChEBI ID; they do not
  resolve the CAS-specific mismatch.

## Recommended Edits

- In `data/ingredients/mapped/Octanol.yaml`, verify the source CAS
  `111-87-5` and re-ground the record to the form-specific `CHEBI:16188`
  `octan-1-ol` if the CultureBotHT source row was CAS-specific.
- Populate InChI and SMILES from the selected form-specific ChEBI term.
- Sync the aggregate record, regenerate the final SSSOM, and rerun strict
  validation, `validate_sssom_invariants.py`, and
  `validate_id_label_correspondence.py`.
