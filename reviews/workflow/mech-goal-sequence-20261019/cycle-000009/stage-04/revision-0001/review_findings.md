# MediaIngredientMech Cycle 9 Stage 4 Review Findings

- **Run ID:** `mech-goal-sequence-20261019`
- **Cycle:** `9` (`cycle-000009`)
- **Stage:** `4` (`stage-04` / `record_review`)
- **Revision:** `1` (`revision-0001`)
- **Reviewed Source Revision:** `d486ad619366a88e4d4e3ed92009e5bfe00840af`
- **Structured Review Bundles (`reviews/structured/`):** `976` total (`961` initial per-record bundles `20261017T083000Z-*` + `1` successor per-record bundle `20261021T120500Z-ca-no32-x-4-h2o` + `14` corpus-wide reconciliation bundles `20261011T*-mim-*`)
- **Total Active Per-Record Findings:** `970` across `960` records (`644` open + `326` deferred in native per-record rubrics, carried forward in workflow lineage as `6` open root-cause cohorts `mim-c01-s04-f001` and `mim-c01-s04-f003` .. `mim-c01-s04-f007` for Cycle 9 Stage 5 resolution/deferral; `mim-c01-s04-f002` remains resolved under [#922](https://github.com/CultureBotAI/MediaIngredientMech/issues/922))

## Overview Table

| Workflow Finding ID | Carried From | Status | Category | Severity | Per-Record Count | Repair Owner Skill | Issue Link(s) | Summary |
| --- | --- | --- | --- | --- | ---: | --- | --- | --- |
| `mim-c01-s04-f001` | `mim-c01-s04-f001` | `open` | `quantity` | `major` | 1 | `.claude/skills/curate-yaml-record/SKILL.md` | [#921](https://github.com/CultureBotAI/MediaIngredientMech/issues/921) | Reconcile missing direct MicrobeDecoder occurrence on `data/ingredients/mapped/(2)-D-lyxose.yaml` (`CHEBI:62318`; native finding `rec-f-444b73747dddc915`) |
| `mim-c01-s04-f002` | `mim-c01-s04-f002` | `resolved` (Cycle 1 Stage 5) | `provenance` | `minor` | 0 active (1 resolved) | `.claude/skills/curate-yaml-record/SKILL.md` | [#922](https://github.com/CultureBotAI/MediaIngredientMech/issues/922) | Resolved in Cycle 1 Stage 5: corrected calcium nitrate correction-receipt identity text (`CHEBI:31348` -> `CHEBI:86159`) in `reports/sssom_completion_20260921/mapping_changes/review-record-issues-20261003.json` for `data/ingredients/mapped/Ca_No32_X_4_H2o.yaml` and verified in `reviews/structured/20261021T120500Z-ca-no32-x-4-h2o/review.yaml` |
| `mim-c01-s04-f003` | `mim-c01-s04-f003` | `open` | `provenance` | `minor` | 19 | `.claude/skills/curate-yaml-record/SKILL.md` | [#923](https://github.com/CultureBotAI/MediaIngredientMech/issues/923) | Normalize non-monotonic `curation_history` timestamp order across 19 mapped ingredient records |
| `mim-c01-s04-f004` | `mim-c01-s04-f004` | `open` | `evidence` | `major` | 624 | `.claude/skills/ingredient-roles/SKILL.md` | [#718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718) | Adjudicate prediction-only or empty primary nutritional/cellular role assertions lacking literature citations across 624 mapped records (`595` single-role + `29` multi-role) |
| `mim-c01-s04-f005` | `mim-c01-s04-f005` | `open` | `evidence` | `minor` | 29 | `.claude/skills/ingredient-roles/SKILL.md` | [#718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718) | Adjudicate prediction-only or empty secondary physicochemical role assertions lacking literature citations across 29 mapped records (`17` single-role + `12` multi-role) |
| `mim-c01-s04-f006` | `mim-c01-s04-f006` | `open` | `identity` / `grounding` | `major` | 266 (262 records) | `.claude/skills/map-media-ingredients/SKILL.md` | [#718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718) | Resolve exact chemical identity, preparation form, or complex parent scope across 262 unmapped/ambiguous records (`266` findings across `261` unmapped identity + `4` complex parent scope + `1` ambiguous `PYGS`) |
| `mim-c01-s04-f007` | `mim-c01-s04-f007` | `open` | `nomenclature` / `representation` / `identity` | `major` / `minor` | 31 | `.claude/skills/curate-yaml-record/SKILL.md` | [#718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718), [#861](https://github.com/CultureBotAI/MediaIngredientMech/issues/861) | Adjudicate context-dependent exported synonym/CAS token scope and component source scope across 31 records (`17` nomenclature token scope + `13` component source scope + `1` Furaltadone CAS alias) |

---

## Detailed Cohort Inventory

### 1. `mim-c01-s04-f001` — Direct MicrobeDecoder occurrence reconciliation for D-lyxose (`CHEBI:62318`)

- **Status:** `open` (carried forward from `mim-c01-s04-f001`)
- **Tracked In:** [#921](https://github.com/CultureBotAI/MediaIngredientMech/issues/921)
- **Category / Severity:** `quantity` / `major`
- **Field Path:** `occurrence_statistics.source_occurrences`
- **Target Record:**
  - `data/ingredients/mapped/(2)-D-lyxose.yaml` — structured review `reviews/structured/20261017T083000Z-2-d-lyxose/review.yaml` (`rec-f-444b73747dddc915`, issue key `mim-reconciliation-source-count-5703779de3d5d6d5`)
- **Observation & Carry-Forward Basis:** `occurrence_statistics.total_occurrences` (`0`) and synonyms reflect MicrobeDecoder merge provenance (`MERGED_FROM` `#398` absorbing `D-(-)-lyxose` and adding `D-lyxose` as a synonym), while `occurrence_statistics.source_occurrences` records only `{source: microbedecoder, count: 1, source_columns: BacDive_Metabolite_utilization}` (`kgmicrobe.trait:2_d_lyxose`) and omits the `159` direct `D-lyxose` (`kgmicrobe.trait:d_lyxose`) occurrences from `data/custom/microbedecoder/unmapped_labels.tsv`. `data/ingredients/mapped/(2)-D-lyxose.yaml` (`sha256: 8324965913eb03c529a1e3dc8187822300f6e0fd47451b1da3c6a3551f694c5b`) is byte-bound in `reports/sssom_completion_20260921/mapping_review/nonmapping_cohorts.json` (`owner_record_sha256: 62258c9bdabaf8728fafb6923345fe4b24b9956069113896acb16e9631c1451e`) and `reports/semantic_review_20260921/resolution/current-review.json` and co-located with open role-evidence finding `SEM:cd74f8ddafa04d7e9a9a` ([#718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718)).

### 2. `mim-c01-s04-f002` — Calcium nitrate correction-receipt identity text (`CHEBI:86159`) [RESOLVED]

- **Status:** `resolved` in Cycle 1 Stage 5 ([#922](https://github.com/CultureBotAI/MediaIngredientMech/issues/922))
- **Target Record:** `data/ingredients/mapped/Ca_No32_X_4_H2o.yaml`
- **Verification:** Successor structured review bundle `reviews/structured/20261021T120500Z-ca-no32-x-4-h2o/review.yaml` confirms `records[0].change` in `reports/sssom_completion_20260921/mapping_changes/review-record-issues-20261003.json` now accurately states `CHEBI:86159` (`calcium nitrate tetrahydrate`) with `verdict: pass_with_limitations`, `native_verdict: mapping_status=MAPPED; open=0; deferred=0; resolved=1`, `findings[0].status: resolved` (`rec-f-b6fa9d9b4f15850a`), and `0` open findings. Not carried forward in `carry_forward_ids`.

### 3. `mim-c01-s04-f003` — Non-monotonic `curation_history` timestamp order across 19 mapped ingredient records

- **Status:** `open` (carried forward from `mim-c01-s04-f003`)
- **Tracked In:** [#923](https://github.com/CultureBotAI/MediaIngredientMech/issues/923)
- **Category / Severity:** `provenance` / `minor`
- **Field Path:** `curation_history`
- **Target Records (19):**
  1. `data/ingredients/mapped/(R)-amygdalin.yaml` — `reviews/structured/20261017T083000Z-r-amygdalin/review.yaml` (`rec-f-1b5c835b0071446e`)
  2. `data/ingredients/mapped/(R)-lactate.yaml` — `reviews/structured/20261017T083000Z-r-lactate/review.yaml` (`rec-f-d55db516999a041d`)
  3. `data/ingredients/mapped/(R)-malic_Acid.yaml` — `reviews/structured/20261017T083000Z-r-malic-acid/review.yaml` (`rec-f-fbadd7724d0161a3`)
  4. `data/ingredients/mapped/(S)-azetidine-2-carboxylic_Acid.yaml` — `reviews/structured/20261017T083000Z-s-azetidine-2-carboxylic-acid/review.yaml` (`rec-f-586cd124536bc61a`)
  5. `data/ingredients/mapped/(S)-mandelic_Acid.yaml` — `reviews/structured/20261017T083000Z-s-mandelic-acid/review.yaml` (`rec-f-2430dd6d12832bea`)
  6. `data/ingredients/mapped/1-methylphenanthrene.yaml` — `reviews/structured/20261017T083000Z-1-methylphenanthrene/review.yaml` (`rec-f-8724f3e14c641797`)
  7. `data/ingredients/mapped/2-aminobenzoate.yaml` — `reviews/structured/20261017T083000Z-2-aminobenzoate/review.yaml` (`rec-f-aef200984b1f0476`)
  8. `data/ingredients/mapped/2-aminopentanoic_Acid.yaml` — `reviews/structured/20261017T083000Z-2-aminopentanoic-acid/review.yaml` (`rec-f-7f671c54445b7c91`)
  9. `data/ingredients/mapped/2-dehydro-D-gluconate.yaml` — `reviews/structured/20261017T083000Z-2-dehydro-d-gluconate/review.yaml` (`rec-f-df1e4f6c68d71909`)
  10. `data/ingredients/mapped/2-deoxyadenosine.yaml` — `reviews/structured/20261017T083000Z-2-deoxyadenosine/review.yaml` (`rec-f-0e7210521e16e8f4`)
  11. `data/ingredients/mapped/2-dichloroethane.yaml` — `reviews/structured/20261017T083000Z-2-dichloroethane/review.yaml` (`rec-f-ed7078c6b49d144b`)
  12. `data/ingredients/mapped/2-naphthyl_Dihydrogen_Phosphate.yaml` — `reviews/structured/20261017T083000Z-2-naphthyl-dihydrogen-phosphate/review.yaml` (`rec-f-cd6b4c06175bc72f`)
  13. `data/ingredients/mapped/2-naphthyl_Tetradecanoate.yaml` — `reviews/structured/20261017T083000Z-2-naphthyl-tetradecanoate/review.yaml` (`rec-f-470e7c790a4e8b31`)
  14. `data/ingredients/mapped/2-oxobutanoate.yaml` — `reviews/structured/20261017T083000Z-2-oxobutanoate/review.yaml` (`rec-f-53d647fe2cab0af6`)
  15. `data/ingredients/mapped/2-oxopentanoate.yaml` — `reviews/structured/20261017T083000Z-2-oxopentanoate/review.yaml` (`rec-f-3ef56bb048245b59`)
  16. `data/ingredients/mapped/3-aminobutyrate.yaml` — `reviews/structured/20261017T083000Z-3-aminobutyrate/review.yaml` (`rec-f-e196a530e349e691`)
  17. `data/ingredients/mapped/3-dehydro-D-gluconate.yaml` — `reviews/structured/20261017T083000Z-3-dehydro-d-gluconate/review.yaml` (`rec-f-2bcff34b33539abc`)
  18. `data/ingredients/mapped/3-hydroxybenzoate.yaml` — `reviews/structured/20261017T083000Z-3-hydroxybenzoate/review.yaml` (`rec-f-0f9fc988bb20137c`)
  19. `data/ingredients/mapped/3-trehalosamine.yaml` — `reviews/structured/20261017T083000Z-3-trehalosamine/review.yaml` (`rec-f-eba9703c056213b5`)
- **Observation & Carry-Forward Basis:** Imported `CurationEvent` entries in `curation_history` appear out of chronological order (`timestamp` decreases between consecutive events due to historical merge append order). All `19` affected records are byte-bound in `reports/sssom_completion_20260921/review.json` (`17` `SUPPORTED` + `2` `WITHHOLD`, with `5` also in `reports/sssom_completion_20260921/mapping_review/nonmapping_cohorts.json`) and `reports/semantic_review_20260921/resolution/current-review.json`, requiring coordinated re-review and receipt refresh under `src/mediaingredientmech/record_refresh.py`.

### 4. `mim-c01-s04-f004` — Prediction-only or empty primary nutritional/cellular role support across 624 mapped records

- **Status:** `open` (carried forward from `mim-c01-s04-f004`)
- **Tracked In:** [#718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718)
- **Category / Severity:** `evidence` / `major`
- **Field Paths:** `nutritional_roles[*]`, `cellular_roles[*]`
- **Sub-cohorts (624 findings across 624 mapped records):**
  - `595` single-role prediction-only findings (`Reassess prediction-only role support: <term>`), e.g.:
    - `data/ingredients/mapped/1-aminocyclopropane-1-carboxylate.yaml` (`reviews/structured/20261017T083000Z-1-aminocyclopropane-1-carboxylate/review.yaml`, `rec-f-cd99e5dd2fa64062`)
    - `data/ingredients/mapped/1-Kestose.yaml` (`reviews/structured/20261017T083000Z-1-kestose/review.yaml`, `rec-f-9445b49fdf863d47`)
    - `data/ingredients/mapped/14-B-D-Galactobiose.yaml` (`reviews/structured/20261017T083000Z-14-b-d-galactobiose/review.yaml`, `rec-f-457506125732ca52`)
  - `29` multi-role prediction-only or empty-evidence findings (`Reassess prediction-only or empty role support: <term>`), e.g.:
    - `data/ingredients/mapped/A-Ketoglutaric_Acid_Disodium_Salt_Hydrate.yaml` (`reviews/structured/20261017T083000Z-a-ketoglutaric-acid-disodium-salt-hydrate/review.yaml`, `rec-f-role-97df33f7b4c5ae1c`)
    - `data/ingredients/mapped/Beef_Extract.yaml` (`reviews/structured/20261017T083000Z-beef-extract/review.yaml`, `rec-f-role-da942f09736a0b84`)
    - `data/ingredients/mapped/Mgso4_X_7_H2o.yaml` (`reviews/structured/20261017T083000Z-mgso4-x-7-h2o/review.yaml`, `rec-f-role-93db3b16772e96e9`)
- **Observation:** Primary `nutritional_roles` or `cellular_roles` entries rely solely on `COMPUTATIONAL_PREDICTION` (`evidence: []` or heuristic notes) without organism- or recipe-backed `Citation` objects (`doi` / `pmid`). Full per-record inventory is indexed in `reviews/reconciliation/20261011T023739Z-all-mim/current-findings.tsv` and `reviews/structured/20261017T083000Z-*/review.yaml`.

### 5. `mim-c01-s04-f005` — Prediction-only or empty secondary physicochemical role support across 29 mapped records

- **Status:** `open` (carried forward from `mim-c01-s04-f005`)
- **Tracked In:** [#718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718)
- **Category / Severity:** `evidence` / `minor`
- **Field Path:** `physicochemical_roles[*]`
- **Sub-cohorts (29 findings across 29 mapped records):**
  - `17` single-role physicochemical findings (`data/ingredients/mapped/Ampicillin_Sodium_Salt.yaml`, `data/ingredients/mapped/Citric_Acidh2o.yaml`, `data/ingredients/mapped/Colistin_Sulfate_Salt.yaml`, `data/ingredients/mapped/D-_-lyxose.yaml`, `data/ingredients/mapped/D-Sucrose.yaml`, `data/ingredients/mapped/Edta_Acid_Form.yaml`, `data/ingredients/mapped/Edta_Chelating_Agent.yaml`, `data/ingredients/mapped/Glycylglycine.yaml`, `data/ingredients/mapped/Α-lipoic_Acid.yaml`, `data/ingredients/mapped/M-inositol.yaml`, `data/ingredients/mapped/Mnso4_X_1_H2o.yaml`, `data/ingredients/mapped/Na2-edta_X_2_H2o.yaml`, `data/ingredients/mapped/Na2s2o4.yaml`, `data/ingredients/mapped/Niso4_X_6_H2o.yaml`, `data/ingredients/mapped/Sodium_Phosphate_Dibasic.yaml`, `data/ingredients/mapped/Sodium_Thiosulfate_Pentahydrate.yaml`, `data/ingredients/mapped/Thioctic_Acid.yaml`).
  - `12` multi-role physicochemical findings (`data/ingredients/mapped/Aces.yaml`, `data/ingredients/mapped/Acetate_Carbon_Source.yaml`, `data/ingredients/mapped/Ammonium_Chloride_Nitrogen_Source.yaml`, `data/ingredients/mapped/Calcium_D-Pantothenate.yaml`, `data/ingredients/mapped/Glucose_2.yaml`, `data/ingredients/mapped/Glycerol_2.yaml`, `data/ingredients/mapped/L-cysteine_Hydrochloride_Monohydrate.yaml`, `data/ingredients/mapped/Maltose_2.yaml`, `data/ingredients/mapped/Mgso47h2o_2.yaml`, `data/ingredients/mapped/Mgso47h2o.yaml`, `data/ingredients/mapped/Sodium_Acetate.yaml`, `data/ingredients/mapped/Sodium_L-lactate.yaml`).

### 6. `mim-c01-s04-f006` — Unresolved exact chemical identity, preparation form, or complex parent scope across 262 unmapped/ambiguous records (266 findings)

- **Status:** `open` (carried forward from `mim-c01-s04-f006`)
- **Tracked In:** [#718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718)
- **Category / Severity:** `identity` & `grounding` / `major`
- **Field Paths:** `mapping_status`, `ontology_id`, `preferred_term`
- **Sub-cohorts (266 findings across 262 records; 4 unmapped records carry both an unresolved-identity finding and an unmapped-parent-scope finding):**
  - `261` unmapped/ambiguous ingredient records under `data/ingredients/unmapped/*.yaml` (`Unresolved exact identity or preparation: <term>`, e.g., `data/ingredients/unmapped/2-Carene-3-One.yaml`, `data/ingredients/unmapped/2-methyladeninyl_Cobamide.yaml`).
  - `4` unmapped complex parent-scope findings on records under `data/ingredients/unmapped/*.yaml`:
    - `data/ingredients/unmapped/Inorganic_Salts-starch_Agar.yaml` (`reviews/structured/20261017T083000Z-inorganic-salts-starch-agar/review.yaml`, `rec-f-db0057fd92fe4a5e`)
    - `data/ingredients/unmapped/Iron_As_Fecl3_In_Edta.yaml` (`reviews/structured/20261017T083000Z-iron-as-fecl3-in-edta/review.yaml`, `rec-f-a82fd6f60ae904bd`)
    - `data/ingredients/unmapped/Khayasin_C.yaml` (`reviews/structured/20261017T083000Z-khayasin-c/review.yaml`, `rec-f-63745f40d17b8fdf`)
    - `data/ingredients/unmapped/Xyloglucan_Heptaoctanona_Saccharides.yaml` (`reviews/structured/20261017T083000Z-xyloglucan-heptaoctanona-saccharides/review.yaml`, `rec-f-3369303f7d065baa`)
  - `1` ambiguous formulation abbreviation finding on a mapped record:
    - `data/ingredients/mapped/PYGS.yaml` (`reviews/structured/20261017T083000Z-pygs/review.yaml`, `rec-f-8c2aaaf16e546640`)

### 7. `mim-c01-s04-f007` — Context-dependent exported synonym/CAS token scope and component source-scope adjudication across 31 records

- **Status:** `open` (carried forward from `mim-c01-s04-f007`)
- **Tracked In:** [#718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718), [#861](https://github.com/CultureBotAI/MediaIngredientMech/issues/861)
- **Category / Severity:** `nomenclature` (`major`, 17), `representation` (`major`, 13), `identity` (`minor`, 1)
- **Field Paths:** `synonyms`, `SSSOM.other`, `occurrence_statistics`, `chemical_properties.cas_rn`
- **Sub-cohorts (31 findings):**
  - `17` `nomenclature` findings (`Adjudicate source scope of exported tokens`): `data/ingredients/mapped/4-vinylphenol.yaml`, `data/ingredients/mapped/Artificial_seawater.yaml`, `data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml`, `data/ingredients/mapped/DL_Vitamins.yaml`, `data/ingredients/mapped/Fatty_Acid_Mixture_See_Medium_No_266.yaml`, `data/ingredients/mapped/Mineral_Solution_See_Medium_No_976.yaml`, `data/ingredients/mapped/Modified_Trace_Vitamins.yaml`, `data/ingredients/mapped/Peptone.yaml`, `data/ingredients/mapped/Potassium_Phosphate_Buffer.yaml`, `data/ingredients/mapped/Riboflavin.yaml`, `data/ingredients/mapped/Sludge_fluid.yaml`, `data/ingredients/mapped/Soil_Extract.yaml`, `data/ingredients/mapped/Trace_Element_Solution_See_Medium_No_187.yaml`, `data/ingredients/mapped/Trace_Metal_Mix_A5.yaml`, `data/ingredients/mapped/Trace_Mineral_Solution.yaml`, `data/ingredients/mapped/Trace_Minerals.yaml`, `data/ingredients/mapped/Yeast_Extract.yaml`.
  - `13` `representation` findings (`Reassess component source scope`): `data/ingredients/mapped/Fastidious_Anaerobe_Broth_With_Meat_Granules.yaml`, `data/ingredients/mapped/Modified_Cooked_Meat_Medium.yaml`, `data/ingredients/mapped/PY-cellobiose.yaml`, `data/ingredients/mapped/PY-fructose.yaml`, `data/ingredients/mapped/PY-glucose-rumen_Fluid.yaml`, `data/ingredients/mapped/PY-maltose.yaml`, `data/ingredients/mapped/PY-pectin.yaml`, `data/ingredients/mapped/PYEG.yaml`, `data/ingredients/mapped/PYG-002_Tween_80.yaml`, `data/ingredients/mapped/PYG_Rumen_Fluid.yaml`, `data/ingredients/mapped/PYG.yaml`, `data/ingredients/mapped/PYGS.yaml`, `data/ingredients/mapped/TYGVS_Glucose.yaml`.
  - `1` `identity` finding (`Verify retained Furaltadone CAS alias`): `data/ingredients/mapped/Furaltadone_Hydrochloride.yaml` (`reviews/structured/20261017T083000Z-furaltadone-hydrochloride/review.yaml`, `rec-f-a7e06cacf823b6f9`).
