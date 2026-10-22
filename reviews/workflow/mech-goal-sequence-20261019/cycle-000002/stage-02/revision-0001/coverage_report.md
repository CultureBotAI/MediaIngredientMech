---
artifact_kind: stage_02_causal_graphs_coverage_report
run_id: mech-goal-sequence-20261019
cycle: 2
stage: 2
stage_name: causal_graphs
revision: 1
repository: CultureBotAI/MediaIngredientMech
base_commit: 4fe89042a00f238c79e34d765792659c572caead
workflow_sha256: 059b5b9401ffeb04483cf7a46570f7f2f3c8c7fe6e574d80954bf71233cc609a
generated_at: "2026-10-22T02:58:00Z"
skills_applied:
  - .claude/skills/mediaingredientmech-evolve-workflow/SKILL.md
  - .claude/skills/curate-causal-graphs/SKILL.md
  - .claude/skills/curate-yaml-record/SKILL.md
records_scanned: 2953
mapped_dir_records: 2690
unmapped_dir_records: 263
eligible_records_reviewed: 2496
ineligible_or_excluded_records: 457
records_currently_carrying_causal_graphs: 0
records_modified: 0
---

# Cycle 2, Stage 2 (`causal_graphs`) — Whole-Corpus Eligibility Inventory, Source-Grounded Claim Review, and Prerequisite Blocker Ledger

## 1. Executive Summary

This report records the Cycle 2, Stage 2 (`causal_graphs`) whole-corpus review for `CultureBotAI/MediaIngredientMech` at `main` commit `4fe89042a00f238c79e34d765792659c572caead` under `.claude/skills/curate-causal-graphs/SKILL.md`, `.claude/skills/curate-yaml-record/SKILL.md`, `docs/CAUSAL_GRAPH_CONTRACT.md`, and `MAPPING_SEMANTICS.md` Section 7.

1. **Whole-Corpus Scope Verified (`2,953` YAML records):** Every YAML record in `data/ingredients/mapped/*.yaml` (`2,690` files) and `data/ingredients/unmapped/*.yaml` (`263` files) was inspected and classified under `docs/CAUSAL_GRAPH_CONTRACT.md` Rule A2 (Identity Gate) and Rule B3 (`CausalGraph.explains` role-grounding invariants). Currently, **`0` of `2,953` records** carry a populated `causal_graphs` slot (`records_modified: 0`).
2. **Contract Implementation Status (`docs/CAUSAL_GRAPH_CONTRACT.md` Section 12):**
   - **Implemented (Steps 1–2):** LinkML schema definitions (`IngredientRecord.causal_graphs`, `CausalGraph`, `CausalNode`, `CausalEdge`, `ProteinExample`, `EvidenceItem`, and `MIM.vocab:*` enums in `src/mediaingredientmech/schema/mediaingredientmech.yaml`), fleet parity and closed-schema rule test suite (`tests/test_causal_graph_schema.py`, 39 tests passing), and the readiness scorer (`scripts/score_causal_graph_readiness.py` + `tests/test_score_causal_graph_readiness.py`, 27 tests passing).
   - **Unimplemented Prerequisites (Steps 3–7, tracked in `INFRA_TASKS.md` under `INFRA-006` / GitHub issue `#925`):**
     - `conf/sibling_pins.yaml` (absent)
     - `mappings/cross_mech_references.tsv` (absent)
     - `mappings/cross_mech_assertions.jsonl` (absent)
     - `mappings/ontology_facts.tsv` (absent)
     - `mappings/cross_mech_links.tsv` (absent)
     - `just qc-causal-graphs` enforcing the 31 rule codes across Rules A1–E2 (absent from `justfile`)
     - Validated native causal-graph writer and one-record canary `data/ingredients/mapped/Na2moo4_X_2_H2o.yaml` (absent)
3. **Native-Only Preservation Policy Enforced:** Per `.claude/skills/curate-causal-graphs/SKILL.md` ("Never hand-write unvalidated `causal_graphs` YAML when the repository's `qc-causal-graphs` gate or snapshot prerequisites are unimplemented"), **`0` ingredient YAML files were modified**. Instead, all `2,496` Rule A2-eligible records and `457` ineligible/excluded records are cataloged with exact dispositions, and 12 representative candidate records spanning all 7 chemical-speciation bridge kinds (`HYDRATE_PART`, `ION_PART`, `PROTONATION`, `STRUCTURAL_FORM`, `GENERIC_SPECIALISATION`, `FORM_OF_PARENT`, `COMPONENT`) and both `graph_kind` values (`ROLES`, `SPECIATION`) are reviewed with source-grounded mechanism claims, `ProteinExample` anchors, and exact prerequisite blockers.

---

## 2. Verified Input Files and SHA-256 Digests

| Input Artifact / Corpus Slice | Path | SHA-256 Digest / Count | Status |
|---|---|---|---|
| Causal Graph Contract | `docs/CAUSAL_GRAPH_CONTRACT.md` | `de889fdea9ad18e6cf3502461d779e76ef6e99f923e374b0a5309fe163871d65` | Verified (Steps 1–2 done; Steps 3–7 planned) |
| Mapping Semantics Contract | `MAPPING_SEMANTICS.md` | `94aad13ea0fc3df82a37383f388f41432b607b04cac61ae5792ce1a381aef805` | Verified (Section 7 chemical-speciation bridge boundary) |
| LinkML Schema | `src/mediaingredientmech/schema/mediaingredientmech.yaml` | `bb43dee29b21fdee72a48022456e733e49e95824c4c09674f9b3165c290fe012` | Verified (`CausalGraph`, `CausalNode`, `CausalEdge`, `ProteinExample`) |
| Duplicate Identifier Baseline | `mappings/duplicate_identifier_baseline.tsv` | `723f613de746bf44b38e19be9786cd1ee7fb719256fbc6195b8b1e20477d5720` | Verified (`15` duplicate identifier groups across `35` mapped records) |
| Canonical SSSOM Mapping File | `mappings/ingredient_mappings.sssom.tsv` | `89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9` | Verified (Rules A, B1–B3, B5, C–L pass; 0 rejects) |
| Infrastructure Backlog Ledger | `INFRA_TASKS.md` | `dda5707f52661e91f46d96fcbabfc256ac39d4cc865a28a3e5ab6f0536958a5e` | Verified (`INFRA-006` / `#925` tracks Steps 3–7) |
| Causal Graph Readiness Scorer | `scripts/score_causal_graph_readiness.py` | `32411c33b4c7f10fd1753bfa245872b455ee14293075b76469cdafc713169354` | Verified (ranks mapped/unmapped records by 100-point rubric) |
| Causal Graph Schema Test Suite | `tests/test_causal_graph_schema.py` | `38b0d02b048ce069bb03d6e3e3475894ed8121d152ea4a7b6211123a82df14f3` | Verified (`39/39` tests pass) |
| Whole Ingredient Corpus (`2,953` YAML files) | `data/ingredients/{mapped,unmapped}/*.yaml` | Composite SHA-256 (`<path>:<sha256>\n` sorted): `4a44101e2fb6199658c0fcced12a4cbd2f6624b60afd520a197e3049ccf502c7` | Verified (`2,690` in `mapped/`, `263` in `unmapped/`; `0` carry `causal_graphs`) |

