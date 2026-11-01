# Melezitose monohydrate: verified form identity, blocked parent correction, retained role finding

- Review: 20261101T005659Z-melezitose-formof-blocked-review
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-11-01T00:56:59.079767Z
- Finished UTC: 2026-11-01T00:56:59.079767Z
- Reviewer: Codex scientific curation agent (self_review)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

Primary database structures support the distinct CAS monohydrate and an asymmetric form-of parent under current policy. The guarded proposal could not pass the native frozen mapping approval pin; original source and canonical rows were restored exactly. No melezitose correction or new release approval ships. The existing prediction-only carbon-role concern remains open.

## Scope And Provenance

One exact monohydrate record, its form/parent evidence, existing role claim, attempted native publication and preserved original source.

Selection: Exact file data/ingredients/mapped/D-_-melezitose_Monohydrate.yaml, cas:10030-67-8; excludes generic hydrate CAS207511-10-2 and anhydrous melezitose.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 4625afd492b6cf43e3b499d1425d2453d490009d.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-05159118f032f1be | data/ingredients/mapped/D-_-melezitose_Monohydrate.yaml | maintained | D-(+)-melezitose monohydrate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native closed-schema validation and exact maintained-surface comparison | passed | True | record-05159118f032f1be | validate_ingredient returned zero errors; aggregate entry equals restored record; original SSSOM rows remain at918/919, with original CAS approval preserved on unchanged bytes. |
| Inspected PubChem and official ChEBI structural identity evidence | passed | True | record-05159118f032f1be | Hydrate formula/InChI/CAS agree; PubChem parent stereochemical InChI equals active CHEBI6731. CHEBI183824 is anhydrous and stereochemically different. |
| Bounded exact-form ontology search | passed | True | record-05159118f032f1be | No exact monohydrate candidate found in current OLS all-ontology name/CAS, NCIT CAS, ChEBI name/CAS or pinned local ChEBI searches. Broad NCIT results were organisms mentioning utilization. |
| Native completion assembler for the unpublished corrected source | failed | True | record-05159118f032f1be | The native assembler rejected the old positive CAS cohort owner/row pin after an approval-free change receipt. This is evidence for deferral, not a failure of the restored current source. |

## Scientific And Domain Assessments

### Distinct hydrate, CAS and stereochemical structure

identity: supported. Targets: record-05159118f032f1be.

CAS10030-67-8 and the monohydrate structure are consistent with inspected primary database records; retain this form separately.

### Asymmetric form-of mapping and native approval dependency

grounding: concern. Targets: record-05159118f032f1be.

Current CLOSE_MATCH is inconsistent with the settled parent-mapping convention. Evidence supports a bounded correction, but native publication is blocked by frozen prior approval and requires PR764.

### Existing provisional carbon role

evidence: concern. Targets: record-05159118f032f1be.

The unchanged role has only computational/name-pattern evidence. This is an evidence gap, not proof that the biological role is false.

### Preserved current native source and dispositions

consistency: supported. Targets: record-05159118f032f1be.

Original record and two canonical rows are restored; source surfaces agree and the prior CAS decision remains bound to unchanged bytes. Proposal and failure are archived separately.

## Findings

### parent-correction-blocked: Evidence-settled form-of parent correction requires native approval supersession

major / deferred / confirmed; issue key: mim-hydrate-parent-formof-d-melezitose-monohydrate.

Retain exact CAS monohydrate identity. The current CLOSE_MATCH should become NARROW_MATCH/skos:broadMatch with B1 only after PR764 supplies the native supersession path and exact current inputs are re-reviewed. The attempted proposal is unpublished; no invariant was waived.

Disposition: Deferred to the explicit native review-pin supersession mechanism; original source was restored.

### carbon-role-open: Prediction-only carbon-role support remains unresolved

major / open / confirmed; issue key: mim-reconciliation-role-support-05159118f032f1be.

nutritional_roles[0] remains CARBON_SOURCE with only COMPUTATIONAL_PREDICTION from a name-pattern rule. Chemical identity evidence does not establish this biological role.

## Recommended Actions And Acceptance Checks

### future-native-correction

After PR764 or a reviewed native successor lands, reassess exact term availability and apply the scoped parent/B1 correction through guarded writers with fresh mapping-specific review.

