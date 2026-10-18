# Per-record structured review: Cucl2_X_6_H2o (data/ingredients/mapped/Cucl2_X_6_H2o.yaml)

- Review: 20261017T083000Z-cucl2-x-6-h2o
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Cucl2_X_6_H2o (data/ingredients/mapped/Cucl2_X_6_H2o.yaml, record-87f6576606d1c4ff, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Cucl2_X_6_H2o.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Cucl2_X_6_H2o.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-87f6576606d1c4ff | data/ingredients/mapped/Cucl2_X_6_H2o.yaml | maintained | Cucl2_X_6_H2o |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-87f6576606d1c4ff | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-87f6576606d1c4ff | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-87f6576606d1c4ff | Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-87f6576606d1c4ff.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-87f6576606d1c4ff.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T12:47:26Z; reviewed SHA-256=617a79e853967c008d7dc62783d291b4189d2d9b5955d9f71b59d6230621b15c; current SHA-256=617a79e853967c008d7dc62783d291b4189d2d9b5955d9f71b59d6230621b15c; hash_changed=False. Reports=["reports/yaml_record_review/Cucl2_X_6_H2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local malformed copper chloride hydrate identity and 8/8 count pass, but the trace-element role is only computationally supported.

### Historical provisional-role concern

evidence: concern. Targets: record-87f6576606d1c4ff.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-a5c541e1e0152b7d: Reassess prediction-only role support: CuCl2 x 6 H2O

major / open / confirmed; issue key: mim-reconciliation-role-support-87f6576606d1c4ff.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-a5c541e1e0152b7d

Reassess prediction-only role support: CuCl2 x 6 H2O

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-541ee6d88d53e210 | data/ingredients/mapped/Cucl2_X_6_H2o.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[777],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:cucl2_x_6_h2o","line":779,"mapping_status":"MAPPED","ontology_id":"CHEBI:49553","preferred_term":"CuCl2 x 6 H2O"}],"identifier":"kgmicrobe.compound:cucl2_x_6_h2o","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":8,"edge_count":8,"occurrences":8},"occurrence_statistics":{"media_count":8,"total_occurrences":8},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:49553","ontology_label":"copper(II) chloride","ontology_source":"CHEBI"},"preferred_term":"CuCl2 x 6 H2O","sssom_rows":[{"data_row":844,"object_id":"CHEBI:49553","object_label":"copper(II) chloride","predicate_id":"skos:closeMatch"},{"data_row":845,"object_id":"kgmicrobe.compound:cucl2_x_6_h2o","object_label":"CuCl2 x 6 H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Cucl2_X_6_H2o","synonym_count":6} |
| ev-81544a52bb1253da | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [777] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-5554f740be7f750e | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Cucl2_X_6_H2o; data-row positions=[844,845] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":844,"object_id":"CHEBI:49553","object_label":"copper(II) chloride","other":"CuCl2 \u00d7 6H2O","predicate_id":"skos:closeMatch","subject_id":"MIM:Cucl2_X_6_H2o","validation_method":""},{"data_row":845,"object_id":"kgmicrobe.compound:cucl2_x_6_h2o","object_label":"CuCl2 x 6 H2O","other":"CuCl2 \u00d7 6H2O","predicate_id":"skos:exactMatch","subject_id":"MIM:Cucl2_X_6_H2o","validation_method":""}] |
| ev-538abbe5d816899c | docs/data/mapped_ingredients.csv; CSV lines=[779] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:cucl2_x_6_h2o","line":779,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"8","ontology_id":"CHEBI:49553","preferred_term":"CuCl2 x 6 H2O","total_occurrences":"8"}] |
| ev-9013677fe794fa50 | reports/yaml_record_review/Cucl2_X_6_H2o.md; &#96;data/ingredients/mapped/Cucl2_X_6_H2o.yaml&#96;:2; Verdict:4; Identity:11; Validation:25; Evidence:45; Completeness:66; Recommended Edits:73 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-204cf3babd74e67e | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[451,1573] | context_only | [{"current_record_sha256":"617a79e853967c008d7dc62783d291b4189d2d9b5955d9f71b59d6230621b15c","finding_id":"SEM:d2125b24b11015bdcd97","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"617a79e853967c008d7dc62783d291b4189d2d9b5955d9f71b59d6230621b15c","finding_id":"SEM:6693c9066d4c4eab5ae8","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-e3eaca6bb4375de1 | data/ingredients/mapped/Cucl2_X_6_H2o.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"TRACE_ELEMENT"}}] |
| ev-e085fdfc21ee35bc | reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml; findings[finding_id=f-a5c541e1e0152b7d] | context_only | Predecessor structured review finding f-a5c541e1e0152b7d in 20261011T024633Z-mim-reconcile-all-batch-05 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-cucl2-x-6-h2o
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Cucl2_X_6_H2o (data/ingredients/mapped/Cucl2_X_6_H2o.yaml)'
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
summary: Per-record structured review for Cucl2_X_6_H2o (data/ingredients/mapped/Cucl2_X_6_H2o.yaml,
  record-87f6576606d1c4ff, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Cucl2_X_6_H2o.yaml
    sha256: 617a79e853967c008d7dc62783d291b4189d2d9b5955d9f71b59d6230621b15c
    role: target
  - path: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
    sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
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
  - path: reports/yaml_record_review/Cucl2_X_6_H2o.md
    sha256: c05625427845cd2a92a988d9ba94590b449eb20cf514ab32d9294feb9a4896b9
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-87f6576606d1c4ff
  path: data/ingredients/mapped/Cucl2_X_6_H2o.yaml
  label: Cucl2_X_6_H2o
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cucl2_X_6_H2o.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Cucl2_X_6_H2o.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Cucl2_X_6_H2o.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-87f6576606d1c4ff
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-87f6576606d1c4ff
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-87f6576606d1c4ff
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05
    and semantic review dispositions on HEAD.
  target_ids:
  - record-87f6576606d1c4ff
evidence:
- evidence_id: ev-541ee6d88d53e210
  kind: record_content
  reference: data/ingredients/mapped/Cucl2_X_6_H2o.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[777],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:cucl2_x_6_h2o","line":779,"mapping_status":"MAPPED","ontology_id":"CHEBI:49553","preferred_term":"CuCl2
    x 6 H2O"}],"identifier":"kgmicrobe.compound:cucl2_x_6_h2o","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":8,"edge_count":8,"occurrences":8},"occurrence_statistics":{"media_count":8,"total_occurrences":8},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:49553","ontology_label":"copper(II)
    chloride","ontology_source":"CHEBI"},"preferred_term":"CuCl2 x 6 H2O","sssom_rows":[{"data_row":844,"object_id":"CHEBI:49553","object_label":"copper(II)
    chloride","predicate_id":"skos:closeMatch"},{"data_row":845,"object_id":"kgmicrobe.compound:cucl2_x_6_h2o","object_label":"CuCl2
    x 6 H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Cucl2_X_6_H2o","synonym_count":6}'
  snapshot_sha256: 617a79e853967c008d7dc62783d291b4189d2d9b5955d9f71b59d6230621b15c
- evidence_id: ev-81544a52bb1253da
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [777]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-5554f740be7f750e
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Cucl2_X_6_H2o; data-row positions=[844,845]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":844,"object_id":"CHEBI:49553","object_label":"copper(II)
    chloride","other":"CuCl2 \u00d7 6H2O","predicate_id":"skos:closeMatch","subject_id":"MIM:Cucl2_X_6_H2o","validation_method":""},{"data_row":845,"object_id":"kgmicrobe.compound:cucl2_x_6_h2o","object_label":"CuCl2
    x 6 H2O","other":"CuCl2 \u00d7 6H2O","predicate_id":"skos:exactMatch","subject_id":"MIM:Cucl2_X_6_H2o","validation_method":""}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-538abbe5d816899c
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[779]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:cucl2_x_6_h2o","line":779,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"8","ontology_id":"CHEBI:49553","preferred_term":"CuCl2
    x 6 H2O","total_occurrences":"8"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-9013677fe794fa50
  kind: prior_review
  reference: reports/yaml_record_review/Cucl2_X_6_H2o.md
  locator: '`data/ingredients/mapped/Cucl2_X_6_H2o.yaml`:2; Verdict:4; Identity:11;
    Validation:25; Evidence:45; Completeness:66; Recommended Edits:73'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: c05625427845cd2a92a988d9ba94590b449eb20cf514ab32d9294feb9a4896b9
  quote: "Recommended Edits:\n- Major: either replace the provisional `TRACE_ELEMENT`\
    \ evidence in\n  `data/ingredients/mapped/Cucl2_X_6_H2o.yaml` with a source-backed\n\
    \  `DATABASE_ENTRY`, or drop the role if the CultureMech rows do not actually\n\
    \  support this unresolved label as the mineral or trace element source.\n- Regenerate\
    \ synchronized products and rerun strict validation, SSSOM QC,\n  aggregate roundtrip,\
    \ and `git diff --check`."
- evidence_id: ev-204cf3babd74e67e
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[451,1573]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"617a79e853967c008d7dc62783d291b4189d2d9b5955d9f71b59d6230621b15c","finding_id":"SEM:d2125b24b11015bdcd97","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"617a79e853967c008d7dc62783d291b4189d2d9b5955d9f71b59d6230621b15c","finding_id":"SEM:6693c9066d4c4eab5ae8","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-e3eaca6bb4375de1
  kind: record_content
  reference: data/ingredients/mapped/Cucl2_X_6_H2o.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"TRACE_ELEMENT"}}]'
  snapshot_sha256: 617a79e853967c008d7dc62783d291b4189d2d9b5955d9f71b59d6230621b15c
