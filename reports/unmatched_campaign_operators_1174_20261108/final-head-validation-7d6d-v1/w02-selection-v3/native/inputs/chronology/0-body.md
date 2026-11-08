# W02-ARCHIVE-HANDOFF-RELATIVE-001

The sealed W02 `HANDOFF.json` SHA `31f84b76edaca928a98c2e9a4e54e4dd4276ca1bd311e32f1618338f1d6fc813` contains two relative path/hash objects that do not resolve from its own directory:

- `/actual_copy_status/read_only_status_receipt/path`: `actual-copy-git-status-v1.json`; exact evidence is `technical/actual-copy-git-status-v1.json`, SHA `087ff028d45496d1ab6797932c68e2c0e3685788b765bb3d13c547c8060b8547`.
- `/controls/technical/actual_tests/path`: `tests-v1.xml`; exact evidence is `technical/tests-v1.xml`, SHA `906207dca4371f540eabe1d067d05216ca329868238f0e20b0bd4994420eaa73`.

The actual first parent is `actual_copy_status`, not `actual_archive`. Fourteen other same-object path/SHA256 references resolve exactly. The handoff itself declares no alternate base. Its link to a technical report does not encode a base for these copied nested objects. The later skeptical receipt documents an interpretation, but does not cure the original handoff's missing base for generic traversal.

This is a pointer defect in my authored metadata. Both evidence files exist with the exact declared hashes; it establishes neither evidence loss nor a scientific/code defect. Preserve the original seal and add explicit corrected locators/base declarations in the new addendum. Do not create aliases, rewrite old files or silently relabel the earlier review as having validated generic traversal.

Reported before any additive correction. Coordinator root owns issue filing. Distinct skeptical confirmation and a complete handoff-reference audit are in progress.

Root reproduced the first missing locator and verified the actual evidence path; W02 and separate peers confirmed the second. This is recorded before the explicit successor locator correction. The old seal remains immutable; the new review must declare its base and preserve both original hashes.
