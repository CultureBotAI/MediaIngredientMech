# #1034: bind the one-time migration test to its historical input

Only `tests/test_repair_heptahydrate_membership.py` changed. Its stable SHA-256 is `a615daeb6276bcf32a3d879efa9b09a4c1c379751ee8a9330f66fb9ab7b384b3`. The repository HEAD remains `0bbe5e6816dc3d4332ab164d04a979cface4e179`; no commit, production application, writer change, data change or GitHub mutation was performed. The issue was filed by the parent before this repair; its supplied body is preserved as `issue-1034-before-fix.md`.

The previous test read the live membership table and required its NCIT:C61946 rows always to equal the 32 recipes/counts from the historical repair. That rejected valid new recipes and repeated listings. The independent pre-fix proof remains untouched at `../step2-independent/live-membership-cohort-review/`.

The replacement historical regression decompresses the **committed application preimage** at `reports/ncit_heptahydrate_875_20261101_membership/application/apply.before-membership.tsv.gz`. It calls the actual pure `writer.repaired_membership`, compares input/output hashes with the original committed receipt and writer constants, preserves the exact 32 recipe/count pairs, source header and unrelated rows, rejects remaining retired IDs, and checks idempotence. It does not use today's membership header or counts as its historical fixture.

The live assertion now forbids the retired identity without imposing a cohort size. The unchanged generic native membership suite still enforces active owners, unique/sorted edges and stable identifiers. Two additional regressions execute the real producer's `main()` on external occurrence fixtures derived from the committed occurrence archive:

| Accepted source evolution | Native media / occurrence counts |
| --- | --- |
| One new recipe with an already accepted exact label | 33 / 33 |
| One additional listing in an existing recipe | 32 / 33 |

Both fixtures have no unknown IDs, preserve unique sorted membership keys and pass the actual live retired-ID assertion. The real effective-statistics helper returns the new counts while the fixture owner's stored 26/26 YAML remains byte-identical. No production membership or YAML counts were altered.

Validation:

- `checks/step2-test1034-focused.{log,json}`: **90 passed**, including the repaired tests and `tests/test_culturemech_membership.py`; native transactions ran without skips. The 13 reported warnings are dependency deprecations.
- `mutation_controls.py` executes each case in a fresh Python/pytest process on copied source files. The unmodified external control passes all three new historical/growth cases.
- Restoring the old live equality assertion fails **both** growth cases.
- Replacing the native producer's listing increment with assignment fails the repeated-listing count regression.
- Bypassing the historical writer's migration fails the archived receipt/output hash regression.
- `verification.json` records successful `git diff --check`, the sole changed tracked file and byte verification of all **364** protected inputs, including the production membership, writers, owner, SSSOM, ledger, unified surfaces and both earlier frozen report trees.

`source-before.py`, `source-after.py` and `source.patch` preserve the exact test change. `baseline.json` binds the protected inputs; `mutation-results.json` binds each command, log and changed copy. Mutation failures are expected negative controls, not production defects or failed current tests. Independent re-review and the parent's eventual final-head/native capture remain pending; this authored evidence does not substitute for them.

`inventory.json` binds this bounded evidence set. It excludes itself, `pytest-focused/`, and `mutations/` (reproducible external fixture trees); the harness, source snapshots, results and complete small logs are included. Earlier frozen inventories were not modified.
