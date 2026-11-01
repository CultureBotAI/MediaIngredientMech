At current main `4625afd492b6cf43e3b499d1425d2453d490009d`, `data/ingredients/mapped/Carnitine_Hydrochloride.yaml` retains the exact synonym `4-amino-2-hydroxy-N,N,N-trimethyl-4-oxobutan-1-aminium chloride` from its superseded carnitinamide mapping. The canonical SSSOM `MIM:Carnitine_Hydrochloride / skos:broadMatch / CHEBI:17126` row publishes it in `other`, and `docs/data/label_index.csv` resolves the name to carnitine hydrochloride.

The record's July 5 correction explicitly removed CHEBI:48601, CAS 461-05-2 and the amide chemistry. The synonym survived that correction. Fresh official [ChEBI:48601](https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:48601) assigns this exact IUPAC name to **carnitinamide chloride**, with formula C7H17N2O2.Cl. The current parent [ChEBI:17126](https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:17126) is carnitine, formula C7H15NO3. This is a different functional group, not one of the seven deferred generic-name/stereochemistry policy cases in #669.

Bounded correction:

- Retain this one name and its original `chebi_synonym_review` source as `REJECTED_LABEL`; append a sourced curation-history event through the native guarded writer.
- Preserve the current record identifier, mapping, status, occurrences, and unresolved salt/CAS/stereochemistry questions.
- Synchronize aggregate/export/SSSOM surfaces through native producers and content-bound mapping-change receipts. Withdraw inherited release support when owner bytes change; do not assign fresh approval.
- Check that the rejected name cannot resolve through the label index or appear in native regenerated `other`; validate the record and run the required data gates.

The target record is absent from the complete live #912 and #914 file lists, although shared aggregates/exports overlap and #912 includes canonical SSSOM. The correction must remain restricted to this record's subject block and generated dependent surfaces. No hydrate-family or unified-mapping work is included.

Pre-edit record SHA-256: `c123a3f76cf2277ca68a08c99e58f96845842fd90c75bdd19b90ab8db7bb6780`. Official OLS responses and exact row/pin evidence are saved in the current curation audit. Search for existing issues containing “carnitinamide” found only closed #114, which records the earlier identity correction; this issue records its remaining synonym defect.
