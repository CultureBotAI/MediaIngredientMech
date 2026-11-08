Title: Correct the tellurium dioxide proposal parent grade before native publication

Worker05 reported **W05-FINAL-CHEM-NEW-01** before fixing it; an independent read-only reproduction confirms a record-grade defect in isolated proposal `CHEM-C1193-tellurium-dioxide`. Its exact payload SHA256 is `d25ae183c58c8616ecff3fd43dfb4615cb30d4df94e8a17399f09c2de3b20e98`, published under head `43f7cf6e8681fa617b5d6d3529d94d537ca01f0d` at `reports/all_unmatched_20261107/worker-05/correction-1193-v1/chemicals/proposed/Tellurium_Dioxide.yaml`, intended new owner `data/ingredients/mapped/Tellurium_Dioxide.yaml`. The original proposal and referral remain immutable; no maintained record or mapping was changed.

The record preserves the exact compound identity `cas:7446-07-3` and uses `CHEBI:33305 tellurium molecular entity` as a broader class. It currently grades that relationship `BROAD_MATCH`. Under MAPPING_SEMANTICS§1/§3, the dioxide is the narrower entity, so the intended asymmetric parent relation requires `NARROW_MATCH`. This is not a request to change the producer's global BROAD_MATCH behavior.

| Actual native projection | Parent relation | Exact registry identities |
| --- | --- | --- |
| Current BROAD_MATCH | closeMatch CHEBI:33305 | cas:7446-07-3 |
| Only grade changed in memory to NARROW_MATCH | broadMatch CHEBI:33305 | cas:7446-07-3 and kgmicrobe.compound:tellurium_dioxide |

The unchanged pinned Claw76c1ebee builder SHA256 `38d59f42953305f6fc51e4fc24dfc59ee1919bfb961595b67a8afe9f8a46a1bc` reproduces both sets exactly. The corrected output additionally places the CAS display token on registry rows, rather than the asymmetric parent row. Review the complete three-row native output; do not substitute one hand-edited predicate cell.

Primary scope remains precise. [CCAP UCM](https://www.ccap.ac.uk/wp-content/uploads/MR_UCM.pdf), PDF SHA256 `29ffa5707345821ccd91e72e7e633652e5364ed04283b42a63b683f09c0006a9`, names TeO2 both in primary trace stock4 (0.034g per100mL with NaOH) and the separate diluted trace stock (0.000034g/L). Its final growth-medium dilution is a further level. The two frozen occurrences belong to those nested source contexts; they are not two independently known final-medium doses. [NITE](https://www.chem-info.nite.go.jp/chem/english/ghs/m-nite-7446-07-3e.html) confirms tellurium dioxide/CAS7446-07-3, and [PubChem62638](https://pubchem.ncbi.nlm.nih.gov/compound/62638) corroborates the dioxide. Preserve the exact compound, raw TeO as rejected provenance, and all source/export/role holds. Do not identify it with elemental tellurium, tellurite, or globally normalize TeO (which can denote monoxide elsewhere).

Append truthful grade-correction history to a new isolated successor after filing; keep the original evidence and quantities intact. §0 does not make this class grounding an exact CAS-to-ontology resolution merely because the distinct compound has a CAS number. Reassess exact-term priority if new evidence establishes an exact term; the original finite searches are not proof of universal ontology absence. Independently review corrected whole bytes and all native rows. The separate new human-only MappingEvidence entry is already covered by #1226 and must be handled honestly in the successor, without a global enum substitution or approval widening.

Deduplication: fresh all-state Tellurium searches including title/body/comments returned no issue. #1238 covers a separate Tris-hydrochloride proposal; #696 and #884 cover the broader grade/schema questions. Their full current bodies/comments were read. No schema, producer, gate, threshold, test or owner-selection change is requested. The original candidate can mechanically project its stored grade; this finding does not claim a current canonical QC failure.

Independent exact evidence: `C/preflight/tellurium-grade-triage-v1/native-reproduction.json`; original reporter receipt SHA256 `76ccc0c0664af7c6977197ebab41ec19c1637ba56c615209a93c2413e1d7bfdf`. Case `CM_NAME:d2520b55885554691a496b8a4aa2baa6ff0f1a1018f135591774ec22fdfc8416`. No source occurrence or downstream release is approved by this grade repair.

<!-- mim-fingerprints:w05-final-chem-new-01-tellurium-parent-grade -->
