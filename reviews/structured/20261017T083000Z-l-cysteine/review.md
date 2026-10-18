# Per-record structured review: L-cysteine (data/ingredients/mapped/L-cysteine.yaml)

- Review: 20261017T083000Z-l-cysteine
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for L-cysteine (data/ingredients/mapped/L-cysteine.yaml, record-6a204d03729399c3, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/L-cysteine.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/L-cysteine.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-6a204d03729399c3 | data/ingredients/mapped/L-cysteine.yaml | maintained | L-cysteine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-6a204d03729399c3 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-6a204d03729399c3 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-6a204d03729399c3 | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-6a204d03729399c3.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-6a204d03729399c3.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:02:36Z; reviewed SHA-256=8c24e38f13a5574684dda7aae35813c6f417016f5ce47089070ccb607aed6e79; current SHA-256=8c24e38f13a5574684dda7aae35813c6f417016f5ce47089070ccb607aed6e79; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050236Z-L-cysteine.md","reports/yaml_record_review/L-cysteine.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/L-cysteine.md&#96; after the record changed from 86735cd67de758a5401fb051cb98ca3483104d4632c7ce2dcdff261ed38c0fc1 to 8c24e38f13a5574684dda7aae35813c6f417016f5ce47089070ccb607aed6e79; preserved the previous major finding floor pending targeted retirement.

## Findings

### rec-f-6c251b4fa0d446c6: Historical review coverage and residual narrative: L-cysteine

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-6a204d03729399c3.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:02:36Z; reviewed SHA-256=8c24e38f13a5574684dda7aae35813c6f417016f5ce47089070ccb607aed6e79; current SHA-256=8c24e38f13a5574684dda7aae35813c6f417016f5ce47089070ccb607aed6e79; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050236Z-L-cysteine.md","reports/yaml_record_review/L-cysteine.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/L-cysteine.md&#96; after the record changed from 86735cd67de758a5401fb051cb98ca3483104d4632c7ce2dcdff261ed38c0fc1 to 8c24e38f13a5574684dda7aae35813c6f417016f5ce47089070ccb607aed6e79; preserved the previous major finding floor pending targeted retirement.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-afcf65e0ca0dd7c5 | data/ingredients/mapped/L-cysteine.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1242],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17561","line":1244,"mapping_status":"MAPPED","ontology_id":"CHEBI:17561","preferred_term":"L-Cysteine"}],"identifier":"CHEBI:17561","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":128,"edge_count":128,"occurrences":129},"occurrence_statistics":{"media_count":128,"total_occurrences":129},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17561","ontology_label":"L-cysteine","ontology_source":"CHEBI"},"preferred_term":"L-Cysteine","sssom_rows":[{"data_row":1606,"object_id":"CHEBI:17561","object_label":"L-cysteine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-cysteine","synonym_count":21} |
| ev-600bc841627ed70a | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1242] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-9eef84f305091015 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:L-cysteine; data-row positions=[1606] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1606,"object_id":"CHEBI:17561","object_label":"L-cysteine","other":"(2R)-2-amino-3-mercaptopropanoic acid&#124;(2R)-2-amino-3-sulfanylpropanoic acid&#124;(2R)-2-ammonio-3-mercaptopropanoate&#124;(2R)-2-ammonio-3-sulfanylpropanoate&#124;(R)-2-amino-3-mercaptopropanoic acid&#124;E 920&#124;E-920&#124;E920&#124;FREE CYSTEINE&#124;L-2-Amino-3-mercaptopropionic acid&#124;L-Cystein&#124;L-Zystein&#124;CYSTEINE&#124;L-cysteine (Sigma)&#124;CAS:52-90-4","predicate_id":"skos:exactMatch","subject_id":"MIM:L-cysteine","validation_method":"manual:apply_669_704_rulings&#124;IDENTITY&#124;2026-09-24"}] |
| ev-9dc4a7f820b9b11b | docs/data/mapped_ingredients.csv; CSV lines=[1244] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:17561","line":1244,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"128","ontology_id":"CHEBI:17561","preferred_term":"L-Cysteine","total_occurrences":"129"}] |
| ev-c67f5b661bda4e71 | reports/yaml_record_review/20261001T050236Z-L-cysteine.md; YAML Record Review: L-Cysteine:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61; Additional Notes:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-cf3da6352be84ff5 | reports/yaml_record_review/L-cysteine.md; &#96;data/ingredients/mapped/L-cysteine.yaml&#96;:2; Verdict:4; Identity:11; Validation:21; Evidence:27; Completeness:48; Recommended Edits:56 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-47ea55c55f42efad | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[810] | context_only | [{"current_record_sha256":"8c24e38f13a5574684dda7aae35813c6f417016f5ce47089070ccb607aed6e79","finding_id":"SEM:69c78f15adaa6af1c4c8","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-l-cysteine
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: L-cysteine (data/ingredients/mapped/L-cysteine.yaml)'
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
summary: Per-record structured review for L-cysteine (data/ingredients/mapped/L-cysteine.yaml,
  record-6a204d03729399c3, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/L-cysteine.yaml
    sha256: 8c24e38f13a5574684dda7aae35813c6f417016f5ce47089070ccb607aed6e79
    role: target
  - path: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
    sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
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
  - path: reports/yaml_record_review/20261001T050236Z-L-cysteine.md
    sha256: e3b15fb03cd6ed4065f0d9523013acc5c9d971a06232fbb07f43107f41afd71b
    role: context
  - path: reports/yaml_record_review/L-cysteine.md
    sha256: 90d241b4642df2428104485294cd4006700ce4da94f2c17c5c8403f3a624367a
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-6a204d03729399c3
  path: data/ingredients/mapped/L-cysteine.yaml
  label: L-cysteine
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-cysteine.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/L-cysteine.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/L-cysteine.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-6a204d03729399c3
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-6a204d03729399c3
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-6a204d03729399c3
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-6a204d03729399c3
evidence:
- evidence_id: ev-afcf65e0ca0dd7c5
  kind: record_content
  reference: data/ingredients/mapped/L-cysteine.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1242],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17561","line":1244,"mapping_status":"MAPPED","ontology_id":"CHEBI:17561","preferred_term":"L-Cysteine"}],"identifier":"CHEBI:17561","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":128,"edge_count":128,"occurrences":129},"occurrence_statistics":{"media_count":128,"total_occurrences":129},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17561","ontology_label":"L-cysteine","ontology_source":"CHEBI"},"preferred_term":"L-Cysteine","sssom_rows":[{"data_row":1606,"object_id":"CHEBI:17561","object_label":"L-cysteine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-cysteine","synonym_count":21}'
  snapshot_sha256: 8c24e38f13a5574684dda7aae35813c6f417016f5ce47089070ccb607aed6e79
- evidence_id: ev-600bc841627ed70a
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1242]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-9eef84f305091015
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:L-cysteine; data-row positions=[1606]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1606,"object_id":"CHEBI:17561","object_label":"L-cysteine","other":"(2R)-2-amino-3-mercaptopropanoic
    acid|(2R)-2-amino-3-sulfanylpropanoic acid|(2R)-2-ammonio-3-mercaptopropanoate|(2R)-2-ammonio-3-sulfanylpropanoate|(R)-2-amino-3-mercaptopropanoic
    acid|E 920|E-920|E920|FREE CYSTEINE|L-2-Amino-3-mercaptopropionic acid|L-Cystein|L-Zystein|CYSTEINE|L-cysteine
    (Sigma)|CAS:52-90-4","predicate_id":"skos:exactMatch","subject_id":"MIM:L-cysteine","validation_method":"manual:apply_669_704_rulings|IDENTITY|2026-09-24"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-9dc4a7f820b9b11b
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1244]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:17561","line":1244,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"128","ontology_id":"CHEBI:17561","preferred_term":"L-Cysteine","total_occurrences":"129"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-c67f5b661bda4e71
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050236Z-L-cysteine.md
  locator: 'YAML Record Review: L-Cysteine:2; Target:10; Validation:20; Identity and
    Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56;
    Follow-up Checks:61; Additional Notes:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: e3b15fb03cd6ed4065f0d9523013acc5c9d971a06232fbb07f43107f41afd71b
  quote: 'Findings:

    - **major**: The previous finding set in `reports/yaml_record_review/L-cysteine.md`
    was tied to the prior record content; carry it forward as an unresolved curation
    floor until a targeted current review retires it. Previous summary: The exact
    CHEBI:17561 identity, CAS value, PubChem structure, nitrogen-source role, and
    filtered rejected hydrate label pass, but final SSSOM still exports the distinct
    zwitterion label.


    Recommended Edits:

    - Resolve or explicitly retire the findings provisionally carried forward from
    `reports/yaml_record_review/L-cysteine.md`.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/L-cysteine.yaml`,
    `just validate-terms data/ingredients/mapped/L-cysteine.yaml` where applicable,
    and `just qc-sssom`.'
- evidence_id: ev-cf3da6352be84ff5
  kind: prior_review
  reference: reports/yaml_record_review/L-cysteine.md
  locator: '`data/ingredients/mapped/L-cysteine.yaml`:2; Verdict:4; Identity:11; Validation:21;
    Evidence:27; Completeness:48; Recommended Edits:56'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 90d241b4642df2428104485294cd4006700ce4da94f2c17c5c8403f3a624367a
  quote: "Recommended Edits:\n- Major: remove `L-cysteine zwitterion` from\n  `data/ingredients/mapped/L-cysteine.yaml`;\
    \ keep that label only on\n  `data/ingredients/mapped/L-cysteine_Zwitterion.yaml`.\n\
    - Sync the aggregate copy and regenerate the SSSOM/docs products so `other`\n\
    \  stops publishing the cross-identity zwitterion synonym; rerun strict, term,\n\
    \  round-trip, component, and SSSOM validation."
- evidence_id: ev-47ea55c55f42efad
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[810]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"8c24e38f13a5574684dda7aae35813c6f417016f5ce47089070ccb607aed6e79","finding_id":"SEM:69c78f15adaa6af1c4c8","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-ee7ea8866184b580
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-6a204d03729399c3
  evidence_ids:
  - ev-afcf65e0ca0dd7c5
  - ev-600bc841627ed70a
  - ev-9eef84f305091015
  - ev-9dc4a7f820b9b11b
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-a2faf026c9207050
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-6a204d03729399c3
  evidence_ids:
  - ev-c67f5b661bda4e71
  - ev-cf3da6352be84ff5
  - ev-afcf65e0ca0dd7c5
  - ev-47ea55c55f42efad
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:02:36Z;
    reviewed SHA-256=8c24e38f13a5574684dda7aae35813c6f417016f5ce47089070ccb607aed6e79;
    current SHA-256=8c24e38f13a5574684dda7aae35813c6f417016f5ce47089070ccb607aed6e79;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050236Z-L-cysteine.md","reports/yaml_record_review/L-cysteine.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/L-cysteine.md` after the record changed from 86735cd67de758a5401fb051cb98ca3483104d4632c7ce2dcdff261ed38c0fc1
    to 8c24e38f13a5574684dda7aae35813c6f417016f5ce47089070ccb607aed6e79; preserved
    the previous major finding floor pending targeted retirement.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-c67f5b661bda4e71
    - ev-cf3da6352be84ff5
    - ev-afcf65e0ca0dd7c5
  - name: legacy-native-ids
    value: '["SEM:69c78f15adaa6af1c4c8"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-afcf65e0ca0dd7c5
    - ev-c67f5b661bda4e71
    - ev-cf3da6352be84ff5
    - ev-47ea55c55f42efad
findings:
- finding_id: rec-f-6c251b4fa0d446c6
  issue_key: mim-reconciliation-historical-review-coverage-and-r-6a204d03729399c3
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: L-cysteine'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:02:36Z;
    reviewed SHA-256=8c24e38f13a5574684dda7aae35813c6f417016f5ce47089070ccb607aed6e79;
    current SHA-256=8c24e38f13a5574684dda7aae35813c6f417016f5ce47089070ccb607aed6e79;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050236Z-L-cysteine.md","reports/yaml_record_review/L-cysteine.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/L-cysteine.md` after the record changed from 86735cd67de758a5401fb051cb98ca3483104d4632c7ce2dcdff261ed38c0fc1
    to 8c24e38f13a5574684dda7aae35813c6f417016f5ce47089070ccb607aed6e79; preserved
    the previous major finding floor pending targeted retirement.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-6a204d03729399c3
  evidence_ids:
  - ev-c67f5b661bda4e71
  - ev-cf3da6352be84ff5
  - ev-afcf65e0ca0dd7c5
  - ev-47ea55c55f42efad
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-cysteine.yaml
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
  with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.
```
