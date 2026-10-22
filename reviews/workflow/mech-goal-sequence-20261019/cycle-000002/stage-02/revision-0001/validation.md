---
artifact_kind: stage_02_causal_graphs_validation_report
run_id: mech-goal-sequence-20261019
cycle: 2
stage: 2
stage_name: causal_graphs
revision: 1
repository: CultureBotAI/MediaIngredientMech
base_commit: 4fe89042a00f238c79e34d765792659c572caead
workflow_sha256: 059b5b9401ffeb04483cf7a46570f7f2f3c8c7fe6e574d80954bf71233cc609a
generated_at: "2026-10-22T03:24:00Z"
skills_applied:
  - .claude/skills/mediaingredientmech-evolve-workflow/SKILL.md
  - .claude/skills/curate-causal-graphs/SKILL.md
  - .claude/skills/curate-yaml-record/SKILL.md
overall_status: PASS
records_modified: 0
---

# Cycle 2, Stage 2 (`causal_graphs`) — Validation Report

## 1. Validation Summary

All repository validation suites, schema parity gates, readiness scoring gates, SSSOM invariant gates, component partonomy checks, duplicate-identifier baseline gates, and instruction reference checks executed cleanly at `main` base commit `4fe89042a00f238c79e34d765792659c572caead`.

| Gate / Check | Command Executed | Exit Code | Result Summary |
|---|---|---:|---|
| **Causal Graph Schema & Readiness Pytest Suite** | `.venv/bin/python -m pytest -o pythonpath=src --no-cov tests/test_causal_graph_schema.py tests/test_score_causal_graph_readiness.py -v` | `0` | **`66 passed` in `2.41s`** (`39/39` schema parity & closed-schema rule cases `P1`–`P5`, `N1`–`N16`, `cellstructuremech` & `traitmech` fleet alignment; `27/27` readiness scorer tests). |
| **Causal Graph Readiness Scorer (`--limit 25` & Full `2,611` Mapped Corpus)** | `.venv/bin/python scripts/score_causal_graph_readiness.py --ingredients-dir data/ingredients --duplicate-baseline mappings/duplicate_identifier_baseline.tsv --limit 25 --out /tmp/cg_readiness.tsv` and `--limit 5000 --out /tmp/cg_readiness_all.tsv` | `0` | **`wrote 25 ranked records to /tmp/cg_readiness.tsv`** (ascending by `readiness_score`: Ranks 1–2 at `7.000` `Rhamnogalacturonan_From_Soy_Bean_Pectic_Fibre.yaml` & `Soyton.yaml`; Ranks 3–8 at `9.000`; Ranks 9–25 at `10.000`) and **`wrote 2611 ranked records to /tmp/cg_readiness_all.tsv`** (highest readiness at Rank `2611` `Mineral_3B_Solution.yaml` `81.500` and Ranks `2592`–`2610` at `79.500` including `Biotin.yaml`, `Kh2po4.yaml`, `Nacl.yaml`, `Thiamine_Hcl.yaml`). |
| **Full Corpus Schema + OAK Ontology Validation** | `.venv/bin/python scripts/validate_all.py --data-dir data/ingredients --mode both` | `0` | **`Validation PASSED`** (`Total files: 5906`, `Total errors: 0`, `Total warnings: 4406`, `Ontology terms checked: 5376`, `Ontology terms valid: 5376`, `OAK lookups: active`). |
| **Strict Closed-Schema Validation (`validate_strict.py`)** | `.venv/bin/python scripts/validate_strict.py data/ingredients --out /tmp/strict_report.tsv` | `0` | **`PASS`** (`files scanned: 2953`, `files with ERROR: 0`, `total ERROR rows: 0`). |
| **Agent Instruction Reference Check** | `.venv/bin/python scripts/check_instruction_refs.py` | `0` | **`OK`** (`Scanned 52 agent-instruction file(s) against 88 recipes. OK: every referenced recipe, path, and Python CLI option exists.`). |
| **SSSOM Invariants Gate** | `.venv/bin/python scripts/validate_sssom_invariants.py --reject-tsv /tmp/needs_curator_review.tsv` | `0` | **`OK`** (`ingredient_mappings.sssom.tsv passed Rules A, B1, B2, B3, B5, C, D, E, F, G, H, I, J, K, L. /tmp/needs_curator_review.tsv written with header only.`). |
| **Component Partonomy Gate** | `.venv/bin/python scripts/validate_component_partonomy.py` | `0` | **`OK`** (`component partonomy: 2953 records, 83 decompositions, 502 components, 0 violation(s)`). |
| **Duplicate Identifier Baseline Gate** | `.venv/bin/python scripts/audit_duplicate_identifiers.py --check` | `0` | **`OK`** (`15 identifier(s) held by more than one record (35 records, 20 excess); OK: duplicate identifiers match the tracked baseline exactly.`). |

