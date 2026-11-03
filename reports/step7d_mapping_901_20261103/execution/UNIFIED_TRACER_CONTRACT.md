# Strict Step 7d unified tracer

`trace_unified_snapshot.py` is external evidence tooling. It reads maintained
inputs, extracts a private base Git archive, builds private exact-current input
copies, and invokes the pinned native loader, resolver, label exporter and TSV
writer on those private fixtures. It observes resolver results without changing
selection. It neither stamps nor replaces any maintained file.

Run through the native wrapper, using resolved paths:

```sh
python3 "$RUN/run_step7d_mim.py" step7c-claw <new-log-name> -- \
  python -B "$D/trace_unified_snapshot.py" \
  --after "<directory containing native UNIFIED_INGREDIENT_MAPPING.tsv and sidecar>" \
  --tsv-sha256 "<exact TSV hash>" \
  --provenance-sha256 "<exact provenance hash>" \
  --mim-head "<exact clean source/export checkpoint>" \
  --out "$D/<new evidence directory>"
```

An alternative `--baseline-only --out <new directory>` validates the baseline
only and explicitly claims no after-pair verification. Output directories must
be new and lie under `D`; evidence files use the native exclusive publisher.
The script is bound to this plan's base, producer and owner-plan hashes. There
is no flag for changing selection, allowing unrelated drift or accepting an
untraced cell.

Full tracing requires all these machine receipt values:

- `status: PASS`
- `after_pair_processed: true`
- `before_native_replay_exact: true`
- `after_native_replay_exact: true`
- `native_provenance_verified: true`
- `all_changed_inputs_accounted_for: true`
- `untraced_cells: 0`
- Exact `base_revision`, `mim_checkpoint`, `producer_revision`,
  `producer_sha256`, `plan_sha256`, `baseline_tsv_sha256`,
  `after_tsv_sha256`, and `after_provenance_sha256` bindings.

The publisher must bind the actual receipt bytes and the named pair hashes,
not merely trust a copied status. Final independent review remains required.
The tracer author is not the final independent reviewer.

`cell-traces.json` carries exact before/after rows, the native source-path
bindings, effective CultureMech term, label-index ruling, anchor, rejection key,
native published-ID result, owner hashes, source group and exact zero-based plan
operation indices. Synonym changes additionally require a token-by-token
operation basis. Owner changes or ambiguous source bindings remain untraced;
an identifier match alone is insufficient. Untraced results are saved and exit
with status 2. Other preflight/replay failures exit nonzero and are retained by
the runner logs.

`native-input-inventory.json.gz` includes the complete input membership and
hashes. The changed source owners must equal the plan endpoints. Both before
and after collections must equal the direct records, excluding only the pinned
native `discussions` field contract, before the native label export is replayed.
The rejection ledger must replay both exact reviewed migration stages. Every
other upstream native input is unchanged, and all inputs are checked again
before evidence publication. `additional-proof-inputs.json` binds the current
collections, frozen plan, baseline inventory and actual pair.

The actual run `step7d-unified-trace-actual-v1` passed at clean MIM checkpoint
`70b0991a821b7c9c0d4c43924b564384cabc54b9`:

- 4,170 rows; unchanged membership, order, occurrence counts, examples and statuses.
- Six changed cells in four rows: two maltose identifiers; cerium CAS and
  identifier; copper identifier and withdrawal of the anhydrous synonym.
- Zero untraced cells.
- Exactly 40 changed native inputs: 38 reviewed owners, the native label-index
  derivative, and the exactly replayed rejection ledger.
- TSV SHA256 `f6a8eb844e578d79da9538abf99c244fc25b2c928c50c64c0477b1218092a0f1`.
- Provenance SHA256 `075fcc6ef6eca25c1e63d65889df37d4893be2b1b9d3630df90704012dc2c831`.

`cas-lookup-native-behavior.json` confirms the helper excludes CAS_RN_LOOKUP
from ontology-label harvesting. Both selected NCIt owners retain the label
independently as a preferred term or source synonym. The two observed maltose
rows publish NCIT:C80300 and preserve their source synonym; sodium carbonate
has no row in this CultureMech name inventory. No affected-row identity or
alias loss was found from that helper behavior in this batch, so this review
does not propose a producer change or a new defect issue for those two rows.
The original frozen trace-approach document is retained; its mistaken statement
about CLOSE_MATCH label handling is corrected explicitly in version 2.

Thirteen external attribution controls passed. The first baseline command had
a syntax error in the new tracer; it failed before work and its log is retained.
The corrected baseline command and actual full trace passed. No maintained test
or assertion was changed.
