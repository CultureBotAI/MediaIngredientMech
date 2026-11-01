# Exact heptahydrate identity correction (#875)

The approved Step 2 decision replaces the local identity and anhydrous-parent
grounding for `Na2HPO4 x 7 H2O` with exact `NCIT:C61946`, while keeping the
anhydrous `CHEBI:34683` rejected in the unified export. Section 3 step 1 of
`MAPPING_SEMANTICS.md` gives an exact form-specific ontology term precedence over
the CAS fallback. The [approved decision](https://github.com/CultureBotAI/MediaIngredientMech/issues/875#issuecomment-6553802172)
is separate from scientific release approval.

The archived [NCI EVS response](sources/ncit-C61946.json) names “Sodium Phosphate,
Dibasic, Heptahydrate”, marks the term active in NCIt 26.10d, and supplies CAS
7782-85-6, formula `2Na.HO4P.7H2O`, and FDA UNII `70WT22SF4B`. Its
[fetch receipt](sources/ncit-C61946-receipt.json) records the official
[EVS endpoint](https://api-evsrest.nci.nih.gov/api/v1/concept/ncit/C61946?include=full),
access time, and SHA256. The writer checks both the exact response hash and
these identity fields. This is a database assertion, not experimental evidence.

The implementation is authored by Codex (GPT-6), with LLM assistance. No
independent review or positive scientific disposition is asserted here.
The inherited anhydrous InChI/SMILES and provisional BUFFER evidence remain
open. This step does not change chemistry, roles, sibling-form rejections,
accepted hydrate aliases, source occurrence statistics, or a stock solution.
The full older record history and mapping evidence remain intact.

## Guarded execution

Run in the verified isolated Claw runtime, with its packages and this MIM
worktree's `src` on PYTHONPATH and MEDIAINGREDIENTMECH_ROOT set to this worktree.
Run `openclaw-cli config validate` first. The writer itself resolves and checks
the configured Git repository and holds its native repository lock.

```bash
python scripts/promote_heptahydrate_ncit.py sources --log /unique/evidence/source-apply.json
python scripts/promote_heptahydrate_ncit.py sources --log /unique/evidence/source-apply.json --apply
```

Both phases are dry-run by default. The source phase checks frozen owner,
ledger, SSSOM and primary-evidence hashes, including duplicate destination
owners in ignored/nested YAML. It validates the proposed owner through MIM's
native writer and stages only the owner and coupled ledger row in
`ValidatedWriteTransaction`. All receipts and backups are exclusively reserved
before mutation. Every original history event and unrelated ledger line is
preserved. Partial migrations refuse; a complete repeat is a no-op.

The transaction validates every staged output before replacement, replaces
each destination atomically, and records a native recovery journal. A process
or I/O failure between replacements is reported as failure with the prepared
receipt and journal retained; it is not reported as a completed two-file
update. Recovery must inspect those before-images and the actual destination
bytes before retrying. No recovery is automatic.

After source application, run `just sync-curated` and verify that the final
owner bytes still match the source receipt. Generate a native Claw SSSOM
candidate into a separate path, preserving its generation receipt and hash.
The bounded promotion consumes that supplied candidate; its command does not
claim to have generated it.

```bash
python scripts/promote_heptahydrate_ncit.py promote \
  --source-log /unique/evidence/source-apply.json \
  --candidate /unique/evidence/native-candidate.sssom.tsv \
  --candidate-sha256 <verified-candidate-sha256> \
  --log /unique/evidence/mapping-promotion.json
# Inspect the dry-run, then repeat the same arguments with --apply.
```

Promotion verifies the finalized owner/ledger receipt, the before-image, the
candidate hash and the complete expected target row. It replaces the two
obsolete owner rows with one native NCIT exactMatch row, preserves all
unrelated SSSOM row bytes, retains historical source-token lineage, and appends
the new inspected NCI/Codex provenance. Old source tokens remain provenance;
they do not independently verify the new NCIT assertion. The old complete
rows and obsolete registry explanation remain in the before-image and mapping
receipt, not in the active identity columns.

The new row uses its actual curation-history date and the native header-date
helper, retains only the two accepted hydrate aliases and CAS token in
`other`, and carries no inherited ChEBI validation stamp. The old registry row
is removed rather than retained as a competing identity. A repeat with the
same inputs is a no-op.

## Receipts, review and validation

The apply/promotion logs expose the native mapping-change receipt's `records`
shape and exact before/after owner hashes. Root must append a fresh
approval-free mapping-change receipt to the existing chain, using the frozen
SSSOM before-image. Its alignment should contain one changed ontology slot and
one removed registry slot. Preserve every earlier receipt; publication of the
new receipt must use exclusive output reservation. Do not use a section-only
refresh receipt for this identity change.

The mapping remains WITHHOLD. Rebuild the content-bound review chain and
companion refresh through their maintained paths, then obtain a separate
mapping-specific review of the final row, final owner, complete synonym/CAS
payload and evidence hashes. Neither a generated row, the apply receipt,
`mapping_status: MAPPED`, nor a validator pass grants scientific approval.
The broader chemistry/BUFFER finding cannot be retired by this identity fix.

Regenerate exports, indexes, unified snapshot/provenance and current-review
through native commands, retaining Step 1's nine representative tombstones,
zero REJECTED rows with empty mim_id, zero kgmicrobe.compound rows with CHEBI,
and 33 bounded source holds. A stale ledger owner must fail generation.
Existing cross-prefix raw-source publication policy is unchanged.

Focused tests cover paired migration, preserved history, genuine no-op,
partial-state and input-drift refusal, output collisions (including symlinks),
candidate/receipt binding, native journal integration, row/source/date scope,
and all three published hydrate spellings. The committed-surface regression is
expected to fail until root applies and regenerates the production surfaces.
Run those tests again afterward, the full native QC/receipt/review gates, and
an independent final-head adversarial review before queueing the PR.
