# Case-review integration and unified snapshot refresh

This integrates PR #754 with main at `dfce1c93` and resolves the existing
snapshot drift under #700. Published historical releases remain unchanged.

The three unmerged case-correction receipts are replayed after main's
`issue669-704-rulings` receipt. Each original before/after row is checked
byte-for-content against the replay; all 48 corrections retain their original
payloads and owner/evidence reviews. The receipts record their original commit
and hash. Main's published receipt is unchanged. The merged SSSOM has 2,999 rows:
1,747 supported and 1,252 withheld. The supported mapping selection is unchanged;
the three additional main-branch assertions remain withheld.

## Unified snapshot

Rebuilt with clean pinned checkouts:

- Claw: `2637172e6fdbfacf163f0b12d289a9828dda2f30`.
- CultureMech: `faaf033b8c5386aaf2cb6f28fc527678d00cf83b`.
- MIM: the reconciled ingredient records bound by
  `UNIFIED_INGREDIENT_MAPPING.provenance.json` and the review receipts.

The generated artifact retains all 3,870 row names, occurrence counts and
example-media references. There are 393 changed rows: 387 synonym cells and
100 primary MIM identifier cells, with associated chemical/registry/source
columns reflecting the current records and builder rejection policy. Full
cell changes are preserved in `unified-snapshot-diff.json`.

The independent owner audit checks all 2,610 resolved rows against the current
MIM records: every identifier has an owner, every MAPPED claim has a mapped
owner, every supplied CAS agrees with an owning record, and no owner's rejected
synonym reappears. There are zero violations. The rejected-identifier gate
passes; wrong-compound synonym probes no longer occur as active tokens. Valid
cadmium-nitrate tetrahydrate synonyms remain on their own compound.

The pinned builder's five unified-mapping regression files pass (66 tests).
Generated curated/browser collections and current review artifacts are rebuilt.
The supported KGX export and both supported/withheld native SSSOM schema checks
pass. This work repairs a generated MIM snapshot; KG-Microbe release promotion
and its existing coverage gate remain separate.

## Reproduction

Use the pinned Claw and CultureMech revisions above, then set
`CULTUREMECH_ROOT` and `MEDIAINGREDIENTMECH_ROOT` to those checkouts and run
Claw's `scripts/build_unified_ingredient_mapping.py --culturemech <path>
--mim <path> --output UNIFIED_INGREDIENT_MAPPING.tsv --format tsv`.
Run MIM's `scripts/check_unified_rejections.py` before
`scripts/check_unified_freshness.py --stamp`.

`receipt-replay.json` binds the original and replayed receipt digests;
`unified-owner-audit.json` binds the owner audit to the regenerated artifact.
