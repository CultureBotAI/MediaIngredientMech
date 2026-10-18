# Per-record structured review: 6-O-sialyllactose_Sodium_Salt (data/ingredients/mapped/6-O-sialyllactose_Sodium_Salt.yaml)

- Review: 20261017T083000Z-6-o-sialyllactose-sodium-salt
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for 6-O-sialyllactose_Sodium_Salt (data/ingredients/mapped/6-O-sialyllactose_Sodium_Salt.yaml, record-053c9832e6c9fcea, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/6-O-sialyllactose_Sodium_Salt.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/6-O-sialyllactose_Sodium_Salt.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-053c9832e6c9fcea | data/ingredients/mapped/6-O-sialyllactose_Sodium_Salt.yaml | maintained | 6-O-sialyllactose_Sodium_Salt |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-053c9832e6c9fcea | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-053c9832e6c9fcea | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-053c9832e6c9fcea | Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-053c9832e6c9fcea.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-053c9832e6c9fcea.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:01:10Z; reviewed SHA-256=252e3146582a0917fbc3827e3ef009885696d96a077b7f0ffdf48bd268cc598e; current SHA-256=252e3146582a0917fbc3827e3ef009885696d96a077b7f0ffdf48bd268cc598e; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050110Z-6-O-sialyllactose_Sodium_Salt.md","reports/yaml_record_review/6-O-sialyllactose_Sodium_Salt.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/6-O-sialyllactose_Sodium_Salt.md&#96; after the record changed from f2ddbc9dd0209c5ed904ebfa976bbc245cc84d951f57c4d0a91a6c10bad0ba41 to 252e3146582a0917fbc3827e3ef009885696d96a077b7f0ffdf48bd268cc598e; preserved the previous major finding floor pending targeted retirement.

### Historical provisional-role concern

evidence: concern. Targets: record-053c9832e6c9fcea.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-b0e32e07f311c273: Reassess prediction-only role support: 6'-O-sialyllactose sodium salt

major / open / confirmed; issue key: mim-reconciliation-role-support-053c9832e6c9fcea.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-b0e32e07f311c273

Reassess prediction-only role support: 6'-O-sialyllactose sodium salt

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-7360e916ff3a59ce | data/ingredients/mapped/6-O-sialyllactose_Sodium_Salt.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[417],"raw_equal":true},"docs_rows":[{"identifier":"cas:157574-76-0","line":419,"mapping_status":"MAPPED","ontology_id":"CHEBI:153372","preferred_term":"6'-O-sialyllactose sodium salt"}],"identifier":"cas:157574-76-0","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:153372","ontology_label":"5-acetamido-3,5-dideoxy-D-glycero-alpha-D-galacto-non-2-ulopyranonosyl-(2-&gt;6)-beta-D-galactopyranosyl-(1-&gt;4)-D-glucopyranose","ontology_source":"CHEBI"},"preferred_term":"6'-O-sialyllactose sodium salt","sssom_rows":[{"data_row":244,"object_id":"CHEBI:153372","object_label":"5-acetamido-3,5-dideoxy-D-glycero-alpha-D-galacto-non-2-ulopyranonosyl-(2-&gt;6)-beta-D-galactopyranosyl-(1-&gt;4)-D-glucopyranose","predicate_id":"skos:broadMatch"},{"data_row":245,"object_id":"cas:157574-76-0","object_label":"6'-O-sialyllactose sodium salt","predicate_id":"skos:exactMatch"},{"data_row":246,"object_id":"kgmicrobe.compound:6-o-sialyllactose_sodium_salt","object_label":"6'-O-sialyllactose sodium salt","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:6-O-sialyllactose_Sodium_Salt","synonym_count":0} |
| ev-648122a570e22199 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [417] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-667f82204a60fb43 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:6-O-sialyllactose_Sodium_Salt; data-row positions=[244, 245, 246] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":244,"object_id":"CHEBI:153372","object_label":"5-acetamido-3,5-dideoxy-D-glycero-alpha-D-galacto-non-2-ulopyranonosyl-(2-&gt;6)-beta-D-galactopyranosyl-(1-&gt;4)-D-glucopyranose","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:6-O-sialyllactose_Sodium_Salt","validation_method":"manual:reconcile_sssom&#124;REMAPPED&#124;2026-09-22"},{"data_row":245,"object_id":"cas:157574-76-0","object_label":"6'-O-sialyllactose sodium salt","other":"CAS:157574-76-0","predicate_id":"skos:exactMatch","subject_id":"MIM:6-O-sialyllactose_Sodium_Salt","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"},{"data_row":246,"object_id":"kgmicrobe.compound:6-o-sialyllactose_sodium_salt","object_label":"6'-O-sialyllactose sodium salt","other":"CAS:157574-76-0","predicate_id":"skos:exactMatch","subject_id":"MIM:6-O-sialyllactose_Sodium_Salt","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-6e00524711f706ac | docs/data/mapped_ingredients.csv; CSV lines=[419] | supports | Published identity and count rows inspected: [{"identifier":"cas:157574-76-0","line":419,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:153372","preferred_term":"6'-O-sialyllactose sodium salt","total_occurrences":"0"}] |
| ev-4b2f6079f8dff43c | reports/yaml_record_review/20261001T050110Z-6-O-sialyllactose_Sodium_Salt.md; YAML Record Review: 6'-O-sialyllactose sodium salt:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61; Additional Notes:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-3737f50800f48571 | reports/yaml_record_review/6-O-sialyllactose_Sodium_Salt.md; &#96;data/ingredients/mapped/6-O-sialyllactose_Sodium_Salt.yaml&#96;:2; Verdict:4; Identity:11; Validation:25; Evidence:37; Completeness:59; Recommended Edits:66 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-ecc0f0fa05e670f8 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[173,1859] | context_only | [{"current_record_sha256":"252e3146582a0917fbc3827e3ef009885696d96a077b7f0ffdf48bd268cc598e","finding_id":"SEM:6ba958600ac333926a57","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"252e3146582a0917fbc3827e3ef009885696d96a077b7f0ffdf48bd268cc598e","finding_id":"SEM:39877065ab9115b774cf","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-882af8654755192c | data/ingredients/mapped/6-O-sialyllactose_Sodium_Salt.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[417],"raw_equal":true},"docs_rows":[{"identifier":"cas:157574-76-0","line":419,"mapping_status":"MAPPED","ontology_id":"CHEBI:153372","preferred_term":"6'-O-sialyllactose sodium salt"}],"identifier":"cas:157574-76-0","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:153372","ontology_label":"5-acetamido-3,5-dideoxy-D-glycero-alpha-D-galacto-non-2-ulopyranonosyl-(2-&gt;6)-beta-D-galactopyranosyl-(1-&gt;4)-D-glucopyranose","ontology_source":"CHEBI"},"preferred_term":"6'-O-sialyllactose sodium salt","sssom_rows":[{"data_row":244,"object_id":"CHEBI:153372","object_label":"5-acetamido-3,5-dideoxy-D-glycero-alpha-D-galacto-non-2-ulopyranonosyl-(2-&gt;6)-beta-D-galactopyranosyl-(1-&gt;4)-D-glucopyranose","predicate_id":"skos:broadMatch"},{"data_row":245,"object_id":"cas:157574-76-0","object_label":"6'-O-sialyllactose sodium salt","predicate_id":"skos:exactMatch"},{"data_row":246,"object_id":"kgmicrobe.compound:6-o-sialyllactose_sodium_salt","object_label":"6'-O-sialyllactose sodium salt","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:6-O-sialyllactose_Sodium_Salt","synonym_count":0} |
| ev-50485f988d77b60f | reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml; findings[finding_id=f-b0e32e07f311c273] | context_only | Predecessor structured review finding f-b0e32e07f311c273 in 20261011T024630Z-mim-reconcile-all-batch-02 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-6-o-sialyllactose-sodium-salt
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: 6-O-sialyllactose_Sodium_Salt (data/ingredients/mapped/6-O-sialyllactose_Sodium_Salt.yaml)'
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
summary: Per-record structured review for 6-O-sialyllactose_Sodium_Salt (data/ingredients/mapped/6-O-sialyllactose_Sodium_Salt.yaml,
  record-053c9832e6c9fcea, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/6-O-sialyllactose_Sodium_Salt.yaml
    sha256: 252e3146582a0917fbc3827e3ef009885696d96a077b7f0ffdf48bd268cc598e
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
  - path: reports/yaml_record_review/20261001T050110Z-6-O-sialyllactose_Sodium_Salt.md
    sha256: 8183eacc70dc21b542bbfa374e26c4c64957a651c7043bd2a6af28cedb0bc42a
    role: context
  - path: reports/yaml_record_review/6-O-sialyllactose_Sodium_Salt.md
    sha256: 92cd44b1c506691508fa849336028c5ab3fe2b3fc51e5c2824446ac1f7c9390d
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-053c9832e6c9fcea
  path: data/ingredients/mapped/6-O-sialyllactose_Sodium_Salt.yaml
  label: 6-O-sialyllactose_Sodium_Salt
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/6-O-sialyllactose_Sodium_Salt.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/6-O-sialyllactose_Sodium_Salt.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/6-O-sialyllactose_Sodium_Salt.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-053c9832e6c9fcea
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-053c9832e6c9fcea
  evidence_ids:
  - ev-7360e916ff3a59ce
  - ev-648122a570e22199
  - ev-667f82204a60fb43
  - ev-6e00524711f706ac
  - ev-882af8654755192c
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-053c9832e6c9fcea
  evidence_ids:
  - ev-7360e916ff3a59ce
  - ev-ecc0f0fa05e670f8
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02
    and semantic review dispositions on HEAD.
  target_ids:
  - record-053c9832e6c9fcea
  evidence_ids:
  - ev-4b2f6079f8dff43c
  - ev-3737f50800f48571
  - ev-ecc0f0fa05e670f8
  - ev-50485f988d77b60f
evidence:
- evidence_id: ev-7360e916ff3a59ce
  kind: record_content
  reference: data/ingredients/mapped/6-O-sialyllactose_Sodium_Salt.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[417],"raw_equal":true},"docs_rows":[{"identifier":"cas:157574-76-0","line":419,"mapping_status":"MAPPED","ontology_id":"CHEBI:153372","preferred_term":"6''-O-sialyllactose
    sodium salt"}],"identifier":"cas:157574-76-0","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:153372","ontology_label":"5-acetamido-3,5-dideoxy-D-glycero-alpha-D-galacto-non-2-ulopyranonosyl-(2->6)-beta-D-galactopyranosyl-(1->4)-D-glucopyranose","ontology_source":"CHEBI"},"preferred_term":"6''-O-sialyllactose
    sodium salt","sssom_rows":[{"data_row":244,"object_id":"CHEBI:153372","object_label":"5-acetamido-3,5-dideoxy-D-glycero-alpha-D-galacto-non-2-ulopyranonosyl-(2->6)-beta-D-galactopyranosyl-(1->4)-D-glucopyranose","predicate_id":"skos:broadMatch"},{"data_row":245,"object_id":"cas:157574-76-0","object_label":"6''-O-sialyllactose
    sodium salt","predicate_id":"skos:exactMatch"},{"data_row":246,"object_id":"kgmicrobe.compound:6-o-sialyllactose_sodium_salt","object_label":"6''-O-sialyllactose
    sodium salt","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:6-O-sialyllactose_Sodium_Salt","synonym_count":0}'
  snapshot_sha256: 252e3146582a0917fbc3827e3ef009885696d96a077b7f0ffdf48bd268cc598e
- evidence_id: ev-648122a570e22199
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [417]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-667f82204a60fb43
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:6-O-sialyllactose_Sodium_Salt; data-row positions=[244,
    245, 246]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":244,"object_id":"CHEBI:153372","object_label":"5-acetamido-3,5-dideoxy-D-glycero-alpha-D-galacto-non-2-ulopyranonosyl-(2->6)-beta-D-galactopyranosyl-(1->4)-D-glucopyranose","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:6-O-sialyllactose_Sodium_Salt","validation_method":"manual:reconcile_sssom|REMAPPED|2026-09-22"},{"data_row":245,"object_id":"cas:157574-76-0","object_label":"6''-O-sialyllactose
    sodium salt","other":"CAS:157574-76-0","predicate_id":"skos:exactMatch","subject_id":"MIM:6-O-sialyllactose_Sodium_Salt","validation_method":"none|UNKNOWN_TERM|2026-07-07"},{"data_row":246,"object_id":"kgmicrobe.compound:6-o-sialyllactose_sodium_salt","object_label":"6''-O-sialyllactose
    sodium salt","other":"CAS:157574-76-0","predicate_id":"skos:exactMatch","subject_id":"MIM:6-O-sialyllactose_Sodium_Salt","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-6e00524711f706ac
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[419]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:157574-76-0","line":419,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:153372","preferred_term":"6''-O-sialyllactose
    sodium salt","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-4b2f6079f8dff43c
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050110Z-6-O-sialyllactose_Sodium_Salt.md
  locator: 'YAML Record Review: 6''-O-sialyllactose sodium salt:2; Target:10; Validation:20;
    Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended
    Edits:56; Follow-up Checks:61; Additional Notes:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 8183eacc70dc21b542bbfa374e26c4c64957a651c7043bd2a6af28cedb0bc42a
  quote: 'Findings:

    - **major**: The previous finding set in `reports/yaml_record_review/6-O-sialyllactose_Sodium_Salt.md`
    was tied to the prior record content; carry it forward as an unresolved curation
    floor until a targeted current review retires it. Previous summary: The local
    CAS identity, PubChem chemistry, and registry rows pass, but the ChEBI parent
    is the generic sodium salt class, SSSOM exports an unrelated propionate label,
    and the carbon-source role is provisional.


    Recommended Edits:

    - Resolve or explicitly retire the findings provisionally carried forward from
    `reports/yaml_record_review/6-O-sialyllactose_Sodium_Salt.md`.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/6-O-sialyllactose_Sodium_Salt.yaml`,
    `just validate-terms data/ingredients/mapped/6-O-sialyllactose_Sodium_Salt.yaml`
    where applicable, and `just qc-sssom`.'
- evidence_id: ev-3737f50800f48571
  kind: prior_review
  reference: reports/yaml_record_review/6-O-sialyllactose_Sodium_Salt.md
  locator: '`data/ingredients/mapped/6-O-sialyllactose_Sodium_Salt.yaml`:2; Verdict:4;
    Identity:11; Validation:25; Evidence:37; Completeness:59; Recommended Edits:66'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 92cd44b1c506691508fa849336028c5ab3fe2b3fc51e5c2824446ac1f7c9390d
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/6-O-sialyllactose_Sodium_Salt.yaml`,\
    \ replace\n  `CHEBI:26714` with a chemically relevant parent if one exists, or\
    \ drop the\n  ChEBI parent and keep only the local CAS and kg-microbe exact registry\
    \ rows.\n- Remove the stale `Propionate (sodium salt)` SSSOM `other` value at\
    \ its\n  maintained source, and add exact source-backed synonyms such as\n  `6'-Sialyllactose\
    \ sodium salt` only if they come from a maintained YAML\n  synonym entry.\n- Remove\
    \ or evidence the provisional `CARBON_SOURCE` role, then rebuild\n  `mappings/ingredient_mappings.sssom.tsv`\
    \ and\n  `data/curated/mapped_ingredients.yaml` and rerun strict validation, SSSOM\n\
    \  invariants, and the id/label correspondence gate."
- evidence_id: ev-ecc0f0fa05e670f8
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[173,1859]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"252e3146582a0917fbc3827e3ef009885696d96a077b7f0ffdf48bd268cc598e","finding_id":"SEM:6ba958600ac333926a57","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"252e3146582a0917fbc3827e3ef009885696d96a077b7f0ffdf48bd268cc598e","finding_id":"SEM:39877065ab9115b774cf","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-882af8654755192c
  kind: record_content
  reference: data/ingredients/mapped/6-O-sialyllactose_Sodium_Salt.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[417],"raw_equal":true},"docs_rows":[{"identifier":"cas:157574-76-0","line":419,"mapping_status":"MAPPED","ontology_id":"CHEBI:153372","preferred_term":"6''-O-sialyllactose
    sodium salt"}],"identifier":"cas:157574-76-0","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:153372","ontology_label":"5-acetamido-3,5-dideoxy-D-glycero-alpha-D-galacto-non-2-ulopyranonosyl-(2->6)-beta-D-galactopyranosyl-(1->4)-D-glucopyranose","ontology_source":"CHEBI"},"preferred_term":"6''-O-sialyllactose
    sodium salt","sssom_rows":[{"data_row":244,"object_id":"CHEBI:153372","object_label":"5-acetamido-3,5-dideoxy-D-glycero-alpha-D-galacto-non-2-ulopyranonosyl-(2->6)-beta-D-galactopyranosyl-(1->4)-D-glucopyranose","predicate_id":"skos:broadMatch"},{"data_row":245,"object_id":"cas:157574-76-0","object_label":"6''-O-sialyllactose
    sodium salt","predicate_id":"skos:exactMatch"},{"data_row":246,"object_id":"kgmicrobe.compound:6-o-sialyllactose_sodium_salt","object_label":"6''-O-sialyllactose
    sodium salt","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:6-O-sialyllactose_Sodium_Salt","synonym_count":0}'
  snapshot_sha256: 252e3146582a0917fbc3827e3ef009885696d96a077b7f0ffdf48bd268cc598e
- evidence_id: ev-50485f988d77b60f
  kind: prior_review
  reference: reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml
  locator: findings[finding_id=f-b0e32e07f311c273]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-b0e32e07f311c273 in 20261011T024630Z-mim-reconcile-all-batch-02
  snapshot_sha256: 799a1a80fa398851bced286dd0f68a97e6a22f7090d53677678dc13b92c6f076
assessments:
- assessment_id: a-e0d1b62e26a76b15
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-053c9832e6c9fcea
  evidence_ids:
  - ev-7360e916ff3a59ce
  - ev-648122a570e22199
  - ev-667f82204a60fb43
  - ev-6e00524711f706ac
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-a3c5578d9ef95b69
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-053c9832e6c9fcea
  evidence_ids:
  - ev-4b2f6079f8dff43c
  - ev-3737f50800f48571
  - ev-7360e916ff3a59ce
  - ev-ecc0f0fa05e670f8
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:01:10Z;
    reviewed SHA-256=252e3146582a0917fbc3827e3ef009885696d96a077b7f0ffdf48bd268cc598e;
    current SHA-256=252e3146582a0917fbc3827e3ef009885696d96a077b7f0ffdf48bd268cc598e;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050110Z-6-O-sialyllactose_Sodium_Salt.md","reports/yaml_record_review/6-O-sialyllactose_Sodium_Salt.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/6-O-sialyllactose_Sodium_Salt.md` after the record
    changed from f2ddbc9dd0209c5ed904ebfa976bbc245cc84d951f57c4d0a91a6c10bad0ba41
    to 252e3146582a0917fbc3827e3ef009885696d96a077b7f0ffdf48bd268cc598e; preserved
    the previous major finding floor pending targeted retirement.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-4b2f6079f8dff43c
    - ev-3737f50800f48571
    - ev-7360e916ff3a59ce
  - name: legacy-native-ids
    value: '["SEM:6ba958600ac333926a57","SEM:39877065ab9115b774cf"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-7360e916ff3a59ce
    - ev-4b2f6079f8dff43c
    - ev-3737f50800f48571
    - ev-ecc0f0fa05e670f8
- assessment_id: a-882af8654755192c
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-053c9832e6c9fcea
  evidence_ids:
  - ev-4b2f6079f8dff43c
  - ev-3737f50800f48571
  - ev-882af8654755192c
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-4b2f6079f8dff43c
    - ev-3737f50800f48571
    - ev-882af8654755192c
findings:
- finding_id: rec-f-b0e32e07f311c273
  issue_key: mim-reconciliation-role-support-053c9832e6c9fcea
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: 6''-O-sialyllactose sodium salt'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-053c9832e6c9fcea
  evidence_ids:
  - ev-4b2f6079f8dff43c
  - ev-3737f50800f48571
  - ev-882af8654755192c
  - ev-50485f988d77b60f
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/6-O-sialyllactose_Sodium_Salt.yaml
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
    review_id: 20261011T024630Z-mim-reconcile-all-batch-02
    finding_id: f-b0e32e07f311c273
actions:
- action_id: rec-action-b0e32e07f311c273
  description: 'Reassess prediction-only role support: 6''-O-sialyllactose sodium
    salt'
  finding_ids:
  - rec-f-b0e32e07f311c273
  target_ids:
  - record-053c9832e6c9fcea
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/6-O-sialyllactose_Sodium_Salt.yaml
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
