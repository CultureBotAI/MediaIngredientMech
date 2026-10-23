# Cycle 3 Stage 4 Record & Cohort Review Report (`record_review`)

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `3` (`cycle-000003`)
- **Stage**: `4` (`stage-04` / `record_review` / `review_yaml_records`)
- **Revision**: `revision-0001`
- **Source Revision (`main`)**: `524fa44d989b3e272cb3bff9d68e53d02407dac7`
- **Scope Frozen At**: `2026-10-23T12:15:00Z`
- **Previous Evidence**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-05/revision-0001/evidence.yaml` (`sha256: ad70008f1b7348a8da9abea22a245585f32fc764a99869942b03f8baab955840`)
- **Repository-Local Skills Applied**:
  - `.claude/skills/review-yaml-record/SKILL.md`
  - `.claude/skills/review-yaml-category/SKILL.md`
  - `.claude/skills/mediaingredientmech-evolve-workflow/SKILL.md`
  - `docs/record-reviews.md` & `docs/record-review-profile.md`

---

## 1. Frozen Inventory & Provenance Digests

The Cycle 3 Stage 4 record review froze the authoritative corpus at `main` commit `524fa44d989b3e272cb3bff9d68e53d02407dac7` (merged PR `#937` from Cycle 3 Stage 3). Between the Cycle 2 Stage 4 frozen revision (`88a0a15a3e340068d442b7e25bfa0ced637e0bcd`) / Cycle 2 Stage 5 frozen revision (`7f56a13130d8d220efa48cef78559e80351c5a46`) and `524fa44d989b3e272cb3bff9d68e53d02407dac7`, `git diff` across `data/ingredients/`, `data/curated/`, and `reviews/structured/` is empty (`0` modified, added, or deleted YAML records or structured review bundles), because Cycle 2 Stages 5–6 and Cycle 3 Stages 1–3 were non-mutating assessment, remediation-reconciliation, and frontier-exhaustion stages.

| Corpus Slice | Path Pattern | File / Record Count | Digest Type | SHA-256 Digest |
| --- | --- | ---: | --- | --- |
| All individual `IngredientRecord` YAML files | `data/ingredients/**/*.yaml` | `2,953` | `sha256sum` manifest (`LC_ALL=C sort`) | `3b760eeec31525e7bdf8e45623ec53fb4ac521866d9ab5bafeea9160a4d2d99f` |
| All individual `IngredientRecord` YAML files | `data/ingredients/**/*.yaml` | `2,953` | `path:sha256` manifest (`LC_ALL=C sort`) | `4a44101e2fb6199658c0fcced12a4cbd2f6624b60afd520a197e3049ccf502c7` |
| Mapped directory individual YAML files | `data/ingredients/mapped/*.yaml` | `2,680` (`2,609` `MAPPED`, `71` `REJECTED`) | `sha256sum` manifest (`LC_ALL=C sort`) | `3cdce1d4d3ca11f92c6c96604bc57052ec841791e58f38ac5ea0070df33e61d8` |
| Unmapped directory individual YAML files | `data/ingredients/unmapped/*.yaml` | `273` (`2` `MAPPED`, `260` `UNMAPPED`, `1` `AMBIGUOUS`, `10` `REJECTED`) | `sha256sum` manifest (`LC_ALL=C sort`) | `c5b8261298412767b8ebdd953819c2891235d8bf397d51f7efd55a8efe43ed99` |
| Active collection file — mapped | `data/curated/mapped_ingredients.yaml` | `1` (`2,680` records) | Single-file SHA-256 | `4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b` |
| Active collection file — unmapped | `data/curated/unmapped_ingredients.yaml` | `1` (`273` records) | Single-file SHA-256 | `8f574be094e741f1d59d55618cc14bf375304644732508bd7a5cd4a817c7fce2` |
| Active collection file — complex media | `data/curated/complex_ingredients.yaml` | `1` (`4` records) | Single-file SHA-256 | `a1cb7ca74c6731e02f36d025cc53de16f715d0efcd405d1c0c563a0808dfcb3c` |
| Historical snapshot — mapped pre-reclassify | `data/curated/mapped_ingredients_pre_reclassify.yaml` | `1` | Single-file SHA-256 | `7323ef988a5e0815b8c04d3ab1f185ef2b1d707f83f2f308155a9bbfe455a44d` |
| Historical snapshot — unmapped pre-reclassify | `data/curated/unmapped_ingredients_pre_reclassify.yaml` | `1` | Single-file SHA-256 | `5df035de8f491a7a5c5f9b87d7bb9e0e5fd0178a945fb45ddcb163281d590b08` |
| Historical snapshot — mapped backup | `data/curated/mapped_ingredients.yaml.bak` | `1` | Single-file SHA-256 | `45de160a8a327b7999a9c2ba72a0400ca34ff519263869fb1d7d768ac663d02f` |
| Historical snapshot — unmapped backup | `data/curated/unmapped_ingredients.yaml.bak` | `1` | Single-file SHA-256 | `8542a04da0e1dc6a0b6c0fd2d50f16fc2752bd2e897bc3c5ec39b433c3b07de9` |
| Native structured review bundles | `reviews/structured/**/review.{yaml,md}` | `976` bundles (`1,952` files) | `sha256sum` manifest (`LC_ALL=C sort`) | `17c962c558829428cc5c6df8c8be66afa4791c20b781b60a846e6695d038bb6f` |
| Record review schema | `schema/record_review.yaml` | `1` | Single-file SHA-256 | `229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb` |
| Ingredient LinkML schema | `src/mediaingredientmech/schema/mediaingredientmech.yaml` | `1` | Single-file SHA-256 | `bb43dee29b21fdee72a48022456e733e49e95824c4c09674f9b3165c290fe012` |
| Tracked review latest index | `reviews/workflow/latest.yaml` | `1` (`6` verified entries) | Single-file SHA-256 | `cb3ab020c5b24a1df52bdbbc8b1bc0a2c2108a6949951e316425875d5c3141f9` |
| Infrastructure task register | `INFRA_TASKS.md` | `1` (`0` pending items) | Single-file SHA-256 | `dda5707f52661e91f46d96fcbabfc256ac39d4cc865a28a3e5ab6f0536958a5e` |

