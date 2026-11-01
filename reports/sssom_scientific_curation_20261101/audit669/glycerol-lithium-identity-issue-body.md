`data/ingredients/mapped/Sn-Glycerol_3-phosphate_Lithium_Salt.yaml` at main `4625afd492b6cf43e3b499d1425d2453d490009d` names **sn-Glycerol 3-phosphate lithium salt**, but its primary `cas:17989-41-2`, formula `C3H9O6P`, PubChem CID 439162, InChI and SMILES describe **sn-glycerol 3-phosphate without lithium**. The record maps `NARROW_MATCH` to CHEBI:15978.

Fresh primary database checks on 2026-11-01:

- [PubChem CAS 17989-41-2 query](https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/17989-41-2/property/Title,MolecularFormula,InChI,InChIKey/JSON) returns CID 439162, sn-glycerol 3-phosphate, formula C3H9O6P.
- [ChEBI:15978](https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15978) carries this same free-acid formula and CAS.
- The record attributes CAS to `CultureBotHT compounds_to_cas.csv` and structure to automated PubChem backfill. The current occurrence statistics are 0/0. Its carbon-source role is explicitly a provisional name-pattern prediction, not form identity evidence.

Earlier #232/#732 work retained two free-acid names as `REJECTED_LABEL`, explicitly leaving identity unadjudicated. The canonical `other` still contains `Glycerol 3-phosphate` under #669's baseline. Neither synonym retirement nor the existing broad parent mapping validates a lithium-salt identity. Any correction must also preserve or explicitly reassess the provisional role and its content-bound evidence; no role approval is implied here.


Recommendation: trace the original CultureBotHT source/catalogue entry and an independently verified supplied form before choosing a replacement identity. If the salt name is supported, curate the salt-specific stable identifier and chemistry, retain the asymmetric parent and required identity rows, and refresh content-bound review receipts. If the supplied material was actually the parent, document that source-backed decision and reconcile the name/identity without losing raw source provenance. The automated name-derived CAS/chemistry is not independent evidence for choosing between these alternatives. Do not guess a replacement CAS, stereochemistry or merge.

Acceptance requires guarded curation/history, synchronized record/aggregate/SSSOM/label-index surfaces, preserved negative review holds, and native validation. No record edits are included in this finding. Neither target record is in the complete current #912 or #914 file list; shared aggregates and generated surfaces still require coordination.

This contradiction was listed as untracked in #887 and is related to the source-lookup risk in #235. Exact record-name and CAS issue searches found no dedicated open issue for this record. Historical #114 treated the parent mapping as acceptable; that does not validate the primary CAS identity. Keep #669 open pending this identity decision.
