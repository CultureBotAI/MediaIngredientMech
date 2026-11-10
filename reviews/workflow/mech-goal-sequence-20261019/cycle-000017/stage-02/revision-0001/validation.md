# Cycle 17 Stage 2 (`causal_graphs`) — Validation & Gate Verification Report

- **Run ID:** `mech-goal-sequence-20261019`
- **Repository:** `CultureBotAI/MediaIngredientMech` (`mediaingredientmech`)
- **Cycle / Stage:** Cycle `17`, Stage `2` (`causal_graphs`), Revision `1` (`revision-0001`)
- **Workflow Token:** `[MECH-WORKFLOW-afbe3d51d051538c241d1cd1]`
- **Evaluated Commit (`main`):** `66b9d1bd1e1f37de733b4b45a48c7baa0f1e3dcc`

---

## 1. Prior Closure & Tracked Review Index Verification

Before executing Stage 2 (`causal_graphs`), prior stage closures and the tracked workflow evidence index were verified:

1. **Prior Cycle & Stage Closures:**
   - Cycle 16 Stage 6 (`infrastructure`) closed on `main` via PR `#1292` (`4c7e36468db89262af45ca6f29bc582668121824`, `head_sha`: `9583dc80614073741305e5fad7db617ad871cf6d`).
   - Cycle 17 Stage 1 (`add_records`) closed on `main` via PR `#1293` (`66b9d1bd1e1f37de733b4b45a48c7baa0f1e3dcc`, `head_sha`: `16819b2cefce4b6173174f72af90bd4190975907`). Because Stage 1 has `required_outputs: []` in [effective-workflow.json](file:///Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/workspace/session-orchestration/20261019/mediaingredientmech/effective-workflow.json), it adds no `goal_evidence` entry to `verified-evidence-index.json`.
2. **Synchronization of [reviews/workflow/latest.yaml](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/reviews/workflow/latest.yaml):**
   - Verified against [/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/workspace/session-orchestration/20261019/mediaingredientmech/verified-evidence-index.json](file:///Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/workspace/session-orchestration/20261019/mediaingredientmech/verified-evidence-index.json) (`48` verified closure entries through Cycle 16 Stage 6 PR `#1292`).
   - [reviews/workflow/latest.yaml](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/reviews/workflow/latest.yaml) (`sha256: 82fe7a70e929502938c0475a66c42825d107bea4428d67669d5c50f41d05cccb`) already matches `verified-evidence-index.json` (`48` entries through Cycle 16 Stage 6 PR `#1292`).

---

## 2. Executed Validation & Readiness Commands

All repository gates, causal-graph schema and readiness unit tests, readiness scoring runs, and strict LinkML/SSSOM/partonomy/duplicate-identifier checks were executed against the live workspace at commit `66b9d1bd1e1f37de733b4b45a48c7baa0f1e3dcc` (cleaning temporary scratch outputs immediately after verification):

| # | Gate / Check | Command Executed | Exit Code | Key Verified Output |
| :-: | :--- | :--- | :---: | :--- |
| 1 | **Workflow Profile Validation** (`mediaingredientmech-evolve-workflow` preflight) | `env PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/src /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/python -m kg_microbe_workflows validate --profile workflow/mech-workflow.yaml --parent workflow/parent/mech-cycle.yaml --schema workflow/parent/workflow.yaml` | `0` | `Workflow profile valid` |
| 2 | **Causal-Graph Schema & Readiness Unit Test Suite** | `.venv/bin/python -m pytest --no-cov -p no:cacheprovider -q tests/test_causal_graph_schema.py tests/test_score_causal_graph_readiness.py` | `0` | `66 passed, 12 warnings in 2.83s` (`test_causal_graph_schema.py` + `test_score_causal_graph_readiness.py`) |
| 3 | **Causal-Graph Readiness Scorer (`--limit 25` & Full Corpus)** | `.venv/bin/python scripts/score_causal_graph_readiness.py --limit 25 --out <scratch>/cg_readiness_c17_s2_top25.tsv && .venv/bin/python scripts/score_causal_graph_readiness.py --out <scratch>/cg_readiness_active_c17_s2.tsv && .venv/bin/python scripts/score_causal_graph_readiness.py --include-rejected --out <scratch>/cg_readiness_all_c17_s2.tsv` | `0` | Top-25 TSV (`sha256: 5a3c5bf4f35158627940614670df85af4711e18ed831d6c77938c049e4a21394`); active `MAPPED` TSV (`2,611` rows, `sha256: 6df1804418e6454bd7689ab201aeaa9b33f7db5fc5f3a95d5588a7dac913f102`); all-mapped-dir TSV (`2,681` rows, `sha256: f9454fe89e94487a4cde0f6ac9443ff369110a1497d94263345dc3304887e769`) |
| 4 | **Agent Instruction Recipe Check** | `.venv/bin/python scripts/check_instruction_refs.py` | `0` | `Scanned 54 agent-instruction file(s) against 88 recipes. OK: every referenced recipe, path, and Python CLI option exists.` |
| 5 | **Vendored Governance Sync Check** | `.venv/bin/python scripts/check_vendored_sync.py` | `0` | `OK: 26 governed artifacts match the pinned claw revision` |
| 6 | **Component Partonomy Gate** (`MAPPING_SEMANTICS.md` §6) | `.venv/bin/python scripts/validate_component_partonomy.py` | `0` | `component partonomy: 2956 records, 83 decompositions, 502 components, 0 violation(s)` |
| 7 | **SSSOM Invariant Gate** (`MAPPING_SEMANTICS.md` §4 & §7.1 A5) | `.venv/bin/python scripts/validate_sssom_invariants.py --reject-tsv <scratch>/needs_curator_review_c17s2.tsv` | `0` | `OK: ingredient_mappings.sssom.tsv passed Rules A, B1, B2, B3, B5, C, D, E, F, G, H, I, J, K, L.` (`0` rejected rows) |
| 8 | **Duplicate Identifier Baseline Gate** (`MAPPING_SEMANTICS.md` §7.1 A2) | `.venv/bin/python scripts/audit_duplicate_identifiers.py --check` | `0` | `15 identifier(s) held by more than one record (35 records, 20 excess) ... OK: duplicate identifiers match the tracked baseline exactly.` |
| 9 | **Strict LinkML Schema & Instance Validation Gate** | `.venv/bin/python scripts/validate_strict.py --out <scratch>/instance_validation_failures_c17s2.tsv` | `0` | `files scanned: 2963, files with ERROR: 0, total ERROR rows: 0` |

---

## 3. Prerequisite Gap Check (`docs/CAUSAL_GRAPH_CONTRACT.md` Status Table)

| Step in [docs/CAUSAL_GRAPH_CONTRACT.md](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/docs/CAUSAL_GRAPH_CONTRACT.md) Status Table | Documented Status | Live Verification in Repository (`66b9d1bd1e1f37de733b4b45a48c7baa0f1e3dcc`) |
| :--- | :---: | :--- |
| **Step 1:** Curator contract (`docs/CAUSAL_GRAPH_CONTRACT.md`) and `MAPPING_SEMANTICS.md` Section 7 | `included` | Verified present (`sha256: de889fdea9ad18e6cf3502461d779e76ef6e99f923e374b0a5309fe163871d65` and `sha256: 6b52f2ac48109ddd5d81996a136b19776cab55efa69a5ec832cf716d6885a062`). |
| **Step 2:** Schema (`causal_graphs` classes `CausalGraph`, `CausalNode`, `CausalEdge`, `EvidenceItem`, `ProteinExample` and 9 enums) + rule tests (`tests/test_causal_graph_schema.py`) | `included` | Present in [src/mediaingredientmech/schema/mediaingredientmech.yaml](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/src/mediaingredientmech/schema/mediaingredientmech.yaml#L881-L1161); `66` tests pass across `test_causal_graph_schema.py` and `test_score_causal_graph_readiness.py`. |
| **Step 3:** `conf/sibling_pins.yaml`, committed snapshots (`mappings/cross_mech_*.{tsv,jsonl}`, `mappings/ontology_facts.tsv`), refresh/fetch recipes, and offline gate `just qc-causal-graphs` | `planned` | Confirmed absent: `0` recipes matching `qc-causal-graphs` in [justfile](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/justfile) (`88` total recipes) and no snapshot files under `conf/` or `mappings/`. |
| **Step 4:** `culturebotai-claw` MIM coverage stanza, narrowed record globs, and evidence walker reading graphs | `separate integration work` | Confirmed `scripts/run_shared_evidence_validator.py` does not yet walk `causal_graphs`. |
| **Step 5:** Graph writer, one-record canary (`Na2moo4_X_2_H2o.yaml`), and worked examples | `planned` | Confirmed `0 / 2,956` records carry `causal_graphs`; blocked on Step 3 (`just qc-causal-graphs`) and Step 5 writer per [docs/CAUSAL_GRAPH_CONTRACT.md](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/docs/CAUSAL_GRAPH_CONTRACT.md) §10 and [.claude/skills/curate-causal-graphs/SKILL.md](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.claude/skills/curate-causal-graphs/SKILL.md). |
| **Step 6:** Consumers (readiness-scorer graph columns, ingredient-page panels, `docs/data/cross_mech_links.json`) | `planned` | Confirmed absent in [scripts/score_causal_graph_readiness.py](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/scripts/score_causal_graph_readiness.py) and [src/mediaingredientmech/utils/browser_export.py](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/src/mediaingredientmech/utils/browser_export.py). |
| **Step 7:** Mechanistic graphs on species records first, then `SPECIATION` proposals (`proposals/causal_graphs/<stem>.yaml`) | `planned` | Confirmed `proposals/causal_graphs/` does not exist yet. |

---

## 4. Artifact Integrity & Non-Mutation Verification

- **Ingredient YAML & Curated Collections:** `0` files modified (`git status --short` clean outside `reviews/workflow/`; [data/curated/mapped_ingredients.yaml](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/data/curated/mapped_ingredients.yaml) `sha256: 774718362b921a560f8474a5d77874f2779e44ac5a6afc992040084a701ea628`; [data/curated/unmapped_ingredients.yaml](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/data/curated/unmapped_ingredients.yaml) `sha256: 284adda3e7ac0940308770552afa0419aa4f30372ddb2074b39b6da630478fb1`; sorted per-record `shasum -a 256` manifest `sha256: 1e978e977f3ce6e522117a4e7e06d25b4fb9d2eeda34a05ede17ad0b250d322d` across `2,956` YAML files).
- **SSSOM Mapping Table ([mappings/ingredient_mappings.sssom.tsv](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/mappings/ingredient_mappings.sssom.tsv)):** Unmodified (`sha256: d5f76fc404967477903fafc79eaba86ecfef9e2c391926ec08c3c1af4a5220b6`).
- **Infrastructure Backlog ([INFRA_TASKS.md](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/INFRA_TASKS.md)):** Unmodified (`sha256: dda5707f52661e91f46d96fcbabfc256ac39d4cc865a28a3e5ab6f0536958a5e`).
- **Stage 2 Output Artifacts:**
  - [reviews/workflow/mech-goal-sequence-20261019/cycle-000017/stage-02/revision-0001/coverage_report.md](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/reviews/workflow/mech-goal-sequence-20261019/cycle-000017/stage-02/revision-0001/coverage_report.md) (`sha256: fa0f6fbbaab1644a7551b4b155b9fcc1bb8d277194a5f9dee05f2bcfbd6eb669`)
  - [reviews/workflow/mech-goal-sequence-20261019/cycle-000017/stage-02/revision-0001/validation.md](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/reviews/workflow/mech-goal-sequence-20261019/cycle-000017/stage-02/revision-0001/validation.md) (this file)
