# Per-record structured review: Desulfovibrio_Trace_Elements (data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml)

- Review: 20261017T083000Z-desulfovibrio-trace-elements
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Desulfovibrio_Trace_Elements (data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml, record-797da68010f27377, mapping_status=MAPPED). Records 1 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-797da68010f27377 | data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml | maintained | Desulfovibrio_Trace_Elements |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-797da68010f27377 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-797da68010f27377 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-797da68010f27377 | Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-797da68010f27377.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-797da68010f27377.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T14:30:48Z; reviewed SHA-256=93db08d82a87268e9c970192268b222cd7f518ef64f468aeceea672e329a20ea; current SHA-256=93db08d82a87268e9c970192268b222cd7f518ef64f468aeceea672e329a20ea; hash_changed=False. Reports=["reports/yaml_record_review/Desulfovibrio_Trace_Elements.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The record exact-maps a named trace-element stock to generic MeSH Trace Elements and leaks an unsafe SSSOM alias.

### Unresolved recipe-reference or truncated-concentration synonyms

nomenclature: concern. Targets: record-797da68010f27377.

Historical tokens are still present on the exact-subject SSSOM rows: [{"reason":"unresolved recipe cross-reference in a resolving synonym","token":"Trace elements (see below)"}]. Truncated concentration strings and context-dependent instructions need scoped curation. This check does not reject catalog/RAW_TEXT synonyms as a class.

### Certainty correction for the exact token observation

nomenclature: unknown. Targets: record-797da68010f27377.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

### Historical provisional-role concern

evidence: concern. Targets: record-797da68010f27377.

Current role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence lists and require source-backed curation support.

## Findings

### rec-scope-f-320ccfb6bddc74ee: Adjudicate source scope of exported tokens: Desulfovibrio trace elements

major / deferred / provisional; issue key: mim-reconciliation-exported-context-tokens-797da68010f27377.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

Disposition: Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

### rec-f-role-797da68010f27377: Reassess prediction-only or empty role support: Desulfovibrio_Trace_Elements

major / open / confirmed; issue key: mim-reconciliation-role-support-797da68010f27377.

Prediction-only or empty evidence payloads remain on the named current role assertions (nutritional_roles[0]). This confirms the local evidence gap, not that the biological role is false.

## Recommended Actions And Acceptance Checks

### rec-act-role-797da68010f27377

Reassess prediction-only or empty role support: Desulfovibrio_Trace_Elements

- Address the exact role fields and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-d6439cb28de651aa | data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[876],"raw_equal":true},"docs_rows":[{"identifier":"mesh:D014131","line":878,"mapping_status":"MAPPED","ontology_id":"mesh:D014131","preferred_term":"Desulfovibrio trace elements"}],"identifier":"mesh:D014131","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"LEXICAL_MATCH","ontology_id":"mesh:D014131","ontology_label":"Trace Elements","ontology_source":"MESH"},"preferred_term":"Desulfovibrio trace elements","sssom_rows":[{"data_row":1021,"object_id":"mesh:D014131","object_label":"Trace Elements","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Desulfovibrio_Trace_Elements","synonym_count":2} |
| ev-749bd53b36a6d5db | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [876] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-42f981730201a7f4 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Desulfovibrio_Trace_Elements; data-row positions=[1021] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1021,"object_id":"mesh:D014131","object_label":"Trace Elements","other":"Trace elements (see below)","predicate_id":"skos:exactMatch","subject_id":"MIM:Desulfovibrio_Trace_Elements","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-107b07b9167d8e86 | docs/data/mapped_ingredients.csv; CSV lines=[878] | supports | Published identity and count rows inspected: [{"identifier":"mesh:D014131","line":878,"mapping_quality":"LEXICAL_MATCH","mapping_status":"MAPPED","media_count":"3","ontology_id":"mesh:D014131","preferred_term":"Desulfovibrio trace elements","total_occurrences":"3"}] |
| ev-ee7e48ee832f8a11 | reports/yaml_record_review/Desulfovibrio_Trace_Elements.md; &#96;data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml&#96;:2; Verdict:4; Identity:12; Validation:28; Evidence:46; Completeness:69; Recommended Edits:78 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-09f3b1749685f149 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[528,2008] | context_only | [{"current_record_sha256":"93db08d82a87268e9c970192268b222cd7f518ef64f468aeceea672e329a20ea","finding_id":"SEM:c747ee61b82b3c551f4e","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"93db08d82a87268e9c970192268b222cd7f518ef64f468aeceea672e329a20ea","finding_id":"SEM:ff674849573fd6612bad","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-823412d1eacb6795 | MAPPING_SEMANTICS.md; Sections on REJECTED_LABEL and the damaged-label RAW_TEXT carve-out | supports | Raw spellings may remain resolvable when they denote the same substance. Wrong-identity labels must not resolve. A recipe-pointer pattern alone does not adjudicate that distinction. |
| ev-9477d91976d0a888 | reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml; findings[finding_id=f-320ccfb6bddc74ee] | context_only | Exact earlier occurrence has open/confirmed status, based on exported-token presence and historical report text. |
| ev-4d30788725c98994 | data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml; identifier, ontology_mapping, synonyms and curation_history | partial | {"candidate_labels": [{"source": "culturemech:output/ingredient_occurrences.tsv", "synonym_text": "Trace elements (see below)", "synonym_type": "RAW_TEXT"}], "history": [{"action": "CREATED_AS_UNMAPPED", "changes": "Imported from CultureBotHT (consolidated_media.json (media-only)). Used in 3 CultureBot media; samples: MoLS4, Dv_base_medium, MoLS4_no_vitamins. No CAS-RN or CHEBI mapping available; curator review needed.", "curator": "audit_add_remaining_culturebotht", "llm_assisted": false, "new_status": "UNMAPPED", "timestamp": "2026-04-29T06:51:33.117170+00:00"}, {"action": "AUTO_UPGRADE_TO_MESH", "changes": "primary UNMAPPED_0294 \u2192 mesh:D014131 (strategy=stem-match)", "curator": "resolve_unmapped_v2", "llm_assisted": false, "timestamp": "2026-05-02T03:18:21.917940+00:00"}, {"action": "ANNOTATED", "changes": "Added media role: TRACE_ELEMENT (confidence: 0.60)", "curator": "claude_in_session_curation", "timestamp": "2026-06-09T04:56:30.247868+00:00"}, {"action": "ANNOTATED", "changes": "Migrated legacy media_roles to role facets (#128): TRACE_ELEMENT -&gt; nutritional_roles.TRACE_ELEMENT", "curator": "migrate_media_roles_to_facets", "timestamp": "2026-07-20T00:00:00+00:00"}, {"action": "ADDED_SYNONYMS", "changes": "Added 1 CultureMech recipe surface form(s) that folded onto this record's published label but were absent from MIM's label index, so CultureMech could not resolve them: 'Trace elements (see below)' (x1 CultureMech mentions). Source: culturemech:output/ingredient_occurrences.tsv.", "curator": "claude_culturemech_alias_backfill", "llm_assisted": false, "timestamp": "2026-08-30T04:48:06.233536+00:00"}], "identifier": "mesh:D014131", "mapping": {"evidence": [{"evidence_type": "DATABASE_MATCH", "notes": "Auto-upgraded from UNMAPPED_0294; matched via 'Desulfovibrio trace elements'; stem-substring", "source": "MESH via OLS (resolve_unmapped_v2 strategy=stem-match)"}], "mapping_quality": "LEXICAL_MATCH", "ontology_id": "mesh:D014131", "ontology_label": "Trace Elements", "ontology_source": "MESH"}} |
| ev-a255c9d3059064fe | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Desulfovibrio_Trace_Elements | supports | [{"comment": "", "confidence": "0.9", "data_row": 1021, "mapping_date": "2026-08-30", "mapping_justification": "semapv:LexicalMatching", "object_id": "mesh:D014131", "object_label": "Trace Elements", "object_source": "registry:mesh", "other": "Trace elements (see below)", "predicate_id": "skos:exactMatch", "source": "MIM:MESH via OLS (resolve_unmapped_v2 strategy=stem-match)&#124;MIM:curator=claude_culturemech_alias_backfill", "subject_id": "MIM:Desulfovibrio_Trace_Elements", "subject_label": "Desulfovibrio trace elements", "validation_method": "none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-e7674a969ec8d8cb | reports/yaml_record_review/Desulfovibrio_Trace_Elements.md; Complete historical report, including Verdict and Recommended Edits | context_only | Historical interpretation was read in full; it is not fresh source adjudication. |
| ev-f700de79d37b3937 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; current_record=data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml | context_only | Semantic review finding dispositions ledger |
| ev-f9a3b6f8e2a4ef2f | reviews/structured/20261011T030852Z-mim-token-scope-reassessment/review.yaml; findings[finding_id=scope-f-320ccfb6bddc74ee] | context_only | Predecessor structured review finding scope-f-320ccfb6bddc74ee in 20261011T030852Z-mim-token-scope-reassessment |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024633Z-mim-reconcile-all-batch-05, 20261011T030852Z-mim-token-scope-reassessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-desulfovibrio-trace-elements
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Desulfovibrio_Trace_Elements (data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml)'
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
native_verdict: mapping_status=MAPPED; open=1; deferred=1
scientific_review: false
summary: Per-record structured review for Desulfovibrio_Trace_Elements (data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml,
  record-797da68010f27377, mapping_status=MAPPED). Records 1 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml
    sha256: 93db08d82a87268e9c970192268b222cd7f518ef64f468aeceea672e329a20ea
    role: target
  - path: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
    sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
    role: context
  - path: reviews/structured/20261011T030852Z-mim-token-scope-reassessment/review.yaml
    sha256: 42a76b000bcbd07b426f6bad61b124b11ec08d8977783a67b732b01754f7c609
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
  - path: reports/yaml_record_review/Desulfovibrio_Trace_Elements.md
    sha256: f655ff5e9d199deb38ad4e8e7e7ddb2aa844aecc6d1ec3efb037bbfade3e6aba
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
  - path: MAPPING_SEMANTICS.md
    sha256: 94aad13ea0fc3df82a37383f388f41432b607b04cac61ae5792ce1a381aef805
    role: context
targets:
- target_id: record-797da68010f27377
  path: data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml
  label: Desulfovibrio_Trace_Elements
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-797da68010f27377
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-797da68010f27377
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-797da68010f27377
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05
    and semantic review dispositions on HEAD.
  target_ids:
  - record-797da68010f27377
evidence:
- evidence_id: ev-d6439cb28de651aa
  kind: record_content
  reference: data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[876],"raw_equal":true},"docs_rows":[{"identifier":"mesh:D014131","line":878,"mapping_status":"MAPPED","ontology_id":"mesh:D014131","preferred_term":"Desulfovibrio
    trace elements"}],"identifier":"mesh:D014131","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"LEXICAL_MATCH","ontology_id":"mesh:D014131","ontology_label":"Trace
    Elements","ontology_source":"MESH"},"preferred_term":"Desulfovibrio trace elements","sssom_rows":[{"data_row":1021,"object_id":"mesh:D014131","object_label":"Trace
    Elements","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Desulfovibrio_Trace_Elements","synonym_count":2}'
  snapshot_sha256: 93db08d82a87268e9c970192268b222cd7f518ef64f468aeceea672e329a20ea
- evidence_id: ev-749bd53b36a6d5db
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [876]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-42f981730201a7f4
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Desulfovibrio_Trace_Elements; data-row positions=[1021]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1021,"object_id":"mesh:D014131","object_label":"Trace
    Elements","other":"Trace elements (see below)","predicate_id":"skos:exactMatch","subject_id":"MIM:Desulfovibrio_Trace_Elements","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-107b07b9167d8e86
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[878]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"mesh:D014131","line":878,"mapping_quality":"LEXICAL_MATCH","mapping_status":"MAPPED","media_count":"3","ontology_id":"mesh:D014131","preferred_term":"Desulfovibrio
    trace elements","total_occurrences":"3"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-ee7e48ee832f8a11
  kind: prior_review
  reference: reports/yaml_record_review/Desulfovibrio_Trace_Elements.md
  locator: '`data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml`:2; Verdict:4;
    Identity:12; Validation:28; Evidence:46; Completeness:69; Recommended Edits:78'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: f655ff5e9d199deb38ad4e8e7e7ddb2aa844aecc6d1ec3efb037bbfade3e6aba
  quote: "Recommended Edits:\n- Major: retarget\n  `data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml`\
    \ to a local\n  stock identity such as\n  `kgmicrobe.ingredient:desulfovibrio_trace_elements`,\
    \ keep\n  `mesh:D014131` at most as a `NARROW_MATCH` parent, synchronize\n  `data/curated/mapped_ingredients.yaml`,\
    \ and regenerate SSSOM so a\n  registry/identity row is emitted beside the MeSH\
    \ parent row.\n- Major: add source-backed `components` and a `component_assertion`\
    \ from the\n  maintained CultureBotHT or CultureMech formulation evidence, or\
    \ document the\n  formulation as unresolved in `discussions` if the exact stock\
    \ recipe cannot\n  be recovered.\n- Major: remove `Trace elements (see below)`\
    \ from final SSSOM `other` by\n  demoting it out of active synonym export or by\
    \ proving it is a true alias for\n  this exact stock.\n- Major: source or remove\
    \ `nutritional_roles.TRACE_ELEMENT`."
- evidence_id: ev-09f3b1749685f149
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[528,2008]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"93db08d82a87268e9c970192268b222cd7f518ef64f468aeceea672e329a20ea","finding_id":"SEM:c747ee61b82b3c551f4e","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"93db08d82a87268e9c970192268b222cd7f518ef64f468aeceea672e329a20ea","finding_id":"SEM:ff674849573fd6612bad","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-823412d1eacb6795
  kind: record_content
  reference: MAPPING_SEMANTICS.md
  locator: Sections on REJECTED_LABEL and the damaged-label RAW_TEXT carve-out
  accessed_at: '2026-10-11T03:08:52Z'
  support: supports
  summary: Raw spellings may remain resolvable when they denote the same substance.
    Wrong-identity labels must not resolve. A recipe-pointer pattern alone does not
    adjudicate that distinction.
  snapshot_sha256: 94aad13ea0fc3df82a37383f388f41432b607b04cac61ae5792ce1a381aef805
- evidence_id: ev-9477d91976d0a888
  kind: prior_review
  reference: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
  locator: findings[finding_id=f-320ccfb6bddc74ee]
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Exact earlier occurrence has open/confirmed status, based on exported-token
    presence and historical report text.
  snapshot_sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
  quote: '{"category": "nomenclature", "certainty": "confirmed", "description": "Historical
    tokens are still present on the exact-subject SSSOM rows: [{\"reason\":\"unresolved
    recipe cross-reference in a resolving synonym\",\"token\":\"Trace elements (see
    below)\"}]. Truncated concentration strings and context-dependent instructions
    need scoped curation. This check does not reject catalog/RAW_TEXT synonyms as
    a class.", "evidence_ids": ["ev-ee7e48ee832f8a11", "ev-42f981730201a7f4"], "external_issues":
    ["https://github.com/CultureBotAI/MediaIngredientMech/issues/718"], "field_paths":
    ["synonyms", "SSSOM.other"], "finding_id": "f-320ccfb6bddc74ee", "issue_key":
    "mim-reconciliation-exported-context-tokens-797da68010f27377", "owner_paths":
    [{"path": "data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml", "repository":
    "CultureBotAI/MediaIngredientMech", "role": "maintained ingredient"}], "severity":
    "major", "status": "open", "tags": ["reconciliation", "bundle-by-owner", "exported-context-tokens"],
    "target_ids": ["record-797da68010f27377"], "title": "Review nonportable exported
    tokens: Desulfovibrio trace elements"}'
- evidence_id: ev-4d30788725c98994
  kind: record_content
  reference: data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml
  locator: identifier, ontology_mapping, synonyms and curation_history
  accessed_at: '2026-10-11T03:08:52Z'
  support: partial
  summary: '{"candidate_labels": [{"source": "culturemech:output/ingredient_occurrences.tsv",
    "synonym_text": "Trace elements (see below)", "synonym_type": "RAW_TEXT"}], "history":
    [{"action": "CREATED_AS_UNMAPPED", "changes": "Imported from CultureBotHT (consolidated_media.json
    (media-only)). Used in 3 CultureBot media; samples: MoLS4, Dv_base_medium, MoLS4_no_vitamins.
    No CAS-RN or CHEBI mapping available; curator review needed.", "curator": "audit_add_remaining_culturebotht",
    "llm_assisted": false, "new_status": "UNMAPPED", "timestamp": "2026-04-29T06:51:33.117170+00:00"},
    {"action": "AUTO_UPGRADE_TO_MESH", "changes": "primary UNMAPPED_0294 \u2192 mesh:D014131
    (strategy=stem-match)", "curator": "resolve_unmapped_v2", "llm_assisted": false,
    "timestamp": "2026-05-02T03:18:21.917940+00:00"}, {"action": "ANNOTATED", "changes":
    "Added media role: TRACE_ELEMENT (confidence: 0.60)", "curator": "claude_in_session_curation",
    "timestamp": "2026-06-09T04:56:30.247868+00:00"}, {"action": "ANNOTATED", "changes":
    "Migrated legacy media_roles to role facets (#128): TRACE_ELEMENT -> nutritional_roles.TRACE_ELEMENT",
    "curator": "migrate_media_roles_to_facets", "timestamp": "2026-07-20T00:00:00+00:00"},
    {"action": "ADDED_SYNONYMS", "changes": "Added 1 CultureMech recipe surface form(s)
    that folded onto this record''s published label but were absent from MIM''s label
    index, so CultureMech could not resolve them: ''Trace elements (see below)'' (x1
    CultureMech mentions). Source: culturemech:output/ingredient_occurrences.tsv.",
    "curator": "claude_culturemech_alias_backfill", "llm_assisted": false, "timestamp":
    "2026-08-30T04:48:06.233536+00:00"}], "identifier": "mesh:D014131", "mapping":
    {"evidence": [{"evidence_type": "DATABASE_MATCH", "notes": "Auto-upgraded from
    UNMAPPED_0294; matched via ''Desulfovibrio trace elements''; stem-substring",
    "source": "MESH via OLS (resolve_unmapped_v2 strategy=stem-match)"}], "mapping_quality":
    "LEXICAL_MATCH", "ontology_id": "mesh:D014131", "ontology_label": "Trace Elements",
    "ontology_source": "MESH"}}'
  snapshot_sha256: 93db08d82a87268e9c970192268b222cd7f518ef64f468aeceea672e329a20ea
