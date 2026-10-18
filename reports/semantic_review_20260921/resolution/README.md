# Historical MIM graph release: 2026-09-21

This page documents the published
[mim-supported-2026-09-21 release](https://github.com/CultureBotAI/MediaIngredientMech/releases/tag/mim-supported-2026-09-21),
from commit `199696ba30ca871c3afec56dcf09c805bc244370`. All counts, validation
receipts and reproduction results below describe that historical snapshot.
The [original review files](https://github.com/CultureBotAI/MediaIngredientMech/tree/mim-supported-2026-09-21/reports/semantic_review_20260921/resolution)
remain available at its release tag.

For current mappings, use the [standalone SSSOM release guide](../../../docs/SSSOM_RELEASE.md)
and [completed mapping disposition review](../../sssom_completion_20260921/README.md):
1,763 supported rows and 1,255 withheld rows. Those decisions supersede the older
mapping selection. This page does not announce a new KGX release; the current
checked-in review ledgers have advanced beyond this published graph snapshot.

The historical supported assertion subset passed semantic release validation.
Unsupported claims were preserved in a separate review backlog. Its complete
source graph retained a **FAIL** verdict; publishing the subset did not change
that verdict or erase its findings.

| Artifact | Scope | Count |
| --- | --- | ---: |
| Supported KGX nodes | All active ingredient record references plus referenced terms | 4,587 |
| Active ingredient record nodes | Source labels and paths; no unreviewed identity annotations | 2,874 |
| Supported KGX edges | Individually reviewed assertions | 2,112 |
| Supported SSSOM | Reviewed mapping rows | 1,603 |
| Supported roles | 97 nutritional, 17 physicochemical, 8 cellular | 122 |
| Supported components | Reviewed material part assertions | 381 |
| Supported environmental assertions | Reviewed contexts | 6 |
| Separate backlog | Current assertions excluded from the supported graph | 2,411 |
| Complete source graph | Preserved source assertions; semantically unapproved | 5,788 nodes / 4,523 edges |

Every active ingredient remains represented as a source-record node. All nodes
use the conservative `biolink:NamedThing` category. Chemical identities, roles,
components, and hierarchy are asserted only by selected reviewed edges. Raw
`record_json`, unreviewed identifier annotations, and old review verdicts are
absent from supported nodes. All 5,788 original full-graph node payloads are
preserved in the separate backlog alongside the 2,411 excluded edges and their
current review dispositions. The backlog is outside the KGX archive.

The full checked-in SSSOM has 3,018 rows and passes structural validation. Its
supported release is a separate 1,603-row SSSOM, with its own mapping-set ID.
Do not describe the full source SSSOM as scientifically approved.

## Source corrections

Original MicrobeDecoder rows and live BacDive records resolved both truncated
chemical names. The original CultureBotHT name/CAS row, KNApSAcK association,
and complete stereochemical InChI comparison resolved Artepaulin's registry
identity. [Identity evidence and plans](identities/README.md) document all three.

Eight cellular roles now cite inspected primary studies and name their organism
and conditions. Dissolved-ion extensions from hydrated salts remain explicit
inferences. [Role evidence and the complete affected-claim ledger](roles/README.md)
preserve the earlier predictions and identify the claims still requiring research.

Original source preparations corrected GYPS starch to elemental sulfur and
showed that CMC/PY/horse-serum had incorrectly collapsed separate growth conditions
into one mixture. BHI's unsupported exact recipe link became an unverified
candidate and stays out of the supported graph. Independent review rejected a
proposed TYGVS peptone substitution based on a different organism's preparation;
its four component claims remain open. See the [component audit](components/README.md).

## Review and release gates

[Finding dispositions](https://github.com/CultureBotAI/MediaIngredientMech/blob/mim-supported-2026-09-21/reports/semantic_review_20260921/resolution/finding-dispositions.tsv) retained all 2,106 historical
findings. [Assertion dispositions](https://github.com/CultureBotAI/MediaIngredientMech/blob/mim-supported-2026-09-21/reports/semantic_review_20260921/resolution/assertion-dispositions.tsv) covered every
full-graph assertion in that release. New positive dispositions required explicit reviewed plans;
historical positives are inherited only for the same source record, identical
source bytes, and identical assertion payload. Every inherited role also requires
a separate assertion-specific source-scope decision. The [role inheritance audit](roles/inherited-role-review.md)
withheld 24 unsupported promotions from generic mineral/growth-factor wording. The relevant 1,455 historical
review reports are archived with their original content hashes in
[historical-review-evidence.json](historical-review-evidence.json), so an ignored
local report directory is not needed to reproduce the release.

The gate checks source freshness, complete finding/assertion coverage, record
lineage, and independently reconstructed graph triples. The supported exporter
then checks the exact approved/excluded partition, sanitizes node annotations,
and verifies the separate backlog and deterministic archive. Missing evidence,
stale reviews, relabeled targets, reversed hierarchy, unrelated tombstones, and
unreviewed assertions cannot acquire approval through structural validation.

Independent adversarial review produced issues
[#711](https://github.com/CultureBotAI/MediaIngredientMech/issues/711),
[#712](https://github.com/CultureBotAI/MediaIngredientMech/issues/712),
[#713](https://github.com/CultureBotAI/MediaIngredientMech/issues/713),
[#714](https://github.com/CultureBotAI/MediaIngredientMech/issues/714),
[#715](https://github.com/CultureBotAI/MediaIngredientMech/issues/715),
[#716](https://github.com/CultureBotAI/MediaIngredientMech/issues/716),
[#717](https://github.com/CultureBotAI/MediaIngredientMech/issues/717),
[#719](https://github.com/CultureBotAI/MediaIngredientMech/issues/719),
[#720](https://github.com/CultureBotAI/MediaIngredientMech/issues/720),
[#721](https://github.com/CultureBotAI/MediaIngredientMech/issues/721), and
[#723](https://github.com/CultureBotAI/MediaIngredientMech/issues/723).
Their corrections have regression coverage. Final consumer review additionally
produced [#724](https://github.com/CultureBotAI/MediaIngredientMech/issues/724)
and [#725](https://github.com/CultureBotAI/MediaIngredientMech/issues/725).
The [finalization review](finalization-review.md) records the trait-bearing
aromatic-compound mapping exclusion and the independent policy that prevents
its hold from being removed or redirected through a rehashed ledger.
Agent review is not human sign-off.

SSSOM JsonSchema, PrefixMapCompleteness, and StrictCurieFormat pass for both
mapping artifacts. The supported archive also passes the native KGX 2.7.0 reader,
including all endpoints, predicates, and retained JSON annotations. Strict
Biolink conformance is not claimed for MIM's native relationships. Exact hashes
are in [supported-release.json](supported-release.json) and the validation receipts.

A clean `git archive` checkout reproduced all 11 full/supported artifact files
byte for byte and reproduced all five dated review proof files, with no ignored source files. The finalization regression run passed 115 focused tests; maintained-package
coverage from the preceding complete CI run was 65% against the 35% floor.
See [validation-summary.json](validation-summary.json) and
[clean-checkout-validation.json](clean-checkout-validation.json). Published visualization metadata now passes its strict currency check after
removing three retired nodes and refreshing 11 nodes in each artifact; see
[visualization-validation.json](visualization-validation.json). Required CI
runs the complete test suite and repository QC before merge.

## Reproduce from a clean checkout

Run these commands from a checkout of tag `mim-supported-2026-09-21` to reproduce
the historical counts and receipts above. Running them on current `main` uses
the later mapping decisions and does not reproduce this published snapshot.

Use new output directories; the exporters refuse to overwrite existing bundles.
The reviewed report binds the complete graph to its deterministic directory and
input contents:

```bash
just export-kgx output/mim-kgx-710-full
just export-supported-kgx reports/semantic_review_20260921/resolution/current-review.json output/mim-kgx-710-supported
just qc-supported-kgx reports/semantic_review_20260921/resolution/current-review.json output/mim-kgx-710-supported
```

The [consumer TSV audit](tsv-consumer-validation.json) verifies format, endpoint
closure, exact SSSOM/KGX mapping agreement, and the complete approved/backlog
partition. There are 1,395 isolated ingredient source-reference nodes. Source
confidence annotations are preserved verbatim, including 12 values of `0.8` and
17 values of `0.95`; their grading-policy provenance remains open in
[#662](https://github.com/CultureBotAI/MediaIngredientMech/issues/662).

The supported directory contains `mim-kgx.tar.gz`,
`ingredient_mappings.sssom.tsv`, `unsupported-backlog.json`, the manifest, and
uncompressed graph TSVs. CI reproduces and validates them and uploads the
`mim-supported-graph` artifact. The backlog's bytes are bound by the manifest;
they are not members of the graph archive.

`build_review.py` reproduces this dated review from its explicit plans and
archived historical evidence. It does not automatically approve new claims.
Re-running the complete-corpus gate with `--require-pass` intentionally exits 1.

## Remaining scientific work

[Issue #718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718) tracks
the separate scientific backlog: 662 prediction-only roles, 11 empty-evidence
roles, 24 additional unsupported role promotions, 43 source-unverified component assertions, the ambiguous CMC/PY expression,
and the unresolved record-level findings. These overlapping findings remain
explicit in the full ledger. New evidence can admit a claim into the supported
release only after another content-bound review.