- No overlap with active record/decision scopes; preserve exact CAS identity and all unresolved role findings.
- Native completion/semantic/reviewed-release checks pass without carrying stale approval or altering frozen holds.
- Canonical parent is broadMatch, B1 identity exists, and hydrate CAS is absent from parent other.

### source-role-evidence

Inspect an original utilization experiment or preparation source for this precise form and organism/conditions before approving or replacing the provisional carbon role.

- Evidence directly supports exact role scope; name or chemical class alone is insufficient.
- Preserve prior findings and save a content-bound successor; no automatic role approval from identity review.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/ingredients/mapped/D-_-melezitose_Monohydrate.yaml | partial | Restored original CAS10030-67-8 monohydrate, CLOSE_MATCH parent6731, no synonyms, one explicitly provisional computational carbon role. |
| hydrate | reports/sssom_scientific_curation_20261101/audit901/sources/pubchem-16217716-properties.json; PropertyTable.Properties[0]; https://pubchem.ncbi.nlm.nih.gov/compound/16217716 | supports | Official PubChem CID16217716 returns C18H34O17 and the exact monohydrate stereochemical InChI in the record. |
| hydrate-cas | reports/sssom_scientific_curation_20261101/audit901/sources/pubchem-16217716-synonyms.json | supports | Official PubChem CID16217716 lists CAS10030-67-8; this is a database cross-reference, not direct CAS Registry access. |
| parent | reports/sssom_scientific_curation_20261101/audit901/sources/ols-CHEBI-6731.json; annotation.inchi_string and generalized_empirical_formula | supports | Active CHEBI6731 is melezitose C18H32O16. Its stereochemical InChI agrees with PubChem parent CID92817; it is anhydrous, so cannot be exact identity for the hydrate. |
| alternative | reports/sssom_scientific_curation_20261101/audit901/sources/ols-CHEBI-183824.json | supports | D(+)-Melezitose183824 has anhydrous formula and different stereochemistry; label similarity does not provide an exact hydrate identity. |
| search | reports/sssom_scientific_curation_20261101/audit901/sources/all-ontology-fetch-receipts.json | supports | Live all-ontology exact monohydrate-name/CAS and NCIT CAS queries found zero; broad NCIT melezitose returned11 organism descriptions, no compound term. |
| local-search | reports/sssom_scientific_curation_20261101/audit901/sources/local-chebi-search-v2.json | supports | Pinned local database name/synonym and CAS searches found no exact hydrate. Corrected actual oio: prefix and positive parent-CAS controls were used. |
| policy | MAPPING_SEMANTICS.md; Section3 and settled form-of ruling | supports | Section3 plus settled form-of ruling require distinct form identity and asymmetric broader parent when no exact term exists. Historical #342 closeMatch rationale does not override current policy. |
| gate | reports/sssom_scientific_curation_20261101/audit901/assembler-blocker.json | refutes | Attempted changed CAS row919/frozen cohort931 triggers Nonmapping-cohort approval has stale owner or row. Old approval was not edited. |
| withdrawal | reports/sssom_scientific_curation_20261101/audit901/melezitose-withdrawal.json | supports | Guarded restoration returns original e17d80e75cf8794f5f4e2cab65a4cff77c92f921add55e36185549f75aff3222 bytes; original rows918/919 restored, proposed B1 removed, other rows/positions preserved. |
| current-checks | reports/sssom_scientific_curation_20261101/audit901/melezitose-current-checks.json | supports | Fresh final-source checks bind exact record bytes, aggregate equality, original rows and current decisions; no new scientific approval. |
| prior-role | reviews/structured/20261017T083000Z-d-melezitose-monohydrate/review.yaml | context_only | Prior role finding rec-f-14aa31dd7ebeaa0c remains confirmed: CARBON_SOURCE is supported only by a name-pattern computational prediction. |
| dependency | reports/sssom_scientific_curation_20261101/audit901/policy/pr-764.json | context_only | Open native PR764 supplies approval-free supersession of old record/row pins; no duplicated guard change was made. |

## Limits And Additional Notes