- evidence_id: ev-a255c9d3059064fe
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Desulfovibrio_Trace_Elements
  accessed_at: '2026-10-11T03:08:52Z'
  support: supports
  summary: '[{"comment": "", "confidence": "0.9", "data_row": 1021, "mapping_date":
    "2026-08-30", "mapping_justification": "semapv:LexicalMatching", "object_id":
    "mesh:D014131", "object_label": "Trace Elements", "object_source": "registry:mesh",
    "other": "Trace elements (see below)", "predicate_id": "skos:exactMatch", "source":
    "MIM:MESH via OLS (resolve_unmapped_v2 strategy=stem-match)|MIM:curator=claude_culturemech_alias_backfill",
    "subject_id": "MIM:Desulfovibrio_Trace_Elements", "subject_label": "Desulfovibrio
    trace elements", "validation_method": "none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-e7674a969ec8d8cb
  kind: prior_review
  reference: reports/yaml_record_review/Desulfovibrio_Trace_Elements.md
  locator: Complete historical report, including Verdict and Recommended Edits
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Historical interpretation was read in full; it is not fresh source adjudication.
  snapshot_sha256: f655ff5e9d199deb38ad4e8e7e7ddb2aa844aecc6d1ec3efb037bbfade3e6aba
  quote: "# `data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml`\n\n## Verdict\n\
    \nNeeds curation. `mesh:D014131` is a valid MeSH term for the generic class\n\
    `Trace Elements`, but the MIM subject is a recipe-local\n`Desulfovibrio trace\
    \ elements` stock or reagent group. The current exactMatch\ntherefore erases specificity,\
    \ omits stock components, and publishes\n`Trace elements (see below)` as an unsafe\
    \ final SSSOM synonym.\n\n## Identity\n\n- Reviewed record:\n  `data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml`.\n\
    - Current grounding: `identifier: mesh:D014131` with\n  `ontology_mapping.ontology_id:\
    \ mesh:D014131`, label `Trace Elements`,\n  source `MESH`, `mapping_quality: LEXICAL_MATCH`,\
    \ and\n  `mapping_status: MAPPED`.\n- Live prefix-specific OLS resolves `mesh:D014131`\
    \ exactly to MeSH\n  `Trace Elements`, and a live exact MeSH search for\n  `Desulfovibrio\
    \ trace elements` returned no class.\n- The source label is a named Desulfovibrio\
    \ trace-elements preparation, not\n  the generic MeSH trace-element class. This\
    \ should be a local\n  `kgmicrobe.ingredient:desulfovibrio_trace_elements` identity\
    \ if no\n  formulation-specific ontology term exists.\n\n## Validation\n\n- `uv\
    \ run --frozen python scripts/validate_strict.py data/ingredients/mapped/Destomycin.yaml\
    \ data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml data/ingredients/mapped/Deuterated_Glucose.yaml\
    \ data/ingredients/mapped/Dextran.yaml data/ingredients/mapped/Dextrin.yaml`:\n\
    \  passed; 5 files scanned, 0 ERROR rows.\n- `uv run --frozen linkml-term-validator\
    \ validate-data ...` over the mixed\n  five-record batch aborted before the MeSH\
    \ record at the local\n  `kgmicrobe.compound:destomycin` registry identifier.\n\
    - `curl -L ... q=Trace Elements&ontology=mesh&exact=true`: live OLS returned\n\
    \  exact `mesh:D014131`.\n- `curl -L ... q=Desulfovibrio trace elements&ontology=mesh&exact=true`:\
    \ live\n  OLS returned 0 rows.\n- `uv run --frozen python scripts/validate_sssom_invariants.py`:\
    \ passed Rules\n  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped\
    \ because\n  the sibling kg-microbe ontology transforms were absent.\n- `uv run\
    \ --frozen python scripts/validate_component_partonomy.py`: passed;\n  the full\
    \ corpus had 2,951 records, 83 decompositions, 505 components, and 0\n  violations.\n\
    \n## Evidence\n\n- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv`\
    \ confirms\n  that `mesh:D014131` resolves through prefix-specific OLS, but that\
    \ only\n  validates the target CURIE. It does not support treating a named\n \
    \ Desulfovibrio trace-element preparation as exact identity with the generic\n\
    \  MeSH class.\n- The hidden/ignored-inclusive exact search over `data/ingredients`,\n\
    \  `data/curated`, `mappings`, `docs/data`, `src`, and `scripts` found no\n  component\
    \ list for this stock record and no exact OLS hit for\n  `Desulfovibrio trace\
    \ elements`.\n- The final `mappings/ingredient_mappings.sssom.tsv` row maps\n\
    \  `MIM:Desulfovibrio_Trace_Elements` to `mesh:D014131` with\n  `skos:exactMatch`\
    \ and `Trace elements (see below)` in `other`. That `other`\n  token is a recipe-local\
    \ pointer, not a real synonym for the modeled MIM\n  subject.\n- `mappings/culturemech_residual_triage.tsv`\
    \ still carries\n  `Trace elements (see below)` as a stale unresolved alias even\
    \ though the\n  alias is now on this record and leaks into final SSSOM.\n- Major:\
    \ `nutritional_roles.TRACE_ELEMENT` is supported only by an in-session\n  `COMPUTATIONAL_PREDICTION`\
    \ role assignment and needs source-backed role\n  evidence if it is retained.\n\
    \n## Completeness\n\n- The occurrence count and raw source labels preserve the\
    \ legacy CultureBotHT\n  provenance: the record was created from `consolidated_media.json`,\
    \ used in 3\n  CultureBot media, and names `MoLS4`, `Dv_base_medium`, and\n  `MoLS4_no_vitamins`\
    \ as samples.\n- Major: the stock has no `components` or `component_assertion`,\
    \ so a reader\n  cannot recover which trace elements are meant.\n\n## Recommended\
    \ Edits\n\n- Major: retarget\n  `data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml`\
    \ to a local\n  stock identity such as\n  `kgmicrobe.ingredient:desulfovibrio_trace_elements`,\
    \ keep\n  `mesh:D014131` at most as a `NARROW_MATCH` parent, synchronize\n  `data/curated/mapped_ingredients.yaml`,\
    \ and regenerate SSSOM so a\n  registry/identity row is emitted beside the MeSH\
    \ parent row.\n- Major: add source-backed `components` and a `component_assertion`\
    \ from the\n  maintained CultureBotHT or CultureMech formulation evidence, or\
    \ document the\n  formulation as unresolved in `discussions` if the exact stock\
    \ recipe cannot\n  be recovered.\n- Major: remove `Trace elements (see below)`\
    \ from final SSSOM `other` by\n  demoting it out of active synonym export or by\
    \ proving it is a true alias for\n  this exact stock.\n- Major: source or remove\
    \ `nutritional_roles.TRACE_ELEMENT`.\n"
