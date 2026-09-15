# Common semantic text map inputs

Includes active ingredient records, excluding REJECTED tombstones. Identity uses
the existing filename-derived MIM CURIE because ontology identifiers can be
shared by distinct records. Pages select the exact source file in the deployed
browser. Text includes name, resolving synonyms, ingredient type, semantic
chemical properties and named components. Mapping confidence, occurrence counts,
history, notes, evidence and machine structure strings (SMILES/InChI) are excluded.

Export with `just text-map-inputs --output data/text_map/inputs.jsonl`. Without `--output`, the command validates a preview. `--record` (repeatable repository-relative YAML path) and `--limit` explicitly select canary subsets; ordinary exports cover every eligible record.

Each JSONL row has exactly `identifier`, `label`, `category`, `page`, `source_path`, `text`, `text_sha256`, and `adapter_version`. The text digest is SHA-256 over the exact UTF-8 text. Input order and text are deterministic; duplicate IDs and unreadable records fail. This adapter makes no model call. Common model/projection generation and publication require the fleet pipeline and full-input checks.

Changing provenance-only fields leaves semantic text unchanged. Editing a selected semantic field changes its digest. This text view supplements the existing graph view; it does not alter graph aggregation or its scientific interpretation.

The `page` field is relative to the directory containing the published map
folder: from `text-map/index.html`, the shared renderer uses `../` plus `page`.
This repository publishes the contents of `docs/`, so the bundle is staged at
`docs/text-map/` and links resolve to records in the same published site root.
