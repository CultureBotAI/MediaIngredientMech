The first actual stable-ID campaign canary cannot produce a candidate from the current, verified adopted corpus because its captured canonical compatibility table still contains a known obsolete opposing-namespace row.

Actual native invocation:
- MIM target head `6677f1e1679bec82f5af5e125454d4b7852780e9`.
- Claw producer head `c1cbd0f715f2d83d7cb6773797af7651e315454d` (PR #1139).
- Native MIM adoption completed and separately verified `COMPLETE_CURRENT_CANDIDATE`. Application SHA256 `51fdaa147297eb3df8b1a217b5c956619dc6a160be749b9bd3998555bd4f5465`.
- `stable_sssom_publication generate` invoked the actual Claw stable CLI with validation enabled and legacy validation-stamp replay disabled.
- It terminated with exit 1 at `stable_mim.py:115`: `Competing registry namespaces for MIM:0002332`. No canonical files were written.

The actual owner is `data/ingredients/mapped/Sodium_Nitrate_070_M_Stock.yaml`, permanent ID `MIM:0002332`, classified `STOCK_SOLUTION`. Its curated primary and explicit curation history retain `kgmicrobe.ingredient:sodium_nitrate_~28070_m_stock~29`; CHEBI:63005 is a broader solute mapping. The current canonical table also retains the old B1-generated `kgmicrobe.compound:sodium_nitrate_070_m_stock` exact row.

Closed [#684](https://github.com/CultureBotAI/culturebotai-claw/issues/684) already documents this exact historical defect. Its generator repair stopped deriving the opposite namespace; it did not remove the literal old canonical row. [MIM #1257](https://github.com/CultureBotAI/MediaIngredientMech/issues/1257) separately documents preserving unselected canonical rows in the earlier campaign publisher.

The stable compatibility adapter now unions the curated primary with all canonical exact registry objects, then correctly refuses competing namespaces. The publication operator needs a successful generation before it can inspect and independently review an old row as `REMOVE_WITH_HISTORY`. Together these leave no demonstrated path to retire this known historical row through the selected native workflow.

Required outcome:
- Establish and implement the smallest reviewed correction route; do not weaken the competing-namespace refusal, automatically choose a namespace, hand-edit the canonical table, or edit a completed adoption receipt.
- Any exclusion/retirement must bind the complete old row and actual current owner/evidence, preserve the original canonical bytes and provenance, and receive the required independent review. Generating a proposal must not grant scientific or release support.
- Preserve ambiguous-owner and unknown-owner refusals, explicit legacy behavior, legitimate same-namespace aliases (including different, mixed-case and escaped slugs), permanent-ID identity and held cases.
- Add regressions for this real stock, a genuine unresolved namespace conflict, unchanged legitimate compatibility aliases, and altered/unauthorized retirement evidence if a new reviewed input is needed.
- Rerun the native canary only with a reviewed fix and a fresh output path. Keep the failed run immutable; no merges or KG rebuild.

Durable campaign evidence under `.temp/all-unmatched-20261107`:
- `preflight/stable-adoption-real-canary-tc-native-generation-v1/RESULT.json`, SHA256 `8e58cb88a0cc2a9a44ed8f6ce31e7058dd74546c128d7914ff97e9edbd39e04a`.
- Native `FAILED.json` SHA256 `2bc78cf70d428272a0a6600d79449be9ed3281e79048202f77cd341fa6ec0c6d`.
- Native `invocation.json` SHA256 `d555a2ac0446a3f55f207aae9678d53630d04e9a710328d87b8bb35a0ba9e1a3`.
- Native stderr SHA256 `2f20a9113e8333aff4ff13ab17ecf73337ee5d9438271075fc5255c4492f6df7`.

Deduplication: current all-state exact-phrase issue searches in both repositories returned no match; the seven currently open Claw PRs were inspected by title/head. #1139 is the relevant owned implementation. This is a concrete integration finding under #1137, not a claim that the strict refusal itself should be removed.