- Direct CAS Common Chemistry pages were inaccessible; CAS cross-reference verification uses PubChem and is not represented as direct CAS Registry confirmation.
- The ontology search is bounded to inspected current OLS responses and a pinned local ChEBI build; future terms or unsearched releases may change the decision.
- No biological literature research or paid provider calls were performed; the carbon role remains open.
- This self-review does not provide independent final-head review, human curator approval, or native release approval.
- The blocked proposal is archived evidence only and must not be executed before the native supersession prerequisite and fresh review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261101T005659Z-melezitose-formof-blocked-review
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Melezitose monohydrate: verified form identity, blocked parent correction,
  retained role finding'
started_at: '2026-11-01T00:56:59.079767Z'
finished_at: '2026-11-01T00:56:59.079767Z'
reviewer:
  identity: Codex scientific curation agent
  kind: agent
  model: gpt-6
  independence: self_review
  independence_basis: This agent researched and authored the unpublished proposal,
    reproduced the native approval-pin failure and restored the original source. This
    is not the independent final-head adversarial review.
skill: curate-yaml-record
completion: partial
verdict: blocked
native_verdict: Distinct CAS monohydrate identity supported; current CLOSE_MATCH correction
  deferred to PR764; provisional carbon role remains unapproved.
scientific_review: true
summary: Primary database structures support the distinct CAS monohydrate and an asymmetric
  form-of parent under current policy. The guarded proposal could not pass the native
  frozen mapping approval pin; original source and canonical rows were restored exactly.
  No melezitose correction or new release approval ships. The existing prediction-only
  carbon-role concern remains open.
source:
  git_revision: 4625afd492b6cf43e3b499d1425d2453d490009d
  state: working_tree
  inputs:
  - path: AGENTS.md
    sha256: fc7728986d82b43359a9055ae233bcf0d4ebaef8bb657ef1b4bb4aa87b2cbaaf
    role: context
  - path: MAPPING_SEMANTICS.md
    sha256: 94aad13ea0fc3df82a37383f388f41432b607b04cac61ae5792ce1a381aef805
    role: context
  - path: data/curated/mapped_ingredients.yaml
    sha256: 56e9eae4e0dd282e9c5a5d6d8c972faa99ddda76127bb26a9df5f5934abce09d
    role: context
  - path: data/ingredients/mapped/D-_-melezitose_Monohydrate.yaml
    sha256: e17d80e75cf8794f5f4e2cab65a4cff77c92f921add55e36185549f75aff3222
    role: target
  - path: mappings/ingredient_mappings.sssom.tsv
    sha256: f408f36b9de77c2089a07907b40d6a27401087e13528f0597a6cf7b386048ac0
    role: context
  - path: reports/semantic_review_20260921/resolution/assertion-dispositions.tsv
    sha256: 0665c35b88d204247c6b7c702fbbd8e6bba8c15b3e17f155385291b7d606b2de
    role: context
  - path: reports/sssom_completion_20260921/review.json
    sha256: 0cc2c8742f905458ebb15ed0195aa0744662f29d6019bad03690f8095904ac40
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit901/assembler-blocker.json
    sha256: 842d9ba5a16b9f98aa280fb30dce3fa5373df862ff747327244bac7211a2f557
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit901/melezitose-current-checks.json
    sha256: 96216b07b2a3c5b4681777fe3de88b098c25688be6c6fc23f6c34a8d03be671a
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit901/melezitose-withdrawal.json
    sha256: b1f93ace38ecc9898274d6774181ded8073f77a26b0a280239504f04b580b620
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit901/policy/pr-764.json
    sha256: 66147346b1bc8ce9171f6f7a2abcf6c1e3f765964b2665eedcd4936f55314392
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit901/sources/all-ontology-fetch-receipts.json
    sha256: a891d5a60d233f2e61f7b9d8ac07a590e964d8fab0317e2adf9dadf7ffdc5fb9
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit901/sources/local-chebi-search-v2.json
    sha256: c09931f27566c3f5ad86ef76f1a2a9f6b604a05b75b3087569f7d5d8eb29b56b
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit901/sources/ols-CHEBI-183824.json
    sha256: 1ef89ffe8b5a794cee9cac9b49573b053b97545fdaff38499fc0994894e3aecc
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit901/sources/ols-CHEBI-6731.json
    sha256: 3257f58844e34b076e55b73ae22b860db2fb1b4fd090cac6c872459c6f0a76ef
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit901/sources/pubchem-16217716-properties.json
    sha256: da1b8c8508819634eebe191a2474e728822040d27731b58640fd089bdf3453ed
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit901/sources/pubchem-16217716-synonyms.json
    sha256: ae84e9495419f1e2bee4373c3902a187f875a4783eb9e65ef792dbb3b6e96c41
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit901/sources/pubchem-92817-properties.json
    sha256: 3a1823edbf8879202cc8a89767402e368111c5851174bbbbc3355e62e7837c76
    role: context
  - path: reviews/structured/20261017T083000Z-d-melezitose-monohydrate/review.yaml
    sha256: e8d10ab2bb995a74632248d64ff0eb44b0ccc203624739031839dda9cc327c16
    role: context
  - path: src/mediaingredientmech/schema/mediaingredientmech.yaml
    sha256: bb43dee29b21fdee72a48022456e733e49e95824c4c09674f9b3165c290fe012
    role: context
