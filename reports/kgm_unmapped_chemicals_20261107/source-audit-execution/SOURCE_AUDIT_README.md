# KG-Microbe chemical source audit, 2026-11-07

This is a read-only source audit and lexical reconciliation. It does not approve an identity, clear a release hold, replace downstream mappings, or rebuild KG-Microbe.

The authoritative source pack is `source-manifest.json` plus its 95 exact file members. The prior manifest is preserved as `source-manifest-v1.json`; its membership predates the MicrobeDecoder source-assertion proof. All 68 upstream snapshot files were rechecked byte-for-byte; the separate raw CSV and large graph hashes are recorded in their proof receipts. `merged_graph_stats.yaml` was already changed in the active KG checkout and was left alone.

## Current queues

- MediaDive: all 415 source-owned ingredient IDs retained, including the native helper's 410 output rows, four context-free lookup recoveries, and blank ID 1944. A lookup recovery is not scientific resolution. The helper's occurrences value is constant 1, not measured recipe frequency. All raw names come from the admitted compounds generation; 44 differ from transformed names.
- MicrobeDecoder: all 10 compound placeholders, including eight below the old threshold of 10, derived with the native helper's `--prefix compound --min-occurrences 0`. The two sugar IDs remain separate. The complete native policy table contains 240 rows; the exact 10 queue IDs select 225 unresolved material uses, independently matched to 225 graph assertions and 220 full original CSV records. Predicate, relation, source field/token/citation, record hash and identity-approved-false evidence are preserved.
- Other current chemical placeholders: 82 metatraits and 42 metatraits_gtdb nodes, with streamed graph incident-edge counts. The historical 122-row metatraits queue is not treated as current. Mixed trait/taxon and other association diagnostics are retained separately.

The ignored-inclusive filename search found no `missing_chem*` artifacts in this checkout. It included hidden/ignored files but did not follow external symlink directories. The exact command and all results are saved.

## Consumed reviewed export

The installed supported input equals the official MIM 0dac278466699129a083343a921c2e0ca18a9ab4 reviewed export: 1,739 supported rows and 1,275 losslessly withheld rows from 3,014 canonical mappings. All four partition artifacts, acquisition/reproduction/promotion receipts, and the exact unified gzip matching input are snapshotted. `PASS_SUPPORTED_SUBSET` is not a full-corpus scientific pass. The admission/launch receipts do not assert completion of the subsequently running downstream validation.

## Native execution boundaries

Both native queue helpers ran under the existing KG Python 3.10 environment with bytecode writes disabled and an audit wrapper that allowed writes only in this source-audit directory. The MediaDive import attempted one socket bind, which the wrapper denied; no network call or upstream write was allowed. Source modules, dependency hashes, runtime information, exact arguments, allowed output paths and denied events are retained. No paid provider was used.

## Reconciliation artifacts

`reconciliation-before-v3` is the corrected baseline report, using the original clean MIM main root and the relocated source pack under this worktree's reports directory. It validates the current native companion before reporting dispositions, checks the consumed partition internally, matches raw/transformed names by exact casefold only, and retains every source ID/category. Its 2,956 records are the direct mapped/unmapped YAML files, including ignored direct files, excluding nested historical backups.

`reconciliation-before-v1.log` preserves an initial exact-witness refusal against the broader 240-row policy table. Selection was corrected to the queue's exact source IDs, retaining the full table. `reconciliation-before-v2` is a superseded diagnostic that included six nested historical backups; issue #1152 documents the corrected inventory rule. Neither earlier result is the final corpus assessment. No source file was cleaned up or deleted.

Counts of triage flags overlap. Supported lexical coverage does not establish scientific identity and never overrides an owner WITHHOLD decision or a downstream hold. Specific scientific dispositions and source curation are supplied by the separate scientific review, not inferred by this script.
