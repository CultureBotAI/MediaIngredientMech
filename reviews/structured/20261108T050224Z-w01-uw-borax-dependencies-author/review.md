# Worker01 three UW borax dependency proposals

- Review: 20261108T050224Z-w01-uw-borax-dependencies-author
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-11-08T05:02:24.105588Z
- Finished UTC: 2026-11-08T05:02:24.452877Z
- Reviewer: /root/issue_context (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Source-verified decahydrate parts follow the corrected CHEBI38888 owner in all3 UW stocks. Native whole-catalog regression and strict schema pass; unrelated inherited formulation and role assertions are not approved.

## Scope And Provenance

All3 dependent UW records and exact proposed changes, with original primary Mixes rows and structural borax correspondence.

Selection: Exact3 maintained MIM_CATALOG references orphaned by KG26-PROP-175-STRUCTURAL-IDENTITY in issue1168.
Coverage: full; 3 reviewed / 3 in the declared population.
Source: working_tree at Git base 58d67db32a86a359869819624568d625e7051358.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| kgmicrobe.ingredient:uw_concentrated_base | reports/all_unmatched_20261107/worker-01/shard/root_substances/kg26/proposals/UW_Concentrated_Base-borax-dependency-v2.yaml | source | UW concentrated base |
| kgmicrobe.ingredient:uw_concentrated_base_no_mo | reports/all_unmatched_20261107/worker-01/shard/root_substances/kg26/proposals/UW_Concentrated_Base_No_Mo-borax-dependency-v2.yaml | source | UW concentrated base no Mo |
| kgmicrobe.ingredient:uw_concentrated_base_no_sulfur | reports/all_unmatched_20261107/worker-01/shard/root_substances/kg26/proposals/UW_Concentrated_Base_No_Sulfur-borax-dependency-v2.yaml | source | UW concentrated base no sulfur |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Primary component identity and structural correspondence | passed | True | kgmicrobe.ingredient:uw_concentrated_base, kgmicrobe.ingredient:uw_concentrated_base_no_mo, kgmicrobe.ingredient:uw_concentrated_base_no_sulfur | Exact source rows and complete records reviewed; supplied borax identity matches corrected owner. |
| Exact rollback and native validated writes | passed | True | kgmicrobe.ingredient:uw_concentrated_base, kgmicrobe.ingredient:uw_concentrated_base_no_mo, kgmicrobe.ingredient:uw_concentrated_base_no_sulfur | Restoring one component identifier and removing added evidence/history yields each exact original parsed record; original byte hashes unchanged. |
| Whole-catalog negative and positive native regression | passed | True | kgmicrobe.ingredient:uw_concentrated_base, kgmicrobe.ingredient:uw_concentrated_base_no_mo, kgmicrobe.ingredient:uw_concentrated_base_no_sulfur | 0baseline /3borax-only /0corrected; no parent filter hides introduced errors. |
| Strict closed schema | passed | True | kgmicrobe.ingredient:uw_concentrated_base, kgmicrobe.ingredient:uw_concentrated_base_no_mo, kgmicrobe.ingredient:uw_concentrated_base_no_sulfur | 3files0errors |

## Scientific And Domain Assessments

### Source-scoped borax component reference

identity: supported. Targets: kgmicrobe.ingredient:uw_concentrated_base.

The explicit decahydrate reagent reference follows the source-verified corrected borax owner. Quantity0.0177G_PER_L, label, scope and all other claims are unchanged.

### Source-scoped borax component reference

identity: supported. Targets: kgmicrobe.ingredient:uw_concentrated_base_no_mo.

The explicit decahydrate reagent reference follows the source-verified corrected borax owner. Quantity0.0177G_PER_L, label, scope and all other claims are unchanged.

### Source-scoped borax component reference

identity: supported. Targets: kgmicrobe.ingredient:uw_concentrated_base_no_sulfur.

The explicit decahydrate reagent reference follows the source-verified corrected borax owner. Quantity0.0177G_PER_L, label, scope and all other claims are unchanged.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| mixes | https://docs.google.com/spreadsheets/d/1lNNW8BtrJL3pBlsnwvrQRKLU-9asECU_qaBfZ36Ft84; Live full A1598:Q1645; borax rows1612/1627/1643 | supports | Each preparation explicitly names sodium tetraborate decahydrate at0.0177g/L; surrounding recipe blocks identify the three exact stock variants. |
| structural | https://doi.org/10.1107/S1600536808010441; Gainsford et al.2008 original borax crystal structure, p.1 | supports | Na2[B4O5(OH)4]·8H2O is conventional sodium tetraborate decahydrate; matches corrected CHEBI38888 bulk formula. |
| ontology | reports/all_unmatched_20261107/worker-01/shard/root_substances/kg26/captures/borate175-ols-38888-v1.json; Complete official CHEBI38888 response | supports | Structural formula and mass support supplied borax form; no global redirect of erroneous131366 entity. |
| regression | reports/all_unmatched_20261107/worker-01/shard/root_substances/kg26/captures/uw-dependency-guard-regression-v2.json; Every full-catalog native partonomy violation, no target filtering | supports | Baseline0; borax-only3 orphaned references; borax plus3 corrected dependencies0. Structural rollback reproduces originals exactly. |
| strict | reports/all_unmatched_20261107/worker-01/shard/root_substances/kg26/captures/uw-native-strict-v2.tsv; Complete strict output for all3 proposed dependent records | supports | 3files,0schema errors. |
| proposal-0 | reports/all_unmatched_20261107/worker-01/shard/root_substances/kg26/proposals/UW_Concentrated_Base-borax-dependency-v2.yaml; Complete after payload | supports | Only borax component identifier plus bounded evidence/history change. |
| before-0 | data/ingredients/mapped/UW_Concentrated_Base.yaml; Complete original owner | supports | All inherited components, quantities, mapping, roles and history read; preserved, not given whole-record approval. |
| proposal-1 | reports/all_unmatched_20261107/worker-01/shard/root_substances/kg26/proposals/UW_Concentrated_Base_No_Mo-borax-dependency-v2.yaml; Complete after payload | supports | Only borax component identifier plus bounded evidence/history change. |
| before-1 | data/ingredients/mapped/UW_Concentrated_Base_No_Mo.yaml; Complete original owner | supports | All inherited components, quantities, mapping, roles and history read; preserved, not given whole-record approval. |
| proposal-2 | reports/all_unmatched_20261107/worker-01/shard/root_substances/kg26/proposals/UW_Concentrated_Base_No_Sulfur-borax-dependency-v2.yaml; Complete after payload | supports | Only borax component identifier plus bounded evidence/history change. |
| before-2 | data/ingredients/mapped/UW_Concentrated_Base_No_Sulfur.yaml; Complete original owner | supports | All inherited components, quantities, mapping, roles and history read; preserved, not given whole-record approval. |

## Limits And Additional Notes

- Author self-review does not satisfy independent review.
- Full original records were read, but unrelated inherited assertions are preserved without renewed scientific approval.
- Whole-catalog check covers baseline plus borax and three dependencies; root separately validates all campaign proposals.
- No maintained source, aggregate or export was changed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261108T050224Z-w01-uw-borax-dependencies-author
kind: batch
repository: CultureBotAI/MediaIngredientMech
title: Worker01 three UW borax dependency proposals
started_at: '2026-11-08T05:02:24.105588Z'
finished_at: '2026-11-08T05:02:24.452877Z'
reviewer:
  identity: /root/issue_context
  kind: agent
  independence: self_review
  independence_basis: Dependency proposal author; separate independent reviewer required.
skill: curate-yaml-record
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Source-verified decahydrate parts follow the corrected CHEBI38888 owner in
  all3 UW stocks. Native whole-catalog regression and strict schema pass; unrelated
  inherited formulation and role assertions are not approved.
source:
  git_revision: 58d67db32a86a359869819624568d625e7051358
  state: working_tree
  inputs:
  - path: MAPPING_SEMANTICS.md
    sha256: 6b52f2ac48109ddd5d81996a136b19776cab55efa69a5ec832cf716d6885a062
    role: context
  - path: data/ingredients/mapped/UW_Concentrated_Base.yaml
    sha256: e676b9237eadf613f04db4121c47cf5b273cf3e8322c1f01e367b9eb5d83b427
    role: context
  - path: data/ingredients/mapped/UW_Concentrated_Base_No_Mo.yaml
    sha256: daa15aae2de103e20e4916c105333d51581a8da24616ef312ba0b6a98d05fb0c
    role: context
  - path: data/ingredients/mapped/UW_Concentrated_Base_No_Sulfur.yaml
    sha256: ab68055139180f35162d25ad6f43160fbad7e09838d653419b10967c3558a28f
    role: context
  - path: reports/all_unmatched_20261107/worker-01/shard/root_substances/kg26/captures/borate175-ols-38888-v1.json
    sha256: 6933410e4ae1d55f63500c3a537f617d0f910fe2e2a8af5be5c21e2ee0825bf2
    role: context
  - path: reports/all_unmatched_20261107/worker-01/shard/root_substances/kg26/captures/borate175-structure-web-v1.json
    sha256: e23bf55ef6dcc3b75354d692f0c4d8c2aceacd920cdaa1a0b56a2c98e118fae7
    role: context
  - path: reports/all_unmatched_20261107/worker-01/shard/root_substances/kg26/captures/uw-dependency-guard-regression-v2.json
    sha256: 21d8857e72edc622af2127f2ddba5863d22dfaae6d6894ece12016dc1d9c6184
    role: context
  - path: reports/all_unmatched_20261107/worker-01/shard/root_substances/kg26/captures/uw-mixes-primary-v1.json
    sha256: c54f58de3f30c9bcd24fb37ea81f428950e92b9dd83820f21d8c366570cdcc84
    role: context
  - path: reports/all_unmatched_20261107/worker-01/shard/root_substances/kg26/captures/uw-native-strict-v2.tsv
    sha256: 4ccba8b77ce80cf210105b5284b5953747729aba576ccdeecb81f7db84eb721b
    role: context
  - path: reports/all_unmatched_20261107/worker-01/shard/root_substances/kg26/proposals/Na2b4o7_X_10_H2o.yaml
    sha256: b93a00e61c3a9ecc88328c44897808c0dd93d89f45ffb1c3e79f8ba1b5d8d69b
    role: context
  - path: reports/all_unmatched_20261107/worker-01/shard/root_substances/kg26/proposals/UW_Concentrated_Base-borax-dependency-v2.yaml
    sha256: d22e71c61fb0689c284ce6af932d3eb328dbbbc16f32b1577e05027d2d931f36
    role: target
  - path: reports/all_unmatched_20261107/worker-01/shard/root_substances/kg26/proposals/UW_Concentrated_Base_No_Mo-borax-dependency-v2.yaml
    sha256: 08f0d1e4f9d344a4263cd1e461d94cbbeedd59f671b0cd2fcbe23c93b6738003
    role: target
  - path: reports/all_unmatched_20261107/worker-01/shard/root_substances/kg26/proposals/UW_Concentrated_Base_No_Sulfur-borax-dependency-v2.yaml
    sha256: eb6b843602bc3c0b45daa9c85fa26e8d979f30ec764c81141b438e2f85dc05b8
    role: target
  - path: src/mediaingredientmech/schema/mediaingredientmech.yaml
    sha256: bb43dee29b21fdee72a48022456e733e49e95824c4c09674f9b3165c290fe012
    role: context
  - path: src/mediaingredientmech/validation/component_partonomy.py
    sha256: d2ec0640fb3d9bbb71d69cd285397a8b6a95876a199957c5b164908fec0f8696
    role: context
targets:
- target_id: kgmicrobe.ingredient:uw_concentrated_base
  path: reports/all_unmatched_20261107/worker-01/shard/root_substances/kg26/proposals/UW_Concentrated_Base-borax-dependency-v2.yaml
  label: UW concentrated base
  kind: source
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/UW_Concentrated_Base.yaml
    role: maintained owner; proposal not applied
- target_id: kgmicrobe.ingredient:uw_concentrated_base_no_mo
  path: reports/all_unmatched_20261107/worker-01/shard/root_substances/kg26/proposals/UW_Concentrated_Base_No_Mo-borax-dependency-v2.yaml
  label: UW concentrated base no Mo
  kind: source
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/UW_Concentrated_Base_No_Mo.yaml
    role: maintained owner; proposal not applied
- target_id: kgmicrobe.ingredient:uw_concentrated_base_no_sulfur
  path: reports/all_unmatched_20261107/worker-01/shard/root_substances/kg26/proposals/UW_Concentrated_Base_No_Sulfur-borax-dependency-v2.yaml
  label: UW concentrated base no sulfur
  kind: source
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/UW_Concentrated_Base_No_Sulfur.yaml
    role: maintained owner; proposal not applied
scope:
  description: All3 dependent UW records and exact proposed changes, with original
    primary Mixes rows and structural borax correspondence.
  selection: Exact3 maintained MIM_CATALOG references orphaned by KG26-PROP-175-STRUCTURAL-IDENTITY
    in issue1168.
  coverage: full
  population_size: 3
  reviewed_target_ids:
  - kgmicrobe.ingredient:uw_concentrated_base
  - kgmicrobe.ingredient:uw_concentrated_base_no_mo
  - kgmicrobe.ingredient:uw_concentrated_base_no_sulfur
  exclusions:
  - target: Unrelated inherited component identities, nutritional roles, full SSSOM
      publication and entire campaign integration
    reason: Scope is the borax component identity and dependent reference integrity
      only.
checks:
- check_id: identity
  name: Primary component identity and structural correspondence
  status: passed
  required: true
  summary: Exact source rows and complete records reviewed; supplied borax identity
    matches corrected owner.
  target_ids:
  - kgmicrobe.ingredient:uw_concentrated_base
  - kgmicrobe.ingredient:uw_concentrated_base_no_mo
  - kgmicrobe.ingredient:uw_concentrated_base_no_sulfur
  evidence_ids:
  - mixes
  - structural
  - ontology
- check_id: guard
  name: Exact rollback and native validated writes
  status: passed
  required: true
  summary: Restoring one component identifier and removing added evidence/history
    yields each exact original parsed record; original byte hashes unchanged.
  target_ids:
  - kgmicrobe.ingredient:uw_concentrated_base
  - kgmicrobe.ingredient:uw_concentrated_base_no_mo
  - kgmicrobe.ingredient:uw_concentrated_base_no_sulfur
  evidence_ids:
  - regression
- check_id: catalog
  name: Whole-catalog negative and positive native regression
  status: passed
  required: true
  summary: 0baseline /3borax-only /0corrected; no parent filter hides introduced errors.
  target_ids:
  - kgmicrobe.ingredient:uw_concentrated_base
  - kgmicrobe.ingredient:uw_concentrated_base_no_mo
  - kgmicrobe.ingredient:uw_concentrated_base_no_sulfur
  evidence_ids:
  - regression
- check_id: strict
  name: Strict closed schema
  status: passed
  required: true
  summary: 3files0errors
  command: .temp/all-unmatched-worker-01/shard-venv/bin/python scripts/validate_strict.py
    reports/all_unmatched_20261107/worker-01/shard/root_substances/kg26/proposals/UW_Concentrated_Base-borax-dependency-v2.yaml
    reports/all_unmatched_20261107/worker-01/shard/root_substances/kg26/proposals/UW_Concentrated_Base_No_Mo-borax-dependency-v2.yaml
    reports/all_unmatched_20261107/worker-01/shard/root_substances/kg26/proposals/UW_Concentrated_Base_No_Sulfur-borax-dependency-v2.yaml
    --out reports/all_unmatched_20261107/worker-01/shard/root_substances/kg26/captures/uw-native-strict-v2.tsv
    --workers 1
  exit_code: 0
  target_ids:
  - kgmicrobe.ingredient:uw_concentrated_base
  - kgmicrobe.ingredient:uw_concentrated_base_no_mo
  - kgmicrobe.ingredient:uw_concentrated_base_no_sulfur
  evidence_ids:
  - strict
evidence:
- evidence_id: mixes
  kind: primary_source
  reference: https://docs.google.com/spreadsheets/d/1lNNW8BtrJL3pBlsnwvrQRKLU-9asECU_qaBfZ36Ft84
  locator: Live full A1598:Q1645; borax rows1612/1627/1643
  accessed_at: '2026-11-08T05:00:13.131Z'
  support: supports
  summary: Each preparation explicitly names sodium tetraborate decahydrate at0.0177g/L;
    surrounding recipe blocks identify the three exact stock variants.
  snapshot_sha256: c54f58de3f30c9bcd24fb37ea81f428950e92b9dd83820f21d8c366570cdcc84
- evidence_id: structural
  kind: primary_source
  reference: https://doi.org/10.1107/S1600536808010441
  locator: Gainsford et al.2008 original borax crystal structure, p.1
  accessed_at: '2026-11-08T05:02:24.105588Z'
  support: supports
  summary: Na2[B4O5(OH)4]·8H2O is conventional sodium tetraborate decahydrate; matches
    corrected CHEBI38888 bulk formula.
  snapshot_sha256: e23bf55ef6dcc3b75354d692f0c4d8c2aceacd920cdaa1a0b56a2c98e118fae7
- evidence_id: ontology
  kind: database
  reference: reports/all_unmatched_20261107/worker-01/shard/root_substances/kg26/captures/borate175-ols-38888-v1.json
  locator: Complete official CHEBI38888 response
  accessed_at: '2026-11-08T05:02:24.105588Z'
  support: supports
  summary: Structural formula and mass support supplied borax form; no global redirect
    of erroneous131366 entity.
  snapshot_sha256: 6933410e4ae1d55f63500c3a537f617d0f910fe2e2a8af5be5c21e2ee0825bf2
- evidence_id: regression
  kind: validation
  reference: reports/all_unmatched_20261107/worker-01/shard/root_substances/kg26/captures/uw-dependency-guard-regression-v2.json
  locator: Every full-catalog native partonomy violation, no target filtering
  accessed_at: '2026-11-08T05:02:24.105588Z'
  support: supports
  summary: Baseline0; borax-only3 orphaned references; borax plus3 corrected dependencies0.
    Structural rollback reproduces originals exactly.
  snapshot_sha256: 21d8857e72edc622af2127f2ddba5863d22dfaae6d6894ece12016dc1d9c6184
- evidence_id: strict
  kind: validation
  reference: reports/all_unmatched_20261107/worker-01/shard/root_substances/kg26/captures/uw-native-strict-v2.tsv
  locator: Complete strict output for all3 proposed dependent records
  accessed_at: '2026-11-08T05:02:24.105588Z'
  support: supports
  summary: 3files,0schema errors.
  snapshot_sha256: 4ccba8b77ce80cf210105b5284b5953747729aba576ccdeecb81f7db84eb721b
- evidence_id: proposal-0
  kind: record_content
  reference: reports/all_unmatched_20261107/worker-01/shard/root_substances/kg26/proposals/UW_Concentrated_Base-borax-dependency-v2.yaml
  locator: Complete after payload
  accessed_at: '2026-11-08T05:02:24.105588Z'
  support: supports
  summary: Only borax component identifier plus bounded evidence/history change.
  snapshot_sha256: d22e71c61fb0689c284ce6af932d3eb328dbbbc16f32b1577e05027d2d931f36
- evidence_id: before-0
  kind: record_content
  reference: data/ingredients/mapped/UW_Concentrated_Base.yaml
  locator: Complete original owner
  accessed_at: '2026-11-08T05:02:24.105588Z'
  support: supports
  summary: All inherited components, quantities, mapping, roles and history read;
    preserved, not given whole-record approval.
  snapshot_sha256: e676b9237eadf613f04db4121c47cf5b273cf3e8322c1f01e367b9eb5d83b427
- evidence_id: proposal-1
  kind: record_content
  reference: reports/all_unmatched_20261107/worker-01/shard/root_substances/kg26/proposals/UW_Concentrated_Base_No_Mo-borax-dependency-v2.yaml
  locator: Complete after payload
  accessed_at: '2026-11-08T05:02:24.105588Z'
  support: supports
  summary: Only borax component identifier plus bounded evidence/history change.
  snapshot_sha256: 08f0d1e4f9d344a4263cd1e461d94cbbeedd59f671b0cd2fcbe23c93b6738003
- evidence_id: before-1
  kind: record_content
  reference: data/ingredients/mapped/UW_Concentrated_Base_No_Mo.yaml
  locator: Complete original owner
  accessed_at: '2026-11-08T05:02:24.105588Z'
  support: supports
  summary: All inherited components, quantities, mapping, roles and history read;
    preserved, not given whole-record approval.
  snapshot_sha256: daa15aae2de103e20e4916c105333d51581a8da24616ef312ba0b6a98d05fb0c
- evidence_id: proposal-2
  kind: record_content
  reference: reports/all_unmatched_20261107/worker-01/shard/root_substances/kg26/proposals/UW_Concentrated_Base_No_Sulfur-borax-dependency-v2.yaml
  locator: Complete after payload
  accessed_at: '2026-11-08T05:02:24.105588Z'
  support: supports
  summary: Only borax component identifier plus bounded evidence/history change.
  snapshot_sha256: eb6b843602bc3c0b45daa9c85fa26e8d979f30ec764c81141b438e2f85dc05b8
- evidence_id: before-2
  kind: record_content
  reference: data/ingredients/mapped/UW_Concentrated_Base_No_Sulfur.yaml
  locator: Complete original owner
  accessed_at: '2026-11-08T05:02:24.105588Z'
  support: supports
  summary: All inherited components, quantities, mapping, roles and history read;
    preserved, not given whole-record approval.
  snapshot_sha256: ab68055139180f35162d25ad6f43160fbad7e09838d653419b10967c3558a28f
assessments:
- assessment_id: uw-0
  area: identity
  topic: Source-scoped borax component reference
  outcome: supported
  summary: The explicit decahydrate reagent reference follows the source-verified
    corrected borax owner. Quantity0.0177G_PER_L, label, scope and all other claims
    are unchanged.
  target_ids:
  - kgmicrobe.ingredient:uw_concentrated_base
  evidence_ids:
  - mixes
  - structural
  - ontology
  - regression
  - proposal-0
  - before-0
- assessment_id: uw-1
  area: identity
  topic: Source-scoped borax component reference
  outcome: supported
  summary: The explicit decahydrate reagent reference follows the source-verified
    corrected borax owner. Quantity0.0177G_PER_L, label, scope and all other claims
    are unchanged.
  target_ids:
  - kgmicrobe.ingredient:uw_concentrated_base_no_mo
  evidence_ids:
  - mixes
  - structural
  - ontology
  - regression
  - proposal-1
  - before-1
- assessment_id: uw-2
  area: identity
  topic: Source-scoped borax component reference
  outcome: supported
  summary: The explicit decahydrate reagent reference follows the source-verified
    corrected borax owner. Quantity0.0177G_PER_L, label, scope and all other claims
    are unchanged.
  target_ids:
  - kgmicrobe.ingredient:uw_concentrated_base_no_sulfur
  evidence_ids:
  - mixes
  - structural
  - ontology
  - regression
  - proposal-2
  - before-2
findings: []
actions: []
limitations:
- Author self-review does not satisfy independent review.
- Full original records were read, but unrelated inherited assertions are preserved
  without renewed scientific approval.
- Whole-catalog check covers baseline plus borax and three dependencies; root separately
  validates all campaign proposals.
- No maintained source, aggregate or export was changed.
```
