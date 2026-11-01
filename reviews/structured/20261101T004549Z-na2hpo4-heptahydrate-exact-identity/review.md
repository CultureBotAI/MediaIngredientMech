# Exact heptahydrate identity audit for issue 875; application deferred to coordinated unified rebuild

- Review: 20261101T004549Z-na2hpo4-heptahydrate-exact-identity
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-11-01T00:44:46Z
- Finished UTC: 2026-11-01T00:45:49Z
- Reviewer: Codex /root/generator_audit (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact active NCIT:C61946 denotes the complete disodium hydrogenphosphate heptahydrate and outranks CAS fallback under Section 3 step 1. The current local identity and inherited anhydrous structures need curation. The protected PR914 unified rebuild requires coordination before atomic identity/ledger/receipt application. This partial review does not reassess BUFFER evidence or retire the broader historical findings.

## Scope And Provenance

One named record: whole-form identity, exact ontology alternative, chemical structure mismatch, current source occurrences/duplicate boundaries, prior decisions and precise PR914 coupling.

Selection: Issue875 names data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml; no corpus sampling or bulk approval.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 4625afd492b6cf43e3b499d1425d2453d490009d.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-e3a107cd8e4ae3b7 | data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml | maintained | Na2HPO4 x 7 H2O |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just validate-strict data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml --out ../audit875/strict-findings.tsv --workers 1 | passed | True | record-e3a107cd8e4ae3b7 | Native focused validation passed on the unchanged target. |
| just validate-terms data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml | passed | True | record-e3a107cd8e4ae3b7 | Native focused validation passed on the unchanged target. |
| Exact-form primary database record comparison | passed | True | record-e3a107cd8e4ae3b7 | Direct NCI, FDA, PubChem and ChEBI records were read and compared at their exact form scopes; the NCIT alternative is positively established. |
| CAS Common Chemistry access | unavailable | False | record-e3a107cd8e4ae3b7 | Page 403 and API 401; contents not inspected or used. NCI/FDA/PubChem provide the positive CAS association, and exact NCIT controls step 1. |
| Post-curation synchronized-surface and release gates | not_applicable | False | record-e3a107cd8e4ae3b7 | No curation was applied. The native mapping disposition and release gates are unchanged; this audit grants no publication approval. |

## Scientific And Domain Assessments

### Section 3 step 1 exact whole-form ontology identity

identity: supported. Targets: record-e3a107cd8e4ae3b7.

NCIT:C61946 is the evidence-backed exact heptahydrate identity; CAS7782-85-6 is corroborated chemistry metadata, not the preferred primary when this exact ontology term exists.

### Inherited anhydrous structures under heptahydrate formula

consistency: concern. Targets: record-e3a107cd8e4ae3b7.

Current InChI/SMILES reproduce CHEBI34683 without seven waters. PubChem supplies the matching whole-form structures; correction remains separate from the identity decision and has not been applied.

### Atomic identity and rejection-ledger update versus PR914 unified rebuild

ownership: concern. Targets: record-e3a107cd8e4ae3b7.

The target YAML and ledger row are not changed by PR914; shared aggregate paths alone are not overlap. The precise unified heptahydrate row and alias regeneration do overlap the protected rebuild. Preserve existing data until coordinated ownership is available.

### Pure compound, stock preparation and sibling hydrate boundaries

scope: supported. Targets: record-e3a107cd8e4ae3b7.

No second maintained record currently owns this exact CAS/NCIT identity in the ignored-inclusive scan. The 0.02 M stock and other hydrates retain distinct identities. Current occurrence differences are diagnostic and were not imported.

### Unreassessed role and historical bundled finding

evidence: unknown. Targets: record-e3a107cd8e4ae3b7.

BUFFER evidence is still provisional on the inspected YAML. Its scientific validity was not reassessed; neither SEM:cb9ec35166086d936f70 nor SEM:e9b3da7873e18001bfdc is retired by this narrower observation.

## Findings

### exact-form-identity: Use the exact NCIT heptahydrate identity after unified rebuild coordination

major / deferred / confirmed; issue key: mim-gh875-exact-heptahydrate-identity.

The exact active NCIT term supersedes the CAS-only option in issue875. Promotion must pair the maintained identity/grounding change with the rejection-ledger key/rationale, guarded history and content-bound SSSOM receipt. PR914 owns the intersecting unified row/rebuild.

Disposition: Scientific identity option is established; application deferred solely to the user-protected PR914 unified rebuild ownership, not to lack of exact-form evidence.

### anhydrous-structure: Heptahydrate record still carries anhydrous InChI and SMILES

major / open / confirmed; issue key: mim-heptahydrate-inherited-anhydrous-structure.

The record formula includes seven waters, but its stored structures equal the anhydrous ChEBI parent. Exact PubChem heptahydrate structures are available. This confirms the structure subclaim without closing the broader legacy finding or its role scope.

## Recommended Actions And Acceptance Checks

### coordinate-unified

Coordinate the exact identity and unified rebuild ownership with PR914 before application; alternatively retain this evidence-only result until that work lands.

- Demonstrate a disjoint or agreed same-row update for the unified heptahydrate rows and provenance.
- Do not infer a conflict merely from sharing mapped_ingredients.yaml or the rejection-ledger path.

### apply-exact-identity

Use the guarded writer to promote primary and exact ontology mapping to NCIT:C61946, append honest LLM-assisted history, preserve form-specific synonyms, update ledger mim_id/rationale atomically, synchronize aggregate/exports, and use the native SSSOM receipt chain.

- Keep CHEBI:34683 rejected as unified identity; whole NCIT identity is exact and any separately retained parent relation has its own supported scope.
- Run validate-all, qc-sssom, qc-roundtrip, qc-flat-coverage, qc-evidence, audit-writers and applicable native mapping receipt/review checks.
- Do not carry scientific approval onto changed/new rows without a new content-bound review.

### correct-structure

Separately review and apply the exact seven-water PubChem structures through the guarded writer with claim-level source provenance, retaining unrelated fields and history.

- Verify the target CAS, hydration state, formula, InChI and SMILES all denote the same seven-water form.
- Synchronize maintained surfaces and pass native validation/export gates.
- Keep BUFFER and broader bundled SEM finding open unless each remaining claim is independently addressed.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| target | data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml; identifier; ontology_mapping; chemical_properties; physicochemical_roles; curation_history | supports | The maintained record preserves a distinct seven-water local identity and CLOSE_MATCH to anhydrous CHEBI:34683, but its InChI/SMILES contain no waters. BUFFER has only explicitly provisional computational evidence. |
| semantics | MAPPING_SEMANTICS.md; Section 3, decision procedure steps 1-3; Section 2 identity and registry rules | supports | Use the exact ontology term before the CAS fallback; distinct hydration states must retain their own identity. |
| ncit | https://api-evsrest.nci.nih.gov/api/v1/concept/ncit/C61946?include=full; reports/sssom_scientific_curation_20261101/audit875/sources/ncit-C61946.json: name, active, version and properties | supports | NCIT:C61946 is active in 26.10d, names Sodium Phosphate, Dibasic, Heptahydrate and records CAS 7782-85-6, formula 2Na.HO4P.7H2O and FDA UNII 70WT22SF4B. |
| fda | https://precision.fda.gov/uniisearch/srs/unii/70WT22SF4B; reports/sssom_scientific_curation_20261101/audit875/sources/fda-unii.html | supports | FDA identifies the dibasic heptahydrate, its CAS and seven-water formula, and links NCIT:C61946. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/6096963/property/MolecularFormula,MolecularWeight,InChI,InChIKey,CanonicalSMILES/JSON; reports/sssom_scientific_curation_20261101/audit875/sources/pubchem-properties.json; CAS resolution in pubchem-cas-resolve.json | supports | CAS resolution returns CID6096963; formula H15Na2O11P, mass 268.07 and structure include seven waters. FDA-linked CID517013 gives the same formula and InChIKey. |
| chebi-parent | https://www.ebi.ac.uk/chebi/CHEBI:34683; reports/sssom_scientific_curation_20261101/audit875/sources/chebi-parent.json: chemical_data and structure | supports | CHEBI:34683 is the anhydrous salt. Its InChI and SMILES match the currently inherited record values, which do not represent the whole heptahydrate. |
| bounded-search | reports/sssom_scientific_curation_20261101/audit875/sources/exact-terms-fetch-manifest.json; OLS ChEBI response snapshots; primary-fetch-manifest.json for earlier CAS/exact-name queries | partial | No exact ChEBI heptahydrate was found in the retained query results; a specific exact NCIT term was positively found. CAS Common Chemistry page/API returned 403/401 and were not used as chemical evidence. |
| occurrences-duplicates | reports/sssom_scientific_curation_20261101/audit875/record-and-occurrence-audit.json; duplicate_hits, current_culturemech and aggregate comparison; current-culturemech-occurrences.tsv; original full-input hashes in input-manifest.json | partial | The target alone currently owns CAS 7782-85-6; the 0.02 M stock is a distinct preparation. Thirty-five explicit heptahydrate occurrences in 35 recipes include 32 local IDs, two unresolved IDs and one stale anhydrous ID. The cached YAML count is 26; the audit changed no count. |
| prior-decisions | reports/sssom_scientific_curation_20261101/audit875/audit875.json; prior_decisions; sources/issue-863.json, issue-334.json, issue-459.json contain full inspected bodies/comments | context_only | #863 withdrew the stale anhydrous kg_microbe_node_id and deferred primary promotion and structure correction; #334 documented CAS scrambling; #459 distinguished ontology coverage absence from chemical impossibility and warned against formula-only identity inference. |
| pr914 | https://github.com/CultureBotAI/MediaIngredientMech/pull/914; reports/sssom_scientific_curation_20261101/audit875/sources/pr-914.diff at 8dc2f266ebf72959a5d2f601d1c767c9138db44f | supports | The target record and its aggregate hunk are unmodified; its rejection-ledger row is unchanged diff context. The same unified Na2HPO4 x 7 H2O row changes 19 to 28 occurrences while retaining the local identifier. An identity promotion would affect that row and aliases and require the explicitly protected unified rebuild. |
| ledger | mappings/unified_mapping_rejections.tsv; ingredient_name=Na2HPO4 x 7 H2O; rejected_id=CHEBI:34683 | supports | The existing rejection is keyed to the local MIM identity. Any promotion must change mim_id and outdated rationale atomically; retain rejection of anhydrous CHEBI:34683 as a unified exact identity. |
| legacy | reviews/structured/20261017T083000Z-na2hpo4-x-7-h2o/review.yaml; assessment a-efe7ca97594ee880; finding rec-f-e076a032ff4695c0; legacy SEM:cb9ec35166086d936f70 and SEM:e9b3da7873e18001bfdc | context_only | The historical identity/structure/BUFFER concern remains broader than this audit. The existing role finding remains open; this focused identity evidence neither supersedes it nor closes the bundled SEM finding. |
| validation | reports/sssom_scientific_curation_20261101/audit875/logs/audit875_strict.json; audit875_strict and audit875_terms JSON/log pairs | context_only | Both focused native validators exited zero on this unchanged record. Structural and term-label validity do not establish exact hydrate identity. |

## Limits And Additional Notes

- Partial scientific scope: exact-form identity and structure only; BUFFER role support and all broader scientific claims were not re-reviewed.
- CAS Common Chemistry page/API were unavailable (403/401); exact NCIT/FDA/PubChem evidence was inspected directly instead.
- ChEBI absence is bounded to the recorded searches and returned results.
- The PR914 conflict is tied to inspected head 8dc2f266ebf72959a5d2f601d1c767c9138db44f; recheck live state before application.
- No curated YAML, aggregates, SSSOM, rejection ledger, scientific dispositions or source occurrence counts were changed by this review.
- This review neither supersedes the previous role review nor closes SEM:cb9ec35166086d936f70; no release approval follows from a validated review bundle.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261101T004549Z-na2hpo4-heptahydrate-exact-identity
kind: record
repository: CultureBotAI/MediaIngredientMech
title: Exact heptahydrate identity audit for issue 875; application deferred to coordinated
  unified rebuild
started_at: '2026-11-01T00:44:46Z'
finished_at: '2026-11-01T00:45:49Z'
reviewer:
  identity: Codex /root/generator_audit
  kind: agent
  independence: independent
  independence_basis: Delegated read-only scientific audit; reviewer did not author
    or mutate the maintained ingredient, aggregate, SSSOM or rejection ledger. This
    bundle preserves the same agent's earlier primary-source audit; it is not a second
    independent review of that audit.
skill: curate-yaml-record
completion: partial
verdict: needs_curation
scientific_review: true
native_verdict: MAPPED unchanged; identity evidence supports NCIT:C61946; application
  deferred; no native release disposition changed
summary: Exact active NCIT:C61946 denotes the complete disodium hydrogenphosphate
  heptahydrate and outranks CAS fallback under Section 3 step 1. The current local
  identity and inherited anhydrous structures need curation. The protected PR914 unified
  rebuild requires coordination before atomic identity/ledger/receipt application.
  This partial review does not reassess BUFFER evidence or retire the broader historical
  findings.
source:
  git_revision: 4625afd492b6cf43e3b499d1425d2453d490009d
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/SKILL.md
    sha256: 4ea8fcaf92b4c05f17c6bee8daa9485bc58da1bb93103a53a582dc1a891b6f7a
    role: context
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: d4df94935abfd922e84c3512e9a9b7735240f8e266d9a3ae23bb4933926b04eb
    role: context
  - path: AGENTS.md
    sha256: fc7728986d82b43359a9055ae233bcf0d4ebaef8bb657ef1b4bb4aa87b2cbaaf
    role: context
  - path: MAPPING_SEMANTICS.md
    sha256: 94aad13ea0fc3df82a37383f388f41432b607b04cac61ae5792ce1a381aef805
    role: context
  - path: data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml
    sha256: e4f20bded8bb984f76d381636cf79b522983413046bf24bc6168e1065c027636
    role: target
  - path: mappings/unified_mapping_rejections.tsv
    sha256: 44b1dca360302189ea218d9faacdf0fef21c18bfe4e3e71c57abe3b3d0a75194
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit875/README.md
    sha256: 619690216563013bb3403210cbc88d45b7c2d79c37376e96cff8093025e00cd2
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit875/artifact-manifest.json
    sha256: 3b838bd3ef740167c06d4e5dcc5e382638e81c59d685cb8042382a55e7521b86
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit875/audit875.json
    sha256: 45478929846569b08ca13f66aa3d0e1f440329952d973c88b47d225a8f02ac5b
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit875/audit875.md
    sha256: c21930fcf257a5eb3552f0b56e2bf96106dc3c629b27511b943543050f0b9c0f
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit875/audit_inputs.py
    sha256: 5eceecddfc48f1c88cc2ea45dad9a78ac7f615fc47b3bb3e4e25b68d0acca40b
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit875/current-culturemech-occurrences.tsv
    sha256: 2cb9daa815ed97faea50b35b8987a00eb3ca4864995d28a7a08830a9cb00c7c2
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit875/fetch_exact_terms.py
    sha256: f0d90b3597c3c3f796fda0cbab594bc24d4a96cb032c4a2d9ee00857be9cfd99
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit875/fetch_primary.py
    sha256: fc507833078348d9b0876f687f470d7c9a65bd5c8c0387b93c67adfeba5315e5
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit875/input-manifest.json
    sha256: b4992838a4e5ff7c775e1a37236ced9d235c59815696723a42bb48735ba673ac
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit875/issue-875-after-comment.json
    sha256: 0c70227eef543f37dd75b79466df3ec0ee066404c85aca654be6077fb7df91ca
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit875/issue-875-before-comment.json
    sha256: 4a97e622784a30b2b094d3ebdf38013ad5ee617ffa67369af08d2415d78e4983
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit875/issue-comment-receipt.json
    sha256: 1178989db9bab555b1a22d5d44523a21f71b8659195fe05e732ef74570305839
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit875/issue-comment.md
    sha256: 502b4567063f0a0709363cb48f0d62a700649439513b9556ba6ea459a9838f6c
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit875/logs/audit875_strict.json
    sha256: beb001c68b5f9dd6898dca634fbc15f3b5f0571f8f5627697f6d804cef2d3f7b
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit875/logs/audit875_strict.log
    sha256: cee1bb42e33fab58f8fcb03b5f39b326af10fa9bb6c886e25cbb751744691085
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit875/logs/audit875_terms.json
    sha256: 10d72b733a14088d010e086b5acd5731bc255d29c119922541967f88c8d89e6f
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit875/logs/audit875_terms.log
    sha256: 23acda1c1d3194d12bc947d897d07de83f4a076a9d93c135148885108530e018
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit875/publication-manifest.json
    sha256: e7170a3bca43cb7968476945b6b605d71ce5962a7a5ca60b79ead621b2823c49
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit875/record-and-occurrence-audit.json
    sha256: b00de89b2cf70e3dec4881d7c3ff635b2a5f6bc1ac3a434ef0b7e13b357fa99f
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit875/sources/cas-commonchemistry.json
    sha256: 3e7db788e384631f8a9f299d1797e6f8af6d16d643a1c91f9e83ae15212de45c
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit875/sources/chebi-parent.json
    sha256: a6714f1020f587eff8a2152ff43ba19c0919ad541b08b5463f008a9e321d6fdc
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit875/sources/exact-terms-fetch-manifest.json
    sha256: 4864e94fcc431ac127208eab64852728a13f3663293352ce760aab0b10ecb872
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit875/sources/fda-unii.html
    sha256: ef1403c101974019957c9747d7b386d245693fa7c3be9c7e9bbf39878b0d504a
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit875/sources/issue-334.json
    sha256: b49585d281931803c14ea6562f78b0052698055b4ba4e3c7fe88a3cd28c6d76c
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit875/sources/issue-459.json
    sha256: cc9cb7547a7031195f3c55a6492591284d77bf6087cf9075feef403f8fadf0b7
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit875/sources/issue-863.json
    sha256: 7bd9fe0618d6eb3959919432f5144bcd49274aff4a8967f0ef54627ea61151c8
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit875/sources/ncit-C61946.json
    sha256: a112c3e91dd6aa46feb112621ba5d13673df69f1b20665e042e22b8aa05a1d83
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit875/sources/ols-all-cas.json
    sha256: 8d33fdeb26a2d16294a3c5f4a7f444578bb462aa6036d45a15e9bfadfe47fbd2
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit875/sources/ols-chebi-cas.json
    sha256: 8d33fdeb26a2d16294a3c5f4a7f444578bb462aa6036d45a15e9bfadfe47fbd2
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit875/sources/ols-chebi-heptahydrate.json
    sha256: caf66db5caab18116377974d4eec11eef33be96271b8d0fbfb5ab2cd9240e966
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit875/sources/ols-chebi-hydrogenphosphate.json
    sha256: 72f41382c5e35efc6e54b57e2c96096ebeed03322f487eb16fd0d8ae32a3d16c
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit875/sources/ols-chebi-name.json
    sha256: 8d33fdeb26a2d16294a3c5f4a7f444578bb462aa6036d45a15e9bfadfe47fbd2
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit875/sources/ols-chebi-phosphate.json
    sha256: 088eceb810f1bbc9319641d1a608e7d58d46525943c9978a08eeed95006f6993
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit875/sources/ols-chebi-salt.json
    sha256: 1ada42eb282d3bf74b418a4e00c338a75b505d76ac384486557f82e2817be194
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit875/sources/ols-ncit-heptahydrate.json
    sha256: 7252875906a2f412a126f1b952716fd43d3e652b5855816a1a9b7732d9da6cea
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit875/sources/pr-914.diff
    sha256: d4b9a2348e26b0e93ae6fd03f8d3ac38dece1f0c08aed6d2bacb8d1e3df08ec3
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit875/sources/primary-fetch-manifest.json
    sha256: c4f6c7cc2bcf40e5ee874296beb58ad2728c027b8a29ea00f3d4361720796e5b
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit875/sources/pubchem-517013-properties.json
    sha256: 94899b2fe6271b954e9497c2f4919971117bdc07d4dae9c93f873c69fd14f892
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit875/sources/pubchem-cas-resolve.json
    sha256: e7683f2240e088bc2ca10527b932b84ab49811be8010ebaca6f153f2f898a5a9
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit875/sources/pubchem-properties.json
    sha256: 09d1ffc91f4fa882bf8a0ea562906640e98e1131609bf46106a7d67dcd88d320
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit875/sources/pubchem-synonyms.json
    sha256: a56deed6f3dc76159c464765c90978fa781ce0751ff3b465f5ba208ba1f0c38d
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit875/sources/web-primary-20261101.txt
    sha256: 103aaee99f6cfbae98294e9ae4894102ebe1510d370618f989980f8e089a9c27
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit875/strict-findings.tsv
    sha256: 4ccba8b77ce80cf210105b5284b5953747729aba576ccdeecb81f7db84eb721b
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit875/target-input.yaml
    sha256: e4f20bded8bb984f76d381636cf79b522983413046bf24bc6168e1065c027636
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit875/write_report.py
    sha256: 3e66e25bdb81484e67fda21fa18bd3a5d9aa162b0e572217af3d00015b52df9c
    role: context
  - path: reports/yaml_record_review/Na2hpo4_X_7_H2o.md
    sha256: 565644c80a0d16c2047d8d90c1c5c519918ac2c87a30007e28591f5d9d01cbac
    role: context
  - path: reviews/structured/20261017T083000Z-na2hpo4-x-7-h2o/review.yaml
    sha256: 414cf888064b1bbca184187cf4053288c063aeebada2cab885d4742a723c891c
    role: context
  - path: src/mediaingredientmech/schema/mediaingredientmech.yaml
    sha256: bb43dee29b21fdee72a48022456e733e49e95824c4c09674f9b3165c290fe012
    role: context
scope:
  description: 'One named record: whole-form identity, exact ontology alternative,
    chemical structure mismatch, current source occurrences/duplicate boundaries,
    prior decisions and precise PR914 coupling.'
  selection: Issue875 names data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml; no corpus
    sampling or bulk approval.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - record-e3a107cd8e4ae3b7
  exclusions:
  - target: physicochemical_roles[0] BUFFER
    reason: Existing provisional evidence and historical finding retained; no fresh
      role-literature review.
  - target: Other ingredient records, recipe-wide semantics and publication approval
    reason: Comparison hits inform duplicate boundaries only; no whole-record approval
      or downstream media review.
targets:
- target_id: record-e3a107cd8e4ae3b7
  path: data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml
  label: Na2HPO4 x 7 H2O
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml
    role: maintained ingredient; guarded writes only
checks:
- check_id: audit875_strict
  name: just validate-strict data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml --out ../audit875/strict-findings.tsv
    --workers 1
  status: passed
  required: true
  summary: Native focused validation passed on the unchanged target.
  target_ids:
  - record-e3a107cd8e4ae3b7
  command: just validate-strict data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml --out
    ../audit875/strict-findings.tsv --workers 1
  exit_code: 0
  evidence_ids:
  - validation
- check_id: audit875_terms
  name: just validate-terms data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml
  status: passed
  required: true
  summary: Native focused validation passed on the unchanged target.
  target_ids:
  - record-e3a107cd8e4ae3b7
  command: just validate-terms data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml
  exit_code: 0
  evidence_ids:
  - validation
- check_id: primary-identity
  name: Exact-form primary database record comparison
  status: passed
  required: true
  summary: Direct NCI, FDA, PubChem and ChEBI records were read and compared at their
    exact form scopes; the NCIT alternative is positively established.
  target_ids:
  - record-e3a107cd8e4ae3b7
  evidence_ids:
  - ncit
  - fda
  - pubchem
  - chebi-parent
- check_id: cas-commonchemistry
  name: CAS Common Chemistry access
  status: unavailable
  required: false
  summary: Page 403 and API 401; contents not inspected or used. NCI/FDA/PubChem provide
    the positive CAS association, and exact NCIT controls step 1.
  target_ids:
  - record-e3a107cd8e4ae3b7
  evidence_ids:
  - bounded-search
- check_id: application-gates
  name: Post-curation synchronized-surface and release gates
  status: not_applicable
  required: false
  summary: No curation was applied. The native mapping disposition and release gates
    are unchanged; this audit grants no publication approval.
  target_ids:
  - record-e3a107cd8e4ae3b7
  evidence_ids:
  - target
  - ledger
evidence:
- evidence_id: target
  kind: record_content
  reference: data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml
  locator: identifier; ontology_mapping; chemical_properties; physicochemical_roles;
    curation_history
  accessed_at: '2026-11-01T00:45:49Z'
  support: supports
  summary: The maintained record preserves a distinct seven-water local identity and
    CLOSE_MATCH to anhydrous CHEBI:34683, but its InChI/SMILES contain no waters.
    BUFFER has only explicitly provisional computational evidence.
  snapshot_sha256: e4f20bded8bb984f76d381636cf79b522983413046bf24bc6168e1065c027636
- evidence_id: semantics
  kind: authority
  reference: MAPPING_SEMANTICS.md
  locator: Section 3, decision procedure steps 1-3; Section 2 identity and registry
    rules
  accessed_at: '2026-11-01T00:45:49Z'
  support: supports
  summary: Use the exact ontology term before the CAS fallback; distinct hydration
    states must retain their own identity.
  snapshot_sha256: 94aad13ea0fc3df82a37383f388f41432b607b04cac61ae5792ce1a381aef805
- evidence_id: ncit
  kind: database
  reference: https://api-evsrest.nci.nih.gov/api/v1/concept/ncit/C61946?include=full
  locator: 'reports/sssom_scientific_curation_20261101/audit875/sources/ncit-C61946.json:
    name, active, version and properties'
  accessed_at: '2026-11-01T00:45:49Z'
  support: supports
  summary: NCIT:C61946 is active in 26.10d, names Sodium Phosphate, Dibasic, Heptahydrate
    and records CAS 7782-85-6, formula 2Na.HO4P.7H2O and FDA UNII 70WT22SF4B.
  snapshot_sha256: a112c3e91dd6aa46feb112621ba5d13673df69f1b20665e042e22b8aa05a1d83
- evidence_id: fda
  kind: database
  reference: https://precision.fda.gov/uniisearch/srs/unii/70WT22SF4B
  locator: reports/sssom_scientific_curation_20261101/audit875/sources/fda-unii.html
  accessed_at: '2026-11-01T00:45:49Z'
  support: supports
  summary: FDA identifies the dibasic heptahydrate, its CAS and seven-water formula,
    and links NCIT:C61946.
  snapshot_sha256: ef1403c101974019957c9747d7b386d245693fa7c3be9c7e9bbf39878b0d504a
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/6096963/property/MolecularFormula,MolecularWeight,InChI,InChIKey,CanonicalSMILES/JSON
  locator: reports/sssom_scientific_curation_20261101/audit875/sources/pubchem-properties.json;
    CAS resolution in pubchem-cas-resolve.json
  accessed_at: '2026-11-01T00:45:49Z'
  support: supports
  summary: CAS resolution returns CID6096963; formula H15Na2O11P, mass 268.07 and
    structure include seven waters. FDA-linked CID517013 gives the same formula and
    InChIKey.
  snapshot_sha256: 09d1ffc91f4fa882bf8a0ea562906640e98e1131609bf46106a7d67dcd88d320
- evidence_id: chebi-parent
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:34683
  locator: 'reports/sssom_scientific_curation_20261101/audit875/sources/chebi-parent.json:
    chemical_data and structure'
  accessed_at: '2026-11-01T00:45:49Z'
  support: supports
  summary: CHEBI:34683 is the anhydrous salt. Its InChI and SMILES match the currently
    inherited record values, which do not represent the whole heptahydrate.
  snapshot_sha256: a6714f1020f587eff8a2152ff43ba19c0919ad541b08b5463f008a9e321d6fdc
- evidence_id: bounded-search
  kind: search
  reference: reports/sssom_scientific_curation_20261101/audit875/sources/exact-terms-fetch-manifest.json
  locator: OLS ChEBI response snapshots; primary-fetch-manifest.json for earlier CAS/exact-name
    queries
  accessed_at: '2026-11-01T00:45:49Z'
  support: partial
  summary: No exact ChEBI heptahydrate was found in the retained query results; a
    specific exact NCIT term was positively found. CAS Common Chemistry page/API returned
    403/401 and were not used as chemical evidence.
  snapshot_sha256: 4864e94fcc431ac127208eab64852728a13f3663293352ce760aab0b10ecb872
  search_scope: 'Live OLS ChEBI queries: CAS 7782-85-6, disodium hydrogenphosphate
    heptahydrate, sodium phosphate heptahydrate (0 each), heptahydrate (all 118 returned),
    hydrogenphosphate (all 12), sodium phosphate (all 44). Snapshots preserve entire
    returned pages; no universal ChEBI-absence claim. CAS Common Chemistry access
    failed, without bypass or paid access.'
- evidence_id: occurrences-duplicates
  kind: search
  reference: reports/sssom_scientific_curation_20261101/audit875/record-and-occurrence-audit.json
  locator: duplicate_hits, current_culturemech and aggregate comparison; current-culturemech-occurrences.tsv;
    original full-input hashes in input-manifest.json
  accessed_at: '2026-11-01T00:45:49Z'
  support: partial
  summary: The target alone currently owns CAS 7782-85-6; the 0.02 M stock is a distinct
    preparation. Thirty-five explicit heptahydrate occurrences in 35 recipes include
    32 local IDs, two unresolved IDs and one stale anhydrous ID. The cached YAML count
    is 26; the audit changed no count.
  snapshot_sha256: b00de89b2cf70e3dec4881d7c3ff635b2a5f6bc1ac3a434ef0b7e13b357fa99f
  search_scope: All maintained data/ingredients/**/*.yaml via pathlib.rglob including
    ignored files, supplemented by rg --no-ignore --hidden CAS/NCIT/name search. CultureMech
    occurrence TSV scanned read-only at a74dd489720c9df96cc073ffd11568d407d3c06c;
    exact source hashes and 35 selected rows retained. Concentration-qualified stock
    and REJECTED_LABEL/history matches distinguished.
- evidence_id: prior-decisions
  kind: prior_review
  reference: reports/sssom_scientific_curation_20261101/audit875/audit875.json
  locator: prior_decisions; sources/issue-863.json, issue-334.json, issue-459.json
    contain full inspected bodies/comments
  accessed_at: '2026-11-01T00:45:49Z'
  support: context_only
  summary: '#863 withdrew the stale anhydrous kg_microbe_node_id and deferred primary
    promotion and structure correction; #334 documented CAS scrambling; #459 distinguished
    ontology coverage absence from chemical impossibility and warned against formula-only
    identity inference.'
  snapshot_sha256: 45478929846569b08ca13f66aa3d0e1f440329952d973c88b47d225a8f02ac5b
- evidence_id: pr914
  kind: record_content
  reference: https://github.com/CultureBotAI/MediaIngredientMech/pull/914
  locator: reports/sssom_scientific_curation_20261101/audit875/sources/pr-914.diff
    at 8dc2f266ebf72959a5d2f601d1c767c9138db44f
  accessed_at: '2026-11-01T00:45:49Z'
  support: supports
  summary: The target record and its aggregate hunk are unmodified; its rejection-ledger
    row is unchanged diff context. The same unified Na2HPO4 x 7 H2O row changes 19
    to 28 occurrences while retaining the local identifier. An identity promotion
    would affect that row and aliases and require the explicitly protected unified
    rebuild.
  snapshot_sha256: d4b9a2348e26b0e93ae6fd03f8d3ac38dece1f0c08aed6d2bacb8d1e3df08ec3
- evidence_id: ledger
  kind: record_content
  reference: mappings/unified_mapping_rejections.tsv
  locator: ingredient_name=Na2HPO4 x 7 H2O; rejected_id=CHEBI:34683
  accessed_at: '2026-11-01T00:45:49Z'
  support: supports
  summary: The existing rejection is keyed to the local MIM identity. Any promotion
    must change mim_id and outdated rationale atomically; retain rejection of anhydrous
    CHEBI:34683 as a unified exact identity.
  snapshot_sha256: 44b1dca360302189ea218d9faacdf0fef21c18bfe4e3e71c57abe3b3d0a75194
- evidence_id: legacy
  kind: prior_review
  reference: reviews/structured/20261017T083000Z-na2hpo4-x-7-h2o/review.yaml
  locator: assessment a-efe7ca97594ee880; finding rec-f-e076a032ff4695c0; legacy SEM:cb9ec35166086d936f70
    and SEM:e9b3da7873e18001bfdc
  accessed_at: '2026-11-01T00:45:49Z'
  support: context_only
  summary: The historical identity/structure/BUFFER concern remains broader than this
    audit. The existing role finding remains open; this focused identity evidence
    neither supersedes it nor closes the bundled SEM finding.
  snapshot_sha256: 414cf888064b1bbca184187cf4053288c063aeebada2cab885d4742a723c891c
- evidence_id: validation
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/audit875/logs/audit875_strict.json
  locator: audit875_strict and audit875_terms JSON/log pairs
  accessed_at: '2026-11-01T00:45:49Z'
  support: context_only
  summary: Both focused native validators exited zero on this unchanged record. Structural
    and term-label validity do not establish exact hydrate identity.
  snapshot_sha256: beb001c68b5f9dd6898dca634fbc15f3b5f0571f8f5627697f6d804cef2d3f7b
assessments:
- assessment_id: exact-identity
  area: identity
  topic: Section 3 step 1 exact whole-form ontology identity
  outcome: supported
  summary: NCIT:C61946 is the evidence-backed exact heptahydrate identity; CAS7782-85-6
    is corroborated chemistry metadata, not the preferred primary when this exact
    ontology term exists.
  target_ids:
  - record-e3a107cd8e4ae3b7
  evidence_ids:
  - ncit
  - fda
  - pubchem
  - semantics
  dimensions:
  - name: supplied-form
    value: Disodium hydrogenphosphate heptahydrate, seven waters
    definition: Whole substance denoted by the record; excludes anhydrous salt and
      concentration-qualified stock.
    evidence_ids:
    - ncit
    - pubchem
  - name: evidence-tier
    value: Official ontology and registry database assertions
    definition: Direct exact-form database records; not experimental mechanistic literature
      or an LLM inference from name alone.
    evidence_ids:
    - ncit
    - fda
    - pubchem
- assessment_id: chemical-structure
  area: consistency
  topic: Inherited anhydrous structures under heptahydrate formula
  outcome: concern
  summary: Current InChI/SMILES reproduce CHEBI34683 without seven waters. PubChem
    supplies the matching whole-form structures; correction remains separate from
    the identity decision and has not been applied.
  target_ids:
  - record-e3a107cd8e4ae3b7
  evidence_ids:
  - target
  - chebi-parent
  - pubchem
- assessment_id: ownership
  area: ownership
  topic: Atomic identity and rejection-ledger update versus PR914 unified rebuild
  outcome: concern
  summary: The target YAML and ledger row are not changed by PR914; shared aggregate
    paths alone are not overlap. The precise unified heptahydrate row and alias regeneration
    do overlap the protected rebuild. Preserve existing data until coordinated ownership
    is available.
  target_ids:
  - record-e3a107cd8e4ae3b7
  evidence_ids:
  - pr914
  - ledger
  - prior-decisions
- assessment_id: boundaries
  area: scope
  topic: Pure compound, stock preparation and sibling hydrate boundaries
  outcome: supported
  summary: No second maintained record currently owns this exact CAS/NCIT identity
    in the ignored-inclusive scan. The 0.02 M stock and other hydrates retain distinct
    identities. Current occurrence differences are diagnostic and were not imported.
  target_ids:
  - record-e3a107cd8e4ae3b7
  evidence_ids:
  - occurrences-duplicates
  - target
- assessment_id: residual-scope
  area: evidence
  topic: Unreassessed role and historical bundled finding
  outcome: unknown
  summary: BUFFER evidence is still provisional on the inspected YAML. Its scientific
    validity was not reassessed; neither SEM:cb9ec35166086d936f70 nor SEM:e9b3da7873e18001bfdc
    is retired by this narrower observation.
  target_ids:
  - record-e3a107cd8e4ae3b7
  evidence_ids:
  - legacy
  - target
findings:
- finding_id: exact-form-identity
  issue_key: mim-gh875-exact-heptahydrate-identity
  category: identity
  severity: major
  status: deferred
  certainty: confirmed
  title: Use the exact NCIT heptahydrate identity after unified rebuild coordination
  description: The exact active NCIT term supersedes the CAS-only option in issue875.
    Promotion must pair the maintained identity/grounding change with the rejection-ledger
    key/rationale, guarded history and content-bound SSSOM receipt. PR914 owns the
    intersecting unified row/rebuild.
  target_ids:
  - record-e3a107cd8e4ae3b7
  field_paths:
  - identifier
  - ontology_mapping
  - mappings/unified_mapping_rejections.tsv mim_id
  evidence_ids:
  - ncit
  - semantics
  - ledger
  - pr914
  rule_id: MAPPING_SEMANTICS Section 3 decision step 1
  native_severity: P2
  normalization_reason: Major curation defect in the primary identifier decision;
    current local identity still preserves hydration rather than falsely exact-matching
    the anhydrous parent.
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml
    role: maintained ingredient; guarded writes only
  disposition_reason: Scientific identity option is established; application deferred
    solely to the user-protected PR914 unified rebuild ownership, not to lack of exact-form
    evidence.
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/875
  - https://github.com/CultureBotAI/MediaIngredientMech/pull/914
- finding_id: anhydrous-structure
  issue_key: mim-heptahydrate-inherited-anhydrous-structure
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Heptahydrate record still carries anhydrous InChI and SMILES
  description: The record formula includes seven waters, but its stored structures
    equal the anhydrous ChEBI parent. Exact PubChem heptahydrate structures are available.
    This confirms the structure subclaim without closing the broader legacy finding
    or its role scope.
  target_ids:
  - record-e3a107cd8e4ae3b7
  field_paths:
  - chemical_properties.inchi
  - chemical_properties.smiles
  evidence_ids:
  - target
  - chebi-parent
  - pubchem
  - legacy
  rule_id: MAPPING_SEMANTICS Section 3 whole-substance identity
  native_severity: P2
  normalization_reason: Major because the molecular structure encodes a different
    hydration form from the represented ingredient.
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml
    role: maintained ingredient; guarded writes only
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/871
actions:
- action_id: coordinate-unified
  description: Coordinate the exact identity and unified rebuild ownership with PR914
    before application; alternatively retain this evidence-only result until that
    work lands.
  finding_ids:
  - exact-form-identity
  target_ids:
  - record-e3a107cd8e4ae3b7
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml
    role: maintained ingredient; guarded writes only
  acceptance_checks:
  - Demonstrate a disjoint or agreed same-row update for the unified heptahydrate
    rows and provenance.
  - Do not infer a conflict merely from sharing mapped_ingredients.yaml or the rejection-ledger
    path.
- action_id: apply-exact-identity
  description: Use the guarded writer to promote primary and exact ontology mapping
    to NCIT:C61946, append honest LLM-assisted history, preserve form-specific synonyms,
    update ledger mim_id/rationale atomically, synchronize aggregate/exports, and
    use the native SSSOM receipt chain.
  finding_ids:
  - exact-form-identity
  target_ids:
  - record-e3a107cd8e4ae3b7
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml
    role: maintained ingredient; guarded writes only
  depends_on:
  - coordinate-unified
  generator: MIM guarded write_validated_ingredient; supported Claw SSSOM and coordinated
    unified builders
  acceptance_checks:
  - Keep CHEBI:34683 rejected as unified identity; whole NCIT identity is exact and
    any separately retained parent relation has its own supported scope.
  - Run validate-all, qc-sssom, qc-roundtrip, qc-flat-coverage, qc-evidence, audit-writers
    and applicable native mapping receipt/review checks.
  - Do not carry scientific approval onto changed/new rows without a new content-bound
    review.
- action_id: correct-structure
  description: Separately review and apply the exact seven-water PubChem structures
    through the guarded writer with claim-level source provenance, retaining unrelated
    fields and history.
  finding_ids:
  - anhydrous-structure
  target_ids:
  - record-e3a107cd8e4ae3b7
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml
    role: maintained ingredient; guarded writes only
  acceptance_checks:
  - Verify the target CAS, hydration state, formula, InChI and SMILES all denote the
    same seven-water form.
  - Synchronize maintained surfaces and pass native validation/export gates.
  - Keep BUFFER and broader bundled SEM finding open unless each remaining claim is
    independently addressed.
limitations:
- 'Partial scientific scope: exact-form identity and structure only; BUFFER role support
  and all broader scientific claims were not re-reviewed.'
- CAS Common Chemistry page/API were unavailable (403/401); exact NCIT/FDA/PubChem
  evidence was inspected directly instead.
- ChEBI absence is bounded to the recorded searches and returned results.
- The PR914 conflict is tied to inspected head 8dc2f266ebf72959a5d2f601d1c767c9138db44f;
  recheck live state before application.
- No curated YAML, aggregates, SSSOM, rejection ledger, scientific dispositions or
  source occurrence counts were changed by this review.
- This review neither supersedes the previous role review nor closes SEM:cb9ec35166086d936f70;
  no release approval follows from a validated review bundle.
related_reviews:
- repository: CultureBotAI/MediaIngredientMech
  review_id: 20261017T083000Z-na2hpo4-x-7-h2o
  relationship: Focused new primary identity/structure evidence; does not supersede
    its unreassessed role finding or broader legacy scope.
links:
- https://github.com/CultureBotAI/MediaIngredientMech/issues/875#issuecomment-6551319986
- https://github.com/CultureBotAI/MediaIngredientMech/pull/914
tags:
- heptahydrate
- identity
- ncit
- partial-scientific-review
- deferred-application
```
