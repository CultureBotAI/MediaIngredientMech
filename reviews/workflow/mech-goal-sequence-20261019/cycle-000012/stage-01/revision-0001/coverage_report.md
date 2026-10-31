# Stage 1 Coverage & Frontier Exhaustion Report — Cycle 12

- **Run ID:** `mech-goal-sequence-20261019`
- **Cycle:** `12` (`cycle-000012`)
- **Stage:** `1` (`stage-01` — `add_records`)
- **Revision:** `1` (`revision-0001`)
- **Source Revision:** `bd337417ad5f04537f6f02dc81d37e229889900e` (`main`)

## 1. Corpus Baseline & Post-Search State

| Surface | Pre-Pass Count | Post-Pass Count | Net Delta |
| :--- | ---: | ---: | ---: |
| `data/ingredients/mapped/*.yaml` | 2,680 | 2,680 | 0 |
| `data/ingredients/unmapped/*.yaml` | 273 | 273 | 0 |
| Total ingredient records | 2,953 | 2,953 | 0 |
| `data/curated/mapped_ingredients.yaml` | 2,680 | 2,680 | 0 |
| `data/curated/unmapped_ingredients.yaml` | 273 | 273 | 0 |
| `mappings/ingredient_mappings.sssom.tsv` rows | 2,987 | 2,987 | 0 |
| `StockComponent` decompositions (`components:`) | 83 records (502 components) | 83 records (502 components) | 0 |

## 2. Repeated Recorded Frontier Search (`Pass 1` and `Pass 2`)

Following the repository-local discovery and record-addition skills (`.claude/skills/add-media/SKILL.md`, `.claude/skills/manage-identifiers/SKILL.md`, `.claude/skills/curate-yaml-record/SKILL.md`) and `MAPPING_SEMANTICS.md`, two independent consecutive passes were executed across all maintained candidate frontier inputs:

### Pass 1 & Pass 2 Results

1. **CultureMech High-Occurrence Gap Labels (`scripts/add_culturemech_gap_labels.py`)**
   - **Pass 1:** `DRY RUN (re-run with --apply) — 0 created, 0 minted, 0 synonym(s), 0 SSSOM row(s)`. All 17 tracked high-occurrence CultureMech gap candidates (`Neutral red`, `Pyridoxine dihydrochloride`, `DL-Tyrosine`, `Defibrinated sheep blood`, `Defibrinated horse blood`, `R2A agar`, `Marine agar 2216`, `Marine broth 2216`, `Peptic digest of soybean meal`, `Sodium sulfide`, `L-glutathione reduced`, `Acid hydrolysate of casein`, `RbCl`, `DL-threonine`, `Defibrinated rabbit blood`, `Natural seawater (filtered, 95% strength)`, `Whole eggs`) are already represented in `data/ingredients/mapped/` as primary labels or preserved synonyms.
   - **Pass 2:** Identical (`0 created, 0 minted, 0 synonym(s), 0 SSSOM row(s)`).

2. **CultureMech Residual Groundings (`scripts/create_records_from_groundings.py --groundings mappings/culturemech_residual_groundings.tsv`)**
   - **Pass 1:** `NEW_RECORD proposals: 123 | records to create: 0 | promote instead: 0 | skipped: 123`. Every proposed ontology or registry grounding in `mappings/culturemech_residual_groundings.tsv` is already held by an existing mapped YAML record.
   - **Pass 2:** Identical (`123 proposals, 0 to create, 0 to promote, 123 skipped`).

3. **MicrobeDecoder Residual Research Proposals (`scripts/promote_microbedecoder_residual.py`)**
   - **Pass 1:** `vetted rows: 20 | to promote: 0 | skipped: 20`. All 20 vetted `PROMOTE` rows in `mappings/microbedecoder_residual_research_proposed.tsv` collide with existing `MAPPED` records (`PK collision (already MAPPED) — merge, not promote`), which belong to deduplication/merge workflows rather than net-new record creation. The remaining 2 rows (`UNMAPPED_0663` `N-propanol`, `UNMAPPED_0714` `Polyvinyl alcohol`) are explicitly tagged `DEFER` (`CHEBI_NOT_FOUND` / polymer repeat-unit vs. substance ambiguity).
   - **Pass 2:** Identical (`vetted rows: 20 | to promote: 0 | skipped: 20`).

4. **MicrobeDecoder Residual Decompositions (`mappings/microbedecoder_residual_research_decomposition.tsv`)**
   - **Pass 1 & Pass 2:** 42 rows across 22 `UNMAPPED_*` mixtures (`UNMAPPED_0609` through `UNMAPPED_0880`). All 22 parent records already exist in `data/ingredients/unmapped/` and are deferred pending upstream recipe-proportion verification or component grounding; none are missing record stubs.

5. **CultureMech Residual Triage (`mappings/culturemech_residual_triage.tsv`)**
   - **Pass 1 & Pass 2:** 1,911 rows partitioned into `RESIDUAL` (`1,208`), `ALIAS` (`414`), `UNMAPPED` (`209`), `AMBIGUOUS` (`57`), `NOISE:bare_number` (`13`), and `NOISE:truncated_quote` (`10`). No uningested admissible `NEW_RECORD` candidates remain outside the 123 already-landed groundings.

## 3. Preserved Unresolved Candidates & Search Limits

- **Unmapped Corpus (`273` records in `data/ingredients/unmapped/`):** Preserved untouched (`UNMAPPED_0007` through `UNMAPPED_0901`). In accordance with `AGENTS.md` and `MAPPING_SEMANTICS.md`, unverified LLM proposals, ambiguous polymer/mixture names, and PK-colliding promotion candidates are not force-promoted or silently merged during Stage 1 (`add_records`).
- **Search Limits:** Discovery was bounded to repository-maintained intake tables (`mappings/culturemech_residual_groundings.tsv`, `mappings/culturemech_residual_triage.tsv`, `mappings/microbedecoder_residual_research_proposed.tsv`, `mappings/microbedecoder_residual_research_decomposition.tsv`, `mappings/edison_residual_merges.tsv`) and `scripts/add_culturemech_gap_labels.py`. Both recorded search passes converged at `0` admissible new records.
