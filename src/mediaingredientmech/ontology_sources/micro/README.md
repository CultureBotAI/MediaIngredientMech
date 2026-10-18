# Reviewed MICRO source

Copied from the user's local KG-Microbe checkout on 2026-09-23. The manifest
records original paths, modification dates, row counts and SHA-256 hashes.
The files are packaged so verification works in a clean checkout and wheel.

* `micro_nodes.tsv` and `micro_edges.tsv` are byte-for-byte copies of the current
  ontology subset (90 nodes, 89 edges).
* `legacy_nodes.tsv` preserves the complete cells of the three reviewed classes
  and their three parents from the archived full ontology nodes. Its original
  full-file hash is recorded separately from the extract hash. The archived
  edge table contains no edges for these three classes; parent evidence comes
  from the current edge table.

| KG-Microbe identifier | Source label | Current source parent |
| --- | --- | --- |
| MICRO:0002393 | Proteose Peptone No. 2 | MICRO:0000180 |
| MICRO:0002392 | rabbit serum | MICRO:0001236 |
| MICRO:0002250 | V-8 juice | MICRO:0000167 |

Both node snapshots contain these exact labels. The archived IDs are
`OBO:MicrO.owl/MICRO_0002393`, `OBO:MicrO.owl/MICRO_0002392`, and
`OBO:MicrO.owl/MICRO_0002250`. Their legacy IRIs are retained in the manifest.
No source description is supplied for these three classes. The current source
has no CAS xref for them. We do not infer a CAS RN from an ancestor, a similar
material, or a broad mapping.

Only `reviewed_terms` admits new identifiers. Existence in this source is not
itself approval of every ingredient mapping, role, synonym, or product variant.
The three ingredient mappings receive separate, complete-row reviews in
`reports/sssom_completion_20260921/mapping_review/kgmicrobe-followup.json`.
