# Lithium tetraborate lookup leads — allocation159

This bounded cache supports worker01's source review. It **does not select a CAS,
CID, hydration state, owner or mapping**, change a hold, or approve curation.

The actual worker capture equals frozen shard01's zero-based allocation159:
`CM_NAME:feaadf9d3b6ed6487f4bc361dcdf9a39d7a4756737bb30c7412182ec966ec065`.
Its canonical case hash is
`aee8ece51d2c44adf0581d33b4e616dac8c8ce0728d88398ecc34bb025c40d7c`.
The source label is `Li2B4O7`; both frozen occurrences and their full recipe
snapshots are preserved. Their stated 0.01 g/L concentration does not establish
the supplied reagent's hydration, supplier, grade or structure.

Exactly five ordinary free official PubChem REST requests were made, once each:
four exact CID property requests and the exact CAS-name CID query for
`12007-60-2`. All returned HTTP200 on 2026-11-08 between 04:29:25 and 04:29:27 UTC.
There was no authentication, challenge bypass, paid provider or extra lookup.
The coordinator's earlier page reCAPTCHA/Unauthorized failures are labelled as
reported failures in `reported-prior-failures.json`; their absent raw responses
are not represented as captured evidence here.

| Requested CID | Returned formula | Returned InChIKey |
|---|---|---|
| 15764247 | B4Li2O7 | PSHMSSXLYVAENJ-UHFFFAOYSA-N |
| 9815330 | B4Li2O7 | XFOCQAMEVCAHGV-UHFFFAOYSA-N |
| 21895667 | B4Li12O12 | XGCILSHUAUFSLI-UHFFFAOYSA-N |
| 90478374 | B4H10Li2O12 | KTDDBABFAZCLKP-UHFFFAOYSA-N |

The first two records have the same formula but different InChI, InChIKey and
IUPACName descriptors. That equality of formula does not establish interchangeable
chemical identity or select either record for this source. CID21895667's returned
formula differs; the prior name-only association was a coordinator lead and was
not queried again. CID90478374 explicitly includes `pentahydrate` in its returned
IUPACName and five waters in its InChI; the source case is not assigned that form.

The exact CAS-name query returned the complete list `[9815330]`. This is a
PubChem lookup result, not independent CAS Registry certification, an exhaustive
proof about alternate representations, or identification of the actual source
reagent. All four requested property records are retained regardless of that
query's result. No alternative was discarded and no new CID was fetched.

[lookup-results.json](lookup-results.json) preserves every returned property and
CID alternative, URL, UTC retrieval time and payload hash, with explicit limits.
[source-binding.json](source-binding.json) binds the exact worker artifact and
frozen case/occurrences. `captures/` contains all raw bodies and HTTP provenance.
`MANIFEST.json` hashes the cache, excluding itself and final verification receipts.

From the campaign root, the offline byte/reference check is:

```sh
PYTHONDONTWRITEBYTECODE=1 ../kgm-unmapped-20261107/env/bin/python \
  evidence-cache/lithium-tetraborate-leads-v1/verify_cache_v1.py
```

Worker01 retains scientific review ownership. No worker artifact, maintained
record, ledger, GitHub state, tmux pane or previously sealed shared cache was edited.
