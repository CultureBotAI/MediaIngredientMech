# Shared primary-reference cache

This cache serves the 18 exact owner paths in the coordinator's lexical-hint
packet, verified against frozen MIM `e000d66dd26ab053e9b17ce7bf8d3c873c3dde99`.
The hints contain 48 owner references to 46 source cases. They are **not identity
matches**. This cache makes zero case decisions, owner edits, role approvals,
mapping approvals or hold changes; it does not replace any worker's shard review.

The cache contains 25 official reference payloads: 23 fresh HTTPS captures and
two reused immutable EBI OLS captures. Fresh requests completed between
2026-11-08 04:22:08 and 04:22:49 UTC. The reused CHEBI:29377 and CHEBI:9532 payloads
retain their original November 1 retrieval times and checked provenance hashes;
they are not described as new live observations. All 17 captured ontology records,
including the historical thiamine chloride contrast, have `is_obsolete: false`
in the captured bytes. This is not a general claim that every related ID is valid.

Start with [owner-reference-index.json](owner-reference-index.json): it binds
each owner path/hash to the exact primary evidence IDs and specific applicability
limits. [primary-records.json](primary-records.json) records each exact URL,
retrieval time, raw payload path/hash, locator and inspected reference fields.
Raw owner snapshots are under `owners/`; successful fresh response bodies and
HTTP metadata are under `network-attempt-v2/` and `referenced-cas-attempt-v3/`.
Two reused official payloads are under `captures/` with provenance in
[reused-captures-v1.json](reused-captures-v1.json).

Important boundaries retained for reviewers:

- The sodium carbonate compound and stock-solution owners remain distinct.
  CHEBI:29377 describes a solute; it does not establish a stock's formulation.
- CHEBI:176843 is a cobalamin-vitamer class. The recorded CAS query returns a
  specific PubChem structure; it does not choose a vitamer for generic source text.
- FOODON:03315720 is a hydrolyzed vegetable-protein category, not proof that
  commercial soy peptones, suppliers or digestion processes are interchangeable.
- TAPS sodium salt retains its CAS identity and existing narrow parent relation.
  The acid term and the recorded salt CID are cached separately. Hydrate terms
  likewise retain their explicit hydration; no source hydration is guessed.
- Thiamine pyrophosphate is an **already recorded mapping concern**, not a new
  identity decision or duplicate issue. The current native export's position2792
  is WITHHOLD. Its formula/SMILES/InChI contain chloride while CHEBI:9532 does not.
  Historical #319 deliberately moved this owner from the chloride term to
  CHEBI:9532; #320 treats its CAS relationship as conjugate-base reasoning. The
  recorded CAS136-09-4 query returns PubChem CID5431 with a chloride-free formula
  and InChI. Its aggregated synonym list also contains a chloride-labelled name:
  that string must not be used as chloride evidence. The separate stock owner
  `02_Thiamine_Pyrophosphate` was the subject of #268's stock cleanup. Workers05/09
  still own per-case supplied-form review; the cache selects no correction.

[reference-flags.json](reference-flags.json) gives the precise field comparisons,
source locators and historical limits. The saved issue histories are coordinator
context, not primary chemistry evidence. The 20 exact native disposition lines
for these owners retain 19 WITHHOLD and one SUPPORTED; no status is conferred on
the source cases by copying those lines. Historical CAS wording in a review reason
does not override the primary records or the documented prior decision.

Failed attempts are preserved separately from usable evidence: three web-tool
URL failures and 19 initial DNS-failed requests. The latter produced empty bodies
and error metadata; those files are **not primary evidence**. Subsequent network
captures succeeded and each payload was checked for the requested exact ontology
ID or explicit CID. CAS queries were checked against their returned CID and exact
CAS synonym. A PubChem synonym remains a depositor-supplied cross-reference, not
independent CAS Registry certification or an alias approval. No paid provider was
used. No authoritative supplier product was inferred from an uncited product name.

`MANIFEST.json` hashes the complete cache inputs, helpers, raw captures and derived
indexes, excluding itself and the final verification receipt. The offline check
can be rerun with the existing maintained Python 3.13 environment:

```sh
PYTHONDONTWRITEBYTECODE=1 ../kgm-unmapped-20261107/env/bin/python \
  evidence-cache/shared-owner-primary-v1/verify_cache_v1.py
```

Run that command from the campaign root. An offline structural check validates
saved bytes and references only; scientific applicability and independent review
remain with the assigned workers and coordinator. The original MIM, KG and
CultureMech sources, workers, ledger, GitHub and tmux were not changed by this task.
