# `data/ingredients/mapped/Alboverticillin.yaml`

## Verdict

Needs curation. The `kgmicrobe.compound:alboverticillin` placeholder was
deliberately retained after a no-hit OLS review, but the `SELECTIVE_AGENT` role
is still only a provisional name-pattern prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Alboverticillin.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.compound:alboverticillin` with the same local
  `ontology_mapping.ontology_id`, source `kgmicrobe.compound`,
  `mapping_quality: PLACEHOLDER`, and `mapping_status: MAPPED`.
- The 2026-05-09 placeholder review found no exact OLS candidate and no
  normalized local mapped duplicate, which supports retaining the local
  placeholder until a real CHEBI/NCIT identity is curated.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Alazopeptin.yaml data/ingredients/mapped/Alboverticillin.yaml data/ingredients/mapped/Alcl3.yaml data/ingredients/mapped/Alcl3_X_6_H2o.yaml data/ingredients/mapped/Algal_Trace_Elements_Solution.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/Alboverticillin.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  exited 1, so `just validate-terms` would skip Engine A for this
  `kgmicrobe.compound` placeholder.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/ingredient_mappings_unknown_term_placeholder_ols_candidates.tsv`
  records `NO_EXACT_CANDIDATE` for this placeholder in the 2026-05-06 OLS
  placeholder search across CHEBI, MESH, NCIT, MICRO, BTO, and FOODON.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` classifies
  `kgmicrobe.compound:alboverticillin` as an expected registry identifier to
  keep pending promotion to an external ontology term.
- `mappings/ingredient_mappings.sssom.tsv` row 362 preserves the
  `kgmicrobe.compound:alboverticillin` exact placeholder row.
- The `SELECTIVE_AGENT` role is still only a computational prediction from a
  curated name-pattern rule and says review is recommended.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `src`, `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found the
  active YAML, aggregate copy, SSSOM row, no-hit placeholder candidate row,
  generated indexes, and ignored aggregate backups.

## Completeness

- Placeholder identity, no-hit review notes, curation history, and
  `ingredient_type` are populated.
- No CAS, formula, component, environmental context, source occurrence, or
  dataset entry is needed until an external chemical identity is available.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- Either cite claim-level evidence for alboverticillin as a selective agent in
  microbial media, or remove `physicochemical_roles.SELECTIVE_AGENT` from
  `data/ingredients/mapped/Alboverticillin.yaml`.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run --frozen python scripts/validate_component_partonomy.py`, and
  `uv run --frozen python scripts/validate_sssom_invariants.py`.
