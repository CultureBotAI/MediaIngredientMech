The approved #669 rollout requires form review before merging `Nh42ni_So42` and `Nh42ni_So42_X_6_H2o`. Related: historical #334.

Both records currently use CHEBI:86149, the hexahydrate. The bare owner's CAS 56110-30-6 and structure were enriched from the selected mapping; the explicit owner uses 7785-20-8. The source claims need to be kept distinct:

- [PubChem's 56110-30-6 lookup](https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/56110-30-6/property/MolecularFormula,MolecularWeight,InChI,InChIKey,IUPACName/JSON) resolves to CID 182663, H20N2NiO14S2, a hexahydrate. Its depositor synonym list includes that CAS string.
- The [PubChem CAS annotation](https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/182663/JSON?heading=CAS) assigns 7785-20-8 through FDA GSRS Q5LM426K64. [ChEBI:86149](https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86149) and [Sigma 574988](https://www.sigmaaldrich.com/US/en/product/aldrich/574988) explicitly identify the hexahydrate with 7785-20-8.
- CAS Common Chemistry API access returned 401, so there is no direct registry response verifying 56110-30-6. The old claim that it necessarily denotes anhydrous material remains unverified.

Archived MediaDive concentrations for some bare-label sources fit roughly 394.99 g/mol. [NBRC 1199](https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1199), however, gives only the bare nickel formula, with no hydration, CAS or catalogue. Omitted water does not prove anhydrous identity. Supplier/NBRC evidence is inspected web extraction; the failed MediaDive compound endpoint responses provide no identity evidence.

For this rollout, SUPPRESS the explicit hexahydrate's preferred name from the bare owner's published `other`, with unchanged records and a sidecar. Preserve the explicit owner's existing rejected bare-formula alias; do not silently reverse it or invent a replacement CAS.

Options are an explicit evidence-backed convention that the generic-label cohort denotes the hexahydrate, permitting a guarded merge, or distinct forms if original preparation/product evidence supports them. Recommendation: retain suppression and leave this issue open until registry/depositor provenance and source scope are reconciled. A future merge must preserve history, negative decisions and union overlapping memberships; current shared IDs are not independent form evidence.
