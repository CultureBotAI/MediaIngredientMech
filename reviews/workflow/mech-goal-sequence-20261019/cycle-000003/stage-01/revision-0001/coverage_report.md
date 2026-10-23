# Cycle 3 Stage 1 (`add_records`) — Bounded Frontier Candidate Discovery & Coverage Report

- **Run ID:** `mech-goal-sequence-20261019`
- **Repository:** `CultureBotAI/MediaIngredientMech` (`mediaingredientmech`)
- **Cycle / Stage / Revision:** Cycle `3`, Stage `1` (`add_domain_objects`, canonical stage `add_records`), Revision `1`
- **Base Commit (`main`):** `40d1358b1077fb0a69d1b07b4315e10d1efe7184`
- **Skills Followed:**
  - `.claude/skills/mediaingredientmech-evolve-workflow/SKILL.md`
  - `.claude/skills/add-media/SKILL.md`
  - `.claude/skills/manage-identifiers/SKILL.md`
  - `.claude/skills/curate-yaml-record/SKILL.md`

---

## 1. Verified Closure Index Synchronization

Before executing Stage 1 candidate discovery, [`reviews/workflow/latest.yaml`](../../../../../latest.yaml) was synchronized from the supervisor's authoritative `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/workspace/session-orchestration/20261019/mediaingredientmech/verified-evidence-index.json` (`authority: verified_closure`) to record all six verified closures through Cycle 2 Stage 6:

1. **Cycle 1, Stage 4 (`review_records`):** PR #919 merged at `515a8cca2a1590a31b0fbf947b178fe8a6bbedc1` (`head_sha: d3210fe5f8f2efd80a371da59af1e80a36d3baff`).
2. **Cycle 1, Stage 5 (`remediate_findings`):** PR #924 merged at `2bf28deedd03aaaa9cf4a1e8939e775b4ad35e23` (`head_sha: e6f1d10ab2e1f804510b9729c956a70b31fdc326`).
3. **Cycle 1, Stage 6 (`implement_infra_tasks`):** PR #926 merged at `8e6531266e17f94d68c2477311be51c49765edee` (`head_sha: 8a505f750509dabf045f87ef6ae74c0c7f52d3a5`).
4. **Cycle 2, Stage 4 (`review_records`):** PR #930 merged at `7f56a13130d8d220efa48cef78559e80351c5a46` (`head_sha: 787f15f2fdf48abf470190b6a3a3c7ee3574a8a4`).
5. **Cycle 2, Stage 5 (`remediate_findings`):** PR #932 merged at `0968cc55bbf3754e3a9b84ef9308593e36937cee` (`head_sha: d1cda26b8c02af2f8f960d5f43b7626b86042766`).
6. **Cycle 2, Stage 6 (`implement_infra_tasks`):** PR #934 merged at `40d1358b1077fb0a69d1b07b4315e10d1efe7184` (`head_sha: ca04901fce6d3e4ffcae0dcbf1a71d9446949bab`).

---

## 2. Repeated, Recorded Search of the Bounded Candidate Frontier

Two full, independent passes (`Pass 1` and `Pass 2`) were executed across every bounded candidate source and native ingestion/promotion driver in the repository to identify any admissible new media ingredient records or supported formulations (`StockComponent` `has-part` decompositions).

### Summary of Candidate Frontier Sweeps (`Pass 1` and `Pass 2`)

