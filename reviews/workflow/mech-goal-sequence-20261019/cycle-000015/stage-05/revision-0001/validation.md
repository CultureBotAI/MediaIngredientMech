# Stage 05 Validation Report — `mech-goal-sequence-20261019` (Cycle 15)

- **Repository**: `mediaingredientmech` (`CultureBotAI/MediaIngredientMech`)
- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `15` (`cycle-000015`)
- **Stage**: `5` (`resolve_review_findings`)
- **Revision**: `1` (`revision-0001`)
- **Source Revision**: `f956c9b43fb286d49abb9a500f57011cbdf117b0`
- **Scope Frozen At**: `2026-11-09T05:52:35Z`
- **Consumed Stage 04 Evidence**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000015/stage-04/revision-0001/evidence.yaml` (`sha256: 2e0e5905f2a976ed7201b13f5700862fdbcecab15c8af1a4bda94911a3c42f8c`)

---

## 1. Tracked Review Index Synchronization (`reviews/workflow/latest.yaml`)

- Synchronized `reviews/workflow/latest.yaml` (`sha256: 8bedbee7b2a802a938b7ec56b09caee0aa8aca54548edbc7e9d16a9f84ab1169`) from `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/workspace/session-orchestration/20261019/mediaingredientmech/verified-evidence-index.json` (`43` verified entries: Cycle 1 Stage 4 `#919`, Cycle 1 Stage 5 `#924`, Cycle 1 Stage 6 `#926`, Cycle 2 Stage 4 `#930`, Cycle 2 Stage 5 `#932`, Cycle 2 Stage 6 `#934`, Cycle 3 Stage 4 `#938`, Cycle 3 Stage 5 `#939`, Cycle 3 Stage 6 `#940`, Cycle 4 Stage 4 `#944`, Cycle 4 Stage 5 `#945`, Cycle 4 Stage 6 `#946`, Cycle 5 Stage 4 `#950`, Cycle 5 Stage 5 `#951`, Cycle 5 Stage 6 `#952`, Cycle 6 Stage 4 `#956`, Cycle 6 Stage 5 `#958`, Cycle 6 Stage 6 `#959`, Cycle 7 Stage 4 `#970`, Cycle 7 Stage 5 `#972`, Cycle 7 Stage 6 `#973`, Cycle 8 Stage 4 `#977`, Cycle 8 Stage 5 `#978`, Cycle 8 Stage 6 `#979`, Cycle 9 Stage 4 `#983`, Cycle 9 Stage 5 `#984`, Cycle 9 Stage 6 `#985`, Cycle 10 Stage 4 `#989`, Cycle 10 Stage 5 `#990`, Cycle 10 Stage 6 `#991`, Cycle 11 Stage 4 `#995`, Cycle 11 Stage 5 `#996`, Cycle 11 Stage 6 `#997`, Cycle 12 Stage 4 `#1002`, Cycle 12 Stage 5 `#1011`, Cycle 12 Stage 6 `#1024`, Cycle 13 Stage 4 `#1127`, Cycle 13 Stage 5 `#1129`, Cycle 13 Stage 6 `#1135`, Cycle 14 Stage 4 `#1141`, Cycle 14 Stage 5 `#1142`, Cycle 14 Stage 6 `#1143`, and Cycle 15 Stage 4 `#1283`).

---

## 2. Exact-Byte Approval & Immutable Report Preservation Verification

1. **Exact-byte approval verification (`src/mediaingredientmech/record_refresh.py`)**:
   - Verified `data/ingredients/mapped/(2)-D-lyxose.yaml` (`mim-c01-s04-f001` / `#921`) retains `owner_record_sha256: 62258c9bdabaf8728fafb6923345fe4b24b9956069113896acb16e9631c1451e` in `reports/sssom_completion_20260921/mapping_review/nonmapping_cohorts.json` (`source_position: 3`) and `reports/semantic_review_20260921/resolution/current-review.json`.
   - Verified all `19/19` mapped records in `mim-c01-s04-f003` (`#923`) are byte-bound in `reports/sssom_completion_20260921/review.json["record_inputs"]` (`17` `SUPPORTED` + `2` `WITHHOLD`, with `5` also byte-bound in `reports/sssom_completion_20260921/mapping_review/nonmapping_cohorts.json`) and `reports/semantic_review_20260921/resolution/current-review.json["record_inputs"]`.
