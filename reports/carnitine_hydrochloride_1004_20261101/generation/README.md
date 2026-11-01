# #1004 generation evidence

This package preserves completed generation, validation and bounded comparison
evidence from the isolated worktree based on
`99fe4b44d78126d78041a69eeb366c52bedf0caa`. The SSSOM and unified producers used the
clean isolated Claw merge `6a7172585eb68da7f4fe01aee75a82458ddd470c`. Exact original
source paths, revisions, timestamps, configuration and hashes remain in the
captured receipts. The package is not a scientific approval or supervisor receipt;
no supervisor binding is invented. Final validation and final-head independent
review are recorded separately by the root.

## Results recorded by the completed commands

The native SSSOM candidate contains **2,975 diagnostic rows**, SHA256
`02b40e540b0663944500071e5725004ec0610e46bf3dd0b83cd4987820af7736`.
The full candidate was not substituted for the canonical table. The guarded
promotion changed two rows and removed four: the five salt claims became one
exact NCIT:C216679 claim, and NLDM's existing mapping acquired the new source/date
provenance. NLDM retained its original validation stamp. The resulting canonical
table has **2,982 rows**, SHA256
`d5cd812a8c44c85438d73c68c7a8c3067a505765e4cd54e3a64cef029f2d8ed6`.
Unrelated canonical row and metadata bytes were preserved. Two Rule K baseline
allowances were retired. The standalone review partitions these rows into
**1,739 supported and 1,243 withheld**.

The regenerated unified table has **4,170 names and 209,330 occurrences**, SHA256
`ca62e2f031ebe0f9e6185efc7816207912095beef9799a04634c889cc27196b5`.
Only `Carnitine Hydrochloride` changes: its identity becomes NCIT:C216679, CAS
becomes 461-05-2, and its two retained salt-name aliases are published. The other
4,169 rows, every occurrence count, and raw unrelated row bytes remain unchanged.
The native publication receipt, beforeimage, candidate and journal are retained.

Changing the NLDM owner withdraws **69 inherited approvals**: one mapping and
68 nonmapping assertions. Component 59 is the only changed nonmapping payload;
the other **67 payloads remain unchanged** but lose their old owner-bound
approval. All 69 assertions remain in the separate unsupported backlog and are
absent from the supported graph. Native semantic integrity passes while the full
scientific release remains **FAIL**, with 1,732 blocking findings and 2,336 open
assertions in this snapshot. The complete graph has 4,487 assertions, of which
2,151 are approved. These are recorded current counts, not a claim that the
remaining science has been resolved.

The companion refresh preserves **51 claims and decisions across 20 unchanged
owners**. Seventeen selected mapping locators move after row removal; their
complete evidence is retained. It adds no approval. Rebuildable full/supported
KGX, reviewed SSSOM and companion outputs are represented here by their manifests,
not copies of the graph products or the 18 MB unsupported backlog.

## Evidence layout

- `native-candidate/`: actual candidate, before/after input manifests, repository
  context, comparison-input hashes, all four label-map receipts, configuration,
  label report and actual-KG invariant receipt/rejects. CultureMech ingredient
  outputs and Mediadive nodes are comparison inputs to this SSSOM run; the
  receipt does not claim that the producer imports them.
- `canonical-validation/`: actual-KG native invariant receipt and zero-row reject
  table for the promoted canonical bytes.
- `native-chain/`: frozen execution preparation and the completed build's start,
  commands, verification and completion. Historical preparation documents remain
  preparation documents; the separate build receipts establish execution.
- `commands/` and `command-index.json`: completed command receipts and their
  exact logs. This includes the successful corrected full comparison, native
  chain, actual generation and validation, completed `just qc`, and 484 passing
  focused tests. These checkpoints do not stand in for final validation.
- `unified/`: actual native publication receipt, before/candidate and journal.
- `rebuildable-output-manifests/`: four native manifests only.
- `analyzer-1039/`: the entire frozen diagnostic-fix package, including original
  and fixed sources, original incorrect diagnostic, 23 passing regressions and
  fresh-process negative controls. The initial 4,166 / 209,323 diagnostic count
  is explicitly superseded. The corrected complete analysis is separately
  captured under `commands/step3-final-data-comparison-after-1039.*`.
- `harnesses/`: exact run-owned orchestration/comparison sources. Their original
  filesystem assumptions are preserved; these copies are provenance, not newly
  relocated execution entrypoints.

`manifest.json` maps every original source path to its portable archive path and
records both raw and archived byte sizes and SHA256 values. Large captures use
gzip with `mtime=0`; the entire frozen #1039 package remains byte-identical,
including its existing compressed fixtures and its original index. The equal
before/after candidate input manifests share one compressed copy while retaining
both source identities. No databases, source caches, whole fixture trees, native
chain `before/` tree, or pending full-suite/gate execution state are copied.
Source mutation receipts and backups are already in the implementation package
and are referenced rather than duplicated here.

## Preserved failures and limits

The first promotion dry-run safely refused NLDM because the initial guard
incorrectly expected an empty prior validation stamp. Its error and finding
[#1038](https://github.com/CultureBotAI/MediaIngredientMech/issues/1038) remain
classified as pre-fix evidence. The later successful promotion retains
`manual:promote_resolved_unmapped|PROMOTED|2026-08-06`. The earlier unified attempt
failed to acquire the repository lock; that failure log is distinct from the
successful v2 publication. Neither failed attempt is relabeled as a successful
publication. [#1039](https://github.com/CultureBotAI/MediaIngredientMech/issues/1039)
was an unpublished analyzer defect, and its original incorrect count remains
visible in the preserved historical evidence.

Both native invariant executions pass with zero reject rows. Their receipts
explicitly list unavailable B4 inputs `bto_nodes.tsv` and `micro_nodes.tsv` under
the read-only KG-Microbe ontology transform directory. Those missing transform
checks are not claimed completed; the actual available transform paths and
hashes are preserved.

The separate independent source audit found **eight pre-existing aggregate
`discussions` omissions**. For all eight, both the individual record and the
aggregate payload remain unchanged from durable base. The three changed targets
match their aggregate entries; this does not establish complete equality for
every unrelated record. The exact eight paths and preserved limitation are in
`summary.json`, attributed to the existing independent receipt at
[`implementation/independent/.../actual-source-application/receipt.json`](../implementation/independent/step3-mim-independent/actual-source-application/receipt.json).
That receipt is a historical source-application checkpoint which still described
promotion as blocked by #1038; only its source/aggregate findings are relied on
for this scope limit. Later generation/promotion success comes from the separate
completed receipts here. No new aggregate divergence is excused or repaired.

The corrected analyzer is dependency-author verification, not an independent
adversarial review. The source audit's separate reviewer identity and evidence
path are retained. Structural validation, hash continuity, and an unchanged
companion cohort do not grant new scientific or release approvals.

## Verify without writing

```bash
python reports/carnitine_hydrochloride_1004_20261101/generation/verify.py
```

This verifies archived and decoded hashes, nested frozen indexes, completed
receipt/log bindings, native candidate/canonical counts, the corrected unified
population, publication before/after continuity, and recorded release boundaries.
It requires only Python's standard library and does not regenerate outputs,
contact providers or write files. Add `--repository .` from the MIM root to check
the explicitly referenced maintained evidence files; `--originals` optionally
compares the captured original source files when the original run still exists.
