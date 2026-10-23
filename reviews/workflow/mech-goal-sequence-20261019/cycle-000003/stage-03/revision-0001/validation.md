---
artifact_kind: stage_03_protein_examples_validation_report
run_id: mech-goal-sequence-20261019
cycle: 3
stage: 3
stage_name: protein_examples
revision: 1
repository: CultureBotAI/MediaIngredientMech
base_commit: 521d90a13583f097382fe5084200be5f8f123684
workflow_sha256: 059b5b9401ffeb04483cf7a46570f7f2f3c8c7fe6e574d80954bf71233cc609a
generated_at: "2026-10-23T10:25:00Z"
validation_status: passed
records_scanned: 2953
records_modified: 0
---

# Cycle 3, Stage 3 (`protein_examples`) — Validation & Closed-Schema Verification Report

## 1. Executed Repository Validation & Test Suites

All repository validation gates and test suites required by `.claude/skills/add-uniprot-protein-examples/SKILL.md`, `.claude/skills/curate-causal-graphs/SKILL.md`, and `CLAUDE.md` were executed on branch `chore/cycle-03-stage-03-protein-examples` against `main` commit `521d90a13583f097382fe5084200be5f8f123684`:

| # | Check / Gate | Command Executed | Exit Code | Verified Output / Result |
|---:|---|---|---:|---|
| 1 | Closed-schema rules & fleet parity (`CausalGraph`, `CausalNode`, `CausalEdge`, `EvidenceItem`, `ProteinExample`) + readiness scorer + skill frontmatter + record review routes | `.venv/bin/python -m pytest -o pythonpath=src --no-cov tests/test_causal_graph_schema.py tests/test_score_causal_graph_readiness.py tests/test_skill_frontmatter.py tests/test_record_review_routes.py -v` | `0` | `178 passed in 3.21s` (`39` tests in `test_causal_graph_schema.py`, including 21 closed-schema rule cases `P1`–`P5`, `N1`–`N16` and 18 fleet shape parity tests across `CellStructureMech` and `TraitMech` for `ProteinExample` and graph classes) |
| 2 | Strict closed JSON Schema validation across all `2,953` YAML records | `.venv/bin/python scripts/validate_strict.py data/ingredients --out /tmp/strict_report_c3_s3.tsv` | `0` | `files scanned: 2953`, `files with ERROR: 0`, `total ERROR rows: 0` |
| 3 | Causal-graph readiness scorer across all `2,611` active `MAPPED` records | `.venv/bin/python scripts/score_causal_graph_readiness.py --ingredients-dir data/ingredients --duplicate-baseline mappings/duplicate_identifier_baseline.tsv --out /tmp/cg_readiness_all_c3_s3.tsv` | `0` | `wrote 2611 ranked records to /tmp/cg_readiness_all_c3_s3.tsv` (`2,496` `IDENTITY_GATE`-eligible + `115` `IDENTITY_GATE`-ineligible active `MAPPED` records) |
| 4 | Agent instruction, path, & skill recipe reference check | `.venv/bin/python scripts/check_instruction_refs.py` | `0` | `OK: every referenced recipe, path, and Python CLI option exists.` |
| 5 | Vendored `culturebotai-claw` governance sync check | `.venv/bin/python scripts/check_vendored_sync.py` | `0` | `OK: 24 governed artifacts match the pinned claw revision` |
| 6 | Canonical SSSOM invariants gate (Rules A, B1–B3, B5, C–L) | `.venv/bin/python scripts/validate_sssom_invariants.py --reject-tsv /tmp/needs_curator_review_c3_s3.tsv` | `0` | `OK: ingredient_mappings.sssom.tsv passed Rules A, B1, B2, B3, B5, C, D, E, F, G, H, I, J, K, L.` |
| 7 | Component partonomy gate (`StockComponent` & `ComponentAssertion`) | `.venv/bin/python scripts/validate_component_partonomy.py` | `0` | `component partonomy: 2953 records, 83 decompositions, 502 components, 0 violation(s)` |

---

## 2. In-Memory Closed-Schema Verification of `ProteinExample` on `CausalNode.protein_examples`

