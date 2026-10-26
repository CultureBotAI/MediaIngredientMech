---
artifact_kind: stage_02_causal_graphs_validation
run_id: mech-goal-sequence-20261019
cycle: 7
stage: 2
stage_name: causal_graphs
revision: 1
repository: CultureBotAI/MediaIngredientMech
base_commit: abc632487b111c3417d59c4bd56eef375817d704
workflow_sha256: 059b5b9401ffeb04483cf7a46570f7f2f3c8c7fe6e574d80954bf71233cc609a
generated_at: "2026-10-26T05:01:00Z"
status: passed
---

# Cycle 7, Stage 2 (`causal_graphs`) — Validation Report

## 1. Validation Commands Executed

All native causal-graph schema tests, readiness scorer tests, strict LinkML closed-schema validation, SSSOM invariant validation, component partonomy validation, duplicate-identifier baseline check, instruction-reference verification, and vendored workflow synchronization checks were executed at base commit `abc632487b111c3417d59c4bd56eef375817d704`:

| # | Gate / Check | Command | Exit Code | Status | Verified Output Summary |
|---:|---|---|---:|---|---|
| 1 | **Causal-Graph Schema & Readiness Scorer Unit Tests** | `.venv/bin/python -m pytest -o addopts="" tests/test_causal_graph_schema.py tests/test_score_causal_graph_readiness.py` | `0` | `passed` | `66 passed` (`39/39` in `tests/test_causal_graph_schema.py` covering `CausalGraph`, `CausalNode`, `CausalEdge`, `ProteinExample`, and closed-schema rules `P1`–`P5`, `N1`–`N16`; `27/27` in `tests/test_score_causal_graph_readiness.py`). |
| 2 | **Causal-Graph Readiness Scorer CLI** | `.venv/bin/python scripts/score_causal_graph_readiness.py --include-rejected --limit 10 --out /tmp/cg_readiness_c7_s2.tsv` | `0` | `passed` | `wrote 10 ranked records to /tmp/cg_readiness_c7_s2.tsv` (and full 2,611-record active ranking verified). |
| 3 | **Agent Instruction Reference Integrity (`instruction-refs`)** | `.venv/bin/python scripts/check_instruction_refs.py` | `0` | `passed` | `Scanned 52 agent-instruction file(s) against 88 recipes. OK: every referenced recipe, path, and Python CLI option exists.` |
| 4 | **Vendored Workflow Sync (`vendored-sync`)** | `.venv/bin/python scripts/check_vendored_sync.py` | `0` | `passed` | `OK: 24 governed artifacts match the pinned claw revision`. |
| 5 | **Component Partonomy Integrity (`qc-component-partonomy`)** | `.venv/bin/python scripts/validate_component_partonomy.py` | `0` | `passed` | `component partonomy: 2953 records, 83 decompositions, 502 components, 0 violation(s)`. |
| 6 | **SSSOM Invariant Validation (`qc-sssom`)** | `.venv/bin/python scripts/validate_sssom_invariants.py --reject-tsv /tmp/needs_curator_review.tsv` | `0` | `passed` | `OK: ingredient_mappings.sssom.tsv passed Rules A, B1, B2, B3, B5, C, D, E, F, G, H, I, J, K, L. /tmp/needs_curator_review.tsv written with header only.` |
| 7 | **Duplicate-Identifier Baseline Check (`qc-duplicate-ids`)** | `.venv/bin/python scripts/audit_duplicate_identifiers.py --check` | `0` | `passed` | `15 identifier(s) held by more than one record (35 records, 20 excess)` — matches `mappings/duplicate_identifier_baseline.tsv` (`0` regressions). |
| 8 | **Strict Closed-Schema LinkML Validation (`validate-strict`)** | `.venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv` | `0` | `passed` | `files scanned: 2960, files with ERROR: 0, total ERROR rows: 0`. |

---

## 2. Corpus & Contract Invariant Verification

- **Corpus Immutability During Gate-Blocked Assessment:**
  - `git status --short data/ mappings/ src/` confirms `0` modifications to `data/ingredients/{mapped,unmapped}/*.yaml`, `mappings/`, or `src/`.
  - Composite SHA-256 of all `2,953` YAML files in `data/ingredients/{mapped,unmapped}/*.yaml` (`<path>:<sha256>\n` sorted): `4a44101e2fb6199658c0fcced12a4cbd2f6624b60afd520a197e3049ccf502c7`.
  - `INFRA_TASKS.md` SHA-256: `dda5707f52661e91f46d96fcbabfc256ac39d4cc865a28a3e5ab6f0536958a5e`.
  - `reviews/workflow/latest.yaml` SHA-256: `848a14567529757e536ece55d107633d25915e461cc2f89bd2a43eac37fd460a` (synchronized with `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/workspace/session-orchestration/20261019/mediaingredientmech/verified-evidence-index.json`, 18 verified closure entries through Cycle 6 Stage 6).
- **Cohort Reconciliation Check:**
  - Ineligible records (`I1: 159` + `I2: 101` + `I3: 79` + `I4: 2` + `I5: 1` + `I6: 26` + `I7: 54` + `I8: 35`) = `457`
  - Eligible records (`E1: 248` + `E2a: 569` + `E2b: 11` + `E3: 1,668`) = `2,496`
  - Total evaluated = `457 + 2,496 = 2,953` (`100.00%` of `data/ingredients/{mapped,unmapped}/*.yaml`).
- **Prerequisite Blocker Verification (`docs/CAUSAL_GRAPH_CONTRACT.md` Steps 3–7):**
  - Confirmed that `conf/sibling_pins.yaml`, `mappings/cross_mech_references.tsv`, `mappings/cross_mech_assertions.jsonl`, `mappings/ontology_facts.tsv`, `mappings/cross_mech_links.tsv`, and `just qc-causal-graphs` are not yet present in the repository (`planned` in `docs/CAUSAL_GRAPH_CONTRACT.md` Status table), so `records_modified: 0` is required by `.claude/skills/curate-causal-graphs/SKILL.md` and `docs/CAUSAL_GRAPH_CONTRACT.md` §10.