---

## 2. Detailed Validation Outputs

### 2.1 Causal Graph Schema & Readiness Pytest Suite (`tests/test_causal_graph_schema.py` + `tests/test_score_causal_graph_readiness.py`)

Command:
```bash
.venv/bin/python -m pytest -o pythonpath=src --no-cov tests/test_causal_graph_schema.py tests/test_score_causal_graph_readiness.py -v
```

Output summary (`exit 0`):
- `tests/test_causal_graph_schema.py`: `39/39` passed:
  - `test_every_design_case_is_ported` (`PASSED`)
  - Positive closed-schema cases `P1`–`P5` (`PASSED`)
  - Negative closed-schema cases `N1`–`N16` (`PASSED`)
  - `test_mim_schema_default_range_is_string` (`PASSED`)
  - `test_fleet_fixture_is_the_pinned_vendored_copy[cellstructuremech, traitmech]` (`PASSED`)
  - `test_graph_class_matches_the_fleet_copy_except_declared_deltas[{cellstructuremech,traitmech}-{EvidenceItem,CausalGraph,CausalNode,CausalEdge,ProteinExample}]` (`10/10 PASSED`)
  - `test_record_graph_slot_matches_the_fleet[cellstructuremech, traitmech]` (`PASSED`)
  - `test_graph_enums_match_the_fleet[cellstructuremech, traitmech]` (`PASSED`)
- `tests/test_score_causal_graph_readiness.py`: `27/27` passed:
  - Verifies role evidence weighting, external locator requirements (`PEER_REVIEWED_PUBLICATION`, `PREPRINT`, `DATABASE_ENTRY`, `TECHNICAL_REPORT`), bare vs. located role evidence diagnostics, duplicate-identifier baseline loading and penalties, and TSV emission.

### 2.2 Corpus Integrity & Native-Only Preservation Verification

- **Corpus file count:** `2,953` YAML files (`2,680` in `data/ingredients/mapped/*.yaml`: `2,611` `MAPPED` + `69` `REJECTED`; `273` in `data/ingredients/unmapped/*.yaml`: `260` `UNMAPPED` + `1` `AMBIGUOUS` + `12` `REJECTED`).
- **Composite SHA-256 digest (`<path>:<sha256>\n` sorted across all `2,953` YAML files):** `4a44101e2fb6199658c0fcced12a4cbd2f6624b60afd520a197e3049ccf502c7` (unchanged before and after Stage 2 execution).
- **Records with `causal_graphs` populated:** `0` of `2,953` (`records_modified: 0`).
- **Prerequisite gate check (`docs/CAUSAL_GRAPH_CONTRACT.md` Status Table Steps 3–7):**
  - `conf/sibling_pins.yaml`: absent (`False`)
  - `mappings/cross_mech_references.tsv`: absent (`False`)
  - `mappings/cross_mech_assertions.jsonl`: absent (`False`)
  - `mappings/ontology_facts.tsv`: absent (`False`)
  - `mappings/cross_mech_links.tsv`: absent (`False`)
  - `just qc-causal-graphs`: absent from `justfile` (`88` recipes scanned)
  - Compliant with `.claude/skills/curate-causal-graphs/SKILL.md` and `docs/CAUSAL_GRAPH_CONTRACT.md` Section 10: no unvalidated `causal_graphs` YAML or unsupported fields were written onto ingredient records while Step 3 (`just qc-causal-graphs` and committed snapshots) and Step 5 (validated graph writer and canary) remain unimplemented.
