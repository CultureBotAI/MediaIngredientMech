# Stable ingredient identity migration (#1265)

This is an identity migration, not new scientific review. It assigns all 2,956
current ingredients permanent `MIM:` IDs in sorted repository-relative path order
from source `0dac278466699129a083343a921c2e0ca18a9ab4`. Filenames remain unchanged.
The immutable mint ledger and append-only lifecycle ledger are under `data/ids/`.
The recorded timestamp, per-record before/after hashes, aliases and SSSOM hashes
are in `migration.json`; every former mapping/placeholder identifier survives.

`identity_projection.py` replays the full before/after corpus and SSSOM and
permits only the dedicated identity fields, one exact mint history event, and
the corresponding SSSOM subject/prefix projection. The complete pre-mint
inventory independently binds all 2,956 path/hash/label assignments. Portable
companion proofs cannot choose a different starting ID or fabricate the mint
order by rehashing their own manifest. Duplicate YAML keys are refused.

Original scientific reports and receipts retain their original bytes. The
`historical-companion/` and `historical-graph/` inputs reproduce their exact
reviewed sources. The new mapping, companion and semantic reports are explicitly
typed identity successors; they inherit only decisions that replay against the
unchanged scientific content. `migration-postimages.json.gz` carries the exact
postimages needed by the unified-snapshot freshness verifier. This verifier also
requires the original sidecar's actual complete input digest and record count;
it does not infer freshness from a Git revision alone.

## Scientific limits

- 3,014 SSSOM rows retain every non-identity cell and their original order.
- 1,739 mapping decisions remain supported; 1,275 remain withheld.
- The complete graph contains 5,798 nodes and 4,519 edges. Its full-release
  verdict remains `FAIL`. The supported subset contains 2,150 edges, and
  2,369 excluded edges stay in a separate backlog.
- The existing scoped companion retains 20 mappings, 18 identifiers,
  three products and ten qualified occurrences. No new occurrence is invented.
- All 2,956 IDs resolve in the local Pages build, including 82 records whose
  mapping status is `REJECTED`. Addressability does not approve their mappings.
- Existing visualization coordinates and scientific metadata are preserved;
  only record IDs and detail addresses change. No embedding/model calls ran.
- The unified 4,170-row mapping snapshot and its original sidecar are unchanged;
  an isolated native rebuild produced byte-identical output.

## Verification evidence

The retained `scripts/adhoc/*1265*` helpers describe their inputs, outputs and
purpose. Native QC, source-copy mutation checks, historical review replay,
consumer tests and independent adversarial reviews verify the transition. The
public receipts contain relative paths; full operational logs remain local.
Historical source copies are byte-preserved, including their existing provenance.

Review findings are tracked in #1267 (ambiguous alias waiver), #1268 (numeric ID
impersonation), #1269 (portable mint-order authority), #1270 (freshness stamp),
#1271 (lifecycle mapping transfer), #1272 (visualization build hashes), #1273
(duplicate YAML keys), and #1274 (mutation setup errors). Final validation and
re-review disposition accompany the pull request; this directory does not claim
that a branch has merged or that Pages has deployed.

See `docs/STABLE_MIM_IDS.md` for the consumer migration contract. The EdgeMech
adapter identity update is a separate follow-up after this migration merges.
