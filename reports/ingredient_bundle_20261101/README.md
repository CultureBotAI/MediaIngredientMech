# Unchanged companion cohort — 2026-11-01

Issue [#1008](https://github.com/CultureBotAI/MediaIngredientMech/issues/1008)
reported a real CI failure: the existing opt-in companion review pinned the
previous complete SSSOM review, so the native exporter correctly rejected it
after the unrelated alias corrections. The original
[`../ingredient_bundle_20260924/review.json`](../ingredient_bundle_20260924/review.json)
remains unchanged, as do the complete companion claims, their decisions, the
selected owner bytes, and the selected scientific evidence entries. The global
mapping-evidence container changed outside this cohort. `prior-review.json` is
an exact byte copy of the historical review; `review.json` is a separate
immutable successor.

The successor changes only three dependency hashes: the complete mapping review,
the complete canonical SSSOM, and its global mapping-evidence document. It keeps
all 51 complete claims and decisions, all 20 exact owning-record hashes, all
selected original SSSOM payloads and scientific dispositions, and their complete
evidence entries (including reasons and basis). The cohort contains 20 mappings,
18 registry annotations, three product claims, and ten occurrences. None of the
eight owners affected by this curation batch belongs to that cohort. The
Carnitine registry-row withdrawal therefore remains outside the companion.

`dependency-refresh.json` records the exact selected rows, decisions, evidence,
input hashes and old/current dependency hashes. The report-local
`refresh_unchanged_cohort.py` validates the complete current base review first,
then independently replays the historical and successor companion inputs through
the native contract. It refuses owner, claim, decision, selected evidence,
column, prefix, semantic metadata, schema or scope-profile changes. It permits
only valid header date/version drift; each header must equal its newest row date
(Rule G). The observed dates are 2026-10-15 and 2026-11-01. Claim payloads are
identical; packaged bundle bytes and header metadata are not identical.

The producer reads historical bytes from commit
`4625afd492b6cf43e3b499d1425d2453d490009d`. New review, receipt and prior-copy
outputs must not exist. The checked-in successor already exists, so reproduce
it into three distinct new paths rather than overwriting historical output:

```bash
PYTHONPATH=src python reports/ingredient_bundle_20261101/refresh_unchanged_cohort.py \
  --output /tmp/issue1008-new-review.json \
  --receipt /tmp/issue1008-new-receipt.json \
  --prior-copy /tmp/issue1008-new-prior.json
python -m mediaingredientmech.export.ingredient_bundle export \
  --review reports/ingredient_bundle_20261101/review.json \
  --output output/ingredient-bundle-20261101-new
```

Independent review found the refresh helper could silently collapse duplicate
CLI output destinations before checking them. Issue
[#1009](https://github.com/CultureBotAI/MediaIngredientMech/issues/1009) was filed
before its fix: ordered destinations are now resolved and checked before any
input is loaded or output is reserved; exact duplicates and path aliases fail
without writes. Existing output files remain protected by exclusive creation.

The native exporter and validator guards are unchanged. This dependency refresh
adds no scientific approval, changes no identities, and clears no release holds.
CI selects the successor explicitly; KG-Microbe consumer activation remains a
separate gate. Tests use portable fixture history and do not require historical
Git objects in a shallow CI checkout.

Validation is saved in [`checks/verification.json`](checks/verification.json)
with exact command and log hashes: 72 focused tests passed; native companion
export and manifest-pinned validation passed; the final guarded helper replayed
to byte-identical successor and prior-review outputs in new paths; Ruff passed.
These are the recorded working-tree checks before the final independent commit
review, not a claim that all repository CI jobs passed.
