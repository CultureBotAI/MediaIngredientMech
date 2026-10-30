# Cycle 9 Stage 1 (`add_records`) Validation Report

- **Repository**: `CultureBotAI/MediaIngredientMech`
- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage / Revision**: `9` / `1` (`add_records`) / `1`
- **Source Revision**: `93cc14eb53d5d1698477db43b8a18e0dfac7c771`

## 1. Validation Commands & Results

1. **Workflow Profile Validation**:
   - Command:
     ```bash
     PYTHONPATH="/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/src" \
       "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/python" \
       -m kg_microbe_workflows validate \
       --profile "/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/workflow/mech-workflow.yaml" \
       --parent "/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/workflow/parent/mech-cycle.yaml" \
       --schema "/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/workflow/parent/workflow.yaml"
     ```
   - Result: `Workflow profile valid` (exit code `0`).

2. **Instruction Reference & Vendored Sync Checks**:
   - Command:
     ```bash
     .venv/bin/python scripts/check_instruction_refs.py && .venv/bin/python scripts/check_vendored_sync.py
     ```
   - Result:
     - `Scanned 52 agent-instruction file(s) against 88 recipes. OK: every referenced recipe, path, and Python CLI option exists.`
     - `OK: 24 governed artifacts match the pinned claw revision`
   - Unit test suite:
     ```bash
     .venv/bin/python -m pytest --no-cov -p no:cacheprovider -q tests/test_check_instruction_refs.py
     ```
     - Result: `16 passed in 1.66s` (exit code `0`).

3. **Repeated Frontier Search Verification (Pass 1 & Pass 2)**:
   - Command:
     ```bash
     .venv/bin/python scripts/add_culturemech_gap_labels.py && \
     .venv/bin/python scripts/create_records_from_groundings.py --groundings mappings/culturemech_residual_groundings.tsv && \
     .venv/bin/python scripts/promote_microbedecoder_residual.py
     ```
   - Result (both Pass 1 and Pass 2):
     - `add_culturemech_gap_labels.py`: `0 created, 0 minted, 0 synonym(s), 0 SSSOM row(s)`
     - `create_records_from_groundings.py`: `NEW_RECORD proposals: 123`, `records to create: 0`, `promote instead: 0`, `skipped: 123`
     - `promote_microbedecoder_residual.py`: `vetted rows: 20   to promote: 0   skipped: 20`

4. **Component Partonomy & SSSOM Invariant Validation**:
   - Commands:
     ```bash
     .venv/bin/python scripts/validate_component_partonomy.py
     .venv/bin/python scripts/validate_sssom_invariants.py --reject-tsv /tmp/needs_curator_review.tsv
     ```
   - Results:
     - `component partonomy: 2953 records, 83 decompositions, 502 components, 0 violation(s)`
     - `OK: ingredient_mappings.sssom.tsv passed Rules A, B1, B2, B3, B5, C, D, E, F, G, H, I, J, K, L.`
