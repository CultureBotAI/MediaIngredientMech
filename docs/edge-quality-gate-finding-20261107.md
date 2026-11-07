# Run native static quality gates for the optional Edge adapter

PR #1147 passed its mandatory pinned-contract integration tier but failed the
native Python quality gate: the new adapter has an unused JSON import and an
unsorted import block. Local mypy also reports the intentionally optional CLAW
imports as unavailable in the base native environment.

Apply native Ruff/Black formatting to the new maintained modules and scope the
existing optional-import mypy policy to the new exporter, keeping all its other
type checks enabled. The mandatory integration tier must continue requiring and
verifying the exact CLAW source pin; do not resolve the LinkML version conflict
by silently upgrading either repository or skipping that tier (see #1144).

Verify `just lint format-check typecheck`, focused integration tests, and the
same pinned real canary. If the adapter byte digest changes, retain the old
receipts and create a new full export after the new canary is verified.
