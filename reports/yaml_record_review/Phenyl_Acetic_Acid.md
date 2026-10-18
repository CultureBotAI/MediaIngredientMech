# `data/ingredients/mapped/Phenyl_Acetic_Acid.yaml`

## Verdict

Needs curation; major. The corrected primary identity now maps exactly to
active `CHEBI:30745` phenylacetic acid, but final SSSOM `other` exports
`LSM-15166`, the unrelated CHEBI class that this record was remapped away from.

## Identity

- Reviewed record: `data/ingredients/mapped/Phenyl_Acetic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:30745` with
  `ontology_mapping.ontology_id: CHEBI:30745`, label `phenylacetic acid`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 6 CultureMech occurrences across 6 recipes.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `CHEBI:30745` resolves `CHEBI:30745`
  `phenylacetic acid`; a separate exact search for `CHEBI:103822` resolves
  `LSM-15166`.
- A local CAS checksum calculation confirmed that `103-82-2` has the expected
  check digit.
- The final SSSOM row was inspected directly and maps
  `MIM:Phenyl_Acetic_Acid` exactly to `CHEBI:30745`.

## Evidence

- The #456 manual curation correctly remapped this record away from
  `CHEBI:103822`/`LSM-15166` to `CHEBI:30745`, and CAS `103-82-2`, the
  structured formula, InChI, and SMILES all describe phenylacetic acid.
- The raw `Role: Carbon source` synonym is filtered and does not leak into
  final SSSOM `other`.
- Major: `LSM-15166` names the unrelated old `CHEBI:103822` target, not
  phenylacetic acid, but final SSSOM still exports it in `other`.
- Major: the `CARBON_SOURCE` role is supported only by
  `COMPUTATIONAL_PREDICTION` evidence from provisional in-session Claude
  reasoning.

## Completeness

- The exact CHEBI mapping is complete enough.
- Role evidence and the final synonym surface remain incomplete while the
  stale old-target label is exported and the carbon-source role is provisional.

## Recommended Edits

- Major: in `data/ingredients/mapped/Phenyl_Acetic_Acid.yaml`, retype or remove
  `LSM-15166` so it is retained, if needed, only as rejected provenance for the
  remapping from `CHEBI:103822` and no longer appears in final SSSOM `other`.
- Major: replace `nutritional_roles.CARBON_SOURCE` with source-backed evidence
  or remove the provisional role facet until it is curated.
