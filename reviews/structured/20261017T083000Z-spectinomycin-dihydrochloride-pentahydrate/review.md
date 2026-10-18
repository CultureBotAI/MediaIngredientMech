# Per-record structured review: Spectinomycin_Dihydrochloride_Pentahydrate (data/ingredients/mapped/Spectinomycin_Dihydrochloride_Pentahydrate.yaml)

- Review: 20261017T083000Z-spectinomycin-dihydrochloride-pentahydrate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Spectinomycin_Dihydrochloride_Pentahydrate (data/ingredients/mapped/Spectinomycin_Dihydrochloride_Pentahydrate.yaml, record-0c32f5978a02bf70, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Spectinomycin_Dihydrochloride_Pentahydrate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Spectinomycin_Dihydrochloride_Pentahydrate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-0c32f5978a02bf70 | data/ingredients/mapped/Spectinomycin_Dihydrochloride_Pentahydrate.yaml | maintained | Spectinomycin_Dihydrochloride_Pentahydrate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-0c32f5978a02bf70 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-0c32f5978a02bf70 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-0c32f5978a02bf70 | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-0c32f5978a02bf70.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-0c32f5978a02bf70.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T16:12:31Z; reviewed SHA-256=1b05f89b24790d65f1318b4499e5aa93ad57d2acc52facdaa1e70cd2cfb012da; current SHA-256=1b05f89b24790d65f1318b4499e5aa93ad57d2acc52facdaa1e70cd2cfb012da; hash_changed=False. Reports=["reports/yaml_record_review/Spectinomycin_Dihydrochloride_Pentahydrate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The salt identity passes, but SELECTIVE_AGENT remains a provisional name-pattern role.

### Historical provisional-role concern

evidence: concern. Targets: record-0c32f5978a02bf70.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-d72f0fd923559b78: Reassess prediction-only role support: Spectinomycin dihydrochloride pentahydrate

major / open / confirmed; issue key: mim-reconciliation-role-support-0c32f5978a02bf70.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-d72f0fd923559b78

Reassess prediction-only role support: Spectinomycin dihydrochloride pentahydrate

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-5b0d011ea23dbea0 | data/ingredients/mapped/Spectinomycin_Dihydrochloride_Pentahydrate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1887],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:9217","line":1889,"mapping_status":"MAPPED","ontology_id":"CHEBI:9217","preferred_term":"Spectinomycin dihydrochloride pentahydrate"}],"identifier":"CHEBI:9217","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:9217","ontology_label":"spectinomycin hydrochloride hydrate","ontology_source":"CHEBI"},"preferred_term":"Spectinomycin dihydrochloride pentahydrate","sssom_rows":[{"data_row":2628,"object_id":"CHEBI:9217","object_label":"spectinomycin hydrochloride hydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Spectinomycin_Dihydrochloride_Pentahydrate","synonym_count":3} |
| ev-13b3b988bf005441 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1887] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-d56db0666e5f9e1e | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Spectinomycin_Dihydrochloride_Pentahydrate; data-row positions=[2628] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2628,"object_id":"CHEBI:9217","object_label":"spectinomycin hydrochloride hydrate","other":"(2R,4aR,5aR,6S,7S,8R,9S,9aR,10aS)-4a,7,9-trihydroxy-2-methyl-6,8-bis(methylamino)decahydro-4H-pyrano[2,3-b][1,4]benzodioxin-4-one dihydrochloride pentahydrate&#124;(2R,4aR,5aR,6S,7S,8R,9S,9aR,10aS)-4a,7,9-trihydroxy-2-methyl-6,8-bis(methylamino)decahydro-4H-pyrano[2,3-b][1,4]benzodioxin-4-one dihydrochloride--water (1/5)&#124;(2R,4aR,5aR,6S,7S,8R,9S,9aR,10aS)-4a,7,9-trihydroxy-N,N',2-trimethyl-4-oxodecahydro-2H-pyrano[2,3-b][1,4]benzodioxine-6,8-diaminium dichloride--water (1/5)&#124;CAS:22189-32-8","predicate_id":"skos:exactMatch","subject_id":"MIM:Spectinomycin_Dihydrochloride_Pentahydrate","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-2d26321a3fc07543 | docs/data/mapped_ingredients.csv; CSV lines=[1889] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:9217","line":1889,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:9217","preferred_term":"Spectinomycin dihydrochloride pentahydrate","total_occurrences":"0"}] |
| ev-925ea0a0b3ee5107 | reports/yaml_record_review/Spectinomycin_Dihydrochloride_Pentahydrate.md; &#96;data/ingredients/mapped/Spectinomycin_Dihydrochloride_Pentahydrate.yaml&#96;:2; Verdict:4; Identity:10; Validation:23; Evidence:32; Completeness:51; Recommended Edits:58 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-9744293f508350da | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1241,1493] | context_only | [{"current_record_sha256":"1b05f89b24790d65f1318b4499e5aa93ad57d2acc52facdaa1e70cd2cfb012da","finding_id":"SEM:35ba4e16a3091036a41a","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"1b05f89b24790d65f1318b4499e5aa93ad57d2acc52facdaa1e70cd2cfb012da","finding_id":"SEM:677173384d7ce4d3ce55","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-00d3e922fb76f84b | data/ingredients/mapped/Spectinomycin_Dihydrochloride_Pentahydrate.yaml; physicochemical_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}] |
| ev-43000cd36a2ed26d | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml; findings[finding_id=f-d72f0fd923559b78] | context_only | Predecessor structured review finding f-d72f0fd923559b78 in 20261011T024638Z-mim-reconcile-all-batch-11 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-spectinomycin-dihydrochloride-pentahydrate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Spectinomycin_Dihydrochloride_Pentahydrate (data/ingredients/mapped/Spectinomycin_Dihydrochloride_Pentahydrate.yaml)'
started_at: '2026-10-17T08:25:00Z'
finished_at: '2026-10-17T08:30:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: claude-opus-4-6
  independence: independent
  independence_basis: Independent per-record structured review and reconciliation
    against current HEAD and historical review inputs.