targets:
- target_id: record-05159118f032f1be
  path: data/ingredients/mapped/D-_-melezitose_Monohydrate.yaml
  label: D-(+)-melezitose monohydrate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-_-melezitose_Monohydrate.yaml
    role: maintained ingredient
scope:
  description: One exact monohydrate record, its form/parent evidence, existing role
    claim, attempted native publication and preserved original source.
  selection: Exact file data/ingredients/mapped/D-_-melezitose_Monohydrate.yaml, cas:10030-67-8;
    excludes generic hydrate CAS207511-10-2 and anhydrous melezitose.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-05159118f032f1be
  exclusions:
  - target: 'All other #901 hydrate records and active PR912/914 scientific cohorts'
    reason: Separate owners and scientific decisions; no blanket cohort migration.
checks:
- check_id: current-source-shape
  name: Native closed-schema validation and exact maintained-surface comparison
  status: passed
  required: true
  summary: validate_ingredient returned zero errors; aggregate entry equals restored
    record; original SSSOM rows remain at918/919, with original CAS approval preserved
    on unchanged bytes.
  command: 'PYTHONPATH=src python - <<PY: validate_ingredient(record); compare aggregate,
    original subject rows, primary structures and current decisions'
  exit_code: 0
  target_ids:
  - record-05159118f032f1be
  evidence_ids:
  - current-checks
- check_id: primary-identity
  name: Inspected PubChem and official ChEBI structural identity evidence
  status: passed
  required: true
  summary: Hydrate formula/InChI/CAS agree; PubChem parent stereochemical InChI equals
    active CHEBI6731. CHEBI183824 is anhydrous and stereochemically different.
  target_ids:
  - record-05159118f032f1be
  evidence_ids:
  - hydrate
  - hydrate-cas
  - parent
  - alternative
  - current-checks
- check_id: exact-term-search
  name: Bounded exact-form ontology search
  status: passed
  required: true
  summary: No exact monohydrate candidate found in current OLS all-ontology name/CAS,
    NCIT CAS, ChEBI name/CAS or pinned local ChEBI searches. Broad NCIT results were
    organisms mentioning utilization.
  target_ids:
  - record-05159118f032f1be
  evidence_ids:
  - search
  - local-search
- check_id: proposal-release-gate
  name: Native completion assembler for the unpublished corrected source
  status: failed
  required: true
  summary: The native assembler rejected the old positive CAS cohort owner/row pin
    after an approval-free change receipt. This is evidence for deferral, not a failure
    of the restored current source.
  command: PYTHONPATH=src python reports/sssom_completion_20260921/assemble_review.py
  exit_code: 1
  target_ids:
  - record-05159118f032f1be
  evidence_ids:
  - gate
  - withdrawal
evidence:
- evidence_id: record
  kind: record_content
  reference: data/ingredients/mapped/D-_-melezitose_Monohydrate.yaml
  accessed_at: '2026-11-01T00:56:59.079767Z'
  support: partial
  summary: Restored original CAS10030-67-8 monohydrate, CLOSE_MATCH parent6731, no
    synonyms, one explicitly provisional computational carbon role.
  snapshot_sha256: e17d80e75cf8794f5f4e2cab65a4cff77c92f921add55e36185549f75aff3222
