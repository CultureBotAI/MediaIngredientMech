# Public ingredient pages

The Pages workflow publishes a fresh `site/` artifact containing the existing
`docs/` landing, browser, maps and assets plus generated record pages. The catalog
links to `records/ingredient/{mapped,unmapped}/<source-slug>.html`; the complete
index lives at `records/index.html`. Slugs come from the shared renderer function,
including source directory, so mapped and unmapped names cannot collide.

From a source checkout, run `uv run python scripts/build_pages_site.py --output site`.
The output must not exist. The builder stages all output, renders every current
source with `force=True`, and verifies catalog coverage, unique URLs, source hashes,
renderer/template hashes, and generated-page hashes before publishing the directory.
`--check site` verifies an existing artifact and fails for missing or stale records.
The required flat-export coverage job runs the same complete build before merge.
No generated detail pages are committed; data changes trigger a fresh Pages build.
The old `just gen-ingredient-pages` command remains a local preview, not the deploy
command. Both routes use the same templates and expose typed material components,
component assertions, evidence, synonyms and provenance.
