# Per-record structured review: Abyssomicin_G (data/ingredients/mapped/Abyssomicin_G.yaml)

- Review: 20261017T083000Z-abyssomicin-g
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Abyssomicin_G (data/ingredients/mapped/Abyssomicin_G.yaml, record-cad48bd9762bd44c, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Abyssomicin_G.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Abyssomicin_G.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-cad48bd9762bd44c | data/ingredients/mapped/Abyssomicin_G.yaml | maintained | Abyssomicin_G |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-cad48bd9762bd44c | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-cad48bd9762bd44c | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-cad48bd9762bd44c | Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-cad48bd9762bd44c.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-cad48bd9762bd44c.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T06:59:02Z; reviewed SHA-256=2fa726b15b881eb658b52e9dc948a7f7d8da8576561d6d4901e167395f46ad17; current SHA-256=2fa726b15b881eb658b52e9dc948a7f7d8da8576561d6d4901e167395f46ad17; hash_changed=False. Reports=["reports/yaml_record_review/Abyssomicin_G.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The placeholder kgmicrobe identity is intentionally retained pending exact ontology identity; OLS candidate review found no exact match, but the selective-agent role is still only provisional computational curation.

### Historical provisional-role concern

evidence: concern. Targets: record-cad48bd9762bd44c.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-134b9f476319755d: Reassess prediction-only role support: Abyssomicin G

major / open / confirmed; issue key: mim-reconciliation-role-support-cad48bd9762bd44c.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-134b9f476319755d

Reassess prediction-only role support: Abyssomicin G

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-af7cdc9e3db85a84 | data/ingredients/mapped/Abyssomicin_G.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[433],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:abyssomicin_g","line":435,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.compound:abyssomicin_g","preferred_term":"Abyssomicin G"}],"identifier":"kgmicrobe.compound:abyssomicin_g","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"PLACEHOLDER","ontology_id":"kgmicrobe.compound:abyssomicin_g","ontology_label":"Abyssomicin G","ontology_source":"kgmicrobe.compound"},"preferred_term":"Abyssomicin G","sssom_rows":[{"data_row":274,"object_id":"kgmicrobe.compound:abyssomicin_g","object_label":"Abyssomicin G","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Abyssomicin_G","synonym_count":0} |
| ev-f52c40e9d01bcffd | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [433] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-1f2a543366cb8171 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Abyssomicin_G; data-row positions=[274] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":274,"object_id":"kgmicrobe.compound:abyssomicin_g","object_label":"Abyssomicin G","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Abyssomicin_G","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-f9bcd5f48a0ef268 | docs/data/mapped_ingredients.csv; CSV lines=[435] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:abyssomicin_g","line":435,"mapping_quality":"PLACEHOLDER","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.compound:abyssomicin_g","preferred_term":"Abyssomicin G","total_occurrences":"0"}] |
| ev-daa9dedee598ce7f | reports/yaml_record_review/Abyssomicin_G.md; &#96;data/ingredients/mapped/Abyssomicin_G.yaml&#96;:2; Verdict:4; Identity:11; Validation:27; Evidence:40; Completeness:59; Recommended Edits:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-b7fed9bd96ab1557 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[191,1968] | context_only | [{"current_record_sha256":"2fa726b15b881eb658b52e9dc948a7f7d8da8576561d6d4901e167395f46ad17","finding_id":"SEM:e96ad9f566308dc006ce","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"2fa726b15b881eb658b52e9dc948a7f7d8da8576561d6d4901e167395f46ad17","finding_id":"SEM:228e13235bf0889f4235","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-15b6ea4c2e3daa35 | data/ingredients/mapped/Abyssomicin_G.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[433],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:abyssomicin_g","line":435,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.compound:abyssomicin_g","preferred_term":"Abyssomicin G"}],"identifier":"kgmicrobe.compound:abyssomicin_g","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"PLACEHOLDER","ontology_id":"kgmicrobe.compound:abyssomicin_g","ontology_label":"Abyssomicin G","ontology_source":"kgmicrobe.compound"},"preferred_term":"Abyssomicin G","sssom_rows":[{"data_row":274,"object_id":"kgmicrobe.compound:abyssomicin_g","object_label":"Abyssomicin G","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Abyssomicin_G","synonym_count":0} |
| ev-aa45fec5815f46e8 | reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml; findings[finding_id=f-134b9f476319755d] | context_only | Predecessor structured review finding f-134b9f476319755d in 20261011T024630Z-mim-reconcile-all-batch-02 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-abyssomicin-g
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Abyssomicin_G (data/ingredients/mapped/Abyssomicin_G.yaml)'
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
summary: Per-record structured review for Abyssomicin_G (data/ingredients/mapped/Abyssomicin_G.yaml,
  record-cad48bd9762bd44c, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Abyssomicin_G.yaml
    sha256: 2fa726b15b881eb658b52e9dc948a7f7d8da8576561d6d4901e167395f46ad17
    role: target
  - path: reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml
    sha256: 799a1a80fa398851bced286dd0f68a97e6a22f7090d53677678dc13b92c6f076
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
  - path: reports/yaml_record_review/Abyssomicin_G.md
    sha256: d3f6db2f7aca4ce81e866ad8418b3664bdf64eb2a98d4883a86c1f08afcec4f4
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-cad48bd9762bd44c
  path: data/ingredients/mapped/Abyssomicin_G.yaml
  label: Abyssomicin_G
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Abyssomicin_G.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Abyssomicin_G.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Abyssomicin_G.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-cad48bd9762bd44c
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-cad48bd9762bd44c
  evidence_ids:
  - ev-af7cdc9e3db85a84
  - ev-f52c40e9d01bcffd
  - ev-1f2a543366cb8171
  - ev-f9bcd5f48a0ef268
  - ev-15b6ea4c2e3daa35
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-cad48bd9762bd44c
  evidence_ids:
  - ev-af7cdc9e3db85a84
  - ev-b7fed9bd96ab1557
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02
    and semantic review dispositions on HEAD.
  target_ids:
  - record-cad48bd9762bd44c
  evidence_ids:
  - ev-daa9dedee598ce7f
  - ev-b7fed9bd96ab1557
  - ev-aa45fec5815f46e8
evidence:
- evidence_id: ev-af7cdc9e3db85a84
  kind: record_content
  reference: data/ingredients/mapped/Abyssomicin_G.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[433],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:abyssomicin_g","line":435,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.compound:abyssomicin_g","preferred_term":"Abyssomicin
    G"}],"identifier":"kgmicrobe.compound:abyssomicin_g","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"PLACEHOLDER","ontology_id":"kgmicrobe.compound:abyssomicin_g","ontology_label":"Abyssomicin
    G","ontology_source":"kgmicrobe.compound"},"preferred_term":"Abyssomicin G","sssom_rows":[{"data_row":274,"object_id":"kgmicrobe.compound:abyssomicin_g","object_label":"Abyssomicin
    G","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Abyssomicin_G","synonym_count":0}'
  snapshot_sha256: 2fa726b15b881eb658b52e9dc948a7f7d8da8576561d6d4901e167395f46ad17
- evidence_id: ev-f52c40e9d01bcffd
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [433]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-1f2a543366cb8171
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Abyssomicin_G; data-row positions=[274]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":274,"object_id":"kgmicrobe.compound:abyssomicin_g","object_label":"Abyssomicin
    G","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Abyssomicin_G","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-f9bcd5f48a0ef268
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[435]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:abyssomicin_g","line":435,"mapping_quality":"PLACEHOLDER","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.compound:abyssomicin_g","preferred_term":"Abyssomicin
    G","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-daa9dedee598ce7f
  kind: prior_review
  reference: reports/yaml_record_review/Abyssomicin_G.md
  locator: '`data/ingredients/mapped/Abyssomicin_G.yaml`:2; Verdict:4; Identity:11;
    Validation:27; Evidence:40; Completeness:59; Recommended Edits:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: d3f6db2f7aca4ce81e866ad8418b3664bdf64eb2a98d4883a86c1f08afcec4f4
  quote: "Recommended Edits:\n- Replace or remove\n  `data/ingredients/mapped/Abyssomicin_G.yaml`'s\n\
    \  `physicochemical_roles.SELECTIVE_AGENT` entry after inspecting evidence that\n\
    \  specifically supports Abyssomicin G as a selective agent. Re-run\n  `scripts/validate_strict.py`\
    \ and `scripts/validate_sssom_invariants.py`.\n- Leave `kgmicrobe.compound:abyssomicin_g`\
    \ in place unless a future exact\n  external ontology identity is found."
- evidence_id: ev-b7fed9bd96ab1557
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[191,1968]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"2fa726b15b881eb658b52e9dc948a7f7d8da8576561d6d4901e167395f46ad17","finding_id":"SEM:e96ad9f566308dc006ce","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"2fa726b15b881eb658b52e9dc948a7f7d8da8576561d6d4901e167395f46ad17","finding_id":"SEM:228e13235bf0889f4235","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-15b6ea4c2e3daa35
  kind: record_content
  reference: data/ingredients/mapped/Abyssomicin_G.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[433],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:abyssomicin_g","line":435,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.compound:abyssomicin_g","preferred_term":"Abyssomicin
    G"}],"identifier":"kgmicrobe.compound:abyssomicin_g","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"PLACEHOLDER","ontology_id":"kgmicrobe.compound:abyssomicin_g","ontology_label":"Abyssomicin
    G","ontology_source":"kgmicrobe.compound"},"preferred_term":"Abyssomicin G","sssom_rows":[{"data_row":274,"object_id":"kgmicrobe.compound:abyssomicin_g","object_label":"Abyssomicin
    G","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Abyssomicin_G","synonym_count":0}'
  snapshot_sha256: 2fa726b15b881eb658b52e9dc948a7f7d8da8576561d6d4901e167395f46ad17
- evidence_id: ev-aa45fec5815f46e8
  kind: prior_review
  reference: reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml
  locator: findings[finding_id=f-134b9f476319755d]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-134b9f476319755d in 20261011T024630Z-mim-reconcile-all-batch-02
  snapshot_sha256: 799a1a80fa398851bced286dd0f68a97e6a22f7090d53677678dc13b92c6f076
assessments:
- assessment_id: a-d7858ddd523f26f3
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-cad48bd9762bd44c
  evidence_ids:
  - ev-af7cdc9e3db85a84
  - ev-f52c40e9d01bcffd
  - ev-1f2a543366cb8171
  - ev-f9bcd5f48a0ef268
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-49b5fee47a8192e0
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-cad48bd9762bd44c
  evidence_ids:
  - ev-daa9dedee598ce7f
  - ev-af7cdc9e3db85a84
  - ev-b7fed9bd96ab1557
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T06:59:02Z;
    reviewed SHA-256=2fa726b15b881eb658b52e9dc948a7f7d8da8576561d6d4901e167395f46ad17;
    current SHA-256=2fa726b15b881eb658b52e9dc948a7f7d8da8576561d6d4901e167395f46ad17;
    hash_changed=False. Reports=["reports/yaml_record_review/Abyssomicin_G.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The placeholder
    kgmicrobe identity is intentionally retained pending exact ontology identity;
    OLS candidate review found no exact match, but the selective-agent role is still
    only provisional computational curation.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-daa9dedee598ce7f
    - ev-af7cdc9e3db85a84
  - name: legacy-native-ids
    value: '["SEM:e96ad9f566308dc006ce","SEM:228e13235bf0889f4235"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-af7cdc9e3db85a84
    - ev-daa9dedee598ce7f
    - ev-b7fed9bd96ab1557
- assessment_id: a-15b6ea4c2e3daa35
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-cad48bd9762bd44c
  evidence_ids:
  - ev-daa9dedee598ce7f
  - ev-15b6ea4c2e3daa35
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-daa9dedee598ce7f
    - ev-15b6ea4c2e3daa35
findings:
- finding_id: rec-f-134b9f476319755d
  issue_key: mim-reconciliation-role-support-cad48bd9762bd44c
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Abyssomicin G'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-cad48bd9762bd44c
  evidence_ids:
  - ev-daa9dedee598ce7f
  - ev-15b6ea4c2e3daa35
  - ev-aa45fec5815f46e8
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Abyssomicin_G.yaml
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
    review_id: 20261011T024630Z-mim-reconcile-all-batch-02
    finding_id: f-134b9f476319755d
actions:
- action_id: rec-action-134b9f476319755d
  description: 'Reassess prediction-only role support: Abyssomicin G'
  finding_ids:
  - rec-f-134b9f476319755d
  target_ids:
  - record-cad48bd9762bd44c
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Abyssomicin_G.yaml
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
  with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.
```
