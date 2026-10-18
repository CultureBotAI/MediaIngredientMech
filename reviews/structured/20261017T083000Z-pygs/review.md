# Per-record structured review: PYGS (data/ingredients/mapped/PYGS.yaml)

- Review: 20261017T083000Z-pygs
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for PYGS (data/ingredients/mapped/PYGS.yaml, record-944c90268f7b375b, mapping_status=MAPPED). Records 0 open finding(s) and 2 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/PYGS.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/PYGS.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-944c90268f7b375b | data/ingredients/mapped/PYGS.yaml | maintained | PYGS |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-944c90268f7b375b | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-944c90268f7b375b | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-944c90268f7b375b | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-944c90268f7b375b.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-944c90268f7b375b.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T08:24:27Z; reviewed SHA-256=b5d43cabed7ee976f44bb5bbc6a3f0ecc127c9bb6097c36c9b5e7ba433aa6f52; current SHA-256=b5d43cabed7ee976f44bb5bbc6a3f0ecc127c9bb6097c36c9b5e7ba433aa6f52; hash_changed=False. Reports=["reports/yaml_record_review/PYGS.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local PYGS identity passes, but the starch component overstates an ambiguous S suffix.

## Findings

### rec-f-1ea57eee68241564: Reassess component source scope: PYGS

major / deferred / provisional; issue key: mim-semantic-component-source-scope-944c90268f7b375b.

Expansion/interpretation is retained as an assertion, but the exact source preparation must be verified before semantic approval. UNKNOWN/PARTIAL completeness is not proof of membership. (Historical finding remains unresolved; no blanket approval.). Affected unit(s): MIM.assertion:1ad8beb3f45e7a2a4358563a0921bba3c1970044333598ca52461c55e399d817, MIM.assertion:252d4f73506272766c798ae7a00d90b218c91d1c0aecf90411b8bd777a30e62d, MIM.assertion:7d02e7d878b16fe16584c3ecdb877df5ba3a642fc3fffe45da5694c56b6fe7c0, MIM.assertion:ec07c272947abaa73a3c585af7fa4c95af90dbc063e9f5b0e13f27457b07cca9.

Disposition: Expansion/interpretation is retained as an assertion, but the exact source preparation must be verified before semantic approval. UNKNOWN/PARTIAL completeness is not proof of membership. (Historical finding remains unresolved; no blanket approval.). Affected unit(s): MIM.assertion:1ad8beb3f45e7a2a4358563a0921bba3c1970044333598ca52461c55e399d817, MIM.assertion:252d4f73506272766c798ae7a00d90b218c91d1c0aecf90411b8bd777a30e62d, MIM.assertion:7d02e7d878b16fe16584c3ecdb877df5ba3a642fc3fffe45da5694c56b6fe7c0, MIM.assertion:ec07c272947abaa73a3c585af7fa4c95af90dbc063e9f5b0e13f27457b07cca9.

### rec-f-8c2aaaf16e546640: Reassess ambiguous abbreviation: PYGS

major / deferred / provisional; issue key: mim-semantic-ambiguous-abbreviation-944c90268f7b375b.

The cited expansion acknowledges that S can mean salts or soluble starch; a definite component choice requires the original recipe context. (Historical finding remains unresolved; no blanket approval.). Affected unit(s): components.

Disposition: The cited expansion acknowledges that S can mean salts or soluble starch; a definite component choice requires the original recipe context. (Historical finding remains unresolved; no blanket approval.). Affected unit(s): components.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-a0f38167634eadb4 | data/ingredients/mapped/PYGS.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[56],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:pygs","line":58,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:pygs","preferred_term":"PYGS"}],"identifier":"kgmicrobe.ingredient:pygs","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:pygs","ontology_label":"PYGS","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"PYGS","sssom_rows":[{"data_row":2185,"object_id":"kgmicrobe.ingredient:pygs","object_label":"PYGS","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:PYGS","synonym_count":1} |
| ev-41e3a492798f594c | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [56] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-ce1969eb362197cc | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:PYGS; data-row positions=[2185] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2185,"object_id":"kgmicrobe.ingredient:pygs","object_label":"PYGS","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:PYGS","validation_method":"manual:move_mapped_out_of_unmapped_collection&#124;MOVED&#124;2026-08-15"}] |
| ev-16ee26de41704479 | docs/data/mapped_ingredients.csv; CSV lines=[58] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:pygs","line":58,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.ingredient:pygs","preferred_term":"PYGS","total_occurrences":"0"}] |
| ev-52d20a20088c66ad | reports/yaml_record_review/PYGS.md; &#96;data/ingredients/mapped/PYGS.yaml&#96;:2; Verdict:4; Identity:10; Validation:20; Evidence:30; Completeness:45; Recommended Edits:52 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-afdf65ca5f479504 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1091,1463,1497,1722,2054,2107] | context_only | [{"current_record_sha256":"b5d43cabed7ee976f44bb5bbc6a3f0ecc127c9bb6097c36c9b5e7ba433aa6f52","finding_id":"SEM:74aaa6e967e4895eab9b","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"b5d43cabed7ee976f44bb5bbc6a3f0ecc127c9bb6097c36c9b5e7ba433aa6f52","finding_id":"SEM:1e048edc602977bf2936","kind":"component_source_scope","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"b5d43cabed7ee976f44bb5bbc6a3f0ecc127c9bb6097c36c9b5e7ba433aa6f52","finding_id":"SEM:eb5b855741a3ae3bfba7","kind":"component_source_scope","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"b5d43cabed7ee976f44bb5bbc6a3f0ecc127c9bb6097c36c9b5e7ba433aa6f52","finding_id":"SEM:7cb86e75df178a5e5f81","kind":"component_source_scope","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"b5d43cabed7ee976f44bb5bbc6a3f0ecc127c9bb6097c36c9b5e7ba433aa6f52","finding_id":"SEM:8abe61f817d4ff766b20","kind":"component_source_scope","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"b5d43cabed7ee976f44bb5bbc6a3f0ecc127c9bb6097c36c9b5e7ba433aa6f52","finding_id":"SEM:c79b63fe97bcfe167306","kind":"ambiguous_abbreviation","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-pygs
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: PYGS (data/ingredients/mapped/PYGS.yaml)'
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
native_verdict: mapping_status=MAPPED; open=0; deferred=2
scientific_review: false
summary: Per-record structured review for PYGS (data/ingredients/mapped/PYGS.yaml,
  record-944c90268f7b375b, mapping_status=MAPPED). Records 0 open finding(s) and 2
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/PYGS.yaml
    sha256: b5d43cabed7ee976f44bb5bbc6a3f0ecc127c9bb6097c36c9b5e7ba433aa6f52
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
  - path: reports/yaml_record_review/PYGS.md
    sha256: 7f1cbd514b6916c6cc40f901f0104ca8f446cccc1aa877b69a0c162d1f29ec5e
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-944c90268f7b375b
  path: data/ingredients/mapped/PYGS.yaml
  label: PYGS
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/PYGS.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/PYGS.yaml covering
    current record state, role evidence support, published surfaces, and residual
    historical review claims.
  selection: Single record data/ingredients/mapped/PYGS.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-944c90268f7b375b
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-944c90268f7b375b
  evidence_ids:
  - ev-a0f38167634eadb4
  - ev-41e3a492798f594c
  - ev-ce1969eb362197cc
  - ev-16ee26de41704479
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-944c90268f7b375b
  evidence_ids:
  - ev-a0f38167634eadb4
  - ev-afdf65ca5f479504
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-944c90268f7b375b
  evidence_ids:
  - ev-52d20a20088c66ad
  - ev-afdf65ca5f479504
