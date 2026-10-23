# MediaIngredientMech Cycle 4 Stage 3 (`protein_examples`) Validation Evidence

- **run_id**: `mech-goal-sequence-20261019`
- **cycle**: `4`
- **stage**: `3` (`protein_examples`)
- **revision**: `1`
- **repository**: `CultureBotAI/MediaIngredientMech`
- **base_commit**: `2ae5293f888a1d7193bb4ec79bbc6358e04257cc`
- **date**: `2026-10-23`

---

## 1. Validation Command & Outcome Matrix

All Stage 3 validation and verification checks were executed against the repository checkout at commit `2ae5293f888a1d7193bb4ec79bbc6358e04257cc`:

| # | Gate / Check | Command Executed | Exit Code | Status | Verified Result & Digest |
|---:|---|---|---:|---|---|
| 1 | Closed-schema unit test suite (`ProteinExample` `PE1`–`PE5`, `N5`, `N10`, readiness scorer, skill frontmatter, review routes) | `.venv/bin/python -m pytest -o pythonpath=src -p no:cacheprovider --no-cov -q tests/test_causal_graph_schema.py tests/test_score_causal_graph_readiness.py tests/test_skill_frontmatter.py tests/test_record_review_routes.py` | `0` | **passed** | `178 passed` (`61` in `test_causal_graph_schema.py` including `PE1`–`PE5`, `N5`, `N10`; `16` in `test_score_causal_graph_readiness.py`; `75` in `test_skill_frontmatter.py`; `26` in `test_record_review_routes.py`) |
| 2 | Full-corpus causal-graph & protein-example readiness scoring | `.venv/bin/python scripts/score_causal_graph_readiness.py --ingredients-dir data/ingredients --duplicate-baseline mappings/duplicate_identifier_baseline.tsv --out /tmp/cg_readiness_all_c4_s3.tsv` | `0` | **passed** | `wrote 2611 ranked records to /tmp/cg_readiness_all_c4_s3.tsv` (`sha256: bf2afe2eefc44907ccc776655fe039c44971a07a56c24fdc0cab09b8ad6b2b3c`); `342` `REJECT_PROVISIONAL` records excluded prior to scoring (`2,611 + 342 = 2,953` total YAML files) |
| 3 | Agent instruction & recipe reference integrity | `.venv/bin/python scripts/check_instruction_refs.py` | `0` | **passed** | `Scanned 52 agent-instruction file(s) against 88 recipes. OK: every referenced recipe, path, and Python CLI option exists.` |
| 4 | Vendored governance artifact sync check | `.venv/bin/python scripts/check_vendored_sync.py` | `0` | **passed** | `OK: 24 governed artifacts match the pinned claw revision` |
| 5 | Component partonomy graph validation | `.venv/bin/python scripts/validate_component_partonomy.py` | `0` | **passed** | `component partonomy: 2953 records, 83 decompositions, 502 components, 0 violation(s)` |
| 6 | SSSOM mapping invariants (`Rules A–L`) | `.venv/bin/python scripts/validate_sssom_invariants.py --reject-tsv /tmp/needs_curator_review_c4_s3.tsv` | `0` | **passed** | `OK: ingredient_mappings.sssom.tsv passed Rules A, B1, B2, B3, B5, C, D, E, F, G, H, I, J, K, L.` (`sha256: 4ad210f7d01a71b2f8be94117b41011ce15bfc383ee51d22fae801b3c34261e7`) |
| 7 | Full-corpus closed-schema strict LinkML validation (`2,953` YAML files) | `.venv/bin/python scripts/validate_strict.py data/ingredients --out /tmp/strict_report_c4_s3.tsv` | `0` | **passed** | `files scanned: 2953`, `files with ERROR: 0`, `total ERROR rows: 0` (`sha256: 4ccba8b77ce80cf210105b5284b5953747729aba576ccdeecb81f7db84eb721b`) |
| 8 | Tracked review index parity (`reviews/workflow/latest.yaml` vs. `verified-evidence-index.json`) | Verified 9 entries across Cycles 1–3 Stages 4–6 | `0` | **passed** | `reviews/workflow/latest.yaml` (`sha256: ceb9752cce067ead132443fac90e6ab2a27bd0fd8fd954c97b1dc2e8e2c4c0ed`) matches `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/workspace/session-orchestration/20261019/mediaingredientmech/verified-evidence-index.json` |

---

## 2. Combined Reproducible Validation Command

```bash
.venv/bin/python -m pytest -o pythonpath=src -p no:cacheprovider --no-cov -q tests/test_causal_graph_schema.py tests/test_score_causal_graph_readiness.py tests/test_skill_frontmatter.py tests/test_record_review_routes.py && .venv/bin/python scripts/score_causal_graph_readiness.py --ingredients-dir data/ingredients --duplicate-baseline mappings/duplicate_identifier_baseline.tsv --out /tmp/cg_readiness_all_c4_s3.tsv && .venv/bin/python scripts/check_instruction_refs.py && .venv/bin/python scripts/check_vendored_sync.py && .venv/bin/python scripts/validate_component_partonomy.py && .venv/bin/python scripts/validate_sssom_invariants.py --reject-tsv /tmp/needs_curator_review_c4_s3.tsv && .venv/bin/python scripts/validate_strict.py data/ingredients --out /tmp/strict_report_c4_s3.tsv
```

---

## 3. Prerequisite Blocker Verification (`docs/CAUSAL_GRAPH_CONTRACT.md` Steps 3 & 5)

- **`references_cache/UniProtKB_*.json`**: `0` cached UniProt JSON files exist in `references_cache/`.
- **`just fetch-uniprot` and `just qc-causal-graphs`**: Not yet defined in `justfile` (`docs/CAUSAL_GRAPH_CONTRACT.md` Step 3, line 18).
- **`conf/sibling_pins.yaml`, `mappings/cross_mech_references.tsv`, `mappings/cross_mech_assertions.jsonl`, `mappings/ontology_facts.tsv`, `mappings/cross_mech_links.tsv`**: Not yet present on disk (`docs/CAUSAL_GRAPH_CONTRACT.md` Step 3, line 18).
- **Validated causal-graph / `ProteinExample` writer**: Not yet implemented (`docs/CAUSAL_GRAPH_CONTRACT.md` Step 5, line 20).
- **Result**: `0` ingredient YAML files were modified (`records_modified: 0`), preserving `0` strict validation errors across all `2,953` records (`4a44101e2fb6199658c0fcced12a4cbd2f6624b60afd520a197e3049ccf502c7`).
