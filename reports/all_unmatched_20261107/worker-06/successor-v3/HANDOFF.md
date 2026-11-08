# Worker06 successor-v3 handoff

Use [selection.json](selection.json) as the **single authoritative complete proposed intake**. All earlier selections and author fragments are historical. This successor is based on published `1b3641853c7105b9091f81b5a9b19c99e8ed351e`; the commit containing this handoff is the publication revision, reported separately after ordinary push.

All 188 assigned cases, 310 frozen CultureMech occurrence IDs and 88 downstream holds are retained. The selection contains 103 proposals (78 new-owner proposals and 25 edits of existing owners) and 1,091 evidence entries. Relative to v2, 23 payloads are new or changed, 26 proposal metadata objects change, and 48 case outcomes or review bindings change. These are isolated proposals; no maintained owner, source selector, SSSOM, canonical export or downstream rebuild was applied.

Final source-case acceptance remains pending independent coordinator re-review. Passing gates and this handoff confer no whole-owner, role or export approval.

## Authoritative hashes

Selector SHA256: `9a3d7f47b6890edd04479e9a8365dfdfbe0700e108034486c0e53e0b8efeb0c5`.

| Ledger | Previous v2 SHA256 | Final v3 SHA256 |
|---|---|---|
| [decisions.json](decisions.json) | `815ea3441a231f3d2464a57089338c7c78d07ac3f9c3f77e77f4865b39c01acd` | `05bd044acaee14d847c30a35cd93a9e76b2da8bb94557cbfb8a4aba41f2b4ad7` |
| [proposals.json](proposals.json) | `2244c896a5b1cf50681da7d7f15c4ccabae916aa31cc9e40e18b95d72e0dfd14` | `4b81f37e58648c2e7afab633ee4aaad4532f5667d4131c216bd1395f18466363` |
| [evidence.json](evidence.json) | `3abee21eb759145e210d5fa5ee3f77fcc3aba0bc0c71eccde35d9b890022fec3` | `337ca676bf7e6b9799ebc6473273f98dd20a835e32b631de50f7f738b759881f` |
| [source-holds.json](source-holds.json) | `eaddfd7ffe5ba2ba1be011696ad741e1b010db2cc9ca4678954a640484f70b77` | `eaddfd7ffe5ba2ba1be011696ad741e1b010db2cc9ca4678954a640484f70b77` |

[Completion receipt](completion-receipt.json) also records original d5 hashes, exact native pair hashes and all independent receipt hashes. [Delta ledger](delta.json) gives every exact old/new proposal payload hash and changed case-object hash.

## Finding dispositions

The full sealed worker03 findings and assessment are preserved unchanged in `review-provenance/`; the original review is not rewritten. [Detailed dispositions](finding-dispositions.json) bind exact affected cases, payloads, independent receipts and residual limits.

| Finding | Proposed correction and retained boundary |
|---|---|
| 001 / issue1207 | One NBRC1308/1356 stock with both source/author lineages; complete named inputs, unquantified NaOH, water input rather than final volume. Final pH7 does not imply another titrant. |
| 002 | Eleven alias payloads corrected: 23 contextual labels become nonresolving, four preferred labels qualified. Identifying named stocks and tablet-qualified product labels remain resolving. |
| 003 | Exact v2 Merck canonical D-glucose child label retained and independently re-reviewed; old failed checks retained. |
| 004 | Remove untranscribed JCM977 stock Water and aqueous claim; retain literal20%w/v glucose. |
| 005 | Remove inferred Water from six other stocks; preserve literal membership and independently unknown solvent/form/percent/gas/closure facts. |
| 006 | JCM381→379 is positive primary evidence; original body and retrieval time retained. |
| 007 | Complete bounded EBIOS tablet, RM trace-metals, source-specific Oxoid BHI supplement and Sheffield TypeB proposals; unknown SKU/doses/forms/excipients remain unknown. |
| 008 | Four failed receiving pages are failed evidence. Separate MediaDive737/876/955 chains support only their exact contexts; J887 remains an explicit access/applicability hold. |
| 009 | TSY frozen amount correctly described as1000ML_PER_L; unknown formula remains unresolved. |
| 010 | Unsupported ingredient1886→JCM187 bridge removed; KG152 unresolved, genuine JCM187 CM106 link retained. |
| 011 | J240 YNB actual1g distinguished from6.7g in1682/1837; no SKU/formulation inferred from dose. |
| 012 | Seven source-qualified Sheffield TypeA contexts attach to unchanged TypeA proposal; four unqualified DSMZ contexts remain excluded. |