- evidence_id: hydrate
  kind: database
  reference: reports/sssom_scientific_curation_20261101/audit901/sources/pubchem-16217716-properties.json
  accessed_at: '2026-11-01T00:56:59.079767Z'
  support: supports
  summary: Official PubChem CID16217716 returns C18H34O17 and the exact monohydrate
    stereochemical InChI in the record.
  locator: PropertyTable.Properties[0]; https://pubchem.ncbi.nlm.nih.gov/compound/16217716
  snapshot_sha256: da1b8c8508819634eebe191a2474e728822040d27731b58640fd089bdf3453ed
- evidence_id: hydrate-cas
  kind: database
  reference: reports/sssom_scientific_curation_20261101/audit901/sources/pubchem-16217716-synonyms.json
  accessed_at: '2026-11-01T00:56:59.079767Z'
  support: supports
  summary: Official PubChem CID16217716 lists CAS10030-67-8; this is a database cross-reference,
    not direct CAS Registry access.
  snapshot_sha256: ae84e9495419f1e2bee4373c3902a187f875a4783eb9e65ef792dbb3b6e96c41
- evidence_id: parent
  kind: database
  reference: reports/sssom_scientific_curation_20261101/audit901/sources/ols-CHEBI-6731.json
  accessed_at: '2026-11-01T00:56:59.079767Z'
  support: supports
  summary: Active CHEBI6731 is melezitose C18H32O16. Its stereochemical InChI agrees
    with PubChem parent CID92817; it is anhydrous, so cannot be exact identity for
    the hydrate.
  locator: annotation.inchi_string and generalized_empirical_formula
  snapshot_sha256: 3257f58844e34b076e55b73ae22b860db2fb1b4fd090cac6c872459c6f0a76ef
- evidence_id: alternative
  kind: database
  reference: reports/sssom_scientific_curation_20261101/audit901/sources/ols-CHEBI-183824.json
  accessed_at: '2026-11-01T00:56:59.079767Z'
  support: supports
  summary: D(+)-Melezitose183824 has anhydrous formula and different stereochemistry;
    label similarity does not provide an exact hydrate identity.
  snapshot_sha256: 1ef89ffe8b5a794cee9cac9b49573b053b97545fdaff38499fc0994894e3aecc
- evidence_id: search
  kind: search
  reference: reports/sssom_scientific_curation_20261101/audit901/sources/all-ontology-fetch-receipts.json
  accessed_at: '2026-11-01T00:56:59.079767Z'
  support: supports
  summary: Live all-ontology exact monohydrate-name/CAS and NCIT CAS queries found
    zero; broad NCIT melezitose returned11 organism descriptions, no compound term.
  search_scope: 'OLS API all ontologies: melezitose monohydrate,10030-67-8; NCIT:melezitose,10030-67-8,
    rows100. Scope bounded to retrieved API responses; no claim of universal ontology
    absence.'
  snapshot_sha256: a891d5a60d233f2e61f7b9d8ac07a590e964d8fab0317e2adf9dadf7ffdc5fb9
- evidence_id: local-search
  kind: search
  reference: reports/sssom_scientific_curation_20261101/audit901/sources/local-chebi-search-v2.json
  accessed_at: '2026-11-01T00:56:59.079767Z'
  support: supports
  summary: 'Pinned local database name/synonym and CAS searches found no exact hydrate.
    Corrected actual oio: prefix and positive parent-CAS controls were used.'
  search_scope: All rows in read-only pinned ChEBI database, including ignored local
    cache; exact SQL and database SHA256 saved. Earlier wrong-prefix exploratory query
    is not absence evidence.
  snapshot_sha256: c09931f27566c3f5ad86ef76f1a2a9f6b604a05b75b3087569f7d5d8eb29b56b
- evidence_id: policy
  kind: authority
  reference: MAPPING_SEMANTICS.md
  accessed_at: '2026-11-01T00:56:59.079767Z'
  support: supports
  summary: 'Section3 plus settled form-of ruling require distinct form identity and
    asymmetric broader parent when no exact term exists. Historical #342 closeMatch
    rationale does not override current policy.'
  locator: Section3 and settled form-of ruling
  snapshot_sha256: 94aad13ea0fc3df82a37383f388f41432b607b04cac61ae5792ce1a381aef805
