# Companion review follow-up — 2026-11-01

This immutable successor follows the provenance and receipt repairs in issues
#1014 and #1017. It was produced by the maintained
[`scripts/refresh_unchanged_cohort.py`](../../scripts/refresh_unchanged_cohort.py)
with explicit baseline `612860e467aff74ecc1339df7c3c32b1bf940b95` and prior review
[`../ingredient_bundle_20261101/review.json`](../ingredient_bundle_20261101/review.json).
The prior review and both historical companion report directories remain intact;
`prior-review.json` is an exact byte copy of the immediate predecessor.

`review.json` preserves all 51 complete companion claims and decisions, all 20
owner hashes, all selected original SSSOM rows, and their complete base decisions
and evidence entries. The cohort still contains 20 mappings, 18 identifier
annotations, three product claims and ten occurrences. Only verified global
dependency hashes change. No scientific approval or release hold changes here.
The exact comparisons and hashes are in `dependency-refresh.json`.

Issues #1012 and #1013 are addressed by moving reusable logic to
`src/mediaingredientmech/ingredient_bundle_refresh.py` and providing explicit
`--baseline`, `--prior-review`, `--output`, `--receipt` and `--prior-copy` arguments.
The preserved report-local helper remains historical source for its original
recorded hashes; it is not the maintained entry point. The current documentation
and CI selector explicitly choose this successor. The command does not update
selectors or grant approval automatically.

The date-independent tests build an internally consistent synthetic base review
from preserved selected claims and evidence, rather than replacing literals in
the live canonical TSV. A real CLI integration test uses two temporary Git
baselines, two prior-review paths, and a later header date; both full native base
reviews validate. Header mutations derive their values from fixture rows, so
Rule G tests still exercise a real date mismatch after that later generation.
Issue #1016 adds actual symlink-directory aliases for all three output pairs,
with no-write assertions. Existing lexical and exact collision checks remain.

The maintained command retains exact owner/claim/evidence and semantic metadata
checks. Only evidence containers named by selected original decisions may refresh;
every selected base and companion evidence entry must remain identical. Packaged
schema/profile changes, scientific changes, invalid dates, changed columns and
stale inputs fail closed. Native exporter/validator guards and the protected
`qc-evidence` workflow are unchanged.

The preserved predecessor is the input for reproducing this exact transition:

```bash
PYTHONPATH=src python scripts/refresh_unchanged_cohort.py \
  --baseline 612860e467aff74ecc1339df7c3c32b1bf940b95 \
  --prior-review reports/ingredient_bundle_20261101/review.json \
  --output output/followup-companion-review.json \
  --receipt output/followup-companion-receipt.json \
  --prior-copy output/followup-companion-prior.json
python -m mediaingredientmech.export.ingredient_bundle export \
  --review reports/ingredient_bundle_20261101_followup/review.json \
  --output output/followup-companion-bundle
```

All output paths must be new. See `checks/verification.json` for the recorded
commands, producer hashes, logs and validation results. These local results are
separate from the final committed-head review and remote CI status.

Independent review subsequently identified the maintained writer's output-reopen
race as issue #1018. The writer now holds its exclusive handles through all
writes and flushing, verifies reserved inode identities, and preserves another
writer's replacement paths during failure cleanup. Deterministic tests replace
a reservation with a symlink or regular file at the snapshot boundary, both with
and without a callback error; immutable targets and replacements survive.

The original `dependency-refresh.json` and `checks/verification.json` preserve
the earlier execution and its producer hash. They are not silently rebound to
the repaired writer. The append-only `checks/issue1018/` evidence records the
repaired producer's new-path replay, byte equivalence and subsequent checks.
