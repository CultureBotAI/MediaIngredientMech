# Per-record structured review: Tobramycin_Sulfate_Salt (data/ingredients/mapped/Tobramycin_Sulfate_Salt.yaml)

- Review: 20261017T083000Z-tobramycin-sulfate-salt
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Tobramycin_Sulfate_Salt (data/ingredients/mapped/Tobramycin_Sulfate_Salt.yaml, record-f6b3c6190dc90db3, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Tobramycin_Sulfate_Salt.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Tobramycin_Sulfate_Salt.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-f6b3c6190dc90db3 | data/ingredients/mapped/Tobramycin_Sulfate_Salt.yaml | maintained | Tobramycin_Sulfate_Salt |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-f6b3c6190dc90db3 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-f6b3c6190dc90db3 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-f6b3c6190dc90db3 | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-f6b3c6190dc90db3.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-f6b3c6190dc90db3.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T19:04:22Z; reviewed SHA-256=083a5b4efa6055f37c630bec23b31a5b1ec52bf018132f98a64c95817019d164; current SHA-256=083a5b4efa6055f37c630bec23b31a5b1ec52bf018132f98a64c95817019d164; hash_changed=False. Reports=["reports/yaml_record_review/Tobramycin_Sulfate_Salt.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS identity is synchronized, but the ChEBI parent is generic sulfate salt and SELECTIVE_AGENT is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-f6b3c6190dc90db3.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-44e938ce76574611: Reassess prediction-only role support: Tobramycin sulfate salt

major / open / confirmed; issue key: mim-reconciliation-role-support-f6b3c6190dc90db3.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-44e938ce76574611

Reassess prediction-only role support: Tobramycin sulfate salt

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-278e9831932fb71e | data/ingredients/mapped/Tobramycin_Sulfate_Salt.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1971],"raw_equal":true},"docs_rows":[{"identifier":"cas:79645-27-5","line":1973,"mapping_status":"MAPPED","ontology_id":"CHEBI:35175","preferred_term":"Tobramycin sulfate salt"}],"identifier":"cas:79645-27-5","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:35175","ontology_label":"sulfate salt","ontology_source":"CHEBI"},"preferred_term":"Tobramycin sulfate salt","sssom_rows":[{"data_row":2787,"object_id":"CHEBI:35175","object_label":"sulfate salt","predicate_id":"skos:broadMatch"},{"data_row":2788,"object_id":"cas:79645-27-5","object_label":"Tobramycin sulfate salt","predicate_id":"skos:exactMatch"},{"data_row":2789,"object_id":"kgmicrobe.compound:tobramycin_sulfate_salt","object_label":"Tobramycin sulfate salt","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Tobramycin_Sulfate_Salt","synonym_count":0} |
| ev-fae8430227d0d551 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1971] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-cf85d876b05becc8 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Tobramycin_Sulfate_Salt; data-row positions=[2787,2788,2789] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2787,"object_id":"CHEBI:35175","object_label":"sulfate salt","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:Tobramycin_Sulfate_Salt","validation_method":"manual:reconcile_sssom&#124;PREDICATE&#124;2026-09-20"},{"data_row":2788,"object_id":"cas:79645-27-5","object_label":"Tobramycin sulfate salt","other":"CAS:79645-27-5","predicate_id":"skos:exactMatch","subject_id":"MIM:Tobramycin_Sulfate_Salt","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"},{"data_row":2789,"object_id":"kgmicrobe.compound:tobramycin_sulfate_salt","object_label":"Tobramycin sulfate salt","other":"CAS:79645-27-5","predicate_id":"skos:exactMatch","subject_id":"MIM:Tobramycin_Sulfate_Salt","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-f8d490ff2ceaa517 | docs/data/mapped_ingredients.csv; CSV lines=[1973] | supports | Published identity and count rows inspected: [{"identifier":"cas:79645-27-5","line":1973,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:35175","preferred_term":"Tobramycin sulfate salt","total_occurrences":"0"}] |
| ev-24dc7ddb5fe32c26 | reports/yaml_record_review/Tobramycin_Sulfate_Salt.md; &#96;data/ingredients/mapped/Tobramycin_Sulfate_Salt.yaml&#96;:2; Verdict:4; Identity:11; Validation:23; Evidence:31; Issues:41; Major: the ChEBI parent erases the tobramycin identity:43; Major: &#96;SELECTIVE_AGENT&#96; is provisional name-pattern evidence:59; Completeness:66; Recommended Edits:73 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-ed744e7560a5a720 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1293,1405] | context_only | [{"current_record_sha256":"083a5b4efa6055f37c630bec23b31a5b1ec52bf018132f98a64c95817019d164","finding_id":"SEM:eb011cee4c125e93e28e","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"083a5b4efa6055f37c630bec23b31a5b1ec52bf018132f98a64c95817019d164","finding_id":"SEM:9bc21f8574a84beb4062","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-55be5b2956d8b8e2 | data/ingredients/mapped/Tobramycin_Sulfate_Salt.yaml; physicochemical_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}] |
| ev-3d55734bc2dd1f41 | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml; findings[finding_id=f-44e938ce76574611] | context_only | Predecessor structured review finding f-44e938ce76574611 in 20261011T024638Z-mim-reconcile-all-batch-11 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.

