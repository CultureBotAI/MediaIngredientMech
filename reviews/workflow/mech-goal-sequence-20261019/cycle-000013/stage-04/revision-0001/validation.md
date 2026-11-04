# Cycle 13 Stage 4 Validation Report (`record_review`)

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `13` (`cycle-000013`)
- **Stage**: `4` (`stage-04` / `record_review`)
- **Revision**: `revision-0001`
- **Base Commit (`main`)**: `99fe4b44d78126d78041a69eeb366c52bedf0caa`

## 1. Local Validation Commands and Results

| Check | Command | Exit Code | Summary |
| --- | --- | --- | --- |
| Structured review bundle validation | `.venv/bin/python scripts/record_review.py check` | `0` | `valid_reviews: 986`, `coverage: "declared_scopes_only"`, `0` stale `source_sha256` digests, `0` schema or profile violations |
| Closed-schema LinkML validation | `.venv/bin/python scripts/validate_strict.py data/ingredients --out /tmp/strict_report_c13_s4.tsv` | `0` | `2955` files scanned (`2680` mapped + `275` unmapped), `0` ERROR rows (header-only report `/tmp/strict_report_c13_s4.tsv`) |
| Component partonomy validation | `.venv/bin/python scripts/validate_component_partonomy.py` | `0` | `2955` records, `83` decompositions, `502` components, `0` partonomy violations |
| SSSOM invariant validation | `.venv/bin/python scripts/validate_sssom_invariants.py --reject-tsv /tmp/needs_curator_review_c13_s4.tsv` | `0` | `0` rejects (`OK: ingredient_mappings.sssom.tsv passed Rules A, B1, B2, B3, B5, C, D, E, F, G, H, I, J, K, L`) |
| Instruction and justfile reference check | `.venv/bin/python scripts/check_instruction_refs.py` | `0` | `52` instruction files checked against `88` justfile recipes (`0` errors) |
| Vendored governance sync check | `.venv/bin/python scripts/check_vendored_sync.py` | `0` | `26` governed artifacts match pinned claw revision (`0` drift) |
| Duplicate identifier audit | `.venv/bin/python scripts/audit_duplicate_identifiers.py --check` | `0` | `0` unexpected duplicate groups (`15` allowlisted salt/hydrate/catalog groups across `35` records) |
| Unit tests for skills, review routes, causal graph schema/readiness, and instruction refs | `.venv/bin/python -m pytest -o pythonpath=src -p no:cacheprovider --no-cov -q tests/test_record_review_routes.py tests/test_skill_frontmatter.py tests/test_causal_graph_schema.py tests/test_score_causal_graph_readiness.py tests/test_check_instruction_refs.py` | `0` | `194 passed in 4.28s` |
| Workflow evidence validation | `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/python -m kg_microbe_workflows validate-evidence --root . --previous reviews/workflow/mech-goal-sequence-20261019/cycle-000012/stage-05/revision-0001/evidence.yaml --required-output review_report --required-output review_findings reviews/workflow/mech-goal-sequence-20261019/cycle-000013/stage-04/revision-0001/evidence.yaml` | `0` | Verified stage `record_review`, `carry_forward_ids` (`6` open findings from Cycle 12 Stage 5), artifacts, and SHA-256 digests |

## 2. Verified Input Digests

- `data/ingredients/**/*.yaml` (`2,955` files):
  - `sha256sum` manifest digest: `7e734ef21db8f041cfd6ab9bbbd939558db7422b85609b38547a04a9375f89be`
  - `path:hash` manifest digest: `150a23387c6906506617e054e91d46a266273d685f6ce55b3ce02d34e6efcc1a`
- `data/ingredients/mapped/*.yaml` (`2,680` files): `fe35b92f81cc507d1112cea6db7d080679145ea0914eb6fa340491a705663fc5`
- `data/ingredients/unmapped/*.yaml` (`275` files): `564f397b0c83d3147996ed648c465880a0c86869ec5c8a5170a55bc4ad787f3f`
- `reviews/structured/*/review.*` (`1,972` files across `986` bundles):
  - `LC_ALL=C sort` `sha256sum` manifest digest: `628a4a27e050aa06addc65d75b9af0a1669b6d800632db0aaae042f4ad5a801a`
  - `review.yaml`+`review.md` concat `sha256sum` manifest digest: `dce9b3370cdc727012ab25e8a72067cd19cf55871cd8928ad69d2e210d95f580`
- `data/curated/mapped_ingredients.yaml`: `2bc4b3663ea6beae04693bd517e2901ce69cf912d828599a0b1f7c19d2f8ba77`
- `data/curated/unmapped_ingredients.yaml`: `22ececf4e0e7a37ca0636d4635ed5408a6517ba7ef6e7a1daf713f09a7802cd8`
- `src/mediaingredientmech/schema/mediaingredientmech.yaml`: `bb43dee29b21fdee72a48022456e733e49e95824c4c09674f9b3165c290fe012`
- `schema/record_review.yaml`: `229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb`
- `INFRA_TASKS.md`: `dda5707f52661e91f46d96fcbabfc256ac39d4cc865a28a3e5ab6f0536958a5e`
- `reviews/workflow/latest.yaml`: `1c7c8912902d4ca266300691825ea83edd302284627d756c1d65c519318d2246`
- `mappings/ingredient_mappings.sssom.tsv`: `68552edd452d5dccf1262b5d03190a6b668341952a554f349149f269403cca67`
- `UNIFIED_INGREDIENT_MAPPING.tsv`: `6126d33febe2a577ff60295a36d6e5dd649a39e73c218f4d18468f3813adbce9`
- `reviews/workflow/mech-goal-sequence-20261019/cycle-000012/stage-05/revision-0001/evidence.yaml`: `4d57ba1b28f9628b2037d98fea9a10e9c55413243c8bc15141c4b09b2b2fe05e`
