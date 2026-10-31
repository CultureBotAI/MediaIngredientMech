# Stage 1 Validation Report — Cycle 12

- **Run ID:** `mech-goal-sequence-20261019`
- **Cycle:** `12` (`cycle-000012`)
- **Stage:** `1` (`stage-01` — `add_records`)
- **Revision:** `1` (`revision-0001`)
- **Source Revision:** `bd337417ad5f04537f6f02dc81d37e229889900e` (`main`)

## 1. Workflow & Vendored Contract Checks

1. **`reviews/workflow/latest.yaml` Synchronization**
   - Synchronized `reviews/workflow/latest.yaml` with `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/workspace/session-orchestration/20261019/mediaingredientmech/verified-evidence-index.json` by appending the newly verified Cycle 11 Stage 6 closure entry (PR `#997`, merge commit `bd337417ad5f04537f6f02dc81d37e229889900e`, `goal_evidence.sha256: 0361c0e3aadc22df08b8b52bf53900a9a798ee5f7a021ae55af292be41c0edbe`, `receipt_sha256: 0382bcf7acb35db57012d5eea622d08b9cab366b90b48143e50a1bc8487254e1`, 33 total verified entries).

2. **Vendored Claw Sync (`scripts/check_vendored_sync.py`)**
   - Command: `.venv/bin/python scripts/check_vendored_sync.py`
   - Result: `OK: 24 governed artifacts match the pinned claw revision` (exit code `0`).

3. **Workflow Contract Validator (`kg_microbe_workflows validate`)**
   - Command: `PYTHONPATH="/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/src" "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/python" -m kg_microbe_workflows validate --profile "/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/workflow/mech-workflow.yaml" --parent "/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/workflow/parent/mech-cycle.yaml" --schema "/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/workflow/parent/workflow.yaml"`
   - Result: `Workflow profile valid` (exit code `0`).

## 2. Frontier Discovery & Data Integrity Gates

1. **Repeated Frontier Search (`Pass 1` and `Pass 2`)**
   - `.venv/bin/python scripts/add_culturemech_gap_labels.py` -> `0 created, 0 minted, 0 synonym(s), 0 SSSOM row(s)` on both passes.
   - `.venv/bin/python scripts/create_records_from_groundings.py --groundings mappings/culturemech_residual_groundings.tsv` -> `123 proposals, 0 to create, 0 to promote, 123 skipped` on both passes.
   - `.venv/bin/python scripts/promote_microbedecoder_residual.py` -> `20 vetted rows, 0 to promote, 20 skipped` on both passes.

2. **Component Partonomy Gate (`scripts/validate_component_partonomy.py`)**
   - Command: `.venv/bin/python scripts/validate_component_partonomy.py`
   - Result: `component partonomy: 2953 records, 83 decompositions, 502 components, 0 violation(s)` (exit code `0`).

3. **SSSOM Invariant Gate (`scripts/validate_sssom_invariants.py`)**
   - Command: `.venv/bin/python scripts/validate_sssom_invariants.py --reject-tsv /tmp/needs_curator_review.tsv`
   - Result: `OK: ingredient_mappings.sssom.tsv passed Rules A, B1, B2, B3, B5, C, D, E, F, G, H, I, J, K, L. /tmp/needs_curator_review.tsv written with header only.` (exit code `0`).

4. **Instruction Reference & Unit Test Verification**
   - Command: `.venv/bin/python scripts/check_instruction_refs.py`
   - Result: `Scanned 52 agent-instruction file(s) against 88 recipes. OK: every referenced recipe, path, and Python CLI option exists.` (exit code `0`).
   - Command: `.venv/bin/python -m pytest --no-cov -p no:cacheprovider -q tests/test_check_instruction_refs.py`
   - Result: `16 passed` (exit code `0`).