2. **Immutable original reports preserved byte-for-byte**:
   - `reviews/structured/20261017T083000Z-ca-no32-x-4-h2o/review.yaml` (`sha256: 685871f022aed7b10ef4d572f484d10f57d221d3e2740a852ece2ef495822ed0`)
   - `reviews/structured/20261021T120500Z-ca-no32-x-4-h2o/review.yaml` (`sha256: a1a264dfa12a87b84d85db52f15a71a792023253d6a1210d58b3dbf3ea469a67`)
   - `reviews/structured/20261017T083000Z-2-d-lyxose/review.yaml` (`sha256: 43cb260ab57440b35965233904389179b7155251c04b0d3b9649d2daf113a61c`)
   - `reviews/workflow/mech-goal-sequence-20261019/cycle-000015/stage-04/revision-0001/evidence.yaml` (`sha256: 2e0e5905f2a976ed7201b13f5700862fdbcecab15c8af1a4bda94911a3c42f8c`)
   - `reviews/workflow/mech-goal-sequence-20261019/cycle-000015/stage-04/revision-0001/review_findings.md` (`sha256: 1793c015acb36a4785a505a6c8e7230ab6e8e12b63edff57652fa21e0dbe7817`)
   - `reviews/workflow/mech-goal-sequence-20261019/cycle-000015/stage-04/revision-0001/review_report.md` (`sha256: 11a1e9702b864ce10656a004fcd8e56c5b4940514893948621ab49111b5f6420`)
   - `reviews/workflow/mech-goal-sequence-20261019/cycle-000015/stage-04/revision-0001/coverage_report.md` (`sha256: ed2441a95979e0212c314e204c2c62e274856fc19b39072aa2fb83fba73f02f4`)
   - `reviews/workflow/mech-goal-sequence-20261019/cycle-000015/stage-04/revision-0001/validation.md` (`sha256: ee1da0dde88eb1bf6fc72768925e8b626cfdc73425671ce776ae86dd61957504`)

---

## 3. Validation Commands and Results

1. **Structured Record Review Bundle Gate**:
   - `.venv/bin/python scripts/record_review.py --repo-root . check` -> `{"valid_reviews": 1015}` (`PASS`)
2. **Reviewed SSSOM Assembly & Schema Gate**:
   - `PYTHONPATH=src .venv/bin/python reports/sssom_completion_20260921/assemble_review.py --check` -> `{"mapping_rows": 3014, "dispositions": {"SUPPORTED": 1739, "WITHHOLD": 1275}, "reproduced": true}` (`PASS`)
   - `PYTHONPATH=src .venv/bin/python -m mediaingredientmech.export.reviewed_sssom --root . --review reports/sssom_completion_20260921/review.json --output .temp/mim-reviewed-sssom-c15s5` -> `{"semantic_status": "PASS_SUPPORTED_SUBSET", "counts": {"source": 3014, "supported": 1739, "withhold": 1275}}` (`PASS`)
   - `PYTHONPATH=src .venv/bin/python scripts/validate_reviewed_sssom_schema.py .temp/mim-reviewed-sssom-c15s5` -> `{"status": "PASS"}` (`PASS`)
3. **Strict Schema, Partonomy, SSSOM Invariants, and Duplicate Identifier Gates**:
   - `.venv/bin/python scripts/validate_strict.py data/ingredients data/curated data/collections --out /dev/null` -> `2963` files scanned, `0` ERROR rows (`PASS`)
   - `.venv/bin/python scripts/validate_component_partonomy.py` -> `component partonomy: 2956 records, 83 decompositions, 502 components, 0 violation(s)` (`PASS`)
   - `.venv/bin/python scripts/validate_sssom_invariants.py --reject-tsv /dev/null` -> `OK: ingredient_mappings.sssom.tsv passed Rules A, B1, B2, B3, B5, C, D, E, F, G, H, I, J, K, L.` (`PASS`)
   - `.venv/bin/python scripts/audit_duplicate_identifiers.py --check` -> `15 identifier(s) held by more than one record (35 records, 20 excess); OK: duplicate identifiers match the tracked baseline exactly.` (`PASS`)
4. **Instruction Contract, Vendored Sync, and Record Refresh Unit Tests**:
   - `.venv/bin/python scripts/check_instruction_refs.py` -> `PASS`
   - `.venv/bin/python scripts/check_vendored_sync.py` -> `OK: 26 governed artifacts match the pinned claw revision` (`PASS`)
   - `PYTHONPATH=src .venv/bin/python -m pytest -o addopts="" tests/test_record_review_routes.py tests/test_skill_frontmatter.py tests/test_record_review_contract.py tests/test_record_refresh.py -q` -> `149 passed` (`PASS`)
5. **Workflow Evidence Gate (`FindingGroupResolution`)**:
   - `PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/src .venv/bin/python -m kg_microbe_workflows validate-evidence --root . --previous reviews/workflow/mech-goal-sequence-20261019/cycle-000015/stage-04/revision-0001/evidence.yaml --required-output issue_map --required-output validation reviews/workflow/mech-goal-sequence-20261019/cycle-000015/stage-05/revision-0001/evidence.yaml` -> `PASS`
