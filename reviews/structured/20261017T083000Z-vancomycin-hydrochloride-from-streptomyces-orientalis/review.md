# Per-record structured review: Vancomycin_Hydrochloride_From_Streptomyces_Orientalis (data/ingredients/mapped/Vancomycin_Hydrochloride_From_Streptomyces_Orientalis.yaml)

- Review: 20261017T083000Z-vancomycin-hydrochloride-from-streptomyces-orientalis
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Vancomycin_Hydrochloride_From_Streptomyces_Orientalis (data/ingredients/mapped/Vancomycin_Hydrochloride_From_Streptomyces_Orientalis.yaml, record-ec3136d3e9fcab8a, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Vancomycin_Hydrochloride_From_Streptomyces_Orientalis.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Vancomycin_Hydrochloride_From_Streptomyces_Orientalis.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-ec3136d3e9fcab8a | data/ingredients/mapped/Vancomycin_Hydrochloride_From_Streptomyces_Orientalis.yaml | maintained | Vancomycin_Hydrochloride_From_Streptomyces_Orientalis |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-ec3136d3e9fcab8a | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-ec3136d3e9fcab8a | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-ec3136d3e9fcab8a | Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-ec3136d3e9fcab8a.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-ec3136d3e9fcab8a.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T20:45:28Z; reviewed SHA-256=1ec3918aaaebfd97d87d712c6539cbdad0a1f063169aed25e7fd0778a438692b; current SHA-256=1ec3918aaaebfd97d87d712c6539cbdad0a1f063169aed25e7fd0778a438692b; hash_changed=False. Reports=["reports/yaml_record_review/Vancomycin_Hydrochloride_From_Streptomyces_Orientalis.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The hydrochloride identity passes, but SELECTIVE_AGENT is provisional and final SSSOM exports a hydrate label on the anhydrous exact row.

### Historical provisional-role concern

evidence: concern. Targets: record-ec3136d3e9fcab8a.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-967295d06670c876: Reassess prediction-only role support: Vancomycin Hydrochloride from Streptomyces orientalis

major / open / confirmed; issue key: mim-reconciliation-role-support-ec3136d3e9fcab8a.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-967295d06670c876

Reassess prediction-only role support: Vancomycin Hydrochloride from Streptomyces orientalis

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-ca0df222216ab0ae | data/ingredients/mapped/Vancomycin_Hydrochloride_From_Streptomyces_Orientalis.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2034],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:9932","line":2036,"mapping_status":"MAPPED","ontology_id":"CHEBI:9932","preferred_term":"Vancomycin Hydrochloride from Streptomyces orientalis"}],"identifier":"CHEBI:9932","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:9932","ontology_label":"Vancomycin hydrochloride","ontology_source":"CHEBI"},"preferred_term":"Vancomycin Hydrochloride from Streptomyces orientalis","sssom_rows":[{"data_row":2885,"object_id":"CHEBI:9932","object_label":"Vancomycin hydrochloride","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Vancomycin_Hydrochloride_From_Streptomyces_Orientalis","synonym_count":1} |
| ev-02d1568d9ca43fed | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2034] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-c7ee1bff9f09963d | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Vancomycin_Hydrochloride_From_Streptomyces_Orientalis; data-row positions=[2885] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2885,"object_id":"CHEBI:9932","object_label":"Vancomycin hydrochloride","other":"Vancomycin Hydrochloride Hydrate&#124;Vancomycin x HCl&#124;CAS:1404-93-9","predicate_id":"skos:exactMatch","subject_id":"MIM:Vancomycin_Hydrochloride_From_Streptomyces_Orientalis","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-c2dc6f580d971db0 | docs/data/mapped_ingredients.csv; CSV lines=[2036] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:9932","line":2036,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"2","ontology_id":"CHEBI:9932","preferred_term":"Vancomycin Hydrochloride from Streptomyces orientalis","total_occurrences":"2"}] |
| ev-bdd490671b736729 | reports/yaml_record_review/Vancomycin_Hydrochloride_From_Streptomyces_Orientalis.md; &#96;data/ingredients/mapped/Vancomycin_Hydrochloride_From_Streptomyces_Orientalis.yaml&#96;:2; Verdict:4; Identity:11; Validation:25; Evidence:36; Issues:44; Completeness:54; Recommended Edits:61 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-86b080433dfa6410 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1334,1910] | context_only | [{"current_record_sha256":"1ec3918aaaebfd97d87d712c6539cbdad0a1f063169aed25e7fd0778a438692b","finding_id":"SEM:79ea0aa9729765e202bc","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"1ec3918aaaebfd97d87d712c6539cbdad0a1f063169aed25e7fd0778a438692b","finding_id":"SEM:d8b61f52d9d23a689323","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-79aa36e9f3ff6a40 | data/ingredients/mapped/Vancomycin_Hydrochloride_From_Streptomyces_Orientalis.yaml; physicochemical_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}] |
| ev-dbca56b9a4097d25 | reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml; findings[finding_id=f-967295d06670c876] | context_only | Predecessor structured review finding f-967295d06670c876 in 20261011T024639Z-mim-reconcile-all-batch-12 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024639Z-mim-reconcile-all-batch-12.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-vancomycin-hydrochloride-from-streptomyces-orientalis
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Vancomycin_Hydrochloride_From_Streptomyces_Orientalis
  (data/ingredients/mapped/Vancomycin_Hydrochloride_From_Streptomyces_Orientalis.yaml)'
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
summary: Per-record structured review for Vancomycin_Hydrochloride_From_Streptomyces_Orientalis
  (data/ingredients/mapped/Vancomycin_Hydrochloride_From_Streptomyces_Orientalis.yaml,
  record-ec3136d3e9fcab8a, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Vancomycin_Hydrochloride_From_Streptomyces_Orientalis.yaml
    sha256: 1ec3918aaaebfd97d87d712c6539cbdad0a1f063169aed25e7fd0778a438692b
    role: target
  - path: reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml
    sha256: 20e55e956f704a8c90164bf2749b9ddf6c35d94cdcbab538776d0675aa150899
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
  - path: reports/yaml_record_review/Vancomycin_Hydrochloride_From_Streptomyces_Orientalis.md
    sha256: 4a556265ece74b5c22cde69f16befcfd2206f17f633e55bc0da76d97007c4737
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-ec3136d3e9fcab8a
  path: data/ingredients/mapped/Vancomycin_Hydrochloride_From_Streptomyces_Orientalis.yaml
  label: Vancomycin_Hydrochloride_From_Streptomyces_Orientalis
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Vancomycin_Hydrochloride_From_Streptomyces_Orientalis.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Vancomycin_Hydrochloride_From_Streptomyces_Orientalis.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Vancomycin_Hydrochloride_From_Streptomyces_Orientalis.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-ec3136d3e9fcab8a
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-ec3136d3e9fcab8a
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-ec3136d3e9fcab8a
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12
    and semantic review dispositions on HEAD.
  target_ids:
  - record-ec3136d3e9fcab8a
evidence:
- evidence_id: ev-ca0df222216ab0ae
  kind: record_content
  reference: data/ingredients/mapped/Vancomycin_Hydrochloride_From_Streptomyces_Orientalis.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2034],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:9932","line":2036,"mapping_status":"MAPPED","ontology_id":"CHEBI:9932","preferred_term":"Vancomycin
    Hydrochloride from Streptomyces orientalis"}],"identifier":"CHEBI:9932","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:9932","ontology_label":"Vancomycin
    hydrochloride","ontology_source":"CHEBI"},"preferred_term":"Vancomycin Hydrochloride
    from Streptomyces orientalis","sssom_rows":[{"data_row":2885,"object_id":"CHEBI:9932","object_label":"Vancomycin
    hydrochloride","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Vancomycin_Hydrochloride_From_Streptomyces_Orientalis","synonym_count":1}'
  snapshot_sha256: 1ec3918aaaebfd97d87d712c6539cbdad0a1f063169aed25e7fd0778a438692b
