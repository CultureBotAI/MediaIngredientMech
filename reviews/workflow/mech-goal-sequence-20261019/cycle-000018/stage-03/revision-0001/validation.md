---
artifact_kind: stage_03_protein_examples_validation_report
run_id: mech-goal-sequence-20261019
cycle: 18
stage: 3
stage_name: protein_examples
revision: 1
repository: CultureBotAI/MediaIngredientMech
base_commit: 4957ebb34e81f6e2762f73984042b4de8b1d39e6
workflow_sha256: 7c320cc21b5f9d88f99208f0344a4bb533fdc96f17020fd091690a780e75b2b6
generated_at: "2026-11-10T14:06:00Z"
skills_applied:
  - .claude/skills/mediaingredientmech-evolve-workflow/SKILL.md
  - .claude/skills/add-uniprot-protein-examples/SKILL.md
  - .claude/skills/curate-causal-graphs/SKILL.md
  - .claude/skills/curate-yaml-record/SKILL.md
validation_status: passed
records_modified: 0
---

# Cycle 18, Stage 3 (`protein_examples`) — Validation & Gate Verification Report

## 1. Workflow Profile, Latest Index & Instruction Reference Verification

1. **Workflow Profile Validation (`kg_microbe_workflows validate`):**
   - Command:
     ```bash
     PYTHONPATH="/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/src" \
       /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/python -m kg_microbe_workflows validate \
       --profile workflow/mech-workflow.yaml \
       --parent workflow/parent/mech-cycle.yaml \
       --schema workflow/parent/workflow.yaml
     ```
   - Exit status: `0` (`Workflow profile valid`).

2. **Tracked Review Latest Index Preflight (`reviews/workflow/latest.yaml`):**
   - Verified `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/workspace/session-orchestration/20261019/mediaingredientmech/verified-evidence-index.json` (`51` entries, `authority: verified_closure`) against `reviews/workflow/latest.yaml` (`sha256: f1c00115aaf4e97addcb11d10c8393cca63d7f0b6b37178959e3a49ba7684382`).
   - Result: Synchronized (`51/51` entries match through Cycle 17 Stage 6 PR #1329; Cycle 18 Stage 1 PR #1341 and Stage 2 PR #1345 have `required_outputs: []`).

3. **Instruction & Vendored Governance Synchronization:**
   - Commands:
     ```bash
     .venv/bin/python scripts/check_instruction_refs.py
     .venv/bin/python scripts/check_vendored_sync.py
     ```
   - Exit status: `0`
     - `Scanned 54 agent-instruction file(s) against 88 recipes. OK: every referenced recipe, path, and Python CLI option exists.`
     - `OK: 26 governed artifacts match the pinned claw revision`

---

## 2. Schema, Unit Test, and `ProteinExample` Closed-Schema Verification

1. **Targeted Unit Test Suite (`pytest`):**
   - Command:
     ```bash
     .venv/bin/python -m pytest --no-cov -p no:cacheprovider -q \
       tests/test_causal_graph_schema.py \
       tests/test_score_causal_graph_readiness.py \
       tests/test_skill_frontmatter.py \
       tests/test_record_review_routes.py
     ```
   - Exit status: `0` (`178 passed in 3.07s`).
   - Includes `39/39` tests in `tests/test_causal_graph_schema.py` (closed-schema rule cases `P1–P5`, `N1–N16` including `N5` `UniProtKB:` rejected in `CausalNode.grounding`, `N9` `NCBITaxon:` required on `protein_examples.taxon_id`, `N10` `NCBITaxon:` rejected in `CausalNode.grounding`, `N16` `minimum_cardinality: 1` on `evidence`, and fleet shape parity for `ProteinExample` across `CellStructureMech` and `TraitMech`).

2. **In-Memory `validate_ingredient` `ProteinExample` Positive & Negative Rule Check:**
   - Executed `validate_ingredient(..., target_class="IngredientRecord", schema_path=SCHEMA_PATH)` on an in-memory copy of `data/ingredients/mapped/D-glucose.yaml` with `ProteinExample` `UniProtKB:P69786` (`PtsG`, `NCBITaxon:83333`, `REVIEWED`, `UP000000625`, `retrieved_on: "2026-11-10"`, `PMID:10852890`) attached to `MOLECULAR_FUNCTION` node `EC:2.7.1.199`:
     - Positive case: **`0` errors** (`pos_errors: 0`).
     - Negative case 1 (`uniprot_id: "UniProtKB:P69786-2"` isoform suffix): **`1` error** (`isoform_suffix: 1`).
     - Negative case 2 (`taxon_id: "83333"` missing `NCBITaxon:` prefix): **`1` error** (`bad_taxon_id: 1`).
     - Negative case 3 (`entry_status: "SWISSPROT"` invalid enum): **`1` error** (`bad_entry_status: 1`).
     - Negative case 4 (`retrieved_on: "11/10/2026"` non-ISO date): **`1` error** (`bad_retrieved_on: 1`).
     - Negative case 5 (`evidence: []` empty evidence list): **`1` error** (`empty_evidence: 1`).
     - Negative case 6 (`CausalNode.grounding: "UniProtKB:P69786"`): **`1` error** (`uniprot_in_node_grounding: 1`).

---

## 3. Corpus-Wide Strict Validation and Invariant Gates

1. **Closed-Schema Strict Corpus Validation (`scripts/validate_strict.py`):**
   - Command:
     ```bash
     .venv/bin/python scripts/validate_strict.py data/ingredients data/curated data/collections --out /dev/null
     ```
   - Exit status: `0` (`files scanned: 2963`, `files with ERROR: 0`, `total ERROR rows: 0`).

2. **Component Partonomy Gate (`scripts/validate_component_partonomy.py`):**
   - Command:
     ```bash
     .venv/bin/python scripts/validate_component_partonomy.py
     ```
   - Exit status: `0` (`component partonomy: 2956 records, 83 decompositions, 502 components, 0 violation(s)`).

3. **SSSOM Invariants Gate (`scripts/validate_sssom_invariants.py`):**
   - Command:
     ```bash
     .venv/bin/python scripts/validate_sssom_invariants.py --reject-tsv /dev/null
     ```
   - Exit status: `0` (`OK: ingredient_mappings.sssom.tsv passed Rules A, B1, B2, B3, B5, C, D, E, F, G, H, I, J, K, L.`).

4. **Duplicate Identifier Baseline Gate (`scripts/audit_duplicate_identifiers.py --check`):**
   - Command:
     ```bash
     .venv/bin/python scripts/audit_duplicate_identifiers.py --check
     ```
   - Exit status: `0` (`15 identifier(s) held by more than one record (35 records, 20 excess); OK: duplicate identifiers match the tracked baseline exactly.`).
