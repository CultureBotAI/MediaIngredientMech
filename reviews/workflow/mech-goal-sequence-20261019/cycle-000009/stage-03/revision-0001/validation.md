# Stage 3 (`protein_examples`) Validation Log — Cycle 9

- **Run:** `mech-goal-sequence-20261019`
- **Cycle:** `9`
- **Stage:** `3` (`protein_examples`)
- **Revision:** `1` (`reviews/workflow/mech-goal-sequence-20261019/cycle-000009/stage-03/revision-0001/`)
- **Repository:** `CultureBotAI/MediaIngredientMech`
- **Base commit on `main`:** `f7171728014503f164f9436b09d60a08104eac11`
- **Timestamp (UTC):** `2026-10-30T19:08:23Z`
- **Ingredient YAML / SSSOM records modified:** `0` (`records_modified: 0`)

---

## Executed Validation Commands & Exit Codes

| # | Command | Exit Code | Key Output & Verification Summary |
| ---: | --- | ---: | --- |
| 1 | `env PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/src /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/python -m kg_microbe_workflows validate --profile workflow/mech-workflow.yaml --repository-key mediaingredientmech` | `0` | `Workflow profile valid` (`workflow/mech-workflow.yaml`, `sha256: 45d7c23d67f490cea6b31e336e5d2ac98b7ce8fa4e791bd9d3be092cfdb5a10d`) |
| 2 | `.venv/bin/python -m pytest -o pythonpath=src -p no:cacheprovider --no-cov -q tests/test_causal_graph_schema.py tests/test_score_causal_graph_readiness.py tests/test_skill_frontmatter.py tests/test_record_review_routes.py` | `0` | `178 passed, 12 warnings in 3.06s` (`32` `ProteinExample`/`CausalGraph` schema tests in `tests/test_causal_graph_schema.py`, `146` readiness scorer tests in `tests/test_score_causal_graph_readiness.py`, skill frontmatter and record review route tests all passing) |
| 3 | `.venv/bin/python scripts/validate_strict.py data/ingredients --out /tmp/strict_report_c9_s3.tsv` | `0` | `files scanned: 2953`, `files with ERROR: 0`, `total ERROR rows: 0` (`/tmp/strict_report_c9_s3.tsv`, `sha256: 4ccba8b77ce80cf210105b5284b5953747729aba576ccdeecb81f7db84eb721b`) |
| 4 | `.venv/bin/python scripts/score_causal_graph_readiness.py --ingredients-dir data/ingredients --status mapped --status unmapped --include-rejected --duplicate-baseline mappings/duplicate_identifier_baseline.tsv --out /tmp/cg_readiness_all_c9_s3.tsv` | `0` | `wrote 2953 ranked records to /tmp/cg_readiness_all_c9_s3.tsv` (`sha256: cbb78d73b703763ffbee41887dddd47f10d6412780467893a72f604f6f8c85ce`; `2,496` `IDENTITY_GATE`-eligible, `457` `IDENTITY_GATE`-ineligible; `248` `Cohort E1`: `206` `P1a` + `5` `P1b` + `37` `P1c`; `580` `Cohort E2`: `507` `P2a` + `62` `P2b` + `11` `P2c`; `1,668` `Cohort P3/E3`) |
| 5 | `.venv/bin/python scripts/check_instruction_refs.py` | `0` | `Scanned 52 agent-instruction file(s) against 88 recipes. OK: every referenced recipe, path, and Python CLI option exists.` |
| 6 | `.venv/bin/python scripts/check_vendored_sync.py` | `0` | `OK: 24 governed artifacts match the pinned claw revision` |
| 7 | `.venv/bin/python scripts/validate_sssom_invariants.py --reject-tsv /tmp/needs_curator_review_c9_s3.tsv` | `0` | `OK: ingredient_mappings.sssom.tsv passed Rules A, B1, B2, B3, B5, C, D, E, F, G, H, I, J, K, L. /tmp/needs_curator_review_c9_s3.tsv written with header only.` |
| 8 | `.venv/bin/python scripts/validate_component_partonomy.py` | `0` | `component partonomy: 2953 records, 83 decompositions, 502 components, 0 violation(s)` |
| 9 | In-memory closed-schema `ProteinExample` check via `validate_ingredient(..., target_class="IngredientRecord", schema_path=Path("src/mediaingredientmech/schema/mediaingredientmech.yaml"))` | `0` | `ProteinExample closed-schema validation OK (0 errors)` for populated `ProteinExample` (`UniProtKB:P69786` `PtsG` in `NCBITaxon:83333`) on `MOLECULAR_FUNCTION` node `EC:2.7.1.199` |

---

## Verified Evidence Index & Contract Artifact Digests

- `reviews/workflow/latest.yaml`: `sha256: b95934b9e5d7cb7367df6e6f851bf95db388b4e5a5804449b00a5428084dc045` (`24` verified entries across Cycles 1–8 Stages 4–6; matches `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/workspace/session-orchestration/20261019/mediaingredientmech/verified-evidence-index.json`)
- `INFRA_TASKS.md`: `sha256: dda5707f52661e91f46d96fcbabfc256ac39d4cc865a28a3e5ab6f0536958a5e`
- `MAPPING_SEMANTICS.md`: `sha256: 94aad13ea0fc3df82a37383f388f41432b607b04cac61ae5792ce1a381aef805`
- `docs/CAUSAL_GRAPH_CONTRACT.md`: `sha256: de889fdea9ad18e6cf3502461d779e76ef6e99f923e374b0a5309fe163871d65`
- `src/mediaingredientmech/schema/mediaingredientmech.yaml`: `sha256: bb43dee29b21fdee72a48022456e733e49e95824c4c09674f9b3165c290fe012`
- `mappings/duplicate_identifier_baseline.tsv`: `sha256: 723f613de746bf44b38e19be9786cd1ee7fb719256fbc6195b8b1e20477d5720`
- `data/curated/mapped_ingredients.yaml`: `sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b`
- `data/curated/unmapped_ingredients.yaml`: `sha256: 8f574be094e741f1d59d55618cc14bf375304644732508bd7a5cd4a817c7fce2`
