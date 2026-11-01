# Withheld mapping disposition inventory

Captured 2026-11-01T00:42:50.597666+00:00 at MIM `4625afd492b6cf43e3b499d1425d2453d490009d`.

Source: **2,987**; supported: **1,741**; withheld: **1,246** across **1,001** owner records.

This is a deterministic classification of existing review reasons, not a new scientific review. No dispositions were changed. Roles, components, KGX and downstream media are outside scope.

| Recorded leading reason | Rows |
| --- | ---: |
| Existing record-specific mapping, identity, alias or evidence concern | 548 |
| Prior review does not establish current non-exact relation and synonym scope | 202 |
| Complete other-token payload lacks individual same-subject documentation | 196 |
| Other preserved native reason | 96 |
| Cross-record baseline remains an explicit unresolved review obligation | 56 |
| Preparation/concentration/instruction tokens need same-subject review | 49 |
| Label-index different-substance chemistry conflict needs per-record review | 39 |
| Lexical or close grounding does not establish exact equivalence | 35 |
| Review no longer binds changed/new row or owner | 20 |
| Assertion lacks mapping-specific positive disposition | 5 |

Withheld predicates: `skos:exactMatch` 997, `skos:broadMatch` 152, `skos:closeMatch` 97.

Categories are disjoint by ordered leading-text rules. A full reason may include several concerns. Inspect `withheld-reason-classification.tsv` for exact selectors, owner hashes, reasons and evidence references; `exact-reason-counts.tsv` preserves every distinct native reason.

Full input bytes are retained in the original run at `output/sssom-curation-20261101T003435Z/audit718/baseline/inputs/`. This publication copy retains the native export manifest and every classified row/reason; `classification.json` records all input hashes and rule definitions. `base-source-verification.json` verifies that the source SSSOM, review and mapping evidence bytes equal Git base `4625afd492b6cf43e3b499d1425d2453d490009d`, from which the native export is reproducible. Native manifest hashes and counts were checked independently. This inventory does not establish that withheld rows are false, approve supported rows anew, or clear any scientific finding.
