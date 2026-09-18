# `data/ingredients/mapped/Oxacillin_Sodium_Salt.yaml`

## Verdict

Needs curation; major. The CAS-derived `CHEBI:52134` oxacillin-sodium identity
passes, but the `SELECTIVE_AGENT` role is only a provisional name-list
prediction.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Oxacillin_Sodium_Salt.yaml`.
- Identifier and grounding: `identifier: CHEBI:52134` with
  `ontology_mapping.ontology_id: CHEBI:52134`, label `oxacillin sodium`,
  source `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no CultureMech media occurrences; the record was imported from
  CultureBotHT CAS-RN `1173-88-2`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data --labels` exited 0 across this
  five-record CHEBI batch.
- The final SSSOM row was inspected directly and maps
  `MIM:Oxacillin_Sodium_Salt` exactly to `CHEBI:52134`.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:52134` as active `oxacillin sodium`,
  reports CAS `1173-88-2`, and carries the exported IUPAC-style synonym for
  the same sodium salt.
- The YAML formula `C19H18N3O5S.Na`, InChI, and SMILES describe the same
  sodium salt rather than the oxacillin free acid.
- The final SSSOM row correctly normalizes the structured CAS as
  `CAS:1173-88-2` and does not export parent oxacillin synonyms that would
  erase the salt boundary.
- The row-review manifest already confirmed the `CHEBI:52134` ontology row.
- The `SELECTIVE_AGENT` role is supported only by
  `COMPUTATIONAL_PREDICTION` evidence from
  `infer_roles_from_name_lists`. The role may be biologically plausible for an
  antibiotic salt, but the record needs a source-backed role facet rather than
  a name-pattern annotation.

## Completeness

- The active ChEBI term, CAS-RN, formula, structure, synonym, and final SSSOM
  identity row agree.
- A gitignore-independent `rg --no-ignore --hidden` search over `data`,
  `mappings`, `reports`, `scripts`, `src`, `tests`, `docs`, and the unified
  snapshot found the expected oxacillin-sodium row-review records and no active
  `needs_curator_review.tsv` row for this subject.

## Recommended Edits

- Major: in `data/ingredients/mapped/Oxacillin_Sodium_Salt.yaml`, either
  replace `physicochemical_roles.SELECTIVE_AGENT` with cited experimental or
  recipe evidence, or remove the provisional role facet until source-backed
  role evidence is curated. Then rebuild the final SSSOM and rerun
  `scripts/validate_sssom_invariants.py`.
