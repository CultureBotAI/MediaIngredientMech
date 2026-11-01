---
artifact_kind: stage_03_protein_examples_validation
run_id: mech-goal-sequence-20261019
cycle: 13
stage: 3
stage_name: protein_examples
revision: 1
repository: CultureBotAI/MediaIngredientMech
base_commit: 65ed88e1505e3b128de998fa4b4897147340c656
workflow_sha256: 059b5b9401ffeb04483cf7a46570f7f2f3c8c7fe6e574d80954bf71233cc609a
generated_at: "2026-11-01T07:27:30Z"
status: passed
---

# Cycle 13, Stage 3 (`protein_examples`) — Validation Report

## 1. Validation Commands Executed

All workflow-profile validation, `ProteinExample` and causal-graph schema unit tests, skill frontmatter and record-review routing tests, closed-schema `validate_ingredient` `ProteinExample` checks, strict LinkML closed-schema validation across all `2,955` ingredient YAML files (plus `7` collection files = `2,962` files), causal-graph readiness scoring, SSSOM invariant validation, component partonomy validation, duplicate-identifier baseline check, instruction-reference verification, and vendored workflow synchronization checks were executed at base commit `65ed88e1505e3b128de998fa4b4897147340c656`:

| # | Gate / Check | Command | Exit Code | Status | Verified Output Summary |
|---:|---|---|---:|---|---|
| 1 | **Workflow Profile Validation (`kg_microbe_workflows`)** | `PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/src .venv/bin/python -m kg_microbe_workflows validate --profile workflow/mech-workflow.yaml --repository-key mediaingredientmech --json` | `0` | `passed` | `valid: true`, `profile_sha256: 45d7c23d67f490cea6b31e336e5d2ac98b7ce8fa4e791bd9d3be092cfdb5a10d`. |
| 2 | **Causal-Graph, `ProteinExample`, Readiness Scorer & Skill Unit Tests** | `.venv/bin/python -m pytest --no-cov tests/test_causal_graph_schema.py tests/test_score_causal_graph_readiness.py tests/test_skill_frontmatter.py tests/test_record_review_routes.py` | `0` | `passed` | `178 passed in 3.31s` (`39/39` in `tests/test_causal_graph_schema.py` covering `ProteinExample` class parity, `UniProtEntryStatusEnum`, and closed-schema rules `P1`–`P5`, `N1`–`N16`; `27/27` in `tests/test_score_causal_graph_readiness.py`; `103/103` in `tests/test_skill_frontmatter.py`; `9/9` in `tests/test_record_review_routes.py`). |
| 3 | **In-Memory `validate_ingredient` `ProteinExample` Positive & Negative Rule Check** | `.venv/bin/python -c '... from mediaingredientmech.validation.write_validated import validate_ingredient; validate_ingredient(...)'` | `0` | `passed` | Valid `ProteinExample` (`UniProtKB:P69786` `PtsG` on `D-glucose.yaml` `MOLECULAR_FUNCTION` node `EC:2.7.1.199`) returned `0` errors; all `6/6` negative tests (isoform suffix `UniProtKB:P09833-2`, unprefixed `taxon_id`, invalid `entry_status`, non-ISO `retrieved_on`, empty `evidence`, and `UniProtKB:` in `CausalNode.grounding`) rejected deterministically (`1` error each). |
| 4 | **Strict Closed-Schema LinkML Validation (`validate-strict`)** | `.venv/bin/python scripts/validate_strict.py data/ingredients --out /tmp/strict_report_c13_s3.tsv` (and `data/ingredients data/curated data/collections --out /tmp/strict_report_all_c13_s3.tsv`) | `0` | `passed` | `files scanned: 2955, files with ERROR: 0, total ERROR rows: 0` (`2,962` total YAML files including `7` collection files also verified with `0` errors). |
| 5 | **Whole-Corpus Readiness Scorer (`score_causal_graph_readiness.py`)** | `.venv/bin/python scripts/score_causal_graph_readiness.py --ingredients-dir data/ingredients --status mapped --status unmapped --include-rejected --duplicate-baseline mappings/duplicate_identifier_baseline.tsv --out /tmp/cg_readiness_all_c13_s3.tsv` (and default active mapped run `--out /tmp/cg_readiness_active_c13_s3.tsv`) | `0` | `passed` | `wrote 2955 ranked records to /tmp/cg_readiness_all_c13_s3.tsv` (`sha256: 7d7281d5fa56a93d044319e3aada269a33d002e1d2d9f714f819decca09353db`); `wrote 2611 ranked records to /tmp/cg_readiness_active_c13_s3.tsv` (`sha256: bf2afe2eefc44907ccc776655fe039c44971a07a56c24fdc0cab09b8ad6b2b3c`). |
| 6 | **Agent Instruction Reference Integrity (`instruction-refs`)** | `.venv/bin/python scripts/check_instruction_refs.py` | `0` | `passed` | `Scanned 52 agent-instruction file(s) against 88 recipes. OK: every referenced recipe, path, and Python CLI option exists.` |
| 7 | **Vendored Workflow Sync (`vendored-sync`)** | `.venv/bin/python scripts/check_vendored_sync.py` | `0` | `passed` | `OK: 26 governed artifacts match the pinned claw revision`. |
| 8 | **Component Partonomy Integrity (`qc-component-partonomy`)** | `.venv/bin/python scripts/validate_component_partonomy.py` | `0` | `passed` | `component partonomy: 2955 records, 83 decompositions, 502 components, 0 violation(s)`. |
| 9 | **SSSOM Invariant Validation (`qc-sssom`)** | `.venv/bin/python scripts/validate_sssom_invariants.py --reject-tsv /tmp/needs_curator_review_c13_s3.tsv` | `0` | `passed` | `OK: ingredient_mappings.sssom.tsv passed Rules A, B1, B2, B3, B5, C, D, E, F, G, H, I, J, K, L. /tmp/needs_curator_review_c13_s3.tsv written with header only.` |
| 10 | **Duplicate-Identifier Baseline Check (`qc-duplicate-ids`)** | `.venv/bin/python -c 'import sys, scripts.audit_duplicate_identifiers as a; a.write_tsv = lambda p, r: None; sys.argv = ["audit_duplicate_identifiers.py", "--check"]; raise SystemExit(a.main())'` | `0` | `passed` | `15 identifier(s) held by more than one record (35 records, 20 excess) ... OK: duplicate identifiers match the tracked baseline exactly.` |