skill: review-yaml-record
completion: partial
verdict: needs_curation
native_verdict: mapping_status=MAPPED; open=1; deferred=0
scientific_review: false
summary: Per-record structured review for Spectinomycin_Dihydrochloride_Pentahydrate
  (data/ingredients/mapped/Spectinomycin_Dihydrochloride_Pentahydrate.yaml, record-0c32f5978a02bf70,
  mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound
  to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Spectinomycin_Dihydrochloride_Pentahydrate.yaml
    sha256: 1b05f89b24790d65f1318b4499e5aa93ad57d2acc52facdaa1e70cd2cfb012da
    role: target
  - path: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml
    sha256: a417d1bfc777756925990a4ecae1a6b539746c3606d042df7e1c29a218c62f8b
    role: context
  - path: data/curated/mapped_ingredients.yaml
    sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
    role: context
  - path: mappings/ingredient_mappings.sssom.tsv
    sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
    role: context
  - path: docs/data/mapped_ingredients.csv
    sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
    role: context
  - path: reports/yaml_record_review/Spectinomycin_Dihydrochloride_Pentahydrate.md
    sha256: 0a003f10b5d2cd37593ba5d0c07907b2559d3cba31492993299295a2f7ac4f7d
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-0c32f5978a02bf70
  path: data/ingredients/mapped/Spectinomycin_Dihydrochloride_Pentahydrate.yaml
  label: Spectinomycin_Dihydrochloride_Pentahydrate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Spectinomycin_Dihydrochloride_Pentahydrate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Spectinomycin_Dihydrochloride_Pentahydrate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Spectinomycin_Dihydrochloride_Pentahydrate.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-0c32f5978a02bf70
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-0c32f5978a02bf70
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-0c32f5978a02bf70
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11
    and semantic review dispositions on HEAD.
  target_ids:
  - record-0c32f5978a02bf70
evidence:
- evidence_id: ev-5b0d011ea23dbea0
  kind: record_content
  reference: data/ingredients/mapped/Spectinomycin_Dihydrochloride_Pentahydrate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1887],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:9217","line":1889,"mapping_status":"MAPPED","ontology_id":"CHEBI:9217","preferred_term":"Spectinomycin
    dihydrochloride pentahydrate"}],"identifier":"CHEBI:9217","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:9217","ontology_label":"spectinomycin
    hydrochloride hydrate","ontology_source":"CHEBI"},"preferred_term":"Spectinomycin
    dihydrochloride pentahydrate","sssom_rows":[{"data_row":2628,"object_id":"CHEBI:9217","object_label":"spectinomycin
    hydrochloride hydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Spectinomycin_Dihydrochloride_Pentahydrate","synonym_count":3}'
  snapshot_sha256: 1b05f89b24790d65f1318b4499e5aa93ad57d2acc52facdaa1e70cd2cfb012da
