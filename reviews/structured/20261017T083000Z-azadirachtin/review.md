# Per-record structured review: Azadirachtin (data/ingredients/mapped/Azadirachtin.yaml)

- Review: 20261017T083000Z-azadirachtin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Azadirachtin (data/ingredients/mapped/Azadirachtin.yaml, record-9b65bbb3049649ec, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Azadirachtin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Azadirachtin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-9b65bbb3049649ec | data/ingredients/mapped/Azadirachtin.yaml | maintained | Azadirachtin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-9b65bbb3049649ec | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-9b65bbb3049649ec | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-9b65bbb3049649ec | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-9b65bbb3049649ec.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-9b65bbb3049649ec.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T09:06:25Z; reviewed SHA-256=ad7624c4f8d824c23c78afe92115f3622ff3a93655d0604b674e3890b2773b0b; current SHA-256=ad7624c4f8d824c23c78afe92115f3622ff3a93655d0604b674e3890b2773b0b; hash_changed=False. Reports=["reports/yaml_record_review/Azadirachtin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact generic CHEBI azadirachtin-family mapping passes, but CAS 11141-17-6 is form-specific and does not belong on the generic CHEBI:38473 record without a re-grounding decision.

## Findings

### rec-f-c0c69b49dea2b131: Historical review coverage and residual narrative: Azadirachtin

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-9b65bbb3049649ec.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T09:06:25Z; reviewed SHA-256=ad7624c4f8d824c23c78afe92115f3622ff3a93655d0604b674e3890b2773b0b; current SHA-256=ad7624c4f8d824c23c78afe92115f3622ff3a93655d0604b674e3890b2773b0b; hash_changed=False. Reports=["reports/yaml_record_review/Azadirachtin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact generic CHEBI azadirachtin-family mapping passes, but CAS 11141-17-6 is form-specific and does not belong on the generic CHEBI:38473 record without a re-grounding decision.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-440c2b038e0a76ae | data/ingredients/mapped/Azadirachtin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[535],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:38473","line":537,"mapping_status":"MAPPED","ontology_id":"CHEBI:38473","preferred_term":"Azadirachtin"}],"identifier":"CHEBI:38473","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:38473","ontology_label":"azadirachtin","ontology_source":"CHEBI"},"preferred_term":"Azadirachtin","sssom_rows":[{"data_row":459,"object_id":"CHEBI:38473","object_label":"azadirachtin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Azadirachtin","synonym_count":0} |
| ev-106c4c5fd8a10804 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [535] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-35fce40374164227 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Azadirachtin; data-row positions=[459] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":459,"object_id":"CHEBI:38473","object_label":"azadirachtin","other":"CAS:11141-17-6","predicate_id":"skos:exactMatch","subject_id":"MIM:Azadirachtin","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-26b97eb4fccb3918 | docs/data/mapped_ingredients.csv; CSV lines=[537] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:38473","line":537,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:38473","preferred_term":"Azadirachtin","total_occurrences":"0"}] |
| ev-5b36fa6077179478 | reports/yaml_record_review/Azadirachtin.md; &#96;data/ingredients/mapped/Azadirachtin.yaml&#96;:2; Verdict:4; Identity:12; Validation:26; Evidence:41; Completeness:56; Recommended Edits:66 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-5d2ee7005bf7ca5f | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[285] | context_only | [{"current_record_sha256":"ad7624c4f8d824c23c78afe92115f3622ff3a93655d0604b674e3890b2773b0b","finding_id":"SEM:eb3a5c818ee47b2718bb","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-azadirachtin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Azadirachtin (data/ingredients/mapped/Azadirachtin.yaml)'
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
summary: Per-record structured review for Azadirachtin (data/ingredients/mapped/Azadirachtin.yaml,
  record-9b65bbb3049649ec, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Azadirachtin.yaml
    sha256: ad7624c4f8d824c23c78afe92115f3622ff3a93655d0604b674e3890b2773b0b
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
  - path: reports/yaml_record_review/Azadirachtin.md
    sha256: 3f172e4329fed1693cc732c17a11a7b6ec1b8972bce3dd953ea3baf6a2cc2adc
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-9b65bbb3049649ec
  path: data/ingredients/mapped/Azadirachtin.yaml
  label: Azadirachtin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Azadirachtin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Azadirachtin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Azadirachtin.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-9b65bbb3049649ec
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-9b65bbb3049649ec
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-9b65bbb3049649ec
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-9b65bbb3049649ec
evidence:
- evidence_id: ev-440c2b038e0a76ae
  kind: record_content
  reference: data/ingredients/mapped/Azadirachtin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[535],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:38473","line":537,"mapping_status":"MAPPED","ontology_id":"CHEBI:38473","preferred_term":"Azadirachtin"}],"identifier":"CHEBI:38473","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:38473","ontology_label":"azadirachtin","ontology_source":"CHEBI"},"preferred_term":"Azadirachtin","sssom_rows":[{"data_row":459,"object_id":"CHEBI:38473","object_label":"azadirachtin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Azadirachtin","synonym_count":0}'
  snapshot_sha256: ad7624c4f8d824c23c78afe92115f3622ff3a93655d0604b674e3890b2773b0b
- evidence_id: ev-106c4c5fd8a10804
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [535]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-35fce40374164227
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Azadirachtin; data-row positions=[459]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":459,"object_id":"CHEBI:38473","object_label":"azadirachtin","other":"CAS:11141-17-6","predicate_id":"skos:exactMatch","subject_id":"MIM:Azadirachtin","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-26b97eb4fccb3918
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[537]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:38473","line":537,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:38473","preferred_term":"Azadirachtin","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-5b36fa6077179478
  kind: prior_review
  reference: reports/yaml_record_review/Azadirachtin.md
  locator: '`data/ingredients/mapped/Azadirachtin.yaml`:2; Verdict:4; Identity:12;
    Validation:26; Evidence:41; Completeness:56; Recommended Edits:66'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 3f172e4329fed1693cc732c17a11a7b6ec1b8972bce3dd953ea3baf6a2cc2adc
  quote: "Recommended Edits:\n- Re-curate `data/ingredients/mapped/Azadirachtin.yaml`\
    \ from the original\n  CultureBotHT `Azadirachtin` + `11141-17-6` source row.\
    \ If the CAS identifies\n  a form-specific external term, re-ground the record\
    \ to that exact term and\n  synchronize `data/curated/mapped_ingredients.yaml`\
    \ plus\n  `mappings/ingredient_mappings.sssom.tsv`; if not, keep `CHEBI:38473`\
    \ as the\n  family record but remove `chemical_properties.cas_rn` and the SSSOM\n\
    \  `CAS:11141-17-6` assertion from this generic identity.\n- Rerun focused strict\
    \ and term validation, SSSOM invariants, product\n  id/label correspondence, and\
    \ flat-export coverage after the maintained\n  curation surfaces are synchronized."
- evidence_id: ev-5d2ee7005bf7ca5f
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[285]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"ad7624c4f8d824c23c78afe92115f3622ff3a93655d0604b674e3890b2773b0b","finding_id":"SEM:eb3a5c818ee47b2718bb","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-bd9200dec93fa3d7
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-9b65bbb3049649ec
  evidence_ids:
  - ev-440c2b038e0a76ae
  - ev-106c4c5fd8a10804
  - ev-35fce40374164227
  - ev-26b97eb4fccb3918
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-bd02d8da41ebb520
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-9b65bbb3049649ec
  evidence_ids:
  - ev-5b36fa6077179478
  - ev-440c2b038e0a76ae
  - ev-5d2ee7005bf7ca5f
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T09:06:25Z;
    reviewed SHA-256=ad7624c4f8d824c23c78afe92115f3622ff3a93655d0604b674e3890b2773b0b;
    current SHA-256=ad7624c4f8d824c23c78afe92115f3622ff3a93655d0604b674e3890b2773b0b;
    hash_changed=False. Reports=["reports/yaml_record_review/Azadirachtin.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact generic
    CHEBI azadirachtin-family mapping passes, but CAS 11141-17-6 is form-specific
    and does not belong on the generic CHEBI:38473 record without a re-grounding decision.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-5b36fa6077179478
    - ev-440c2b038e0a76ae
  - name: legacy-native-ids
    value: '["SEM:eb3a5c818ee47b2718bb"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-440c2b038e0a76ae
    - ev-5b36fa6077179478
    - ev-5d2ee7005bf7ca5f
findings:
- finding_id: rec-f-c0c69b49dea2b131
  issue_key: mim-reconciliation-historical-review-coverage-and-r-9b65bbb3049649ec
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Azadirachtin'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T09:06:25Z;
    reviewed SHA-256=ad7624c4f8d824c23c78afe92115f3622ff3a93655d0604b674e3890b2773b0b;
    current SHA-256=ad7624c4f8d824c23c78afe92115f3622ff3a93655d0604b674e3890b2773b0b;
    hash_changed=False. Reports=["reports/yaml_record_review/Azadirachtin.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact generic
    CHEBI azadirachtin-family mapping passes, but CAS 11141-17-6 is form-specific
    and does not belong on the generic CHEBI:38473 record without a re-grounding decision.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-9b65bbb3049649ec
  evidence_ids:
  - ev-5b36fa6077179478
  - ev-440c2b038e0a76ae
  - ev-5d2ee7005bf7ca5f
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Azadirachtin.yaml
    role: maintained ingredient
  field_paths:
  - curation_history
  tags:
  - reconciliation
  - bundle-by-owner
  - historical-review-coverage-and-r
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
  with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.
```
