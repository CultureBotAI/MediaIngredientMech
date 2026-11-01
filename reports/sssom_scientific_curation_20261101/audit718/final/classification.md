# Withheld mapping disposition inventory

Captured 2026-11-01T00:55:43.714546+00:00 at MIM `4625afd492b6cf43e3b499d1425d2453d490009d`.

Source: **2,987**; supported: **1,740**; withheld: **1,247** across **1,001** owner records.

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
| Review no longer binds changed/new row or owner | 21 |
| Assertion lacks mapping-specific positive disposition | 5 |

Withheld predicates: `skos:exactMatch` 998, `skos:broadMatch` 152, `skos:closeMatch` 97.

Categories are disjoint by ordered leading-text rules. A full reason may include several concerns. Inspect `withheld-reason-classification.tsv` for exact selectors, owner hashes, reasons and evidence references; `exact-reason-counts.tsv` preserves every distinct native reason.

Input bytes are retained under `inputs/`; `classification.json` records hashes and rule definitions. Native manifest hashes and counts were checked independently. This inventory does not establish that withheld rows are false, approve supported rows anew, or clear any scientific finding.
