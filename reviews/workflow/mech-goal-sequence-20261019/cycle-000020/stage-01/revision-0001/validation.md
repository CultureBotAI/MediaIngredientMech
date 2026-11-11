# Cycle 20 — Stage 1 (`add_records`) Validation Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Repository**: `CultureBotAI/MediaIngredientMech` (`mediaingredientmech`)
- **Cycle / Stage / Revision**: `cycle-000020` / `stage-01` (`add_records`) / `revision-0001`
- **Workflow SHA-256**: `7c320cc21b5f9d88f99208f0344a4bb533fdc96f17020fd091690a780e75b2b6`
- **Baseline `main` Commit**: `563e1759e1a75e2a1aca8da5f7d26d11fd5aba79`

---

## 1. Workflow & Governance Validation

### 1.1 Workflow Profile Validation (`kg_microbe_workflows validate`)

```text
$ /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/python -m kg_microbe_workflows validate --profile workflow/mech-workflow.yaml --parent workflow/parent/mech-cycle.yaml --schema workflow/parent/workflow.yaml
topClass is deprecated - use top_class
topClass is deprecated - use top_class
Workflow profile valid
```
- **Exit code**: `0`

### 1.2 Vendored Workflow Sync (`scripts/check_vendored_sync.py`)

```text
$ .venv/bin/python scripts/check_vendored_sync.py
OK: 26 governed artifacts match the pinned claw revision
```
- **Exit code**: `0`

### 1.3 Instruction References & Unit Tests (`scripts/check_instruction_refs.py` + `pytest`)

```text
$ .venv/bin/python scripts/check_instruction_refs.py
Scanned 54 agent-instruction file(s) against 88 recipes.
  (19 `../` reference(s) point outside the repo and were not verified.)
OK: every referenced recipe, path, and Python CLI option exists.

$ .venv/bin/python -m pytest --no-cov -p no:cacheprovider -q tests/test_check_instruction_refs.py
................                                                         [100%]
16 passed in 1.26s
```
- **Exit code**: `0`

### 1.4 Tracked Review Index Verification (`reviews/workflow/latest.yaml`)

- Synchronized `reviews/workflow/latest.yaml` (`sha256: 104a95e61c15121eab2c93f1bf84471949de53baaa8411f4e70eb64f62dccddc`) with all `57` `entries` from `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/workspace/session-orchestration/20261019/mediaingredientmech/verified-evidence-index.json` through Cycle 19 Stage 6 (`pr_number: 1363`, `head_sha: ce9b5b37b8962f8a878987d08df693c7e212cf3b`, `merge_commit_sha: 563e1759e1a75e2a1aca8da5f7d26d11fd5aba79`, `receipt_sha256: d85e359b2df4cffbd021afd0cfa0e556d928157019b704f815bfc863c7386c21`).

---

## 2. Corpus & Mapping Invariant Gates

### 2.1 Component Partonomy Validation (`scripts/validate_component_partonomy.py`)

```text
$ .venv/bin/python scripts/validate_component_partonomy.py
component partonomy: 2956 records, 83 decompositions, 502 components, 0 violation(s)
```
- **Exit code**: `0`

### 2.2 SSSOM Invariants Validation (`scripts/validate_sssom_invariants.py`)

```text
$ .venv/bin/python scripts/validate_sssom_invariants.py --reject-tsv .temp/needs_curator_review.tsv
WARNING: Rule B4 skipped — kg-microbe ontology transforms not found at /Users/marcin/Documents/VIMSS/ontology/Mechs/kg-microbe/data/transformed/ontologies for prefix(es): BTO, CHEBI, ENVO, FOODON, MICRO, UBERON. To enable Rule B4 locally, check out kg-microbe at the sibling path and run its `just transform` recipe. (CI typically lacks these transforms; the validator does not exit-2 on B4 alone in that case.)
OK: ingredient_mappings.sssom.tsv passed Rules A, B1, B2, B3, B5, C, D, E, F, G, H, I, J, K, L. .temp/needs_curator_review.tsv written with header only.
```
- **Exit code**: `0` (temporary scratch file `.temp/needs_curator_review.tsv` removed immediately after verification)

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

All Cycle 20 Stage 1 (`add_records`) validation gates passed (`exit_code: 0`).
