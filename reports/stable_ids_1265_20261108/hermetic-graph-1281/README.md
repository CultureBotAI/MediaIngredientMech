# Hermetic native graph replay — issue #1281

Date: 2026-11-08. Finding: https://github.com/CultureBotAI/MediaIngredientMech/issues/1281.

The complete graph-proof test previously required ignored local output that CI did not build. Its fixture now shares only local Git objects into a no-checkout clone, copies the explicit current records, aggregates, ledgers and historical proof dependencies, and exports the native graph into that isolated clone. The original proof, path checks, rechecks and exact report/disposition comparisons are unchanged. No production code or scientific data changed.

Inputs are the current native corpus/exporter and fixed historical proof. Outputs are disposable fixture clones and graph bundles under repository `.temp/`, plus the retained focused log and mutation receipts here. No remote Git operations or providers are used.

Validation: all eight focused tests passed; Ruff and diff checks passed. Fresh-process mutation control passed. Removing only the native-export setup failed on the isolated missing graph manifest, even though the development checkout retained its ignored output. A separate read-only reviewer found no issue in the test/helper; final review must bind the committed head.

Reproduction:

```sh
uv run --no-sync python -m pytest tests/test_identity_projection_graph.py -q -p no:cacheprovider --basetemp .temp/hermetic-graph-1281-focused
uv run --no-sync python scripts/adhoc/check_hermetic_graph_mutation_1281.py --output reports/stable_ids_1265_20261108/hermetic-graph-1281/repeat-mutation
```

Use a fresh output name for the mutation helper. `summary.json` records source hashes; `mutation/results.json` binds the exact helper/test and both child-process outcomes. No commits or pushes were performed by this subtask.