Using `validate_ingredient` from `src/mediaingredientmech/validation/write_validated.py` (`target_class="IngredientRecord"`, `schema_path="src/mediaingredientmech/schema/mediaingredientmech.yaml"`), an in-memory copy of `data/ingredients/mapped/Na2moo4_X_2_H2o.yaml` (`CHEBI:75213`, the planned Step 5 canary record) was populated with a `CausalGraph` (`graph_id: molybdate_abc_assimilation`, `graph_kind: ASSIMILATION`, `scope_status: REVIEW_NEEDED`, `explains: ["nutritional_roles#TRACE_ELEMENT"]`, `organism_scope: "NCBITaxon:83333"`) containing `MOLECULAR_FUNCTION` node `moda_molybdate_abc` (`grounding: "GO:0015412"`, `xrefs: ["EC:7.3.2.5"]`) and `ProteinExample` `UniProtKB:P09833` (`ModA`, `NCBITaxon:83333`, `entry_status: REVIEWED`, `proteome_id: UP000000625`, `retrieved_on: "2026-10-23"`):

| Case ID | Test Case Description | Mutation Applied to In-Memory `Na2moo4_X_2_H2o.yaml` Payload | `validate_ingredient` Error Count | Verified JSON Schema Diagnostic |
|---|---|---|---:|---|
| `PE-POS-1` | Valid `ProteinExample` (`UniProtKB:P09833` `ModA` on `MOLECULAR_FUNCTION` node `GO:0015412`) | None (canonical `ProteinExample` payload from `coverage_report.md` Row #1) | `0` | Valid (`0` errors) |
| `PE-NEG-1` | Isoform suffix on `ProteinExample.uniprot_id` | `uniprot_id = "UniProtKB:P09833-2"` | `1` | `'UniProtKB:P09833-2' does not match '^UniProtKB:(?:[OPQ][0-9][A-Z0-9]{3}[0-9]\|[A-NR-Z][0-9](?:[A-Z][A-Z0-9]{2}[0-9]){1,2})$' in /causal_graphs/0/nodes/3/protein_examples/0/uniprot_id` |
| `PE-NEG-2` | Unprefixed `ProteinExample.taxon_id` | `taxon_id = "83333"` | `1` | `'83333' does not match '^NCBITaxon:[0-9]+$' in /causal_graphs/0/nodes/3/protein_examples/0/taxon_id` |
| `PE-NEG-3` | Invalid `ProteinExample.entry_status` enum value | `entry_status = "SWISSPROT"` | `1` | `'SWISSPROT' is not one of ['REVIEWED', 'UNREVIEWED'] in /causal_graphs/0/nodes/3/protein_examples/0/entry_status` |
| `PE-NEG-4` | Missing required `ProteinExample.retrieved_on` | `pop("retrieved_on")` | `1` | `'retrieved_on' is a required property in /causal_graphs/0/nodes/3/protein_examples/0` |
| `PE-NEG-5` | Empty `ProteinExample.evidence` list (`minimum_cardinality: 1`) | `evidence = []` | `1` | `[] should be non-empty in /causal_graphs/0/nodes/3/protein_examples/0/evidence` |
| `N5` (suite) | `UniProtKB:` CURIE placed in `CausalNode.grounding` (genome firewall violation) | `nodes[1].grounding = "UniProtKB:P20166"` (`tests/test_causal_graph_schema.py::test_closed_schema_rule_case[N5]`) | `1` | `'UniProtKB:P20166' does not match '^(?!(?:UniProtKB\|NCBITaxon\|...):)...' in /causal_graphs/0/nodes/1/grounding` |
| `N10` (suite) | `NCBITaxon:` CURIE placed in `CausalNode.grounding` (genome firewall violation) | `nodes[1].grounding = "NCBITaxon:83333"` (`tests/test_causal_graph_schema.py::test_closed_schema_rule_case[N10]`) | `1` | `'NCBITaxon:83333' does not match '^(?!(?:UniProtKB\|NCBITaxon\|...):)...' in /causal_graphs/0/nodes/1/grounding` |

---

## 3. Data Integrity & Non-Mutation Verification

- `git diff --name-only data/ mappings/ src/ scripts/ tests/ conf/ docs/` confirms **`0` modifications** to ingredient YAML records (`data/ingredients/mapped/*.yaml`, `data/ingredients/unmapped/*.yaml`), SSSOM mappings (`mappings/ingredient_mappings.sssom.tsv`), schema files, or scripts.
- All `16` candidate record SHA-256 digests in `coverage_report.md` match ground truth on `main` (`16/16` exact matches).
- Composite SHA-256 across all `2,953` ingredient YAML files remains `4a44101e2fb6199658c0fcced12a4cbd2f6624b60afd520a197e3049ccf502c7`.
- `INFRA_TASKS.md` (`sha256: dda5707f52661e91f46d96fcbabfc256ac39d4cc865a28a3e5ab6f0536958a5e`) remains unchanged (`tasks: []`).
