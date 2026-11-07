# Native mapping assertions for EdgeMech

`mediaingredientmech.export.edge_curation.build_native_assertions` transports
an immutable reviewed SSSOM release into CLAW's native assertion contract.
The caller supplies the source archive SHA256, source Git commit, export
manifest SHA256, and one-based source positions. The complete native source,
review input inventory, owner records, output partition, and dispositions are
verified before a selection is returned. No ingredient records are rewritten.

Each assertion retains the full source row, native decision, selected evidence
entry, owner binding, historical source locator, and pinned interpretation.
Supported status means inherited native mapping review. Withheld rows remain
scoped backlog entries. Neither status creates a new scientific review or
approves a current KG occurrence. A triple match identifies a candidate; reuse
requires the complete native payload and dependency bindings. Ingredient
identity never establishes an organism-growth or medium-preference claim.

The shared source pin is in `tool.mediaingredientmech.edge-curation` in
`pyproject.toml`. The dedicated `Edge curation native adapter` workflow checks
out that exact CLAW revision and verifies both Git identity and Python import
origin before running the feature tests. `MIM_REQUIRE_EDGE_CONTRACT=1` makes a
missing contract an error in this tier. The ordinary native suite may skip
these optional integration tests when CLAW is absent.

Use `scripts/adhoc/run_edge_adapter_canary_20261107.py` with explicit archive,
bundle, commit and hash arguments. `--positions 1 21 25` selects the historical
supported/withheld canary; `--all` uses the same path for a full export only
after verifying that canary. `--output` must name a new directory. Publication
stages and validates `assertions.jsonl` and `manifest.json`, exclusively reserves
a new destination, and publishes the manifest last after syncing the payload.
Files and directories are synced; readers ignore incomplete destinations without
a manifest. The manifest reports persisted row/status counters and
hashes. Outputs belong in ignored `output/`; do not create a GitHub record per
mapping or publish these assertion payloads as independently reviewed claims.

The optional integration uses shared source rather than installing the full
CLAW distribution because MIM currently pins LinkML below 1.10 and CLAW
requires LinkML 1.10 or later. Splitting out a minimal shared-contract package
is follow-up packaging work; this adapter does not change native schema tooling.