---

## 3. Prerequisite Gate & Snapshot Infrastructure Check (`docs/CAUSAL_GRAPH_CONTRACT.md` Steps 3–7)

| Prerequisite Component | Contract Reference | Expected Path / Recipe | Present in Repo? | Impact on Stage 2 Curation |
|---|---|---|---|---|
| Sibling repository SHA & ontology version pins | Step 3 (Section 10.1) | `conf/sibling_pins.yaml` | `False` (absent) | Blocks deterministic cross-repo snapshot generation (`UNPINNED_EXTERNAL_ASSERTION` / `SNAPSHOT_PIN_DRIFT`). |
| Cross-Mech reference index | Step 3 (Section 10.2) | `mappings/cross_mech_references.tsv` | `False` (absent) | Blocks validation of `CultureMech`, `TraitMech`, `CellStructureMech`, `PerytonMech`, and `CommunityMech` target nodes (`CROSS_MECH_REF_UNINDEXED`). |
| Cross-Mech assertion snapshot | Step 3 (Section 10.3) | `mappings/cross_mech_assertions.jsonl` | `False` (absent) | Blocks `CROSS_MECH_ASSERTION_DRIFT` verification for edges citing sibling mechanism records. |
| Pinned ontology fact table | Step 4 (Section 4.3, 10.4) | `mappings/ontology_facts.tsv` | `False` (absent) | Blocks `CHEMICAL_STRUCTURE` and `ONTOLOGY_ASSERTED` bridge verification (`SPECIATION_FACT_NOT_FOUND` / `ONTOLOGY_BRIDGE_NOT_IN_SNAPSHOT`). |
| Cross-Mech edge index | Step 6 (Section 11) | `mappings/cross_mech_links.tsv` | `False` (absent) | Blocks downstream KG-Microbe cross-Mech edge ingestion. |
| Offline/online causal-graph QC gate | Step 4 (Section 9) | `just qc-causal-graphs` (`--offline` / `--online`) | `False` (absent from `justfile`) | Blocks enforcement of all 31 rule codes across Rules A1–E2; per skill rules, graphs cannot be written onto records without this gate. |
| Validated causal-graph writer & canary | Step 5 (Section 12) | Writer script + `data/ingredients/mapped/Na2moo4_X_2_H2o.yaml` canary | `False` (absent) | Blocks native YAML mutation; all candidate graphs must remain documented proposals until Step 4 & Step 5 land (`#925`). |

---

## 4. Whole-Corpus Causal-Graph Eligibility Inventory (`2,953` Records)

### 4.1 Mutually Exclusive Corpus Partition under Rule A2 (Identity Gate) and Rule B3 (`explains` Role Gate)

Every record in `data/ingredients/mapped/*.yaml` (`2,690`) and `data/ingredients/unmapped/*.yaml` (`263`) falls into exactly one of the following mutually exclusive cohorts:

| Cohort ID | Eligibility Class | Rule A2 / Rule B3 Criteria | Record Count | Skill Disposition (`curate-causal-graphs`) | Representative Record (`path` / `identifier`) |
|---|---|---|---:|---|---|
| **I1** | Ineligible (`UNMAPPED` non-`NAMED_MEDIUM`) | `mapping_status=UNMAPPED`, `ingredient_type != NAMED_MEDIUM` (`NOT_ELIGIBLE_RECORD`) | `159` | `excluded` (`not_mapped`) | `data/ingredients/unmapped/Acids.yaml` (`UNMAPPED_0063`) |
| **I2** | Ineligible (`UNMAPPED` + `NAMED_MEDIUM`) | `mapping_status=UNMAPPED`, `ingredient_type=NAMED_MEDIUM` (`NOT_ELIGIBLE_RECORD`) | `101` | `excluded` (`not_mapped` + `not_applicable`) | `data/ingredients/unmapped/2x_YT_Broth.yaml` (`UNMAPPED_0146`) |
| **I3** | Ineligible (`REJECTED` merge tombstones, non-baseline) | `mapping_status=REJECTED`, not in `mappings/duplicate_identifier_baseline.tsv` (`NOT_ELIGIBLE_RECORD`) | `79` | `excluded` (`rejected_tombstone`) | `data/ingredients/mapped/Agar_Noble.yaml` (`CHEBI:2509`) |
| **I4** | Ineligible (`REJECTED` merge tombstones in duplicate baseline) | `mapping_status=REJECTED`, identifier listed in `mappings/duplicate_identifier_baseline.tsv` (`NOT_ELIGIBLE_RECORD`) | `2` | `excluded` (`rejected_tombstone`) | `data/ingredients/mapped/Bacto_Soytone.yaml` (`FOODON:03315720`), `data/ingredients/mapped/Mgcl2x_6_H2o.yaml` (`CHEBI:86345`) |
| **I5** | Ineligible (`AMBIGUOUS`) | `mapping_status=AMBIGUOUS` (`NOT_ELIGIBLE_RECORD`) | `1` | `excluded` (`ambiguous_identity`) | `data/ingredients/mapped/PYGS.yaml` (`MICRO:0000604`) |
| **I6** | Ineligible (`MAPPED` + `NAMED_MEDIUM`) | `mapping_status=MAPPED`, `ingredient_type=NAMED_MEDIUM` (`NOT_ELIGIBLE_RECORD`; CultureMech owns medium recipes) | `26` | `not_applicable` | `data/ingredients/mapped/Bg-11_Medium.yaml` (`ENVO:00002030`) |
| **I7** | Ineligible (`MAPPED` + `PLACEHOLDER` quality) | `mapping_status=MAPPED`, `ontology_mapping.mapping_quality=PLACEHOLDER` (`NOT_ELIGIBLE_RECORD`) | `54` | `excluded` (`placeholder_grounding`) | `data/ingredients/mapped/Aburamycin_A.yaml` (`kgmicrobe.compound:aburamycin_a`) |
| **I8** | Ineligible (`MAPPED` in duplicate-identifier baseline) | `mapping_status=MAPPED`, identifier shared across >1 non-rejected record in `mappings/duplicate_identifier_baseline.tsv` (`15` identifier groups) | `35` | `excluded` (`duplicate_identifier_baseline`, `#218` / `#226` / `#924`) | `data/ingredients/mapped/Na2hpo4_X_12_H2o.yaml` (`CHEBI:34683`), `data/ingredients/mapped/Beef_Extract.yaml` (`NCIT:C896`) |
| **Subtotal (Ineligible / Excluded)** | **Fails Rule A2 Identity Gate** | **`NOT_ELIGIBLE_RECORD`** | **`457`** | **`excluded` / `not_applicable`** | — |
| **E1** | Eligible — Role & External Locator Ready | Passes Rule A2; has $\ge 1$ typed role assignment; every assigned role has external locator-backed evidence (`DATABASE_ENTRY`, `PEER_REVIEWED_PUBLICATION`, or `TECHNICAL_REPORT`) | `248` | `checked` + `blocked` (blocked only on Steps 3–7 gate/snapshot/writer prerequisites, `#925`) | `data/ingredients/mapped/Na2moo4_X_2_H2o.yaml` (`CHEBI:75213`), `data/ingredients/mapped/Feso4_X_7_H2o.yaml` (`CHEBI:75836`) |
| **E2a** | Eligible — Role Assigned, Computational/Non-External Role Citation | Passes Rule A2; has $\ge 1$ typed role assignment, but $\ge 1$ role is backed only by `COMPUTATIONAL_PREDICTION` without an external DOI/PMID/URL locator | `569` | `checked` + `evidence-limited` (needs external role citation) + `blocked` (`#925`) | `data/ingredients/mapped/Biotin.yaml` (`CHEBI:15956`), `data/ingredients/mapped/L-glutamate.yaml` (`CHEBI:16015`) |
| **E2b** | Eligible — Role Assigned, Empty Role Evidence List | Passes Rule A2; has $\ge 1$ typed role assignment, and $\ge 1$ assigned role has `evidence: []` | `11` | `checked` + `evidence-limited` (needs role evidence item) + `blocked` (`#925`) | `data/ingredients/mapped/Na2so4.yaml` (`CHEBI:32149`, secondary `MINERAL_SOURCE` role has `evidence: []`) |
| **E3** | Eligible — Missing Typed Role Assignment (`0` roles on record) | Passes Rule A2; currently has `0` entries across `nutritional_roles`, `physicochemical_roles`, and `cellular_metabolic_roles` (would fail Rule B3 `EXPLAINS_ROLE_NOT_ON_RECORD` unless a `ROLES` graph is preceded by role curation or uses `graph_kind=SPECIATION`) | `1,668` | `checked` + `evidence-limited` (needs role curation or `SPECIATION` decomposition first) + `blocked` (`#925`) | `data/ingredients/mapped/Na2s2o3.yaml` (`CHEBI:132112`), `data/ingredients/mapped/ATCC_Wolfes_Mineral_Mix.yaml` (`kgmicrobe.ingredient:atcc_wolfes_mineral_mix`) |
| **Subtotal (Eligible under Rule A2)** | **Passes Rule A2 Identity Gate** | **All `2,496` eligible records audited** | **`2,496`** | **`checked` + `blocked` / `evidence-limited`** | — |
| **Total Corpus** | **All YAML files in `data/ingredients/{mapped,unmapped}`** | **`457 + 2,496 = 2,953`** | **`2,953`** | **`100%` accounted for** | — |

