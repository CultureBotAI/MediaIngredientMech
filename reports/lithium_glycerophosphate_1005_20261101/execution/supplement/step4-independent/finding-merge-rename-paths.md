Independent review of the proposed Step 4 closure verifier found an additional changed-path coverage defect while re-reviewing #1045. This finding is filed before repair or any branch cleanup.

The corrected NUL/literal-path verifier still uses Git's default rename detection when enumerating changed paths. For a reviewed rename, `git diff --name-only -z BASE HEAD` lists only the destination. A simulated merge can retain that correct destination and resurrect the removed source, and the comparison accepts it because the source was not enumerated.

The reviewer reproduced this with real isolated Git trees and a Unicode owner rename. The exact proposed helper was `verify_mim_merge_nul.py`, SHA256 `869d6925c57402f7867e8ab8f1c6a2b472125b57faa945332472993cea3b080a`. Evidence: `output/approved-plan-20261101T031134Z/step4-independent/probe_merge_rename.py` and `merge-rename-proof.json`. No historical production merge mismatch or cleanup is claimed.

Severity: medium, incomplete verified merge-content scope. Enumerate changed files with `--no-renames` so both deleted source and added destination are checked, preserve NUL parsing and literal path handling, and add a regression that a renamed-source resurrection is rejected. Retain positive rename, deletion and previous non-ASCII/path controls. Re-review the exact repaired helper before using it for the approved merge/cleanup sequence.
