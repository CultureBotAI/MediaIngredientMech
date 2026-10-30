# Stage 05 Validation Report — `mech-goal-sequence-20261019` (Cycle 8)

- **Repository**: `mediaingredientmech` (`CultureBotAI/MediaIngredientMech`)
- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `8` (`cycle-000008`)
- **Stage**: `5` (`resolve_review_findings`)
- **Revision**: `1` (`revision-0001`)
- **Source Revision**: `1a5df87cf66a510c0b1586cad64af9133ae80ddb`
- **Scope Frozen At**: `2026-10-30T13:45:00Z`
- **Consumed Stage 04 Evidence**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000008/stage-04/revision-0001/evidence.yaml` (`sha256: 9fd485a1c19d85af0fc002f36f20c67db5fc312674aea5b1efd9a75f45fbcfd9`)

---

## 1. Tracked Review Index Synchronization (`reviews/workflow/latest.yaml`)

- Synchronized `reviews/workflow/latest.yaml` (`sha256: 2a784d8ab55d90684ca00e62e3387ea8ca13c0562be786ea09517838b922a034`) from `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/workspace/session-orchestration/20261019/mediaingredientmech/verified-evidence-index.json` (`22` verified entries: Cycle 1 Stage 4 `#919`, Cycle 1 Stage 5 `#924`, Cycle 1 Stage 6 `#926`, Cycle 2 Stage 4 `#930`, Cycle 2 Stage 5 `#932`, Cycle 2 Stage 6 `#934`, Cycle 3 Stage 4 `#938`, Cycle 3 Stage 5 `#939`, Cycle 3 Stage 6 `#940`, Cycle 4 Stage 4 `#944`, Cycle 4 Stage 5 `#945`, Cycle 4 Stage 6 `#946`, Cycle 5 Stage 4 `#950`, Cycle 5 Stage 5 `#951`, Cycle 5 Stage 6 `#952`, Cycle 6 Stage 4 `#956`, Cycle 6 Stage 5 `#958`, Cycle 6 Stage 6 `#959`, Cycle 7 Stage 4 `#970`, Cycle 7 Stage 5 `#972`, Cycle 7 Stage 6 `#973`, and Cycle 8 Stage 4 `#977`).

---

## 2. Exact-Byte Approval & Immutable Report Preservation Verification

1. **Exact-byte approval verification (`src/mediaingredientmech/record_refresh.py`)**:
   - Verified `data/ingredients/mapped/(2)-D-lyxose.yaml` (`mim-c01-s04-f001` / `#921`) retains `owner_record_sha256: 62258c9bdabaf8728fafb6923345fe4b24b9956069113896acb16e9631c1451e` in `reports/sssom_completion_20260921/mapping_review/nonmapping_cohorts.json` (`source_position: 3`) and `reports/semantic_review_20260921/resolution/current-review.json`.
   - Verified all `19/19` mapped records in `mim-c01-s04-f003` (`#923`) are byte-bound in `reports/sssom_completion_20260921/review.json["record_inputs"]` (`17` `SUPPORTED` + `2` `WITHHOLD`, with `5` also byte-bound in `reports/sssom_completion_20260921/mapping_review/nonmapping_cohorts.json`) and `reports/semantic_review_20260921/resolution/current-review.json["record_inputs"]`.
2. **Immutable original reports preserved byte-for-byte**:
   - `reviews/structured/20261017T083000Z-ca-no32-x-4-h2o/review.yaml` (`sha256: 685871f022aed7b10ef4d572f484d10f57d221d3e2740a852ece2ef495822ed0`)
   - `reviews/structured/20261021T120500Z-ca-no32-x-4-h2o/review.yaml` (`sha256: a1a264dfa12a87b84d85db52f15a71a792023253d6a1210d58b3dbf3ea469a67`)
   - `reviews/structured/20261017T083000Z-2-d-lyxose/review.yaml` (`sha256: 43cb260ab57440b35965233904389179b7155251c04b0d3b9649d2daf113a61c`)
   - `reviews/workflow/mech-goal-sequence-20261019/cycle-000008/stage-04/revision-0001/evidence.yaml` (`sha256: 9fd485a1c19d85af0fc002f36f20c67db5fc312674aea5b1efd9a75f45fbcfd9`)
   - `reviews/workflow/mech-goal-sequence-20261019/cycle-000008/stage-04/revision-0001/review_findings.md` (`sha256: 368e5b022ac501454ce2b9b01425c48eb5294c23bdf3427a74dd9b5e6d4bdc00`)
   - `reviews/workflow/mech-goal-sequence-20261019/cycle-000008/stage-04/revision-0001/review_report.md` (`sha256: 68229f00d1f53f2921ad34472c3ef9c3d887ed2d9738342c4f7f076f22f43332`)
   - `reviews/workflow/mech-goal-sequence-20261019/cycle-000008/stage-04/revision-0001/coverage_report.md` (`sha256: d72b1a258d246518058cad40594131865bd25c6abf6917f157b4780e7e715dac`)

---

## 3. Validation Commands and Results

1. **Structured Record Review Bundle Gate**:
   - `.venv/bin/python scripts/record_review.py --repo-root . check` -> `{"valid_reviews": 976}` (`PASS`)
2. **Reviewed SSSOM Assembly & Schema Gate**:
   - `PYTHONPATH=src .venv/bin/python reports/sssom_completion_20260921/assemble_review.py --check` -> `{"mapping_rows": 2987, "dispositions": {"SUPPORTED": 1741, "WITHHOLD": 1246}, "reproduced": true}` (`PASS`)
   - `PYTHONPATH=src .venv/bin/python -m mediaingredientmech.export.reviewed_sssom --root . --review reports/sssom_completion_20260921/review.json --output /tmp/mim-reviewed-sssom-c8s5` -> `{"semantic_status": "PASS_SUPPORTED_SUBSET", "counts": {"source": 2987, "supported": 1741, "withhold": 1246}}` (`PASS`)
   - `PYTHONPATH=src .venv/bin/python scripts/validate_reviewed_sssom_schema.py /tmp/mim-reviewed-sssom-c8s5` -> `{"status": "PASS"}` (`PASS`)
3. **Instruction Contract & Record Refresh Unit Tests**:
   - `.venv/bin/python scripts/check_instruction_refs.py` -> `PASS`
   - `PYTHONPATH=src .venv/bin/python -m pytest -o addopts="" tests/test_record_review_routes.py tests/test_skill_frontmatter.py tests/test_record_review_contract.py tests/test_record_refresh.py -q` -> `149 passed` (`PASS`)
4. **Workflow Evidence Gate (`FindingGroupResolution`)**:
   - `PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/src .venv/bin/python -m kg_microbe_workflows validate-evidence --root . --previous reviews/workflow/mech-goal-sequence-20261019/cycle-000008/stage-04/revision-0001/evidence.yaml --required-output issue_map --required-output validation reviews/workflow/mech-goal-sequence-20261019/cycle-000008/stage-05/revision-0001/evidence.yaml` -> `PASS`