---

## 2. Corpus Stratification & Review Coverage (`100%`)

Every eligible `IngredientRecord` YAML file (`2,953 / 2,953`) and every collection YAML document (`7 / 7`) in the frozen inventory was audited against:
1. Closed-schema LinkML validation (`scripts/validate_strict.py`),
2. Native structured review bundle verification (`scripts/record_review.py check` across all `976` bundles in `reviews/structured/`),
3. Component partonomy invariants (`scripts/validate_component_partonomy.py` across `83` decomposed mixtures and `502` `StockComponent` assertions),
4. SSSOM invariant verification (`scripts/validate_sssom_invariants.py`),
5. Duplicate identifier audit (`scripts/audit_duplicate_identifiers.py --check`),
6. Semantic review ledger (`reports/semantic_review_20260921/resolution/current-review.json` and `reports/semantic_review_20260921/resolution/finding-dispositions.tsv`).

### 2.1 By Mapping Status and Identifier Family

| Mapping Status | Identifier Prefix | Record Count | Clean Records (`0` Active Findings) | Records with Active Findings | Active Finding Count |
| --- | --- | ---: | ---: | ---: | ---: |
| `MAPPED` | `CHEBI:` | `2,243` | `1,622` | `621` | `626` |
| `MAPPED` | `FOODON:` | `87` | `78` | `9` | `10` |
| `MAPPED` | `UBERON:` | `15` | `14` | `1` | `1` |
| `MAPPED` | `ENVO:` | `11` | `10` | `1` | `1` |
| `MAPPED` | `NCIT:` | `7` | `7` | `0` | `0` |
| `MAPPED` | `MESH:` | `1` | `1` | `0` | `0` |
| `MAPPED` | `CAS-RN:` | `94` | `61` | `33` | `33` |
| `MAPPED` | `PUBCHEM.COMPOUND:` | `20` | `8` | `12` | `12` |
| `MAPPED` | `KEGG.COMPOUND:` | `1` | `1` | `0` | `0` |
| `MAPPED` | `KEGG.DRUG:` | `1` | `1` | `0` | `0` |
| `MAPPED` | `DRUGBANK:` | `1` | `1` | `0` | `0` |
| `MAPPED` | `SIGMA:` | `1` | `0` | `1` | `1` |
| `MAPPED` | `CONFLICT_` | `6` | `6` | `0` | `0` |
| `MAPPED` | `kgmicrobe.ingredient:` | `123` | `102` | `21` | `21` |
| **Subtotal (`MAPPED`)** | — | **`2,611`** | **`1,912`** | **`699`** | **`705`** |
| `UNMAPPED` | `UNMAPPED_` | `259` | `0` | `259` | `263` |
| `UNMAPPED` | `CHEBI:` (`unmapped/Water.yaml`) | `1` | `0` | `1` | `1` |
| `AMBIGUOUS` | `UNMAPPED_0249` (`PYGS.yaml`) | `1` | `0` | `1` | `1` |
| **Subtotal (`UNMAPPED` + `AMBIGUOUS`)** | — | **`261`** | **`0`** | **`261`** | **`265`** |
| `REJECTED` | `UNMAPPED_` (`80`) / `CHEBI:` (`1`) | `81` | `81` | `0` | `0` |
| **Total Individual Records** | — | **`2,953`** | **`1,993`** | **`960`** | **`970`** |

