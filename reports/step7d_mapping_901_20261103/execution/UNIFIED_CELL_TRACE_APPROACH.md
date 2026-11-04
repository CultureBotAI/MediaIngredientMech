# Step 7d unified snapshot cell tracing

This is preparation for the reviewed rebuild, not a rebuild, promotion or
approval. No changed output is accepted merely because its owner appears in the
selected cohort.

## Verified starting point

`unified-baseline/comparison.json` records a full native diagnostic at MIM
`467aa319a06ef992035f509f66fe251082b44ae1` and isolated Claw
`3022b8738dcc9e01c7464a8d5c95aa9be2eef141`. Its diagnostic and maintained TSV are
byte-identical, SHA256
`1edaba0f0f2d1afb84129a2ba185963a2cdf3e9b982690fdfd610df1fd78cc88`.
There are 4,170 rows, unchanged order and membership, and zero changed cells.
Thus baseline input drift has zero measured output contribution. It cannot be
used as a blanket explanation for any future changed cell.

The before/after native input inventories and tracked inventories match in
`unified-baseline/stability.json`. The unchanged native producer captured at
`unified-baseline/executed-producer.py` hashes to
`26d0c6808728ddaef5201ccebe24fff8c4174c4a5b37753e79c671a628c521d1`.
The diagnostic uses CultureMech normalized recipes, MIM direct records, MIM
label index and the reviewed rejection ledger. This native command path does
not consume a live KG-Microbe checkout or CommunityMech inputs.

## Freeze the after generation before tracing

Use the unchanged native CLI to an external candidate path after the reviewed
source edits, coupled references and native exports. Capture the actual input
inventory, clean commit context, producer/import hashes, command, TSV and native
provenance sidecar. Compare the new inventory with the baseline inventory. Every
changed native input must be a reviewed source owner, the exact planned ledger
migration, or a reproducible derived label-index change from those records.
The source-plan evidence/history does not justify additional owner changes.
CultureMech and producer/import inputs must be byte-identical to the baseline.

Before accepting a cell report, require identical columns, ingredient names and
order, occurrence counts, examples and mapping statuses. Exporter logic is
unchanged. A membership, status or unexpected input change is a stop for
investigation, not an automatically attributable result.

## Derive an owner trace using the native resolver

Load the before and after indexes with the captured native implementation.
Before indexes must use actual base record bytes and base label index/ledger;
after indexes must use actual reviewed current bytes and current label index/
ledger. Resolve each changed ingredient using the native `build_unified_rows`
path, including source-label rejections, `label_ruling`, retired source IDs,
owner-keyed rejection, `resolve_mim_record` and `_published_ids`.

Do not identify an owner from `mim_id` alone. The producer explicitly documents
that an identifier is not a unique record key. Use the complete source catalogue
and bind the returned native record to the exact source path and whole parsed
record; retain identifier and preferred term as visible evidence. Ambiguous
binding stops tracing. The four reviewed primary identifier promotions are
cerium, copper, D-maltose and sodium carbonate; only the first three have coupled
reference migrations. An identifier change must not be reported as a new owner.

If the selected before/after owner paths differ, preserve both native resolution
traces and explain the specific reviewed alias or identity operation responsible.
Do not classify that as unchanged ownership or silently select a preferred
record. Reject any unreviewed ownership change. The owner-selection code and
thresholds remain untouched.

## Per-cell evidence

For every changed cell save: one-based row position, ingredient name, column,
exact old/new cell, native before/after owner path, owner before/after SHA256,
source receipt group, precise plan operation(s), and relevant native function.
Include the full native before/after row and source term ID, label ruling and
rejection-ledger key used during resolution. Useful column paths are:

| Column | Required direct trace |
| --- | --- |
| `mim_id` | Same owner's reviewed `identifier` operation and native returned identity. |
| `cas_rn` | Same owner's exact `chemical_properties.cas_rn` operation, or a fully explained reviewed native owner-resolution change. |
| `synonyms` | Exact set difference produced by `_identity_ontology_mapping`, `_is_publishable_mim_synonym`, rejection filtering and sorted native serialization; link every added/removed token to its reviewed mapping/alias operation. |
| `chebi_id`, `culturemech_term_id` | Exact native `_published_ids` decision plus any coupled reviewed rejection key; neither a parent mapping nor a changed identifier alone authorizes a guessed cell. |
| `kg_microbe_node_id` | Exact reviewed owner field operation; none may be inferred from ontology identity. If no such operation exists, stop. |

The native loader exposes an ontology label as a synonym only for equivalence
mapping grades. Changing CLOSE_MATCH to NARROW_MATCH therefore removes the
parent ontology label from exported synonyms even when the source synonyms list
is unchanged. That removal must name the exact mapping-quality operation. A
separate accepted source synonym with the same text can still retain that token,
so a label-level assumption is insufficient. The five independent alias fixes
must be traced to their exact REJECTED_LABEL operations.

The unmodified native row builder also applies rejection/nonidentity filters
across its name index; for any cell affected by another record, save that exact
dependency rather than attributing it only to the selected row's owner.

## Completion condition

Save a machine-readable cell report and a TSV, with an explicit
`untraced_cells` list. The allowed result is zero untraced cells and every
changed native input accounted for. Recompute both candidate hashes and verify
the native sidecar's input and output binding. Independent review must compare
the actual committed snapshot pair to this frozen evidence, including all
source and cell traces. No scientific approval, role approval, new mappings,
budget/threshold change or owner merge is inferred from a successful replay.