Issue1217 groups002–012 have bounded proposed corrections. Issue1207 group001 has a newly reviewed membership correction. Neither issue is closed by this handoff. The additional EBIOS cross-worker identity overlap was filed **before** its proposal as [issue1221](https://github.com/CultureBotAI/MediaIngredientMech/issues/1221); competing worker01/02/06 uninstalled choices require coordinator reconciliation. No other worker was edited and no maintained owners were merged.

## Independent review and checks

[Review coverage](review-coverage.json) records actual authors, distinct scientific reviewers and exact final case/payload hashes. A authored alias corrections, reviewed by B; B authored product preparations, reviewed by A; C authored membership/source corrections, reviewed by root; root authored the stock membership correction, reviewed by A. Existing author lineages are disclosed. [Sealed-review reading scopes](sealed-review-read-coverage.json) cover all188 original case and100 payload assessments; this is not a claim that this turn repeated fresh primary research for every unchanged case.

Final independent integration review: [C metadata/diff receipt](research-c/final-assembly-review/review-final.json). Scientific reviews and final central binding addenda are hash-listed in the completion receipt. Final publication metadata/native/handoff review is recorded in `research-c/final-assembly-review/publication-review.json` before publication.

Passed gates:

- Complete188-case/evidence/owner binding audit and1,091 capture hashes.
- Strict closed-schema validation of all103 selected payloads.
- Native partonomy on all2,956 baseline records and the isolated3,034-record successor overlay:152 decompositions,1,037 components, zero violations.
- Forty-seven focused positive/negative control pairs for alias identity, source-success classification, literal membership, unsupported bridges and exact context subsets.
- Native review inspect, validate, save and full retained-review check. The exact command exits and full logs are in [native/](native/) and [logs/full-final-v2/](logs/full-final-v2/).
- All1,758 original d5 manifest members and115 v2 members remain byte-identical, including failed checks and native pairs. No existing tracked file changes.

Native batch review: [YAML](../../../../reviews/structured/20261108T064951Z-w06-successor-v3-reconciliation/review.yaml) and [rendered Markdown](../../../../reviews/structured/20261108T064951Z-w06-successor-v3-reconciliation/review.md). Its74 targets are the26 changed proposal entries and48 affected case outcomes, with claims limited as stated. It does not fabricate terminal native predecessor lineage from the private worker03 fixture.

Initial authored candidates, the first central evidence-kind failure, and the independent metadata reviewer's corrected checker assumption remain saved as historical evidence. `assembly-attempt-1/`, B `author-attempt-1/`, original review receipts and old negative-control bindings are not current intake. Final gates use the current selector hashes. The initial `progress.json` is preserved; completion-receipt.json and this handoff describe completion.

## Remaining holds

[Source holds](source-holds.json) are exactly unchanged. [Remaining limits](remaining-holds.json) enumerates every explicit case limitation and all frozen downstream holds;29 cases retain unresolved dispositions. In particular, retain J887 receiving-source verification, ingredient1886 source continuity, unqualified Sheffield contexts, EBIOS cross-worker selection, historical product/lot/SKU distinctions, unspecified solvents/forms/doses/percent bases/gas content and final-volume uncertainty. Full formula uncertainty does not invalidate the bounded product preparations already supplied.

All original captures and retrieval dates remain unchanged. The shared immutable cache supplied no automatic source-case, owner or export approval. The maintained catalogue and all-source duplicate checks are scoped to the actual frozen/current worker inputs and recorded candidates, not an assertion about uninspected remote main.

Coordinator owns final acceptance, guarded integration and export. Worker06 publishes by ordinary commit/push on its assigned branch and then idles; no standalone PR, merge or branch deletion.
