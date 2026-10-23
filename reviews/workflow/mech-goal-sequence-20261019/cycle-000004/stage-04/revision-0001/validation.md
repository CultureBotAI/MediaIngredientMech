# Cycle 4 Stage 4 Validation Report (`record_review`)

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `4` (`cycle-000004`)
- **Stage**: `4` (`stage-04` / `record_review`)
- **Revision**: `revision-0001`
- **Base Commit (`main`)**: `478e4b633b46e573808297b8e613efb6b5144725`

## 1. Local Validation Commands and Results

| Check | Command | Exit Code | Summary |
| --- | --- | --- | --- |
| Structured review bundle validation | `.venv/bin/python scripts/record_review.py check` | `0` | `valid_reviews: 976`, `coverage: "declared_scopes_only"`, `0` stale `source_sha256` digests, `0` schema or profile violations |
| Closed-schema LinkML validation | `.venv/bin/python scripts/validate_strict.py data/ingredients --out /tmp/strict_report_c4_s4.tsv` | `0` | `2953` files scanned (`2680` mapped + `273` unmapped), `0` ERROR rows, `5897` WARN rows (`curation_history` timestamp format) |
| Component partonomy validation | `.venv/bin/python scripts/validate_component_partonomy.py` | `0` | `2953` records, `83` records with `has_parts`, `502` total components, `0` partonomy violations |
| SSSOM invariant validation | `.venv/bin/python scripts/validate_sssom_invariants.py --reject-tsv /tmp/needs_curator_review_c4_s4.tsv` | `0` | `0` rejects (`OK: ingredient_mappings.sssom.tsv passed Rules A, B1, B2, B3, B5, C, D, E, F, G, H, I, J, K, L`) |
| Instruction and justfile reference check | `.venv/bin/python scripts/check_instruction_refs.py` | `0` | `52` instruction files checked against `88` justfile recipes (`0` errors) |
| Vendored governance sync check | `.venv/bin/python scripts/check_vendored_sync.py` | `0` | `24` governed artifacts match pinned claw revision (`0` drift) |
| Duplicate identifier audit | `.venv/bin/python scripts/audit_duplicate_identifiers.py --check` | `0` | `0` unexpected duplicate groups (`15` allowlisted salt/hydrate/catalog groups) |
| Unit tests for skills, review routes, and instruction refs | `.venv/bin/python -m pytest -o pythonpath=src -p no:cacheprovider --no-cov -q tests/test_skill_frontmatter.py tests/test_record_review_routes.py tests/test_check_instruction_refs.py` | `0` | `128 passed in 1.81s` |
| Workflow evidence validation | `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/python -m kg_microbe_workflows validate-evidence --root . --previous reviews/workflow/mech-goal-sequence-20261019/cycle-000003/stage-05/revision-0001/evidence.yaml --required-output review_report --required-output review_findings reviews/workflow/mech-goal-sequence-20261019/cycle-000004/stage-04/revision-0001/evidence.yaml` | `0` | Verified stage `record_review`, `carry_forward_ids` (`6` open findings from Cycle 3 Stage 5), artifacts, and SHA-256 digests |

## 2. Verified Input Digests

- `data/ingredients/**/*.yaml` (`2,953` files):
  - `sha256sum` manifest digest: `3b760eeec31525e7bdf8e45623ec53fb4ac521866d9ab5bafeea9160a4d2d99f`
  - `path:hash` manifest digest: `4a44101e2fb6199658c0fcced12a4cbd2f6624b60afd520a197e3049ccf502c7`
- `data/ingredients/mapped/*.yaml` (`2,680` files): `3cdce1d4d3ca11f92c6c96604bc57052ec841791e58f38ac5ea0070df33e61d8`
- `data/ingredients/unmapped/*.yaml` (`273` files): `c5b8261298412767b8ebdd953819c2891235d8bf397d51f7efd55a8efe43ed99`
- `reviews/structured/**/review.{yaml,md}` (`1,952` files across `976` bundles): `17c962c558829428cc5c6df8c8be66afa4791c20b781b60a846e6695d038bb6f`
- `data/curated/mapped_ingredients.yaml`: `4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b`
- `data/curated/unmapped_ingredients.yaml`: `8f574be094e741f1d59d55618cc14bf375304644732508bd7a5cd4a817c7fce2`
- `src/mediaingredientmech/schema/mediaingredientmech.yaml`: `bb43dee29b21fdee72a48022456e733e49e95824c4c09674f9b3165c290fe012`
- `schema/record_review.yaml`: `229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb`
- `INFRA_TASKS.md`: `dda5707f52661e91f46d96fcbabfc256ac39d4cc865a28a3e5ab6f0536958a5e`
- `reviews/workflow/latest.yaml`: `ceb9752cce067ead132443fac90e6ab2a27bd0fd8fd954c97b1dc2e8e2c4c0ed`
- `reviews/workflow/mech-goal-sequence-20261019/cycle-000003/stage-05/revision-0001/evidence.yaml`: `a23ce6760e8875543ebd580ba190a077063822cfda3a73c71193c11107d1fa3a`
