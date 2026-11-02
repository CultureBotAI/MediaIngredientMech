Approved-plan Step 7(a) starts from merged main `61ff4ed4789e61ef64f6f75a792adf3b934e7c82` on a new isolated branch. The explicit no-unified-snapshot constraint makes this a source-only correction; this issue will remain open for the published snapshot debt and the broader cross-prefix policy.

Remove only the reviewed stale `kg_microbe_node_id` field and append an accurate curation event for these six owners:

| Owner | Pointer to remove |
|---|---|
| Casamino_Acids | CHEBI:78020 |
| Casein | CHEBI:3448 |
| 02_Thiamine_Pyrophosphate | CHEBI:9532 |
| Fish-sperm_Dna | CHEBI:16991 |
| Bacto_Soytone | CHEBI:8150 |
| Deoxyribonucleic_Acid_From_Herring_Sperm | CHEBI:16991 |

The owner histories and archived primary term responses support these removals: the current identities were already corrected, the stock and fish-source records retain their distinct local identities, and rejected records retain their current status and pointers. Preserve primary IDs, ontology mappings, chemistry, aliases, counts, role assertions, historical events and existing tombstone metadata. Do not invent a representative where none exists.

The schema explicitly permits the identifier scheme actually used by a KG node. Accordingly, add a recurrence guard for the five reviewed stale identity/node pairs covering these six owners, with regression tests; do not turn every unequal prefix into a scientific error or invent an exception allowlist.

Keep the unified TSV, its provenance and rejection ledger byte-identical. The current snapshot still contains 21 affected identity cells in 15 unique rows across the four published owner families. Adding the proposed rejection-ledger entries without rebuilding would fail the native rejection check; the approved snapshot ban takes precedence over that broader proposed remedy. Source cleanup will not be reported as removal of those published assertions.

Use the guarded writer, native synchronization and exports, an approval-free mapping/owner receipt, the full review chain and `just qc`. Preserve the existing five WITHHOLD mapping decisions for these source owners and the deferred #912 alias obligations. A fresh independent review and successful PR/merge-group checks remain required before the authorized squash merge.
