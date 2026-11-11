# Cycle 19 Stage 3 (`protein_examples`) Validation Report

- **Run ID:** `mech-goal-sequence-20261019`
- **Cycle / Stage:** Cycle `19`, Stage `3` (`protein_examples`, Revision `1`)
- **Goal ID:** `MECH-WORKFLOW-4a12831b8d1770095c511808`
- **Repository:** `CultureBotAI/MediaIngredientMech` (`repository_key: mediaingredientmech`)
- **Base Commit Audited:** `c79fbc41c0bc4014c68696ab941143db1a027919` (`origin/main`)
- **Records Modified:** `0` (`data/ingredients/**/*.yaml`, `data/curated/*.yaml`, and `mappings/ingredient_mappings.sssom.tsv` untouched because `docs/CAUSAL_GRAPH_CONTRACT.md` Steps 3 and 5 prerequisites remain `planned`)

---

## 1. Workflow Profile, Schema, and Evidence Index Validation

1. **Workflow profile validation (`kg_microbe_workflows validate`):**
   - **Command:**
     ```bash
     env PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/src \
       /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/python \
       -m kg_microbe_workflows validate \
       --profile workflow/mech-workflow.yaml \
       --parent /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/src/kg_microbe_workflows/templates/mech-cycle-v1.yaml \
       --schema /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/src/kg_microbe_workflows/schema/workflow-v1.yaml \
       --repository-key mediaingredientmech --json
     ```
   - **Result:** Passed (`exit code 0`).
   - **Verified Digests:**
     - `parent_sha256`: `32d499de747333e42ed45d40940bfa06c60f85710814155e0fad5f7c4d2fee82`
     - `profile_sha256` (`workflow/mech-workflow.yaml`): `45d7c23d67f490cea6b31e336e5d2ac98b7ce8fa4e791bd9d3be092cfdb5a10d`
     - `schema_sha256`: `66194b3aba4540e9ee7adf91bc1fd7fb597aede130ef1603031a92002152e1d8`
     - `workflow_sha256` (`effective-workflow.json`): `7c320cc21b5f9d88f99208f0344a4bb533fdc96f17020fd091690a780e75b2b6`
2. **Verified closure index synchronization (`reviews/workflow/latest.yaml`):**
   - **Check:** Compared `reviews/workflow/latest.yaml` against `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/workspace/session-orchestration/20261019/mediaingredientmech/verified-evidence-index.json`.
   - **Result:** Exact match (`54` verified stage entries through Cycle 18 Stage 6 PR `#1351`; Cycle 19 Stage 1 PR `#1353` and Cycle 19 Stage 2 PR `#1355` have `required_outputs: []` and therefore do not add `goal_evidence` entries to `verified-evidence-index.json`).

---

## 2. Repository Test Suite and Gate Checks Executed

