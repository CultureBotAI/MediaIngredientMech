# Complete mapping disposition review

Issue [#729](https://github.com/CultureBotAI/MediaIngredientMech/issues/729)
finalizes the standalone MIM SSSOM. Every source row has an explicit disposition:
1,740 supported and 1,246 withheld, out of 2,986. Unsupported claims remain in a
separate, lossless SSSOM backlog, as requested. Completing disposition coverage
does not mean every source mapping has been scientifically approved.

- `baseline-mapping-review.json` preserves the prior source rows and decisions.
- `mapping_review/` contains the complete remaining-cohort reviews, original
  hashed report text, live issue intersections, changed-owner decisions and
  adversarial findings. Whole-record role/component concerns do not imply a
  mapping failure or a mapping approval.
- `trait_synonyms/` records the source correction for all 46 trait phrases in
  39 records, preserving their text and provenance as `REJECTED_LABEL`.
- `trait-synonym-refresh.json` verifies the bounded synonym-only output change
  against the pinned Claw producer. All other source row fields are unchanged.
- `mapping_changes/` holds one receipt per verified mapping-change batch
  (re-anchored parents, regrades, later re-groundings, merges, mints), in
  `sequence` order after the two synonym refreshes. A receipt records the
  SSSOM digest before and after, every owner record's before/after YAML hash
  with the curator's verification, every changed/added/removed row with both
  positions, and a position map so the position-keyed cohorts and holds carry
  forward. It is a link, not an approval: every row it touches is withheld
  until a mapping-specific review approves the corrected mapping, and every
  owner it touches loses the byte-identical carry-forward. `make_receipt.py`
  writes one from a mutator's apply log.
- `record_refreshes/` holds audit-only section-refresh receipts
  (`src/mediaingredientmech/record_refresh.py`, written by
  `scripts/make_record_refresh_receipt.py`). They document bounded
  `occurrence_statistics` or `causal_graphs` changes and their curation events.
  Verification can reconstruct the earlier bytes for audit, but no receipt
  preserves an approval or advances the reviewed baseline. **Any changed record
  bytes require fresh approval**, including counts, graphs, formatting and
  curation history. Historical receipts remain readable. The assembler,
  semantic review builder, follow-ups and release holds bind exact bytes.
- `mapping-evidence.json` and `review.json` bind all final decisions to current
  sources. `assemble_review.py --check` reproduces the decisions and negative
  overrides without accepting refreshed source hashes as scientific approval.

When #731 finalized this review, compared with the earlier 1,603-row supported
release, 1,510 approvals remained, 253 rows gained a mapping-specific approval,
and 93 prior approvals were withheld after stricter scope and alias review. The
mapping-change receipts since then account for the difference from the totals
above. The earlier published release remains a historical snapshot; these
decisions supersede it for current SSSOM use.

The complete source SSSOM SHA-256 is
`68552edd452d5dccf1262b5d03190a6b668341952a554f349149f269403cca67`.
The original negative aromatic-compound review (#724/#725) is retained, with a
separate, exact source-correction resolution. Removing a hold or rehashing its
old payload cannot release that unsupported claim.

Receipt `issue669-1003-scoped-alias-corrections` records nine changed rows across
eight owners, with no added or removed rows and every source position retained.
The changed carnitine hydrochloride owner withdraws one prior registry-row
approval; the remaining corrected rows were already withheld. The unresolved
historical `DL-carnitine` alias stays withheld, without new identity support.
The proposed melezitose correction was blocked by the existing approval pin
and restored to its original bytes; its unpublished evidence is retained under
`reports/sssom_scientific_curation_20261101/audit901/blocked-proposal/` pending
the native supersession mechanism in PR #764.

Receipt `issue875-ncit-exact-heptahydrate` changes one mapping to the exact
NCIT:C61946 heptahydrate identity and removes its obsolete local registry row.
The corrected row remains withheld; all unrelated SSSOM bytes are preserved.
The chemistry and BUFFER findings remain open.

Native semantic integrity passes, while the complete graph remains FAIL with
1,733 blocking findings and 2,271 blocking assertions. The assertion ledger's
2,986 mapping-source hashes bind the changed canonical table; they are not new
scientific approvals or cleared backlog findings.

Adversarial review [#730](https://github.com/CultureBotAI/MediaIngredientMech/issues/730)
identified relation-strengthening errors, formula/catalog and preparation-alias
overclaims, an owner-resolution bypass, historical-payload tampering and export
integrity failures. Known unsafe mappings are withheld; regression tests cover
the integrity failures. This is agent-assisted evidence review, not human
curator sign-off or new experimental evidence.

See [the release guide](../../docs/SSSOM_RELEASE.md) for use and validation.