| Frontier Source / Driver | Total Candidates | Already Present / Mapped | Admissible New Records Added | Unresolved / Held Candidates | Verification Outcome (Pass 1 & Pass 2) |
| :--- | ---: | ---: | ---: | ---: | :--- |
| `scripts/add_culturemech_gap_labels.py` (CultureMech gap labels) | 17 | 17 | 0 | 0 | `0 created, 0 minted, 0 synonym(s), 0 SSSOM row(s)`; all 17 labels/synonyms already present in `data/ingredients/mapped/` or `data/ingredients/unmapped/` |
| `mappings/culturemech_residual_groundings.tsv` via `scripts/create_records_from_groundings.py` | 158 | 141 (`123 NEW_RECORD` + `18 SYNONYM_ONTO_EXISTING`) | 0 | 17 (`MULTIPLE_EXACT`) | `NEW_RECORD proposals: 123; records to create: 0; promote instead: 0; skipped: 123`; all 141 single-term proposals (`123 NEW_RECORD` + `18 SYNONYM_ONTO_EXISTING`) already ingested in PR #886 |
| `mappings/culturemech_residual_triage.tsv` (`ALIAS` / `AMBIGUOUS` / `NOISE` / `RESIDUAL` / `UNMAPPED`) | 1,911 | 555 (`414 ALIAS` + `123 NEW_RECORD` + `18 SYNONYM_ONTO_EXISTING`) | 0 | 1,356 (`209 UNMAPPED` + `57 AMBIGUOUS` + `23 NOISE` + `17 MULTIPLE_EXACT` + `1,050 ungrounded RESIDUAL`) | No additional verified single-term groundings ready for deterministic creation |
| `mappings/microbedecoder_residual_grounded.tsv` via `scripts/promote_microbedecoder_residual.py` | 20 | 20 | 0 | 0 | `vetted rows: 20; to promote: 0; skipped: 20` (all 20 already promoted to `MAPPED` in `data/ingredients/mapped/`) |
| `mappings/microbedecoder_residual_research_proposed.tsv` | 22 | 22 | 0 | 0 | All 22 rows (`16 UNMAPPED_*` proposals + `6` accession-ceiling antibiotics: `Carbomycin`, `Colistin_Sulfate`, `Gentamicin`, `Lysostaphin`, `Netilmycin`, `Polymyxin_B`, including `keratin` -> `mesh:D007633` and `Mono- And Disaccharides` -> `kgmicrobe.ingredient:mono_and_disaccharides`) already promoted or merged into `data/ingredients/mapped/` |
| `mappings/microbedecoder_residual_research_decomposition.tsv` | 42 (42 distinct `UNMAPPED_*` records) | 42 | 0 | 0 | All 42 rows promoted to `kgmicrobe.ingredient:*` records in `data/ingredients/mapped/` and decomposed into `data/curated/complex_ingredient_decompositions.yaml` by `scripts/apply_curated_decompositions.py` (`b9f25f3`) |
| `mappings/edison_residual_merges.tsv` | 5 | 5 | 0 | 0 | All 5 Edison-verified synonyms (`3-hydroxy 2-butanone`, `D-lactate`, `Iso-butanol`, `N-acetyl-neuraminic Acid`, `Trimethyleneglycol`) already merged onto their target mapped records in `data/ingredients/mapped/` |
| Supported Formulations (`StockComponent` `has-part` assertions in `data/ingredients/mapped/`) | 83 formulations (502 component assertions) | 83 | 0 | 23 (`UNMAPPED` complex/stock placeholders) | All 83 mapped decompositions pass `just qc-component-partonomy` (`2953 records, 83 decompositions, 502 components, 0 violation(s)`); remaining 23 unmapped complex/stock records lack quantitative primary-source recipes in local inputs |

### Recorded Command Evidence

1. **Pass 1 & Pass 2 — CultureMech Gap Labels (`scripts/add_culturemech_gap_labels.py`):**
   ```text
   $ .venv/bin/python scripts/add_culturemech_gap_labels.py
   DRY RUN (re-run with --apply) — 0 created, 0 minted, 0 synonym(s), 0 SSSOM row(s)
     SKIPPED Neutral red: a record already carries this label
     SKIPPED Pyridoxine dihydrochloride: a record already carries this label
     SKIPPED DL-Tyrosine: a record already carries this label
     SKIPPED Defibrinated sheep blood: a record already carries this label
     SKIPPED Defibrinated horse blood: a record already carries this label
     SKIPPED R2A agar: a record already carries this label
     SKIPPED Marine agar 2216: already MAPPED
     SKIPPED Marine broth 2216: already MAPPED
     SKIPPED Peptic digest of soybean meal: already a synonym of 'Soy peptone'
     SKIPPED Sodium sulfide: already a synonym of 'Na2S'
     SKIPPED L-glutathione reduced: already a synonym of 'Glutathione'
     SKIPPED Acid hydrolysate of casein: already a synonym of 'Casein hydrolysate'
     SKIPPED RbCl: already a synonym of 'rubidium chloride'
     SKIPPED DL-threonine: already a synonym of 'Threonine'
     SKIPPED Defibrinated rabbit blood: already a synonym of 'Rabbit blood'
     SKIPPED Natural seawater (filtered, 95% strength): already a synonym of 'Filtered Seawater'
     SKIPPED Whole eggs: already a synonym of 'Whole egg'
   ```