| Check / Gate | Command Executed | Exit Code | Summary of Verified Output |
|---|---|---:|---|
| Causal-graph & `ProteinExample` schema, readiness, skill frontmatter, and review-route unit tests | `.venv/bin/python -m pytest --no-cov -p no:cacheprovider -q tests/test_causal_graph_schema.py tests/test_score_causal_graph_readiness.py tests/test_skill_frontmatter.py tests/test_record_review_routes.py` | `0` | `178 passed in 3.56s` (`39` in `test_causal_graph_schema.py` covering the 21 closed-schema rule cases and fleet graph parity including `ProteinExample`; `27` in `test_score_causal_graph_readiness.py`; `53` in `test_skill_frontmatter.py`; `59` in `test_record_review_routes.py`). |
| In-memory `ProteinExample` closed-schema positive & negative validation | `.venv/bin/python -c '... validate_ingredient(rec, target_class="IngredientRecord", schema_path=SCHEMA_PATH) ...'` | `0` | Valid `ProteinExample` (`UniProtKB:P69786` `PtsG` in `NCBITaxon:83333` on `MOLECULAR_FUNCTION` node `EC:2.7.1.199` on `D-glucose.yaml`) produced `0` errors; all `6` negative mutations (`UniProtKB:P69786-2` isoform suffix, unprefixed `taxon_id`, invalid `entry_status`, non-ISO `retrieved_on`, empty `evidence: []`, and `UniProtKB:P69786` in `CausalNode.grounding`) were rejected with `1` error each. |
| Strict closed-schema validation across all YAML instances | `.venv/bin/python scripts/validate_strict.py` | `0` | `files scanned: 2963` (`2,681` mapped + `275` unmapped + `7` curated collections), `files with ERROR: 0`, `total ERROR rows: 0`. |
| Instruction reference check | `.venv/bin/python scripts/check_instruction_refs.py` | `0` | `Scanned 54 agent-instruction file(s) against 88 recipes. OK: every referenced recipe, path, and Python CLI option exists.` |
| Vendored claw artifact sync check | `.venv/bin/python scripts/check_vendored_sync.py` | `0` | `OK: 26 governed artifacts match the pinned claw revision` |
| Component partonomy QC | `.venv/bin/python scripts/validate_component_partonomy.py` | `0` | `component partonomy: 2956 records, 83 decompositions, 502 components, 0 violation(s)` |
| SSSOM invariant validation | `.venv/bin/python scripts/validate_sssom_invariants.py` | `0` | `OK: ingredient_mappings.sssom.tsv passed Rules A, B1, B2, B3, B5, C, D, E, F, G, H, I, J, K, L. mappings/needs_curator_review.tsv written with header only.` |
| Duplicate identifier baseline check | `.venv/bin/python scripts/audit_duplicate_identifiers.py --check` | `0` | `15 identifier(s) held by more than one record (35 records, 20 excess) ... OK: duplicate identifiers match the tracked baseline exactly.` |

---

## 3. Input and Artifact Digests Verified

