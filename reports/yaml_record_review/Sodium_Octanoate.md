# `data/ingredients/mapped/Sodium_Octanoate.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:132100` sodium octanoate identity,
CAS-backed structure, ChEBI synonyms, occurrence count, and final SSSOM row
pass, but the `CARBON_SOURCE` role is still a provisional computational
prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Sodium_Octanoate.yaml`.
- Identifier and grounding: `identifier: CHEBI:132100` with
  `ontology_mapping.ontology_id: CHEBI:132100`, label `sodium octanoate`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 5 source occurrences across 5 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sodium_Nitrate_Nitrogen_Source` through `Sodium_Pantothenate`: exited 0 and
  wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- `uv run --frozen python scripts/run_shared_evidence_validator.py` is
  unavailable because the sibling `culturebotai-claw` checkout is absent.

## Evidence

- Fresh EBI OLS4 lookup resolves active `CHEBI:132100` with label
  `sodium octanoate`, all five curated ChEBI synonyms, and CAS
  `1984-06-1`.
- Fresh PubChem lookup for CAS `1984-06-1` resolves to sodium octanoate with
  the same sodium octanoate InChI and SMILES as the record.
- The final SSSOM `other` column keeps the five same-substance ChEBI aliases
  plus `CAS:1984-06-1`; the raw `Role: Carbon source` import text is correctly
  filtered out of final synonyms.
- Major: `nutritional_roles.CARBON_SOURCE` is backed only by
  `reference_type: COMPUTATIONAL_PREDICTION` from a curated name-pattern rule
  with a `review recommended` note. That does not meet the role evidence
  standard even though the identity fields are correct.

## Completeness

- The ChEBI ID, label, CAS RN, formula, structure, occurrence count, active
  synonyms, and final exact row agree.
- The only consequential gap is replacing or removing the provisional
  carbon-source role.

## Recommended Edits

- Major: in `data/ingredients/mapped/Sodium_Octanoate.yaml`, either replace the
  provisional `COMPUTATIONAL_PREDICTION` role evidence with checked
  CultureMech source evidence for `Role: Carbon source`, or drop
  `nutritional_roles.CARBON_SOURCE` if that original role cannot be recovered.