- evidence_id: ev-13b3b988bf005441
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1887]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-d56db0666e5f9e1e
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Spectinomycin_Dihydrochloride_Pentahydrate; data-row positions=[2628]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2628,"object_id":"CHEBI:9217","object_label":"spectinomycin
    hydrochloride hydrate","other":"(2R,4aR,5aR,6S,7S,8R,9S,9aR,10aS)-4a,7,9-trihydroxy-2-methyl-6,8-bis(methylamino)decahydro-4H-pyrano[2,3-b][1,4]benzodioxin-4-one
    dihydrochloride pentahydrate|(2R,4aR,5aR,6S,7S,8R,9S,9aR,10aS)-4a,7,9-trihydroxy-2-methyl-6,8-bis(methylamino)decahydro-4H-pyrano[2,3-b][1,4]benzodioxin-4-one
    dihydrochloride--water (1/5)|(2R,4aR,5aR,6S,7S,8R,9S,9aR,10aS)-4a,7,9-trihydroxy-N,N'',2-trimethyl-4-oxodecahydro-2H-pyrano[2,3-b][1,4]benzodioxine-6,8-diaminium
    dichloride--water (1/5)|CAS:22189-32-8","predicate_id":"skos:exactMatch","subject_id":"MIM:Spectinomycin_Dihydrochloride_Pentahydrate","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-2d26321a3fc07543
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1889]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:9217","line":1889,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:9217","preferred_term":"Spectinomycin
    dihydrochloride pentahydrate","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-925ea0a0b3ee5107
  kind: prior_review
  reference: reports/yaml_record_review/Spectinomycin_Dihydrochloride_Pentahydrate.md
  locator: '`data/ingredients/mapped/Spectinomycin_Dihydrochloride_Pentahydrate.yaml`:2;
    Verdict:4; Identity:10; Validation:23; Evidence:32; Completeness:51; Recommended
    Edits:58'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 0a003f10b5d2cd37593ba5d0c07907b2559d3cba31492993299295a2f7ac4f7d
  quote: "Recommended Edits:\n- Major: either remove `physicochemical_roles.SELECTIVE_AGENT`\
    \ from\n  `data/ingredients/mapped/Spectinomycin_Dihydrochloride_Pentahydrate.yaml`,\
    \ or\n  replace the name-pattern evidence with a source that explicitly uses\n\
    \  spectinomycin dihydrochloride pentahydrate as a selective agent in a culture\n\
    \  context."
- evidence_id: ev-9744293f508350da
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1241,1493]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"1b05f89b24790d65f1318b4499e5aa93ad57d2acc52facdaa1e70cd2cfb012da","finding_id":"SEM:35ba4e16a3091036a41a","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"1b05f89b24790d65f1318b4499e5aa93ad57d2acc52facdaa1e70cd2cfb012da","finding_id":"SEM:677173384d7ce4d3ce55","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-00d3e922fb76f84b
  kind: record_content
  reference: data/ingredients/mapped/Spectinomycin_Dihydrochloride_Pentahydrate.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}]'
  snapshot_sha256: 1b05f89b24790d65f1318b4499e5aa93ad57d2acc52facdaa1e70cd2cfb012da
