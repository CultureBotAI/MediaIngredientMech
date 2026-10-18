# Per-record structured review: PYG (data/ingredients/mapped/PYG.yaml)

- Review: 20261017T083000Z-pyg
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for PYG (data/ingredients/mapped/PYG.yaml, record-edbb2f79997b9e9e, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/PYG.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/PYG.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-edbb2f79997b9e9e | data/ingredients/mapped/PYG.yaml | maintained | PYG |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-edbb2f79997b9e9e | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-edbb2f79997b9e9e | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-edbb2f79997b9e9e | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-edbb2f79997b9e9e.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-edbb2f79997b9e9e.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T08:24:27Z; reviewed SHA-256=2560177ec64534d39f8b7a9a151bbddd08b70f1c34ce50d7cc6f603dd44ddb83; current SHA-256=2560177ec64534d39f8b7a9a151bbddd08b70f1c34ce50d7cc6f603dd44ddb83; hash_changed=False. Reports=["reports/yaml_record_review/PYG.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local kgmicrobe.ingredient PYG mixture is internally clean, but MICRO:0001573 may be a promotable public term.

## Findings

### rec-f-e6aadac40bd2b53a: Reassess component source scope: PYG

major / deferred / provisional; issue key: mim-semantic-component-source-scope-edbb2f79997b9e9e.

Expansion/interpretation is retained as an assertion, but the exact source preparation must be verified before semantic approval. UNKNOWN/PARTIAL completeness is not proof of membership. (Historical finding remains unresolved; no blanket approval.). Affected unit(s): MIM.assertion:aa19cfc3c85a8742a6f189be5d6c1e1300fd99e772d77253905ded84b4b6b2a4, MIM.assertion:d355adadf96b6288ce36974d79d816537ae9b9b05df9da518df6e6cbbe517286, MIM.assertion:e5cf9cccb55065f0704d23038f0ffe71da08615401f01578de9f83be35efffb7.

Disposition: Expansion/interpretation is retained as an assertion, but the exact source preparation must be verified before semantic approval. UNKNOWN/PARTIAL completeness is not proof of membership. (Historical finding remains unresolved; no blanket approval.). Affected unit(s): MIM.assertion:aa19cfc3c85a8742a6f189be5d6c1e1300fd99e772d77253905ded84b4b6b2a4, MIM.assertion:d355adadf96b6288ce36974d79d816537ae9b9b05df9da518df6e6cbbe517286, MIM.assertion:e5cf9cccb55065f0704d23038f0ffe71da08615401f01578de9f83be35efffb7.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-647bda3c0dc23f84 | data/ingredients/mapped/PYG.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[55],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:pyg","line":57,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:pyg","preferred_term":"PYG"}],"identifier":"kgmicrobe.ingredient:pyg","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":114,"source":"microbedecoder","source_columns":"bergey:substrates"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:pyg","ontology_label":"PYG","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"PYG","sssom_rows":[{"data_row":2182,"object_id":"kgmicrobe.ingredient:pyg","object_label":"PYG","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:PYG","synonym_count":1} |
| ev-d8a874aba6ac00e6 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [55] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-49a500789daf5d0d | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:PYG; data-row positions=[2182] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2182,"object_id":"kgmicrobe.ingredient:pyg","object_label":"PYG","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:PYG","validation_method":"manual:move_mapped_out_of_unmapped_collection&#124;MOVED&#124;2026-08-15"}] |
| ev-52a11515022034b2 | docs/data/mapped_ingredients.csv; CSV lines=[57] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:pyg","line":57,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.ingredient:pyg","preferred_term":"PYG","total_occurrences":"0"}] |
| ev-bd00027f8ab15097 | reports/yaml_record_review/PYG.md; &#96;data/ingredients/mapped/PYG.yaml&#96;:2; Verdict:4; Identity:10; Validation:20; Evidence:29; Completeness:47; Recommended Edits:54 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-f4337d7822a86900 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1090,1855,1975,2030] | context_only | [{"current_record_sha256":"2560177ec64534d39f8b7a9a151bbddd08b70f1c34ce50d7cc6f603dd44ddb83","finding_id":"SEM:221b5e55fef6d0417565","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"2560177ec64534d39f8b7a9a151bbddd08b70f1c34ce50d7cc6f603dd44ddb83","finding_id":"SEM:bd092a1dc97dbe2d7627","kind":"component_source_scope","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"2560177ec64534d39f8b7a9a151bbddd08b70f1c34ce50d7cc6f603dd44ddb83","finding_id":"SEM:daaee2adea08a4acf238","kind":"component_source_scope","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"2560177ec64534d39f8b7a9a151bbddd08b70f1c34ce50d7cc6f603dd44ddb83","finding_id":"SEM:bde0616e0417d37fdc20","kind":"component_source_scope","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-9b7fa5c37ead0f6f | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; current_record=data/ingredients/mapped/PYG.yaml | context_only | Semantic review finding dispositions ledger |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-pyg
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: PYG (data/ingredients/mapped/PYG.yaml)'
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
native_verdict: mapping_status=MAPPED; open=0; deferred=1
scientific_review: false
summary: Per-record structured review for PYG (data/ingredients/mapped/PYG.yaml, record-edbb2f79997b9e9e,
  mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound
  to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/PYG.yaml
    sha256: 2560177ec64534d39f8b7a9a151bbddd08b70f1c34ce50d7cc6f603dd44ddb83
    role: target
  - path: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
    sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
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
  - path: reports/yaml_record_review/PYG.md
    sha256: 9a616201f420e52e39256da3f2efbff66266a636838ee48ec968443c948b7e05
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-edbb2f79997b9e9e
  path: data/ingredients/mapped/PYG.yaml
  label: PYG
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/PYG.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/PYG.yaml covering
    current record state, role evidence support, published surfaces, and residual
    historical review claims.
  selection: Single record data/ingredients/mapped/PYG.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-edbb2f79997b9e9e
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-edbb2f79997b9e9e
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-edbb2f79997b9e9e
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-edbb2f79997b9e9e
evidence:
- evidence_id: ev-647bda3c0dc23f84
  kind: record_content
  reference: data/ingredients/mapped/PYG.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[55],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:pyg","line":57,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:pyg","preferred_term":"PYG"}],"identifier":"kgmicrobe.ingredient:pyg","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":114,"source":"microbedecoder","source_columns":"bergey:substrates"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:pyg","ontology_label":"PYG","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"PYG","sssom_rows":[{"data_row":2182,"object_id":"kgmicrobe.ingredient:pyg","object_label":"PYG","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:PYG","synonym_count":1}'
  snapshot_sha256: 2560177ec64534d39f8b7a9a151bbddd08b70f1c34ce50d7cc6f603dd44ddb83
- evidence_id: ev-d8a874aba6ac00e6
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [55]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-49a500789daf5d0d
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:PYG; data-row positions=[2182]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2182,"object_id":"kgmicrobe.ingredient:pyg","object_label":"PYG","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:PYG","validation_method":"manual:move_mapped_out_of_unmapped_collection|MOVED|2026-08-15"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-52a11515022034b2
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[57]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:pyg","line":57,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.ingredient:pyg","preferred_term":"PYG","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-bd00027f8ab15097
  kind: prior_review
  reference: reports/yaml_record_review/PYG.md
  locator: '`data/ingredients/mapped/PYG.yaml`:2; Verdict:4; Identity:10; Validation:20;
    Evidence:29; Completeness:47; Recommended Edits:54'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 9a616201f420e52e39256da3f2efbff66266a636838ee48ec968443c948b7e05
  quote: "Recommended Edits:\n- Major: evaluate `MICRO:0001573` as a replacement grounding\
    \ for\n  `data/ingredients/mapped/PYG.yaml`. If it denotes the same PYG formulation,\n\
    \  promote the record from `kgmicrobe.ingredient:pyg` to a MICRO mapping, rebuild\n\
    \  `mappings/ingredient_mappings.sssom.tsv`, and rerun\n  `scripts/validate_sssom_invariants.py`\
    \ plus\n  `scripts/validate_component_partonomy.py`."
- evidence_id: ev-f4337d7822a86900
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1090,1855,1975,2030]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"2560177ec64534d39f8b7a9a151bbddd08b70f1c34ce50d7cc6f603dd44ddb83","finding_id":"SEM:221b5e55fef6d0417565","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"2560177ec64534d39f8b7a9a151bbddd08b70f1c34ce50d7cc6f603dd44ddb83","finding_id":"SEM:bd092a1dc97dbe2d7627","kind":"component_source_scope","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"2560177ec64534d39f8b7a9a151bbddd08b70f1c34ce50d7cc6f603dd44ddb83","finding_id":"SEM:daaee2adea08a4acf238","kind":"component_source_scope","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"2560177ec64534d39f8b7a9a151bbddd08b70f1c34ce50d7cc6f603dd44ddb83","finding_id":"SEM:bde0616e0417d37fdc20","kind":"component_source_scope","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-9b7fa5c37ead0f6f
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: current_record=data/ingredients/mapped/PYG.yaml
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Semantic review finding dispositions ledger
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-378b7238a1c0d517
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-edbb2f79997b9e9e
  evidence_ids:
  - ev-647bda3c0dc23f84
  - ev-d8a874aba6ac00e6
  - ev-49a500789daf5d0d
  - ev-52a11515022034b2
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-65dadbddc2c716c8
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-edbb2f79997b9e9e
  evidence_ids:
  - ev-bd00027f8ab15097
  - ev-647bda3c0dc23f84
  - ev-f4337d7822a86900
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T08:24:27Z;
    reviewed SHA-256=2560177ec64534d39f8b7a9a151bbddd08b70f1c34ce50d7cc6f603dd44ddb83;
    current SHA-256=2560177ec64534d39f8b7a9a151bbddd08b70f1c34ce50d7cc6f603dd44ddb83;
    hash_changed=False. Reports=["reports/yaml_record_review/PYG.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The local kgmicrobe.ingredient
    PYG mixture is internally clean, but MICRO:0001573 may be a promotable public
    term.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-bd00027f8ab15097
    - ev-647bda3c0dc23f84
  - name: legacy-native-ids
    value: '["SEM:221b5e55fef6d0417565","SEM:bd092a1dc97dbe2d7627","SEM:daaee2adea08a4acf238","SEM:bde0616e0417d37fdc20"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-647bda3c0dc23f84
    - ev-bd00027f8ab15097
    - ev-f4337d7822a86900
findings:
- finding_id: rec-f-e6aadac40bd2b53a
  issue_key: mim-semantic-component-source-scope-edbb2f79997b9e9e
  category: representation
  severity: major
  status: deferred
  certainty: provisional
  title: 'Reassess component source scope: PYG'
  description: 'Expansion/interpretation is retained as an assertion, but the exact
    source preparation must be verified before semantic approval. UNKNOWN/PARTIAL
    completeness is not proof of membership. (Historical finding remains unresolved;
    no blanket approval.). Affected unit(s): MIM.assertion:aa19cfc3c85a8742a6f189be5d6c1e1300fd99e772d77253905ded84b4b6b2a4,
    MIM.assertion:d355adadf96b6288ce36974d79d816537ae9b9b05df9da518df6e6cbbe517286,
    MIM.assertion:e5cf9cccb55065f0704d23038f0ffe71da08615401f01578de9f83be35efffb7.'
  disposition_reason: 'Expansion/interpretation is retained as an assertion, but the
    exact source preparation must be verified before semantic approval. UNKNOWN/PARTIAL
    completeness is not proof of membership. (Historical finding remains unresolved;
    no blanket approval.). Affected unit(s): MIM.assertion:aa19cfc3c85a8742a6f189be5d6c1e1300fd99e772d77253905ded84b4b6b2a4,
    MIM.assertion:d355adadf96b6288ce36974d79d816537ae9b9b05df9da518df6e6cbbe517286,
    MIM.assertion:e5cf9cccb55065f0704d23038f0ffe71da08615401f01578de9f83be35efffb7.'
  target_ids:
  - record-edbb2f79997b9e9e
  evidence_ids:
  - ev-647bda3c0dc23f84
  - ev-9b7fa5c37ead0f6f
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/PYG.yaml
    role: maintained ingredient
  field_paths:
  - synonyms
  - occurrence_statistics
  tags:
  - reconciliation
  - bundle-by-owner
  - component-source-scope
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
actions: []
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
  with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.
```