> **Historical Resolution Verified (`Ca_No32_X_4_H2o.yaml`)**: In Cycle 1 Stage 5 (PR `#924`, issue `#922`), `data/ingredients/mapped/Ca_No32_X_4_H2o.yaml` was remediated (`curation_history` timestamp ordered monotonically and `occurrence_statistics.total_occurrences` reconciled to `42`) and superseded by native review bundle `reviews/structured/20261021T120500Z-ca-no32-x-4-h2o/` (`overall_verdict: pass`, `0` active findings). Thus `1,993` records pass with `0` active findings (`1,912` `MAPPED` + `81` `REJECTED`) and `960` records carry `970` active findings across `6` carry-forward cohorts (`mim-c01-s04-f001` and `mim-c01-s04-f003` .. `mim-c01-s04-f007`).

---

## 3. Native Structured Review Bundles (`reviews/structured/`)

All `976` structured review bundles in `reviews/structured/` pass `scripts/record_review.py check` (`valid_reviews: 976`, `0` stale `source_sha256` hashes):

1. **Corpus-wide & Category Reconciliation Bundles (`14` bundles, `20261011T*-mim-*`)**:
   - `20261011T091315Z-mim-review-reconcile`: Reconciled legacy review cohorts (`15` resolved findings).
   - `20261011T105147Z-mim-20260921-1509-chebi-53753-mapping`: Resolved `CHEBI:53753` mapping split (`1` resolved finding).
   - `20261011T114628Z-mim-corpus-audit-a` (`A–E`, `562` mapped records, `0` findings, `pass`).
   - `20261011T114629Z-mim-corpus-audit-f` (`F–L`, `493` mapped records, `0` findings, `pass`).
   - `20261011T114630Z-mim-corpus-audit-m` (`M–R`, `578` mapped records, `0` findings, `pass`).
   - `20261011T114631Z-mim-corpus-audit-s` (`S–Z`, `978` mapped records, `1` finding on `(2)-D-lyxose.yaml`, `needs_follow_up`).
   - `20261011T114632Z-mim-corpus-audit-unmapped` (`261` unmapped/ambiguous records, `0` structural errors, `pass`).
   - `20261011T114633Z-mim-corpus-audit-rejected` (`81` rejected records, `0` findings, `pass`).
   - `20261011T150500Z-mim-20261011-114631-s-d-lyxose-occurrence`: Detailed trace of `kgmicrobe.trait:d_lyxose` (`159` occurrences) across `(2)-D-lyxose.yaml` (`CHEBI:62318`) and `D-lyxose.yaml` (`CHEBI:17140`).
   - `20261011T163951Z-mim-curation-history-order-mapped-a` (`A–P`, `9` records with non-monotonic `curation_history` timestamps).
   - `20261011T163952Z-mim-curation-history-order-mapped-b` (`S–Z`, `11` initial records with non-monotonic `curation_history` timestamps, `1` of which — `Ca_No32_X_4_H2o.yaml` — was resolved in Cycle 1 Stage 5).
   - `20261011T183500Z-mim-semantic-review-20260921-active-findings` (`944` records carrying `950` active semantic review findings).
   - `20261011T194500Z-mim-collection-files-audit` (`7` collection YAML files in `data/curated/`).
   - `20261011T211000Z-mim-ca-no32-x-4-h2o-occurrence-total` (`Ca_No32_X_4_H2o.yaml` occurrence total mismatch, resolved in Cycle 1 Stage 5 and superseded by `20261021T120500Z-ca-no32-x-4-h2o`).
2. **Per-Record Structured Review Bundles (`962` bundles: `961` initial `20261017T083000Z-*` + `1` successor `20261021T120500Z-ca-no32-x-4-h2o`)**:
   - Every one of the `960` records with active findings has an up-to-date individual bundle in `reviews/structured/20261017T083000Z-<slug>/review.{yaml,md}` whose `reviewed_paths[0].source_sha256` matches the current file on `main`.
   - `data/ingredients/mapped/Ca_No32_X_4_H2o.yaml` has its historical bundle `20261017T083000Z-ca-no32-x-4-h2o` superseded by `20261021T120500Z-ca-no32-x-4-h2o` (`overall_verdict: pass`, `source_sha256: 7f2aa363d61df3d375b4503ba77c0472ffbc8d0a341b66c55cf88557c1cc11dd`).

