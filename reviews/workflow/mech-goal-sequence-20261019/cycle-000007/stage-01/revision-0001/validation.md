# Cycle 7, Stage 1 (`add_domain_objects`) — Validation Report

- **Run ID:** `mech-goal-sequence-20261019`
- **Cycle / Stage:** Cycle 7, Stage 1 (`add_domain_objects`, canonical stage `add_records`)
- **Status:** `passed`

## Executed Command

```bash
.venv/bin/python scripts/check_instruction_refs.py && .venv/bin/python scripts/check_vendored_sync.py && .venv/bin/python scripts/validate_component_partonomy.py && .venv/bin/python scripts/validate_sssom_invariants.py --reject-tsv /tmp/needs_curator_review.tsv && .venv/bin/python -m pytest -o pythonpath=src -p no:cacheprovider --no-cov -q tests/test_skill_frontmatter.py tests/test_record_review_routes.py tests/test_check_instruction_refs.py
```

## Verification Output Summary

1. **Instruction Reference Check (`scripts/check_instruction_refs.py`):**
   - `Scanned 52 agent-instruction file(s) against 88 recipes.`
   - `OK: every referenced recipe, path, and Python CLI option exists.`
2. **Vendored Governance Sync (`scripts/check_vendored_sync.py`):**
   - `OK: 24 governed artifacts match the pinned claw revision`
3. **Component Partonomy Validation (`scripts/validate_component_partonomy.py`):**
   - `component partonomy: 2953 records, 83 decompositions, 502 components, 0 violation(s)`
4. **SSSOM Invariant Validation (`scripts/validate_sssom_invariants.py`):**
   - `OK: ingredient_mappings.sssom.tsv passed Rules A, B1, B2, B3, B5, C, D, E, F, G, H, I, J, K, L. /tmp/needs_curator_review.tsv written with header only.`
5. **Pytest Suite:**
   - `128 passed`
6. **Repeated Candidate Frontier Verification (`Pass 1` & `Pass 2`):**
   - `.venv/bin/python scripts/add_culturemech_gap_labels.py`: `0 created, 0 minted, 0 synonym(s), 0 SSSOM row(s)` (all 17 gap labels already represented in `data/ingredients/{mapped,unmapped}/`).
   - `.venv/bin/python scripts/create_records_from_groundings.py --groundings mappings/culturemech_residual_groundings.tsv`: `NEW_RECORD proposals: 123, records to create: 0, promote instead: 0, skipped: 123`.
   - `.venv/bin/python scripts/promote_microbedecoder_residual.py`: `vetted rows: 20, to promote: 0, skipped: 20`.
