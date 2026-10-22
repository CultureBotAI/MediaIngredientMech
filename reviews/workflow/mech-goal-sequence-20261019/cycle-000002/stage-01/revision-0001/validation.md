# Cycle 2 Stage 1 (`add_records`) — Validation Report

- **Run ID:** `mech-goal-sequence-20261019`
- **Repository:** `CultureBotAI/MediaIngredientMech` (`mediaingredientmech`)
- **Cycle / Stage / Revision:** Cycle `2`, Stage `1` (`add_records`), Revision `1`
- **Base Commit (`main`):** `8e6531266e17f94d68c2477311be51c49765edee`

---

## 1. Bounded Candidate Frontier Validation

```text
$ .venv/bin/python scripts/add_culturemech_gap_labels.py
DRY RUN (re-run with --apply) — 0 created, 0 minted, 0 synonym(s), 0 SSSOM row(s)

$ .venv/bin/python scripts/create_records_from_groundings.py --groundings mappings/culturemech_residual_groundings.tsv
NEW_RECORD proposals: 123
  records to create:    0
  promote instead:      0
  skipped:              123
Dry run. Re-run with --apply to write.

$ .venv/bin/python scripts/promote_microbedecoder_residual.py
vetted rows: 20   to promote: 0   skipped: 20
(dry-run — pass --apply to write collections + SSSOM)
```

---

## 2. Repository Integrity & Contract Validation Suite

```text
$ .venv/bin/python scripts/check_instruction_refs.py && .venv/bin/python scripts/check_vendored_sync.py && .venv/bin/python scripts/validate_component_partonomy.py && .venv/bin/python scripts/validate_sssom_invariants.py --reject-tsv /tmp/needs_curator_review.tsv && .venv/bin/python -m pytest -o pythonpath=src -p no:cacheprovider --no-cov -q tests/test_skill_frontmatter.py tests/test_record_review_routes.py tests/test_check_instruction_refs.py
Scanned 52 agent-instruction file(s) against 88 recipes.
  (19 `../` reference(s) point outside the repo and were not verified.)
OK: every referenced recipe, path, and Python CLI option exists.
OK: 24 governed artifacts match the pinned claw revision
component partonomy: 2953 records, 83 decompositions, 502 components, 0 violation(s)
OK: ingredient_mappings.sssom.tsv passed Rules A, B1, B2, B3, B5, C, D, E, F, G, H, I, J, K, L. /tmp/needs_curator_review.tsv written with header only.
128 passed in 2.61s
```

---

## 3. Summary of Validation Outcomes

| Check | Command | Status |
| :--- | :--- | :--- |
| Instruction & CLI Reference Gate | `.venv/bin/python scripts/check_instruction_refs.py` | **PASSED** (`52` files, `88` recipes) |
| Vendored Sync Gate | `.venv/bin/python scripts/check_vendored_sync.py` | **PASSED** (`24` governed artifacts in sync) |
| StockComponent Partonomy QC | `.venv/bin/python scripts/validate_component_partonomy.py` | **PASSED** (`2,953` records, `83` decompositions, `502` components, `0` violations) |
| SSSOM Invariants QC | `.venv/bin/python scripts/validate_sssom_invariants.py --reject-tsv /tmp/needs_curator_review.tsv` | **PASSED** (`2,987` rows, `0` violations) |
| Skill Frontmatter, Review Routes & Instruction Reference Tests | `.venv/bin/python -m pytest -o pythonpath=src -p no:cacheprovider --no-cov -q tests/test_skill_frontmatter.py tests/test_record_review_routes.py tests/test_check_instruction_refs.py` | **PASSED** (`128 passed`) |
