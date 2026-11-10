---
name: manage-identifiers
description: Manage permanent MediaIngredientMech record IDs, append-only mint and lifecycle ledgers, and preserved legacy identifiers. Every ingredient has a required opaque mim_id such as MIM:0000001. Its existing identifier remains an ontology, registry or unresolved mapping value. Use for record creation, promotion, rename, merge, retirement and ambiguous legacy-reference resolution.
category: workflow
requires_database: false
requires_internet: false
version: 3.1.0
---

# Identifier management

Every record under `data/ingredients/mapped/` or `data/ingredients/unmapped/`
has a permanent `mim_id`. Mapping status, label corrections, filename changes
and promotion between directories do not change it. Keep existing filenames;
the ID does not derive from them.

Read `MAPPING_SEMANTICS.md` for scientific mapping policy and
`docs/STABLE_MIM_IDS.md` for the migration and consumer contract. The previous
legacy `id` field stays retired; this contract introduces the distinct required
field `mim_id`.

| Field | Purpose |
| --- | --- |
| `mim_id` | Permanent opaque record key, `MIM:` plus seven digits, starting at `MIM:0000001` |
| `identifier` | Existing ontology, registry, local mapping or unresolved placeholder value |
| `ontology_mapping` | Evidence-backed mapping target, grade and provenance |
| `legacy_identifiers` | Preserved former mapping/placeholder values and filename-based MIM aliases |

A permanent record ID establishes no ontology equivalence or scientific review.
Known duplicate mapping values may occur on distinct records; their permanent
MIM IDs remain distinct until a reviewed merge explicitly retires one.

## New records

1. Check the current corpus and aliases for an existing ingredient. An ambiguous
   legacy identifier requires disambiguation; never choose the first record.
2. Resolve and verify the owned repository and acquire its normal short write
   lock. Re-read both ledgers under that lock:
   `data/ids/mim_id_registry.tsv` and `data/ids/mim_id_lifecycle.tsv`.
3. Use `mediaingredientmech.stable_ids.allocate_ids` to plan IDs. Supply current
   registry state and a mapping keyed by exact repository-relative new-record
   paths, with a date in `YYYY-MM-DD` format. It allocates missing IDs in sorted
   path order and preserves existing assignments. It is a pure planner, not a
   writer or lock manager. Never compute a new ID from file counts or invent a
   sequence in a separate script.
4. Assign each planned `mim_id` to its record. Keep the scientifically justified
   `identifier`; preserve previous identifiers and filename CURIEs in
   `legacy_identifiers`. Do not replace an unresolved value with a fabricated
   ontology match. The sibling
   [`map-media-ingredients`](../map-media-ingredients/SKILL.md) skill owns mapping
   curation, and [`merge-ingredients`](../merge-ingredients/SKILL.md) owns merges.
5. Stage the record changes and newly appended registry rows together through
   the native validated writer workflow. Validate the complete candidate corpus
   and ledgers before promotion; do not leave an allocated ID without a record
   or a record without a registered ID. Preserve field order and append a
   `curation_history` event. The allocator alone does not provide an atomic
   multi-file write.
6. Synchronize individual and aggregate records in the correct direction and
   regenerate the affected published artifacts. Run the identity gate and
   applicable native QC before committing the bounded batch.

## Existing records, merges and retirement

Changing a label, mapping value, mapping status or file path retains `mim_id`.
Before replacing `identifier`, preserve the previous value in
`legacy_identifiers` and record the evidence-backed transition in history.
An ingredient with `mapping_status: REJECTED` still has an active permanent ID;
mapping rejection is not ID retirement.

Mint rows are immutable. A reviewed lifecycle change appends one terminal
event using `stable_ids.append_lifecycle`, with a UTC timestamp and a reason
binding the actual curation evidence. Keep the five-column format:

- `merged` or `retired`: one already registered `replaced_by` ID.
- `split`: at least two distinct registered IDs, sorted and separated by `|`.
- `deprecated`: empty `replaced_by`; do not guess a successor.

Never edit the original mint row, delete an old event, reuse an ID or create a
cycle. Whole source/target concept decisions and affected reference provenance
must justify the event; different spellings alone do not establish a split.
Preserve historical records and negative holds in the curation evidence. The
current inventory contains exactly the active IDs, not terminal source IDs.
Transfer aliases only where the scientific decision supports it.

Use `inspect_id`/`inspect_ids` for typed lifecycle context. `resolve_id` raises
`UnresolvedIdError` when a chain reaches a split or deprecation; its resolution
exposes the exact direct successors without choosing a child. This remains true
if split descendants later converge. Address replacement never transfers a
mapping assertion or scientific approval.

## Resolution and checks

`MIM:` expands to
`https://culturebotai.github.io/MediaIngredientMech/ingredient/MIM_`.
The Pages builder creates stable ID routes and retirement/replacement pages,
while retaining current filename-based record pages. A w3id redirect is a
separate future change requiring approval.

`CurieNormalizer.resolve()` reads the registry and current corpus, follows
replacement chains and returns a current permanent ID for an unambiguous
preserved alias. Split/deprecated chains return `SPLIT_SUBJECT` or
`DEPRECATED_SUBJECT`. Shared external aliases remain stored; lookup refuses them
with `AMBIGUOUS_ALIAS`. A mapping identifier is not a unique record address.

Run `just qc-stable-ids` for the current inventory. The supported validator
`scripts/validate_stable_ids.py` accepts `--base` with a full trusted ancestor
commit and `--require-history` to enforce append-only history as CI does.
The gate checks exactly one ID per record, uniqueness, complete active-registry
coverage, immutable earlier rows, and replacement-chain validity. Also run
`just validate-strict`, the native SSSOM and round-trip checks, and Pages/browser
freshness checks appropriate to the batch. Do not alter historical receipts to
make them describe the new identity representation.
