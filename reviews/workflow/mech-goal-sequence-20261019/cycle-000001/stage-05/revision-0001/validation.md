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
3. **`reports/ingredient_bundle_20260924/review.json`** (`sha256: 45f17b9365c90238599bfa4309ce8ad98c8267d83a02ed5164f48efac7829713`):
   - Updated `base_review_sha256` to `6c74c7cc3eb8075ec18e20ab594a9b5eae9910b08b98c9d0746b3374af6c7ac6`.
4. **`reports/semantic_review_20260921/resolution/current-review.json`**:
   - Updated `inputs["reports/sssom_completion_20260921/mapping_changes/review-record-issues-20261003.json"]` and `inputs["reports/sssom_completion_20260921/review.json"]` to match the synchronized SHA-256 digests.

---

## 2. Linked Fresh Review Evidence & Immutable Report Preservation

- **Saved successor structured review bundle**:
  - `reviews/structured/20261021T120500Z-ca-no32-x-4-h2o/review.yaml`
  - `reviews/structured/20261021T120500Z-ca-no32-x-4-h2o/review.md`
  - Saved via `.venv/bin/python scripts/record_review.py save` and validated via `.venv/bin/python scripts/record_review.py validate reviews/structured/20261021T120500Z-ca-no32-x-4-h2o/review.yaml` (`{"valid_reviews": 1}`).
  - Links `previous_reviews: ["reviews/structured/20261017T083000Z-ca-no32-x-4-h2o/review.yaml"]` and records `rec-f-5b1b1ab939d20218` with `disposition: resolved`.
- **Immutable original reports preserved byte-for-byte**:
  - `reviews/structured/20261017T083000Z-ca-no32-x-4-h2o/review.yaml` (`c9a899907d5de8e89e7481bc611c8a50499825d9a5543e0ccdc29855a454df4c`)
  - `reviews/structured/20261017T083000Z-2-d-lyxose/review.yaml` (`8cb55264f72c38f8246bc295610a6ab2db422a2a8c28d79b1cf7068757d7b6de`)
  - `reviews/structured/20261017T083000Z-mapped-cohort-20261017/review.yaml` (`a3a830da2080fc7b5b15149c1a15880b977bb2062473f206f4e657be67a29612`)
  - `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/evidence.yaml` (`4d81bb6763c9c382558ddc6a9180d127349ee8f6ab3d9459989bbe29c2d71045`)

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
   - `PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/src /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/python -m kg_microbe_workflows.cli validate-evidence reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-05/revision-0001/evidence.yaml --root . --previous reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/evidence.yaml` -> `PASS`
