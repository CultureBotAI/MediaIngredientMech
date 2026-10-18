# Per-record structured review: L-Glutamic_Acid_Monopotassium_Salt_Monohydrate (data/ingredients/mapped/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.yaml)

- Review: 20261017T083000Z-l-glutamic-acid-monopotassium-salt-monohydrate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for L-Glutamic_Acid_Monopotassium_Salt_Monohydrate (data/ingredients/mapped/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.yaml, record-56516b17e8993494, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-56516b17e8993494 | data/ingredients/mapped/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.yaml | maintained | L-Glutamic_Acid_Monopotassium_Salt_Monohydrate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-56516b17e8993494 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-56516b17e8993494 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-56516b17e8993494 | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-56516b17e8993494.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-56516b17e8993494.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:02:35Z; reviewed SHA-256=0026680a282b367ec2a228dcc4f04e70aec4ed812ca8629652e0137838b9636e; current SHA-256=0026680a282b367ec2a228dcc4f04e70aec4ed812ca8629652e0137838b9636e; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050235Z-L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.md","reports/yaml_record_review/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.md&#96; after the record changed from b81046e7b35a714c71af86de076d1c15c18c454eafce07e5b3508935b3c0cc9d to 0026680a282b367ec2a228dcc4f04e70aec4ed812ca8629652e0137838b9636e; preserved the previous major finding floor pending targeted retirement.

### Historical provisional-role concern

evidence: concern. Targets: record-56516b17e8993494.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-d4446fbf321814e9: Reassess prediction-only role support: L-Glutamic acid monopotassium salt monohydrate

major / open / confirmed; issue key: mim-reconciliation-role-support-56516b17e8993494.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-d4446fbf321814e9

Reassess prediction-only role support: L-Glutamic acid monopotassium salt monohydrate

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-d053240a3df37a39 | data/ingredients/mapped/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1223],"raw_equal":true},"docs_rows":[{"identifier":"cas:6382-01-0","line":1225,"mapping_status":"MAPPED","ontology_id":"CHEBI:16015","preferred_term":"L-Glutamic acid monopotassium salt monohydrate"}],"identifier":"cas:6382-01-0","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":16,"edge_count":16,"occurrences":16},"occurrence_statistics":{"media_count":16,"total_occurrences":16},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:16015","ontology_label":"L-glutamic acid","ontology_source":"CHEBI"},"preferred_term":"L-Glutamic acid monopotassium salt monohydrate","sssom_rows":[{"data_row":1573,"object_id":"CHEBI:16015","object_label":"L-glutamic acid","predicate_id":"skos:closeMatch"},{"data_row":1574,"object_id":"cas:6382-01-0","object_label":"L-Glutamic acid monopotassium salt monohydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-Glutamic_Acid_Monopotassium_Salt_Monohydrate","synonym_count":3} |
| ev-69568114dc23d52a | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1223] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-3a3b9f2f6a49f55b | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:L-Glutamic_Acid_Monopotassium_Salt_Monohydrate; data-row positions=[1573,1574] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1573,"object_id":"CHEBI:16015","object_label":"L-glutamic acid","other":"L-Glutamic acid potassium salt monohydrate, L-Glutamic acid potassium salt&#124;CAS:6382-01-0","predicate_id":"skos:closeMatch","subject_id":"MIM:L-Glutamic_Acid_Monopotassium_Salt_Monohydrate","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"},{"data_row":1574,"object_id":"cas:6382-01-0","object_label":"L-Glutamic acid monopotassium salt monohydrate","other":"CAS:6382-01-0","predicate_id":"skos:exactMatch","subject_id":"MIM:L-Glutamic_Acid_Monopotassium_Salt_Monohydrate","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-40093ae55be88afb | docs/data/mapped_ingredients.csv; CSV lines=[1225] | supports | Published identity and count rows inspected: [{"identifier":"cas:6382-01-0","line":1225,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"16","ontology_id":"CHEBI:16015","preferred_term":"L-Glutamic acid monopotassium salt monohydrate","total_occurrences":"16"}] |
| ev-c76156df1c57a404 | reports/yaml_record_review/20261001T050235Z-L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.md; YAML Record Review: L-Glutamic acid monopotassium salt monohydrate:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61; Additional Notes:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-e0890a44575c5ab6 | reports/yaml_record_review/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.md; &#96;data/ingredients/mapped/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.yaml&#96;:2; Verdict:4; Identity:12; Validation:23; Evidence:34; Completeness:67; Recommended Edits:77 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-f0b3b22c8d35b7eb | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[790,1820] | context_only | [{"current_record_sha256":"0026680a282b367ec2a228dcc4f04e70aec4ed812ca8629652e0137838b9636e","finding_id":"SEM:2278e3d9e996777632c3","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"0026680a282b367ec2a228dcc4f04e70aec4ed812ca8629652e0137838b9636e","finding_id":"SEM:003bcfa57643badb2a69","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-46dfb072057ddcf5 | data/ingredients/mapped/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"AMINO_ACID_SOURCE"}}] |
| ev-d3081a7e9ae0f84f | reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml; findings[finding_id=f-d4446fbf321814e9] | context_only | Predecessor structured review finding f-d4446fbf321814e9 in 20261011T024635Z-mim-reconcile-all-batch-07 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-l-glutamic-acid-monopotassium-salt-monohydrate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: L-Glutamic_Acid_Monopotassium_Salt_Monohydrate
  (data/ingredients/mapped/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.yaml)'
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
summary: Per-record structured review for L-Glutamic_Acid_Monopotassium_Salt_Monohydrate
  (data/ingredients/mapped/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.yaml, record-56516b17e8993494,
  mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound
  to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.yaml
    sha256: 0026680a282b367ec2a228dcc4f04e70aec4ed812ca8629652e0137838b9636e
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
  - path: reports/yaml_record_review/20261001T050235Z-L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.md
    sha256: 14bc7bedad4be78774ad76c31c2bb9435fbfd1ee315f686f11289b911b99beb2
    role: context
  - path: reports/yaml_record_review/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.md
    sha256: 8ff876ad33e7018fcef3e41499487eea75b19734285ad0b0afcbaaf5d3466ca5
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-56516b17e8993494
  path: data/ingredients/mapped/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.yaml
  label: L-Glutamic_Acid_Monopotassium_Salt_Monohydrate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-56516b17e8993494
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-56516b17e8993494
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-56516b17e8993494
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-56516b17e8993494
evidence:
- evidence_id: ev-d053240a3df37a39
  kind: record_content
  reference: data/ingredients/mapped/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1223],"raw_equal":true},"docs_rows":[{"identifier":"cas:6382-01-0","line":1225,"mapping_status":"MAPPED","ontology_id":"CHEBI:16015","preferred_term":"L-Glutamic
    acid monopotassium salt monohydrate"}],"identifier":"cas:6382-01-0","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":16,"edge_count":16,"occurrences":16},"occurrence_statistics":{"media_count":16,"total_occurrences":16},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:16015","ontology_label":"L-glutamic
    acid","ontology_source":"CHEBI"},"preferred_term":"L-Glutamic acid monopotassium
    salt monohydrate","sssom_rows":[{"data_row":1573,"object_id":"CHEBI:16015","object_label":"L-glutamic
    acid","predicate_id":"skos:closeMatch"},{"data_row":1574,"object_id":"cas:6382-01-0","object_label":"L-Glutamic
    acid monopotassium salt monohydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-Glutamic_Acid_Monopotassium_Salt_Monohydrate","synonym_count":3}'
  snapshot_sha256: 0026680a282b367ec2a228dcc4f04e70aec4ed812ca8629652e0137838b9636e
- evidence_id: ev-69568114dc23d52a
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1223]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-3a3b9f2f6a49f55b
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:L-Glutamic_Acid_Monopotassium_Salt_Monohydrate; data-row
    positions=[1573,1574]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1573,"object_id":"CHEBI:16015","object_label":"L-glutamic
    acid","other":"L-Glutamic acid potassium salt monohydrate, L-Glutamic acid potassium
    salt|CAS:6382-01-0","predicate_id":"skos:closeMatch","subject_id":"MIM:L-Glutamic_Acid_Monopotassium_Salt_Monohydrate","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"},{"data_row":1574,"object_id":"cas:6382-01-0","object_label":"L-Glutamic
    acid monopotassium salt monohydrate","other":"CAS:6382-01-0","predicate_id":"skos:exactMatch","subject_id":"MIM:L-Glutamic_Acid_Monopotassium_Salt_Monohydrate","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-40093ae55be88afb
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1225]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:6382-01-0","line":1225,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"16","ontology_id":"CHEBI:16015","preferred_term":"L-Glutamic
    acid monopotassium salt monohydrate","total_occurrences":"16"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-c76156df1c57a404
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050235Z-L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.md
  locator: 'YAML Record Review: L-Glutamic acid monopotassium salt monohydrate:2;
    Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46;
    Findings:52; Recommended Edits:56; Follow-up Checks:61; Additional Notes:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 14bc7bedad4be78774ad76c31c2bb9435fbfd1ee315f686f11289b911b99beb2
  quote: 'Findings:

    - **major**: The previous finding set in `reports/yaml_record_review/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.md`
    was tied to the prior record content; carry it forward as an unresolved curation
    floor until a targeted current review retires it. Previous summary: The CAS primary
    identity, PubChem monohydrate structure, close parent, exact CAS row, and hydrate
    review pass, but the local registry anchor is missing, parent synonyms publish,
    and AMINO_ACID_SOURCE is provisional.


    Recommended Edits:

    - Resolve or explicitly retire the findings provisionally carried forward from
    `reports/yaml_record_review/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.md`.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.yaml`,
    `just validate-terms data/ingredients/mapped/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.yaml`
    where applicable, and `just qc-sssom`.'
- evidence_id: ev-e0890a44575c5ab6
  kind: prior_review
  reference: reports/yaml_record_review/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.md
  locator: '`data/ingredients/mapped/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.yaml`:2;
    Verdict:4; Identity:12; Validation:23; Evidence:34; Completeness:67; Recommended
    Edits:77'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 8ff876ad33e7018fcef3e41499487eea75b19734285ad0b0afcbaaf5d3466ca5
  quote: "Recommended Edits:\n- Major: repair final SSSOM generation for this CAS-primary\
    \ close-match hydrate\n  so `MIM:L-Glutamic_Acid_Monopotassium_Salt_Monohydrate`\
    \ receives an exact\n  local `kgmicrobe.compound:l-glutamic_acid_monopotassium_salt_monohydrate`\
    \ row\n  alongside the close parent and exact CAS rows.\n- Major: split or demote\
    \ the comma-joined salt synonym and remove parent\n  L-glutamic acid synonyms\
    \ from\n  `data/ingredients/mapped/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.yaml`;\n\
    \  only labels for the monopotassium salt monohydrate should publish on the\n\
    \  parent SSSOM row.\n- Major: remove `nutritional_roles.AMINO_ACID_SOURCE` unless\
    \ an inspected\n  CultureMech, FEBA, Hans80, or literature source can support\
    \ L-glutamic acid\n  monopotassium salt monohydrate as an amino acid source.\n\
    - Rerun strict, term, hydrate, round-trip, role, component, and SSSOM validation\n\
    \  after those changes."
- evidence_id: ev-f0b3b22c8d35b7eb
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[790,1820]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"0026680a282b367ec2a228dcc4f04e70aec4ed812ca8629652e0137838b9636e","finding_id":"SEM:2278e3d9e996777632c3","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"0026680a282b367ec2a228dcc4f04e70aec4ed812ca8629652e0137838b9636e","finding_id":"SEM:003bcfa57643badb2a69","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-46dfb072057ddcf5
  kind: record_content
  reference: data/ingredients/mapped/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"AMINO_ACID_SOURCE"}}]'
  snapshot_sha256: 0026680a282b367ec2a228dcc4f04e70aec4ed812ca8629652e0137838b9636e
- evidence_id: ev-d3081a7e9ae0f84f
  kind: prior_review
  reference: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
  locator: findings[finding_id=f-d4446fbf321814e9]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-d4446fbf321814e9 in 20261011T024635Z-mim-reconcile-all-batch-07
  snapshot_sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
assessments:
- assessment_id: a-271494fbce820fb5
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-56516b17e8993494
  evidence_ids:
  - ev-d053240a3df37a39
  - ev-69568114dc23d52a
  - ev-3a3b9f2f6a49f55b
  - ev-40093ae55be88afb
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-d15f5bd561a2b31d
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-56516b17e8993494
  evidence_ids:
  - ev-c76156df1c57a404
  - ev-e0890a44575c5ab6
  - ev-d053240a3df37a39
  - ev-f0b3b22c8d35b7eb
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:02:35Z;
    reviewed SHA-256=0026680a282b367ec2a228dcc4f04e70aec4ed812ca8629652e0137838b9636e;
    current SHA-256=0026680a282b367ec2a228dcc4f04e70aec4ed812ca8629652e0137838b9636e;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050235Z-L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.md","reports/yaml_record_review/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.md`
    after the record changed from b81046e7b35a714c71af86de076d1c15c18c454eafce07e5b3508935b3c0cc9d
    to 0026680a282b367ec2a228dcc4f04e70aec4ed812ca8629652e0137838b9636e; preserved
    the previous major finding floor pending targeted retirement.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-c76156df1c57a404
    - ev-e0890a44575c5ab6
    - ev-d053240a3df37a39
  - name: legacy-native-ids
    value: '["SEM:2278e3d9e996777632c3","SEM:003bcfa57643badb2a69"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-d053240a3df37a39
    - ev-c76156df1c57a404
    - ev-e0890a44575c5ab6
    - ev-f0b3b22c8d35b7eb
- assessment_id: a-46dfb072057ddcf5
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-56516b17e8993494
  evidence_ids:
  - ev-c76156df1c57a404
  - ev-e0890a44575c5ab6
  - ev-46dfb072057ddcf5
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-c76156df1c57a404
    - ev-e0890a44575c5ab6
    - ev-46dfb072057ddcf5
findings:
- finding_id: rec-f-d4446fbf321814e9
  issue_key: mim-reconciliation-role-support-56516b17e8993494
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: L-Glutamic acid monopotassium salt
    monohydrate'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-56516b17e8993494
  evidence_ids:
  - ev-c76156df1c57a404
  - ev-e0890a44575c5ab6
  - ev-46dfb072057ddcf5
  - ev-d3081a7e9ae0f84f
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.yaml
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
    review_id: 20261011T024635Z-mim-reconcile-all-batch-07
    finding_id: f-d4446fbf321814e9
actions:
- action_id: rec-action-d4446fbf321814e9
  description: 'Reassess prediction-only role support: L-Glutamic acid monopotassium
    salt monohydrate'
  finding_ids:
  - rec-f-d4446fbf321814e9
  target_ids:
  - record-56516b17e8993494
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.yaml
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
