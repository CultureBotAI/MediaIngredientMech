# Native correction/publication canary

The canary in `tests/test_additional_mapping_successor_publication.py` performs
adoption, two reviewed source corrections and canonical preparation, dry-run,
application and terminal verification. All records, evidence and review judgments
are synthetic. The real native APIs, Claw generator, SSSOM validator, operational
fit and lease rules run intact. It preserves the predecessor receipts and holds;
it supplies no scientific or public-release approval.

Run from this checkout with an explicit maintained Python 3.13 environment and
an isolated Claw checkout at the reviewed producer revision:

```bash
"$MIM_CANARY_PYTHON" scripts/adhoc/run_release_recovery_canary.py \
  --python "$MIM_CANARY_PYTHON" \
  --claw-root "$MIM_CANARY_CLAW" \
  --claw-head 7070392fcb5e31282499a599f7147b56b96e5aca \
  --output .temp/release-canary/run-1
```

The helper requires the expected HTTPS Git origins, clean producer source and a
fresh physical output path. It records the command, exact source hashes, log,
JUnit result, four completion phases and nonempty native receipts/artifacts.
It clears ambient pytest options and returns failure when completion evidence is
missing, including a zero-exit collection-only run. Use a new output directory
for a necessary new run; preserve earlier evidence. The observed local canary
required about 35 minutes. Do not repeat it just to refresh a status line.

The [retained public result](reviews/native-release-recovery-canary-20261115.json)
records the successful run and artifact hashes. Private absolute command paths
are omitted from this projection; original command/result hashes are retained.
CI selects the same Claw source independently of the unchanged governance pin.
Local general pytest runs skip this integration case unless
`MIM_ADDITIONAL_ASSERTION_CLAW_SRC` is supplied; CI supplies it explicitly.

Issues #1420, #1423, #1425 and #1426 track the source-replay/publication repairs.
Independent findings #1427 and #1428 repaired the canary helper's completion and
output-boundary checks. The separate published-predecessor regression is
`tests/test_curation_successor_chain_publication.py`; this canary's two source
corrections precede its first canonical publication.

The four real campaign source corrections, their native assessment, changed
actual generation and consumer/release review are separate work. A successful
synthetic canary never authorizes public release or consumer installation.

## Type-only qualification follow-up

Issue #1430 records eight inherited mypy errors. The follow-up adds type
declarations and explicitly qualifies the resulting successor source digest,
retaining the previously tested digest. All function/method executable code
compares equal after excluding line metadata; the new typing import and class
annotation metadata are separately disclosed. The compile-only helper
`scripts/adhoc/compare_type_only_sources.py` and its
[results](reviews/native-release-recovery-types-20261115.json) are retained.
Changing an executable guard condition makes the comparison fail.

The original canary and its artifacts remain tied to their recorded source
commit. They were not rerun or relabelled for this annotation-only follow-up.
Exact source-counterpart admission/refusal and focused replay/assertion tests
validate the final qualification separately. These checks do not replace real
campaign science or release gates.

The separate [published-predecessor result](reviews/native-published-predecessor-20261115.json)
records a genuine native canonical application followed by predecessor admission
and both missing-publication and missing-review refusals. It passed at the
recorded pre-typing commit; predecessor bytes remained unchanged.

Independent follow-up findings #1432–#1434 made the comparison helper more
conservative: executable annotation targets, local-binding changes, ordinary
constant stores and scalar type/bit distinctions cannot disappear. Twelve
comparison regressions pass; targeted mutations make the relevant tests fail.
The corrected helper regenerates only its type-comparison evidence for the same
production source hashes. Original native canary and predecessor artifacts are
preserved with their original tested commits.
