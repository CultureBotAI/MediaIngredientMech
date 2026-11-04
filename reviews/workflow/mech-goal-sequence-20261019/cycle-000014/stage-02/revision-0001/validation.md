# Cycle 14 Stage 2 (`causal_graphs`) — Validation & Gate Verification Report

- **Run ID:** `mech-goal-sequence-20261019`
- **Repository:** `CultureBotAI/MediaIngredientMech` (`mediaingredientmech`)
- **Cycle / Stage:** Cycle `14`, Stage `2` (`causal_graphs`), Revision `1` (`revision-0001`)
- **Workflow Token:** `[MECH-WORKFLOW-fb0459db40325c0f1badd29f]`
- **Evaluated Commit (`main`):** `6ef8b63f56a593d509ea3a3810ebe4fa45b6bf33`

---

## 1. Prior Closure & Tracked Review Index Verification

Before executing Stage 2 (`causal_graphs`), prior stage closures and the tracked workflow evidence index were verified:

1. **Prior Cycle & Stage Closures:**
   - Cycle 13 Stage 5 (`remediate_findings`) closed on `main` via PR `#1129` (`62e73759a6a12643cdc2b6acc8f8bc736981bf30`).
   - Cycle 13 Stage 6 (`implement_infrastructure`) closed on `main` via PR `#1135` (`0ec77480e8202c045a2569d9b18fe8983f27f892`).
   - Cycle 14 Stage 1 (`add_records`) closed on `main` via PR `#1137` (`6ef8b63f56a593d509ea3a3810ebe4fa45b6bf33`). Because Stage 1 has `required_outputs: []` in [effective-workflow.json](file:///Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/workspace/session-orchestration/20261019/mediaingredientmech/effective-workflow.json), it adds no `goal_evidence` entry to `verified-evidence-index.json`.
2. **Synchronization of [reviews/workflow/latest.yaml](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/reviews/workflow/latest.yaml):**
   - Verified against [/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/workspace/session-orchestration/20261019/mediaingredientmech/verified-evidence-index.json](file:///Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/workspace/session-orchestration/20261019/mediaingredientmech/verified-evidence-index.json) (`39` verified closure entries through Cycle 13 Stage 6 PR `#1135`).
   - [reviews/workflow/latest.yaml](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/reviews/workflow/latest.yaml) (`sha256: 3fa8a6b1175d90fd88a90569a093f89bcdc26eed4620d969766e0def106a1194`) already matches `verified-evidence-index.json` exactly (`39` entries through Cycle 13 Stage 6 PR `#1135`).

---

## 2. Executed Validation & Readiness Commands

All repository gates, causal-graph schema and readiness unit tests, readiness scoring runs, and strict LinkML/SSSOM/partonomy/duplicate-identifier checks were executed against the live workspace at commit `6ef8b63f56a593d509ea3a3810ebe4fa45b6bf33`:

| # | Gate / Check | Command Executed | Exit Code | Key Verified Output |
| :-: | :--- | :--- | :---: | :--- |
| 1 | **Workflow Profile Validation** (`mediaingredientmech-evolve-workflow` preflight) | `PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/src /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/python -m kg_microbe_workflows validate --repo mediaingredientmech --root /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw --repo-root /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech` | `0` | `Workflow profile valid: mediaingredientmech (6 goals)` |
| 2 | **Causal-Graph Schema & Readiness Unit Test Suite** | `.venv/bin/pytest tests/test_causal_graph_schema.py tests/test_score_causal_graph_readiness.py` | `0` | `66 passed in 0.56s` (`47` tests in `test_causal_graph_schema.py` + `19` tests in `test_score_causal_graph_readiness.py`) |
| 3 | **Causal-Graph Readiness Scorer (`--limit 25` & Full Corpus)** | `.venv/bin/python scripts/score_causal_graph_readiness.py --limit 25 --out /tmp/cg_readiness_c14_s2_top25.tsv && .venv/bin/python scripts/score_causal_graph_readiness.py --out /tmp/cg_readiness_active_c14_s2.tsv && .venv/bin/python scripts/score_causal_graph_readiness.py --include-rejected --out /tmp/cg_readiness_all_c14_s2.tsv` | `0` | Top-25 TSV (`sha256: 5a3c5bf4f35158627940614670df85af4711e18ed831d6c77938c049e4a21394`); active `MAPPED` TSV (`2,611` rows, `sha256: 6df1804418e6454bd7689ab201aeaa9b33f7db5fc5f3a95d5588a7dac913f102`); all-mapped-dir TSV (`2,681` rows, `sha256: f9454fe89e94487a4cde0f6ac9443ff369110a1497d94263345dc3304887e769`) |
| 4 | **Agent Instruction Recipe Check** | `.venv/bin/python scripts/check_instruction_refs.py` | `0` | `Scanned 52 agent-instruction file(s) against 88 recipes. OK` |
| 5 | **Vendored Governance Sync Check** | `.venv/bin/python scripts/check_vendored_sync.py` | `0` | `OK: 26 governed artifacts match the pinned claw revision` |
| 6 | **Component Partonomy Gate** (`PARTONOMY_SEPARATION` §2.3) | `.venv/bin/python scripts/validate_component_partonomy.py` | `0` | `component partonomy: 2956 records, 83 decompositions, 502 components, 0 violation(s)` |
| 7 | **SSSOM Invariant Gate** (`ANCHOR_INDEPENDENCE` §2.1) | `.venv/bin/python scripts/validate_sssom_invariants.py --reject-tsv /tmp/needs_curator_review.tsv` | `0` | `OK: ingredient_mappings.sssom.tsv passed Rules A, B1, B2, B3, B5, C, D, E, F, G, H, I, J, K, L.` (`0` rejected rows) |
| 8 | **Duplicate Identifier Baseline Gate** (`IDENTITY_GATE` §3.3) | `.venv/bin/python scripts/audit_duplicate_identifiers.py --check` | `0` | `15 identifier(s) held by more than one record (35 records, 20 excess) ... OK: duplicate identifiers match the tracked baseline exactly.` |
| 9 | **Strict LinkML Schema & Instance Validation Gate** | `.venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv` | `0` | `files scanned: 2963, files with ERROR: 0, total ERROR rows: 0` |

---

## 3. Prerequisite Gap Check (`docs/CAUSAL_GRAPH_CONTRACT.md` §10)

| Rollout Deliverable in [docs/CAUSAL_GRAPH_CONTRACT.md](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/docs/CAUSAL_GRAPH_CONTRACT.md) §10 | Documented Status in §10 | Live Verification in Repository (`6ef8b63f56a593d509ea3a3810ebe4fa45b6bf33`) |
| :--- | :---: | :--- |
| LinkML classes `CausalGraph`, `CausalNode`, `CausalEdge`, `CausalEvidence`, `OrganismContext`, `CellularLocation` + 5 enums | Shipped (`#573` / `#575`) | Present in [src/mediaingredientmech/schema/mediaingredientmech.yaml](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/src/mediaingredientmech/schema/mediaingredientmech.yaml#L276-L702); `47` schema tests pass in [tests/test_causal_graph_schema.py](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/tests/test_causal_graph_schema.py). |
| Readiness scorer `scripts/score_causal_graph_readiness.py` | Shipped (`#573` / `#575`) | Present in [scripts/score_causal_graph_readiness.py](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/scripts/score_causal_graph_readiness.py); `19` unit tests pass in [tests/test_score_causal_graph_readiness.py](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/tests/test_score_causal_graph_readiness.py). |
| Validator `just qc-causal-graphs` enforcing §9 error codes (`ANCHOR_MISMATCH`, `SPECIES_BRIDGE_MISSING`, `PARTONOMY_OVERLAP`, `PROVENANCE_EMPTY`, `ROLE_GRAPH_CONFLICT`, `NAMED_MEDIUM_GRAPH`) | `_pending_` | Confirmed absent: `0` recipes matching `causal` in [justfile](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/justfile) (`88` total recipes) and no `scripts/validate_causal_graphs.py` script. |
| Pilot `causal_graphs` records (`3`–`5` top readiness candidates across anhydrous, hydrate salt, vitamin cofactor) | `_pending_` | Confirmed `0 / 2,956` records carry `causal_graphs`; blocked on `just qc-causal-graphs`, native writer/CLI, and browser export projection per [.claude/skills/curate-causal-graphs/SKILL.md](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.claude/skills/curate-causal-graphs/SKILL.md). |
| Browser export (`docs/data/ingredients.json`) includes `causal_graphs` summary | `_pending_` | Confirmed absent in [src/mediaingredientmech/utils/browser_export.py](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/src/mediaingredientmech/utils/browser_export.py#L140-L234) (`export_browser_data()` projects 11 fields and omits `causal_graphs`). |

---

## 4. Artifact Integrity & Non-Mutation Verification

- **Ingredient YAML & Curated Collections:** `0` files modified (`git status --short` clean outside `reviews/workflow/`; whole-corpus composite `sha256: 8e2972ec31744c09572ac2f513da673b17467a9d11974cfab88c68cc96c44f76` across `2,956` YAML files).
- **SSSOM Mapping Table ([mappings/ingredient_mappings.sssom.tsv](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/mappings/ingredient_mappings.sssom.tsv)):** Unmodified (`sha256: d5f76fc404967477903fafc79eaba86ecfef9e2c391926ec08c3c1af4a5220b6`).
- **Infrastructure Backlog ([INFRA_TASKS.md](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/INFRA_TASKS.md)):** Unmodified (`sha256: dda5707f52661e91f46d96fcbabfc256ac39d4cc865a28a3e5ab6f0536958a5e`, respecting `infrastructure_note_policy.allow_edits: false`).
- **Stage 2 Required Output Artifacts:**
  - [reviews/workflow/mech-goal-sequence-20261019/cycle-000014/stage-02/revision-0001/coverage_report.md](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/reviews/workflow/mech-goal-sequence-20261019/cycle-000014/stage-02/revision-0001/coverage_report.md) (`sha256: 397687dfb366984d2abb64d79cc3f37653259e53f60ae956427048e5698822ff`)
  - [reviews/workflow/mech-goal-sequence-20261019/cycle-000014/stage-02/revision-0001/validation.md](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/reviews/workflow/mech-goal-sequence-20261019/cycle-000014/stage-02/revision-0001/validation.md) (this file)