2. **Pass 1 & Pass 2 — CultureMech Residual Groundings (`scripts/create_records_from_groundings.py`):**
   ```text
   $ .venv/bin/python scripts/create_records_from_groundings.py --groundings mappings/culturemech_residual_groundings.tsv
   NEW_RECORD proposals: 123
     records to create:    0
     promote instead:      0
     skipped:              123
   Dry run. Re-run with --apply to write.
   ```

3. **Pass 1 & Pass 2 — MicrobeDecoder Vetted Residual Groundings (`scripts/promote_microbedecoder_residual.py`):**
   ```text
   $ .venv/bin/python scripts/promote_microbedecoder_residual.py
   vetted rows: 20   to promote: 0   skipped: 20
   (dry-run — pass --apply to write collections + SSSOM)
   ```

4. **Pass 1 & Pass 2 — Edison Residual Merges (`mappings/edison_residual_merges.tsv`):**
   All 5 rows (`3-hydroxy 2-butanone` -> `CHEBI:15688`, `D-lactate` -> `CHEBI:16004`, `Iso-butanol` -> `CHEBI:46645`, `N-acetyl-neuraminic Acid` -> `CHEBI:17012`, `Trimethyleneglycol` -> `CHEBI:16109`) verified present on their target mapped records in `data/ingredients/mapped/`.

---

## 3. Current Corpus Totals Verified After Repeated Search

- **Mapped Collection (`data/curated/mapped_ingredients.yaml`):** `2,680` records (`2,611` `MAPPED`, `69` `REJECTED` tombstones)
- **Unmapped Collection (`data/curated/unmapped_ingredients.yaml`):** `273` records (`260` `UNMAPPED`, `1` `AMBIGUOUS` (`PYGS.yaml`), `12` `REJECTED` tombstones)
- **Individual Ingredient YAML Files:** `2,953` (`2,680` in `data/ingredients/mapped/`, `273` in `data/ingredients/unmapped/`)
- **Supported Formulations (`has-part` decompositions):** `83` mapped records carrying `502` `StockComponent` assertions with `ComponentAssertion` provenance (`component partonomy: 2953 records, 83 decompositions, 502 components, 0 violation(s)`)
- **Published SSSOM Mapping Rows (`mappings/ingredient_mappings.sssom.tsv`):** `2,987` rows (`0 GAP, 0 ORPHAN, 0 STALE`)

---

## 4. Preserved Unresolved Candidates & Search Limits

### A. Preserved Unresolved Candidates

