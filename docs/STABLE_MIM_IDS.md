# Permanent ingredient IDs and consumer migration

[Issue #1265](https://github.com/CultureBotAI/MediaIngredientMech/issues/1265)
introduces a permanent `mim_id` for every ingredient, including unmapped and
mapping-rejected records. The format is `MIM:0000001`: an opaque, positive,
seven-digit number allocated once. It is separate from `identifier`, which
retains the existing external, registry or unresolved mapping value, and from
the evidence-bearing `ontology_mapping` object.

Existing filenames are retained. Labels, ontology corrections, and moves between
`mapped/` and `unmapped/` do not change the permanent ID. Historical filename
CURIEs and original mapping/placeholder identifiers survive in
`legacy_identifiers`; they are not discarded during the migration. Shared
external aliases are allowed, but record lookup refuses ambiguous matches.

The five historical `data/curated/unmapped_*.yaml` category snapshots
`unmapped_placeholder`, `unmapped_incomplete_formula`, `unmapped_other`,
`unmapped_complex_media` and `unmapped_already_mapped` contain 85 archival
entries. They remain frozen pre-ID snapshots, not additional current ingredients
or a source of new IDs. Only the maintained `mapped_ingredients.yaml` and
`unmapped_ingredients.yaml` aggregates mirror the current per-record inventory.
Preserve the archival bytes rather than silently modernizing their identity
claims.

## Allocation and lifecycle

The initial allocator sorts exact repository-relative record paths before
assigning the sequence. Paths are only the initial deterministic ordering input,
not part of permanent identity. Existing IDs are preserved on subsequent plans.

`data/ids/mim_id_registry.tsv` has immutable mint rows with `mim_id`,
`label_at_minting`, `minted_on`, `status: active` and an empty `replaced_by`.
`data/ids/mim_id_lifecycle.tsv` appends terminal events with `mim_id`, `status`,
`replaced_by`, `changed_at` and `reason`. A retired or merged ID stays registered;
its replacement chain must end at an active record. IDs and events are never
removed or reused. Mint status is independent of scientific mapping status.

Use `stable_ids.allocate_ids` and `stable_ids.append_lifecycle` to plan changes
under the repository's short native write lock. These APIs validate and return
data; they do not acquire locks or write files. Re-read the latest ledgers under
that lock, stage ledger and record updates together through the native validated
writer workflow, validate the complete candidate, and synchronize individual and
aggregate records. Keep the allocation within the same reviewed commit batch.
See [identifier management](../.claude/skills/manage-identifiers/SKILL.md).

`just qc-stable-ids` checks the current inventory. CI also invokes
`scripts/validate_stable_ids.py` with `--require-history --base` and an explicit
trusted ancestor SHA. It rejects changed earlier registry/event rows, reused or
duplicate IDs, unregistered record IDs, missing active records and invalid
replacement chains. The normal schema, scientific review, mapping and artifact
checks remain required.

## Public resolution

The `MIM:` prefix is
`https://culturebotai.github.io/MediaIngredientMech/ingredient/MIM_`.
The Pages builder emits `ingredient/MIM_0000001/index.html` and finds the active
record from its ID at build time. A label, filename or directory change therefore
updates the destination without changing the resolver route. Tombstone pages
retain retired/merged IDs, their original mint labels and replacement links.
Current filename-based detail pages remain available as well.

Registry and lifecycle bytes are inputs to site freshness; resolver content and
page hashes are checked before promotion. Browser rows carry the permanent ID in
`record_id`, retain the mapping value in `id`, and publish `stable_url` separately
from the existing `detail_page` URL. Neither a passing local build nor a source
commit claims that Pages deployment has already completed. A future w3id alias
requires its own approval.

## Consumer impact and order

| Consumer | Required adaptation and limits |
| --- | --- |
| EdgeMech adapter, [#1147](https://github.com/CultureBotAI/MediaIngredientMech/pull/1147) | The original adapter PR has merged. Wait for #1265 to merge, then prepare a separately reviewed follow-up that re-pins the shared contract and updates its projected subject and dependency inventory to use `mim_id`. Preserve native mapping payloads, review evidence and older immutable receipts. Stable identity does not turn withheld mappings into supported ones. The follow-up merge remains a separate decision. |
| CultureMech recipe references | Existing external/placeholder values remain aliases. Resolve them against a pinned current MIM corpus; shared aliases require explicit record context. New record references should retain the permanent MIM ID plus separately relevant mapping evidence. This PR does not rewrite CultureMech. |
| KG-Microbe | New graph and mapping inputs join on permanent MIM IDs. Consume the changed prefix expansion and revised publication manifests, preserving old release provenance. Scoped companion consumers must support and replay the declared `identity-projection-v1` capability; older consumers must refuse it rather than drop the proof. Do not merge records or replace a specific form with a broader ontology term merely because an alias is shared. |
| SSSOM | New subject IDs come from `mim_id`; object identifiers and predicates retain their scientific meanings. Registry/identity mapping targets remain external/local mapping values and are no longer derived from the MIM subject's suffix. Consumers that split a subject into a filename or mapping slug must migrate. |
| Browser, Pages and CURIE lookup | Use the stable ID/URL for new links; use `CurieNormalizer.resolve()` for known unambiguous legacy aliases and lifecycle replacement chains. Unknown MIM IDs and ambiguous legacy references fail closed; syntax checks on an external CURIE do not establish ontology existence. |

Land the ID migration before the adapter's revised export is considered. Review
the regenerated SSSOM, KGX, browser and Pages artifacts against the same corpus;
coordinate downstream adoption separately. Do not rewrite old evidence to imply
that its earlier source already used the new IDs. Minting IDs, resolving aliases
and producing transport artifacts create no new scientific approvals.