- evidence_id: gate
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/audit901/assembler-blocker.json
  accessed_at: '2026-11-01T00:56:59.079767Z'
  support: refutes
  summary: Attempted changed CAS row919/frozen cohort931 triggers Nonmapping-cohort
    approval has stale owner or row. Old approval was not edited.
  snapshot_sha256: 842d9ba5a16b9f98aa280fb30dce3fa5373df862ff747327244bac7211a2f557
- evidence_id: withdrawal
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/audit901/melezitose-withdrawal.json
  accessed_at: '2026-11-01T00:56:59.079767Z'
  support: supports
  summary: Guarded restoration returns original e17d80e75cf8794f5f4e2cab65a4cff77c92f921add55e36185549f75aff3222
    bytes; original rows918/919 restored, proposed B1 removed, other rows/positions
    preserved.
  snapshot_sha256: b1f93ace38ecc9898274d6774181ded8073f77a26b0a280239504f04b580b620
- evidence_id: current-checks
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/audit901/melezitose-current-checks.json
  accessed_at: '2026-11-01T00:56:59.079767Z'
  support: supports
  summary: Fresh final-source checks bind exact record bytes, aggregate equality,
    original rows and current decisions; no new scientific approval.
  snapshot_sha256: 96216b07b2a3c5b4681777fe3de88b098c25688be6c6fc23f6c34a8d03be671a
- evidence_id: prior-role
  kind: prior_review
  reference: reviews/structured/20261017T083000Z-d-melezitose-monohydrate/review.yaml
  accessed_at: '2026-11-01T00:56:59.079767Z'
  support: context_only
  summary: 'Prior role finding rec-f-14aa31dd7ebeaa0c remains confirmed: CARBON_SOURCE
    is supported only by a name-pattern computational prediction.'
  snapshot_sha256: e8d10ab2bb995a74632248d64ff0eb44b0ccc203624739031839dda9cc327c16
- evidence_id: dependency
  kind: prior_review
  reference: reports/sssom_scientific_curation_20261101/audit901/policy/pr-764.json
  accessed_at: '2026-11-01T00:56:59.079767Z'
  support: context_only
  summary: Open native PR764 supplies approval-free supersession of old record/row
    pins; no duplicated guard change was made.
  snapshot_sha256: 66147346b1bc8ce9171f6f7a2abcf6c1e3f765964b2665eedcd4936f55314392
assessments:
- assessment_id: identity
  area: identity
  topic: Distinct hydrate, CAS and stereochemical structure
  outcome: supported
  summary: CAS10030-67-8 and the monohydrate structure are consistent with inspected
    primary database records; retain this form separately.
  target_ids:
  - record-05159118f032f1be
  evidence_ids:
  - hydrate
  - hydrate-cas
  - parent
  - alternative
  - current-checks
- assessment_id: mapping
  area: grounding
  topic: Asymmetric form-of mapping and native approval dependency
  outcome: concern
  summary: Current CLOSE_MATCH is inconsistent with the settled parent-mapping convention.
    Evidence supports a bounded correction, but native publication is blocked by frozen
    prior approval and requires PR764.
  target_ids:
  - record-05159118f032f1be
  evidence_ids:
  - policy
  - gate
  - dependency
  - withdrawal
- assessment_id: role
  area: evidence
  topic: Existing provisional carbon role
  outcome: concern
  summary: The unchanged role has only computational/name-pattern evidence. This is
    an evidence gap, not proof that the biological role is false.
  target_ids:
  - record-05159118f032f1be
  evidence_ids:
  - record
  - prior-role
- assessment_id: surface
  area: consistency
  topic: Preserved current native source and dispositions
  outcome: supported
  summary: Original record and two canonical rows are restored; source surfaces agree
    and the prior CAS decision remains bound to unchanged bytes. Proposal and failure
    are archived separately.
  target_ids:
  - record-05159118f032f1be
  evidence_ids:
  - withdrawal
  - current-checks
