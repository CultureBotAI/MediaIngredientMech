# Reviewed MIM release with a separate scientific backlog

The supported assertion subset passes semantic release validation. The user
explicitly chose to preserve unsupported claims separately rather than publish
them as supported knowledge. The complete source graph still has a **FAIL**
verdict; this release does not change that verdict or erase its findings.

| Artifact | Scope | Count |
| --- | --- | ---: |
| Supported KGX nodes | All active ingredient record references plus referenced terms | 4,588 |
| Active ingredient record nodes | Source labels and paths; no unreviewed identity annotations | 2,874 |
| Supported KGX edges | Individually reviewed assertions | 2,137 |
| Supported SSSOM | Reviewed mapping rows | 1,604 |
| Supported roles | 121 nutritional, 17 physicochemical, 8 cellular | 146 |
| Supported components | Reviewed material part assertions | 381 |
| Supported environmental assertions | Reviewed contexts | 6 |
| Separate backlog | Current assertions excluded from the supported graph | 2,386 |
| Complete source graph | Preserved source assertions; semantically unapproved | 5,788 nodes / 4,523 edges |

Every active ingredient remains represented as a source-record node. All nodes
use the conservative `biolink:NamedThing` category. Chemical identities, roles,
components, and hierarchy are asserted only by selected reviewed edges. Raw
`record_json`, unreviewed identifier annotations, and old review verdicts are
absent from supported nodes. All 5,788 original full-graph node payloads are
preserved in the separate backlog alongside the 2,386 excluded edges and their
current review dispositions. The backlog is outside the KGX archive.

The full checked-in SSSOM has 3,018 rows and passes structural validation. Its
supported release is a separate 1,604-row SSSOM, with its own mapping-set ID.
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

[Finding dispositions](finding-dispositions.tsv) retain all 2,106 historical
findings. [Assertion dispositions](assertion-dispositions.tsv) cover every current
full-graph assertion. New positive dispositions require explicit reviewed plans;
historical positives are inherited only for the same source record, identical
source bytes, and identical assertion payload. The relevant 1,455 historical
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
[#716](https://github.com/CultureBotAI/MediaIngredientMech/issues/716), and
[#717](https://github.com/CultureBotAI/MediaIngredientMech/issues/717).
Their corrections have regression coverage. Agent review is not human sign-off.

SSSOM JsonSchema, PrefixMapCompleteness, and StrictCurieFormat pass for both
mapping artifacts. The supported archive also passes the native KGX 2.7.0 reader,
including all endpoints, predicates, and retained JSON annotations. Strict
Biolink conformance is not claimed for MIM's native relationships. Exact hashes
are in [supported-release.json](supported-release.json) and the validation receipts.

## Reproduce from a clean checkout

Use new output directories; the exporters refuse to overwrite existing bundles.
The reviewed report binds the complete graph to its deterministic directory and
input contents:

```bash
just export-kgx output/mim-kgx-710-full
just export-supported-kgx reports/semantic_review_20260921/resolution/current-review.json output/mim-kgx-710-supported
just qc-supported-kgx reports/semantic_review_20260921/resolution/current-review.json output/mim-kgx-710-supported
```

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
roles, 43 source-unverified component assertions, the ambiguous CMC/PY expression,
and the unresolved record-level findings. These overlapping findings remain
explicit in the full ledger. New evidence can admit a claim into the supported
release only after another content-bound review.
