Worker04's frozen source review found a stoichiometry conflict that should be resolved by tracing source occurrences before changing the whole owner.

`data/ingredients/mapped/Mg-citrate.yaml` denotes CHEBI:131391 trimagnesium dicitrate / CAS 3344-18-1, but retains 1:1 magnesium-citrate properties and synonyms. Its exact bytes were checked against live `main` on 2026-11-08 at 05:13 UTC and match the assigned frozen baseline (SHA256 `6601f382062758877609574deeb7a2d72d9f0c6d693139b55ac031cfc6e2fb1f`).

[MediaDive ingredient404](https://mediadive.dsmz.de/ingredients/404) exposes CAS144-23-0, formula C6H6MgO7 and molecular weight214.413. The frozen source record's g/L-to-mM conversion agrees with that 1:1 representation. [CHEBI:131389](https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:131389) and [CHEBI:131391](https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:131391) distinguish 1:1 magnesium hydrogen citrate from 3:2 trimagnesium dicitrate. MediaDive's automatic metadata and derived conversion are mutually consistent, but are not independent procurement evidence.

The prior #320 decision and #353 implementation deliberately selected 3:2 using a name-preprocessed CAS. That history must remain visible. One later source record is insufficient to reverse all five occurrences represented by the owner.

Proposed follow-up:

- Trace all five owner occurrences to original recipes and supplier/CAS/form evidence, distinguishing observed reagent identity from automatic database enrichment.
- Propose a source-bound split or a fully justified reground. Reconcile identifier, ontology, CAS, formula, mass and aliases together; retain rejected provenance.
- Withdraw inherited complete-payload support for changed owners and run guarded synchronization, SSSOM and native complete-payload review at integration.

No owner change or hold release is proposed in worker04 for this case. Frozen case: `KG_CASE:6fd10b406feae9b043de0cb1b917ea47ac39dd6157b4170e26daab2fd5600a20`. Evidence, full prior comments and independent review are in `reports/all_unmatched_20261107/worker-04/` on branch `review/all-unmatched-w04-source-review-20261107` (campaign dependency #1158; coordinator integration pending).

Deduplication checked all current MIM issue/PR titles and bodies before filing; #320/#353 are historical context, not a currently open source404 split task. This finding does not supersede the campaign-wide publication hold in #1157.
