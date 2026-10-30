# Cycle 9 Stage 1 (`add_records`) Coverage Report

- **Repository**: `CultureBotAI/MediaIngredientMech`
- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage / Revision**: `9` / `1` (`add_records`) / `1`
- **Source Revision**: `93cc14eb53d5d1698477db43b8a18e0dfac7c771` (`main` after Cycle 8 Stage 6 merge `PR #979`)

## 1. Preflight & Workflow Index Synchronization

1. **Workflow Profile & Parent Validation**:
   - Validated `workflow/mech-workflow.yaml` against `workflow/parent/mech-cycle.yaml` and `workflow/parent/workflow.yaml` via `kg_microbe_workflows validate` (`Workflow profile valid`).
   - Verified `scripts/check_instruction_refs.py` (`Scanned 52 agent-instruction file(s) against 88 recipes. OK: every referenced recipe, path, and Python CLI option exists.`) and `scripts/check_vendored_sync.py` (`OK: 24 governed artifacts match the pinned claw revision`).
2. **Tracked `reviews/workflow/latest.yaml` Synchronization**:
   - Synchronized `reviews/workflow/latest.yaml` from `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/workspace/session-orchestration/20261019/mediaingredientmech/verified-evidence-index.json` by adding verified entry 24 for Cycle 8 Stage 6 (`PR #979`, merge commit `93cc14eb53d5d1698477db43b8a18e0dfac7c771`, `evidence.yaml` SHA-256 `a22ab6f3b40973b04eb8c0594b628cca4d134d0cc7e95215c7588baba30df7f8`, receipt SHA-256 `a5e00f849937b0ee06e11d3d56474843790f7b870797cb40a6c855941b9d4660`, `verified_at: 2026-10-30T16:15:40.952086+00:00`).

## 2. Repeated Recorded Search of the Bounded Candidate Frontier

Two independent passes (`Pass 1` and `Pass 2`) were executed across all maintained candidate-ingestion and formulation-decomposition surfaces in `MediaIngredientMech` using the `.claude/skills/add-media/SKILL.md`, `.claude/skills/manage-identifiers/SKILL.md`, and `.claude/skills/curate-yaml-record/SKILL.md` rules:

| Frontier Surface | Command / Source Inspected | Pass 1 Result | Pass 2 Result | Admissible New Records |
| --- | --- | --- | --- | --- |
| CultureMech high-occurrence gap labels | `.venv/bin/python scripts/add_culturemech_gap_labels.py` | `0 created, 0 minted, 0 synonym(s), 0 SSSOM row(s)` (all 17 target gap labels skipped as already mapped or present as synonyms) | `0 created, 0 minted, 0 synonym(s), 0 SSSOM row(s)` (identical) | `0` |
| CultureMech residual groundings (`NEW_RECORD` proposals) | `.venv/bin/python scripts/create_records_from_groundings.py --groundings mappings/culturemech_residual_groundings.tsv` | `NEW_RECORD proposals: 123; records to create: 0; promote instead: 0; skipped: 123` (all 123 ontology/CURIE targets already held by existing mapped records) | `NEW_RECORD proposals: 123; records to create: 0; promote instead: 0; skipped: 123` (identical) | `0` |
| MicrobeDecoder vetted residual groundings | `.venv/bin/python scripts/promote_microbedecoder_residual.py` | `vetted rows: 20; to promote: 0; skipped: 20` (all 20 target CHEBI IDs already held by existing mapped records; PK collision guard prevents duplicate creation) | `vetted rows: 20; to promote: 0; skipped: 20` (identical) | `0` |
| CultureMech residual triage table | `mappings/culturemech_residual_triage.tsv` (`1,911` rows) | `RESIDUAL: 1,208`, `ALIAS: 414`, `UNMAPPED: 209`, `AMBIGUOUS: 57`, `NOISE:bare_number: 13`, `NOISE:truncated_quote: 10`; `0` uningested `NEW_RECORD` candidates | Identical (`1,911` rows; `0` new record candidates) | `0` |
| MicrobeDecoder & Edison research residual tables | `mappings/microbedecoder_residual_research_proposed.tsv` (`22` rows), `mappings/microbedecoder_residual_research_decomposition.tsv` (`42` rows), `mappings/edison_residual_merges.tsv` (`5` rows) | All admissible promotions/merges already applied; remaining entries are `DECOMPOSE`, `KEEP_UNMAPPED`, or collision-guarded merge candidates | Identical (`22`, `42`, and `5` rows; `0` admissible new records) | `0` |
| Stock / medium `StockComponent` (`has-part`) partonomy | `.venv/bin/python scripts/validate_component_partonomy.py` | `2953 records, 83 decompositions, 502 components, 0 violation(s)` | `2953 records, 83 decompositions, 502 components, 0 violation(s)` | `0` |

## 3. Preserved Corpus Counts & Search Limits

- **Maintained YAML Corpus**:
  - `data/ingredients/mapped/*.yaml`: `2,680` individual files (`2,680` records in `data/curated/mapped_ingredients.yaml`)
  - `data/ingredients/unmapped/*.yaml`: `273` individual files (`273` records in `data/curated/unmapped_ingredients.yaml`)
  - **Total maintained ingredient records**: `2,953`
  - **SSSOM mapping rows** (`mappings/ingredient_mappings.sssom.tsv`): `2,987` rows (`0` invariant violations)
- **Preserved Unresolved Candidates & Search Limits**:
  - `273` unmapped records remain in `data/ingredients/unmapped/` (including catalog codes, incomplete or underspecified medium recipes, complex solutions awaiting vendor composition sheets, and ambiguous chemical names).
  - `1,208` `RESIDUAL` rows and `57` `AMBIGUOUS` rows in `mappings/culturemech_residual_triage.tsv` remain preserved without speculative minting or unverified ontology grounding.
  - Both recorded passes over the bounded candidate frontier returned `0` admissible new ingredient or formulation records.
