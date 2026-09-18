# `data/ingredients/mapped/Na_Glutamate.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:64220` monosodium glutamate identity,
duplicate merge, occurrence count, `NITROGEN_SOURCE` role, and hidden-hydrate
rejection pass, but the CAS-backed chemical block no longer reproduces and a
disodium glutamate alias still publishes in final SSSOM.

## Identity

- Reviewed record: `data/ingredients/mapped/Na_Glutamate.yaml`.
- Identifier and grounding: `identifier: CHEBI:64220` with
  `ontology_mapping.ontology_id: CHEBI:64220`, label `monosodium glutamate`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 162 CultureMech recipe occurrences across 162 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na3-citrate_X_2_H2o` through `Nabr`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:64220` as active
  `monosodium glutamate`, with formula `C5H8NO4.Na` and the same InChI and
  SMILES as the record.
- The `NITROGEN_SOURCE` role is supported by CultureMech `DATABASE_ENTRY`
  evidence whose curator note preserves the original `Nitrogen Source` role
  text.
- The #251 repair correctly marked the monohydrate label as `REJECTED_LABEL`,
  and that rejected label is filtered from final SSSOM.
- Major: a fresh PubChem CAS lookup for the stored CAS `142-47-2` resolves to a
  chiral hydrated monosodium glutamate record, not to the anhydrous,
  stereo-unspecified structure stored from `CHEBI:64220`.
- Major: final SSSOM `other` publishes `Na2-glutamate`, which crosses the
  monosodium/disodium salt boundary.

## Completeness

- The active ChEBI term, 162/162 occurrence count, duplicate merge,
  nitrogen-source role, rejected hidden-hydrate label, and exact final SSSOM row
  otherwise agree.
- The remaining consequential gaps are the stale/mismatched CAS-backed
  chemistry and the disodium alias.

## Recommended Edits

- Major: verify whether `142-47-2` still supports the exact anhydrous,
  stereo-unspecified `CHEBI:64220` structure; if not, remove or replace the CAS
  and any derived chemistry that cannot be reproduced from that CAS. Rerun
  strict validation after the chemical block changes.
- Major: reject or delete `Na2-glutamate` so it no longer publishes as an exact
  `CHEBI:64220` synonym. Rebuild final SSSOM and rerun final SSSOM validation
  plus product label validation.