### 4.2 Breakdown of the `2,496` Rule A2-Eligible Records

1. **By `ingredient_type` (`2,496` records):**
   - `SINGLE_INGREDIENT`: `2,037` (`81.61%`)
   - `None` (legacy untyped mapped records): `227` (`9.09%`)
   - `STOCK_SOLUTION`: `119` (`4.77%`)
   - `UNDEFINED_MIXTURE`: `113` (`4.53%`)
2. **By `ontology_mapping.ontology_source` (`2,496` records):**
   - `CHEBI`: `1,971` (`78.97%`)
   - `kgmicrobe.ingredient`: `129` (`5.17%`)
   - `MESH`: `92` (`3.69%`)
   - `CAS`: `79` (`3.17%`)
   - `NCIT`: `75` (`3.00%`)
   - `MICRO`: `59` (`2.36%`)
   - `FOODON`: `46` (`1.84%`)
   - `kgmicrobe.compound`: `23` (`0.92%`)
   - `ENVO`: `17` (`0.68%`)
   - `UBERON`: `4` (`0.16%`)
   - `BTO`: `1` (`0.04%`)
3. **By `ontology_mapping.mapping_quality` (`2,496` records):**
   - `EXACT_MATCH`: `1,543` (`61.82%`)
   - `CAS_RN_LOOKUP`: `250` (`10.02%`)
   - `FALLBACK_REGISTRY`: `229` (`9.17%`)
   - `SYNONYM_MATCH`: `196` (`7.85%`)
   - `NARROW_MATCH`: `151` (`6.05%`)
   - `CLOSE_MATCH`: `110` (`4.41%`)
   - `LEXICAL_MATCH`: `15` (`0.60%`)
   - `MANUAL_CURATION`: `1` (`0.04%`)
   - `BROAD_MATCH`: `1` (`0.04%`)
4. **By Structural Decomposition Slots (`2,496` records):**
   - Carrying `components` (`StockComponent` partonomy, eligible for `COMPONENT` bridge edges with `RECORD_COMPONENT` basis): `59` records (`24` additional records with `components` lie in the `457` ineligible slice, totaling `83` decomposed records corpus-wide).
   - Carrying `supplied_form`: `7` eligible records.
5. **By Assigned Role Slot Distribution (`828` of `2,496` eligible records carry $\ge 1$ role):**
   - `nutritional_roles` only: `593` records
   - `physicochemical_roles` only: `226` records
   - `cellular_metabolic_roles` only: `8` records (`data/ingredients/mapped/L-glutamate.yaml`, `L-proline.yaml`, `Glycine_Betaine.yaml`, `Trehalose.yaml`, `Sucrose.yaml`, `Glycerol.yaml`, `D-sorbitol.yaml`, `Ectoine.yaml`)
   - Both `nutritional_roles` and `physicochemical_roles`: `1` record (`data/ingredients/mapped/Trace_Vitamins.yaml`)
   - Total with $\ge 1$ role: `828` (`248` Cohort E1 + `569` Cohort E2a + `11` Cohort E2b).

---

## 5. Top-25 Readiness Ranking (`scripts/score_causal_graph_readiness.py`)

Running `.venv/bin/python scripts/score_causal_graph_readiness.py --ingredients-dir data/ingredients --duplicate-baseline mappings/duplicate_identifier_baseline.tsv --limit 25 --out /tmp/cg_readiness.tsv` produces the highest-priority Cohort E1 records ready for causal-graph authoring as soon as Steps 3–5 of `docs/CAUSAL_GRAPH_CONTRACT.md` land:

| Rank | Record Path | Identifier | Preferred Term | `ingredient_type` | `mapping_quality` | Total Score | ID | Spec | Role | Evid | Usage | Occurrences | Roles | Ext Role Citations | Issues |
|---:|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | `data/ingredients/mapped/Na2so4.yaml` | `CHEBI:32149` | `Na2SO4` | `SINGLE_INGREDIENT` | `EXACT_MATCH` | `93.0` | 30 | 20 | 15 | 13 | 15.0 | 1,422 | 2 | 1 | `role_without_external_source` (2nd role `MINERAL_SOURCE` has `evidence: []`) |
| 2 | `data/ingredients/mapped/Feso4_X_7_H2o.yaml` | `CHEBI:75836` | `FeSO4 x 7 H2O` | `SINGLE_INGREDIENT` | `EXACT_MATCH` | `90.0` | 30 | 20 | 15 | 10 | 15.0 | 4,347 | 1 | 1 | — |
| 3 | `data/ingredients/mapped/H3bo3.yaml` | `CHEBI:33118` | `H3BO3` | `SINGLE_INGREDIENT` | `EXACT_MATCH` | `90.0` | 30 | 20 | 15 | 10 | 15.0 | 3,893 | 1 | 1 | — |
| 4 | `data/ingredients/mapped/Mncl2_X_4_H2o.yaml` | `CHEBI:86368` | `MnCl2 x 4 H2O` | `SINGLE_INGREDIENT` | `EXACT_MATCH` | `90.0` | 30 | 20 | 15 | 10 | 15.0 | 3,521 | 1 | 1 | — |
| 5 | `data/ingredients/mapped/Cocl2_X_6_H2o.yaml` | `CHEBI:35696` | `CoCl2 x 6 H2O` | `SINGLE_INGREDIENT` | `EXACT_MATCH` | `90.0` | 30 | 20 | 15 | 10 | 15.0 | 3,471 | 1 | 1 | — |
| 6 | `data/ingredients/mapped/Znso4_X_7_H2o.yaml` | `CHEBI:32312` | `ZnSO4 x 7 H2O` | `SINGLE_INGREDIENT` | `EXACT_MATCH` | `90.0` | 30 | 20 | 15 | 10 | 15.0 | 3,441 | 1 | 1 | — |
| 7 | `data/ingredients/mapped/Na2moo4_X_2_H2o.yaml` | `CHEBI:75213` | `Na2MoO4 x 2 H2O` | `SINGLE_INGREDIENT` | `EXACT_MATCH` | `90.0` | 30 | 20 | 15 | 10 | 15.0 | 3,310 | 1 | 1 | — |
| 8 | `data/ingredients/mapped/Cucl2_X_2_H2o.yaml` | `CHEBI:86318` | `CuCl2 x 2 H2O` | `SINGLE_INGREDIENT` | `EXACT_MATCH` | `90.0` | 30 | 20 | 15 | 10 | 15.0 | 2,469 | 1 | 1 | — |
| 9 | `data/ingredients/mapped/Nicl2_X_6_H2o.yaml` | `CHEBI:53542` | `NiCl2 x 6 H2O` | `SINGLE_INGREDIENT` | `EXACT_MATCH` | `90.0` | 30 | 20 | 15 | 10 | 15.0 | 2,402 | 1 | 1 | — |
| 10 | `data/ingredients/mapped/K2hpo4.yaml` | `CHEBI:32031` | `K2HPO4` | `SINGLE_INGREDIENT` | `EXACT_MATCH` | `90.0` | 30 | 20 | 15 | 10 | 15.0 | 2,218 | 1 | 1 | — |
| 11 | `data/ingredients/mapped/Nanhco3.yaml` | `CHEBI:32139` | `NaHCO3` | `SINGLE_INGREDIENT` | `EXACT_MATCH` | `90.0` | 30 | 20 | 15 | 10 | 15.0 | 2,175 | 1 | 1 | — |
| 12 | `data/ingredients/mapped/D-glucose.yaml` | `CHEBI:17634` | `D-Glucose` | `SINGLE_INGREDIENT` | `EXACT_MATCH` | `90.0` | 30 | 20 | 15 | 10 | 15.0 | 2,146 | 2 | 1 | `role_without_external_source` (`ENERGY_SOURCE` is `COMPUTATIONAL_PREDICTION`) |
| 13 | `data/ingredients/mapped/Nh4cl.yaml` | `CHEBI:31206` | `NH4Cl` | `SINGLE_INGREDIENT` | `EXACT_MATCH` | `90.0` | 30 | 20 | 15 | 10 | 15.0 | 2,142 | 1 | 1 | — |
| 14 | `data/ingredients/mapped/Kh2po4.yaml` | `CHEBI:63036` | `KH2PO4` | `SINGLE_INGREDIENT` | `EXACT_MATCH` | `90.0` | 30 | 20 | 15 | 10 | 15.0 | 2,135 | 1 | 1 | — |
| 15 | `data/ingredients/mapped/Cacl2_X_2_H2o.yaml` | `CHEBI:86158` | `CaCl2 x 2 H2O` | `SINGLE_INGREDIENT` | `EXACT_MATCH` | `90.0` | 30 | 20 | 15 | 10 | 15.0 | 1,923 | 1 | 1 | — |
| 16 | `data/ingredients/mapped/Cuso4_X_5_H2o.yaml` | `CHEBI:31440` | `CuSO4 x 5 H2O` | `SINGLE_INGREDIENT` | `EXACT_MATCH` | `90.0` | 30 | 20 | 15 | 10 | 15.0 | 1,196 | 1 | 1 | — |
| 17 | `data/ingredients/mapped/Glucose.yaml` | `CHEBI:17234` | `Glucose` | `SINGLE_INGREDIENT` | `EXACT_MATCH` | `90.0` | 30 | 20 | 15 | 10 | 15.0 | 1,111 | 1 | 1 | — |
| 18 | `data/ingredients/mapped/Na2-edta.yaml` | `CHEBI:64734` | `Na2-EDTA` | `SINGLE_INGREDIENT` | `EXACT_MATCH` | `90.0` | 30 | 20 | 15 | 10 | 15.0 | 1,093 | 1 | 1 | — |
| 19 | `data/ingredients/mapped/Resazurin.yaml` | `CHEBI:8806` | `Resazurin` | `SINGLE_INGREDIENT` | `EXACT_MATCH` | `90.0` | 30 | 20 | 15 | 10 | 15.0 | 1,053 | 1 | 1 | — |
| 20 | `data/ingredients/mapped/Fecl2_X_4_H2o.yaml` | `CHEBI:86249` | `FeCl2 x 4 H2O` | `SINGLE_INGREDIENT` | `EXACT_MATCH` | `90.0` | 30 | 20 | 15 | 10 | 15.0 | 909 | 1 | 1 | — |
| 21 | `data/ingredients/mapped/L-cysteine_Hcl_X_H2o.yaml` | `CHEBI:91249` | `L-Cysteine HCl x H2O` | `SINGLE_INGREDIENT` | `EXACT_MATCH` | `90.0` | 30 | 20 | 15 | 10 | 15.0 | 886 | 1 | 1 | — |
| 22 | `data/ingredients/mapped/Na2s_X_9_H2o.yaml` | `CHEBI:86360` | `Na2S x 9 H2O` | `SINGLE_INGREDIENT` | `EXACT_MATCH` | `90.0` | 30 | 20 | 15 | 10 | 15.0 | 853 | 1 | 1 | — |
| 23 | `data/ingredients/mapped/Mgcl2_X_6_H2o.yaml` | `CHEBI:86345` | `MgCl2 x 6 H2O` | `SINGLE_INGREDIENT` | `EXACT_MATCH` | `90.0` | 30 | 20 | 15 | 10 | 15.0 | 762 | 1 | 1 | — |
| 24 | `data/ingredients/mapped/Kcl.yaml` | `CHEBI:32588` | `KCl` | `SINGLE_INGREDIENT` | `EXACT_MATCH` | `90.0` | 30 | 20 | 15 | 10 | 15.0 | 741 | 1 | 1 | — |
| 25 | `data/ingredients/mapped/zncl2.yaml` | `CHEBI:49976` | `ZnCl2` | `SINGLE_INGREDIENT` | `EXACT_MATCH` | `90.0` | 30 | 20 | 15 | 10 | 15.0 | 709 | 1 | 1 | — |

