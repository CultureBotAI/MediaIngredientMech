# Step 2 execution evidence: exact NCIT heptahydrate (#875)

This snapshot records the guarded application of the approved exact
`NCIT:C61946` identity, paired rejection-ledger migration, native candidate
generation, bounded SSSOM promotion, and native mapping receipt sequence 16.
The mapping remains **WITHHOLD**. No scientific approval is added; the inherited
anhydrous structure and provisional BUFFER evidence remain open.

The [original README](../README.md) and [primary NCI evidence](../sources/ncit-C61946.json)
are frozen pre-application files. Their instructions and pending checks describe
that earlier point in time. This execution snapshot documents what actually
ran through receipt publication. Later full QC, regenerated-surface checks,
independent review, and any final-head evidence must be appended separately.
This author-authored package does not claim independent review.

## What changed

The [source receipt](application/source-apply.json) binds the one corrected
record and coupled ledger row. It records the actual Codex/GPT-6 event with LLM
assistance. Read-only [snapshot checks](snapshot-checks.json) confirm that the
entire earlier history remains a prefix and that only one ledger line changed.
The [bounded promotion receipt](application/mapping-promotion.json) records one
changed ontology row and one removed obsolete registry row. Every unrelated
SSSOM data line is byte-identical to the durable baseline.

| Table | Data rows | SHA256 |
| --- | ---: | --- |
| Baseline canonical | 2,987 | `a2b83ccdcaad67d89943ccf0f0e30d796cdbc5e418ead247313631b713e89722` |
| Full native diagnostic candidate | 2,979 | `fc7401ab99f2a6d8f31fc695d74b670dee8f61f63bc4dbcde33797caf3f11136` |
| Bounded canonical result | 2,986 | `68552edd452d5dccf1262b5d03190a6b668341952a554f349149f269403cca67` |

The full native candidate was **not** promoted wholesale. Compare the target
[before rows](excerpts/before-target.tsv), [native candidate row](excerpts/candidate-target.tsv),
and [canonical row](excerpts/canonical-target.tsv). These are extracted rows,
not full SSSOM documents. Canonical promotion retains the old CHEBI/KG source
tokens as historical provenance; they do not independently support the new
NCIT identity. The active row uses the native candidate's comment, not the
obsolete registry explanation, and inherits no ChEBI validation stamp.

The [publication receipt](application/receipt-publication.json) binds native
[sequence 16](../../sssom_completion_20260921/mapping_changes/issue875-ncit-exact-heptahydrate.json)
and the unchanged hashes of the 15 earlier receipts. Its approval is NONE.
The content-bound [mapping-review excerpt](excerpts/mapping-review-target.json)
confirms WITHHOLD for the new row. That excerpt preserves the old review reason
verbatim, including superseded CAS-promotion wording; the chosen identity is
the approved exact NCIT term. Chemistry/BUFFER and fresh mapping-specific
review remain unresolved.

## Generation and validation limits

The [generation receipt](generation/generation-receipt.json) binds the clean
Claw producer revision `0cc221bd0f4eb460030eb2e5d14b91a311ed2965`, the actual
[generation harness](harnesses/generate_candidate.py), candidate hash, and
label captures. The [before](generation/inputs-before.json) and
[after](generation/inputs-after.json) input manifests are byte-identical.
The four `label-input-*.json` files preserve the native CHEBI/OLS loader returns;
they are not replacements injected into the producer. The official
[NCI fetch receipt](../sources/ncit-C61946-receipt.json) and separate
[read-only NCIT cache probe](preflight/ncit-C61946-local-readonly.json) preserve
their distinct access dates and ontology versions (EVS 26.10d, local 26.02d).

The [native invariant receipt](generation/native-invariants/receipt.json)
reports zero rejects on the diagnostic candidate. B4 used the actual read-only
KG ontology directory, but **skipped BTO and MICRO** because their transforms
were absent. The [ID/label log](logs/step2-candidate-labels.log) reports 2,216
canonical, 4 synonym and 4 exception pairs, with **3,734 pairs skipped for lack
of an adapter** and zero flagged pairs. A zero-reject/zero-flag result therefore
does not establish complete ontology coverage. The [CURIE check](logs/step2-candidate-curies.log)
checks syntax and known prefixes, not scientific identity.

The [repository context](generation/repository-context.json) records actual
checkout identities and dirty state at generation. The
[comparison-input list](generation/comparison-inputs.json) hashes CultureMech
outputs and Mediadive nodes as comparison-only inputs: the raw SSSOM builder
did not consume them. Optional residual input was absent, as recorded by the
generation receipt. These are captured execution facts, not claims about later
checkout state.

## Writer checks and portable use

The [focused run](logs/step2-writer-focused-green.log) passed 35 tests with the
committed-surface test deselected. The separately retained
[pre-application red test](logs/step2-writer-committed-preapply-red.log) failed
as expected before production application and regeneration; it is not a final
green check. The [mutation results](writer/mutation-results.json) and individual
logs record a fresh-process positive control and six negative controls: omitted
ledger migration, lost history, lost historical sources, inherited validation
stamp, ignored input race, and ignored candidate hash. Each mutant failed.
[The harness](writer/run_mutations.py) records the exact substitutions.

Raw execution logs and their JSON wrappers are copied byte-for-byte. The
[artifact index](artifact-locations.json) maps historical absolute paths to
portable packaged paths and identifies files intentionally not duplicated.
Large candidate/canonical tables, external databases, and native recovery
journals remain hash-indexed; this is not a self-contained regeneration archive.
The baseline canonical table is recoverable with `git show` at durable commit
`40b787d37d33d544551389ff019f2d64ad63d7cc`. The current canonical table, owner,
ledger, writer/tests, and native receipt are maintained elsewhere in this same
repository. The archived harnesses retain their run-specific paths and require
explicit environment adaptation before reuse.

[Preflight probes](preflight/producer-compatibility-probes.json) are explicitly
hypothetical compatibility checks and do not establish production application.
[The writer source freeze](writer/stable-inputs.json) predates application;
its `production_application_performed: false` describes that time, not the
later source/promotion receipts.

The [inventory](inventory.json) hashes every file in this report at packaging
time, including the unchanged original files. Verify the archived bytes with:

```bash
python reports/ncit_heptahydrate_875_20261101/execution/verify_inventory.py
```

The verifier reads files only. It grants no approval and does not run a
generator, apply a record change, or replace final QC and independent review.
