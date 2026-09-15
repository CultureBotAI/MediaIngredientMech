# MediaIngredientMech ingredient graph provenance

Graph maps retain their KG-Microbe DeepWalk features and domain matching policies. The fleet's common BGE text map is a separate view. This work follows #678 and #679.

Run `python scripts/generate_ingredient_umap.py --embeddings-path /path/to/source.tsv.gz --method pacmap --output docs/data/ingredient_umap.json`. For the retained force-directed graph, use `--method sfdp --output docs/data/ingredient_graph.json`. Each JSON receives a sibling `.metadata.json`; the two graph pages verify the exact fetched JSON against its own receipt. `--method umap` is also available.

The complete input corpus includes mapped and unmapped YAML files. Rejected files are recorded outside the eligible population. Every eligible record has a matching or omission ledger entry. Direct identifiers, ontology mappings, synonym references and history references remain distinct. Missing vectors are omitted without synthetic noise. Browser headings derive the actual reducer from verified metadata; historical data without a receipt is explicitly unverified.

New generation reads the selected TSV or TSV.gz stream directly and hashes the exact bytes while parsing. Old basename/size/mtime pickle caches are ignored, including when `force_reload` is false. The scan is streaming and retains only required node vectors; the full source file is still read once per generation. Do not infer source identity by hashing a different file beside old coordinates.

Schema-v2 receipts bind the full corpus, matching/omission ledger, ordered reducer matrix, actual algorithm/normalization/settings and installed backend versions to checksums of every output. PaCMAP records fitted pair counts. The sfdp backend, where available, records the symmetric union-kNN construction, DOT checksum, Graphviz version and command arguments. Failed generation leaves previous outputs unchanged; publication rolls back ordinary write failures. A process kill can leave a `.graph-recovery-*` directory for recovery and is not claimed to be an atomic website deployment.

Validate a completed generation with:

```python
from pathlib import Path
from mediaingredientmech.graph_embedding_receipts import load_receipt

receipt = load_receipt(Path("path/to/projection.metadata.json"))
```

This verifies all sibling artifacts declared by the receipt. It is not a tool for attaching newly guessed provenance to legacy arrays. Full published artifacts must be regenerated from reviewed current inputs before the graph correction is considered complete.

## Current publication gate

Run `just check-graph-receipts` before publishing. The standalone equivalent,
`python -S scripts/check_graph_receipts.py`, uses only the standard library. It
validates both graph JSON/receipt pairs, exact output membership and bytes,
ordered point identities and lookup methods, and coverage of every current
`data/ingredients/{mapped,unmapped}/*.yaml` file, including ignored and rejected
files. It does not load embeddings or rerun a layout.

`just build-docs` and `just check-visualizations` run this gate first. Pages also
runs it before any site writes or upload, even when the common semantic text
map is disabled. A source edit, addition/removal, missing receipt or damaged
output refuses current publication while leaving the previous site intact.
Semantic text freshness alone is insufficient: a MediaDive reference in notes
can change graph matching without changing the common BGE input. Such changes
require a local graph refresh from the reviewed vector source before publication.
The historical no-receipt browser fallback remains available for archived data;
it does not exempt the two maintained current graphs from this required gate.
