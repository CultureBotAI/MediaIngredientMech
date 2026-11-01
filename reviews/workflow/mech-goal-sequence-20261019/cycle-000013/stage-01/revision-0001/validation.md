# Cycle 13 — Stage 1 (`add_records`) Validation Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Repository**: `CultureBotAI/MediaIngredientMech` (`mediaingredientmech`)
- **Cycle / Stage / Revision**: `cycle-000013` / `stage-01` (`add_records`) / `revision-0001`
- **Workflow SHA-256**: `059b5b9401ffeb04483cf7a46570f7f2f3c8c7fe6e574d80954bf71233cc609a`
- **Baseline `main` Commit**: `11676462b4ca583b42c08bbc9042e3b407ab60da`

---

## 1. Workflow & Governance Validation

### 1.1 Vendored Workflow Sync (`scripts/check_vendored_sync.py`)

```text
$ .venv/bin/python scripts/check_vendored_sync.py
OK: 26 governed artifacts match the pinned claw revision
```
- **Exit code**: `0`

### 1.2 Workflow Profile Validation (`kg_microbe_workflows validate`)

```text
$ PYTHONPATH="/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/src" "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/python" -m kg_microbe_workflows validate --profile "/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/workflow/mech-workflow.yaml" --parent "/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/workflow/parent/mech-cycle.yaml" --schema "/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/workflow/parent/workflow.yaml"
topClass is deprecated - use top_class
topClass is deprecated - use top_class
Workflow profile valid
```
- **Exit code**: `0`

### 1.3 Instruction References & Unit Tests (`scripts/check_instruction_refs.py` + `pytest`)

```text
$ .venv/bin/python scripts/check_instruction_refs.py
Scanned 52 agent-instruction file(s) against 88 recipes.
  (19 `../` reference(s) point outside the repo and were not verified.)
OK: every referenced recipe, path, and Python CLI option exists.

$ .venv/bin/python -m pytest --no-cov -p no:cacheprovider -q tests/test_check_instruction_refs.py
................                                                         [100%]
16 passed in 1.40s
```
- **Exit code**: `0`

---

## 2. Corpus & Mapping Invariant Gates

### 2.1 Component Partonomy Validation (`scripts/validate_component_partonomy.py`)

```text
$ .venv/bin/python scripts/validate_component_partonomy.py
component partonomy: 2953 records, 83 decompositions, 502 components, 0 violation(s)
```
- **Exit code**: `0`

### 2.2 SSSOM Invariants Validation (`scripts/validate_sssom_invariants.py`)

```text
$ .venv/bin/python scripts/validate_sssom_invariants.py --reject-tsv /tmp/needs_curator_review.tsv
WARNING: Rule B4 skipped — kg-microbe ontology transforms not found at /Users/marcin/Documents/VIMSS/ontology/Mechs/kg-microbe/data/transformed/ontologies for prefix(es): BTO, CHEBI, ENVO, FOODON, MICRO, UBERON. To enable Rule B4 locally, check out kg-microbe at the sibling path and run its `just transform` recipe. (CI typically lacks these transforms; the validator does not exit-2 on B4 alone in that case.)
OK: ingredient_mappings.sssom.tsv passed Rules A, B1, B2, B3, B5, C, D, E, F, G, H, I, J, K, L. /tmp/needs_curator_review.tsv written with header only.
```
- **Exit code**: `0`

---

## 3. Repeated Frontier Discovery Passes (`Pass 1` and `Pass 2`)

Both consecutive passes (`Pass 1` and `Pass 2`) of the three frontier discovery pipelines exited `0` and confirmed zero admissible new records remain in the bounded frontier:

| Pipeline Command | Pass 1 Exit / Summary | Pass 2 Exit / Summary |
|---|---|---|
| `.venv/bin/python scripts/add_culturemech_gap_labels.py` | Exit `0` — `0 created, 0 minted, 0 synonym(s), 0 SSSOM row(s)` (17 skipped) | Exit `0` — `0 created, 0 minted, 0 synonym(s), 0 SSSOM row(s)` (17 skipped) |
| `.venv/bin/python scripts/create_records_from_groundings.py --groundings mappings/culturemech_residual_groundings.tsv` | Exit `0` — `NEW_RECORD proposals: 123, records to create: 0, promote instead: 0, skipped: 123` | Exit `0` — `NEW_RECORD proposals: 123, records to create: 0, promote instead: 0, skipped: 123` |
| `.venv/bin/python scripts/promote_microbedecoder_residual.py` | Exit `0` — `vetted rows: 20, to promote: 0, skipped: 20` | Exit `0` — `vetted rows: 20, to promote: 0, skipped: 20` |

---

## 4. Summary

All Cycle 13 Stage 1 (`add_records`) validation gates passed (`exit_code: 0`).
