Four source owners assert a broader descriptor, another molecule's chemistry, or a component class as though it described the supplied material. The worker-10 source review proposes bounded corrections while preserving existing release holds. These findings concern the frozen campaign baseline `e000d66dd26ab053e9b17ce7bf8d3c873c3dde99`; no maintained ingredient was edited.

## Findings and primary evidence

### Levorin descriptor collapse

Owner: `data/ingredients/mapped/Levorin.yaml`. Proposal: `kg-levorin-concept-scope`.

The owner uses MeSH D002174 as exact Candicidin identity. NLM's preferred Candicidin concept M0003252 explicitly has narrower Levorin concept M0352008; sharing the descriptor does not make those concepts chemically identical. Restore the historical local `kgmicrobe.compound:levorin` identity and retain Candicidin only with `NARROW_MATCH`, published as `skos:broadMatch`. The inherited `SINGLE_INGREDIENT` classification remains unadjudicated against antibiotic-complex scope. This proposal does not establish a specific candicidin molecular component.

Primary references: [kg-mesh_M0003252](https://id.nlm.nih.gov/mesh/M0003252.json); [kg-mesh_M0352008](https://id.nlm.nih.gov/mesh/M0352008.json).

### Ristocetin B inherited another molecule's structure

Owner: `data/ingredients/mapped/Ristocetin_B.yaml`. Proposal: `kg-ristocetin-b-parent-chemistry`.

The local B owner carries CHEBI:85129 parent-derived C95H110N8O44, InChI and SMILES. PubChem CID 90478637 identifies ristocetin B as C84H92N8O35, a different molecular composition. Remove the unsupported parent and borrowed structural fields; retain the local B identity with fallback registry mapping until a justified exact ontology/registry selection is available. Do not infer a CAS identity from aggregated synonyms. The already rejected `produces:ristocetin B` trait phrase stays rejected.

Primary references: [kg-pc_ristocetin_b](https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/90478637/property/InChI,InChIKey,IUPACName,MolecularFormula/JSON); [kg-pc_ristocetin_b_names](https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/90478637/synonyms/JSON); [kg-CHEBI_85129](https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_85129).

### Unsuffixed halomicin is an antibiotic mixture

Owner: `data/ingredients/mapped/Halomicin.yaml`. Proposal: `kg-halomicin-complex`.

The current local compound is classified as a single ingredient. Original patent US3511909A describes halomicin as at least four chromatographic components A, B, C and D. The unsuffixed source supports an undefined mixture with a `kgmicrobe.ingredient` identity, not a chosen component molecule. Preserve the original source provenance and do not invent component proportions or complete structures.

Primary references: [kg-halomicin_patent](https://patents.google.com/patent/US3511909A/en).

### ISP4 medium is not an inorganic salt

Owner: `data/ingredients/unmapped/Inorganic_Salts-starch_Agar.yaml`. Proposal: `kg-isp4-remove-salt-parent`.

The named inorganic salts-starch agar owner is grounded to the inorganic-salt class CHEBI:24839. Official JCM medium 58 lists starch, inorganic salts, trace salts, agar and water. Remove that invalid whole-medium parent while retaining the existing UNMAPPED named-medium owner. The bounded correction does not mint a new formulation or assign a component identity to the preparation.

Primary references: [kg-md1692](https://mediadive.dsmz.de/rest/ingredient/1692); [kg-jcm58](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=58); [kg-CHEBI_24839](https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_24839).

## Exact proposal artifacts

All paths below are relative to `reports/all_unmatched_20261107/worker-10/` on `review/all-unmatched-w10-source-review-20261107`. Source captures include URLs, retrieval times and SHA256 digests in `kg/evidence.json`. `kg/decisions.json` binds each claim to its frozen case. `reviews/root-review-of-kg-v1.json` independently assesses all 52 KG cases and nine bounded proposal deltas.

| Proposal | Baseline owner SHA256 | Proposed payload and SHA256 |
| --- | --- | --- |
| `kg-levorin-concept-scope` | `77cccb8ad35797ec34744abe85b0125c5783466a832ec52b7a3442e51cd441a4` | `kg/proposed/levorin-concept-scope.yaml`; `7490a66ecda86d31016fc8096b10a5b20f5da32803e3bdc19af55bc31da27079` |
| `kg-ristocetin-b-parent-chemistry` | `9630cba6e27f198278c5aa247dfc10bef5de0a07ea34991777913de887b1e1e6` | `kg/proposed/ristocetin-b-parent-chemistry.yaml`; `31f6897af214e673e8a859c1c2c14bd60e119a3a8c4373ae2266a3197ab4c3de` |
| `kg-halomicin-complex` | `8c0bad7398d8e43ee0812117f6d368303dc8c6a0ff5a2f098b976b565bf5ac5e` | `kg/proposed/halomicin-complex.yaml`; `61cc2355010ce9a7bea6d2e5534cbaad49ab443147a217346d9f37c3df4db09c` |
| `kg-isp4-remove-salt-parent` | `76a430265f543685167823888f68629d2cbfc652f6faced54387692517118178` | `kg/proposed/isp4-remove-salt-parent.yaml`; `70c4b138c58230159aa991533c6048a4503761e01853a0a54b7759b96eb76435` |

## Required follow-up and limits

Review the exact current owner bytes before applying the proposed deltas. If they have changed since the frozen baseline, reconcile those changes explicitly. Preserve every existing WITHHOLD, REJECTED_LABEL, source-context and downstream hold. Complete owner/role/publication assessment remains separate from these supported corrections. Structural LinkML validation of the proposal files does not establish scientific completeness.

Apply any accepted correction through the native guarded workflow with curation history, synchronized maintained surfaces, appropriate SSSOM updates and required validation. No owner merge, downstream rebuild, blanket alias activation or release approval is requested by this issue.

## Deduplication

The live all-state issue snapshot and relevant comments did not contain these four owner-specific defects. #312 is a broader historical research-versus-mapping conflict ledger, and #718 is the continuing withheld-claim umbrella. #703 already resolved process/trait synonyms; the ristocetin B finding here concerns borrowed chemistry and does not reopen that completed cleanup.

The checked GitHub issue snapshots and complete relevant comment payloads are retained under `context/kg-issue-*-live.json`; the all-state snapshot is `context/kg-issues-all-live.json`. The borax component dependency already belongs to #1168 and is excluded here.

<!-- mim-review-round: 20261108T052536Z-worker10-kg-source-review -->
<!-- mim-review-bundle: kg-owner-identity-defects -->
<!-- mim-fingerprints: fe1fee7bcc07e14a4f5b8844f107639a850c493503a496958427b78593e3709a,910bcb507fb663855394f924fd161272e30f1b4873d568fcce9e1d13baecfa68,0c2873cbb6dfb24d179ae919e2835e1ec3827a58bc00ee16780d81d885f47e91,6d896cbc3a4a0a45e474ffb328fe94c201c6e9922d7e99ae5c2f69ef077c1c1f -->