- evidence_id: ev-02d1568d9ca43fed
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2034]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-c7ee1bff9f09963d
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Vancomycin_Hydrochloride_From_Streptomyces_Orientalis; data-row
    positions=[2885]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2885,"object_id":"CHEBI:9932","object_label":"Vancomycin
    hydrochloride","other":"Vancomycin Hydrochloride Hydrate|Vancomycin x HCl|CAS:1404-93-9","predicate_id":"skos:exactMatch","subject_id":"MIM:Vancomycin_Hydrochloride_From_Streptomyces_Orientalis","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-c2dc6f580d971db0
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2036]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:9932","line":2036,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"2","ontology_id":"CHEBI:9932","preferred_term":"Vancomycin
    Hydrochloride from Streptomyces orientalis","total_occurrences":"2"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-bdd490671b736729
  kind: prior_review
  reference: reports/yaml_record_review/Vancomycin_Hydrochloride_From_Streptomyces_Orientalis.md
  locator: '`data/ingredients/mapped/Vancomycin_Hydrochloride_From_Streptomyces_Orientalis.yaml`:2;
    Verdict:4; Identity:11; Validation:25; Evidence:36; Issues:44; Completeness:54;
    Recommended Edits:61'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 4a556265ece74b5c22cde69f16befcfd2206f17f633e55bc0da76d97007c4737
  quote: "Issues:\n- Major: `physicochemical_roles.SELECTIVE_AGENT` rests on\n  `COMPUTATIONAL_PREDICTION`\
    \ evidence whose note says the name-pattern rule is\n  provisional and still needs\
    \ review.\n- Major: the final SSSOM exact row\n  `MIM:Vancomycin_Hydrochloride_From_Streptomyces_Orientalis\
    \ skos:exactMatch\n  CHEBI:9932` exports `Vancomycin Hydrochloride Hydrate` in\
    \ `other`. That text\n  names the distinct hydrate sibling, not the anhydrous\
    \ `CHEBI:9932` term.\n\nRecommended Edits:\n- Replace or remove\n  `data/ingredients/mapped/Vancomycin_Hydrochloride_From_Streptomyces_Orientalis.yaml`\n\
    \  `physicochemical_roles.SELECTIVE_AGENT`; keep it only if a maintained source\n\
    \  supports vancomycin hydrochloride as a selective agent in the specific media\n\
    \  records that use it.\n- Remove `Vancomycin Hydrochloride Hydrate` from the\
    \ SSSOM synonym enrichment\n  or hydrate-family allowance feeding `MIM:Vancomycin_Hydrochloride_From_Streptomyces_Orientalis`,\n\
    \  then rerun the SSSOM build and invariant checks."
