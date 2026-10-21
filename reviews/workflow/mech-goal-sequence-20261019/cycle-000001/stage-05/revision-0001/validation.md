# Stage 05 Validation Report — `mech-goal-sequence-20261019` (Cycle 1)

- **Repository**: `mediaingredientmech` (`CultureBotAI/MediaIngredientMech`)
- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `1`
- **Stage**: `5` (`resolve_review_findings`)
- **Revision**: `1`
- **Consumed Stage 04 Evidence**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/evidence.yaml` (`sha256: 4d81bb6763c9c382558ddc6a9180d127349ee8f6ab3d9459989bbe29c2d71045`)

---

## 1. Local Fix and Manifest Synchronization (`mim-c01-s04-f002` / `#922`)

1. **`reports/sssom_completion_20260921/mapping_changes/review-record-issues-20261003.json`** (`sha256: 9b578f6c25c1ebabb8e58c5a59d6188b7c1f2dd3c8c70ed021b35144c6da1226`):
   - Corrected `records[0].change` for `data/ingredients/mapped/Ca_No32_X_4_H2o.yaml` from `CHEBI:31348 (calcium dinitrate)` to `CHEBI:86159 (calcium nitrate tetrahydrate)` so the correction receipt matches both the stoichiometric tetrahydrate record and the canonical SSSOM mapping row (`mappings/ingredient_mappings.sssom.tsv` line 614).
2. **`reports/sssom_completion_20260921/review.json`** (`sha256: 6c74c7cc3eb8075ec18e20ab594a9b5eae9910b08b98c9d0746b3374af6c7ac6`):
   - Updated `inputs["reports/sssom_completion_20260921/mapping_changes/review-record-issues-20261003.json"]` to `9b578f6c25c1ebabb8e58c5a59d6188b7c1f2dd3c8c70ed021b35144c6da1226`.
3. **`reports/ingredient_bundle_20260924/review.json`** (`sha256: e0bdc20106e9db70acd72db49bc24a4394f802e3aa8ac1187d3cff7025937dc6`):
   - Updated `base_review_sha256` to `6c74c7cc3eb8075ec18e20ab594a9b5eae9910b08b98c9d0746b3374af6c7ac6`.
4. **`reports/semantic_review_20260921/resolution/current-review.json`** (`sha256: 1f0ea7040b5820263b135a3c7c0000157ebdece3370a8d9d60e37332926486d9`):
   - Updated `inputs["reports/sssom_completion_20260921/mapping_changes/review-record-issues-20261003.json"]`, `inputs["reports/sssom_completion_20260921/review.json"]`, and `inputs["output/mim-kgx-710-full/manifest.json"]` to match the synchronized SHA-256 digests.

---

## 2. Linked Fresh Review Evidence & Immutable Report Preservation

- **Saved successor structured review bundle**:
  - `reviews/structured/20261021T120500Z-ca-no32-x-4-h2o/review.yaml` (`sha256: a1a264dfa12a87b84d85db52f15a71a792023253d6a1210d58b3dbf3ea469a67`)
  - `reviews/structured/20261021T120500Z-ca-no32-x-4-h2o/review.md` (`sha256: be342ca1ad5fbaf05694712cfd89d7367b328e940122516ca246a62ddbb24d61`)
  - Validated via `PYTHONPATH=src .venv/bin/python scripts/record_review.py --repo-root /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech check` (`{"valid_reviews": 976}`).
  - Links predecessor review `reviews/structured/20261017T083000Z-ca-no32-x-4-h2o/review.yaml` via `source.inputs`, `evidence` (`ev-stage05-pred`), and `findings[0].previous_occurrences` (`review_id: 20261017T083000Z-ca-no32-x-4-h2o`, `finding_id: rec-f-5b1b1ab939d20218`) with `status: resolved`.
- **Immutable original reports preserved byte-for-byte**:
  - `reviews/structured/20261017T083000Z-ca-no32-x-4-h2o/review.yaml` (`685871f022aed7b10ef4d572f484d10f57d221d3e2740a852ece2ef495822ed0`)
  - `reviews/structured/20261017T083000Z-2-d-lyxose/review.yaml` (`43cb260ab57440b35965233904389179b7155251c04b0d3b9649d2daf113a61c`)
  - `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/evidence.yaml` (`4d81bb6763c9c382558ddc6a9180d127349ee8f6ab3d9459989bbe29c2d71045`)
  - `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/review_findings.md` (`926fb14a4a2cafdee331ed8ac7ac595c21fd0c5e6f5d3c12eed4ecb094b29420`)
  - `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/review_report.md` (`6397472ae5a4381df5f8befe0ab8b522c92970472a144eef6df17117f53a6609`)

---

## 3. Validation Commands and Results

1. **Reviewed SSSOM Assembly and Schema Check**:
   - `.venv/bin/python reports/sssom_completion_20260921/assemble_review.py --check` -> `{"mapping_rows": 2987, "dispositions": {"SUPPORTED": 1741, "WITHHOLD": 1246}, "reproduced": true}`
   - `PYTHONPATH=src .venv/bin/python -m mediaingredientmech.export.reviewed_sssom --root . --review reports/sssom_completion_20260921/review.json --output /tmp/mim-reviewed-sssom-test` -> `semantic_status: PASS_SUPPORTED_SUBSET`
   - `.venv/bin/python scripts/validate_reviewed_sssom_schema.py /tmp/mim-reviewed-sssom-test` -> `status: PASS` (`1741` supported rows, `1246` withheld rows)
2. **Ingredient Bundle Export Check**:
   - `PYTHONPATH=src .venv/bin/python -m mediaingredientmech.export.ingredient_bundle export --root . --review reports/ingredient_bundle_20260924/review.json --output /tmp/mim-ingredient-bundle-test` -> `{"identifiers": 18, "manifest_sha256": "45f17b9365c90238599bfa4309ce8ad98c8267d83a02ed5164f48efac7829713", "mappings": 20, "occurrences": 10, "products": 3}`
3. **Full KGX & Supported KGX Release Gate**:
   - `PYTHONPATH=src .venv/bin/python -m mediaingredientmech.export.supported_kgx --root . --report reports/semantic_review_20260921/resolution/current-review.json --output /tmp/mim-supported-kgx-new --validate-only` -> `PASS`
4. **Structured Record Review & Instruction Contract Gates**:
   - `.venv/bin/python scripts/record_review.py check` -> `PASS`
   - `.venv/bin/python scripts/check_instruction_refs.py` -> `PASS`
   - `.venv/bin/pytest tests/test_record_review_routes.py tests/test_skill_frontmatter.py tests/test_record_review_contract.py -q` -> `PASS`
5. **Workflow Evidence Gate**:
   - `PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/src /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/python -m kg_microbe_workflows validate-evidence reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-05/revision-0001/evidence.yaml --root . --previous reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/evidence.yaml` -> `PASS`
