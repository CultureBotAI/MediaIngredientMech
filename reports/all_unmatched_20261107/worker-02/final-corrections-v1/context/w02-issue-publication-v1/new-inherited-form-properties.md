# Correct three inherited chemical-property blocks that contradict the stated substance form

Reviewed W02 head `0597d00417be4d7cdfb5a31970043eec9bbc88fe`, frozen campaign base `e000d66dd26ab053e9b17ce7bf8d3c873c3dde99`. Authoritative peer review is `assembly-v2/review.yaml` (SHA256 `31cac38cae0cfb3dcfae4453a01402dc98d249f70ad9a7698a89b25eed5eae11`) in the sealed W04 independent W02 packet, whose 2,399-member SHA256SUMS is `99306617655b1e3df84368079e49f4341a0fd05667bdf9fedf18dda24f4f7ca7`. The coordinator verified all manifest members, rebound all188 case decisions and106 selected payloads, and independently repeated all106 native guarded writes and baseline/overlay partonomy. Structural validation passes; the scientific verdict remains needs_curation. These are unapplied proposal corrections, not changes already made to main or whole-owner/export approval.

`W02-F-INHERITED-PROPERTIES` (`W02C-006`, `w02-external-b-012`) concerns existing baseline fields, not newly introduced source aliases. Exact targets:

| Owner / frozen SHA256 | Contradiction |
|---|---|
| `L-Malic_Acid_Disodium_Salt_Monohydrate.yaml` / `4896efa3f3c06d572e3bf8dffffb131ab36f1e1a31fac75394acca8db7c43080` | Identity cas:207511-06-6 states L-disodium monohydrate, but formula C4H4NaO5−, PubChem197014 and stored structure carry one sodium, no water and unspecified stereochemistry. |
| `Coso4_X_7_H2o.yaml` / `3e14e4d57dab11eb3974f45db2894b12bd71aa7a761d823ae8ce401300ceba8d` | CHEBI:91244/formula/CAS state heptahydrate; InChI and SMILES describe anhydrous cobalt sulfate and are attributed to CHEBI53470. |
| `Voso4_X_N_H2o.yaml` / `bd15f57d4e547908edcffa874470f4cc2adfe672002fe3532be67c30e63caeaf` | Variable-n hydrate formula coexists with one-water InChI/SMILES copied from CHEBI87020 metadata. The ontology's same internal inconsistency is not independent evidence fixing n=1. |

Independently verify a form-specific property source, replacing only demonstrably exact supported fields; otherwise withdraw unsupported structure/CID/formula fields with preserved historical provenance. No generated structure, inferred fixed water count, stereochemistry or CAS reassignment is authorized. Retain valid identity/form evidence and record-level holds.

The complete baseline fields are preserved in W02C-006. Captured [CHEBI91244](https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:91244) SHA256 `c8bf30f1c2b4e9c2bcc10bd256b68a090795c083c207baf2d9d9ebb201d0d3c5`; [CHEBI87020](https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:87020) `fbf850a3ccae6ed0e62d3e78d0da4bd252a51af85a59c3d70294801eef4adaeb`. Reinspect exact malate registry/form evidence before any replacement; the current contradictory atom count does not license choosing a new identity.

Deduplication: closed871's fourteen repaired owners are a different set;315/321 preserve historical identity corrections, and321's recent comment concerns nickel properties, not these three blocks.268 is the general derived-chemistry mechanism;1220 owns a separate pentahydrate vanadyl alias/source question. Fresh exact-owner and comment searches found no tracker documenting these three current field corrections. Link those histories without reopening their successful identity fixes.

Preserve published original payloads/reviews, capture timestamps, histories, rejected text and all precise source/form/role/release holds. Prepare immutable corrected proposals through existing guarded validation, record claim-specific changes, and obtain independent review of the exact successor. No corpus application, owner merge, gate/schema/test/producer change or approval transfer follows from this issue.
