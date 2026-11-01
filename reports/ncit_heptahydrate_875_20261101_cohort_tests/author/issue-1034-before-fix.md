Independent final review of PR #1030 at `0bbe5e6816dc3d4332ab164d04a979cface4e179` found that `tests/test_repair_heptahydrate_membership.py:301–306` pins the mutable published membership table to the one-time repair cohort forever.

The repair correctly migrates exactly 32 existing recipe/count pairs. Its frozen preimage, recipe set, expected output hash and archived receipt should keep that exact assertion. The new test instead reads the live `mappings/culturemech_recipe_membership.tsv` and requires its NCIT:C61946 group always to equal `dict.fromkeys(writer.RECIPES, "1")`.

Two independent native producer controls demonstrate the defect:

- Adding an already accepted exact heptahydrate label in one new recipe produces 33 recipes / 33 occurrences.
- Adding one legitimate listing in an existing recipe produces 32 recipes / 33 occurrences.

Both full-table fixtures pass the actual active-owner, unique-edge, sortedness and stable-ID invariants with zero unknown IDs, but fail the new live-table equality test. The archived 32/32 baseline passes. The maintained producer documents recipe membership as mutable and occurrence counts as listing-derived; this is not a permanent scientific quota. This is the same mutable-live-input pinning class as #1012, distinct from #1031's repaired dangling identity.

Acceptance:

- Preserve exact-32 migration/preimage/receipt regression coverage against frozen historical fixtures.
- Remove the migration-time recipe/count pin from the live corpus assertion; retain current owner/retired-ID safety through native invariants.
- Cover both valid producer evolution cases without changing the production membership table or the existing repair receipt.
- Run focused tests and required checks, independently re-review the final head, and preserve the earlier failed probes and review history.

Evidence is frozen under the approved run's `step2-independent/live-membership-cohort-review/`: `review.md`, `results.json`, `probe.py`, captured logs and exact pre-fix sources. Root dequeued #1030 before merge; no source or production data fix has been applied yet. Production remains the valid, bounded 32-pair repair.