---

## 2. Corpus & Contract Invariant Verification

- **Corpus Immutability During Gate-Blocked Stage 3 Assessment:**
  - `git status --short data/ mappings/ src/` confirms `0` modifications to `data/ingredients/{mapped,unmapped}/*.yaml`, `data/curated/*.yaml`, `mappings/`, or `src/`.
  - Composite SHA-256 of all `2,955` YAML files in `data/ingredients/{mapped,unmapped}/*.yaml` (`<path>:<sha256>\n` sorted): `1f8ccdb8aecff95898afcc58e415dc077c914f540a0b25e1b2210cee7d87019c` (and `<sha256>  <path>\n` sorted: `0ba1685dd5babf55ea281b504d828a86932c4f8c663ed5c4d9a6b3f321db827d`).
  - `INFRA_TASKS.md` SHA-256: `dda5707f52661e91f46d96fcbabfc256ac39d4cc865a28a3e5ab6f0536958a5e`.
  - `reviews/workflow/latest.yaml` SHA-256: `1c7c8912902d4ca266300691825ea83edd302284627d756c1d65c519318d2246` (synchronized with `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/workspace/session-orchestration/20261019/mediaingredientmech/verified-evidence-index.json`, 36 verified closure entries through Cycle 12 Stage 6 PR #1024).
  - Stage 3 Coverage Report (`reviews/workflow/mech-goal-sequence-20261019/cycle-000013/stage-03/revision-0001/coverage_report.md`) SHA-256: `4f771f03988e940c0f926c114eb9b57c332d15b62562e1d84e08c6f31eed6104`.
- **Cohort Reconciliation Check:**
  - Ineligible / Excluded records (`I1: 161` + `I2: 101` + `I3: 79` + `I4: 2` + `I5: 1` + `I6: 26` + `I7: 54` + `I8: 35`) = `459`
  - Eligible Biological / Conditional records (`P1a: 206` + `P1b: 5` + `P2a: 507` + `P2c: 11` + `P3: 1,668`) = `2,397`
  - Eligible Abiotic-Only `MEDIUM_CONDITIONING` records (`P1c: 37` + `P2b: 62`, `not_applicable` for `protein_examples`) = `99`
  - Total Eligible (`2,397 + 99`) = `2,496`
  - Grand Total (`459 + 2,496`) = `2,955` (`100.00%` of `data/ingredients/{mapped,unmapped}/*.yaml`), plus `7` collection YAML files = `2,962` strict-validated YAML files.
- **Prerequisite Blocker Verification (`docs/CAUSAL_GRAPH_CONTRACT.md` Steps 3 & 5):**
  - Confirmed that `just fetch-uniprot`, `references_cache/UniProtKB_<acc>.json`, `conf/sibling_pins.yaml`, `mappings/cross_mech_references.tsv`, `mappings/cross_mech_assertions.jsonl`, `mappings/ontology_facts.tsv`, `mappings/cross_mech_links.tsv`, `just qc-causal-graphs`, and the validated graph/protein writer are not yet implemented in the repository (`planned` in `docs/CAUSAL_GRAPH_CONTRACT.md` Status table), so `records_modified: 0` is required by `.claude/skills/add-uniprot-protein-examples/SKILL.md` and `docs/CAUSAL_GRAPH_CONTRACT.md` §10.
