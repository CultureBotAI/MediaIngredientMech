# Cycle 13 — Stage 1 (`add_records`) Coverage Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Repository**: `CultureBotAI/MediaIngredientMech` (`mediaingredientmech`)
- **Cycle / Stage / Revision**: `cycle-000013` / `stage-01` (`add_records`) / `revision-0001`
- **Workflow SHA-256**: `059b5b9401ffeb04483cf7a46570f7f2f3c8c7fe6e574d80954bf71233cc609a`
- **Baseline `main` Commit**: `11676462b4ca583b42c08bbc9042e3b407ab60da`
- **Execution Mode**: Exhaustive (`exhaustive: true`) — repeated recorded search of the bounded candidate frontier until a consecutive pass finds zero admissible new records.

---

## 1. Corpus Baseline & Tracked Evidence Index Sync

At the start of Cycle 13 Stage 1 on `main` (`11676462b4ca583b42c08bbc9042e3b407ab60da`), the maintained MediaIngredientMech corpus and mapping surfaces were verified via live inspection:

| Surface | Count | Notes |
|---|---:|---|
| `data/ingredients/mapped/*.yaml` | 2,680 | Synchronized with `data/curated/mapped_ingredients.yaml` |
| `data/ingredients/unmapped/*.yaml` | 273 | Synchronized with `data/curated/unmapped_ingredients.yaml` |
| **Total Ingredient Records** | **2,953** | 90.76% mapped (`2,680 / 2,953`) |
| `mappings/ingredient_mappings.sssom.tsv` data rows | 2,987 | Reflects retirement of 7 generated aliases in PR `#1007` (`2add44fbfe37544218d2f4daeb322b35debc5dd4`) |
| `StockComponent` decompositions (`validate_component_partonomy.py`) | 83 | 502 total `StockComponent` assertions across 2,953 records (`0` violations) |
| `reviews/workflow/latest.yaml` verified entries | 36 | Synchronized from `verified-evidence-index.json` through Cycle 12 Stage 6 (PR `#1024`) |

---

## 2. Bounded Candidate Frontier Inventory

The bounded candidate frontier for Stage 1 (`add_records`) spans five maintained discovery and residual-triage inputs:

1. **CultureMech Top-Gap Curated Labels (`scripts/add_culturemech_gap_labels.py`)**:
   - 17 curated high-frequency CultureMech gap candidates (`CREATE`, `MINT`, and `SYNONYM` buckets).
2. **CultureMech Residual Groundings (`mappings/culturemech_residual_groundings.tsv` via `scripts/create_records_from_groundings.py`)**:
   - 158 grounded CultureMech residual rows (`123 NEW_RECORD`, `18 SYNONYM_ONTO_EXISTING`, `17 MULTIPLE_EXACT`).
3. **MicrobeDecoder Vetted Residual Promotions (`scripts/promote_microbedecoder_residual.py`)**:
   - 20 vetted `UNMAPPED_NNNN` promotion candidates from MicrobeDecoder residual curation.
4. **MicrobeDecoder Residual Research Decomposition (`mappings/microbedecoder_residual_research_decomposition.tsv`)**:
   - 42 complex mixture / formulation / split rows (`38 split`, `3 map_to_medium`, `1 map_to_ingredient`).
5. **CultureMech Residual Triage (`mappings/culturemech_residual_triage.tsv`)**:
   - 1,911 total triaged strings across 6 buckets:
     - `RESIDUAL`: 1,208
     - `ALIAS`: 414
     - `UNMAPPED`: 209
     - `AMBIGUOUS`: 57
     - `NOISE:bare_number`: 13
     - `NOISE:truncated_quote`: 10

---

## 3. Repeated Recorded Frontier Search (`Pass 1` and `Pass 2`)

Two independent consecutive search passes (`Pass 1` and `Pass 2`) were executed across all executable candidate-addition pipelines on the bounded frontier.

### 3.1 `scripts/add_culturemech_gap_labels.py`

- **Command**: `.venv/bin/python scripts/add_culturemech_gap_labels.py`
- **Pass 1 Result**: `0 created, 0 minted, 0 synonym(s), 0 SSSOM row(s)` (`17 skipped`)
- **Pass 2 Result**: `0 created, 0 minted, 0 synonym(s), 0 SSSOM row(s)` (`17 skipped`)
- **Disposition of all 17 candidates**:
  - 8 candidates (`Neutral red`, `Pyridoxine dihydrochloride`, `DL-Tyrosine`, `Defibrinated sheep blood`, `Defibrinated horse blood`, `R2A agar`, `Marine agar 2216`, `Marine broth 2216`) already exist as mapped records carrying the target label.
  - 9 candidates (`Peptic digest of soybean meal`, `Sodium sulfide`, `L-glutathione reduced`, `Acid hydrolysate of casein`, `RbCl`, `DL-threonine`, `Defibrinated rabbit blood`, `Natural seawater (filtered, 95% strength)`, `Whole eggs`) are already recorded as synonyms on their respective canonical records (`Soy peptone`, `Na2S`, `Glutathione`, `Casein hydrolysate`, `rubidium chloride`, `Threonine`, `Rabbit blood`, `Filtered Seawater`, `Whole egg`).

### 3.2 `scripts/create_records_from_groundings.py --groundings mappings/culturemech_residual_groundings.tsv`