## Complete Structured Record

The sibling review.yaml is authoritative.

````yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-tobramycin-sulfate-salt
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Tobramycin_Sulfate_Salt (data/ingredients/mapped/Tobramycin_Sulfate_Salt.yaml)'
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
summary: Per-record structured review for Tobramycin_Sulfate_Salt (data/ingredients/mapped/Tobramycin_Sulfate_Salt.yaml,
  record-f6b3c6190dc90db3, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Tobramycin_Sulfate_Salt.yaml
    sha256: 083a5b4efa6055f37c630bec23b31a5b1ec52bf018132f98a64c95817019d164
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
  - path: reports/yaml_record_review/Tobramycin_Sulfate_Salt.md
    sha256: caf038340fa1ca4252a3e0afa3ad58e2690a042ff6577dd692749c2de0cf8e0d
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-f6b3c6190dc90db3
  path: data/ingredients/mapped/Tobramycin_Sulfate_Salt.yaml
  label: Tobramycin_Sulfate_Salt
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Tobramycin_Sulfate_Salt.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Tobramycin_Sulfate_Salt.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Tobramycin_Sulfate_Salt.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-f6b3c6190dc90db3
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-f6b3c6190dc90db3
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-f6b3c6190dc90db3
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11
    and semantic review dispositions on HEAD.
  target_ids:
  - record-f6b3c6190dc90db3
evidence:
- evidence_id: ev-278e9831932fb71e
  kind: record_content
  reference: data/ingredients/mapped/Tobramycin_Sulfate_Salt.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1971],"raw_equal":true},"docs_rows":[{"identifier":"cas:79645-27-5","line":1973,"mapping_status":"MAPPED","ontology_id":"CHEBI:35175","preferred_term":"Tobramycin
    sulfate salt"}],"identifier":"cas:79645-27-5","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:35175","ontology_label":"sulfate
    salt","ontology_source":"CHEBI"},"preferred_term":"Tobramycin sulfate salt","sssom_rows":[{"data_row":2787,"object_id":"CHEBI:35175","object_label":"sulfate
    salt","predicate_id":"skos:broadMatch"},{"data_row":2788,"object_id":"cas:79645-27-5","object_label":"Tobramycin
    sulfate salt","predicate_id":"skos:exactMatch"},{"data_row":2789,"object_id":"kgmicrobe.compound:tobramycin_sulfate_salt","object_label":"Tobramycin
    sulfate salt","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Tobramycin_Sulfate_Salt","synonym_count":0}'
  snapshot_sha256: 083a5b4efa6055f37c630bec23b31a5b1ec52bf018132f98a64c95817019d164
- evidence_id: ev-fae8430227d0d551
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1971]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-cf85d876b05becc8
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Tobramycin_Sulfate_Salt; data-row positions=[2787,2788,2789]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2787,"object_id":"CHEBI:35175","object_label":"sulfate
    salt","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:Tobramycin_Sulfate_Salt","validation_method":"manual:reconcile_sssom|PREDICATE|2026-09-20"},{"data_row":2788,"object_id":"cas:79645-27-5","object_label":"Tobramycin
    sulfate salt","other":"CAS:79645-27-5","predicate_id":"skos:exactMatch","subject_id":"MIM:Tobramycin_Sulfate_Salt","validation_method":"none|UNKNOWN_TERM|2026-07-07"},{"data_row":2789,"object_id":"kgmicrobe.compound:tobramycin_sulfate_salt","object_label":"Tobramycin
    sulfate salt","other":"CAS:79645-27-5","predicate_id":"skos:exactMatch","subject_id":"MIM:Tobramycin_Sulfate_Salt","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-f8d490ff2ceaa517
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1973]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:79645-27-5","line":1973,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:35175","preferred_term":"Tobramycin
    sulfate salt","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-24dc7ddb5fe32c26
  kind: prior_review
  reference: reports/yaml_record_review/Tobramycin_Sulfate_Salt.md
  locator: '`data/ingredients/mapped/Tobramycin_Sulfate_Salt.yaml`:2; Verdict:4; Identity:11;
    Validation:23; Evidence:31; Issues:41; Major: the ChEBI parent erases the tobramycin
    identity:43; Major: `SELECTIVE_AGENT` is provisional name-pattern evidence:59;
    Completeness:66; Recommended Edits:73'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: caf038340fa1ca4252a3e0afa3ad58e2690a042ff6577dd692749c2de0cf8e0d
  quote: "Issues:\n\n\nMajor: the ChEBI parent erases the tobramycin identity:\nThe\
    \ stem-substring repair landed on:\n\n```yaml\nontology_mapping:\n  ontology_id:\
    \ CHEBI:35175\n  ontology_label: sulfate salt\n  mapping_quality: NARROW_MATCH\n\
    ```\n\nEvery sulfate antibiotic salt is narrower than generic `sulfate salt`,\
    \ so this\nparent does not carry the biologically important tobramycin identity\
    \ into the\nontology row. A specific `CHEBI:756148` `tobramycin sulfate` term\
    \ is now\nvisible in OLS and should be evaluated for exact remapping.\n\nMajor:\
    \ `SELECTIVE_AGENT` is provisional name-pattern evidence:\nThe only role assertion\
    \ is still the `infer_roles_from_name_lists`\n`COMPUTATIONAL_PREDICTION` entry\
    \ with the curator note `Provisional role from a\ncurated name-pattern rule; review\
    \ recommended.` That needs curated evidence or\nremoval just like the other antibiotic-salt\
    \ records.\n\nRecommended Edits:\n- Evaluate exact remapping to `CHEBI:756148`\
    \ `tobramycin sulfate`; if accepted,\n  retire the generic `CHEBI:35175` parent\
    \ and the local registry companion row.\n- Replace or remove the provisional `SELECTIVE_AGENT`\
    \ role evidence."