evidence:
- evidence_id: ev-a0f38167634eadb4
  kind: record_content
  reference: data/ingredients/mapped/PYGS.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[56],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:pygs","line":58,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:pygs","preferred_term":"PYGS"}],"identifier":"kgmicrobe.ingredient:pygs","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:pygs","ontology_label":"PYGS","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"PYGS","sssom_rows":[{"data_row":2185,"object_id":"kgmicrobe.ingredient:pygs","object_label":"PYGS","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:PYGS","synonym_count":1}'
  snapshot_sha256: b5d43cabed7ee976f44bb5bbc6a3f0ecc127c9bb6097c36c9b5e7ba433aa6f52
- evidence_id: ev-41e3a492798f594c
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [56]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-ce1969eb362197cc
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:PYGS; data-row positions=[2185]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2185,"object_id":"kgmicrobe.ingredient:pygs","object_label":"PYGS","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:PYGS","validation_method":"manual:move_mapped_out_of_unmapped_collection|MOVED|2026-08-15"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-16ee26de41704479
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[58]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:pygs","line":58,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.ingredient:pygs","preferred_term":"PYGS","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-52d20a20088c66ad
  kind: prior_review
  reference: reports/yaml_record_review/PYGS.md
  locator: '`data/ingredients/mapped/PYGS.yaml`:2; Verdict:4; Identity:10; Validation:20;
    Evidence:30; Completeness:45; Recommended Edits:52'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 7f1cbd514b6916c6cc40f901f0104ca8f446cccc1aa877b69a0c162d1f29ec5e
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/PYGS.yaml`, either\
    \ replace the starch\n  component with a representation of the unresolved mineral-salts-versus-starch\n\
    \  ambiguity, or split the source labels if MicrobeDecoder has enough context\
    \ to\n  distinguish the two `PYGS` formulations. Keep\n  `mappings/microbedecoder_residual_research_decomposition.tsv`\
    \ synchronized\n  with the decision and rerun `scripts/validate_component_partonomy.py`."
- evidence_id: ev-afdf65ca5f479504
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1091,1463,1497,1722,2054,2107]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"b5d43cabed7ee976f44bb5bbc6a3f0ecc127c9bb6097c36c9b5e7ba433aa6f52","finding_id":"SEM:74aaa6e967e4895eab9b","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"b5d43cabed7ee976f44bb5bbc6a3f0ecc127c9bb6097c36c9b5e7ba433aa6f52","finding_id":"SEM:1e048edc602977bf2936","kind":"component_source_scope","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"b5d43cabed7ee976f44bb5bbc6a3f0ecc127c9bb6097c36c9b5e7ba433aa6f52","finding_id":"SEM:eb5b855741a3ae3bfba7","kind":"component_source_scope","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"b5d43cabed7ee976f44bb5bbc6a3f0ecc127c9bb6097c36c9b5e7ba433aa6f52","finding_id":"SEM:7cb86e75df178a5e5f81","kind":"component_source_scope","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"b5d43cabed7ee976f44bb5bbc6a3f0ecc127c9bb6097c36c9b5e7ba433aa6f52","finding_id":"SEM:8abe61f817d4ff766b20","kind":"component_source_scope","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"b5d43cabed7ee976f44bb5bbc6a3f0ecc127c9bb6097c36c9b5e7ba433aa6f52","finding_id":"SEM:c79b63fe97bcfe167306","kind":"ambiguous_abbreviation","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-f195e2c97090c067
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-944c90268f7b375b
  evidence_ids:
  - ev-a0f38167634eadb4
  - ev-41e3a492798f594c
  - ev-ce1969eb362197cc
  - ev-16ee26de41704479
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-8a3c6d524b37ce4a
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-944c90268f7b375b
  evidence_ids:
  - ev-52d20a20088c66ad
  - ev-a0f38167634eadb4
  - ev-afdf65ca5f479504
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T08:24:27Z;
    reviewed SHA-256=b5d43cabed7ee976f44bb5bbc6a3f0ecc127c9bb6097c36c9b5e7ba433aa6f52;
    current SHA-256=b5d43cabed7ee976f44bb5bbc6a3f0ecc127c9bb6097c36c9b5e7ba433aa6f52;
    hash_changed=False. Reports=["reports/yaml_record_review/PYGS.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The local PYGS identity
    passes, but the starch component overstates an ambiguous S suffix.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-52d20a20088c66ad
    - ev-a0f38167634eadb4
  - name: legacy-native-ids
    value: '["SEM:74aaa6e967e4895eab9b","SEM:1e048edc602977bf2936","SEM:eb5b855741a3ae3bfba7","SEM:7cb86e75df178a5e5f81","SEM:8abe61f817d4ff766b20","SEM:c79b63fe97bcfe167306"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-a0f38167634eadb4
    - ev-52d20a20088c66ad
    - ev-afdf65ca5f479504
findings:
- finding_id: rec-f-1ea57eee68241564
  issue_key: mim-semantic-component-source-scope-944c90268f7b375b
  category: representation
  severity: major
  status: deferred
  certainty: provisional
  title: 'Reassess component source scope: PYGS'
  description: 'Expansion/interpretation is retained as an assertion, but the exact
    source preparation must be verified before semantic approval. UNKNOWN/PARTIAL
    completeness is not proof of membership. (Historical finding remains unresolved;
    no blanket approval.). Affected unit(s): MIM.assertion:1ad8beb3f45e7a2a4358563a0921bba3c1970044333598ca52461c55e399d817,
    MIM.assertion:252d4f73506272766c798ae7a00d90b218c91d1c0aecf90411b8bd777a30e62d,
    MIM.assertion:7d02e7d878b16fe16584c3ecdb877df5ba3a642fc3fffe45da5694c56b6fe7c0,
    MIM.assertion:ec07c272947abaa73a3c585af7fa4c95af90dbc063e9f5b0e13f27457b07cca9.'
  disposition_reason: 'Expansion/interpretation is retained as an assertion, but the
    exact source preparation must be verified before semantic approval. UNKNOWN/PARTIAL
    completeness is not proof of membership. (Historical finding remains unresolved;
    no blanket approval.). Affected unit(s): MIM.assertion:1ad8beb3f45e7a2a4358563a0921bba3c1970044333598ca52461c55e399d817,
    MIM.assertion:252d4f73506272766c798ae7a00d90b218c91d1c0aecf90411b8bd777a30e62d,
    MIM.assertion:7d02e7d878b16fe16584c3ecdb877df5ba3a642fc3fffe45da5694c56b6fe7c0,
    MIM.assertion:ec07c272947abaa73a3c585af7fa4c95af90dbc063e9f5b0e13f27457b07cca9.'
  target_ids:
  - record-944c90268f7b375b
  evidence_ids:
  - ev-a0f38167634eadb4
  - ev-afdf65ca5f479504
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/PYGS.yaml
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
- finding_id: rec-f-8c2aaaf16e546640
  issue_key: mim-semantic-ambiguous-abbreviation-944c90268f7b375b
  category: identity
  severity: major
  status: deferred
  certainty: provisional
  title: 'Reassess ambiguous abbreviation: PYGS'
  description: 'The cited expansion acknowledges that S can mean salts or soluble
    starch; a definite component choice requires the original recipe context. (Historical
    finding remains unresolved; no blanket approval.). Affected unit(s): components.'
  disposition_reason: 'The cited expansion acknowledges that S can mean salts or soluble
    starch; a definite component choice requires the original recipe context. (Historical
    finding remains unresolved; no blanket approval.). Affected unit(s): components.'
  target_ids:
  - record-944c90268f7b375b
  evidence_ids:
  - ev-a0f38167634eadb4
  - ev-afdf65ca5f479504
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/PYGS.yaml
    role: maintained ingredient
  field_paths:
  - preferred_term
  - mapping_status
  - ontology_id
  tags:
  - reconciliation
  - bundle-by-owner
  - ambiguous-abbreviation
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
