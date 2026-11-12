# Current semantic graph after a native publication

Issue #1387 adds an explicit current graph route. The legacy ordinary and fixed
identity-projection routes keep their original authorities and checks. A data
PR selects this route only after its genuine current mapping and companion
reviews, publication artifacts and full graph exist. No selectors are changed
by the implementation alone.

The new route keeps three scopes distinct:

- The original native application and `verify_completed` run at their original
  roots. Their receipts preserve their original Git, runtime, acquisition and
  operational identities.
- A semantic transition capture retains those exact artifacts. Its consumer
  reconstructs full owner and mapping transitions, suppression/history payloads
  and installed bytes in CI. It does not claim to rerun the original transaction,
  providers, locks or acquisition environment.
- Current ordinary mapping/companion reviews and current held-claim assessments
  supply release decisions. Source correction, installation and archived review
  decisions never supply new release approval.

## Authoring sequence

Use a genuine disjoint historical checkout at the independently reviewed full
commit, as described in `CURRENT_REVIEWED_EXPORTS.md`. The graph route additionally
replays the exact original pre-migration graph with its pinned historical native
implementation before checking the stable identity projection. The original
mapping-change receipt endpoint and frozen aromatic review are not rewritten.

After original-root publication application and verification, capture a fresh
evidence directory using the maintained runtime:

```bash
python -m mediaingredientmech.validation.current_semantic_release capture-transition \
  --root PATH_TO_ORIGINAL_PUBLICATION_ROOT \
  --publication-stage RELATIVE_NATIVE_PREPARED_STAGE \
  --publication-receipt RELATIVE_NATIVE_APPLICATION_JSON \
  --output FRESH_RELATIVE_EVIDENCE_DIRECTORY
```

The command runs the real same-root verifier, captures original files and
beforeimages with their qualified identities, and verifies/rechecks them before
publishing the packet. It does not modify curated records or canonical mappings.
The printed `path`/`sha256` pair identifies `transition.json`. Captured members and
their original identities must be retained together. The packet is not a trust
certificate: the current graph consumer reconstructs its semantic links.

The current graph request is a closed JSON object with these fields:

| Field | Required value |
| --- | --- |
| `schema_version` | `1` |
| `capability` | `mim-current-semantic-graph/v1` |
| `historical_root`, `historical_revision` | Genuine disjoint historical checkout and full reviewed SHA |
| `transition` | Actual capture's `path`/`sha256` pair |
| `mapping_review`, `companion_review` | Genuine current ordinary review paths |
| `bundle` | Actual full native KGX export directory |
| `hold_reviews` | Hold ID to primary/independent native report references, or `{}` |
| `review_inputs` | Exact additional current evidence path-to-SHA256 bindings |
| `finding_dispositions` | Complete current finding-disposition TSV; `null` only during inspection |
| `record_lineage` | Current explicit native-compatible lineage JSON path, or `null` |

Rebuild the complete graph through `mediaingredientmech.export.kgx`, using the
actual workflow output path. Then inspect the request into a fresh directory:

```bash
python -m mediaingredientmech.validation.current_semantic_release inspect \
  --root . --request CURRENT_REQUEST_JSON --output FRESH_INSPECTION_DIRECTORY
```

Inspection emits exact current hold payloads. A payload includes the complete
original negative finding, frozen resolution, legacy row, stable projected row,
current owner hash, current full row and every changed cell. Review it through
the repository's native `record_review` inspect/validate/save workflow.

Each supplied hold assessment must bind that complete payload with a
`sha256-canonical-json-v1` snapshot-row digest, use
`semantic_scope=current_mapping_release_and_historical_hold`, and explicitly
choose `SUPPORTED` or `WITHHOLD`. References contain `path`, `sha256`,
`markdown_sha256`, `target_id` and `assessment_id`. A positive resolution needs
two distinct reviewer identities and separate reports, with the second declaring
independence and its basis. Missing review or disagreement retains WITHHOLD.
An installation-scope report cannot satisfy this release scope.
The assessment must cite evidence whose exact snapshot hash is in its captured
input inventory. A positive decision additionally needs supporting primary,
database or authority evidence; a record's own assertion or context-only source
does not supply that positive evidence (#1394).

Every original finding also needs a complete current disposition and actual
current owner hash, with native evidence and lineage where relevant. The
unchanged `adjudicate_findings` contract enforces these requirements (#1390).
Copying old dispositions is not a refresh. Unreviewed role, component and other
nonmapping graph assertions remain OPEN.

After the actual current assessments and finding dispositions exist:

```bash
python -m mediaingredientmech.validation.current_semantic_release build \
  --root . --request CURRENT_REQUEST_JSON \
  --hold-payloads ACTUAL_INSPECTION_DIRECTORY/hold-payloads.json \
  --output FRESH_CURRENT_REVIEW_DIRECTORY
python -m mediaingredientmech.validation.current_semantic_release validate \
  --root . --report ACTUAL_CURRENT_REVIEW_DIRECTORY/review.json
```

The report can have integrity PASS and semantic release FAIL when unresolved
claims remain. Supported graph export retains excluded claims separately. A
data PR must retain the packet, original historical authority, current reports,
current finding/hold evidence and actual full-graph producer inputs, and select
the new report explicitly in its existing reviewed workflow. Other structural,
scientific and release gates still apply.

## Refusals and limits

The adapter rejects incomplete owner or row inventories, undeclared deltas,
changed permanent identities, altered history prefixes, unproved moves, stale
current findings, missing mandatory invalid-CAS holds, full-row or suppression
drift, unreviewed held-row changes, wrong historical proof and late input drift.
Broad/close/narrow mapping relations retain their typed meaning; they are not
subclass assertions.

Original acquisition reviews retained only as history keep their exact
YAML/Markdown, qualified source identities and declared input inventories. CI
does not thereby revalidate their acquisition environment or inherit their
positive science. Current positive decisions require current evidence and review.
Unsupported transition shapes fail explicitly and need a separately reviewed
extension; an arbitrary rehashed receipt or saved successful verifier result is
never a replacement for reconstruction.

The consumer's genuine MediaIngredientMech Git object database must contain the
original adoption, source-correction, installation and diagnostic CAS review
revisions. Native `source_provenance` validates
their committed input blobs; working-tree reports retain only their original
attestation status. A missing revision, wrong repository or false committed-byte
claim is a refusal. This Git proof does not pretend to reproduce the original
filesystem path or acquisition environment.

For diagnostic CAS history, this adapter capability accepts exactly the reviewed
native `stable_mim.py` implementation from Claw
`4287dce16ee8b5f897bf70f915bdca9aa1484bb6` (SHA256
`3a04bc0435c4f6801994901cffbde9005ca1f589723cc79b32d079fdf6f6ad33`).
That authority is checked before executing captured bytes; mutually rehashed
producer declarations cannot select a different validation policy (#1395).
This does not modify the producer or vendored pins. The original native CAS pair
still has to bind each complete diagnostic claim, action and retained hold, with
its exact captured evidence and independent reviewer identities. The consumer
uses a declared physical byte-lookup namespace and its genuine Git objects;
only the returned absolute lookup path is qualified back to the preserved
original acquisition path. No scientific fields or decisions are rewritten.
