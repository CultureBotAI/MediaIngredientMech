# `data/ingredients/mapped/Candimycin.yaml`

## Verdict

Needs curation, major. The `kgmicrobe.compound:candimycin` placeholder was
deliberately retained after no-hit external-ontology review, but the active
`SELECTIVE_AGENT` role is still only a provisional name-pattern prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Candimycin.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.compound:candimycin`,
  matching `ontology_mapping.ontology_id`, `ontology_source:
  kgmicrobe.compound`, `mapping_quality: PLACEHOLDER`, `mapping_status:
  MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- The 2026-05-09 placeholder review retained the local identifier because no
  exact OLS candidate or normalized local duplicate supported promotion to a
  CHEBI/NCIT primary identifier.
- A fresh CHEBI/NCIT OLS search for `candimycin` also found 0 candidates.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Camphomycin.yaml data/ingredients/mapped/Camptothecin.yaml data/ingredients/mapped/Canarius.yaml data/ingredients/mapped/Canavanine.yaml data/ingredients/mapped/Candimycin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/Candimycin.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  exited 1/skipped for this `kgmicrobe.compound` placeholder.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.GkFQqh`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.GkFQqh`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/ingredient_mappings_unknown_term_placeholder_ols_candidates.tsv`
  records `NO_EXACT_CANDIDATE` in the 2026-05-06 placeholder search across
  CHEBI, MESH, NCIT, MICRO, BTO, and FOODON.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` classifies
  `kgmicrobe.compound:candimycin` as an expected local registry identifier to
  keep until an exact external term is curated.
- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `docs/data`, and `reports`, excluding bulky backups and generated
  review-report directories, found the active `MIM:Candimycin` SSSOM row with
  the local identifier plus matching aggregate/docs rows.
- The `SELECTIVE_AGENT` role has only `reference_type:
  COMPUTATIONAL_PREDICTION` from a curated name-pattern rule and explicitly
  says review is recommended.

## Completeness

- The placeholder identity, no-hit review notes, curation history,
  single-ingredient classification, SSSOM row, and aggregate copy are present.
- No CAS, formula, chemical structure, component list, or external ontology ID
  is required while the record intentionally remains a local registry
  placeholder.

## Recommended Edits

- In `data/ingredients/mapped/Candimycin.yaml`, remove
  `physicochemical_roles.SELECTIVE_AGENT` unless a future curator can attach
  compound-specific evidence for candimycin as a selective agent in microbial
  media.
- Regenerate `data/curated/mapped_ingredients.yaml`, docs data, and any role
  exports that consume the aggregate; prove the cleanup with strict validation
  and `scripts/validate_sssom_invariants.py`.
