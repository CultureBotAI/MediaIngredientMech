Independent adversarial review reproduced a missing proof-role separation check in the new #669 deferred-alias companion-refresh verifier, before real publication.

At source SHA256 `c963671ab86ecae0c29fe69f44f8012498e220de90e40910adbae7eb96127e27`, `verify_owned_name_suppression` only reads the manifest update's `publication_log` path. A caller can point that role at either the publication plan or the canonical SSSOM, repin the manifest, and pass verification. Both real native-chain fixtures return acceptance with no scientific approval added. The valid control also passes.

The agreed contract gives the completed external publication log a distinct attribution role. Reusing another proof input as that log violates the contract even though native receipt replay still verifies the row transition. The current external publisher emits the correct distinct path; this finding concerns the maintained verifier's accepted boundary, not observed corrupted mapping content.

Reject publication-log role reuse of any plan, inventory, source, generation artifact, native receipt, review, code or output input; preserve actual regular-file byte binding and the existing alias protections. Add regression cases for at least plan and canonical reuse, representative remaining proof roles, and an unchanged positive case. Keep all native payload, historical prefix, source inventory, unchanged approval and old typed-context assertions. Do not broaden the projection or weaken any gate.

Preserved evidence: `reports/owned_name_deferred_669_20261103/review-findings/proof-role-alias-v1/{context-before.py,test-before.py,probe-v1.py,result.json,archive.json}`. The probe's separate selected-evidence experiment is exploratory and is not asserted as a defect by this issue.

All current issue/PR pages were inspected; no existing issue covers this new verifier's proof-role reuse. This is separate from #1131's immediate writer completion membership check.
