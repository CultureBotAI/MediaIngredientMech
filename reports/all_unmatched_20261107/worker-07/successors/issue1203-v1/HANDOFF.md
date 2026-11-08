# Worker07 issue1203 successor handoff

All17 frozen occurrences have an explicit independently reviewed outcome: six7.5g/L stocks, six350g/L stocks and five heptahydrate solute components. CHEBI:31795 is preserved. The global pure-owner RAW_TEXT alias proposal is withdrawn.

The published be2f4c36d3d4ed79aabe29401c555ae3fd65d7b0 bundle is unchanged. Use this successor’s decisions.json/evidence.json/proposals.json together with occurrence-dispositions.json and supersession.json. The remaining186 decisions and98 proposals are inherited unchanged, not newly scientifically approved.

The7.5g/L proposal reuses C-P08’s registry identity; the350g/L proposal is distinct after an ignored-inclusive search of the catalogue and all ten campaign report roots. The complete isolated payloads are proposed_owners/stock-7p5g-L-v2.yaml and proposed_owners/stock-350g-L.yaml. Both retain UNKNOWN composition completeness because stock solvent/preparation is unreported. The earlier stock-7p5g-L.yaml is a superseded draft retained as evidence, not a current candidate.

| Frozen recipe | DSMZ context | Material disposition | Quantity/preparation limit |
|---|---|---|---|
| CultureMech:001268 | 1845 | CHEBI:31795 solute component | mixedbasalstock denominator |
| CultureMech:001070 | 1593 | 7.5g/L nominal stock | stock solvent and preparation |
| CultureMech:001157 | 1673 | 350g/L nominal stock | stock solvent and preparation |
| CultureMech:001159 | 1677 | 350g/L nominal stock | stock solvent and preparation; dose and final-medium concentration |
| CultureMech:001160 | 1678 | 350g/L nominal stock | stock solvent and preparation; dose and final-medium concentration |
| CultureMech:001069 | 1592 | 7.5g/L nominal stock | stock solvent and preparation |
| CultureMech:001071 | 1593a | 7.5g/L nominal stock | stock solvent and preparation |
| CultureMech:001251 | 1818 | CHEBI:31795 solute component | No missing identity evidence; see explicit source normalization |
| CultureMech:014409 | 1592 | 7.5g/L nominal stock | stock solvent and preparation |
| CultureMech:014591 | 1593 | 7.5g/L nominal stock | stock solvent and preparation |
| CultureMech:014626 | 1673 | 350g/L nominal stock | stock solvent and preparation |
| CultureMech:014628 | 1677 | 350g/L nominal stock | stock solvent and preparation; dose and final-medium concentration |
| CultureMech:014629 | 1678 | 350g/L nominal stock | stock solvent and preparation; dose and final-medium concentration |
| CultureMech:014959 | 1593a | 7.5g/L nominal stock | stock solvent and preparation |
| CultureMech:014988 | 1818 | CHEBI:31795 solute component | No missing identity evidence; see explicit source normalization |
| CultureMech:015035 | 1845 | CHEBI:31795 solute component | mixedbasalstock denominator |
| CultureMech:015915 | 1897 | CHEBI:31795 solute component | No missing identity evidence; see explicit source normalization |

Final description correction is independently reviewed in review/independent-description-correction-v1.json; description-correction-supersession.json preserves the prior intermediate ledger/handoff bytes and explains the fourth stale1845 description.

Independent reviewer: /root/mg_independent_reviewer, different from /root/mg_occurrence_author, /root/mg_stock_dedup and /root. Science receipt: review/independent-science-review-v1.json; native attachment receipt: review/independent-native-attachment-review-v1.json. Actual scopes are published in subagent-scopes.json. Final inventory/diff review is recorded separately.

Validation passed: whole-shard binding188/188, all100 isolated proposal schemas, exact17 occurrence bindings with five adversarial controls, native whole-catalogue partonomy, current pure-owner schema, and preserved maintained baseline. Native review inspect/validate/save/check passed. Native report: reviews/structured/20261108T060949Z-worker07-issue1203-stock-scope/review.yaml and review.md; one actual owner, pass_with_limitations, zero new native findings. It does not supersede the other76 owners or five open findings in the preceding native report.

Remaining blockers:

- Both nominal stocks: solvent identity/amount and preparation convention remain unreported. UNKNOWN component-list completeness; no exact equivalence of unreported preparation details.
- DSMZ1677/MediaDive5781 and DSMZ1678/MediaDive5782 disagree on dispensing units or derived dose fields. Four exact CM occurrences retain sourcequantity/final-medium conversion holds;350g/L stock identity is settled.
- DSMZ1845/MediaDive6448 omits the20x mixedbasalstock final volume. Two exact CM component occurrences retain denominator/finaldose holds;7g heptahydrate component identity is settled.
- Coordinator integration and native publication review remain necessary; existing Mgso4_X_7_H2o WITHHOLD row1888 and all unrelated source/owner holds remain unchanged.

Already settled integration requirements (no further evidence needed): source-qualified stock routing,1818’s0.1g/500mL normalization, and1845’s nested mixed-stock component hierarchy. Source edits and coordinator integration are outside this worker’s authorized write scope. The four inherited source descriptions are superseded descriptions, not current support.

| Ledger | Current SHA256 | Superseded SHA256 |
|---|---|---|
| decisions.json | `7106e1646f83cc1779cd24b6d1185c82afb3d00f0ff1fb2cd4930fe67a76cae8` | `3c6b0f91601c80d59b7b36dbc624eb5399464a5d071c0ebcb98f8643bbbedae7` |
| evidence.json | `c40a837baf4ddfd75ea6ac5c5e44a4381de9616e7ad894d9b22a3690caf211e4` | `7d23421abae7f3908d0c44ea142b39a51d237c04980270a40e3becb457702a06` |
| proposals.json | `9ac4fb31e9116535336ba5d68953cdf1338098c531638107bcce31b74f1c3f1d` | `4a0b7f0f59161df72dd1c163d158a4250b6c13da735788d99baff32c4294663b` |

Publication: ordinary commit and non-force push on review/all-unmatched-w07-source-review-20261107. Resolve the commit containing this handoff with git log; the final coordinator message and private publication receipt record the exact verified remote head. Coordinator alone integrates. No PR or merge. Worker idles after publication.