- evidence_id: ev-f700de79d37b3937
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: current_record=data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Semantic review finding dispositions ledger
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-f9a3b6f8e2a4ef2f
  kind: prior_review
  reference: reviews/structured/20261011T030852Z-mim-token-scope-reassessment/review.yaml
  locator: findings[finding_id=scope-f-320ccfb6bddc74ee]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding scope-f-320ccfb6bddc74ee in 20261011T030852Z-mim-token-scope-reassessment
  snapshot_sha256: 42a76b000bcbd07b426f6bad61b124b11ec08d8977783a67b732b01754f7c609
assessments:
- assessment_id: a-fec3ddec705a07d1
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-797da68010f27377
  evidence_ids:
  - ev-d6439cb28de651aa
  - ev-749bd53b36a6d5db
  - ev-42f981730201a7f4
  - ev-107b07b9167d8e86
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-47f77398a23b7377
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-797da68010f27377
  evidence_ids:
  - ev-ee7e48ee832f8a11
  - ev-d6439cb28de651aa
  - ev-09f3b1749685f149
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T14:30:48Z;
    reviewed SHA-256=93db08d82a87268e9c970192268b222cd7f518ef64f468aeceea672e329a20ea;
    current SHA-256=93db08d82a87268e9c970192268b222cd7f518ef64f468aeceea672e329a20ea;
    hash_changed=False. Reports=["reports/yaml_record_review/Desulfovibrio_Trace_Elements.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The record
    exact-maps a named trace-element stock to generic MeSH Trace Elements and leaks
    an unsafe SSSOM alias.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-ee7e48ee832f8a11
    - ev-d6439cb28de651aa
  - name: legacy-native-ids
    value: '["SEM:c747ee61b82b3c551f4e","SEM:ff674849573fd6612bad"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-d6439cb28de651aa
    - ev-ee7e48ee832f8a11
    - ev-09f3b1749685f149
- assessment_id: a-b5c432d211805289
  area: nomenclature
  topic: Unresolved recipe-reference or truncated-concentration synonyms
  outcome: concern
  summary: 'Historical tokens are still present on the exact-subject SSSOM rows: [{"reason":"unresolved
    recipe cross-reference in a resolving synonym","token":"Trace elements (see below)"}].
    Truncated concentration strings and context-dependent instructions need scoped
    curation. This check does not reject catalog/RAW_TEXT synonyms as a class.'
  target_ids:
  - record-797da68010f27377
  evidence_ids:
  - ev-ee7e48ee832f8a11
  - ev-42f981730201a7f4
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-ee7e48ee832f8a11
    - ev-42f981730201a7f4
- assessment_id: scope-f-320ccfb6bddc74ee
  area: nomenclature
  topic: Certainty correction for the exact token observation
  outcome: unknown
  summary: Token presence remains reproducible, but the earlier pattern-based observation
    did not establish whether the exact source label denotes this subject or a different
    preparation. Fresh source-context adjudication is required before a confirmed
    defect or label removal. This successor corrects certainty only; it does not establish
    that the token is valid or that another identity allegation is fixed.
  target_ids:
  - record-797da68010f27377
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-9477d91976d0a888
  - ev-4d30788725c98994
  - ev-a255c9d3059064fe
  - ev-e7674a969ec8d8cb
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Source-scope question only, not a disposition of the complete historical
      report.
    evidence_ids:
    - ev-823412d1eacb6795
    - ev-9477d91976d0a888
    - ev-4d30788725c98994
    - ev-a255c9d3059064fe
    - ev-e7674a969ec8d8cb
- assessment_id: a-role-797da68010f27377
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Current role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence lists and require source-backed curation support.
  target_ids:
  - record-797da68010f27377
  evidence_ids:
  - ev-d6439cb28de651aa
  - ev-f700de79d37b3937
  dimensions:
  - name: legacy-disposition
    value: still_present
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-d6439cb28de651aa
    - ev-f700de79d37b3937
findings:
- finding_id: rec-scope-f-320ccfb6bddc74ee
  issue_key: mim-reconciliation-exported-context-tokens-797da68010f27377
  category: nomenclature
  severity: major
  status: deferred
  certainty: provisional
  title: 'Adjudicate source scope of exported tokens: Desulfovibrio trace elements'
  description: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed.
  target_ids:
  - record-797da68010f27377
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-9477d91976d0a888
  - ev-4d30788725c98994
  - ev-a255c9d3059064fe
  - ev-e7674a969ec8d8cb
  - ev-f9a3b6f8e2a4ef2f
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml
    role: maintained ingredient
  field_paths:
  - synonyms
  - SSSOM.other
  tags:
  - reconciliation
  - bundle-by-owner
  - exported-context-tokens
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/861
  disposition_reason: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed.
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T030852Z-mim-token-scope-reassessment
    finding_id: scope-f-320ccfb6bddc74ee
- finding_id: rec-f-role-797da68010f27377
  issue_key: mim-reconciliation-role-support-797da68010f27377
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only or empty role support: Desulfovibrio_Trace_Elements'
  description: Prediction-only or empty evidence payloads remain on the named current
    role assertions (nutritional_roles[0]). This confirms the local evidence gap,
    not that the biological role is false.
  target_ids:
  - record-797da68010f27377
  evidence_ids:
  - ev-d6439cb28de651aa
  - ev-f700de79d37b3937
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[0]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
actions:
- action_id: rec-act-role-797da68010f27377
  description: 'Reassess prediction-only or empty role support: Desulfovibrio_Trace_Elements'
  finding_ids:
  - rec-f-role-797da68010f27377
  target_ids:
  - record-797da68010f27377
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml
    role: maintained ingredient
  acceptance_checks:
  - Address the exact role fields and evidence gap described in this finding; preserve
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
  with lineage to 20261011T024633Z-mim-reconcile-all-batch-05, 20261011T030852Z-mim-token-scope-reassessment.
```
