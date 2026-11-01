The native reviewed export was regenerated and its source/review/partition hashes checked at MIM `4625afd492b6cf43e3b499d1425d2453d490009d`. Before the separately scoped melezitose correction, the current reproducible source contains **2,987 mapping rows: 1,741 supported and 1,246 withheld**, with withheld rows belonging to 1,001 owner records. The 3,018 / 1,763 / 1,255 numbers above describe the historical September release and should not be read as current corpus counts.

I classified every existing withheld disposition by its recorded leading reason, retaining the full row selector, owner hash, reason and evidence reference. These are disjoint text-based inventory categories, not new scientific judgments:

| Recorded leading reason | Rows |
| --- | ---: |
| Record-specific mapping, identity, alias or evidence concern | 548 |
| Current non-exact relation and synonym scope not established | 202 |
| Complete synonym payload lacks individual same-subject documentation | 196 |
| Individual reasons outside those standard prefixes, preserved verbatim | 96 |
| Cross-record baseline remains an unresolved review obligation | 56 |
| Preparation/concentration/instruction tokens need same-subject review | 49 |
| Label-index different-substance chemistry conflict | 39 |
| Lexical or close grounding does not establish exact equivalence | 35 |
| Changed/new row or owner no longer bound by the prior review | 20 |
| No mapping-specific positive disposition | 5 |

The withheld predicates are **997 exactMatch, 152 broadMatch and 97 closeMatch**. All 1,741 supported rows are exactMatch. A recorded reason can contain several concerns; the full text, rather than the leading-reason category, governs follow-up. A withheld row is not automatically a false assertion.

This is a mapping-only, deterministic inventory (`scientific_review: false`). It does not approve roles, components, the complete source graph, or downstream media; it does not reassess the other historical counts in the issue body. The exact snapshot and classification rules are saved under `output/sssom-curation-20261101T003435Z/audit718/baseline/`, including native manifest, disposition and evidence bytes and SHA-256 hashes.

The stale counts in `docs/SSSOM_RELEASE.md` will be refreshed against the final verified native export after this batch's content-bound mapping receipts are assembled. That document update will distinguish the historical published release from the reproducible current export. No blanket scientific approval or disposition change is part of this documentation correction; this issue remains open.
