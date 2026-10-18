# Standalone MIM ingredient graph

The [reviewed release](../reports/semantic_review_20260921/resolution/README.md)
contains only supported assertions and preserves the rest in a separate backlog.
Build and check it with:

```bash
just export-kgx output/mim-kgx-710-full
just export-supported-kgx reports/semantic_review_20260921/resolution/current-review.json output/mim-kgx-710-supported
just qc-supported-kgx reports/semantic_review_20260921/resolution/current-review.json output/mim-kgx-710-supported
```

The supported output includes its own SSSOM subset and a separate
`unsupported-backlog.json`. PASS applies to that reviewed subset. The complete
source projection described below retains its failing semantic verdict.

Use these three TSVs from the same supported bundle:

| File | Contents |
| --- | --- |
| `ingredient_mappings.sssom.tsv` | Reviewed identity and parent mappings, with SSSOM metadata |
| `mim_nodes.tsv` | Active ingredient record references and terms used by reviewed assertions |
| `mim_edges.tsv` | Reviewed mappings, roles, components, and environmental assertions |

Load both KGX TSVs together, or load `mim-kgx.tar.gz`, which contains the two
graph TSVs and their manifest. The SSSOM and `unsupported-backlog.json` are
separate files outside that archive. The backlog preserves excluded assertions
and raw source node annotations; it must not be loaded as approved graph data.
An ingredient node alone identifies a source record, not an approved chemical
identity. Isolated ingredient nodes are retained deliberately.

Read TSVs as UTF-8 tab-delimited files. Skip `#` metadata lines when reading the
SSSOM with a generic TSV reader. KGX JSON annotations escape literal pipes;
decode the JSON cells to recover the original values. The manifest binds the
review, counts, and data file hashes. A versioned data snapshot additionally
includes `SHA256SUMS`, validation receipts, and `release-provenance.json` naming
the exact source commit. Verify all downloaded files with `sha256sum -c
SHA256SUMS` (or `shasum -a 256 -c SHA256SUMS` on macOS).

