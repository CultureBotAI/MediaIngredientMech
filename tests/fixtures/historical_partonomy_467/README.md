# Historical partonomy test context (#467)

`context.json.gz` contains four complete, byte-exact inputs from commit
`085948099b3b8f37eced6248704a60cee3d9502c`: both ingredient collections,
the reviewed decomposition table, and the earlier component correction
before-records. The fixture helper pins the compressed archive, revision,
membership, every input hash and byte length. The original three regression
test bodies and every assertion remain unchanged.

Those tests describe the September 2026 corpus, including its 83/502 counts
after the CMC correction and 84/506 historical replay. They must not combine
its old parent records with today's different active identity catalog. Only
those three tests receive this data context; current code and validators run.
Separate added tests validate the complete live corpus and the historical
writer's refusal to change it. Current data, schema and scientific holds are
not changed by this fixture.

This fixes the reproduced historical-context regression under #467. It does
not claim completion of that issue's separate original first-transition and
on-disk synchronization acceptance criteria. The genuine pre-migration commit
`caa918a94f6081947b2b713b84209282f4f0d7d9` still carries 23 parent-type values
that today's validator rejects; replacing or ignoring those values would
misrepresent the historical transition. That original replay needs its own
explicit historical schema/validator qualification.

The archive can be reproduced without network access from the named commit:
read each input using `git show COMMIT:PATH`, store its bytes as base64 with
SHA256 and byte length, serialize the documented context schema using sorted
keys and compact JSON plus one newline, then gzip with `mtime=0`. The helper's
input table is the exact file list. No current record is used to fill gaps.