---

## 4. Summary of Active Findings Carry-Forward (`6` Root-Cause Cohorts)

All `970` active per-record findings across `960` records roll up into `6` stable root-cause finding IDs carried forward from `mim-c01-s04-f001` and `mim-c01-s04-f003` .. `mim-c01-s04-f007` (with `mim-c01-s04-f002` resolved in Cycle 1 Stage 5):

| Finding ID | Carried From |Tracked Issue | Records Affected | Active Findings | Severity / Effort | Disposition for Stage 5 |
| --- | --- | --- | ---: | ---: | --- | --- |
| `mim-c01-s04-f001` | `mim-c01-s04-f001` | [#921](https://github.com/CultureBotAI/MediaIngredientMech/issues/921) | `1` | `1` | `warning` / `low` | Preserve for Stage 5 (byte-bound in `nonmapping_cohorts.json` and `current-review.json`; co-located with `SEM:cd74f8ddafa04d7e9a9a`) |
| `mim-c01-s04-f003` | `mim-c01-s04-f003` | [#923](https://github.com/CultureBotAI/MediaIngredientMech/issues/923) | `19` | `19` | `warning` / `low` | Preserve for Stage 5 (all `19` records are byte-bound in `reports/sssom_completion_20260921/review.json` and `current-review.json`) |
| `mim-c01-s04-f004` | `mim-c01-s04-f004` | [#718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718) | `624` | `624` | `warning` / `medium` | Preserve for Stage 5 (requires primary `doi`/`pmid` literature citations for nutritional/cellular roles) |
| `mim-c01-s04-f005` | `mim-c01-s04-f005` | [#718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718) | `29` | `29` | `warning` / `medium` | Preserve for Stage 5 (requires primary literature/formulation citations for physicochemical roles) |
| `mim-c01-s04-f006` | `mim-c01-s04-f006` | [#718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718) | `262` | `266` | `warning`–`error` / `medium`–`high` | Preserve for Stage 5 (requires source-backed identity or recipe-form resolution across `261` unmapped/ambiguous + `4` complex records) |
| `mim-c01-s04-f007` | `mim-c01-s04-f007` | [#718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718) | `31` | `31` | `warning`–`error` / `medium` | Preserve for Stage 5 (requires source-recipe verification and coordinated SSSOM/component receipt updates across `17` token-scope + `13` component-scope + `1` CAS alias records) |

*(Note: `6` records overlap between cohorts: `(2)-D-lyxose.yaml` is in `mim-c01-s04-f001` and `mim-c01-s04-f004`; `H3bo4.yaml`, `Magnesium_Chloride_Anhydrous.yaml`, `Mnso4_X_7_H2o.yaml`, `Modified_Pfennig_Medium_Sl-8_Solution_B_Medium_28.yaml`, and `Trace_Element_Solution_Sl-8_Medium_192.yaml` are in both `mim-c01-s04-f003` and `mim-c01-s04-f004`/`f006`/`f007`, yielding `960` unique records with active findings.)*

---

## 5. Limitations & Guardrails Observed

1. **Byte-Bound Receipt Invariants (`src/mediaingredientmech/record_refresh.py`)**:
   - `reports/sssom_completion_20260921/review.json`, `reports/sssom_completion_20260921/mapping_review/nonmapping_cohorts.json`, and `reports/semantic_review_20260921/resolution/current-review.json` bind reviewed records by exact `owner_record_sha256` / `subject_record_sha256`. Under `src/mediaingredientmech/record_refresh.py`, mechanical edits to those records cannot preserve byte-bound semantic/SSSOM approvals via receipt chains without full re-review of the record's semantic/SSSOM findings.
2. **Evidence & Grounding Non-Fabrication**:
   - No synthetic `doi`/`pmid` references, speculative ChEBI/FoodOn/UBERON identifiers, or unverified component assertions were introduced during this review stage.
3. **Tracked Review Index Verification (`reviews/workflow/latest.yaml`)**:
   - Verified that `reviews/workflow/latest.yaml` (`sha256: cb3ab020c5b24a1df52bdbbc8b1bc0a2c2108a6949951e316425875d5c3141f9`) already matches all `6` verified evidence entries in `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/workspace/session-orchestration/20261019/mediaingredientmech/verified-evidence-index.json` (Cycle 1 Stages 4–6 and Cycle 2 Stages 4–6).