---

## 6. Source-Grounded Claim Review & Proposed Native Mechanism / Protein-Example Candidate Table

To verify that `docs/CAUSAL_GRAPH_CONTRACT.md` and `MAPPING_SEMANTICS.md` Section 7 cover the real representation needs of the MediaIngredientMech corpus without schema drift, 12 candidate records were audited in detail across all 7 `MIM.vocab:chemical_bridge_kind` values (`HYDRATE_PART`, `ION_PART`, `PROTONATION`, `STRUCTURAL_FORM`, `GENERIC_SPECIALISATION`, `FORM_OF_PARENT`, `COMPONENT`) and both `MIM.vocab:graph_kind` values (`ROLES`, `SPECIATION`):

| # | Record Path & File SHA-256 | Record Identifier & Preferred Term | `graph_kind` & `explains` Role(s) | Chemical-Speciation Bridge Chain (`predicate` / `bridge_kind` / `bridge_basis` / `stoichiometry`) | Biological / Cross-Mech Target Node(s) & Edge(s) | Candidate `ProteinExample` (`id`, `label`, `organism_id`, `organism`) | Source Locators & Scope (`EvidenceItem`) | Disposition & Prerequisite Blockers |
|---:|---|---|---|---|---|---|---|---|
| 1 | `data/ingredients/mapped/Na2moo4_X_2_H2o.yaml`<br>`sha256: d8ecba6c664d94d9d0f0da89410808b99c3d6ad4cfeb55f122b5df2d7d8b5612` | `CHEBI:75213`<br>`Na2MoO4 x 2 H2O` | `ROLES`<br>explains: `[TRACE_ELEMENT]` | 1. `CHEBI:75213` → `CHEBI:75215` (`disodium molybdate`): `BFO:0000051`, `HYDRATE_PART`, `CHEMICAL_STRUCTURE`, stoich `1`<br>2. `CHEBI:75215` → `CHEBI:36264` (`molybdate`): `BFO:0000051`, `ION_PART`, `CHEMICAL_STRUCTURE`, stoich `1` | `CHEBI:36264` → `GO:0015412` (`ABC-type molybdate transporter activity`, `EC:7.3.2.5`, `TCDB:3.A.1.8.1`) via `RO:0002327` / `RO:0000056`; → `CHEBI:25373` (`molybdenum cofactor`) → `MIM.vocab:TRACE_ELEMENT` via `MIM.vocab:supports_media_role` | `id: UniProtKB:P09833`<br>`label: Molybdate-binding periplasmic protein ModA`<br>`organism_id: NCBITaxon:83333`<br>`organism: Escherichia coli K-12` | Role evidence on record: `CHEBI:75213` (`DATABASE_ENTRY`). Biological edge sources: `PMID:9352922` / `DOI:10.1111/j.1365-2958.1997.mmi532.x` (ModABC molybdate uptake); `UniProtKB:P09833` (`reviewed`). | `checked` + `blocked`<br>Planned Step 5 Canary in `docs/CAUSAL_GRAPH_CONTRACT.md` §12; blocked on `mappings/ontology_facts.tsv`, `just qc-causal-graphs`, and validated writer (`#925`). |
| 2 | `data/ingredients/mapped/Na2so4.yaml`<br>`sha256: a58a2bf0cb953270beb578b442267e856098cc72abb3470742c6f6a50b5e2e81` | `CHEBI:32149`<br>`Na2SO4` | `ROLES`<br>explains: `[SULFUR_SOURCE, MINERAL_SOURCE]` | 1. `CHEBI:32149` → `CHEBI:16189` (`sulfate`): `BFO:0000051`, `ION_PART`, `CHEMICAL_STRUCTURE`, stoich `1`<br>2. `CHEBI:32149` → `CHEBI:29101` (`sodium(1+)`): `BFO:0000051`, `ION_PART`, `CHEMICAL_STRUCTURE`, stoich `2` | `CHEBI:16189` → `traitmech:000001` (`assimilatory sulfate reduction`) via `RO:0000056` → `MIM.vocab:SULFUR_SOURCE` via `MIM.vocab:supports_media_role`; `CHEBI:29101` → `MIM.vocab:MINERAL_SOURCE` via `MIM.vocab:supports_media_role` | `id: UniProtKB:P16700`<br>`label: Sulfate-binding protein Sbp`<br>`organism_id: NCBITaxon:83333`<br>`organism: Escherichia coli K-12` | Role evidence on record: `SULFUR_SOURCE` cites `DOI:10.1099/00207713-33-2-438`; `MINERAL_SOURCE` currently has `evidence: []`. Contract worked example in `docs/CAUSAL_GRAPH_CONTRACT.md` §8. | `checked` + `evidence-limited` + `blocked`<br>Secondary role `MINERAL_SOURCE` needs locator-backed `EvidenceItem` before `explains: [SULFUR_SOURCE, MINERAL_SOURCE]` is promoted; blocked on `mappings/ontology_facts.tsv`, `mappings/cross_mech_references.tsv`, `just qc-causal-graphs` (`#925`). |
| 3 | `data/ingredients/mapped/Feso4_X_7_H2o.yaml`<br>`sha256: becd0250e47dc561b10ebceb0d366018bd4790156c055cd299489f0cb034f172` | `CHEBI:75836`<br>`FeSO4 x 7 H2O` | `ROLES`<br>explains: `[IRON_SOURCE]` | 1. `CHEBI:75836` → `CHEBI:75832` (`iron(2+) sulfate (anhydrous)`): `BFO:0000051`, `HYDRATE_PART`, `CHEMICAL_STRUCTURE`, stoich `1`<br>2. `CHEBI:75832` → `CHEBI:29033` (`iron(2+)`): `BFO:0000051`, `ION_PART`, `CHEMICAL_STRUCTURE`, stoich `1` | `CHEBI:29033` → `TCDB:9.A.8` (`Ferrous Iron Uptake (FeoB) Family`, `PANTHER:PTHR43185`, `GO:0015093`) via `RO:0000056` → `MIM.vocab:IRON_SOURCE` via `MIM.vocab:supports_media_role` | `id: UniProtKB:P33650`<br>`label: Ferrous iron transport protein B (FeoB)`<br>`organism_id: NCBITaxon:83333`<br>`organism: Escherichia coli K-12` | Role evidence on record: `CHEBI:75836` (`DATABASE_ENTRY`). Biological edge sources: `PMID:8387141` / `DOI:10.1128/jb.175.10.3218-3222.1993` (`feoAB` ferrous iron uptake); `UniProtKB:P33650`. | `checked` + `blocked`<br>Blocked on `mappings/ontology_facts.tsv`, `just qc-causal-graphs`, and validated writer (`#925`). |
| 4 | `data/ingredients/mapped/D-glucose.yaml`<br>`sha256: dd603850555b5735acd54dcc6f4695a23a0d789b120d77000db239427bad0914` | `CHEBI:17634`<br>`D-Glucose` | `ROLES`<br>explains: `[CARBON_SOURCE]` | `CHEBI:17634` (`D-glucose`) → `CHEBI:4167` (`D-glucopyranose`): `RO:0002351` (`has member` / inverse `rdfs:subClassOf`), `STRUCTURAL_FORM`, `ONTOLOGY_ASSERTED` | `CHEBI:4167` → `EC:2.7.1.199` (`protein-Npi-phosphohistidine-D-glucose phosphotransferase`, `GO:0008982`) via `RO:0000056` → `MIM.vocab:CARBON_SOURCE` via `MIM.vocab:supports_media_role` | `id: UniProtKB:P69786`<br>`label: PTS system glucose-specific EIICB component (PtsG)`<br>`organism_id: NCBITaxon:83333`<br>`organism: Escherichia coli K-12` | Role evidence on record: `CARBON_SOURCE` cites `CHEBI:17634` (`DATABASE_ENTRY`); `ENERGY_SOURCE` is `COMPUTATIONAL_PREDICTION`. Biological edge sources: `PMID:11160082` / `DOI:10.1074/jbc.M009482200`; `UniProtKB:P69786`. | `checked` + `evidence-limited` (on secondary role `ENERGY_SOURCE`) + `blocked`<br>Blocked on `mappings/ontology_facts.tsv` (`ONTOLOGY_ASSERTED` `rdfs:subClassOf` check) and `just qc-causal-graphs` (`#925`). |
| 5 | `data/ingredients/mapped/Glucose.yaml`<br>`sha256: 5a3fea70783e1f7ae2676807615116972b687afcddb3c65ed98b5a8f16ea39cb` | `CHEBI:17234`<br>`Glucose` | `ROLES`<br>explains: `[CARBON_SOURCE]` | Direct molecular/class anchor (`CHEBI:17234` is the root `CausalNode`; no bridge edge required when the downstream `TraitMech` node consumes `CHEBI:17234` directly per `docs/CAUSAL_GRAPH_CONTRACT.md` §3.2) | `CHEBI:17234` → `traitmech:000026` (`lactic acid fermentation`) via `RO:0000056` (`participates in`) → `MIM.vocab:CARBON_SOURCE` via `MIM.vocab:supports_media_role` | `id: UniProtKB:P00338`<br>`label: L-lactate dehydrogenase (Ldh)`<br>`organism_id: NCBITaxon:1582`<br>`organism: Lactobacillus delbrueckii subsp. bulgaricus` | Role evidence on record: `CHEBI:17234` (`DATABASE_ENTRY`). Cross-Mech reference: `TraitMech` `traitmech:000026` (`docs/CAUSAL_GRAPH_CONTRACT.md` §3.2). | `checked` + `blocked`<br>Blocked on `conf/sibling_pins.yaml`, `mappings/cross_mech_references.tsv`, `mappings/cross_mech_assertions.jsonl`, and `just qc-causal-graphs` (`#925`). |
| 6 | `data/ingredients/mapped/Biotin.yaml`<br>`sha256: 26056efadc5e57f081cde6e4ce0c2e25c03530c6d564ef0df25da3bcacb59c30` | `CHEBI:15956`<br>`Biotin` | `ROLES`<br>explains: `[VITAMIN_SOURCE]` | `CHEBI:15956` (`biotin`) → `CHEBI:57586` (`biotin(1-)`): `RO:0002434` / ChEBI `is_conjugate_acid_of`, `PROTONATION`, `ONTOLOGY_ASSERTED` | `CHEBI:57586` → `EC:6.3.4.15` (`biotin--[acetyl-CoA-carboxylase] ligase`, `GO:0004077`) via `MIM.vocab:satisfies_cofactor_requirement` → `MIM.vocab:VITAMIN_SOURCE` via `MIM.vocab:supports_media_role` | `id: UniProtKB:P06709`<br>`label: Bifunctional ligase/repressor BirA`<br>`organism_id: NCBITaxon:83333`<br>`organism: Escherichia coli K-12` | Role evidence on record: `COMPUTATIONAL_PREDICTION` only (no external locator yet). Biological edge sources: `PMID:8576049` / `DOI:10.1074/jbc.271.4.2121`; `UniProtKB:P06709`. | `checked` + `evidence-limited` + `blocked`<br>Role `VITAMIN_SOURCE` needs locator-backed `EvidenceItem` upgrade; blocked on `mappings/ontology_facts.tsv` (`is_conjugate_acid_of`) and `just qc-causal-graphs` (`#925`). |
| 7 | `data/ingredients/mapped/Vitamin_B12.yaml`<br>`sha256: 9ee0b669c9ef90950273ea3755e02d960efbfdef7252c13edf180bd70b3fad6c` | `CHEBI:176843`<br>`Vitamin B12` | `ROLES`<br>explains: `[VITAMIN_SOURCE]` | `CHEBI:176843` (`vitamin B12`) → `CHEBI:17439` (`cyanocob(III)alamin`) or `CHEBI:140785` (`R-cob(III)alamin`): `RO:0002351`, `GENERIC_SPECIALISATION`, `ONTOLOGY_ASSERTED` (`rdfs:subClassOf+` in ChEBI) | `CHEBI:140785` → `EC:7.6.2.8` (`ABC-type vitamin B12 transporter`, `GO:0015420`, `TCDB:3.A.1.13.1`) via `RO:0000056` → `MIM.vocab:VITAMIN_SOURCE` via `MIM.vocab:supports_media_role` | `id: UniProtKB:P06609`<br>`label: Vitamin B12-binding protein BtuF`<br>`organism_id: NCBITaxon:83333`<br>`organism: Escherichia coli K-12` | Role evidence on record: `COMPUTATIONAL_PREDICTION` only. Biological edge sources: `PMID:12016218` / `DOI:10.1126/science.1070870` (BtuCD-BtuF structure/mechanism); `UniProtKB:P06609`. | `checked` + `evidence-limited` + `blocked`<br>Role `VITAMIN_SOURCE` needs locator-backed `EvidenceItem` upgrade; blocked on `mappings/ontology_facts.tsv` (`rdfs:subClassOf+`) and `just qc-causal-graphs` (`#925`). |
| 8 | `data/ingredients/mapped/Na2s2o3_X_5_H2o.yaml`<br>`sha256: 9f44114f08227176ff8d8981123a2943407ef1585543287c6e66b1914b0090dd` | `CHEBI:32150`<br>`Na2S2O3 x 5 H2O` | `SPECIATION` (delegating to `CHEBI:132112` `Na2s2o3.yaml` or `CHEBI:26977` `Thiosulfate.yaml`) or `ROLES` (`[ELECTRON_DONOR]`) | 1. `CHEBI:32150` → `CHEBI:132112` (`sodium thiosulfate` anhydrous, `Na2s2o3.yaml`): `BFO:0000051`, `HYDRATE_PART`, `CHEMICAL_STRUCTURE`, stoich `1`<br>2. `CHEBI:132112` → `CHEBI:26977` (`thiosulfate(2-)`, `Thiosulfate.yaml`): `BFO:0000051`, `ION_PART`, `CHEMICAL_STRUCTURE`, stoich `1` | For `ROLES`: `CHEBI:26977` → `GO:0019417` (`sulfur oxidation` / Sox multienzyme complex) via `RO:0000056` → `MIM.vocab:ELECTRON_DONOR` via `MIM.vocab:supports_media_role` | `id: UniProtKB:O32167`<br>`label: L-cysteine S-thiosulfotransferase SoxA`<br>`organism_id: NCBITaxon:34090`<br>`organism: Paracoccus pantotrophus` | Role evidence on record: `PMID:27565613` (`DOI:10.1128/AEM.02111-16`, `PEER_REVIEWED_PUBLICATION`). Biological edge sources: `PMID:11470376` / `DOI:10.1128/AEM.67.7.2873-2882.2001`; `UniProtKB:O32167`. | `excluded` (`duplicate_identifier_baseline`, `#218` / `#924`) + `blocked` (`#925`)<br>`CHEBI:32150` is currently in `mappings/duplicate_identifier_baseline.tsv` (`HYDRATE_FAMILY_UNREVIEWED`, shared with `Na2s2o3_X_5_H2o_2.yaml`); must resolve duplicate identifier before Rule A2 passes, and `SPECIATION` target `Thiosulfate.yaml` must carry a `ROLES` graph (`SPECIATION_TARGET_HAS_NO_ROLES_GRAPH`). |
| 9 | `data/ingredients/mapped/Nitrous_Oxide.yaml`<br>`sha256: 1d11386343ebe50b5f2504359b14ae0818b092f532d99768e1a897143b513932` | `CHEBI:17045`<br>`nitrous oxide` | `ROLES`<br>explains: `[ELECTRON_ACCEPTOR]` | Direct molecular anchor (`CHEBI:17045` is the root `CausalNode`; no chemical bridge needed because `CHEBI:17045` is directly the substrate of `EC:1.7.2.4`) | `CHEBI:17045` → `EC:1.7.2.4` (`nitrous-oxide reductase`, `GO:0050304`) via `RO:0000056` → `MIM.vocab:ELECTRON_ACCEPTOR` via `MIM.vocab:supports_media_role` | `id: UniProtKB:Q51480`<br>`label: Nitrous-oxide reductase NosZ`<br>`organism_id: NCBITaxon:287`<br>`organism: Pseudomonas aeruginosa` | Role evidence on record: `PMID:27084012` (`DOI:10.1128/AEM.00409-16`, `PEER_REVIEWED_PUBLICATION`). Biological edge source: `PMID:27084012`; `UniProtKB:Q51480`. | `checked` + `blocked`<br>Passes Rule A2 and Rule B3 (`Cohort E1`); blocked only on `just qc-causal-graphs` and validated writer (`#925`). |
| 10 | `data/ingredients/mapped/Tetrachloroethene.yaml`<br>`sha256: b8e43c00cd45e09f72e7e496b1cc606e1d64e44ce559fa34a1ee7a6781f07a82` | `CHEBI:17300`<br>`Tetrachloroethene` | `ROLES`<br>explains: `[ELECTRON_ACCEPTOR]` | Direct molecular anchor (`CHEBI:17300` is the root `CausalNode`; directly reduced by `EC:1.21.99.5`) | `CHEBI:17300` → `EC:1.21.99.5` (`tetrachloroethene reductive dehalogenase`, `GO:0018862`) via `RO:0000056` → `MIM.vocab:ELECTRON_ACCEPTOR` via `MIM.vocab:supports_media_role` | `id: UniProtKB:Q9F9W6`<br>`label: Tetrachloroethene reductive dehalogenase PceA`<br>`organism_id: NCBITaxon:146891`<br>`organism: Sulfurospirillum multivorans` | Role evidence on record: `PMID:10388710` (`DOI:10.1128/AEM.65.7.3108-3113.1999`, `PEER_REVIEWED_PUBLICATION`). Biological edge source: `PMID:10388710`; `UniProtKB:Q9F9W6`. | `checked` + `blocked`<br>Passes Rule A2 and Rule B3 (`Cohort E1`); blocked only on `just qc-causal-graphs` and validated writer (`#925`). |
| 11 | `data/ingredients/mapped/2-Hydroxybutyric_Acid_Sodium_Salt.yaml`<br>`sha256: 8a2c69adcb8c2dff48034d0fdb7c5b271f64da8c03fa4bee355cd70ad9957173` | `cas:5094-24-6`<br>`2-Hydroxybutyric acid sodium salt` | `ROLES`<br>explains: `[CARBON_SOURCE]` | `cas:5094-24-6` (`2-Hydroxybutyric acid sodium salt`) → `CHEBI:1148` (`2-hydroxybutyric acid`): `RO:0002434` / `skos:broadMatch`, `FORM_OF_PARENT`, `RECORD_SSSOM` (verified in `mappings/ingredient_mappings.sssom.tsv`: `cas:5094-24-6` `skos:broadMatch` `CHEBI:1148`) | `CHEBI:1148` → `EC:1.1.1.27` (`L-lactate / 2-hydroxybutyrate dehydrogenase`) via `RO:0000056` → `MIM.vocab:CARBON_SOURCE` via `MIM.vocab:supports_media_role` | `id: UniProtKB:P52643`<br>`label: D-lactate dehydrogenase LdhA`<br>`organism_id: NCBITaxon:83333`<br>`organism: Escherichia coli K-12` | Role evidence on record: currently `0` roles (`Cohort E3`). SSSOM grounding row: `cas:5094-24-6` `skos:broadMatch` `CHEBI:1148` (`FALLBACK_REGISTRY`). *(Contrast: `Sodium_Perchlorate_Monohydrate.yaml`, `cas:7791-07-3`, uses `skos:closeMatch CHEBI:132103` per `#342` and is rejected by `FORM_OF_PARENT`'s `skos:broadMatch`-only rule.)* | `checked` + `evidence-limited` + `blocked`<br>Needs `CARBON_SOURCE` role added to record first (`EXPLAINS_ROLE_NOT_ON_RECORD`); blocked on `just qc-causal-graphs` and writer (`#925`). |
| 12 | `data/ingredients/mapped/ATCC_Wolfes_Mineral_Mix.yaml`<br>`sha256: d1a3c0cd0b18a8df04ba988240ea929afbff4c94b0bad76ea348c12c9129ebf4` | `kgmicrobe.ingredient:atcc_wolfes_mineral_mix`<br>`ATCC Wolfe's mineral mix` | `SPECIATION`<br>explains: `[]` (delegates to constituent records per `docs/CAUSAL_GRAPH_CONTRACT.md` §4.1 & §5) | `kgmicrobe.ingredient:atcc_wolfes_mineral_mix` → 13 `components` (`CHEBI:4735` nitrilotriacetic acid, `CHEBI:31795` `MgSO4 x 7 H2O`, `CHEBI:86364` `MnSO4 x H2O`, `CHEBI:26710` `NaCl`, `CHEBI:75836` `FeSO4 x 7 H2O`, `CHEBI:35696` `CoCl2 x 6 H2O`, `CHEBI:86158` `CaCl2 x 2 H2O`, `CHEBI:32312` `ZnSO4 x 7 H2O`, `CHEBI:31440` `CuSO4 x 5 H2O`, `CHEBI:86124` `AlK(SO4)2 x 12 H2O`, `CHEBI:33118` `H3BO3`, `CHEBI:75213` `Na2MoO4 x 2 H2O`, `CHEBI:53542` `NiCl2 x 6 H2O`): `BFO:0000051`, `COMPONENT`, `RECORD_COMPONENT` | Delegates biological mechanisms to constituent `SINGLE_INGREDIENT` records (`FeSO4 x 7 H2O`, `Na2MoO4 x 2 H2O`, `CoCl2 x 6 H2O`, etc.) via `graph_kind=SPECIATION` | Constituent protein examples live on the target `ROLES` records (`UniProtKB:P09833` on `Na2moo4_X_2_H2o.yaml`, `UniProtKB:P33650` on `Feso4_X_7_H2o.yaml`) per Rule B2 (`SPECIATION` graphs have no biological edges) | Record `components` carry `ComponentAssertion` provenance (`PMID:3360536` / ATCC Medium 1045 Wolfe's mineral solution). | `checked` + `blocked`<br>Under Rule B2 (`SPECIATION_TARGET_HAS_NO_ROLES_GRAPH`), a `SPECIATION` graph can only be written after at least one constituent record carries a `ROLES` graph; blocked on `#925`. |

---

## 7. Blocker Matrix and Issue/Task Traceability

| Blocker Category | Rule Code(s) (`docs/CAUSAL_GRAPH_CONTRACT.md` §9) | Affected Record Count | Root Cause | Tracked Issue / Task | Required Remediation |
|---|---|---:|---|---|---|
| **Unimplemented QC Gate, Snapshots, and Writer** | `SNAPSHOT_PIN_DRIFT`, `UNPINNED_EXTERNAL_ASSERTION`, `CROSS_MECH_REF_UNINDEXED`, `CROSS_MECH_ASSERTION_DRIFT`, `SPECIATION_FACT_NOT_FOUND`, `ONTOLOGY_BRIDGE_NOT_IN_SNAPSHOT` | `2,496` (all Rule A2-eligible records) | Steps 3–7 of `docs/CAUSAL_GRAPH_CONTRACT.md` (`conf/sibling_pins.yaml`, `mappings/cross_mech_references.tsv`, `mappings/cross_mech_assertions.jsonl`, `mappings/ontology_facts.tsv`, `mappings/cross_mech_links.tsv`, `just qc-causal-graphs`, and the validated graph writer) are not yet implemented. | `INFRA_TASKS.md` `INFRA-006` / GitHub issue `#925` (`#266`, `#219`) | Implement `just qc-causal-graphs` (`--offline` / `--online`), build pinned snapshots from `conf/sibling_pins.yaml`, and land the one-record `Na2moo4_X_2_H2o.yaml` canary. |
| **Missing Typed Role Assignments on Eligible Records** | `EXPLAINS_ROLE_NOT_ON_RECORD`, `EMPTY_EXPLAINS_ON_ROLES_GRAPH` | `1,668` (Cohort E3) | Records pass Rule A2 identity checks (`MAPPED`, non-`NAMED_MEDIUM`, non-`PLACEHOLDER`, non-duplicate), but have `0` assigned roles across `nutritional_roles`, `physicochemical_roles`, and `cellular_metabolic_roles`. | `.claude/skills/ingredient-roles/SKILL.md` / `.claude/skills/curate-yaml-record/SKILL.md` | Curate evidence-backed role assignments on the record before adding a `ROLES` graph (or use `graph_kind=SPECIATION` for stock solutions/hydrates whose constituent/ion record carries the `ROLES` graph). |
| **Role Assignments Lacking External Locator Citations** | Readiness penalty (`role_without_external_source`); Rule C1 (`EVIDENCE_MISSING_PROVENANCE` if reused on graph edges) | `580` (`569` Cohort E2a + `11` Cohort E2b) | Assigned roles rely solely on `COMPUTATIONAL_PREDICTION` without DOI/PMID/URL locators (`569` records) or have `evidence: []` (`11` records, including `Na2so4.yaml`'s `MINERAL_SOURCE`). | `.claude/skills/curate-yaml-record/SKILL.md` | Upgrade role `EvidenceItem` entries with locator-backed `PEER_REVIEWED_PUBLICATION`, `DATABASE_ENTRY`, or `TECHNICAL_REPORT` citations alongside causal-graph authoring. |
| **Duplicate-Identifier Baseline Families** | `NOT_ELIGIBLE_RECORD` (Rule A2 clause 4) | `35` mapped records (`+ 2` rejected records = `37` total in `15` identifier groups) | Shared primary `identifier` across multiple mapped records in `mappings/duplicate_identifier_baseline.tsv`. | `INFRA_TASKS.md` `INFRA-005` / GitHub issues `#924`, `#218`, `#226` | Resolve each duplicate-identifier family (`MERGE_SAME_SUBSTANCE`, `NEEDS_OWN_ID`, `HYDRATE_FAMILY_UNREVIEWED`) via mapped-to-mapped merge or regrounding before authoring causal graphs on those records. |
| **Placeholder Grounding on Mapped Records** | `NOT_ELIGIBLE_RECORD` (Rule A2 clause 3) | `54` (`Cohort I7`) | `ontology_mapping.mapping_quality: PLACEHOLDER` (`kgmicrobe.compound:*` / `kgmicrobe.ingredient:*` placeholders). | `INFRA_TASKS.md` `INFRA-002` / GitHub issue `#921` (`#246`) | Promote placeholder groundings to verified ChEBI/CAS/FoodOn terms or curated `FALLBACK_REGISTRY` / `MANUAL_CURATION` quality before causal-graph eligibility. |
| **SSSOM `skos:closeMatch` vs `skos:broadMatch` on Hydrate-on-Anhydrous Registry Fallbacks** | `FORM_OF_PARENT_NOT_IN_SSSOM` (Rule B1) | `1` verified exemplar (`Sodium_Perchlorate_Monohydrate.yaml`, `cas:7791-07-3`) | `FORM_OF_PARENT` requires `predicate_id == skos:broadMatch` in `mappings/ingredient_mappings.sssom.tsv`, whereas hydrate-on-anhydrous registry fallbacks use `skos:closeMatch` per `#342`. | GitHub issue `#342` / `docs/CAUSAL_GRAPH_CONTRACT.md` §4.2 | Keep `FORM_OF_PARENT` restricted to `skos:broadMatch` parent rows (such as `2-Hydroxybutyric_Acid_Sodium_Salt.yaml`, `cas:5094-24-6`), or reground hydrate records to a ChEBI hydrate term (`HYDRATE_PART`) when ChEBI adds the hydrate. |
