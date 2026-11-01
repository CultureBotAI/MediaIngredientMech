# Receipt-reservation repair (#1029)

Independent review found that replacing a reserved receipt or backup path after
reservation could allow the original writer to complete its native data
transaction while losing the advertised evidence path. The
[original independent probe](independent-original-probe.py) and
[results](independent-original-race.json) reproduce that defect in isolated
fixtures. [Issue #1029](https://github.com/CultureBotAI/MediaIngredientMech/issues/1029)
was filed before this repair. No such race was observed during the original
production application.

The [archived historical writer](historical-applied-writer.py) has SHA256
`a66389a3379a761ee263aceb08222b6508f57cb9b8e69e996e82af732b59bb85`.
That is the producer used by the existing application receipts. Those receipts,
backups and journals remain unchanged; they are not relabeled as executions of
the repaired writer. It also preserves the exact source referenced by the
earlier execution artifact index, whose repository path now contains the fix.

The repaired writer has SHA256
`f7cd1b46dc464cc8801a73f6b1cbd251bd5c0c7ffdf7241eff0e9cbee6f1c131`.
It retains each reserved descriptor's device/inode identity and checks each
directory entry without following symlinks before native mutation, during
native validation, and before/after receipt completion. A detected replacement
raises an error. The writer preserves competing paths and native recovery
journals and changes its surviving receipt to `failed` through the original
held descriptor. If native mutation was interrupted, `applied: null` explicitly
leaves its completion unknown and requires recovery inspection. There is no
automatic rollback or overwrite of a competing path.

The new regression matrix covers sources and promotion, the receipt and every
backup path, regular-file and symlink replacement, and four timing boundaries:
reservation, prepared receipt, completed native commit, and completion receipt.
All cases use the real native transaction. A fresh pytest process running the
original writer failed [all 48 race cases](logs/step2-reservation-red.log).
The repaired writer passed [all 84 focused tests](logs/step2-reservation-green.log),
including the now-regenerated committed surfaces. Ruff also passed. These
results extend the earlier 35-test pre-application snapshot; they do not rewrite
its historical logs.

An [isolated replay](replay-result.json) through the repaired writer consumed
the actual frozen owner, full ledger, full canonical pre-image and actual native
candidate. It used the real Claw transaction. The resulting ledger and canonical
SSSOM bytes match production exactly, the history prefix is preserved, and both
repeat calls are no-ops. Its fixture has only the target owner; it is not a
fresh full-corpus identity audit. The new fixture event has its actual replay
timestamp, and no production event was reapplied or rewritten. The replay
verified production owner/ledger/SSSOM and every original application evidence
file unchanged before/after.

[The repair summary](repair-summary.json) and [artifact index](artifact-locations.json)
bind the exact sources and logs. These are author tests and replay, not
independent scientific approval. Independent re-review and final full QC are
reported separately. The mapping remains WITHHOLD and chemistry/BUFFER remain
open.
