# MediaIngredientMech Causal-Graph Validation Log — Cycle 8, Stage 2 (`causal_graphs`)

- **Run ID:** `mech-goal-sequence-20261019`
- **Cycle / Stage / Revision:** `cycle-000008` / `stage-02` (`causal_graphs`) / `revision-0001`
- **Goal Instruction ID:** `MECH-WORKFLOW-7d0f20c28584e6e28bf1b5a9` (`/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/workspace/session-orchestration/20261019/mediaingredientmech/instructions/7d0f20c28584e6e28bf1b5a9.json`)
- **Repository:** `CultureBotAI/MediaIngredientMech`
- **Baseline `origin/main` Commit:** `9165e2d9fefa9d0225661d2f8a4933a7e0a74c13` (`chore(workflow): record cycle 8 stage 1 add-records review and validation (#974)`)

---

## 1. Executed Validation Commands and Exact Results

| # | Check / Validator | Command Executed | Exit Code | Summary of Output |
|---:|---|---|---:|---|
| 1 | **Workflow Profile Preflight (`kg_microbe_workflows validate`)** | `PYTHONPATH="/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/src" "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/python" -m kg_microbe_workflows validate --profile "/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/workflow/mech-workflow.yaml" --parent "/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/workflow/parent/mech-cycle.yaml" --schema "/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/workflow/parent/workflow.yaml"` | `0` | `Workflow profile valid` |
| 2 | **Causal-Graph Schema & Readiness Scorer Unit Tests (`pytest`)** | `.venv/bin/python -m pytest --no-cov -p no:cacheprovider -q tests/test_causal_graph_schema.py tests/test_score_causal_graph_readiness.py` | `0` | `66 passed, 12 warnings in 3.08s` (`49` causal-graph schema tests `P1–P7` and `N1–N18` + `17` readiness scorer tests) |
| 3 | **Causal-Graph Readiness Scorer CLI (Top 25 & Full Active Corpus)** | `.venv/bin/python scripts/score_causal_graph_readiness.py --ingredients-dir data/ingredients --duplicate-baseline mappings/duplicate_identifier_baseline.tsv --limit 25 --out /tmp/cg_readiness_c8_s2_top25.tsv && .venv/bin/python scripts/score_causal_graph_readiness.py --ingredients-dir data/ingredients --duplicate-baseline mappings/duplicate_identifier_baseline.tsv --limit 3000 --out /tmp/cg_readiness_active_c8_s2.tsv` | `0` | `wrote 25 ranked records to /tmp/cg_readiness_c8_s2_top25.tsv` (`sha256: 5a3c5bf4f35158627940614670df85af4711e18ed831d6c77938c049e4a21394`); `wrote 2611 ranked records to /tmp/cg_readiness_active_c8_s2.tsv` (`sha256: bf2afe2eefc44907ccc776655fe039c44971a07a56c24fdc0cab09b8ad6b2b3c`) |
| 4 | **Instruction Reference Check** | `.venv/bin/python scripts/check_instruction_refs.py` | `0` | `Scanned 52 agent-instruction file(s) against 88 recipes. OK: every referenced recipe, path, and Python CLI option exists.` |
| 5 | **Vendored Governance Sync Check** | `.venv/bin/python scripts/check_vendored_sync.py` | `0` | `OK: 24 governed artifacts match the pinned claw revision` |
| 6 | **Component Partonomy Validator** | `.venv/bin/python scripts/validate_component_partonomy.py` | `0` | `component partonomy: 2953 records, 83 decompositions, 502 components, 0 violation(s)` |
| 7 | **SSSOM Invariant Validator** | `.venv/bin/python scripts/validate_sssom_invariants.py --reject-tsv /tmp/needs_curator_review.tsv` | `0` | `OK: ingredient_mappings.sssom.tsv passed Rules A, B1, B2, B3, B5, C, D, E, F, G, H, I, J, K, L. /tmp/needs_curator_review.tsv written with header only.` |
| 8 | **Duplicate-Identifier Baseline Check** | `.venv/bin/python scripts/audit_duplicate_identifiers.py --check` | `0` | `15 identifier(s) held by more than one record (35 records, 20 excess) ... OK: duplicate identifiers match the tracked baseline exactly.` |
| 9 | **Closed-Schema Strict YAML Validation (`validate_strict.py`)** | `.venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv` | `0` | `files scanned: 2960, files with ERROR: 0, total ERROR rows: 0` |