- **Command**: `.venv/bin/python scripts/create_records_from_groundings.py --groundings mappings/culturemech_residual_groundings.tsv`
- **Pass 1 Result**: `NEW_RECORD proposals: 123 | records to create: 0 | promote instead: 0 | skipped: 123`
- **Pass 2 Result**: `NEW_RECORD proposals: 123 | records to create: 0 | promote instead: 0 | skipped: 123`
- **Disposition**:
  - Every one of the 123 `NEW_RECORD` grounding proposals is already held by an existing mapped YAML record in `data/ingredients/mapped/` (e.g., `Horse blood` -> `MICRO:0001234` in `Horse_blood.yaml`, `[1,1′-Biphenyl]-2-ol` -> `CHEBI:17043` in `11-Biphenyl-2-ol.yaml`, `Sheep blood` -> `MICRO:0001230` in `Sheep_blood.yaml`, `Artificial seawater` -> `MICRO:0001715` in `Artificial_seawater.yaml`, `Air` -> `ENVO:00002005` in `Air.yaml`, `Oat flakes` -> `FOODON:03306272` in `Oat_flakes.yaml`, `Nickel Sulfate` -> `CHEBI:53001` in `Nickel_Sulfate.yaml`, `Olive oil` -> `FOODON:03301826` in `Olive_oil.yaml`, `Zinc Acetate` -> `CHEBI:62984` in `Zinc_Acetate.yaml`, `Clarified rumen fluid` -> `MICRO:0000520` in `Clarified_rumen_fluid.yaml`, `Ferrous ammonium sulfate` -> `CHEBI:76243` in `Ferrous_ammonium_sulfate.yaml`).
  - The remaining 35 rows in `mappings/culturemech_residual_groundings.tsv` are `18 SYNONYM_ONTO_EXISTING` (not new records) and `17 MULTIPLE_EXACT` (ambiguous multi-term hits excluded from automated record minting under `MAPPING_SEMANTICS.md`).

### 3.3 `scripts/promote_microbedecoder_residual.py`

- **Command**: `.venv/bin/python scripts/promote_microbedecoder_residual.py`
- **Pass 1 Result**: `vetted rows: 20 | to promote: 0 | skipped: 20`
- **Pass 2 Result**: `vetted rows: 20 | to promote: 0 | skipped: 20`
- **Disposition**:
  - All 20 rows (`UNMAPPED_0783`, `UNMAPPED_0782`, `UNMAPPED_0660`, `UNMAPPED_0669`, `UNMAPPED_0652`, `UNMAPPED_0681`, `UNMAPPED_0797`, `UNMAPPED_0653`, `UNMAPPED_0641`, `UNMAPPED_0644`, `UNMAPPED_0728`, `UNMAPPED_0624`, `UNMAPPED_0684`, `UNMAPPED_0818`, `UNMAPPED_0689`, `UNMAPPED_0633`, `UNMAPPED_0837`, `UNMAPPED_0658`, `UNMAPPED_0732`, `UNMAPPED_0686`) collide with primary keys already held by existing `MAPPED` records (`PK collision (already MAPPED) — merge, not promote`), so none is an admissible new record.

---

## 4. Preserved Unresolved Candidates & Search Limits

In accordance with the Stage 1 objective ("Preserve unresolved candidates and search limits") and `.claude/skills/add-media/SKILL.md`:

- **Complex mixtures / multi-component strings (`mappings/microbedecoder_residual_research_decomposition.tsv`)**:
  - All admissible commercial/named formulations from this frontier are already represented among the 83 `StockComponent` decompositions (`502` total components, `0` violations verified by `scripts/validate_component_partonomy.py`).
  - The remaining `38 split` entries are slash/plus/parenthetical co-listings of multiple distinct substances from MicrobeDecoder source tables; under `MAPPING_SEMANTICS.md` ("One ingredient record denotes one distinct substance"), multi-substance co-listings must not be minted as single composite `IngredientRecord` entries.
- **Unresolved CultureMech residual strings (`mappings/culturemech_residual_triage.tsv`)**:
  - `1,050` ungrounded `RESIDUAL` strings (`1,208` total `RESIDUAL` minus `158` grounded in `culturemech_residual_groundings.tsv`) lack verified ontology/registry identities or source recipe definitions sufficient to disambiguate substance identity without guessing.
  - `57 AMBIGUOUS` strings and `17 MULTIPLE_EXACT` groundings require source-recipe disambiguation before any record creation or mapping.
  - `23 NOISE` strings (`13 NOISE:bare_number`, `10 NOISE:truncated_quote`) are parsing artifacts excluded from ingredient minting.
  - `414 ALIAS` and `209 UNMAPPED` strings already correspond to existing mapped or unmapped records in the 2,953-record corpus.

---

## 5. Summary of Stage 1 Changes

- **New ingredient records added**: `0` (bounded frontier exhausted across two consecutive recorded passes).
- **Synchronized workflow index updated**: `reviews/workflow/latest.yaml` updated from `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/workspace/session-orchestration/20261019/mediaingredientmech/verified-evidence-index.json` to include the 36th verified entry (`cycle: 12`, `stage: 6`, PR `#1024`, merge commit `11676462b4ca583b42c08bbc9042e3b407ab60da`).
