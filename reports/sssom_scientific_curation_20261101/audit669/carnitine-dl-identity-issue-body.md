`data/ingredients/mapped/Carnitine_Dl_Hydrochloride.yaml` at main `4625afd492b6cf43e3b499d1425d2453d490009d` names **Carnitine (Dl) Hydrochloride**, but its primary `cas:461-06-3`, formula `C7H15NO3`, PubChem CID 288, InChI and SMILES describe **DL-carnitine without chloride**. The record maps `NARROW_MATCH` to CHEBI:17126 and still has the free-base systematic synonym.

Fresh primary database checks on 2026-11-01:

- [PubChem CAS 461-06-3 query](https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/461-06-3/property/Title,MolecularFormula,InChI,InChIKey/JSON) returns CID 288, title DL-Carnitine, formula C7H15NO3.
- [ChEBI:17126](https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17126) is carnitine and carries the same CAS and formula.
- The record attributes the CAS to `CultureBotHT compounds_to_cas.csv` and its chemistry to automated PubChem backfill. Its current occurrence statistics are 0/0; this does not establish which supplied form the original label intended.

The contradiction is in primary identity, not merely in the broad parent mapping or `other` alias. Removing `DL-carnitine` from a generated synonym payload would hide one symptom without deciding what substance this record denotes. The sibling Carnitine_Hydrochloride's residual amide synonym is separately tracked in #1003 and does not resolve this CAS conflict.


Recommendation: trace the original CultureBotHT source/catalogue entry and an independently verified supplied form before choosing a replacement identity. If the salt name is supported, curate the salt-specific stable identifier and chemistry, retain the asymmetric parent and required identity rows, and refresh content-bound review receipts. If the supplied material was actually the parent, document that source-backed decision and reconcile the name/identity without losing raw source provenance. The automated name-derived CAS/chemistry is not independent evidence for choosing between these alternatives. Do not guess a replacement CAS, stereochemistry or merge.

Acceptance requires guarded curation/history, synchronized record/aggregate/SSSOM/label-index surfaces, preserved negative review holds, and native validation. No record edits are included in this finding. Neither target record is in the complete current #912 or #914 file list; shared aggregates and generated surfaces still require coordination.

This contradiction was listed as untracked in #887 and is related to the source-lookup risk in #235. Exact record-name and CAS issue searches found no dedicated open issue for this record. Historical #114 treated the parent mapping as acceptable; that does not validate the primary CAS identity. Keep #669 open pending this identity decision.
