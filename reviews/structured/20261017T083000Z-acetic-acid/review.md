# Per-record structured review: Acetic_Acid (data/ingredients/mapped/Acetic_Acid.yaml)

- Review: 20261017T083000Z-acetic-acid
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Acetic_Acid (data/ingredients/mapped/Acetic_Acid.yaml, record-30469c685512326a, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Acetic_Acid.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Acetic_Acid.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-30469c685512326a | data/ingredients/mapped/Acetic_Acid.yaml | maintained | Acetic_Acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-30469c685512326a | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-30469c685512326a | Role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-30469c685512326a | Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-30469c685512326a.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-30469c685512326a.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T07:02:19Z; reviewed SHA-256=1abbee46f4daba495b5996ebff330179a6bd048e4ce5bb805f6a3f5647e1c8d9; current SHA-256=1abbee46f4daba495b5996ebff330179a6bd048e4ce5bb805f6a3f5647e1c8d9; hash_changed=False. Reports=["reports/yaml_record_review/Acetic_Acid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact acetic acid identity, CAS, exact synonyms, chemistry, SSSOM row, and aggregate pass, but the ENERGY_SOURCE role is still only provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-30469c685512326a.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-686fcdac8a2fc45a: Reassess prediction-only role support: Acetic acid

major / open / confirmed; issue key: mim-reconciliation-role-support-30469c685512326a.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-686fcdac8a2fc45a

Reassess prediction-only role support: Acetic acid

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-3bdcccb6e6053c34 | data/ingredients/mapped/Acetic_Acid.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[440],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15366","line":442,"mapping_status":"MAPPED","ontology_id":"CHEBI:15366","preferred_term":"Acetic acid"}],"identifier":"CHEBI:15366","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":56,"edge_count":56,"occurrences":56},"occurrence_statistics":{"media_count":56,"total_occurrences":56},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:15366","ontology_label":"acetic acid","ontology_source":"CHEBI"},"preferred_term":"Acetic acid","sssom_rows":[{"data_row":280,"object_id":"CHEBI:15366","object_label":"acetic acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Acetic_Acid","synonym_count":18} |
| ev-15ab5abd411e323f | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [440] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-bab766fdd5a8b289 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Acetic_Acid; data-row positions=[280] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":280,"object_id":"CHEBI:15366","object_label":"acetic acid","other":"AcOH&#124;CH3-COOH&#124;CH3CO2H&#124;E 260&#124;E-260&#124;E260&#124;Essigsaeure&#124;Ethanoic acid&#124;Ethylic acid&#124;HOAc&#124;INS No. 260&#124;MeCO2H&#124;MeCOOH&#124;Methanecarboxylic acid&#124;acide acetique&#124;ethoic acid&#124;CAS:64-19-7","predicate_id":"skos:exactMatch","subject_id":"MIM:Acetic_Acid","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-52bb223c9369bac9 | docs/data/mapped_ingredients.csv; CSV lines=[442] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:15366","line":442,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"56","ontology_id":"CHEBI:15366","preferred_term":"Acetic acid","total_occurrences":"56"}] |
| ev-584f796d342ab412 | reports/yaml_record_review/Acetic_Acid.md; &#96;data/ingredients/mapped/Acetic_Acid.yaml&#96;:2; Verdict:4; Identity:11; Validation:26; Evidence:43; Completeness:60; Recommended Edits:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-54aa9e74b9d1dee2 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[197,1786] | context_only | [{"current_record_sha256":"1abbee46f4daba495b5996ebff330179a6bd048e4ce5bb805f6a3f5647e1c8d9","finding_id":"SEM:387a7a9783da053124a0","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"1abbee46f4daba495b5996ebff330179a6bd048e4ce5bb805f6a3f5647e1c8d9","finding_id":"SEM:f6c670a990cd7309117a","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-2a3e95000a873463 | data/ingredients/mapped/Acetic_Acid.yaml; nutritional_roles[1] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[440],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15366","line":442,"mapping_status":"MAPPED","ontology_id":"CHEBI:15366","preferred_term":"Acetic acid"}],"identifier":"CHEBI:15366","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":56,"edge_count":56,"occurrences":56},"occurrence_statistics":{"media_count":56,"total_occurrences":56},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:15366","ontology_label":"acetic acid","ontology_source":"CHEBI"},"preferred_term":"Acetic acid","sssom_rows":[{"data_row":280,"object_id":"CHEBI:15366","object_label":"acetic acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Acetic_Acid","synonym_count":18} |
| ev-332934ca95ac584c | reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml; findings[finding_id=f-686fcdac8a2fc45a] | context_only | Predecessor structured review finding f-686fcdac8a2fc45a in 20261011T024630Z-mim-reconcile-all-batch-02 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-acetic-acid
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Acetic_Acid (data/ingredients/mapped/Acetic_Acid.yaml)'
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
summary: Per-record structured review for Acetic_Acid (data/ingredients/mapped/Acetic_Acid.yaml,
  record-30469c685512326a, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Acetic_Acid.yaml
    sha256: 1abbee46f4daba495b5996ebff330179a6bd048e4ce5bb805f6a3f5647e1c8d9
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
  - path: reports/yaml_record_review/Acetic_Acid.md
    sha256: 3cdea762066c6fd5264df211867d300367acf1ee7ad1f4726c989e426406b63e
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-30469c685512326a
  path: data/ingredients/mapped/Acetic_Acid.yaml
  label: Acetic_Acid
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Acetic_Acid.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Acetic_Acid.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Acetic_Acid.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-30469c685512326a
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-30469c685512326a
  evidence_ids:
  - ev-3bdcccb6e6053c34
  - ev-15ab5abd411e323f
  - ev-bab766fdd5a8b289
  - ev-52bb223c9369bac9
  - ev-2a3e95000a873463
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-30469c685512326a
  evidence_ids:
  - ev-3bdcccb6e6053c34
  - ev-54aa9e74b9d1dee2
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02
    and semantic review dispositions on HEAD.
  target_ids:
  - record-30469c685512326a
  evidence_ids:
  - ev-584f796d342ab412
  - ev-54aa9e74b9d1dee2
  - ev-332934ca95ac584c
evidence:
- evidence_id: ev-3bdcccb6e6053c34
  kind: record_content
  reference: data/ingredients/mapped/Acetic_Acid.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[440],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15366","line":442,"mapping_status":"MAPPED","ontology_id":"CHEBI:15366","preferred_term":"Acetic
    acid"}],"identifier":"CHEBI:15366","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":56,"edge_count":56,"occurrences":56},"occurrence_statistics":{"media_count":56,"total_occurrences":56},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:15366","ontology_label":"acetic
    acid","ontology_source":"CHEBI"},"preferred_term":"Acetic acid","sssom_rows":[{"data_row":280,"object_id":"CHEBI:15366","object_label":"acetic
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Acetic_Acid","synonym_count":18}'
  snapshot_sha256: 1abbee46f4daba495b5996ebff330179a6bd048e4ce5bb805f6a3f5647e1c8d9
- evidence_id: ev-15ab5abd411e323f
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [440]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-bab766fdd5a8b289
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Acetic_Acid; data-row positions=[280]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":280,"object_id":"CHEBI:15366","object_label":"acetic
    acid","other":"AcOH|CH3-COOH|CH3CO2H|E 260|E-260|E260|Essigsaeure|Ethanoic acid|Ethylic
    acid|HOAc|INS No. 260|MeCO2H|MeCOOH|Methanecarboxylic acid|acide acetique|ethoic
    acid|CAS:64-19-7","predicate_id":"skos:exactMatch","subject_id":"MIM:Acetic_Acid","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-52bb223c9369bac9
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[442]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:15366","line":442,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"56","ontology_id":"CHEBI:15366","preferred_term":"Acetic
    acid","total_occurrences":"56"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-584f796d342ab412
  kind: prior_review
  reference: reports/yaml_record_review/Acetic_Acid.md
  locator: '`data/ingredients/mapped/Acetic_Acid.yaml`:2; Verdict:4; Identity:11;
    Validation:26; Evidence:43; Completeness:60; Recommended Edits:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 3cdea762066c6fd5264df211867d300367acf1ee7ad1f4726c989e426406b63e
  quote: "Recommended Edits:\n- Replace or remove\n  `data/ingredients/mapped/Acetic_Acid.yaml`'s\n\
    \  `nutritional_roles.ENERGY_SOURCE` entry after inspecting evidence that\n  specifically\
    \ supports acetic acid as an energy source. Re-run\n  `scripts/validate_strict.py`\
    \ and `scripts/validate_sssom_invariants.py`."
- evidence_id: ev-54aa9e74b9d1dee2
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[197,1786]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"1abbee46f4daba495b5996ebff330179a6bd048e4ce5bb805f6a3f5647e1c8d9","finding_id":"SEM:387a7a9783da053124a0","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"1abbee46f4daba495b5996ebff330179a6bd048e4ce5bb805f6a3f5647e1c8d9","finding_id":"SEM:f6c670a990cd7309117a","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-2a3e95000a873463
  kind: record_content
  reference: data/ingredients/mapped/Acetic_Acid.yaml
  locator: nutritional_roles[1]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[440],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15366","line":442,"mapping_status":"MAPPED","ontology_id":"CHEBI:15366","preferred_term":"Acetic
    acid"}],"identifier":"CHEBI:15366","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":56,"edge_count":56,"occurrences":56},"occurrence_statistics":{"media_count":56,"total_occurrences":56},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:15366","ontology_label":"acetic
    acid","ontology_source":"CHEBI"},"preferred_term":"Acetic acid","sssom_rows":[{"data_row":280,"object_id":"CHEBI:15366","object_label":"acetic
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Acetic_Acid","synonym_count":18}'
  snapshot_sha256: 1abbee46f4daba495b5996ebff330179a6bd048e4ce5bb805f6a3f5647e1c8d9
- evidence_id: ev-332934ca95ac584c
  kind: prior_review
  reference: reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml
  locator: findings[finding_id=f-686fcdac8a2fc45a]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-686fcdac8a2fc45a in 20261011T024630Z-mim-reconcile-all-batch-02
  snapshot_sha256: 799a1a80fa398851bced286dd0f68a97e6a22f7090d53677678dc13b92c6f076
assessments:
- assessment_id: a-8e6945ccae58deb0
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-30469c685512326a
  evidence_ids:
  - ev-3bdcccb6e6053c34
  - ev-15ab5abd411e323f
  - ev-bab766fdd5a8b289
  - ev-52bb223c9369bac9
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-fd2f6c5252f19633
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-30469c685512326a
  evidence_ids:
  - ev-584f796d342ab412
  - ev-3bdcccb6e6053c34
  - ev-54aa9e74b9d1dee2
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T07:02:19Z;
    reviewed SHA-256=1abbee46f4daba495b5996ebff330179a6bd048e4ce5bb805f6a3f5647e1c8d9;
    current SHA-256=1abbee46f4daba495b5996ebff330179a6bd048e4ce5bb805f6a3f5647e1c8d9;
    hash_changed=False. Reports=["reports/yaml_record_review/Acetic_Acid.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact acetic
    acid identity, CAS, exact synonyms, chemistry, SSSOM row, and aggregate pass,
    but the ENERGY_SOURCE role is still only provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-584f796d342ab412
    - ev-3bdcccb6e6053c34
  - name: legacy-native-ids
    value: '["SEM:387a7a9783da053124a0","SEM:f6c670a990cd7309117a"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-3bdcccb6e6053c34
    - ev-584f796d342ab412
    - ev-54aa9e74b9d1dee2
- assessment_id: a-2a3e95000a873463
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-30469c685512326a
  evidence_ids:
  - ev-584f796d342ab412
  - ev-2a3e95000a873463
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-584f796d342ab412
    - ev-2a3e95000a873463
findings:
- finding_id: rec-f-686fcdac8a2fc45a
  issue_key: mim-reconciliation-role-support-30469c685512326a
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Acetic acid'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-30469c685512326a
  evidence_ids:
  - ev-584f796d342ab412
  - ev-2a3e95000a873463
  - ev-332934ca95ac584c
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Acetic_Acid.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[1]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024630Z-mim-reconcile-all-batch-02
    finding_id: f-686fcdac8a2fc45a
actions:
- action_id: rec-action-686fcdac8a2fc45a
  description: 'Reassess prediction-only role support: Acetic acid'
  finding_ids:
  - rec-f-686fcdac8a2fc45a
  target_ids:
  - record-30469c685512326a
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Acetic_Acid.yaml
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
