Confirmed in-scope test defect: the live membership table is pinned to the repair's historical32-pair cohort

At reviewed head`0bbe5e6816dc3d4332ab164d04a979cface4e179`, `tests/test_repair_heptahydrate_membership.py:301` reads the live maintained membership table and line306 requires the complete NCIT:C61946 recipe/count dictionary to equal the frozen migration list with every count1. This rejects ordinary supported future source evolution. It is a real regression-test contract defect, medium priority, even though the current committed snapshot satisfies it.

The exact32-pair constraint is correct for this one guarded historical migration. It already belongs in the frozen migration fixtures and archived occurrence replay. The production membership artifact has a different ongoing contract: `scripts/build_culturemech_membership.py:68` explicitly says recipe IDs are stable but their set is not; `collect` at line94 counts accepted occurrence rows, and repeated ingredient listings increase occurrences rather than duplicate edges. `justfile:318` exposes the maintained rebuild against refreshed CultureMech output. The effective-count helper reads the rebuilt membership without changing historical YAML counts. Nothing in this producer contract sets a permanent32-recipe limit for the ingredient.

Independent native reproduction

`probe.py` loads the actual current producer, the actual new live test function, and the existing native membership invariant functions. It selects the32 accepted source rows from the immutable audit875 occurrence archive. Each result uses native `collect` and `write`, preserving all unrelated live membership edges in an external fixture. No production file or source code is changed.

| Source fixture | Native target result | Unknown IDs | Actual ownership/unique/sorted/stable-ID tests | Actual new live test |
|---|---:|---:|---|---|
|Unchanged archived32 rows|32 recipes /32 occurrences|0|PASS|PASS|
|One new recipe using an already accepted exact label|33 recipes /33 occurrences|0|PASS|FAIL at line306|
|Second listing within one existing recipe|32 recipes /33 occurrences|0|PASS|FAIL at line306|

The new recipe is a clearly synthetic future-source fixture (`CultureMech:999999`), not a claim that a new real CultureMech recipe currently exists. Its record shape and accepted source label follow the native producer contract; the second case independently demonstrates failure without adding a recipe identity at all. Both positive source evolutions are already supported by the maintained producer, including the existing unit test for repeated listings. Complete native outputs, full-size membership fixtures, tracebacks and hashes are retained in `results.json`, `probe.log` and the case subdirectories. This is not a hand-edited membership-table demonstration.

The producer emits202,099 total edges for the new-recipe case and202,098 for the baseline and repeated-listing cases; the latter appropriately increases one occurrence count. Effective counts follow33/33 and32/33. The current production membership hash remains`55ce5fabd42eb4cc1df628d4fd6a45b813caccbc7d7773105ece5633dd313897`; all inspected source hashes and the clean worktree are preserved.

Narrow fix boundary

Keep exact membership/cohort/header/count preservation in the guarded migration tests and immutable archived-source replay. Keep a live regression against reintroducing the retired identifier and the existing general active-owner invariant. Remove the fixed complete32-pair equality from the ongoing published artifact, or bind that equality to the frozen repair beforeimage/afterimage rather than the live table. Demonstrate that the two native source-evolution controls pass the intended ongoing invariants after the test correction. Do not alter production membership, the32-pair application receipt, owner counts, source-label routing, exports or scientific decisions merely to satisfy the test.

This is the same general defect class documented by archived #1012: a test hard-codes mutable maintained output and breaks a later valid rebuild. The comparison is to the archived issue's description of live SSSOM header pinning; this review did not fetch or assert the current issue state. The exact historical32-cohort migration remains valid and must remain tested.

Root was informed of the reproduced finding before any fix. The prior queue-readiness verdict is superseded for this defect; correction and independent re-review of the new final head are required. No GitHub mutation or implementation edit was performed by this reviewer.