findings:
- finding_id: parent-correction-blocked
  issue_key: mim-hydrate-parent-formof-d-melezitose-monohydrate
  category: grounding
  severity: major
  native_severity: P2
  normalization_reason: The settled directional mapping contract is not represented;
    correction is scientifically bounded but blocked by native approval provenance.
  status: deferred
  certainty: confirmed
  title: Evidence-settled form-of parent correction requires native approval supersession
  description: Retain exact CAS monohydrate identity. The current CLOSE_MATCH should
    become NARROW_MATCH/skos:broadMatch with B1 only after PR764 supplies the native
    supersession path and exact current inputs are re-reviewed. The attempted proposal
    is unpublished; no invariant was waived.
  target_ids:
  - record-05159118f032f1be
  field_paths:
  - ontology_mapping.mapping_quality
  evidence_ids:
  - policy
  - hydrate
  - parent
  - gate
  - withdrawal
  - dependency
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-_-melezitose_Monohydrate.yaml
    role: maintained ingredient
  disposition_reason: Deferred to the explicit native review-pin supersession mechanism;
    original source was restored.
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/901
  - https://github.com/CultureBotAI/MediaIngredientMech/pull/764
- finding_id: carbon-role-open
  issue_key: mim-reconciliation-role-support-05159118f032f1be
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: An asserted biological role lacks organism/condition-specific
    primary support; retained as provisional rather than approved.
  status: open
  certainty: confirmed
  title: Prediction-only carbon-role support remains unresolved
  description: nutritional_roles[0] remains CARBON_SOURCE with only COMPUTATIONAL_PREDICTION
    from a name-pattern rule. Chemical identity evidence does not establish this biological
    role.
  target_ids:
  - record-05159118f032f1be
  field_paths:
  - nutritional_roles[0]
  evidence_ids:
  - record
  - prior-role
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-_-melezitose_Monohydrate.yaml
    role: maintained ingredient
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261017T083000Z-d-melezitose-monohydrate
    finding_id: rec-f-14aa31dd7ebeaa0c
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
actions:
- action_id: future-native-correction
  description: After PR764 or a reviewed native successor lands, reassess exact term
    availability and apply the scoped parent/B1 correction through guarded writers
    with fresh mapping-specific review.
  finding_ids:
  - parent-correction-blocked
  target_ids:
  - record-05159118f032f1be
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-_-melezitose_Monohydrate.yaml
    role: maintained ingredient
  acceptance_checks:
  - No overlap with active record/decision scopes; preserve exact CAS identity and
    all unresolved role findings.
  - Native completion/semantic/reviewed-release checks pass without carrying stale
    approval or altering frozen holds.
  - Canonical parent is broadMatch, B1 identity exists, and hydrate CAS is absent
    from parent other.
- action_id: source-role-evidence
  description: Inspect an original utilization experiment or preparation source for
    this precise form and organism/conditions before approving or replacing the provisional
    carbon role.
  finding_ids:
  - carbon-role-open
  target_ids:
  - record-05159118f032f1be
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-_-melezitose_Monohydrate.yaml
    role: maintained ingredient
  acceptance_checks:
  - Evidence directly supports exact role scope; name or chemical class alone is insufficient.
  - Preserve prior findings and save a content-bound successor; no automatic role
    approval from identity review.
limitations:
- Direct CAS Common Chemistry pages were inaccessible; CAS cross-reference verification
  uses PubChem and is not represented as direct CAS Registry confirmation.
- The ontology search is bounded to inspected current OLS responses and a pinned local
  ChEBI build; future terms or unsearched releases may change the decision.
- No biological literature research or paid provider calls were performed; the carbon
  role remains open.
- This self-review does not provide independent final-head review, human curator approval,
  or native release approval.
- The blocked proposal is archived evidence only and must not be executed before the
  native supersession prerequisite and fresh review.
related_reviews:
- repository: CultureBotAI/MediaIngredientMech
  review_id: 20261017T083000Z-d-melezitose-monohydrate
  relationship: Successor assessment of exact identity and unchanged open carbon-role
    finding; preserves full predecessor target scope.
links:
- https://github.com/CultureBotAI/MediaIngredientMech/issues/901
- https://github.com/CultureBotAI/MediaIngredientMech/pull/764
tags:
- scientific-curation
- melezitose
- blocked-proposal
- no-release-approval
```
