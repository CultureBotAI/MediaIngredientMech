# Per-record structured review: Kijanimicin (data/ingredients/mapped/Kijanimicin.yaml)

- Review: 20261017T083000Z-kijanimicin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Kijanimicin (data/ingredients/mapped/Kijanimicin.yaml, record-82fa279e85827b63, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Kijanimicin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Kijanimicin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-82fa279e85827b63 | data/ingredients/mapped/Kijanimicin.yaml | maintained | Kijanimicin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-82fa279e85827b63 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-82fa279e85827b63 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-82fa279e85827b63 | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-82fa279e85827b63.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-82fa279e85827b63.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:02:32Z; reviewed SHA-256=9ea82812bb3f0165e7cf8f74c66d00c9bbe3b4bb2756a617e8156da7e59edae1; current SHA-256=9ea82812bb3f0165e7cf8f74c66d00c9bbe3b4bb2756a617e8156da7e59edae1; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050232Z-Kijanimicin.md","reports/yaml_record_review/Kijanimicin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Kijanimicin.md&#96; after the record changed from 5d9e9ceb7aba870eebf32f97a85dc5a4594284ce37da5b105109339c93d1aff0 to 9ea82812bb3f0165e7cf8f74c66d00c9bbe3b4bb2756a617e8156da7e59edae1; preserved the previous major finding floor pending targeted retirement.

### Historical provisional-role concern

evidence: concern. Targets: record-82fa279e85827b63.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-782f2318c021cd5b: Reassess prediction-only role support: kijanimicin

major / open / confirmed; issue key: mim-reconciliation-role-support-82fa279e85827b63.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-782f2318c021cd5b

Reassess prediction-only role support: kijanimicin

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-dfdd6aef591d9c9b | data/ingredients/mapped/Kijanimicin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1206],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:220048","line":1208,"mapping_status":"MAPPED","ontology_id":"CHEBI:220048","preferred_term":"kijanimicin"}],"identifier":"CHEBI:220048","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:220048","ontology_label":"Kijanimicin","ontology_source":"CHEBI"},"preferred_term":"kijanimicin","sssom_rows":[{"data_row":1550,"object_id":"CHEBI:220048","object_label":"Kijanimicin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Kijanimicin","synonym_count":2} |
| ev-ac754b5eb5c96c16 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1206] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-9bc55ca4e1e2a3a3 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Kijanimicin; data-row positions=[1550] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1550,"object_id":"CHEBI:220048","object_label":"Kijanimicin","other":"methyl N-[(2R,3R,4S,6R)-6-[[(1S,3R,6S,7E,9S,11E,13S,16S,17S,18S,20S,21R,22S,23E)-17-[(2R,4R,5S,6S)-4-[(2S,6S)-4-[(2S,4S,5R,6S)-4,5-dihydroxy-6-methyloxan-2-yl]oxy-5-[(2R,4R,5R,6S)-4-hydroxy-5-methoxy-6-methyloxan-2-yl]oxy-6-methyloxan-2-yl]oxy-5-hydroxy-6-methyloxan-2-yl]oxy-23-hydroxy-4-(hydroxymethyl)-3,8,12,18,20,22-hexamethyl-25,27-dioxo-26-oxapentacyclo[22.2.1.01,6.013,22.016,21]heptacosa-4,7,11,14,23-pentaen-9-yl]oxy]-2,4-dimethyl-4-nitrooxan-3-yl]carbamate","predicate_id":"skos:exactMatch","subject_id":"MIM:Kijanimicin","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-cb2bb995c0a40a2d | docs/data/mapped_ingredients.csv; CSV lines=[1208] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:220048","line":1208,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:220048","preferred_term":"kijanimicin","total_occurrences":"0"}] |
| ev-e2c513c7b183713b | reports/yaml_record_review/20261001T050232Z-Kijanimicin.md; YAML Record Review: kijanimicin:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61; Additional Notes:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-3a45fb3dc3f75a5a | reports/yaml_record_review/Kijanimicin.md; &#96;data/ingredients/mapped/Kijanimicin.yaml&#96;:2; Verdict:4; Identity:11; Validation:21; Evidence:32; Completeness:52; Recommended Edits:60 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-7f0e9512ce70d6b5 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[777,1477] | context_only | [{"current_record_sha256":"9ea82812bb3f0165e7cf8f74c66d00c9bbe3b4bb2756a617e8156da7e59edae1","finding_id":"SEM:5f975e83de838de585c8","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"9ea82812bb3f0165e7cf8f74c66d00c9bbe3b4bb2756a617e8156da7e59edae1","finding_id":"SEM:cd5a2da8de5544e5034d","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-c0e2cddca9b821db | data/ingredients/mapped/Kijanimicin.yaml; physicochemical_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}] |
| ev-a673472f860873b6 | reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml; findings[finding_id=f-782f2318c021cd5b] | context_only | Predecessor structured review finding f-782f2318c021cd5b in 20261011T024635Z-mim-reconcile-all-batch-07 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-kijanimicin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Kijanimicin (data/ingredients/mapped/Kijanimicin.yaml)'
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
summary: Per-record structured review for Kijanimicin (data/ingredients/mapped/Kijanimicin.yaml,
  record-82fa279e85827b63, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Kijanimicin.yaml
    sha256: 9ea82812bb3f0165e7cf8f74c66d00c9bbe3b4bb2756a617e8156da7e59edae1
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
  - path: reports/yaml_record_review/20261001T050232Z-Kijanimicin.md
    sha256: c2d1a89d68723c01b6abca3fa4bee92bafd217d5d7bd680ab62448a32b817959
    role: context
  - path: reports/yaml_record_review/Kijanimicin.md
    sha256: ad7ac24da8610131b8900749e82cc556fdd37cf8181c9a3667d5b29463fdfc8a
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-82fa279e85827b63
  path: data/ingredients/mapped/Kijanimicin.yaml
  label: Kijanimicin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Kijanimicin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Kijanimicin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Kijanimicin.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-82fa279e85827b63
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-82fa279e85827b63
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-82fa279e85827b63
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-82fa279e85827b63
evidence:
- evidence_id: ev-dfdd6aef591d9c9b
  kind: record_content
  reference: data/ingredients/mapped/Kijanimicin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1206],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:220048","line":1208,"mapping_status":"MAPPED","ontology_id":"CHEBI:220048","preferred_term":"kijanimicin"}],"identifier":"CHEBI:220048","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:220048","ontology_label":"Kijanimicin","ontology_source":"CHEBI"},"preferred_term":"kijanimicin","sssom_rows":[{"data_row":1550,"object_id":"CHEBI:220048","object_label":"Kijanimicin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Kijanimicin","synonym_count":2}'
  snapshot_sha256: 9ea82812bb3f0165e7cf8f74c66d00c9bbe3b4bb2756a617e8156da7e59edae1
