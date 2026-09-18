# `data/ingredients/mapped/Na2so4.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:32149` anhydrous sodium sulfate
identity, CAS-backed structure, duplicate merge, occurrence count, and hidden
decahydrate rejection pass, but final SSSOM still publishes a malformed formula
and decahydrate aliases, and the migrated role facets need evidence cleanup.

## Identity

- Reviewed record: `data/ingredients/mapped/Na2so4.yaml`.
- Identifier and grounding: `identifier: CHEBI:32149` with
  `ontology_mapping.ontology_id: CHEBI:32149`, label `sodium sulfate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 1305 CultureMech recipe occurrences across 1304 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na2so3_X_5_H2o` through `Na2wo4_X_2_H2o`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:32149` as active anhydrous
  `sodium sulfate` with formula `2Na.O4S`, CAS `7757-82-6`, and an InChI
  matching the record.
- A fresh PubChem CAS lookup for `7757-82-6` resolves to anhydrous sodium
  sulfate with the same formula and InChI, confirming the chemical block.
- The #251 repair correctly marked explicit decahydrate labels as
  `REJECTED_LABEL`, and those rejected labels are filtered from final SSSOM.
- Major: final SSSOM `other` still publishes `Glauber's salt` and `Glaubersalz`.
  Fresh OLS confirms both names belong on `CHEBI:32586` sodium sulfate
  decahydrate, not on the anhydrous `CHEBI:32149` row.
- Major: final SSSOM also publishes `NaSO4`, a malformed formula that is not a
  synonym for sodium sulfate.
- Major: `nutritional_roles.SULFUR_SOURCE` is justified only with the generic
  imported `Mineral source` role text, while the added `MINERAL_SOURCE` facet
  has an empty evidence list.
- Minor: the auto-proposed PMID evidence on the ontology mapping is redundant
  and generic experimental-use evidence; the exact formula/CHEBI mapping does
  not need it.

## Completeness

- The active ChEBI term, CAS RN, formula, structure, 1304/1305 occurrence
  statistics, duplicate merge, and exact final SSSOM row otherwise agree.
- The remaining consequential gaps are cross-hydrate and malformed final
  synonyms plus role evidence that does not support each asserted facet.

## Recommended Edits

- Major: in `data/ingredients/mapped/Na2so4.yaml`, reject or demote
  `Glauber's salt`, `Glaubersalz`, and `NaSO4` so they no longer publish as
  exact `CHEBI:32149` synonyms. Rebuild final SSSOM and rerun final SSSOM
  validation plus product label validation.
- Major: audit `SULFUR_SOURCE` and `MINERAL_SOURCE`; either attach
  claim-specific source evidence to each retained role or remove the facets that
  are not supported beyond formula inference.
- Minor: remove the weak auto-proposed PMID evidence from
  `ontology_mapping.evidence` or replace it with a source that actually
  supports this CultureMech-to-ChEBI mapping.
