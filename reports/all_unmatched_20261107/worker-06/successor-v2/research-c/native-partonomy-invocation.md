# Native partonomy on the isolated successor

Stage the final99 proposals over read-only maintained owners, then invoke the native checker. The stage directory is private session state, not an installed catalog.

```bash
PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.venv/bin/python .temp/all-unmatched-worker-06/successor-v2/research-c/stage_partonomy.py --proposals reports/all_unmatched_20261107/worker-06/successor-v2/proposals.json --artifact-root reports/all_unmatched_20261107/worker-06 --out-dir .temp/all-unmatched-worker-06/successor-v2/research-c/partonomy-overlay --expected-count 99
PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.venv/bin/python scripts/validate_component_partonomy.py --curated-dir .temp/all-unmatched-worker-06/successor-v2/research-c/partonomy-overlay
```

The native CLI reads both temporary collections. It validates catalog references, duplicate/self components, required assertion evidence and paired values/units without network, synchronization or downstream output. Science and strict schema remain separate. The JSON binds the inspected native code and helper hashes.
