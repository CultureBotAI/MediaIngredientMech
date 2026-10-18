# Per-record structured review: Bafilomycin_B1 (data/ingredients/mapped/Bafilomycin_B1.yaml)

- Review: 20261017T083000Z-bafilomycin-b1
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Bafilomycin_B1 (data/ingredients/mapped/Bafilomycin_B1.yaml, record-3887feec7173fbc4, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Bafilomycin_B1.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Bafilomycin_B1.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-3887feec7173fbc4 | data/ingredients/mapped/Bafilomycin_B1.yaml | maintained | Bafilomycin_B1 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-3887feec7173fbc4 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-3887feec7173fbc4 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-3887feec7173fbc4 | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-3887feec7173fbc4.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: not_applicable. Targets: record-3887feec7173fbc4.

The latest legacy review reports no outstanding finding. This run verifies local consistency only; it does not renew that earlier scientific pass.

Latest manifest verdict=pass; severity=none; reviewed_at=2026-09-16T09:19:41Z; reviewed SHA-256=82d0577a0a3661bcf782c35e4363b60d70c7f2043a573cb8dc57d768e4d3e0f4; current SHA-256=82d0577a0a3661bcf782c35e4363b60d70c7f2043a573cb8dc57d768e4d3e0f4; hash_changed=False. Reports=["reports/yaml_record_review/Bafilomycin_B1.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI bafilomycin B1 identity, CAS, formula, InChI, SMILES, exact synonym, SSSOM row, and aggregate copy pass.

### Historical provisional-role concern

evidence: concern. Targets: record-3887feec7173fbc4.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-58d32941990f1b2f: Reassess prediction-only role support: Bafilomycin B1

major / open / confirmed; issue key: mim-reconciliation-role-support-3887feec7173fbc4.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-58d32941990f1b2f

Reassess prediction-only role support: Bafilomycin B1

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-afb71a1b7f430d83 | data/ingredients/mapped/Bafilomycin_B1.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[554],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:199416","line":556,"mapping_status":"MAPPED","ontology_id":"CHEBI:199416","preferred_term":"Bafilomycin B1"}],"identifier":"CHEBI:199416","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:199416","ontology_label":"Bafilomycin B1","ontology_source":"CHEBI"},"preferred_term":"Bafilomycin B1","sssom_rows":[{"data_row":484,"object_id":"CHEBI:199416","object_label":"Bafilomycin B1","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Bafilomycin_B1","synonym_count":1} |
| ev-3639ef2a55e7ead3 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [554] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-dd028e9ff709df4c | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Bafilomycin_B1; data-row positions=[484] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":484,"object_id":"CHEBI:199416","object_label":"Bafilomycin B1","other":"[2-hydroxy-2-[3-hydroxy-4-[(4E,6E,12E,14Z)-10-hydroxy-3,15-dimethoxy-7,9,11,13-tetramethyl-16-oxo-1-oxacyclohexadeca-4,6,12,14-tetraen-2-yl]pentan-2-yl]-5-methyl-6-propan-2-yloxan-4-yl] (E)-4-[(2-hydroxy-5-oxocyclopenten-1-yl)amino]-4-oxobut-2-enoate&#124;CAS:88899-56-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Bafilomycin_B1","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-2f694847d73c55b4 | docs/data/mapped_ingredients.csv; CSV lines=[556] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:199416","line":556,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:199416","preferred_term":"Bafilomycin B1","total_occurrences":"0"}] |
| ev-5f6730e8261bc151 | reports/yaml_record_review/Bafilomycin_B1.md; &#96;data/ingredients/mapped/Bafilomycin_B1.yaml&#96;:2; Verdict:4; Identity:10; Validation:23; Evidence:33; Completeness:50; Recommended Edits:57 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-a713ea5aa2c17b4e | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1566] | context_only | [{"current_record_sha256":"82d0577a0a3661bcf782c35e4363b60d70c7f2043a573cb8dc57d768e4d3e0f4","finding_id":"SEM:84e5a7c12025bf311f41","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-726b27e4a4332e97 | data/ingredients/mapped/Bafilomycin_B1.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[554],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:199416","line":556,"mapping_status":"MAPPED","ontology_id":"CHEBI:199416","preferred_term":"Bafilomycin B1"}],"identifier":"CHEBI:199416","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:199416","ontology_label":"Bafilomycin B1","ontology_source":"CHEBI"},"preferred_term":"Bafilomycin B1","sssom_rows":[{"data_row":484,"object_id":"CHEBI:199416","object_label":"Bafilomycin B1","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Bafilomycin_B1","synonym_count":1} |
| ev-e1eee5ed89019aca | reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml; findings[finding_id=f-58d32941990f1b2f] | context_only | Predecessor structured review finding f-58d32941990f1b2f in 20261011T024631Z-mim-reconcile-all-batch-03 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-bafilomycin-b1
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Bafilomycin_B1 (data/ingredients/mapped/Bafilomycin_B1.yaml)'
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
summary: Per-record structured review for Bafilomycin_B1 (data/ingredients/mapped/Bafilomycin_B1.yaml,
  record-3887feec7173fbc4, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Bafilomycin_B1.yaml
    sha256: 82d0577a0a3661bcf782c35e4363b60d70c7f2043a573cb8dc57d768e4d3e0f4
    role: target
  - path: reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml
    sha256: 6b3844c17bf3608ea8f73f824efec195e906ab8d2703fef4cd97fda04f0e65bf
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
  - path: reports/yaml_record_review/Bafilomycin_B1.md
    sha256: 9b0653eef91e772e2cc093e834bbd2a213c760cdd585c14d1fbff5be8e6dd620
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-3887feec7173fbc4
  path: data/ingredients/mapped/Bafilomycin_B1.yaml
  label: Bafilomycin_B1
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Bafilomycin_B1.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Bafilomycin_B1.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Bafilomycin_B1.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-3887feec7173fbc4
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-3887feec7173fbc4
  evidence_ids:
  - ev-afb71a1b7f430d83
  - ev-3639ef2a55e7ead3
  - ev-dd028e9ff709df4c
  - ev-2f694847d73c55b4
  - ev-726b27e4a4332e97
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-3887feec7173fbc4
  evidence_ids:
  - ev-afb71a1b7f430d83
  - ev-a713ea5aa2c17b4e
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-3887feec7173fbc4
  evidence_ids:
  - ev-5f6730e8261bc151
  - ev-a713ea5aa2c17b4e
  - ev-e1eee5ed89019aca
evidence:
- evidence_id: ev-afb71a1b7f430d83
  kind: record_content
  reference: data/ingredients/mapped/Bafilomycin_B1.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[554],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:199416","line":556,"mapping_status":"MAPPED","ontology_id":"CHEBI:199416","preferred_term":"Bafilomycin
    B1"}],"identifier":"CHEBI:199416","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:199416","ontology_label":"Bafilomycin
    B1","ontology_source":"CHEBI"},"preferred_term":"Bafilomycin B1","sssom_rows":[{"data_row":484,"object_id":"CHEBI:199416","object_label":"Bafilomycin
    B1","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Bafilomycin_B1","synonym_count":1}'
  snapshot_sha256: 82d0577a0a3661bcf782c35e4363b60d70c7f2043a573cb8dc57d768e4d3e0f4
- evidence_id: ev-3639ef2a55e7ead3
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [554]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-dd028e9ff709df4c
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Bafilomycin_B1; data-row positions=[484]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":484,"object_id":"CHEBI:199416","object_label":"Bafilomycin
    B1","other":"[2-hydroxy-2-[3-hydroxy-4-[(4E,6E,12E,14Z)-10-hydroxy-3,15-dimethoxy-7,9,11,13-tetramethyl-16-oxo-1-oxacyclohexadeca-4,6,12,14-tetraen-2-yl]pentan-2-yl]-5-methyl-6-propan-2-yloxan-4-yl]
    (E)-4-[(2-hydroxy-5-oxocyclopenten-1-yl)amino]-4-oxobut-2-enoate|CAS:88899-56-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Bafilomycin_B1","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-2f694847d73c55b4
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[556]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:199416","line":556,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:199416","preferred_term":"Bafilomycin
    B1","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-5f6730e8261bc151
  kind: prior_review
  reference: reports/yaml_record_review/Bafilomycin_B1.md
  locator: '`data/ingredients/mapped/Bafilomycin_B1.yaml`:2; Verdict:4; Identity:10;
    Validation:23; Evidence:33; Completeness:50; Recommended Edits:57'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 9b0653eef91e772e2cc093e834bbd2a213c760cdd585c14d1fbff5be8e6dd620
  quote: 'Recommended Edits:

    - None.'
- evidence_id: ev-a713ea5aa2c17b4e
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1566]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"82d0577a0a3661bcf782c35e4363b60d70c7f2043a573cb8dc57d768e4d3e0f4","finding_id":"SEM:84e5a7c12025bf311f41","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-726b27e4a4332e97
  kind: record_content
  reference: data/ingredients/mapped/Bafilomycin_B1.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[554],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:199416","line":556,"mapping_status":"MAPPED","ontology_id":"CHEBI:199416","preferred_term":"Bafilomycin
    B1"}],"identifier":"CHEBI:199416","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:199416","ontology_label":"Bafilomycin
    B1","ontology_source":"CHEBI"},"preferred_term":"Bafilomycin B1","sssom_rows":[{"data_row":484,"object_id":"CHEBI:199416","object_label":"Bafilomycin
    B1","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Bafilomycin_B1","synonym_count":1}'
  snapshot_sha256: 82d0577a0a3661bcf782c35e4363b60d70c7f2043a573cb8dc57d768e4d3e0f4
- evidence_id: ev-e1eee5ed89019aca
  kind: prior_review
  reference: reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml
  locator: findings[finding_id=f-58d32941990f1b2f]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-58d32941990f1b2f in 20261011T024631Z-mim-reconcile-all-batch-03
  snapshot_sha256: 6b3844c17bf3608ea8f73f824efec195e906ab8d2703fef4cd97fda04f0e65bf
assessments:
- assessment_id: a-0e5a8521f96cb1cb
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-3887feec7173fbc4
  evidence_ids:
  - ev-afb71a1b7f430d83
  - ev-3639ef2a55e7ead3
  - ev-dd028e9ff709df4c
  - ev-2f694847d73c55b4
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-00a880103f28ed4b
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: not_applicable
  summary: The latest legacy review reports no outstanding finding. This run verifies
    local consistency only; it does not renew that earlier scientific pass.
  target_ids:
  - record-3887feec7173fbc4
  evidence_ids:
  - ev-5f6730e8261bc151
  - ev-afb71a1b7f430d83
  - ev-a713ea5aa2c17b4e
  details: 'Latest manifest verdict=pass; severity=none; reviewed_at=2026-09-16T09:19:41Z;
    reviewed SHA-256=82d0577a0a3661bcf782c35e4363b60d70c7f2043a573cb8dc57d768e4d3e0f4;
    current SHA-256=82d0577a0a3661bcf782c35e4363b60d70c7f2043a573cb8dc57d768e4d3e0f4;
    hash_changed=False. Reports=["reports/yaml_record_review/Bafilomycin_B1.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI bafilomycin B1 identity, CAS, formula, InChI, SMILES, exact synonym, SSSOM
    row, and aggregate copy pass.'
  dimensions:
  - name: legacy-native-ids
    value: '["SEM:84e5a7c12025bf311f41"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-afb71a1b7f430d83
    - ev-5f6730e8261bc151
    - ev-a713ea5aa2c17b4e
- assessment_id: a-726b27e4a4332e97
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-3887feec7173fbc4
  evidence_ids:
  - ev-5f6730e8261bc151
  - ev-726b27e4a4332e97
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-5f6730e8261bc151
    - ev-726b27e4a4332e97
findings:
- finding_id: rec-f-58d32941990f1b2f
  issue_key: mim-reconciliation-role-support-3887feec7173fbc4
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Bafilomycin B1'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-3887feec7173fbc4
  evidence_ids:
  - ev-5f6730e8261bc151
  - ev-726b27e4a4332e97
  - ev-e1eee5ed89019aca
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Bafilomycin_B1.yaml
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
    review_id: 20261011T024631Z-mim-reconcile-all-batch-03
    finding_id: f-58d32941990f1b2f
actions:
- action_id: rec-action-58d32941990f1b2f
  description: 'Reassess prediction-only role support: Bafilomycin B1'
  finding_ids:
  - rec-f-58d32941990f1b2f
  target_ids:
  - record-3887feec7173fbc4
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Bafilomycin_B1.yaml
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
  with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.
```
