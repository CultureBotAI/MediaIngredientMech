# Stage 3 (`protein_examples`) Validation Report — Cycle 8 (`mech-goal-sequence-20261019`)

- **Run ID:** `mech-goal-sequence-20261019`
- **Cycle:** `8`
- **Stage:** `3` (`protein_examples`)
- **Revision:** `revision-0001`
- **Repository:** `CultureBotAI/MediaIngredientMech` (`mediaingredientmech`)
- **Base Commit on `main`:** `dc363220af5b8db2f08b36f050300a432c7a8815`
- **Workflow Profile SHA-256:** `059b5b9401ffeb04483cf7a46570f7f2f3c8c7fe6e574d80954bf71233cc609a`
- **Validation Status:** `passed`

---

## 1. Combined Validation Command Executed

```bash
.venv/bin/python -m pytest -o pythonpath=src -p no:cacheprovider --no-cov -q tests/test_causal_graph_schema.py tests/test_score_causal_graph_readiness.py tests/test_skill_frontmatter.py tests/test_record_review_routes.py && .venv/bin/python scripts/validate_strict.py data/ingredients --out /tmp/strict_report_c8_s3.tsv && .venv/bin/python scripts/score_causal_graph_readiness.py --ingredients-dir data/ingredients --status mapped --status unmapped --include-rejected --duplicate-baseline mappings/duplicate_identifier_baseline.tsv --out /tmp/cg_readiness_all_c8_s3.tsv && .venv/bin/python scripts/check_instruction_refs.py && .venv/bin/python scripts/check_vendored_sync.py && .venv/bin/python scripts/validate_sssom_invariants.py --reject-tsv /tmp/needs_curator_review_c8_s3.tsv && .venv/bin/python scripts/validate_component_partonomy.py
```

---

## 2. Sub-Gate Results

| # | Validation Gate | Command | Result | Details |
| ---: | :--- | :--- | :---: | :--- |
| 1 | **Causal-Graph & `ProteinExample` Schema + Readiness + Skill Frontmatter + Review Route Tests** | `.venv/bin/python -m pytest -o pythonpath=src -p no:cacheprovider --no-cov -q tests/test_causal_graph_schema.py tests/test_score_causal_graph_readiness.py tests/test_skill_frontmatter.py tests/test_record_review_routes.py` | **PASSED (`0`)** | `178 passed, 12 warnings in 3.11s` — Includes `ProteinExample` fleet parity and closed-schema validation tests (`N5` rejects `UniProtKB:` as `CausalNode.grounding`; `N10` rejects `NCBITaxon:` as `CausalNode.grounding`). |
| 2 | **Strict Closed-Schema YAML Instance Validation (`validate_strict.py`)** | `.venv/bin/python scripts/validate_strict.py data/ingredients --out /tmp/strict_report_c8_s3.tsv` | **PASSED (`0`)** | `files scanned: 2953`, `files with ERROR: 0`, `total ERROR rows: 0` (`14,768` advisory `WARN` rows; TSV SHA-256 `4ccba8b77ce80cf210105b5284b5953747729aba576ccdeecb81f7db84eb721b`). |
| 3 | **Whole-Corpus Causal-Graph & Protein-Example Readiness Scorer (`score_causal_graph_readiness.py`)** | `.venv/bin/python scripts/score_causal_graph_readiness.py --ingredients-dir data/ingredients --status mapped --status unmapped --include-rejected --duplicate-baseline mappings/duplicate_identifier_baseline.tsv --out /tmp/cg_readiness_all_c8_s3.tsv` | **PASSED (`0`)** | `wrote 2953 ranked records to /tmp/cg_readiness_all_c8_s3.tsv` (`2,496` `IDENTITY_GATE`-eligible, `457` ineligible; TSV SHA-256 `cbb78d73b703763ffbee41887dddd47f10d6412780467893a72f604f6f8c85ce`). |
| 4 | **Agent-Instruction Reference Check (`check_instruction_refs.py`)** | `.venv/bin/python scripts/check_instruction_refs.py` | **PASSED (`0`)** | `Scanned 52 agent-instruction file(s) against 88 recipes. OK: every referenced recipe, path, and Python CLI option exists.` |
| 5 | **Vendored Workflow Governance Sync (`check_vendored_sync.py`)** | `.venv/bin/python scripts/check_vendored_sync.py` | **PASSED (`0`)** | `OK: 24 governed artifacts match the pinned claw revision` |
| 6 | **SSSOM Invariant Validation (`validate_sssom_invariants.py`)** | `.venv/bin/python scripts/validate_sssom_invariants.py --reject-tsv /tmp/needs_curator_review_c8_s3.tsv` | **PASSED (`0`)** | `OK: ingredient_mappings.sssom.tsv passed Rules A, B1, B2, B3, B5, C, D, E, F, G, H, I, J, K, L. /tmp/needs_curator_review_c8_s3.tsv written with header only.` |
| 7 | **Component Partonomy Validation (`validate_component_partonomy.py`)** | `.venv/bin/python scripts/validate_component_partonomy.py` | **PASSED (`0`)** | `component partonomy: 2953 records, 83 decompositions, 502 components, 0 violation(s)` |
| 8 | **In-Memory `ProteinExample` Closed-Schema Verification (`write_validated.validate_ingredient`)** | In-memory verification of `ProteinExample` attachment on `Glucose.yaml` (`UniProtKB:P69786` `PtsG`, `NCBITaxon:83333`) and `Na2moo4_X_2_H2o.yaml` (`UniProtKB:P09833` `ModA`, `NCBITaxon:83333`) | **PASSED (`0`)** | `0` validation errors on both positive records; confirmed deterministic rejection on malformed `uniprot_id` (`UniProtKB:P09833-2`), malformed `taxon_id`, invalid `entry_status`, bad `retrieved_on`, empty `evidence`, and `UniProtKB:`/`NCBITaxon:` in `CausalNode.grounding`. |

---

## 3. Corpus & Tracked Artifact Integrity Summary

- **Ingredient corpus files (`data/ingredients/**/*.yaml`):** `2,953` files (`2,680` mapped + `273` unmapped); composite SHA-256 `4a44101e2fb6199658c0fcced12a4cbd2f6624b60afd520a197e3049ccf502c7`; `0` records modified (`records_modified: 0`).
- **Infrastructure task ledger (`INFRA_TASKS.md`):** SHA-256 `dda5707f52661e91f46d96fcbabfc256ac39d4cc865a28a3e5ab6f0536958a5e`.
- **Tracked review index (`reviews/workflow/latest.yaml`):** SHA-256 `c796d64c158ecf8189fee775fdbf189c4fbe8d3d16759395cefd2188dec06a5e` (synchronized with `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/workspace/session-orchestration/20261019/mediaingredientmech/verified-evidence-index.json`, `21` verified entries across Cycles 1–7 Stages 4–6).
