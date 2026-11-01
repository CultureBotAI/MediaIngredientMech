# PR 1007 adversarial-review fixes

This follow-up starts at `612860e467aff74ecc1339df7c3c32b1bf940b95` on the
existing PR branch. It preserves prior scientific evidence, receipts 1–14,
both historical companion-review directories, and all earlier structured
reviews. New evidence is appended. No other PR branch is modified, and no
merge, cycle transition or paid research is performed.

| Issue | Final change and regression |
| --- | --- |
| [#1012](https://github.com/CultureBotAI/MediaIngredientMech/issues/1012) | Refresh fixtures derive and deliberately modify header/row dates rather than replacing the live `2026-11-01` string. A real CLI succession test also advances a valid fixture by 400 days. Invalid and stale-date checks must still fail for their intended reasons. |
| [#1013](https://github.com/CultureBotAI/MediaIngredientMech/issues/1013) | Maintained `scripts/refresh_unchanged_cohort.py` delegates to `mediaingredientmech.ingredient_bundle_refresh`. Baseline, prior review and all three outputs are explicit arguments. The native proof is replayed across different Git commits and prior/successor paths. Selected owner, claim, decision, evidence and semantic changes still fail closed. Historical report-local helpers remain historical evidence, not the current command. |
| [#1014](https://github.com/CultureBotAI/MediaIngredientMech/issues/1014) | Restore the complete original `source` cells on both carnitine rows and the original #390 comment. A bounded guarded writer verifies the exact prior receipt, owner bytes and input digest. Tests prove that only source/comment cells change, rejected aliases stay rejected, dates survive, ambiguous preimages fail, and the scientific patch remains nine rows. |
| [#1015](https://github.com/CultureBotAI/MediaIngredientMech/issues/1015) | The seven-alias writer exclusively reserves its receipt and both backups through the shared helper before source mutation. Tests cover collisions at all three opens, concurrent creation, rollback, prior-file preservation and flushed backups. Default YAML callers remain compatible. |
| [#1016](https://github.com/CultureBotAI/MediaIngredientMech/issues/1016) | Actual symlink-directory aliases are exercised through the maintained CLI and writer; duplicate resolved destinations fail before reading inputs or writing evidence. |
| [#1017](https://github.com/CultureBotAI/MediaIngredientMech/issues/1017) | The assembler records both applicable `synonym_correction` and `mapping_change` bases independently of disposition precedence. An isolated complete-assembler regression covers both, each alone and neither. Rows 184, 901 and 2528 retain the original parent-name-refresh basis alongside the later correction. |
| [#1018](https://github.com/CultureBotAI/MediaIngredientMech/issues/1018) | Fresh independent review reproduced reservation replacement races in both writers. The bundle publisher retains exclusive handles, checks device/inode identities and never reopens output names for writing. The shared helper checks identities before yielding; rollback removes only still-owned entries while handles remain open. Injected symlink/replacement and successful/failed late-reservation probes preserve competing evidence and prevent source mutation. |

## Canonical scope and provenance choice

The canonical SSSOM remains **2,987 rows**, with exactly nine changed positions
relative to the PR's original base `4625afd492b6cf43e3b499d1425d2453d490009d`:
184, 258, 535, 648, 649, 901, 1728, 2528 and 2588. No row is added, deleted or
repositioned. All 2,978 other payloads remain identical.

- Seven rows change only `other`, removing the seven previously reviewed false
  aliases. Their mapping dates, source tokens and comments are unchanged.
- Carnitine parent row 648 changes only `other` and `mapping_date` relative to
  the original base. The carnitinamide label remains excluded; the unresolved
  `DL-carnitine` token remains. The historical source vocabulary and #390
  predicate-reconciliation comment are restored exactly.
- Carnitine registry row 649 changes only `mapping_date` relative to the
  original base. Its historical source tokens are restored exactly.

**Choice for #1014:** retain the original source vocabulary. The alias
correction does not replace the historical mapping inputs or the #390
predicate decision. The new curation provenance is recorded by the YAML
history and append-only receipts; it does not require rewriting the published
source vocabulary or inserting an unavailable manifest reference. The raw
Claw diagnostic remains separate and unpromoted. No Claw source change or
new ingredient-generation run was necessary for this metadata restoration.

The unchanged 2,980-row raw diagnostic is still not promoted. Against the
restored canonical provenance it would change 2,365 payloads, remove ten rows
and add three; 1,329 currently supported payloads would change. These counts
are recomputed for this follow-up rather than copied from the initial report.

The guarded restoration appends native
[receipt 15](../../sssom_completion_20260921/mapping_changes/issue1014-provenance-restoration.json).
It changes two rows from the previous PR head without granting approval.
The canonical SHA256 is
`a2b83ccdcaad67d89943ccf0f0e30d796cdbc5e418ead247313631b713e89722`;
the completed review SHA256 is
`36a22b230bd9bc4c82a1816438d21e28a0aa2fcf21f21e63cd30b6459bb8d23c`.

## Explicit review-policy answers

**Row 649 is not meant to be automatically re-approved through PR #764.**
That PR makes obsolete content-bound approvals supersedable; its documented
behavior withdraws superseded approval rather than granting a new one. Row 649
remains WITHHOLD because its owner changed. Restoring support requires a
separate mapping-specific scientific review bound to the current owner and
complete row. This PR neither implements that approval nor changes PR #764.

**The seven unchanged mapping dates are intentional.** These are generated
synonym-only removals: no owner YAML, target, predicate, grounding or historical
mapping-date claim changes. The correction's execution time belongs in its
auditable receipt. Keeping the original dates avoids presenting the cleanup
as a fresh mapping review. The set header remains aligned with the newest
actual row date, 2026-11-01, under Rule G.

Every disposition remains **1,740 SUPPORTED / 1,247 WITHHOLD**. Both carnitine
rows remain withheld. Semantic integrity passes; the complete scientific
release still fails with **1,733 findings and 2,272 assertions**. No role,
component, identity or withheld mapping approval is inferred from these fixes.

## Reusable companion refresh and validation

The maintained CLI creates a new
[companion successor](../../ingredient_bundle_20261101_followup/README.md)
from the previous PR head and prior companion. All 51 claims, 20 owners,
selected complete mapping rows and scientific decisions/evidence remain
identical. The new review binds the revised global containers without
overwriting historical review bytes. Future refreshes use explicit arguments
documented in [the current command guide](../../../docs/INGREDIENT_BUNDLE.md);
they do not automatically accept changed scientific claims or update CI pins.

The receipt chain was replayed through the complete graph, completed mapping
review, semantic ledger, supported KGX and reviewed SSSOM exporters and their
validators. The supported graph retains 1,740 mappings and 2,220 approved
edges; 2,272 excluded assertions remain in its separate backlog. The semantic
disposition table rebinds mapping assertions to the new whole-file source
digest; that is not a new scientific review of every mapping.

Exact commands, exit codes, input/output hashes and retained failing regression
probes are in the adjacent `checks/` evidence and the companion report.
The full suite completed with **3,276 passed, six skipped**. Maintained-package
coverage is **71%**, above the 35% floor. Full `just qc`, Ruff, Black and mypy
pass. The final annotated refresh producer separately passes all 82 bundle
tests and reproduces the successor bytes; the evidence records the annotation
timing during the broad run rather than rebinding earlier producer hashes.
Independent final-head review is published on PR #1007 after the final commit;
this report is an implementation record, not an independent approval.

The protected `qc-evidence.yaml`, unified mapping, cycle profile and shared
Claw checkout are untouched. Native generated aggregate/export/review paths
can overlap other PRs at the file level; none of their individual ingredient
edits or approval-supersession implementations is included here.
