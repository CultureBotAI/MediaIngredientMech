Independent #1174 review reproduced a minor preflight/receipt roundtrip defect in provisional `campaign_owner_apply.py` SHA256 `74a448602d8d512a1b12037d88d0eba0a9ac9e1ea55c89e6bd3051afb23f0a99`.

Top-level plan and acceptance arguments are made absolute but their saved repository-relative spelling is not checked with the same canonical-path rule used by `verify_completed`. The CLI passes the spelling through.

In a private actual native fixture, `intake/../plan.json` and `intake/../acceptance.json` refer to existing regular files inside the same root. Preparation accepts them; application changes owners and returns complete. Its completed verifier then rejects its own saved acceptance reference as `Noncanonical relative path`. No symlink, outside-root target, real campaign data or author-file mutation is involved.

Reject noncanonical top-level root/plan/acceptance/receipt spellings before rendering, output reservation or source writes, consistently with the completed verifier. Preserve alias protections instead of resolving symlinks away. Add regression refusals proving source/receipt bytes remain unchanged and a canonical positive roundtrip.

Finding `IR-CAMPAIGN-OPERATORS-4`, SHA256 `1eb8040969565287cb758048ef9e015f85b4eab9fd385d3b04fcdf2b37911d85`. Probe SHA256 `31e6f57c1272e3f259f91392778d8909c8f03b5435caba258231f9cae9008ea4`; result SHA256 `e5eadc31942aa1f5a9d47fc46ab9ffb7e809e29b79b6ef48f7d3960bbcec14e2`. Evidence will accompany the implementation PR.

Live all-state campaign/path search was checked. #1161 is a separate accounting-observer path-role defect; #1194 covers late membership, #1195 loaded code, and #1197 chain continuity. This is an early argument-validation omission, not a scientific identity finding or a claim of silent publication.
