The maintained yeast-mannan record uses an organism as its material parent and carries molecular properties belonging to amylotetraose. This was independently verified during worker 10 of the authorized all-unmatched source-review campaign; no maintained data have been changed.

Affected owner: `data/ingredients/mapped/Mannan_From_Saccharomyces_Cerevisiae.yaml`, primary identifier `cas:9036-88-8`. The current `main` file was fetched through the GitHub contents API and is byte-identical to the frozen baseline `e000d66dd26ab053e9b17ce7bf8d3c873c3dde99`.

Before SHA256: `d207aa565406598234d8b79a8de8e92643e65d029caf513a1f760d72f3b3ad7f`.

### Verified defects and primary support

- The current `ontology_mapping` is `NCIT:C14271`, labelled *Saccharomyces cerevisiae*, with `NARROW_MATCH`. [The ontology record](https://www.ebi.ac.uk/ols4/api/ontologies/ncit/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FNCIT_C14271) denotes the organism, not a mannan material category. Source organism does not make the polymer a narrower kind of organism.
- The current `chemical_properties` contains PubChem CID `870`, formula `C24H42O21`, and its associated SMILES/InChI. [PubChem CID 870](https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/870/property/Title,MolecularFormula,IUPACName/JSON) is amylotetraose, also named alpha-1,4-tetraglucose. These finite glucooligosaccharide properties do not describe yeast mannan. The proposed payload removes those four active fields and preserves their exact old values in curation history.
- [The Sigma M7504 certificate](https://www.sigmaaldrich.cn/certificates/sapfs/PROD/sap/certificate_pdfs/COFA/Q14/M7504-5G0000507515.pdf) identifies mannan from *S. cerevisiae* with CAS `9036-88-8`. This supports retaining the material CAS; it does **not** establish that the source recipe used this supplier product or lot.
- [CHEBI:28808](https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_28808) supplies a broader mannan category. It is not asserted as an exact source-qualified identity. [TOGO M2313](https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2313) provides the case-specific `mannan (Saccharomyces cerevisiae)` label and alternative-carbon-source recipe context.

### Concrete proposal, not publication approval

Retain `cas:9036-88-8` and the yeast-source material boundary. Replace the organism parent with `CHEBI:28808` / `mannan`, retaining native `NARROW_MATCH` semantics and the resulting `skos:broadMatch` parent edge plus the required CAS registry identity sibling. Remove the unrelated molecular formula, SMILES, InChI and PubChem CID. Preserve original evidence/history as historical, superseded grounding. Add only the reviewed material label from this exact source case; do not merge with carob-seed mannan or infer a supplier product.

Exact proposal artifact: `reports/all_unmatched_20261107/worker-10/bio/owners/Mannan_From_Saccharomyces_Cerevisiae.after.yaml` on `review/all-unmatched-w10-source-review-20261107` (campaign handoff; publication awaits coordinator push).

Proposed SHA256: `3b54626f2e1a3f32a1b0ebc96e4f0261ec1a859db56524d28ef44fcaf71303e8`.

Independent skeptical review: `reports/all_unmatched_20261107/worker-10/reviews/kg-review-of-bio-v1.json`, reviewer `/root/kg_research`, covering case 128 and the exact proposed bytes. The proposed YAML passed the native strict closed-schema validator. Source captures retain URLs, original access times and hashes in `bio/evidence.json`.

**Full publication hold remains:** this issue does not approve inherited role assertions, process-qualified synonyms, the complete owner record, source-case resolution outside the reviewed context, or generated exports. Any implementation must reconcile concurrent owner proposals, withdraw inherited support for changed bytes, run the guarded native integration/synchronization/validation workflow, and review the complete final published payload. All existing source/material holds remain. No downstream rebuild or merge is part of this campaign.

### Duplicate check

A fresh complete visible all-state issue listing (634 results, requested limit 2000), live `mannan` discussion search, and current bodies/comments of #414, #321 and successor #218 were checked. #414/#218 concern historical duplicate identifiers, including the separate carob/yeast boundary; #321 concerns hydrate detection, with a carob-mannan false positive. Neither tracks this organism-parent plus amylotetraose-property correction. #587 concerns imported instruction-like synonyms and likewise does not cover it. These related boundaries are preserved; this report makes no claim that all mannan curation is new.
