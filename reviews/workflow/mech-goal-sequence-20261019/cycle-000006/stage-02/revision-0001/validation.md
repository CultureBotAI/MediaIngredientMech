# Cycle 6, Stage 2 (`causal_graphs`) — Validation Evidence

- **Run ID:** `mech-goal-sequence-20261019`
- **Cycle / Stage / Revision:** `cycle-000006` / `stage-02` (`causal_graphs`) / `revision-0001`
- **Repository:** `CultureBotAI/MediaIngredientMech`
- **Base Commit (`main`):** `7c657bf1df19a2d1acc88f0157959281aab655c3`

---

## 1. Combined Validation Command

```bash
.venv/bin/python -m pytest -o addopts="" tests/test_causal_graph_schema.py tests/test_score_causal_graph_readiness.py && .venv/bin/python scripts/score_causal_graph_readiness.py --include-rejected --limit 10 --out /tmp/cg_readiness_c6_s2.tsv && .venv/bin/python scripts/check_instruction_refs.py && .venv/bin/python scripts/check_vendored_sync.py && .venv/bin/python scripts/validate_component_partonomy.py && .venv/bin/python scripts/validate_sssom_invariants.py --reject-tsv /tmp/needs_curator_review.tsv && .venv/bin/python scripts/audit_duplicate_identifiers.py --check && .venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv
```

---

## 2. Gate-by-Gate Results

| Gate / Validator | Command | Exit Code | Verified Output Summary |
|---|---|---:|---|
| **Causal-Graph Schema & Readiness Unit Tests** | `.venv/bin/python -m pytest -o addopts="" tests/test_causal_graph_schema.py tests/test_score_causal_graph_readiness.py` | `0` | `66 passed` (`39` in `tests/test_causal_graph_schema.py` + `27` in `tests/test_score_causal_graph_readiness.py` in `2.92s`) |
| **Causal-Graph Corpus Readiness Scorer (Sample & Full)** | `.venv/bin/python scripts/score_causal_graph_readiness.py --include-rejected --limit 10 --out /tmp/cg_readiness_c6_s2.tsv` (and full `2,680`-record run to `/tmp/cg_readiness_all_c6_s2.tsv` + `2,611`-record active run to `/tmp/cg_readiness_active_c6_s2.tsv`) | `0` | `wrote 10 ranked records to /tmp/cg_readiness_c6_s2.tsv` (`2,680` total mapped records scored with `--include-rejected`; `2,611` active records scored without `--include-rejected`) |
| **Instruction Reference Integrity** | `.venv/bin/python scripts/check_instruction_refs.py` | `0` | `Scanned 52 agent-instruction file(s) against 88 recipes. OK: every referenced recipe, path, and Python CLI option exists.` |
| **Vendored Governance Artifact Sync** | `.venv/bin/python scripts/check_vendored_sync.py` | `0` | `OK: 24 governed artifacts match the pinned claw revision` |
| **Stock-Component Partonomy Gate (`COMPOSITION_GATE`)** | `.venv/bin/python scripts/validate_component_partonomy.py` | `0` | `component partonomy: 2953 records, 83 decompositions, 502 components, 0 violation(s)` |
| **SSSOM Invariant Validator** | `.venv/bin/python scripts/validate_sssom_invariants.py --reject-tsv /tmp/needs_curator_review.tsv` | `0` | `OK: ingredient_mappings.sssom.tsv passed Rules A, B1, B2, B3, B5, C, D, E, F, G, H, I, J, K, L. /tmp/needs_curator_review.tsv written with header only.` |
| **Duplicate Identifier Baseline Check (`IDENTITY_GATE`)** | `.venv/bin/python scripts/audit_duplicate_identifiers.py --check` | `0` | `15 identifier(s) held by more than one record (35 records, 20 excess)` — matches `mappings/duplicate_identifier_baseline.tsv` (`37` rows across `15` identifier groups, `0` unbaselined duplicates) |
| **Strict Closed-Schema LinkML Instance Validation** | `.venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv` | `0` | `files scanned: 2960, files with ERROR: 0, total ERROR rows: 0` |
| **Tracked Review Index Sync** | `reviews/workflow/latest.yaml` vs `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/workspace/session-orchestration/20261019/mediaingredientmech/verified-evidence-index.json` | `0` | `15` verified stage entries through Cycle 5 Stage 6 (`sha256: b4460b3cabc762006aa32d82c3d9ba7640db8591fa8199fc13b0c69dbdca5268`) match `verified-evidence-index.json` (`sha256: de4a78a5d0ae5dd0e244327efcf9525ca1a396f1dc744353c2f87db5e0e14d3a`). |

---

## 3. Verified Artifact Hashes

- `reviews/workflow/mech-goal-sequence-20261019/cycle-000006/stage-02/revision-0001/coverage_report.md`: verified in `completion.json`
- `reviews/workflow/mech-goal-sequence-20261019/cycle-000006/stage-02/revision-0001/validation.md`: verified in `completion.json`
- `INFRA_TASKS.md`: `dda5707f52661e91f46d96fcbabfc256ac39d4cc865a28a3e5ab6f0536958a5e`
- `reviews/workflow/latest.yaml`: `b4460b3cabc762006aa32d82c3d9ba7640db8591fa8199fc13b0c69dbdca5268`
