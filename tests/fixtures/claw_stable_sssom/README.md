# Native stable SSSOM producer fixture

These are unmodified source bytes from CultureBotAI/culturebotai-claw commit
`c1cbd0f715f2d83d7cb6773797af7651e315454d`, retained solely for offline native
integration tests for MIM issue #1335. `ORIGIN.json` records each original path,
its SHA-256 and byte count. The `.txt` suffix prevents test and formatting tools
from treating the retained upstream sources as MIM implementation files.

The fixture contains the complete 15-file Python snapshot enumerated by the
upstream stable builder, its fleet manifest, and the two root metadata files
required by the native adoption/lease verifier. The materializer verifies every
source byte and commits a new synthetic checkout. Generation receipts record
that actual synthetic Git HEAD; they do not claim it is the upstream commit.

No producer, validator, lock, or review gate is replaced with a test double.
Synthetic inputs use NCIT grounding, whose native generator path uses stored
labels without a provider request. Actual SSSOM validation still runs.

The upstream checkout had no LICENSE, COPYING, or NOTICE file in an
ignored-inclusive search, and no license declaration was found in its root
`pyproject.toml` or `README.md`. No license text has been invented here.

`STABLE_SSSOM_CLAW_ROOT` can explicitly select a real checkout at the reviewed
commit for the same integration tests. Tests clone that checkout privately;
the supplied producer remains read-only. The repository's product pin and
workflows are unaffected.
