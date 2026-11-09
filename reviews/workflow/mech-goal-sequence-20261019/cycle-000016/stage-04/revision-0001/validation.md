# Cycle 16 Stage 4 Validation Report (`record_review`)

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `16` (`cycle-000016`)
- **Stage**: `4` (`stage-04` / `record_review`)
- **Revision**: `revision-0001`
- **Base Commit (`main`)**: `f9e11194d768bcf67cd5a9d5aecff540223fa98b`

---

## 1. Validation Commands Executed and Results

| Check | Command | Exit Code | Summary |
| --- | --- | ---: | --- |
| Workflow profile validation | `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/python -m kg_microbe_workflows validate --profile workflow/mech-workflow.yaml --parent workflow/parent/mech-cycle.yaml --schema workflow/parent/workflow.yaml` | `0` | `Workflow profile valid` |
| Native structured review validation | `.venv/bin/python scripts/record_review.py --repo-root . check` | `0` | `valid_reviews: 1015`, `coverage: "declared_scopes_only"`, `0` schema/profile errors, `0` stale `source_sha256` target hashes across all `1,015` structured review bundles (`2,030` files) |
| Strict LinkML schema validation | `.venv/bin/python scripts/validate_strict.py data/ingredients data/curated data/collections --out /dev/null` | `0` | `files scanned: 2963`, `files with ERROR: 0`, `total ERROR rows: 0` |
| Component partonomy validation | `.venv/bin/python scripts/validate_component_partonomy.py` | `0` | `component partonomy: 2956 records, 83 decompositions, 502 components, 0 violation(s)` |
| SSSOM invariant validation | `.venv/bin/python scripts/validate_sssom_invariants.py --reject-tsv /dev/null` | `0` | `OK: ingredient_mappings.sssom.tsv passed Rules A, B1, B2, B3, B5, C, D, E, F, G, H, I, J, K, L.` (`0` rejection rows) |
| Duplicate identifier baseline check | `.venv/bin/python scripts/audit_duplicate_identifiers.py --check` | `0` | `15 identifier(s) held by more than one record (35 records, 20 excess)` — `OK: duplicate identifiers match the tracked baseline exactly.` |
| Instruction and recipe reference check | `.venv/bin/python scripts/check_instruction_refs.py` | `0` | `Scanned 54 agent-instruction file(s) against 88 recipes. OK: every referenced recipe, path, and Python CLI option exists.` |
| Vendored governance sync check | `.venv/bin/python scripts/check_vendored_sync.py` | `0` | `OK: 26 governed artifacts match the pinned claw revision` |
| Focused unit test suite | `.venv/bin/python -m pytest -o pythonpath=src -p no:cacheprovider --no-cov -q tests/test_record_review_routes.py tests/test_skill_frontmatter.py tests/test_causal_graph_schema.py tests/test_score_causal_graph_readiness.py tests/test_check_instruction_refs.py` | `0` | `194 passed, 12 warnings in 4.09s` |
| Workflow evidence manifest validation | `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/python -m kg_microbe_workflows validate-evidence --root . --previous reviews/workflow/mech-goal-sequence-20261019/cycle-000015/stage-05/revision-0001/evidence.yaml --required-output review_report --required-output review_findings reviews/workflow/mech-goal-sequence-20261019/cycle-000016/stage-04/revision-0001/evidence.yaml` | `0` | `valid: true` (`errors: []`) |
