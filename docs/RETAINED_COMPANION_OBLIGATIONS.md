# Complete companion cohorts with held owner mappings

Issue [#1222](https://github.com/CultureBotAI/MediaIngredientMech/issues/1222)
requires the complete original 20-owner, 51-claim cohort to survive a current
scientific hold. A held owner mapping cannot authorize a scoped identity, active
xref, product or occurrence through its companion claims. Retaining only the
other owners would lose the original obligation census.

An ordinary current companion can opt into `retained-companion-obligations-v1`.
This is a native partition of the complete reviewed cohort. It is not a new
scientific approval, a substitute for a complete canonical mapping review, or
permission to modify historical reports. The original positive mapping path
remains unchanged. Old-format bundle bytes and capability requirements remain
unchanged.

## Input

Keep every current claim in the ordinary `claims` file and give every claim its
own complete current decision and owner/evidence proof. Add this field to the
ordinary companion review:

```json
{
  "retained_obligations": {
    "capability": "retained-companion-obligations-v1",
    "historical_review": {"path": "archive/original-review.json", "sha256": "EXACT_ORIGINAL_HASH"},
    "historical_sources": {
      "original/relative/path": {"path": "archive/original/relative/path", "sha256": "EXACT_ORIGINAL_HASH"}
    },
    "lineage": [
      {"previous_claim_id": "ORIGINAL_ID", "previous_sha256": "COMPLETE_ORIGINAL_ENVELOPE_HASH", "claim_id": "CURRENT_ID", "sha256": "COMPLETE_CURRENT_ENVELOPE_HASH"}
    ]
  }
}
```

All references must occur in the hash-bound current `inputs`. Historical
transport must exactly cover the declared inputs of the existing fixed original
companion authority, which is replayed natively against its original bytes.
The current claims and ordered lineage must cover every original envelope and
all original owners, without omissions or duplicates. This bounded extension
does not accept an arbitrary smaller historical baseline.

The opt-in path executes a private captured module closure rather than cached
public imports. Its authoritative finite path list is `PATHS` in
`export/companion_producer.py`: 13 native modules, the companion and reused
source capture loaders, two packaged schema/profile resources, the dependency
lock, package metadata and maintained Python version (20 unique paths). Every
path must also be present in the current review's `inputs` with identical bytes.
Relative native imports and resource reads use the captured buffers. Unknown
native imports/resources, stale selected bytes, aliases and changes through
completion fail closed. The manifest retains this actual executable closure
and runtime; it is not a signature or a new scientific approval. The current
semantic route additionally captures this membership only for the opt-in path.

The current `inputs` also contain both permanent-ID ledgers, every current
mapped/unmapped owner, the original migration manifest and its independently
pinned complete baseline record inventory. Native registry and mint-order
validation establish the original owner's permanent address. Keeping a slug
alias alone is insufficient. This extension does not rename owning file paths,
merge owners, redirect retired IDs or choose ambiguous aliases.

Current nonmapping payloads preserve all original raw science and source data.
Only the authenticated owner address, dependent annotation ID and a reviewed
SUPPORTED-to-WITHHOLD status withdrawal may differ. Withdrawing an identifier
also clears its active-xref eligibility. No quantity, preparation, alternative,
catalog number, evidence attribution or chemistry is inferred or normalized.
Mappings instead require the actual complete current canonical row and renewed
scope evidence; the old row is retained verbatim in lineage.

## Validation and partition

Every held mapping requires all of:

- Its exact complete row in the current base review with disposition WITHHOLD.
- Its current scoped claim decision and scope status WITHHOLD.
- `ext_identity_authorized: "false"` and valid scope/evidence fields.
- Exact current owner and complete claim evidence.

The native validator derives the retained dependency closure from the owner,
not a caller-supplied list. Every annotation, product and occurrence of that
owner enters the retained partition, including all product alternatives. The
complete product-reference graph is checked before partitioning. A reference
cannot move a held claim to another owner's active output.

Source-level scientific status and active eligibility remain separate. For
example, an accurately captured source observation may still be scientifically
SUPPORTED while retained because its owner's external mapping is held. It must
not enter an active identity, xref, product or occurrence index. The unsupported
JCM220 quantity retains its own WITHHOLD status and original reported payload;
this extension does not assert a corrected concentration.

The remaining emitted claims pass through the existing positive companion
validator. No held mapping is made supported to satisfy that validator. The
bundle's native `retained_companion_obligations.json` accounts for every
original and current envelope, complete current decision, derived emitted or
retained partition and blocking mapping claim. Its exact bytes are reconstructed
during bundle validation. The manifest cohort still includes all reviewed
owners. The required new capability and artifact cannot be stripped.

The ordinary export commands are unchanged:

```bash
python -m mediaingredientmech.export.ingredient_bundle export \
  --root ACTUAL_ROOT --review ACTUAL_COMPLETE_COMPANION --output NEW_OUTPUT
python -m mediaingredientmech.export.ingredient_bundle validate \
  NEW_OUTPUT --manifest-sha256 ACTUAL_MANIFEST_SHA256
```

Scientific assessments, current full canonical review, immutable historical
projection proof and independent full-packet review remain separate requirements.
Nothing in this implementation creates those reports or changes the cohort.

## KG-Microbe acceptance fixture

The currently inspected KG-Microbe consumer builds indexes from the validated
`mappings`, `identifiers`, `products` and `occurrences` arrays. The new MIM
validator returns only ordinary emitted claims in those arrays. Existing
nonmapping WITHHOLD entries retain their native status and inactive xref rules;
emission does not mean scientific support. Retained complete claims
are accessible only through `retained_obligations`, for evidence and review.
No KG-Microbe source or mapping input is changed by this implementation.

A consumer must explicitly implement and accept the new capability. An older
validator rejects it before consumption; removing the capability also fails
native reconstruction. A consumer fixture must demonstrate:

- Full native 51-claim/20-owner accounting, with exact old/current lineage.
- The held BSA mapping and all 13 dependents remain present in the native
  retained artifact, absent from active consumer arrays and indexes.
- Retained CAS annotations do not become active xrefs; catalog alternatives do
  not become selected products; retained occurrences cannot resolve a source.
- New-capability refusal by an older consumer, and unchanged old-format output.
- Permanent `MIM:` ingredient URLs retain their explicit meaning when graph
  spelling changes to `MIM.ingredient:`; no collision with Biolink's MIM prefix.
- No new ontology-parent or subclass edge, no identity collapse, and no
  production activation inferred from a successfully validated candidate.

The fixtures in `tests/test_retained_companion.py` exercise native complete
accounting, real export/replay, old positives and adversarial current/history,
dependency and transport changes. They are explicitly synthetic scientific
decisions, not campaign acceptance. A real KG consumer fixture and its adoption
remain required before downstream use; no KG rebuild is performed here.