1. **`MULTIPLE_EXACT` Multi-Hit Ontology Ambiguities (`mappings/culturemech_residual_groundings.tsv`, 17 candidates):**
   1. `Potato` (occ `11`, `FOODON:03301449|FOODON:03315354`, `potato (whole, raw)|white potato food product`, `2 ontology hits`)
   2. `Sodium borate` (occ `4`, `CHEBI:131366|CHEBI:75227`, `disodium tetraborate|sodium borate`, `2 ontology hits`)
   3. `Fe-citrate` (occ `3`, `MICRO:0000735|MICRO:0001190`, `iron citrate|ferric citrate`, `2 ontology hits`)
   4. `5-Hydroxyectoine` (occ `2`, `CHEBI:49432|CHEBI:85413`, `(4S,5S)-5-hydroxyectoine|5-hydroxyectoine`, `2 ontology hits`)
   5. `Propenoate` (occ `2`, `CHEBI:18308|CHEBI:37080`, `acrylic acid|acrylate`, `2 ontology hits`)
   6. `Zinc` (occ `2`, `CHEBI:27363|CHEBI:30185`, `zinc(0)|zinc atom`, `2 ontology hits`)
   7. `dTMP` (occ `2`, `CHEBI:17013|CHEBI:63528`, `thymidine 5'-monophosphate|thymidine 5'-monophosphate(2-)`, `2 ontology hits`)
   8. `CM-Cellulose` (occ `1`, `MICRO:0002714|MICRO:0002778`, `O-carboxymethylcellulose|carboxymethylcellulose`, `2 ontology hits`)
   9. `Culture supernatant (see below)` (occ `1`, `BTO:0002217|BTO:0002233`, `conditioned medium|cell-free system`, `2 ontology hits`)
   10. `D-Ribose 5-phosphate` (occ `1`, `CHEBI:17797|CHEBI:52742`, `alpha-D-ribose 5-phosphate|D-ribose 5-phosphate`, `2 ontology hits`)
   11. `Fe-Citrate` (occ `1`, `MICRO:0000735|MICRO:0001190`, `iron citrate|ferric citrate`, `2 ontology hits`)
   12. `GDP` (occ `1`, `CHEBI:17552|CHEBI:58189`, `GDP|GDP(3-)`, `2 ontology hits`)
   13. `Retinol` (occ `1`, `CHEBI:17336|CHEBI:50211`, `all-trans-retinol|retinol`, `2 ontology hits`)
   14. `Sterile` (occ `1`, `NCIT:C27010|NCIT:C63385`, `Infertility|Sterile`, `2 ontology hits`)
   15. `Titanium citrate` (occ `1`, `MICRO:0000735|MICRO:0001190`, `iron citrate|ferric citrate`, `2 ontology hits`)
   16. `lactic acid` (occ `1`, `MICRO:0000963|MICRO:0002945`, `(S)-lactate|(R)-lactate`, `2 ontology hits`)
   17. `mannan (Saccharomyces cerevisiae)` (occ `1`, `CHEBI:149779|CHEBI:28808`, `alpha-D-mannan|mannan`, `2 ontology hits`)
   - *Disposition:* Preserved in `mappings/culturemech_residual_groundings.tsv`; resolving these requires source-recipe disambiguation of oxidation state, charge state, stereochemistry, or food-product preparation per `docs/MAPPING_SEMANTICS.md`.

2. **Remaining Unmapped / Ambiguous Placeholder Cohort (`data/ingredients/unmapped/*.yaml`, 261 active unmapped/ambiguous records alongside 12 `REJECTED` tombstones; 273 total files):**
   - Consists of `260` `UNMAPPED` records and `1` `AMBIGUOUS` record (`PYGS.yaml`), including `23` complex media / stock solution placeholders (`Brain Heart Infusion`, `Solution A`–`G`, `Trace elements`, `Vitamin solution`, etc.) and `238` chemical/biological placeholders (catalog strings, abbreviated salts, trade names, and recipe-specific tokens).
   - *Disposition:* Tracked in `https://github.com/CultureBotAI/MediaIngredientMech/issues/718` (`mim-c01-s04-f006`, `mim-c01-s05-g004`); excluded from speculative record minting without primary-source recipe verification.

3. **Ungrounded / Ambiguous / Noise CultureMech Triage Rows (`mappings/culturemech_residual_triage.tsv`, 1,050 ungrounded `RESIDUAL` rows, plus 17 `MULTIPLE_EXACT`, 57 `AMBIGUOUS`, 23 `NOISE`, and 209 `UNMAPPED` rows):**
   - Consist of recipe-specific preparation annotations, truncated parser strings (`NOISE:bare_number`, `NOISE:truncated_quote`), homonymous normalized labels (`AMBIGUOUS`), concentration-prefixed labels, or ungrounded environmental/undefined mixtures that failed exact and normalized lexical lookup against local OAK databases (`CHEBI`, `NCIT`, `FOODON`, `ENVO`, `MICRO`, `UBERON`, `BTO`, `MESH`).

### B. Search Limits

- **Bounded Local Frontier Only:** Discovery was bounded to tracked repository manifests (`mappings/*.tsv`, `data/curated/*.yaml`, `scripts/*.py`) and local OAK ontology SQLite caches (`CHEBI`, `NCIT`, `FOODON`, `ENVO`, `MICRO`, `UBERON`, `BTO`, `MESH`), without paid external literature search (Edison/Falcon) or cross-repository mutations.
- **No Speculative Minting:** Per `.claude/skills/add-media/SKILL.md`, `.claude/skills/manage-identifiers/SKILL.md`, and `docs/MAPPING_SEMANTICS.md` Section 3, `kgmicrobe.ingredient:*` and `kgmicrobe.compound:*` identifiers are never minted for ambiguous strings, parser artifacts, or unverified complex solutions lacking citable composition evidence.
