# Independent source review of #1031 membership repair

Recorded2026-11-01T06:05:19Z. Preliminary review of uncommitted source over `cb9f59a0d045f104ee2c3c00c8d6c4ad4f4eaf1f`; not approval of a final head or production apply. Only external fixtures and notes were written.

Reviewed source hashes:

| File | SHA256 |
|---|---|
| scripts/repair_heptahydrate_membership.py | 85317d72170174119ced30394194e0b1503bee9cc1fac1035147ad8fe2d064a2 |
| tests/test_repair_heptahydrate_membership.py | 5fc2361617c1a34ef57c2077d62aeb816df680cd17c4e25d2db1d4872351748f |
| src/mediaingredientmech/utils/culturemech_occurrences.py | 8ecd6beb22527e50524319a0321b6bcd35b4f56607ef71eb78d3740f3f90dbdf |
| scripts/promote_heptahydrate_ncit.py (reused native publisher) | f7cd1b46dc464cc8801a73f6b1cbd251bd5c0c7ffdf7241eff0e9cbee6f1c131 |

**Confirmed guard defect, reported to root before fixes:** the new writer calls `unique_destination(root)` before reserving evidence outputs, but neither the reused publisher's native validator nor its later checks repeats that namespace check. A new competing owner introduced after reservation is therefore outside the four frozen input paths. The real native transaction applies the membership repair and returns a `complete` receipt even though its own uniqueness helper then raises a collision. This is a non-cooperating writer race; the CLI's repository lock protects cooperative callers, but the current tests and guard design explicitly also check input/output replacement races at this boundary.

The first proof injected a minimal mapped owner. The stronger independent proof in `probe_valid_owner.py` uses a complete copy of the current NCIT record with a different preferred term, accepted by the native validated serializer before insertion under `data/ingredients/mapped/.ignored-backup/competing.yaml`. `valid-owner-race.json` records apply=true, complete receipt, exact expected output hash, and the failing post-success uniqueness check. Native journals and receipts are retained in their fixture directories. These probes do not alter production inputs.

Suggested narrow correction: make owner uniqueness part of native validation at the write boundary and add a regression inserting a new ignored/nested valid owner after reservation. Retain fail-closed input and evidence-path checks; preserve the competing record; do not solve this by deleting or overwriting it. A whole-corpus semantic approval or Step6 approval-model change is unnecessary.

Positive independent assessments:

- Actual frozen membership bytes produce exactly202098 output rows, with the same32 recipe/count pairs moved and202066 unrelated rows equal. Header bytes are identical. Expected output SHA256 is55ce5fabd42eb4cc1df628d4fd6a45b813caccbc7d7773105ece5633dd313897. See `scope-comparison.json`.
- A real native apply writes only membership, preserves all three owner/ledger/SSSOM anchors, preserves the complete before-image and native recovery journal, and repeat apply is a no-op without replacing the receipt. See `results.json`.
- Independently ran69 focused tests successfully,1 production-state assertion intentionally deselected before apply. They include real native receipt/backup replacement races, source preimage drift, structural/partial/collision refusals, native producer behavior and negative sibling/parent controls. Twelve emitted warnings are dependency deprecations. Exact command: `PYTHONPATH=src:../claw-source/src RUN/envs/mim/bin/python -m pytest -q -o addopts='' -p no:cacheprovider --basetemp ../step2-independent/membership-repair-review-20261101T060400Z/pytest-tmp tests/test_repair_heptahydrate_membership.py -k 'not committed_memberships' tests/test_semantic_identity_occurrences.py`.
- Routing delta on the previously captured complete1381-row relevant source slice changes exactly28 preferred-label plus4 dotted-label occurrences. Bullet `•` is accepted by current YAML; middle-dot `·` and English-name expansion remain outside this narrowly selected source repair. Their known remaining routing discrepancy is explicitly retained, not silently claimed repaired. See `routing-delta.json` and the earlier scope probe.
- No ingredient YAML, canonical SSSOM, rejection ledger or unified mapping edit is part of the writer. Frozen anchor hashes are checked and receipt approval is explicitlyNONE. The repair preserves the historical source snapshot and YAML26/26; regenerated count-bearing products should recover32/32 from the corrected membership.

Final acceptance still requires the guard finding's recorded disposition, stable source re-review, actual production membership/export inspection, full checks and receipt replay, a newly captured native review bundle, and independent review of the final committed head. The prior Step2 PASS remains superseded; no unreviewed future head is approved here.