The supported SSSOM preserves source confidence annotations verbatim, including
values whose grading provenance remains under discussion in
[#662](https://github.com/CultureBotAI/MediaIngredientMech/issues/662). Semantic
review does not silently rescale those annotations.

Build a complete projection of the assertions held by MIM:

```bash
just export-kgx output/mim-kgx
# Equivalent, with the editable project installed:
python -m mediaingredientmech.export.kgx --output output/mim-kgx
```

The destination must be a new directory. The exporter validates and stages the
bundle before publishing it locally. It needs no network connection, KG-Microbe
checkout, or KGX installation. Files under `output/` are ignored by Git.
For a non-editable installation, supply `--repo-root /path/to/MediaIngredientMech`.
Local ignored review ledgers are not loaded implicitly. Supply `--review-ledger
reports/path/to/ledger.tsv` to include a particular review; its bytes are then
recorded as an export input. This keeps default exports reproducible in a clean
checkout and a research workspace.

## Scope and identity

Every active mapped, unmapped, or explicitly ambiguous ingredient has its own node. Mapped records use
their published SSSOM subject IDs, resolved through unambiguous current preferred
terms. Unmapped and ambiguous records use `MIM.unmapped:<record identifier>`;
their original status is retained and no identity mapping is invented. Records sharing a
primary ontology identifier remain distinct: their evidence and roles are not
silently combined. Rejected records are excluded from the graph and retained in
`excluded_records.tsv` with their complete source data.

Only terms referenced by MIM assertions are added as external nodes. This does
not import the KG-Microbe graph or whole ontologies. External labels are MIM's
supplied labels; all observed labels are retained, and the category is the
conservative `biolink:NamedThing`.

| Source assertion | Graph relationship |
| --- | --- |
| SSSOM exact and close matches | Corresponding Biolink match predicate |
| SSSOM broad and narrow matches | Specific-to-broader `biolink:broad_match`; inverse mappings reverse endpoints |
| Nutritional, physicochemical, cellular metabolic roles | `biolink:has_chemical_role` to facet-specific `MIM.role:` nodes |
| Community organism roles, when present | `biolink:has_attribute` to facet-specific role nodes |
| Components | `biolink:has_part`, with `BFO:0000051` as the relation |
| Environmental context | `MIM.vocab:environmental_context`, preserving the source qualifiers |
| CultureMech recipe reference | `MIM.vocab:recipe_<relationship>`, retaining candidate status where applicable |

For `broadMatch`, the **object is broader than the subject**. The exporter follows
MIM's explicit [mapping contract](../MAPPING_SEMANTICS.md#1-predicate-semantics):
both asymmetric predicates become specific-to-broader `biolink:broad_match`
edges with `relation=skos:broadMatch`, reversing endpoints for `narrowMatch`.
The complete original row, including its original endpoints and predicate,
remains in `assertion_json`. A broader alignment does not establish an ontology
subclass relationship (#245/#734). The application checks broader-link cycles
separately from material part cycles; neither check implies identity or subsumption.
The retired local ingredient-variant hierarchy is not recreated. Role enum mappings to broader classes or METPO predicates are
retained as annotations, not treated as identities of role nodes.

A known component points to its supplied semantic identifier. It does not choose
an arbitrary local record when multiple records share that identifier. Unmapped
components use parent-scoped `MIM.component:` IDs; a common label does not imply
that components in different records are identical. Reference scope, quantity,
unit, completeness, method, and evidence remain attached to each component edge.
These assertions do not establish complete CultureMech recipes.

## Complete source projection: files and annotations

The output contains `mim_nodes.tsv`, `mim_edges.tsv`, `excluded_records.tsv`,
`manifest.json`, and a deterministic `mim-kgx.tar.gz` containing the four other
files. Nodes precede edges in the archive for streaming readers.

* `record_json` preserves each complete ingredient record, including synonyms,
  history, and discussions. `source_record` identifies the source file.
* `assertion_json` preserves each complete edge assertion, including evidence,
  confidence, metabolic context, and component assertion metadata. Convenience
  columns expose common values without replacing the original data.
* `definition_json` preserves each role enum definition.
* `review_json` retains the historical review ledger entry. `review_status` exposes
  a positive verdict only when the ledger's `record_sha256` matches the current
  file; otherwise it is `historical_review_unverified`. Existing unresolved
  findings remain visible. These fields do not grant whole-graph release approval.
  A ledger entry is not a fresh, content-bound approval of the current record.
* JSON cells escape literal pipes so KGX list parsing does not split them.
  Parse them as JSON to recover the original strings, including tabs/newlines.
* Edge IDs use `MIM.assertion:` hashes of the complete assertion and provenance.
  Distinct evidence-bearing assertions remain distinct even if triples coincide.
  The manifest reports both edge rows and unique subject/predicate/object triples.
  Consumers that merge by triple must retain all assertion annotations.

The manifest declares local prefixes, counts by assertion and node kind, input
and implementation hashes, and output member hashes. Local namespace declarations
are identifiers, not promises of deployed resolvers. Source attribution is
`MIM:ingredients`, matching the SSSOM dataset identifier.

## Validation and limits

The exporter checks closed-schema source validity, collection/per-record agreement
(excluding per-record-only discussions), component reference scope, exact primary
identity coverage, current ontology grounding direction, unique identities,
endpoint closure, declared CURIE prefixes, directed hierarchy and material-part
cycles, and stable inputs through publication. Only live files directly under
`data/ingredients/{mapped,unmapped}` are read; backup subdirectories are not inputs.

Run regression tests with `pytest tests/test_kgx_export.py`. The SSSOM's own schema,
currency, label, and predicate checks remain separate validation steps; use the
existing SSSOM quality workflow as well.

This is a KGX TSV graph with documented native MIM predicates. Strict Biolink
conformance is not claimed for those extensions. Structural validation and faithful
projection do not adjudicate every biological assertion or resolve existing
curation findings. Consumer counts should distinguish ingredient nodes from
external reference and role nodes; read the exact artifact's manifest rather than
using KG-Microbe aggregate statistics.

The [2026-09-21 semantic review](../reports/semantic_review_20260921/README.md)
covers the current source snapshot and records a **failing semantic release
verdict**. Passing export/format checks do not close that correction backlog.