- evidence_id: ev-ed744e7560a5a720
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1293,1405]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"083a5b4efa6055f37c630bec23b31a5b1ec52bf018132f98a64c95817019d164","finding_id":"SEM:eb011cee4c125e93e28e","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"083a5b4efa6055f37c630bec23b31a5b1ec52bf018132f98a64c95817019d164","finding_id":"SEM:9bc21f8574a84beb4062","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-55be5b2956d8b8e2
  kind: record_content
  reference: data/ingredients/mapped/Tobramycin_Sulfate_Salt.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}]'
  snapshot_sha256: 083a5b4efa6055f37c630bec23b31a5b1ec52bf018132f98a64c95817019d164
- evidence_id: ev-3d55734bc2dd1f41
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml
  locator: findings[finding_id=f-44e938ce76574611]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-44e938ce76574611 in 20261011T024638Z-mim-reconcile-all-batch-11
  snapshot_sha256: a417d1bfc777756925990a4ecae1a6b539746c3606d042df7e1c29a218c62f8b
assessments:
- assessment_id: a-81b65a53ce00780f
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-f6b3c6190dc90db3
  evidence_ids:
  - ev-278e9831932fb71e
  - ev-fae8430227d0d551
  - ev-cf85d876b05becc8
  - ev-f8d490ff2ceaa517
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-e40abef5da2744e9
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-f6b3c6190dc90db3
  evidence_ids:
  - ev-24dc7ddb5fe32c26
  - ev-278e9831932fb71e
  - ev-ed744e7560a5a720
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T19:04:22Z;
    reviewed SHA-256=083a5b4efa6055f37c630bec23b31a5b1ec52bf018132f98a64c95817019d164;
    current SHA-256=083a5b4efa6055f37c630bec23b31a5b1ec52bf018132f98a64c95817019d164;
    hash_changed=False. Reports=["reports/yaml_record_review/Tobramycin_Sulfate_Salt.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CAS
    identity is synchronized, but the ChEBI parent is generic sulfate salt and SELECTIVE_AGENT
    is provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-24dc7ddb5fe32c26
    - ev-278e9831932fb71e
  - name: legacy-native-ids
    value: '["SEM:eb011cee4c125e93e28e","SEM:9bc21f8574a84beb4062"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-278e9831932fb71e
    - ev-24dc7ddb5fe32c26
    - ev-ed744e7560a5a720
- assessment_id: a-55be5b2956d8b8e2
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-f6b3c6190dc90db3
  evidence_ids:
  - ev-24dc7ddb5fe32c26
  - ev-55be5b2956d8b8e2
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-24dc7ddb5fe32c26
    - ev-55be5b2956d8b8e2
findings:
- finding_id: rec-f-44e938ce76574611
  issue_key: mim-reconciliation-role-support-f6b3c6190dc90db3
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Tobramycin sulfate salt'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-f6b3c6190dc90db3
  evidence_ids:
  - ev-24dc7ddb5fe32c26
  - ev-55be5b2956d8b8e2
  - ev-3d55734bc2dd1f41
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Tobramycin_Sulfate_Salt.yaml
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
    finding_id: f-44e938ce76574611
actions:
- action_id: rec-action-44e938ce76574611
  description: 'Reassess prediction-only role support: Tobramycin sulfate salt'
  finding_ids:
  - rec-f-44e938ce76574611
  target_ids:
  - record-f6b3c6190dc90db3
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Tobramycin_Sulfate_Salt.yaml
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
````