| File Path | Role | SHA-256 Digest |
|---|---|---|
| `src/mediaingredientmech/schema/mediaingredientmech.yaml` | LinkML schema (`CausalGraph`, `CausalNode`, `ProteinExample`) | `bb43dee29b21fdee72a48022456e733e49e95824c4c09674f9b3165c290fe012` |
| `docs/CAUSAL_GRAPH_CONTRACT.md` | Normative causal-graph and `ProteinExample` contract | `de889fdea9ad18e6cf3502461d779e76ef6e99f923e374b0a5309fe163871d65` |
| `MAPPING_SEMANTICS.md` | Identity, bridge, and genome-firewall contract (§7) | `6b52f2ac48109ddd5d81996a136b19776cab55efa69a5ec832cf716d6885a062` |
| `.claude/skills/add-uniprot-protein-examples/SKILL.md` | Stage 3 (`protein_examples`) skill definition | `8ef4e475fe3d0f72c658c4577143467d554de0545cd0b90dc52fd4fdc64de2c4` |
| `src/mediaingredientmech/validation/write_validated.py` | Closed-schema write-time validator | `6763083be385b38dceb911f13dbd9575aea0dc42425204ccc43360f93c0dcbc9` |
| `scripts/score_causal_graph_readiness.py` | Readiness scorer and `IDENTITY_GATE` classifier | `32411c33b4c7f10fd1753bfa245872b455ee14293075b76469cdafc713169354` |
| `tests/test_causal_graph_schema.py` | 21 closed-schema rule cases & fleet graph parity tests | `38b0d02b048ce069bb03d6e3e3475894ed8121d152ea4a7b6211123a82df14f3` |
| `mappings/duplicate_identifier_baseline.tsv` | Tracked shared-identifier dispositions | `723f613de746bf44b38e19be9786cd1ee7fb719256fbc6195b8b1e20477d5720` |
| `INFRA_TASKS.md` | Infrastructure task notebook | `dda5707f52661e91f46d96fcbabfc256ac39d4cc865a28a3e5ab6f0536958a5e` |
| `reviews/workflow/latest.yaml` | Tracked verified closure index (`54` entries) | `7b837a3c7b6b3ae5e2fc5aef1e9e09b9501fa41f191402b112cbc0db1ce18a29` |
| `data/ingredients/mapped/Na2moo4_X_2_H2o.yaml` | Priority candidate #1 (`UniProtKB:P09833` `ModA`, Step 5 canary) | `d8ecba6c664d94d9d0f0da89410808b99c3d6ad4cfeb55f122b5df2d7d8b5612` |
| `data/ingredients/mapped/Na2so4.yaml` | Priority candidate #2 (`UniProtKB:P0AAK4`, `P21156`, `P23845`) | `a58a2bf0cb953270beb578b442267e856098cc72abb3470742c6f6a50b5e2e81` |
| `data/ingredients/mapped/Feso4_X_7_H2o.yaml` | Priority candidate #3 (`UniProtKB:P33650` `FeoB`) | `becd0250e47dc561b10ebceb0d366018bd4790156c055cd299489f0cb034f172` |
| `data/ingredients/mapped/Biotin.yaml` | Priority candidate #4 (`UniProtKB:O31652` `BioY`, `P06709` `BirA`) | `26056efadc5e57f081cde6e4ce0c2e25c03530c6d564ef0df25da3bcacb59c30` |
| `data/ingredients/mapped/Thiamine_Hcl.yaml` | Priority candidate #5 (`UniProtKB:P31550` `ThiB`, `P75949` `ThiL`) | `8e7d3802dc19872e85d753b6c7a0e1fb34c552311e69c450e697d9f1e55b2732` |
| `data/ingredients/mapped/Pyridoxine_Hydrochloride.yaml` | Priority candidate #6 (`UniProtKB:P40191` `PdxK`) | `26ea82b1c3e173c0695085ce08a4143db32a702dae3295702d60a61e944d0a40` |
| `data/ingredients/mapped/D-glucose.yaml` | Priority candidate #7 (`UniProtKB:P69786` `PtsG`) | `dd603850555b5735acd54dcc6f4695a23a0d789b120d77000db239427bad0914` |
| `data/ingredients/mapped/Thiosulfate.yaml` | Priority candidate #8 (`UniProtKB:Q8KC91` `SoxB`) | `2a7055e92068a39ea08e4e758cb7e09f9fa6e6678457b0873c60993f207f4713` |
| `data/ingredients/mapped/Nitrate.yaml` | Priority candidate #9 (`UniProtKB:P09152` `NarG`, `P42433` `NasC`) | `f51fcdc1e9784fe5cc27805cf868ef10a1af1c683a2828776a80f01f2cca6e2c` |
| `data/ingredients/mapped/Ammonium.yaml` | Priority candidate #10 (`UniProtKB:P69681` `AmtB`, `P0A9C5` `GlnA`) | `b31c98cdd0fcc6f15cd6004839b327258499fc37a5b3b506773920c42d0da49c` |
| `data/ingredients/mapped/Rifampicin.yaml` | Priority candidate #11 (`UniProtKB:P0A8V2` `RpoB`) | `b599ba097d626617fed33af7c58f1c66998af0df19d1a52781d628d2311356dc` |
| `data/ingredients/mapped/Ampicillin.yaml` | Priority candidate #12 (`UniProtKB:P0AD68` `FtsI`/`PBP3`) | `41b4b2f941c10fd8123b15831f9f9522507f3a7a4305b42b4207e6f308cd50d4` |
| `data/ingredients/mapped/Khco3.yaml` | Priority candidate #13 (`UniProtKB:Q55460` `CmpA` + abiotic `BUFFER`) | `09e05ed22bebdd41792345d0e3cd3bf3fbaf2a1d7b6b6f8be3ee41b6a95e5fc5` |
| `data/ingredients/mapped/Uracil.yaml` | Priority candidate #14 (`UniProtKB:P0A8F0` `Upp`) | `aa1282ae9e8737fa46ae6a24682f90ea29ff40a4251cc7b7fcca3122273ff516` |
| `data/ingredients/mapped/Na2s2o3_X_5_H2o.yaml` | Priority candidate #15 (`SPECIATION` delegation control) | `9f44114f08227176ff8d8981123a2943407ef1585543287c6e66b1914b0090dd` |
| `data/ingredients/mapped/Resazurin.yaml` | Priority candidate #16 (`MEDIUM_CONDITIONING` abiotic control) | `b7aee64c3b58a3c1c0f2bb01c7a75e035dbd9a7e036828872a5513b5b5bac59a` |
