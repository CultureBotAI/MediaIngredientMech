`Trimethylamine-hcl.yaml` retains `Methylamine-HCl` as an `EXACT_SYNONYM` of
`CHEBI:64700` (trimethylamine hydrochloride). Its history also records absorbing
`Methylamine-hcl.yaml` during the 2026-04-19 duplicate merge. This allows a
one-carbon methylamine salt label to resolve to a three-carbon trimethylamine
salt.

Observed on the campaign's frozen candidate baseline
`e000d66dd26ab053e9b17ce7bf8d3c873c3dde99` (unmerged dependency PR #1158):

- [Maintained owner](https://github.com/CultureBotAI/MediaIngredientMech/blob/e000d66dd26ab053e9b17ce7bf8d3c873c3dde99/data/ingredients/mapped/Trimethylamine-hcl.yaml)
- [ChEBI methylamine hydrochloride, CHEBI:59337](https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:59337), CAS 593-51-1, one carbon.
- [ChEBI trimethylamine hydrochloride, CHEBI:64700](https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:64700), CAS 593-81-7, three carbons.
- [DSMZ methylamine hydrochloride ingredient 278](https://www.bacmedia.dsmz.de/ingredients/278) explicitly includes the spelling `Methylamine-HCl`. Its automatically matched identifiers are corroboration, not the sole identity evidence.

This is an existing scientific finding, not a new claim of discovery:
`SEM:069f2686d478755f354c` remains `OPEN` in
`reports/semantic_review_20260921/resolution/finding-dispositions.tsv`; the
historical report is `reports/yaml_record_review/Trimethylamine-hcl.md`.
The earlier native reconciliation is
`20261011T024639Z-mim-reconcile-all-batch-12`. The current task prepares an
isolated correction proposal and preserves that lineage; it does not apply the
proposal or retire the historical finding.

Follow-up:

- Retain the original synonym text and source as `REJECTED_LABEL`, with a
  claim-specific history event and the two distinct chemical identities as
  evidence.
- Resolve the original methylamine occurrences separately before restoring or
  creating any methylamine owner. Do not infer historical occurrence counts or
  roles from the merged total.
- Integrate through the guarded writer, withdraw inherited review support for
  changed owner bytes, synchronize the maintained surfaces, and regenerate the
  canonical outputs in the coordinator's integration work.
- Verify that `Methylamine-HCl` no longer resolves to the trimethylamine owner
  or appears in its exported `other` tokens. Re-review the complete changed
  owner/publication payload before release.

No maintained data, selector, canonical SSSOM or downstream KG is changed by
worker-02. The assignment's source-specific holds remain in force.
