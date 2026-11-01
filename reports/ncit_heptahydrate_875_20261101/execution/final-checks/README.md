# Regenerated products and validation snapshot

The native [full `just qc` run](logs/step2-full-qc-after-exports.json) completed
with exit code 0 at 2026-11-01T05:35:25Z. Its
[full log](logs/step2-full-qc-after-exports.log.gz) is losslessly compressed.
This is the completed generation/QC snapshot; final native capture and final
committed-head review remain separate requirements.

The [preliminary independent integration review](independent-review/review.md)
reports no unresolved implementation blocker after #1029. Its
[16-artifact index](independent-review/evidence-index.json), probe scripts,
original failures, repaired results and logs are copied byte-for-byte. The
reviewer did not author the fix; this report's author only packaged the saved
review artifacts. The repaired writer/refresh suite passed 133 tests. The
separate [author repair/replay](../reservation-repair/README.md) preserves the
original application producer and explains the repaired producer's hash.

## Bounded product changes

The corrected [v2 comparison](unified/final-comparison-v2.json), independently
confirmed by the [product verification](independent-review/products-verification.json),
records 4,170 unified rows and 209,330 occurrences. Three heptahydrate spellings
change only `mim_id` to `NCIT:C61946` and gain the canonical NCI label in
`synonyms`; 4,167 rows remain identical. Occurrences and recipe examples are
preserved. The bounded canonical SSSOM has 2,986 rows, distinct from the
2,979-row diagnostic candidate described in the preceding execution README.

The native [unified generation receipt](unified/unified-generation-receipt.json.gz)
is losslessly compressed and preserves all input hashes. The native
[freshness stamp log](logs/step2-unified-stamp.log) passed. The
[visualization comparison](visualization-delta.json) verifies that one node in
each of the graph and UMAP JSON files changes only its five identity/mapping
metadata fields. Every other field, node and coordinate remains unchanged.

The native [companion refresh](logs/step2-companion-refresh.log),
[export](logs/step2-companion-export.log), and
[validation](logs/step2-companion-validate.log) passed. The independently
replayed successor preserves 20 owners and all 51 claims/decisions; 14 mapping
locators move because of the removed SSSOM row. The selected scientific
assertions and their complete resolved evidence are unchanged. The mapping
remains WITHHOLD, BUFFER remains OPEN, no finding is retired, and no scientific
approval is added.

The post-generation [receipt/regression suite](logs/step2-receipt-regression-tests-after-generation.log)
passed 207 tests; the [companion regression suite](logs/step2-companion-regression-tests.log)
passed 46. Native reviewed-SSSOM export/QC, semantic-integrity, subject-resolution,
supported-KGX export/QC and writer-audit logs are retained with their exact
command wrappers. These local runs do not claim completion of later PR CI or
release approval.

## Validation limits and retained diagnostics

The [canonical invariant receipt](canonical-invariants/receipt.json) binds the
actual canonical hash and reports zero rejects. It uses the actual KG ontology
directory and explicitly skips B4 for missing **BTO and MICRO** transforms.
The [product-label run](logs/step2-product-labels.log) exits successfully but
reports **101 nonblocking warnings** and **5,312 pairs without an adapter**.
These limits remain visible; a passing gate is not comprehensive ontology or
scientific approval.

The following artifacts are historical diagnostics, not final passing results:

- [Incorrect v1 unified counts](unified/diagnostic-incorrect-final-comparison-v1.json)
  came from applying an SSSOM comment-filtering reader to a plain TSV. It dropped
  four legitimate ingredient names beginning with `#`, undercounting rows and
  occurrences. Use v2 and the corrected [analysis harness](harnesses/analyze_step2_final.py).
- [Initial full QC](logs/step2-full-qc.json) failed because the graph/UMAP target
  metadata was stale. The [metadata refresh](logs/step2-visualization-metadata.log)
  and successful full QC above resolve that execution failure.
- [Initial receipt/regression tests](logs/step2-receipt-regression-tests.log)
  included the expected stale unified-surface failure before generation.
  The post-generation run is the completed result.
- The original reservation-race and unchanged-cohort negative controls are
  expected failures demonstrating the corresponding defects; repaired checks
  are recorded separately. The independent preliminary test log also retains
  its pre-regeneration failure.

The [initial copy index](initial-artifact-locations.json) and
[final QC copy index](qc-artifact-locations.json) bind every source and packaged
hash. Gzip entries identify both compressed and original-byte hashes; they can
be inspected with `gzip -cd`. External fixture directories and multi-gigabyte
ontology/KG inputs were not duplicated. The report-wide inventory verifies
these packaged files without relying on the historical absolute run paths.