- evidence_id: ev-43000cd36a2ed26d
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml
  locator: findings[finding_id=f-d72f0fd923559b78]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-d72f0fd923559b78 in 20261011T024638Z-mim-reconcile-all-batch-11
  snapshot_sha256: a417d1bfc777756925990a4ecae1a6b539746c3606d042df7e1c29a218c62f8b
assessments:
- assessment_id: a-d8c539673c0b0cbc
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-0c32f5978a02bf70
  evidence_ids:
  - ev-5b0d011ea23dbea0
  - ev-13b3b988bf005441
  - ev-d56db0666e5f9e1e
  - ev-2d26321a3fc07543
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-d4789d873975cb35
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-0c32f5978a02bf70
  evidence_ids:
  - ev-925ea0a0b3ee5107
  - ev-5b0d011ea23dbea0
  - ev-9744293f508350da
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T16:12:31Z;
    reviewed SHA-256=1b05f89b24790d65f1318b4499e5aa93ad57d2acc52facdaa1e70cd2cfb012da;
    current SHA-256=1b05f89b24790d65f1318b4499e5aa93ad57d2acc52facdaa1e70cd2cfb012da;
    hash_changed=False. Reports=["reports/yaml_record_review/Spectinomycin_Dihydrochloride_Pentahydrate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The salt
    identity passes, but SELECTIVE_AGENT remains a provisional name-pattern role.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-925ea0a0b3ee5107
    - ev-5b0d011ea23dbea0
  - name: legacy-native-ids
    value: '["SEM:35ba4e16a3091036a41a","SEM:677173384d7ce4d3ce55"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-5b0d011ea23dbea0
    - ev-925ea0a0b3ee5107
    - ev-9744293f508350da
- assessment_id: a-00d3e922fb76f84b
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-0c32f5978a02bf70
  evidence_ids:
  - ev-925ea0a0b3ee5107
  - ev-00d3e922fb76f84b
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-925ea0a0b3ee5107
    - ev-00d3e922fb76f84b
findings:
- finding_id: rec-f-d72f0fd923559b78
  issue_key: mim-reconciliation-role-support-0c32f5978a02bf70
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Spectinomycin dihydrochloride pentahydrate'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-0c32f5978a02bf70
  evidence_ids:
  - ev-925ea0a0b3ee5107
  - ev-00d3e922fb76f84b
  - ev-43000cd36a2ed26d
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Spectinomycin_Dihydrochloride_Pentahydrate.yaml
    role: maintained ingredient
  field_paths:
  - physicochemical_roles[0]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024638Z-mim-reconcile-all-batch-11
    finding_id: f-d72f0fd923559b78
actions:
- action_id: rec-action-d72f0fd923559b78
  description: 'Reassess prediction-only role support: Spectinomycin dihydrochloride
    pentahydrate'
  finding_ids:
  - rec-f-d72f0fd923559b78
  target_ids:
  - record-0c32f5978a02bf70
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Spectinomycin_Dihydrochloride_Pentahydrate.yaml
    role: maintained ingredient
  acceptance_checks:
  - Address the exact fields/tokens and evidence gap described in this finding; preserve
    unrelated source labels and audit history.
  - Inspect the original preparation, organism, or mapping evidence where needed;
    do not promote a label/name-pattern inference to proof.
  - For an authorized fix, synchronize maintained surfaces, run focused validation,
    and save an evidence-backed successor citing this finding.
limitations:
- 'Read-only per-record structured review (scientific_review: false); no ingredient
  YAML, curated aggregate, or SSSOM files were modified.'
- Confirmed local evidence gaps and structural issues are recorded as open with bounded
  remediation actions; historical or source-context claims requiring primary recipe/literature
  verification remain deferred (provisional).
tags:
- record-review
- per-record
- reconciliation
- bundle-by-owner
notes:
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb)
  with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.
```
