# Source and migration inputs

The five response files under `sources/` are unchanged successful primary API
captures from 2026-11-01, with their original URL/status/time/hash receipts.
`sources/manifest.json` binds the exact selection. The CAS-routed and CID-routed
PubChem responses have identical bytes: both retrieval receipts are preserved,
but they are one evidence payload, not independent confirmations or a direct
CAS Registry lookup. The earlier inaccessible web-tool attempt is recorded as
a transport limitation, not chemical evidence. No new provider call was made
for this implementation.

ChEBI17754 supplies negative alias evidence for Gro, glycerolum and glycyl
alcohol; its evidence belongs in the rejection history and receipt, not as
support for a phosphate mapping. Existing `sssom_other_backfill` attribution is
preserved. The OLS CHEBI36218 response scopes LACTOSE as `hasRelatedSynonym`
with `pdb-ccd` attribution. ChEBI17270 and the one PubChem CID2735049 payload
support correcting the disodium glycerophosphate pentahydrate's parent while
retaining its CAS identity, raw labels, chemistry and counts.

`decisions/posted.json` records the issue decisions posted before implementation;
the corresponding exact bodies are retained. The sodium succinate and ammonium
nickel form questions remain open in #1049 and #1050, and magnesium in #811.
They authorize SUPPRESS without guessing a merge. Earlier proposed diagnostic
origins in `pair-plan.json` are historical precuration observations, not the
future actual generation binding. Four historical-only pairs must retain any
additional origins observed in the fresh diagnostic alongside prior_sssom.

The immutable fixture at `tests/fixtures/issue669-owned-name-before/` binds
13 affected owner preimages plus 11 additional credited preferred-name owners,
the full canonical preimage compressed once with deterministic gzip, and the
baseline at MIM `be7170deb00a7c5490f8ade82facf86d45a852a4`. These are one-time
migration fixtures, not permanent live-count constraints. No ontology database,
whole generated graph, or unrelated historical report corpus is copied.

Source correction, export suppression, and scientific approval remain separate.
L-asparagine's YAML and approved role payload/position/hash remain unchanged;
the migration receipt records its export-only change without fabricating a
history event. New generation must bind the verified merged Claw producer
`9bd09b2ba163212a65289b91313f98cb0937476f` separately from MIM's unchanged
pinned validator runtime. No generation or scientific release approval is
asserted by this source-input note.
