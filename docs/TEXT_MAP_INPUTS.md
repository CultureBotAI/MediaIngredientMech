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


## Publish the common semantic view

`conf/text_map.yaml` enables the common map selected by
`data/text_map/current.json`. The governed runtime is installed at
`scripts/embedding_pipeline.py`. Publication requires the pinned fleet BGE
model, revision, dimension and 512-token window, actual PaCMAP, valid checksums,
and fresh complete adapter inputs. Missing or stale enabled inputs fail loudly.

`just stage-text-map` validates and stages the three public files at
`docs/text-map/` without inference. It binds the exact immutable generation
approved by preflight, refusing pointer changes or manifest substitution before
publication. The Pages workflow performs the same validation before uploading
`docs/`; a standalone stage does not regenerate existing browser pages.

The shared text map complements the existing domain graph views. Record URLs
are relative to `docs/`, so the shared map's `../` link prefix resolves to the
existing browser/detail routes. No legacy graph vector or model artifact is
relabeled as BGE.

`just build-docs` stages the map before its other generators. Static navigation
starts hidden and is enabled only after successful staging writes an explicit
boolean status at `docs/data/text_map_status.json`; disabling clears that status.

For local generation and refresh, follow the
[locked runtime instructions](../conf/embedding-runtime/README.md). After a
semantic record change, export the complete input, reuse the matching verified
vector cache to encode only changed text, and project a new immutable bundle
before running `just build-docs`. Keep the same recorded model/runtime profile
to reuse its cache. Normal CI and Pages validation perform no model inference;
they reject a stale enabled bundle until this explicit refresh is complete.
