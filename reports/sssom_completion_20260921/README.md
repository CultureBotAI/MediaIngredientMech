# Complete mapping disposition review

Issue [#729](https://github.com/CultureBotAI/MediaIngredientMech/issues/729)
finalizes the standalone MIM SSSOM. Every source row has an explicit disposition:
1,763 supported and 1,255 withheld, out of 3,018. Unsupported claims remain in a
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
- `mapping-evidence.json` and `review.json` bind all final decisions to current
  sources. `assemble_review.py --check` reproduces the decisions and negative
  overrides without accepting refreshed source hashes as scientific approval.

Compared with the earlier 1,603-row supported release, 1,510 approvals remain,
253 rows gain a mapping-specific approval, and 93 prior approvals are withheld
after stricter scope and alias review. The earlier published release remains a
historical snapshot; these decisions supersede it for current SSSOM use.

The complete source SSSOM SHA-256 is
`761b7dee1e7eef7ecd999a848f6188fe1a0d394c79a8b53b957c2e477cec9f3f`.
The original negative aromatic-compound review (#724/#725) is retained, with a
separate, exact source-correction resolution. Removing a hold or rehashing its
old payload cannot release that unsupported claim.

Adversarial review [#730](https://github.com/CultureBotAI/MediaIngredientMech/issues/730)
identified relation-strengthening errors, formula/catalog and preparation-alias
overclaims, an owner-resolution bypass, historical-payload tampering and export
integrity failures. Known unsafe mappings are withheld; regression tests cover
the integrity failures. This is agent-assisted evidence review, not human
curator sign-off or new experimental evidence.

See [the release guide](../../docs/SSSOM_RELEASE.md) for use and validation.