---

## 2. Prerequisite & Contract Gate Verification (`docs/CAUSAL_GRAPH_CONTRACT.md`)

1. **`docs/CAUSAL_GRAPH_CONTRACT.md` Status Table (Lines 21–32):**
   - **Step 1 (`landed`):** `docs/CAUSAL_GRAPH_CONTRACT.md` (`sha256: de889fdea9ad18e6cf3502461d779e76ef6e99f923e374b0a5309fe163871d65`) + `MAPPING_SEMANTICS.md` Section 7 (`sha256: 94aad13ea0fc3df82a37383f388f41432b607b04cac61ae5792ce1a381aef805`).
   - **Step 2 (`landed`):** `src/mediaingredientmech/schema/mediaingredientmech.yaml` (`sha256: bb43dee29b21fdee72a48022456e733e49e95824c4c09674f9b3165c290fe012`), `tests/test_causal_graph_schema.py` (`sha256: 38b0d02b048ce069bb03d6e3e3475894ed8121d152ea4a7b6211123a82df14f3`), and `scripts/score_causal_graph_readiness.py` (`sha256: 32411c33b4c7f10fd1753bfa245872b455ee14293075b76469cdafc713169354`).
   - **Steps 3–7 (`planned`):** `conf/sibling_pins.yaml`, `mappings/cross_mech_references.tsv`, `mappings/cross_mech_assertions.jsonl`, `mappings/ontology_facts.tsv`, `mappings/cross_mech_links.tsv`, `just qc-causal-graphs`, and the native causal-graph writer are all verified absent on `main` (`9165e2d9fefa9d0225661d2f8a4933a7e0a74c13`).
2. **Skill Guardrail Compliance (`.claude/skills/curate-causal-graphs/SKILL.md`):**
   - Because Step 3 (`just qc-causal-graphs` and committed snapshot inputs) and Step 5 (native causal-graph writer) are still marked `planned` and not yet implemented, `0` ingredient YAML files were modified (`records_modified: 0`), preserving `data/ingredients/{mapped,unmapped}/*.yaml` (`composite sha256: 3b760eeec31525e7bdf8e45623ec53fb4ac521866d9ab5bafeea9160a4d2d99f`) and `data/curated/{mapped,unmapped}_ingredients.yaml` unchanged.

---

## 3. Artifact Inventory & Digests

| Artifact Path | SHA-256 Digest | Purpose |
|---|---|---|
| `reviews/workflow/mech-goal-sequence-20261019/cycle-000008/stage-02/revision-0001/coverage_report.md` | `9086c965ed6d0987a1c89d06f43aa6b728acc3deb20f1864130ccbdfb5fc9e63` | Whole-corpus (`2,953` records) causal-graph eligibility & readiness audit, 12-record source-grounded mechanism/protein-example candidate review, and blocker matrix |
| `reviews/workflow/mech-goal-sequence-20261019/cycle-000008/stage-02/revision-0001/validation.md` | *(self)* | Validation command log, prerequisite verification, and artifact inventory for Cycle 8 Stage 2 |
| `INFRA_TASKS.md` | `dda5707f52661e91f46d96fcbabfc256ac39d4cc865a28a3e5ab6f0536958a5e` | Tracked infrastructure backlog (`tasks: []`, unchanged) |
| `reviews/workflow/latest.yaml` | `c796d64c158ecf8189fee775fdbf189c4fbe8d3d16759395cefd2188dec06a5e` | Verified closure evidence index (`21` entries through Cycle 7 Stage 6 `PR #973`) |
