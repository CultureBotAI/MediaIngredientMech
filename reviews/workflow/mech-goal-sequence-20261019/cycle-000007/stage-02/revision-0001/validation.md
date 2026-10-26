---
run_id: mech-goal-sequence-20261019
cycle: 7
stage: 2
stage_name: curate_causal_graphs
repository_key: mediaingredientmech
base_commit: abc632487b111c3417d59c4bd56eef375817d704
generated_at: "2026-10-26T04:49:00Z"
validation_status: passed
---

# Cycle 7 Stage 2 Validation Report — `curate_causal_graphs`

## 1. Validation Command Suite Executed

The following repository-local causal-graph, readiness-scorer, governance, partonomy, SSSOM invariant, duplicate-identifier, and closed-schema instance validation gates were executed for Cycle 7 Stage 2 (`curate_causal_graphs`):

```bash
.venv/bin/python -m pytest -o addopts="" tests/test_causal_graph_schema.py tests/test_score_causal_graph_readiness.py && \
  .venv/bin/python scripts/score_causal_graph_readiness.py --include-rejected --limit 10 --out /tmp/cg_readiness_c7_s2.tsv && \
  .venv/bin/python scripts/check_instruction_refs.py && \
  .venv/bin/python scripts/check_vendored_sync.py && \
  .venv/bin/python scripts/validate_component_partonomy.py && \
  .venv/bin/python scripts/validate_sssom_invariants.py --reject-tsv /tmp/needs_curator_review.tsv && \
  .venv/bin/python scripts/audit_duplicate_identifiers.py --check && \
  .venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv
```

---

## 2. Gate-by-Gate Results

| # | Gate / Validator | Command | Exit Code | Result Summary |
|---:|---|---|---:|---|
| 1 | Causal-Graph Closed-Schema & Readiness-Scorer Unit Tests | `.venv/bin/python -m pytest -o addopts="" tests/test_causal_graph_schema.py tests/test_score_causal_graph_readiness.py` | `0` | `66 passed` (`39` in `tests/test_causal_graph_schema.py`: `P1`–`P8` positive + `N1`–`N31` negative closed-schema fixtures; `27` in `tests/test_score_causal_graph_readiness.py`). |
| 2 | Causal-Graph Readiness Scorer CLI | `.venv/bin/python scripts/score_causal_graph_readiness.py --include-rejected --limit 10 --out /tmp/cg_readiness_c7_s2.tsv` | `0` | Scored all `2,953` YAML records (`2,496` `IDENTITY_GATE`-eligible, `457` ineligible) and wrote top 10 ranked rows to `/tmp/cg_readiness_c7_s2.tsv` (`Biotin.yaml` rank `2953`, score `109.163`; `Na2moo4_X_2_H2o.yaml` rank `2944`, score `103.500`). |
| 3 | Agent Instruction Reference Gate | `.venv/bin/python scripts/check_instruction_refs.py` | `0` | `Scanned 52 agent-instruction file(s) against 88 recipes. OK: every referenced recipe, path, and Python CLI option exists.` |
| 4 | Vendored Governance Sync Gate | `.venv/bin/python scripts/check_vendored_sync.py` | `0` | `OK: 24 governed artifacts match the pinned claw revision` |
| 5 | Component Partonomy Validator | `.venv/bin/python scripts/validate_component_partonomy.py` | `0` | `component partonomy: 2953 records, 83 decompositions, 502 components, 0 violation(s)` |
| 6 | SSSOM Invariants Validator | `.venv/bin/python scripts/validate_sssom_invariants.py --reject-tsv /tmp/needs_curator_review.tsv` | `0` | `OK: ingredient_mappings.sssom.tsv passed Rules A, B1, B2, B3, B5, C, D, E, F, G, H, I, J, K, L. /tmp/needs_curator_review.tsv written with header only.` |
| 7 | Duplicate-Identifier Baseline Check | `.venv/bin/python scripts/audit_duplicate_identifiers.py --check` | `0` | `15 identifier(s) held by more than one record (35 records, 20 excess)` — matches `mappings/duplicate_identifier_baseline.tsv` with `0` regressions. |
| 8 | Strict Closed-Schema LinkML Instance Validator | `.venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv` | `0` | `Validated 2960 files: 0 with ERRORs, 0 total ERROR rows, 0 total WARN rows.` (`2,953` ingredient YAML files + `7` collection/metadata YAML files). |

---

## 3. Prerequisite Gate Audit (`docs/CAUSAL_GRAPH_CONTRACT.md` Steps 3–7)

| Contract Artifact / Recipe | Expected Location | Status | Notes |
|---|---|---|---|
| `conf/sibling_pins.yaml` | `conf/sibling_pins.yaml` | `blocked_absent` | Step 3 of `docs/CAUSAL_GRAPH_CONTRACT.md` Status table (`planned`). |
| `mappings/cross_mech_references.tsv` | `mappings/cross_mech_references.tsv` | `blocked_absent` | Step 3 snapshot (`planned`). |
| `mappings/cross_mech_assertions.jsonl` | `mappings/cross_mech_assertions.jsonl` | `blocked_absent` | Step 3 snapshot (`planned`). |
| `mappings/ontology_facts.tsv` | `mappings/ontology_facts.tsv` | `blocked_absent` | Step 3 snapshot (`planned`). |
| `mappings/cross_mech_links.tsv` | `mappings/cross_mech_links.tsv` | `blocked_absent` | Step 3 derived artifact (`planned`). |
| `just qc-causal-graphs` | `justfile` | `blocked_absent` | Step 3 QC gate (`planned`); required before writing `causal_graphs` onto YAML records. |
