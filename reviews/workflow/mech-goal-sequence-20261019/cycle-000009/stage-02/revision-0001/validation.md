---
artifact_kind: stage_02_causal_graphs_validation
run_id: mech-goal-sequence-20261019
cycle: 9
stage: 2
stage_name: causal_graphs
revision: 1
repository: CultureBotAI/MediaIngredientMech
base_commit: 85d56e250d8c9c948d5f686eaf24af62601af602
workflow_sha256: 059b5b9401ffeb04483cf7a46570f7f2f3c8c7fe6e574d80954bf71233cc609a
generated_at: "2026-10-30T17:52:00Z"
status: passed
---

# Cycle 9, Stage 2 (`causal_graphs`) — Validation Report

## 1. Validation Commands Executed

All workflow-profile validation, native causal-graph schema tests, readiness scorer tests, strict LinkML closed-schema validation, SSSOM invariant validation, component partonomy validation, duplicate-identifier baseline check, instruction-reference verification, and vendored workflow synchronization checks were executed at base commit `85d56e250d8c9c948d5f686eaf24af62601af602`:

| # | Gate / Check | Command | Exit Code | Status | Verified Output Summary |
|---:|---|---|---:|---|---|
| 1 | **Workflow Profile Validation (`kg_microbe_workflows`)** | `env PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/src /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/python -m kg_microbe_workflows validate --profile workflow/mech-workflow.yaml --repository-key mediaingredientmech` | `0` | `passed` | `Workflow profile valid`. |
| 2 | **Causal-Graph Schema & Readiness Scorer Unit Tests** | `.venv/bin/python -m pytest -o addopts="" tests/test_causal_graph_schema.py tests/test_score_causal_graph_readiness.py` | `0` | `passed` | `66 passed` (`39/39` in `tests/test_causal_graph_schema.py` covering `CausalGraph`, `CausalNode`, `CausalEdge`, `ProteinExample`, and closed-schema rules `P1`–`P5`, `N1`–`N16`; `27/27` in `tests/test_score_causal_graph_readiness.py`). |
| 3 | **Causal-Graph Readiness Scorer CLI** | `.venv/bin/python scripts/score_causal_graph_readiness.py --ingredients-dir data/ingredients --duplicate-baseline mappings/duplicate_identifier_baseline.tsv --limit 25 --out /tmp/cg_readiness_c9_s2_top25.tsv` | `0` | `passed` | `wrote 25 ranked records to /tmp/cg_readiness_c9_s2_top25.tsv` (`sha256: 5a3c5bf4f35158627940614670df85af4711e18ed831d6c77938c049e4a21394`; full `2,611`-record active ranking verified in `/tmp/cg_readiness_active_c9_s2.tsv`, `sha256: bf2afe2eefc44907ccc776655fe039c44971a07a56c24fdc0cab09b8ad6b2b3c`). |
| 4 | **Agent Instruction Reference Integrity (`instruction-refs`)** | `.venv/bin/python scripts/check_instruction_refs.py` | `0` | `passed` | `Scanned 52 agent-instruction file(s) against 88 recipes. OK: every referenced recipe, path, and Python CLI option exists.` |
| 5 | **Vendored Workflow Sync (`vendored-sync`)** | `.venv/bin/python scripts/check_vendored_sync.py` | `0` | `passed` | `OK: 24 governed artifacts match the pinned claw revision`. |
| 6 | **Component Partonomy Integrity (`qc-component-partonomy`)** | `.venv/bin/python scripts/validate_component_partonomy.py` | `0` | `passed` | `component partonomy: 2953 records, 83 decompositions, 502 components, 0 violation(s)`. |
| 7 | **SSSOM Invariant Validation (`qc-sssom`)** | `.venv/bin/python scripts/validate_sssom_invariants.py --reject-tsv /tmp/needs_curator_review.tsv` | `0` | `passed` | `OK: ingredient_mappings.sssom.tsv passed Rules A, B1, B2, B3, B5, C, D, E, F, G, H, I, J, K, L. /tmp/needs_curator_review.tsv written with header only.` |
| 8 | **Duplicate-Identifier Baseline Check (`qc-duplicate-ids`)** | `.venv/bin/python scripts/audit_duplicate_identifiers.py --check` | `0` | `passed` | `15 identifier(s) held by more than one record (35 records, 20 excess)` — matches `mappings/duplicate_identifier_baseline.tsv` (`0` regressions). |
| 9 | **Strict Closed-Schema LinkML Validation (`validate-strict`)** | `.venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv` | `0` | `passed` | `files scanned: 2960, files with ERROR: 0, total ERROR rows: 0`. |

---

## 2. Corpus & Contract Invariant Verification

- **Corpus Immutability During Gate-Blocked Assessment:**
  - `git status --short data/ mappings/ src/` confirms `0` modifications to `data/ingredients/{mapped,unmapped}/*.yaml`, `mappings/`, or `src/`.
  - Composite SHA-256 of all `2,953` YAML files in `data/ingredients/{mapped,unmapped}/*.yaml` (`<path>:<sha256>\n` sorted): `4a44101e2fb6199658c0fcced12a4cbd2f6624b60afd520a197e3049ccf502c7`.
  - `INFRA_TASKS.md` SHA-256: `dda5707f52661e91f46d96fcbabfc256ac39d4cc865a28a3e5ab6f0536958a5e`.
  - `reviews/workflow/latest.yaml` SHA-256: `b95934b9e5d7cb7367df6e6f851bf95db388b4e5a5804449b00a5428084dc045` (synchronized with `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/workspace/session-orchestration/20261019/mediaingredientmech/verified-evidence-index.json`, 24 verified closure entries through Cycle 8 Stage 6).
- **Cohort Reconciliation Check:**
  - Ineligible records (`I1: 159` + `I2: 101` + `I3: 79` + `I4: 2` + `I5: 1` + `I6: 26` + `I7: 54` + `I8: 35`) = `457`
  - Eligible records (`E1: 248` + `E2a: 569` + `E2b: 11` + `E3: 1,668`) = `2,496`
  - Total evaluated = `457 + 2,496 = 2,953` (`100.00%` of `data/ingredients/{mapped,unmapped}/*.yaml`).
- **Prerequisite Blocker Verification (`docs/CAUSAL_GRAPH_CONTRACT.md` Steps 3–7):**
  - Confirmed that `conf/sibling_pins.yaml`, `mappings/cross_mech_references.tsv`, `mappings/cross_mech_assertions.jsonl`, `mappings/ontology_facts.tsv`, `mappings/cross_mech_links.tsv`, and `just qc-causal-graphs` are not yet present in the repository (`planned` in `docs/CAUSAL_GRAPH_CONTRACT.md` Status table), so `records_modified: 0` is required by `.claude/skills/curate-causal-graphs/SKILL.md` and `docs/CAUSAL_GRAPH_CONTRACT.md` §10.