- evidence_id: ev-e085fdfc21ee35bc
  kind: prior_review
  reference: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
  locator: findings[finding_id=f-a5c541e1e0152b7d]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-a5c541e1e0152b7d in 20261011T024633Z-mim-reconcile-all-batch-05
  snapshot_sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
assessments:
- assessment_id: a-13ade5cb9ca49478
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-87f6576606d1c4ff
  evidence_ids:
  - ev-541ee6d88d53e210
  - ev-81544a52bb1253da
  - ev-5554f740be7f750e
  - ev-538abbe5d816899c
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-a9aecded1009cc20
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-87f6576606d1c4ff
  evidence_ids:
  - ev-9013677fe794fa50
  - ev-541ee6d88d53e210
  - ev-204cf3babd74e67e
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T12:47:26Z;
    reviewed SHA-256=617a79e853967c008d7dc62783d291b4189d2d9b5955d9f71b59d6230621b15c;
    current SHA-256=617a79e853967c008d7dc62783d291b4189d2d9b5955d9f71b59d6230621b15c;
    hash_changed=False. Reports=["reports/yaml_record_review/Cucl2_X_6_H2o.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The local malformed
    copper chloride hydrate identity and 8/8 count pass, but the trace-element role
    is only computationally supported.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-9013677fe794fa50
    - ev-541ee6d88d53e210
  - name: legacy-native-ids
    value: '["SEM:d2125b24b11015bdcd97","SEM:6693c9066d4c4eab5ae8"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-541ee6d88d53e210
    - ev-9013677fe794fa50
    - ev-204cf3babd74e67e
- assessment_id: a-e3eaca6bb4375de1
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-87f6576606d1c4ff
  evidence_ids:
  - ev-9013677fe794fa50
  - ev-e3eaca6bb4375de1
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-9013677fe794fa50
    - ev-e3eaca6bb4375de1
findings:
- finding_id: rec-f-a5c541e1e0152b7d
  issue_key: mim-reconciliation-role-support-87f6576606d1c4ff
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: CuCl2 x 6 H2O'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-87f6576606d1c4ff
  evidence_ids:
  - ev-9013677fe794fa50
  - ev-e3eaca6bb4375de1
  - ev-e085fdfc21ee35bc
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cucl2_X_6_H2o.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[0]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024633Z-mim-reconcile-all-batch-05
    finding_id: f-a5c541e1e0152b7d
actions:
- action_id: rec-action-a5c541e1e0152b7d
  description: 'Reassess prediction-only role support: CuCl2 x 6 H2O'
  finding_ids:
  - rec-f-a5c541e1e0152b7d
  target_ids:
  - record-87f6576606d1c4ff
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cucl2_X_6_H2o.yaml
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
  with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.
```
