---
name: add-uniprot-protein-examples
description: Assess and curate MediaIngredientMech UniProt protein references only
  through verified native maintained inputs and gates; report prerequisite gaps without
  changing generated or unsupported fields.
---

# MediaIngredientMech UniProt protein references

Read [native contract](../../../docs/CAUSAL_GRAPH_CONTRACT.md),
[the schema](../../../src/mediaingredientmech/schema/mediaingredientmech.yaml), current `CLAUDE.md`,
`justfile`, native validators and tests before deciding whether writes are
supported. `IngredientRecord.causal_graphs` uses graph-list nodes/edges. Each graph has
one supplied-form INGREDIENT anchor; chemistry bridges and role/sibling claims
must satisfy `MAPPING_SEMANTICS.md` section 7. NAMED_MEDIUM records cannot carry
graphs. Inventory both GENE_OR_PROTEIN and MOLECULAR_FUNCTION nodes: the schema
supports taxon-paired `protein_examples` on both. UniProt and organism instances
never replace generic node groundings.

## Verify prerequisites before applying

At the 2026-10-19 local checkout inspection, the contract marks semantic gate,
snapshots and graph writer/canary as planned; current inspected `justfile`, `src`
and `scripts` expose graph refresh receipts but no `qc-causal-graphs` gate.
Schema validity alone is insufficient to authorize mechanistic curation.

These are current-checkout observations, not permanent assertions about published
main. Search hidden/ignored source and existing branches for the required route;
when reporting current published capability, pin and inspect the published
revision. If another session has implemented it, read its writer, validator,
provenance and canary tests and prove reproduction before using it. Do not
silently cherry-pick, switch or overwrite the active session's checkout.

While prerequisites are absent, complete the useful source-grounded inventory,
claim review and proposed native graph/protein candidate table, with exact IDs,
source locators, source scope and unresolved representation requirements. Save
an honest blocked/partial assessment using the native record-review contract.
Keep the curation goal blocked rather than marking unsupported writes complete.
A separately authorized prerequisite implementation must add maintained inputs,
a validated writer, semantic checks, history, derived-output handling and a
round-trip/canary test before corpus application. Merely adding this skill does
not supply that implementation. Preserve generated records and native status.

After verified prerequisites land, follow the current native contract and
`curate-yaml-record`, run its focused and full gates, and record evidence that
new assertions survive regeneration. Use actual documented commands, not the
names of planned recipes.
## Protein identity and evidence

Inspect live UniProt entry metadata or a release-pinned, provenance-verifiable
native snapshot. Check primary accession and active/merged/deleted state,
organism and strain, sequence/isoform, gene/locus mapping and source identity.
Prefer an exact assayed protein over a convenient ortholog. A named gene alone
is not a unique protein match. Keep family, whole complex, individual subunit,
native protein and experimental construct distinct. UniProt identity metadata
supports identity; primary role evidence supports participation in the record's
mechanism. Retain the original accession and an explicit mapping rationale when
resolving a changed identifier. Do not silently substitute species or isoforms.
## Scope and completion

For one target, read the whole maintained record and its generated projection or
components. For a corpus goal, first freeze an inventory of record IDs, paths,
input hashes and applicable graph/protein elements; resume that ledger after an
interruption. Include hidden and ignored inputs when establishing absence.
Classify each target as checked, changed, evidence-limited, excluded, not
applicable or blocked, with reasons and inspected sources. A sample, a provider
report and a validator pass do not establish whole-corpus scientific completion.

Use [curate-yaml-record](../curate-yaml-record/SKILL.md) for the local evidence,
write, history and status contract; this adapter does not replace its managed
method. Record actual agent identity. Preserve scientific status rules and
unrelated edits. Use inspected primary evidence for mechanistic claims and exact
active identifiers for instances; never infer causality from association or
coverage from an empty query. A quotation is source text; interpretation belongs
in the native notes/explanation field.

Save final scientific assessments through
[review-yaml-record](../review-yaml-record/SKILL.md),
[record reviews](../../../docs/record-reviews.md), and the
[local profile](../../../docs/record-review-profile.md), including their native
persistence exceptions. Keep coverage/checkpoint accounting even when a clean
review should not produce a bundle. Unavailable prerequisites remain blocked;
a skipped target is not a completed enrichment. This skill authorizes no paid
provider call by itself.

After a completed goal, follow the user's authorized commit, push/PR,
adversarial review, issue/fix, merge and branch-cleanup sequence under the current
repository guidance. Carry forward existing authorization without asking again.
Use fresh required checks and native merge-queue rules. Verify actual merge and
landed content before deleting that feature branch or starting the next goal.
Only genuine review findings become issues; a no-diff goal needs a documented
no-op receipt rather than an artificial commit.