- evidence_id: ev-ac754b5eb5c96c16
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1206]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-9bc55ca4e1e2a3a3
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Kijanimicin; data-row positions=[1550]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1550,"object_id":"CHEBI:220048","object_label":"Kijanimicin","other":"methyl
    N-[(2R,3R,4S,6R)-6-[[(1S,3R,6S,7E,9S,11E,13S,16S,17S,18S,20S,21R,22S,23E)-17-[(2R,4R,5S,6S)-4-[(2S,6S)-4-[(2S,4S,5R,6S)-4,5-dihydroxy-6-methyloxan-2-yl]oxy-5-[(2R,4R,5R,6S)-4-hydroxy-5-methoxy-6-methyloxan-2-yl]oxy-6-methyloxan-2-yl]oxy-5-hydroxy-6-methyloxan-2-yl]oxy-23-hydroxy-4-(hydroxymethyl)-3,8,12,18,20,22-hexamethyl-25,27-dioxo-26-oxapentacyclo[22.2.1.01,6.013,22.016,21]heptacosa-4,7,11,14,23-pentaen-9-yl]oxy]-2,4-dimethyl-4-nitrooxan-3-yl]carbamate","predicate_id":"skos:exactMatch","subject_id":"MIM:Kijanimicin","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-cb2bb995c0a40a2d
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1208]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:220048","line":1208,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:220048","preferred_term":"kijanimicin","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-e2c513c7b183713b
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050232Z-Kijanimicin.md
  locator: 'YAML Record Review: kijanimicin:2; Target:10; Validation:20; Identity
    and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56;
    Follow-up Checks:61; Additional Notes:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: c2d1a89d68723c01b6abca3fa4bee92bafd217d5d7bd680ab62448a32b817959
  quote: 'Findings:

    - **major**: The previous finding set in `reports/yaml_record_review/Kijanimicin.md`
    was tied to the prior record content; carry it forward as an unresolved curation
    floor until a targeted current review retires it. Previous summary: The exact
    ChEBI kijanimicin identity, structure fields, and IUPAC synonym pass, but final
    SSSOM exports produces: kijanimicin and SELECTIVE_AGENT is only provisional name-pattern
    evidence.


    Recommended Edits:

    - Resolve or explicitly retire the findings provisionally carried forward from
    `reports/yaml_record_review/Kijanimicin.md`.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Kijanimicin.yaml`,
    `just validate-terms data/ingredients/mapped/Kijanimicin.yaml` where applicable,
    and `just qc-sssom`.'
- evidence_id: ev-3a45fb3dc3f75a5a
  kind: prior_review
  reference: reports/yaml_record_review/Kijanimicin.md
  locator: '`data/ingredients/mapped/Kijanimicin.yaml`:2; Verdict:4; Identity:11;
    Validation:21; Evidence:32; Completeness:52; Recommended Edits:60'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: ad7ac24da8610131b8900749e82cc556fdd37cf8181c9a3667d5b29463fdfc8a
  quote: "Recommended Edits:\n- Major: remove or demote `produces: kijanimicin` in\n\
    \  `data/ingredients/mapped/Kijanimicin.yaml`, then regenerate the aggregate and\n\
    \  final SSSOM so it disappears from `mappings/ingredient_mappings.sssom.tsv`.\n\
    - Major: remove `physicochemical_roles.SELECTIVE_AGENT` unless an inspected\n\
    \  kg-microbe, CultureMech, FEBA, Hans80, or literature source can support\n \
    \ kijanimicin as a selective agent.\n- Rerun strict, term, round-trip, component,\
    \ and SSSOM validation after those\n  changes."
- evidence_id: ev-7f0e9512ce70d6b5
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[777,1477]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"9ea82812bb3f0165e7cf8f74c66d00c9bbe3b4bb2756a617e8156da7e59edae1","finding_id":"SEM:5f975e83de838de585c8","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"9ea82812bb3f0165e7cf8f74c66d00c9bbe3b4bb2756a617e8156da7e59edae1","finding_id":"SEM:cd5a2da8de5544e5034d","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-c0e2cddca9b821db
  kind: record_content
  reference: data/ingredients/mapped/Kijanimicin.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}]'
  snapshot_sha256: 9ea82812bb3f0165e7cf8f74c66d00c9bbe3b4bb2756a617e8156da7e59edae1
- evidence_id: ev-a673472f860873b6
  kind: prior_review
  reference: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
  locator: findings[finding_id=f-782f2318c021cd5b]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-782f2318c021cd5b in 20261011T024635Z-mim-reconcile-all-batch-07
  snapshot_sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
assessments:
- assessment_id: a-fbe05f87ede0ba1e
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-82fa279e85827b63
  evidence_ids:
  - ev-dfdd6aef591d9c9b
  - ev-ac754b5eb5c96c16
  - ev-9bc55ca4e1e2a3a3
  - ev-cb2bb995c0a40a2d
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-42218baf2886d651
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-82fa279e85827b63
  evidence_ids:
  - ev-e2c513c7b183713b
  - ev-3a45fb3dc3f75a5a
  - ev-dfdd6aef591d9c9b
  - ev-7f0e9512ce70d6b5
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:02:32Z;
    reviewed SHA-256=9ea82812bb3f0165e7cf8f74c66d00c9bbe3b4bb2756a617e8156da7e59edae1;
    current SHA-256=9ea82812bb3f0165e7cf8f74c66d00c9bbe3b4bb2756a617e8156da7e59edae1;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050232Z-Kijanimicin.md","reports/yaml_record_review/Kijanimicin.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Kijanimicin.md` after the record changed from 5d9e9ceb7aba870eebf32f97a85dc5a4594284ce37da5b105109339c93d1aff0
    to 9ea82812bb3f0165e7cf8f74c66d00c9bbe3b4bb2756a617e8156da7e59edae1; preserved
    the previous major finding floor pending targeted retirement.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-e2c513c7b183713b
    - ev-3a45fb3dc3f75a5a
    - ev-dfdd6aef591d9c9b
  - name: legacy-native-ids
    value: '["SEM:5f975e83de838de585c8","SEM:cd5a2da8de5544e5034d"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-dfdd6aef591d9c9b
    - ev-e2c513c7b183713b
    - ev-3a45fb3dc3f75a5a
    - ev-7f0e9512ce70d6b5
- assessment_id: a-c0e2cddca9b821db
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-82fa279e85827b63
  evidence_ids:
  - ev-e2c513c7b183713b
  - ev-3a45fb3dc3f75a5a
  - ev-c0e2cddca9b821db
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-e2c513c7b183713b
    - ev-3a45fb3dc3f75a5a
    - ev-c0e2cddca9b821db
findings:
- finding_id: rec-f-782f2318c021cd5b
  issue_key: mim-reconciliation-role-support-82fa279e85827b63
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: kijanimicin'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-82fa279e85827b63
  evidence_ids:
  - ev-e2c513c7b183713b
  - ev-3a45fb3dc3f75a5a
  - ev-c0e2cddca9b821db
  - ev-a673472f860873b6
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Kijanimicin.yaml
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
    review_id: 20261011T024635Z-mim-reconcile-all-batch-07
    finding_id: f-782f2318c021cd5b
actions:
- action_id: rec-action-782f2318c021cd5b
  description: 'Reassess prediction-only role support: kijanimicin'
  finding_ids:
  - rec-f-782f2318c021cd5b
  target_ids:
  - record-82fa279e85827b63
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Kijanimicin.yaml
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
  with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.
```
