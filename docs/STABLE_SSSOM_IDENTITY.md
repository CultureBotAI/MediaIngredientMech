# Permanent SSSOM identity migration (#1371)

The accepted stable-ID requirement in #1265 and #1299 supersedes mandatory
filename-derived registry-handle synthesis for validated permanent MIM subjects.
The older Rule B1 prose in MAPPING_SEMANTICS.md describes the legacy slug route;
it did not already document this permanent-identity branch. This additive
migration note does not change ingredient science or the frozen adoption inputs.

For a permanent subject, Rule B1 now requires all of the following:

- The declared MIM URI is the permanent ingredient namespace.
- The subject is a canonical positive seven-digit MIM identifier.
- Native mint/lifecycle validation and the complete mapped/unmapped inventory
  establish exactly one current active owner for every active minted identifier.
- The external row's subject and label resolve directly to its current MAPPED
  owner, independently of its label at minting, filename or legacy aliases.
- Captured owner/ledger bytes, file/ancestor identities and inventory membership
  remain current through validation or reviewed publication.

The ordinary reviewed-SSSOM route requires the complete identity closure in its
existing `inputs`/`record_inputs` hash maps. `record_inputs` still covers exactly
the row owners; put the remaining current owners and both ledger files in
`inputs`. Every supported or withheld external row still needs its existing
explicit evidence-bound decision. Permanent identity never promotes a withheld
external or registry claim. Historical projection review is unchanged.

Legacy MIM slug subjects retain their existing matching registry exact row rule.
Malformed numeric spellings, unknown or retired IDs and incomplete inventories
cannot fall back to that route. Existing registry rows and their reviewed
retirement/history obligations remain; this change creates or removes no row.
Rule B5 and all other mapping, date, synonym and external-evidence gates remain.

The source export continues to express source-to-permanent-MIM identity
separately from external ontology assertions. A broad/close/narrow mapping is
not an identity or subclass edge. A MIM-only source needs no invented external
match, registry handle or self-loop. Rename and legacy alias preservation remain
native stable-ID and source-export responsibilities.

TC admission may use the code/test commit independently of this documentation
commit to preserve exact scientific input hashes. Admission must still verify
the actual completed adoption and generation closures; a descendant commit is
not evidence of scientific acceptance or release approval.
