The same Git quoting defect also exists in the run-owned generic merge/cleanup verifier `verify_mim_merge.py`, which is planned for this sequence. This extension is recorded before repair.

A real isolated Git fixture with `Α-lipoic_Acid.yaml` demonstrates that `git diff --name-only` returns a quoted/escaped string. Passing that string back as a pathname makes the existing verifier's comparison report no difference even when the reviewed and simulated merged file contents differ. NUL-delimited enumeration preserves the exact path and detects the difference. The source-byte digest loop also skips the quoted string because it is not an existing filesystem path.

This is a medium-severity verification weakness for changed non-ASCII paths. No historical production merge mismatch is alleged; prior exact-head/integration reviews and closure evidence remain preserved. The fixture proof is `output/approved-plan-20261101T031134Z/step4-independent/{probe_merge_path_quoting.py,merge-path-quoting-proof.json}`.

The Step 4 closure will use a separately preserved corrected verifier with NUL-delimited Git paths and regression coverage, independently reviewed before any cleanup. This extends #1045's same root cause to the publication/cleanup boundary; it does not authorize deleting any unrelated branch or changing scientific content.