- evidence_id: ev-86b080433dfa6410
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1334,1910]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"1ec3918aaaebfd97d87d712c6539cbdad0a1f063169aed25e7fd0778a438692b","finding_id":"SEM:79ea0aa9729765e202bc","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"1ec3918aaaebfd97d87d712c6539cbdad0a1f063169aed25e7fd0778a438692b","finding_id":"SEM:d8b61f52d9d23a689323","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-79aa36e9f3ff6a40
  kind: record_content
  reference: data/ingredients/mapped/Vancomycin_Hydrochloride_From_Streptomyces_Orientalis.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}]'
  snapshot_sha256: 1ec3918aaaebfd97d87d712c6539cbdad0a1f063169aed25e7fd0778a438692b
- evidence_id: ev-dbca56b9a4097d25
  kind: prior_review
  reference: reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml
  locator: findings[finding_id=f-967295d06670c876]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-967295d06670c876 in 20261011T024639Z-mim-reconcile-all-batch-12
  snapshot_sha256: 20e55e956f704a8c90164bf2749b9ddf6c35d94cdcbab538776d0675aa150899
assessments:
- assessment_id: a-d9b9be5c82179547
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-ec3136d3e9fcab8a
  evidence_ids:
  - ev-ca0df222216ab0ae
  - ev-02d1568d9ca43fed
  - ev-c7ee1bff9f09963d
  - ev-c2dc6f580d971db0
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-f6a8a7a4b33af6cb
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-ec3136d3e9fcab8a
  evidence_ids:
  - ev-bdd490671b736729
  - ev-ca0df222216ab0ae
  - ev-86b080433dfa6410
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T20:45:28Z;
    reviewed SHA-256=1ec3918aaaebfd97d87d712c6539cbdad0a1f063169aed25e7fd0778a438692b;
    current SHA-256=1ec3918aaaebfd97d87d712c6539cbdad0a1f063169aed25e7fd0778a438692b;
    hash_changed=False. Reports=["reports/yaml_record_review/Vancomycin_Hydrochloride_From_Streptomyces_Orientalis.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The hydrochloride
    identity passes, but SELECTIVE_AGENT is provisional and final SSSOM exports a
    hydrate label on the anhydrous exact row.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-bdd490671b736729
    - ev-ca0df222216ab0ae
  - name: legacy-native-ids
    value: '["SEM:79ea0aa9729765e202bc","SEM:d8b61f52d9d23a689323"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-ca0df222216ab0ae
    - ev-bdd490671b736729
    - ev-86b080433dfa6410
- assessment_id: a-79aa36e9f3ff6a40
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-ec3136d3e9fcab8a
  evidence_ids:
  - ev-bdd490671b736729
  - ev-79aa36e9f3ff6a40
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-bdd490671b736729
    - ev-79aa36e9f3ff6a40
findings:
- finding_id: rec-f-967295d06670c876
  issue_key: mim-reconciliation-role-support-ec3136d3e9fcab8a
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Vancomycin Hydrochloride from Streptomyces
    orientalis'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-ec3136d3e9fcab8a
  evidence_ids:
  - ev-bdd490671b736729
  - ev-79aa36e9f3ff6a40
  - ev-dbca56b9a4097d25
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Vancomycin_Hydrochloride_From_Streptomyces_Orientalis.yaml
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
    review_id: 20261011T024639Z-mim-reconcile-all-batch-12
    finding_id: f-967295d06670c876
actions:
- action_id: rec-action-967295d06670c876
  description: 'Reassess prediction-only role support: Vancomycin Hydrochloride from
    Streptomyces orientalis'
  finding_ids:
  - rec-f-967295d06670c876
  target_ids:
  - record-ec3136d3e9fcab8a
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Vancomycin_Hydrochloride_From_Streptomyces_Orientalis.yaml
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
  with lineage to 20261011T024639Z-mim-reconcile-all-batch-12.
```
