# `data/ingredients/mapped/Na-caseinate.yaml`

## Verdict

Pass. The CultureMech residual surface was correctly grounded to exact
`MICRO:0001611` sodium caseinate synonym `Na-caseinate`, carries restored
structured provenance, and publishes a clean final SSSOM exact row.

## Identity

- Reviewed record: `data/ingredients/mapped/Na-caseinate.yaml`.
- Identifier and grounding: `identifier: MICRO:0001611` with
  `ontology_mapping.ontology_id: MICRO:0001611`, label `sodium caseinate`,
  source `MICRO`, `mapping_quality: SYNONYM_MATCH`, `match_level: NORMALIZED`,
  `mapping_status: MAPPED`, and no unsupported chemical or role facets.
- Occurrences: 5 CultureMech recipe occurrences across 5 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na-benzoate` through `Na-crotonate`: exited 0 and wrote zero ERROR rows.
- Engine A term validation was skipped for this record:
  `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/Na-caseinate.yaml
  "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"` exited 1 because `MICRO` is
  not in the narrow OBO-safe prefix set.

## Evidence

- A fresh OLS4 lookup resolves `MICRO:0001611` as `sodium caseinate` with exact
  synonym `Na-caseinate`, which matches the CultureMech residual surface.
- `mappings/culturemech_residual_groundings.tsv` records the 5-occurrence
  residual decision to create a new record for the exact `MICRO:0001611` match,
  and the 2026-09-06 curation event restored the same CultureMech occurrence
  table provenance into `ontology_mapping.evidence`.
- The final SSSOM exact row for `MIM:Na-caseinate` maps to `MICRO:0001611`, cites
  `MIM:culturemech:output/ingredient_occurrences.tsv`, and emits no unsupported
  synonyms.

## Completeness

- The exact-synonym grounding, 5/5 occurrence count, restored structured
  evidence, empty synonym list, and final exact mapping row agree.
- No chemical properties or media role facets are needed for this residual
  protein-salt ingredient.

## Recommended Edits

- None.
