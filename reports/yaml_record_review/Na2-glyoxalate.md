# `data/ingredients/mapped/Na2-glyoxalate.yaml`

## Verdict

Needs curation - major. The record's `CHEBI:91251` sodium glyoxylate grounding,
CAS-backed structure, source-backed carbon role, synonyms, and final exact
target pass, but the maintained `Na2-glyoxalate` label overstates the sodium
stoichiometry of this monosodium salt and is published as the final subject
label.

## Identity

- Reviewed record: `data/ingredients/mapped/Na2-glyoxalate.yaml`.
- Identifier and grounding: `identifier: CHEBI:91251` with
  `ontology_mapping.ontology_id: CHEBI:91251`, label `sodium glyoxylate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 3 CultureMech recipe occurrences across 3 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na2-edta_X_2_H2o` through `Na2HPO4-NaH2PO4_Buffer`: exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:91251` as active
  `sodium glyoxylate`, with `cas:2706-75-4`, formula `C2HO3.Na`, the stored
  structure, and the accepted glyoxylate synonyms.
- The `CARBON_SOURCE` facet is source-backed by CultureMech original role text
  that explicitly says `Carbon Source`; the raw `Role: Carbon source` string is
  correctly absent from final SSSOM `other`.
- Major: `Na2-glyoxalate` is not an accepted ChEBI synonym and implies a
  disodium salt, while `CHEBI:91251` is the monosodium salt of glyoxylic acid.
  The misleading preferred term also becomes the final SSSOM subject label.

## Completeness

- The active ChEBI target, CAS RN, formula, structure, exact synonyms, 3/3
  occurrence count, source-backed `CARBON_SOURCE` role, and final exact target
  agree.
- The remaining gap is the sodium-count typo in the maintained label and final
  subject label.

## Recommended Edits

- Major: rename `data/ingredients/mapped/Na2-glyoxalate.yaml` and its
  `preferred_term` to a monosodium label such as `Na-glyoxalate` or
  `Na-glyoxylate`, preserve the old source surface as non-published provenance
  if needed, then rebuild final SSSOM and re-run final SSSOM validation plus
  product label validation.
