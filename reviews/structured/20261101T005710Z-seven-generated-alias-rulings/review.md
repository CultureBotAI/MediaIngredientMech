# Seven exact generated alias claims: evidence-backed chemical-form separation

- Review: 20261101T005710Z-seven-generated-alias-rulings
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-11-01T00:55:58.478803Z
- Finished UTC: 2026-11-01T00:57:10.014126Z
- Reviewer: Codex scientific curation agent (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Seven named unqualified alias tokens conflate a maintained salt, hydrate or stock identity with a distinct form. Their removal is scientifically supported within those exact claims; every underlying record and scientific hold is preserved.

## Scope And Provenance

Seven named unqualified alias tokens conflate a maintained salt, hydrate or stock identity with a distinct form. Their removal is scientifically supported within those exact claims; every underlying record and scientific hold is preserved.

Selection: Exactly the listed claim selectors, not all claims of their owner records.
Coverage: full; 7 reviewed / 7 in the declared population.
Source: working_tree at Git base 4625afd492b6cf43e3b499d1425d2453d490009d.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| generated-alias-1 | reports/sssom_scientific_curation_20261101/audit669/seven-alias-apply.before.tsv # {"object_id": "CHEBI:48430", "predicate_id": "skos:broadMatch", "subject_id": "MIM:4-Methyl-2-oxopentanoic_Acid_Sodium_Salt", "token": "4-Methyl-2-oxovaleric acid"} | snapshot_row | MIM:4-Methyl-2-oxopentanoic_Acid_Sodium_Salt / 4-Methyl-2-oxovaleric acid |
| generated-alias-2 | reports/sssom_scientific_curation_20261101/audit669/seven-alias-apply.before.tsv # {"object_id": "CHEBI:32139", "predicate_id": "skos:broadMatch", "subject_id": "MIM:84_GL_NaHCO3_Solution", "token": "NaHCO3"} | snapshot_row | MIM:84_GL_NaHCO3_Solution / NaHCO3 |
| generated-alias-3 | reports/sssom_scientific_curation_20261101/audit669/seven-alias-apply.before.tsv # {"object_id": "CHEBI:17750", "predicate_id": "skos:broadMatch", "subject_id": "MIM:Betaine_Hydrochloride", "token": "Betaine x H2O"} | snapshot_row | MIM:Betaine_Hydrochloride / Betaine x H2O |
| generated-alias-4 | reports/sssom_scientific_curation_20261101/audit669/seven-alias-apply.before.tsv # {"object_id": "CHEBI:17369", "predicate_id": "skos:broadMatch", "subject_id": "MIM:D-Mannose_6-phosphate_Sodium_Salt", "token": "Mannose-6-Phosphate"} | snapshot_row | MIM:D-Mannose_6-phosphate_Sodium_Salt / Mannose-6-Phosphate |
| generated-alias-5 | reports/sssom_scientific_curation_20261101/audit669/seven-alias-apply.before.tsv # {"object_id": "CHEBI:39005", "predicate_id": "skos:broadMatch", "subject_id": "MIM:MES_Hydrat", "token": "MES [2-(N-morpholino) ethane sulfonic acid]"} | snapshot_row | MIM:MES_Hydrat / MES [2-(N-morpholino) ethane sulfonic acid] |
| generated-alias-6 | reports/sssom_scientific_curation_20261101/audit669/seven-alias-apply.before.tsv # {"object_id": "CHEBI:15978", "predicate_id": "skos:broadMatch", "subject_id": "MIM:Sn-glycerol_3-phosphate_Bis_Cyclohexylammonium_Salt", "token": "Glycerol 3-phosphate"} | snapshot_row | MIM:Sn-glycerol_3-phosphate_Bis_Cyclohexylammonium_Salt / Glycerol 3-phosphate |
| generated-alias-7 | reports/sssom_scientific_curation_20261101/audit669/seven-alias-apply.before.tsv # {"object_id": "CHEBI:132103", "predicate_id": "skos:exactMatch", "subject_id": "MIM:Sodium_Perchlorate", "token": "Sodium perchlorate monohydrate"} | snapshot_row | MIM:Sodium_Perchlorate / Sodium perchlorate monohydrate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Primary database and maintained-form comparisons | passed | True | generated-alias-1, generated-alias-2, generated-alias-3, generated-alias-4, generated-alias-5, generated-alias-6, generated-alias-7 | All seven selected distinctions were checked against saved official ChEBI/PubChem assertions or the explicit maintained stock-solution identity. Dictionary absence was not used as scientific proof. |
| alias final code regressions | passed | True | generated-alias-1, generated-alias-2, generated-alias-3, generated-alias-4, generated-alias-5, generated-alias-6, generated-alias-7 | All 48 scoped final-code tests passed. |
| final scoped alias verification | passed | True | generated-alias-1, generated-alias-2, generated-alias-3, generated-alias-4, generated-alias-5, generated-alias-6, generated-alias-7 | Final selective payload, unchanged owner, exact baseline and withheld-disposition checks passed. |

## Scientific And Domain Assessments

### Exact token scope: 4-Methyl-2-oxovaleric acid

nomenclature: supported. Targets: generated-alias-1.

PubChem CAS 4502-00-5 is sodium 4-methyl-2-oxovalerate, C6H9NaO3; ChEBI:48430 is the acid C6H10O3. The parent preferred name cannot assert exact substance identity for this sodium salt. The exact selected token is therefore not published as an unqualified same-substance alias of this maintained form; other fields, YAML and native holds remain unchanged.

### Exact token scope: NaHCO3

nomenclature: supported. Targets: generated-alias-2.

The maintained identity is explicitly a stock solution kgmicrobe.ingredient:84_gl_nahco3_solution, with concentration and solution curation; the owner NaHCO3 is neat sodium hydrogencarbonate CHEBI:32139. This is a mixture/concentration boundary, not merely spelling. The exact selected token is therefore not published as an unqualified same-substance alias of this maintained form; other fields, YAML and native holds remain unchanged.

### Exact token scope: Betaine x H2O

nomenclature: supported. Targets: generated-alias-3.

PubChem CAS 590-46-5 is betaine chloride C5H12ClNO2; the owner ChEBI:91242 is glycine betaine monohydrate C5H11NO2.H2O (CAS 590-47-6). Chloride and hydrate identities differ. The exact selected token is therefore not published as an unqualified same-substance alias of this maintained form; other fields, YAML and native holds remain unchanged.

### Exact token scope: Mannose-6-Phosphate

nomenclature: supported. Targets: generated-alias-4.

PubChem CAS 70442-25-0 is sodium mannose 6-phosphate C6H12NaO9P; ChEBI:17369 is D-mannose 6-phosphate C6H13O9P. The sodium counterion is chemically material. The exact selected token is therefore not published as an unqualified same-substance alias of this maintained form; other fields, YAML and native holds remain unchanged.

### Exact token scope: MES [2-(N-morpholino) ethane sulfonic acid]

nomenclature: supported. Targets: generated-alias-5.

PubChem CAS 145224-94-8 is MES hydrate C6H15NO5S; ChEBI:39005 is MES C6H13NO4S. This evidence supports a form boundary independent of KG alias availability. The exact selected token is therefore not published as an unqualified same-substance alias of this maintained form; other fields, YAML and native holds remain unchanged.

### Exact token scope: Glycerol 3-phosphate

nomenclature: supported. Targets: generated-alias-6.

PubChem CAS 29849-82-9 is the bis(cyclohexylammonium) salt C15H35N2O6P; ChEBI:15978 is the free acid C3H9O6P. Removing the unqualified parent alias does not require guessing the salt identity. The exact selected token is therefore not published as an unqualified same-substance alias of this maintained form; other fields, YAML and native holds remain unchanged.

### Exact token scope: Sodium perchlorate monohydrate

nomenclature: supported. Targets: generated-alias-7.

PubChem CAS 7601-89-0 is sodium perchlorate ClNaO4; CAS 7791-07-3 is monohydrate ClH2NaO5. ChEBI:132103 confirms the anhydrous subject. The exact selected token is therefore not published as an unqualified same-substance alias of this maintained form; other fields, YAML and native holds remain unchanged.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| semantics | MAPPING_SEMANTICS.md; Section 3 | supports | The contract distinguishes salts, hydrates, stock solutions and their parent substances; source alias scope must not collapse those identities. |
| original-claims | reports/sssom_scientific_curation_20261101/audit669/seven-alias-apply.before.tsv; Seven target selectors | supports | Frozen pre-transform canonical preserves each exact original triple and removed other token. This is an intermediate snapshot, not the final canonical. |
| migration | reports/sssom_scientific_curation_20261101/audit669/seven-alias-apply.json | supports | Receipt preserves all seven unchanged owner hashes and verifies independent omission in the final native generated candidate; baseline obligations retired 45→38 without inventing YAML rejection entries. |
| final-proof | reports/sssom_scientific_curation_20261101/audit669/final-scoped-verification.json; seven_aliases; exact_remaining_baseline_pairs_preserved | supports | All seven final rows differ only in other from their frozen pre-transform row; every owner hash is unchanged, all 18 owner rows remain WITHHOLD, and remaining 38 baseline pairs including seven YAML policy cases persist. |
| regression-receipt | reports/sssom_scientific_curation_20261101/audit669/logs/alias_final_code_regressions.json | supports | All 48 final maintained-code tests passed, including owner changes, missing/duplicate/changed selectors, candidate disagreement, byte preservation and receipt/backup collisions. |
| mapping-receipt | reports/sssom_completion_20260921/mapping_changes/issue669-1003-scoped-alias-corrections.json | supports | Native approval-free mapping receipt binds the seven changed rows to unchanged owner bytes and preserves withheld status. |
| owner-1 | data/ingredients/mapped/4-Methyl-2-oxopentanoic_Acid_Sodium_Salt.yaml; identifier; preferred_term; ontology_mapping; supplied-form and source history | supports | Maintained record identity/form inspected for this exact alias-scope contrast. No other claim is scientifically approved. |
| source-1-1 | reports/sssom_scientific_curation_20261101/audit669/sources/PubChem-CAS-4502-00-5.json; Official response term/properties; source URL and capture time in companion manifests | supports | PubChem CAS 4502-00-5 is sodium 4-methyl-2-oxovalerate, C6H9NaO3; ChEBI:48430 is the acid C6H10O3. The parent preferred name cannot assert exact substance identity for this sodium salt. |
| source-1-2 | reports/sssom_scientific_curation_20261101/audit669/sources/CHEBI_48430.ols.json; Official response term/properties; source URL and capture time in companion manifests | supports | PubChem CAS 4502-00-5 is sodium 4-methyl-2-oxovalerate, C6H9NaO3; ChEBI:48430 is the acid C6H10O3. The parent preferred name cannot assert exact substance identity for this sodium salt. |
| owner-2 | data/ingredients/mapped/84_GL_NaHCO3_Solution.yaml; identifier; preferred_term; ontology_mapping; supplied-form and source history | supports | Maintained record identity/form inspected for this exact alias-scope contrast. No other claim is scientifically approved. |
| source-2-1 | reports/sssom_scientific_curation_20261101/audit669/sources/CHEBI_32139.ols.json; Official response term/properties; source URL and capture time in companion manifests | supports | The maintained identity is explicitly a stock solution kgmicrobe.ingredient:84_gl_nahco3_solution, with concentration and solution curation; the owner NaHCO3 is neat sodium hydrogencarbonate CHEBI:32139. This is a mixture/concentration boundary, not merely spelling. |
| owner-3 | data/ingredients/mapped/Betaine_Hydrochloride.yaml; identifier; preferred_term; ontology_mapping; supplied-form and source history | supports | Maintained record identity/form inspected for this exact alias-scope contrast. No other claim is scientifically approved. |
| source-3-1 | reports/sssom_scientific_curation_20261101/audit669/sources/PubChem-CAS-590-46-5.json; Official response term/properties; source URL and capture time in companion manifests | supports | PubChem CAS 590-46-5 is betaine chloride C5H12ClNO2; the owner ChEBI:91242 is glycine betaine monohydrate C5H11NO2.H2O (CAS 590-47-6). Chloride and hydrate identities differ. |
| source-3-2 | reports/sssom_scientific_curation_20261101/audit669/sources/CHEBI_91242.ols.json; Official response term/properties; source URL and capture time in companion manifests | supports | PubChem CAS 590-46-5 is betaine chloride C5H12ClNO2; the owner ChEBI:91242 is glycine betaine monohydrate C5H11NO2.H2O (CAS 590-47-6). Chloride and hydrate identities differ. |
| owner-4 | data/ingredients/mapped/D-Mannose_6-phosphate_Sodium_Salt.yaml; identifier; preferred_term; ontology_mapping; supplied-form and source history | supports | Maintained record identity/form inspected for this exact alias-scope contrast. No other claim is scientifically approved. |
| source-4-1 | reports/sssom_scientific_curation_20261101/audit669/sources/PubChem-CAS-70442-25-0.json; Official response term/properties; source URL and capture time in companion manifests | supports | PubChem CAS 70442-25-0 is sodium mannose 6-phosphate C6H12NaO9P; ChEBI:17369 is D-mannose 6-phosphate C6H13O9P. The sodium counterion is chemically material. |
| source-4-2 | reports/sssom_scientific_curation_20261101/audit669/sources/CHEBI_17369.ols.json; Official response term/properties; source URL and capture time in companion manifests | supports | PubChem CAS 70442-25-0 is sodium mannose 6-phosphate C6H12NaO9P; ChEBI:17369 is D-mannose 6-phosphate C6H13O9P. The sodium counterion is chemically material. |
| owner-5 | data/ingredients/mapped/MES_Hydrat.yaml; identifier; preferred_term; ontology_mapping; supplied-form and source history | supports | Maintained record identity/form inspected for this exact alias-scope contrast. No other claim is scientifically approved. |
| source-5-1 | reports/sssom_scientific_curation_20261101/audit669/sources/PubChem-CAS-145224-94-8.json; Official response term/properties; source URL and capture time in companion manifests | supports | PubChem CAS 145224-94-8 is MES hydrate C6H15NO5S; ChEBI:39005 is MES C6H13NO4S. This evidence supports a form boundary independent of KG alias availability. |
| source-5-2 | reports/sssom_scientific_curation_20261101/audit669/sources/CHEBI_39005.ols.json; Official response term/properties; source URL and capture time in companion manifests | supports | PubChem CAS 145224-94-8 is MES hydrate C6H15NO5S; ChEBI:39005 is MES C6H13NO4S. This evidence supports a form boundary independent of KG alias availability. |
| owner-6 | data/ingredients/mapped/Sn-glycerol_3-phosphate_Bis_Cyclohexylammonium_Salt.yaml; identifier; preferred_term; ontology_mapping; supplied-form and source history | supports | Maintained record identity/form inspected for this exact alias-scope contrast. No other claim is scientifically approved. |
| source-6-1 | reports/sssom_scientific_curation_20261101/audit669/sources/PubChem-CAS-29849-82-9.json; Official response term/properties; source URL and capture time in companion manifests | supports | PubChem CAS 29849-82-9 is the bis(cyclohexylammonium) salt C15H35N2O6P; ChEBI:15978 is the free acid C3H9O6P. Removing the unqualified parent alias does not require guessing the salt identity. |
| source-6-2 | reports/sssom_scientific_curation_20261101/audit669/sources/CHEBI_15978.ols.json; Official response term/properties; source URL and capture time in companion manifests | supports | PubChem CAS 29849-82-9 is the bis(cyclohexylammonium) salt C15H35N2O6P; ChEBI:15978 is the free acid C3H9O6P. Removing the unqualified parent alias does not require guessing the salt identity. |
| owner-7 | data/ingredients/mapped/Sodium_Perchlorate.yaml; identifier; preferred_term; ontology_mapping; supplied-form and source history | supports | Maintained record identity/form inspected for this exact alias-scope contrast. No other claim is scientifically approved. |
| source-7-1 | reports/sssom_scientific_curation_20261101/audit669/sources/PubChem-CAS-7601-89-0.json; Official response term/properties; source URL and capture time in companion manifests | supports | PubChem CAS 7601-89-0 is sodium perchlorate ClNaO4; CAS 7791-07-3 is monohydrate ClH2NaO5. ChEBI:132103 confirms the anhydrous subject. |
| source-7-2 | reports/sssom_scientific_curation_20261101/audit669/sources/PubChem-CAS-7791-07-3.json; Official response term/properties; source URL and capture time in companion manifests | supports | PubChem CAS 7601-89-0 is sodium perchlorate ClNaO4; CAS 7791-07-3 is monohydrate ClH2NaO5. ChEBI:132103 confirms the anhydrous subject. |
| source-7-3 | reports/sssom_scientific_curation_20261101/audit669/sources/CHEBI_132103.ols.json; Official response term/properties; source URL and capture time in companion manifests | supports | PubChem CAS 7601-89-0 is sodium perchlorate ClNaO4; CAS 7791-07-3 is monohydrate ClH2NaO5. ChEBI:132103 confirms the anhydrous subject. |

## Limits And Additional Notes

- This is a claim-specific self-review, not independent review or whole-record chemical approval.
- Historical validation stamps are retained provenance; no fresh scientific approval or role support is inferred.
- Native scientific release holds remain authoritative; a passing scoped review does not promote assertions.
- The source record can still contain unrelated incomplete or contradictory scientific claims; these are outside this alias-only ruling. In particular, stock concentration/source details and full molecular or role assertions are not certified.
- The seven YAML generic-name policy cases, 23 pairs overlapping active PR #912, and 8 identity/alias-scope cases remain open; no full candidate promotion or family merge follows.
- Source database assertions establish the stated chemical-form contrasts; they are not primary experimental studies or evidence of biological roles.
- Whole repository data/release validators and independent review are reported in the parent run; this review only states its listed checks.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261101T005710Z-seven-generated-alias-rulings
kind: batch
repository: CultureBotAI/MediaIngredientMech
title: 'Seven exact generated alias claims: evidence-backed chemical-form separation'
started_at: '2026-11-01T00:55:58.478803Z'
finished_at: '2026-11-01T00:57:10.014126Z'
reviewer:
  identity: Codex scientific curation agent
  kind: agent
  model: gpt-6
  independence: self_review
  independence_basis: This agent inspected the cited database assertions and authored
    the bounded correction and regression tests. Independent review is separate; this
    document does not claim independence.
skill: review-sssom-output
completion: completed
verdict: pass_with_limitations
native_verdict: Selected synonym correction supported; mapping_status and native WITHHOLD
  decisions retained
scientific_review: true
summary: Seven named unqualified alias tokens conflate a maintained salt, hydrate
  or stock identity with a distinct form. Their removal is scientifically supported
  within those exact claims; every underlying record and scientific hold is preserved.
source:
  git_revision: 4625afd492b6cf43e3b499d1425d2453d490009d
  state: working_tree
  inputs:
  - path: MAPPING_SEMANTICS.md
    sha256: 94aad13ea0fc3df82a37383f388f41432b607b04cac61ae5792ce1a381aef805
    role: context
  - path: data/ingredients/mapped/4-Methyl-2-oxopentanoic_Acid_Sodium_Salt.yaml
    sha256: 8d5da3b1c891a79adf823a2ea778b04ef2658cc6bc175469631251c3874a314b
    role: context
  - path: data/ingredients/mapped/4-Methyl-2-oxovaleric_Acid.yaml
    sha256: 8de711f4ed9b972971a6ecce2fcb1e7e790b245b92efadbe48dc854a5f601c8b
    role: context
  - path: data/ingredients/mapped/84_GL_NaHCO3_Solution.yaml
    sha256: 1a8f4136f2de11105febf3112e5ca27fd95fcf9266ca1bb2283210267f70a509
    role: context
  - path: data/ingredients/mapped/Betaine_Hydrochloride.yaml
    sha256: 77cf04f3fafb04a92080656711b7807ed4e9af7c79f7852ffd31a09fe428f4ac
    role: context
  - path: data/ingredients/mapped/Betaine_X_H2o.yaml
    sha256: 30e8e68f84a2fb6e866ce4356a4514f21701286b04a0f70847d6bf9cb2a0320f
    role: context
  - path: data/ingredients/mapped/D-Mannose_6-phosphate_Sodium_Salt.yaml
    sha256: 280c8b5687a3ccd348984cd3b37518d2d1d298a80d1cd0c2b9a911b06f9a0535
    role: context
  - path: data/ingredients/mapped/Glycerol_3-phosphate.yaml
    sha256: 541136769c3854f039e315c0882f4d8fe5d6b7b0d35e897b1045ef720dc9518f
    role: context
  - path: data/ingredients/mapped/MES_Hydrat.yaml
    sha256: 24292497ec7bae482bb3611b8afb9cd1f795332d655be8900f4c59f8d929ebb6
    role: context
  - path: data/ingredients/mapped/Mannose-6-Phosphate.yaml
    sha256: ba93ffc65cac2dcd83d8852d4d805c249f5c4be37beb789599fd93ba76dc9415
    role: context
  - path: data/ingredients/mapped/Mes_2-_N-morpholino_Ethane_Sulfonic_Acid.yaml
    sha256: 74b9b9ad58114bc8b6b1cb6248f12b9857093f0339635bb3c1c4d8e6e3a02f46
    role: context
  - path: data/ingredients/mapped/Nahco3.yaml
    sha256: 97cc3f952982f9f22d0024c4ccb5aaa942c22edb5332782c69aee96d7b744998
    role: context
  - path: data/ingredients/mapped/Sn-glycerol_3-phosphate_Bis_Cyclohexylammonium_Salt.yaml
    sha256: 185d299a1d5a117e5ce42e2826e3f9fb83cba57459c5fc7e09f2dcf263a660f1
    role: context
  - path: data/ingredients/mapped/Sodium_Perchlorate.yaml
    sha256: 5b8a68b008ebce2e98c040b9dfff7b5b16f2370b320bb77cf0d3db32e680e0e0
    role: context
  - path: data/ingredients/mapped/Sodium_Perchlorate_Monohydrate.yaml
    sha256: 1f39286747eb8f3a2ec3da7919f9e6cb197221fcfef46af69a6784afd8f83ccc
    role: context
  - path: mappings/ingredient_mappings.sssom.tsv
    sha256: f408f36b9de77c2089a07907b40d6a27401087e13528f0597a6cf7b386048ac0
    role: context
  - path: mappings/other_cross_record_baseline.tsv
    sha256: 170368983e4105773348122d44da5417745e675dfa9151f72270f19da7a26008
    role: context
  - path: reports/sssom_completion_20260921/mapping_changes/issue669-1003-scoped-alias-corrections.json
    sha256: 00049aa1d2b19565020d4ecbec999fc723d2cf5954968ec6bf5cebdc0da73f34
    role: context
  - path: reports/sssom_completion_20260921/review.json
    sha256: 0cc2c8742f905458ebb15ed0195aa0744662f29d6019bad03690f8095904ac40
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit669/final-scoped-verification.json
    sha256: 4536bdc56695a08d80d7afd04f1cef4007f8064911b58b64f84b98d7870c122c
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit669/logs/alias_final_code_regressions.json
    sha256: e34b2a139a933d22e7997147f299002df4899c3fa1436fc3c97523e88fef7079
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit669/logs/alias_final_code_regressions.log
    sha256: bb04bd3f24f91cb478289e160999e182cff84b63d1a4fa4c807233c60441fa7a
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit669/logs/final_scoped_alias_verification.json
    sha256: 1da8b09b878ff70e9e4f111c2d400cb5eda8b6b6a2d1fa33c6f80ba591bd3076
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit669/seven-alias-apply.baseline-before.tsv
    sha256: b717cfa99d0ad0e386fe2dc9d8c93b6b0d902fbfdbd3358f5a149697ee71e41b
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit669/seven-alias-apply.before.tsv
    sha256: 757643bf567a992c2b89cebb74e3c6410fcf944b93ca3663c8338ba07ae22b18
    role: target
  - path: reports/sssom_scientific_curation_20261101/audit669/seven-alias-apply.json
    sha256: 021d2cf58f890cf321eef26956fb294bdb50f3f5a11669fcd28295fc348fdb63
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit669/seven-removal-feasibility.json
    sha256: 46bb592150a1f7e5e7f96f3f6a14532af7a71ee37c01a2642eb496fb9becba29
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit669/sources/CHEBI_132103.ols.json
    sha256: b9c17be4c36719cbf8972e959153772ad12b6efffaba915f6a84d219cf16eb01
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit669/sources/CHEBI_15978.ols.json
    sha256: 565d77bfa309af5e1d427dea7d26f7266d815189a470203fd82c4a0cfcf1e3e1
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit669/sources/CHEBI_17369.ols.json
    sha256: d722a50189087d6b8141cc28d7d7ca893e0d97dfb47221dce598de9f3b03396f
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit669/sources/CHEBI_32139.ols.json
    sha256: 51709e2510736d0b63369147b10ec6ffe80d5d5c3a40605381de9b3ed78634c3
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit669/sources/CHEBI_39005.ols.json
    sha256: 0924879ff890ef5624ea83cc42f75ca645247948e1f62270aef5f45cfd487c4c
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit669/sources/CHEBI_48430.ols.json
    sha256: 9791f4da2a3cdb25de4cfd7cb3990d288735afb7aab155ffca8b070661471f8c
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit669/sources/CHEBI_91242.ols.json
    sha256: 245044748707015ad714c1bbb2deae5793806cc83a59a100b847b1357acb5cf2
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit669/sources/PubChem-CAS-145224-94-8.json
    sha256: 0b92fe032b10fa400e8d1a036b35b057dd4ce92e77ab8694650bc672d8c27e46
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit669/sources/PubChem-CAS-29849-82-9.json
    sha256: 2a1ec78b1a642194de4426cfd207c4986459fc5d78c7b6939db700e83b34c5ef
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit669/sources/PubChem-CAS-4502-00-5.json
    sha256: fbf0e32a45db47198f99697349812100fbb711a8d44c64c91b449af99af3ede7
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit669/sources/PubChem-CAS-590-46-5.json
    sha256: 1d7c1f0966a710c1734b09575eb4499b1bb0d9749d91ec5cdbf736e9c0fff0e5
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit669/sources/PubChem-CAS-70442-25-0.json
    sha256: d5b3975ada83fe9c6250bbfbc51dd37dd282df434d0d9b4ead4e55a97c023e54
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit669/sources/PubChem-CAS-7601-89-0.json
    sha256: 72b3f22d2373b88510295b51144228c0dcb2a000c67588305579fd349d496ec9
    role: context
  - path: reports/sssom_scientific_curation_20261101/audit669/sources/PubChem-CAS-7791-07-3.json
    sha256: 5da16842ccf25f8fd40b70737d350f3a96e9e65dde797bda446db2df6e6baf24
    role: context
  - path: scripts/retire_reviewed_generated_aliases.py
    sha256: 9481efcd80acd5351cd498d09fc5912fb25bb9d143dbf229fbaaee4d181e536b
    role: context
  - path: src/mediaingredientmech/schema/mediaingredientmech.yaml
    sha256: bb43dee29b21fdee72a48022456e733e49e95824c4c09674f9b3165c290fe012
    role: context
  - path: tests/test_retire_reviewed_generated_aliases.py
    sha256: 81258f35c8a8b17fda1c9e8539bcb944176230c0df5ce9095db2bd4c4d6f33f5
    role: context
scope:
  description: Seven named unqualified alias tokens conflate a maintained salt, hydrate
    or stock identity with a distinct form. Their removal is scientifically supported
    within those exact claims; every underlying record and scientific hold is preserved.
  selection: Exactly the listed claim selectors, not all claims of their owner records.
  coverage: full
  population_size: 7
  reviewed_target_ids:
  - generated-alias-1
  - generated-alias-2
  - generated-alias-3
  - generated-alias-4
  - generated-alias-5
  - generated-alias-6
  - generated-alias-7
  exclusions:
  - target: Unselected scientific claims and source families
    reason: Identity, salt/stereochemistry disputes, roles, components, concentrations,
      occurrence interpretation, the seven generic-alias policy cases and other Rule
      K obligations are not adjudicated by this bounded claim review.
targets:
- target_id: generated-alias-1
  path: reports/sssom_scientific_curation_20261101/audit669/seven-alias-apply.before.tsv
  selector: '{"object_id": "CHEBI:48430", "predicate_id": "skos:broadMatch", "subject_id":
    "MIM:4-Methyl-2-oxopentanoic_Acid_Sodium_Salt", "token": "4-Methyl-2-oxovaleric
    acid"}'
  label: MIM:4-Methyl-2-oxopentanoic_Acid_Sodium_Salt / 4-Methyl-2-oxovaleric acid
  kind: snapshot_row
  record_class: SSSOM other alias
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/4-Methyl-2-oxopentanoic_Acid_Sodium_Salt.yaml
    role: maintained scientific owner
  - repository: CultureBotAI/MediaIngredientMech
    path: scripts/retire_reviewed_generated_aliases.py
    role: bounded generated-alias correction; native generator remains external CLAW
- target_id: generated-alias-2
  path: reports/sssom_scientific_curation_20261101/audit669/seven-alias-apply.before.tsv
  selector: '{"object_id": "CHEBI:32139", "predicate_id": "skos:broadMatch", "subject_id":
    "MIM:84_GL_NaHCO3_Solution", "token": "NaHCO3"}'
  label: MIM:84_GL_NaHCO3_Solution / NaHCO3
  kind: snapshot_row
  record_class: SSSOM other alias
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/84_GL_NaHCO3_Solution.yaml
    role: maintained scientific owner
  - repository: CultureBotAI/MediaIngredientMech
    path: scripts/retire_reviewed_generated_aliases.py
    role: bounded generated-alias correction; native generator remains external CLAW
- target_id: generated-alias-3
  path: reports/sssom_scientific_curation_20261101/audit669/seven-alias-apply.before.tsv
  selector: '{"object_id": "CHEBI:17750", "predicate_id": "skos:broadMatch", "subject_id":
    "MIM:Betaine_Hydrochloride", "token": "Betaine x H2O"}'
  label: MIM:Betaine_Hydrochloride / Betaine x H2O
  kind: snapshot_row
  record_class: SSSOM other alias
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Betaine_Hydrochloride.yaml
    role: maintained scientific owner
  - repository: CultureBotAI/MediaIngredientMech
    path: scripts/retire_reviewed_generated_aliases.py
    role: bounded generated-alias correction; native generator remains external CLAW
- target_id: generated-alias-4
  path: reports/sssom_scientific_curation_20261101/audit669/seven-alias-apply.before.tsv
  selector: '{"object_id": "CHEBI:17369", "predicate_id": "skos:broadMatch", "subject_id":
    "MIM:D-Mannose_6-phosphate_Sodium_Salt", "token": "Mannose-6-Phosphate"}'
  label: MIM:D-Mannose_6-phosphate_Sodium_Salt / Mannose-6-Phosphate
  kind: snapshot_row
  record_class: SSSOM other alias
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-Mannose_6-phosphate_Sodium_Salt.yaml
    role: maintained scientific owner
  - repository: CultureBotAI/MediaIngredientMech
    path: scripts/retire_reviewed_generated_aliases.py
    role: bounded generated-alias correction; native generator remains external CLAW
- target_id: generated-alias-5
  path: reports/sssom_scientific_curation_20261101/audit669/seven-alias-apply.before.tsv
  selector: '{"object_id": "CHEBI:39005", "predicate_id": "skos:broadMatch", "subject_id":
    "MIM:MES_Hydrat", "token": "MES [2-(N-morpholino) ethane sulfonic acid]"}'
  label: MIM:MES_Hydrat / MES [2-(N-morpholino) ethane sulfonic acid]
  kind: snapshot_row
  record_class: SSSOM other alias
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/MES_Hydrat.yaml
    role: maintained scientific owner
  - repository: CultureBotAI/MediaIngredientMech
    path: scripts/retire_reviewed_generated_aliases.py
    role: bounded generated-alias correction; native generator remains external CLAW
- target_id: generated-alias-6
  path: reports/sssom_scientific_curation_20261101/audit669/seven-alias-apply.before.tsv
  selector: '{"object_id": "CHEBI:15978", "predicate_id": "skos:broadMatch", "subject_id":
    "MIM:Sn-glycerol_3-phosphate_Bis_Cyclohexylammonium_Salt", "token": "Glycerol
    3-phosphate"}'
  label: MIM:Sn-glycerol_3-phosphate_Bis_Cyclohexylammonium_Salt / Glycerol 3-phosphate
  kind: snapshot_row
  record_class: SSSOM other alias
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sn-glycerol_3-phosphate_Bis_Cyclohexylammonium_Salt.yaml
    role: maintained scientific owner
  - repository: CultureBotAI/MediaIngredientMech
    path: scripts/retire_reviewed_generated_aliases.py
    role: bounded generated-alias correction; native generator remains external CLAW
- target_id: generated-alias-7
  path: reports/sssom_scientific_curation_20261101/audit669/seven-alias-apply.before.tsv
  selector: '{"object_id": "CHEBI:132103", "predicate_id": "skos:exactMatch", "subject_id":
    "MIM:Sodium_Perchlorate", "token": "Sodium perchlorate monohydrate"}'
  label: MIM:Sodium_Perchlorate / Sodium perchlorate monohydrate
  kind: snapshot_row
  record_class: SSSOM other alias
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sodium_Perchlorate.yaml
    role: maintained scientific owner
  - repository: CultureBotAI/MediaIngredientMech
    path: scripts/retire_reviewed_generated_aliases.py
    role: bounded generated-alias correction; native generator remains external CLAW
checks:
- check_id: scientific-form-comparisons
  name: Primary database and maintained-form comparisons
  status: passed
  required: true
  summary: All seven selected distinctions were checked against saved official ChEBI/PubChem
    assertions or the explicit maintained stock-solution identity. Dictionary absence
    was not used as scientific proof.
  target_ids:
  - generated-alias-1
  - generated-alias-2
  - generated-alias-3
  - generated-alias-4
  - generated-alias-5
  - generated-alias-6
  - generated-alias-7
  evidence_ids:
  - owner-1
  - source-1-1
  - source-1-2
  - owner-2
  - source-2-1
  - owner-3
  - source-3-1
  - source-3-2
  - owner-4
  - source-4-1
  - source-4-2
  - owner-5
  - source-5-1
  - source-5-2
  - owner-6
  - source-6-1
  - source-6-2
  - owner-7
  - source-7-1
  - source-7-2
  - source-7-3
  - semantics
- check_id: alias-final-code-regressions
  name: alias final code regressions
  status: passed
  required: true
  summary: All 48 scoped final-code tests passed.
  target_ids:
  - generated-alias-1
  - generated-alias-2
  - generated-alias-3
  - generated-alias-4
  - generated-alias-5
  - generated-alias-6
  - generated-alias-7
  command: uv run pytest -q --no-cov tests/test_reject_carnitinamide_synonym.py tests/test_retire_reviewed_generated_aliases.py
    tests/test_label_index_precedence.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - regression-receipt
- check_id: final-scoped-alias-verification
  name: final scoped alias verification
  status: passed
  required: true
  summary: Final selective payload, unchanged owner, exact baseline and withheld-disposition
    checks passed.
  target_ids:
  - generated-alias-1
  - generated-alias-2
  - generated-alias-3
  - generated-alias-4
  - generated-alias-5
  - generated-alias-6
  - generated-alias-7
  command: python ../audit669/verify_final_alias_scope.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - final-proof
evidence:
- evidence_id: semantics
  kind: authority
  reference: MAPPING_SEMANTICS.md
  accessed_at: '2026-11-01T00:57:10.014126Z'
  support: supports
  summary: The contract distinguishes salts, hydrates, stock solutions and their parent
    substances; source alias scope must not collapse those identities.
  locator: Section 3
  snapshot_sha256: 94aad13ea0fc3df82a37383f388f41432b607b04cac61ae5792ce1a381aef805
- evidence_id: original-claims
  kind: record_content
  reference: reports/sssom_scientific_curation_20261101/audit669/seven-alias-apply.before.tsv
  accessed_at: '2026-11-01T00:57:10.014126Z'
  support: supports
  summary: Frozen pre-transform canonical preserves each exact original triple and
    removed other token. This is an intermediate snapshot, not the final canonical.
  locator: Seven target selectors
  snapshot_sha256: 757643bf567a992c2b89cebb74e3c6410fcf944b93ca3663c8338ba07ae22b18
- evidence_id: migration
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/audit669/seven-alias-apply.json
  accessed_at: '2026-11-01T00:57:10.014126Z'
  support: supports
  summary: Receipt preserves all seven unchanged owner hashes and verifies independent
    omission in the final native generated candidate; baseline obligations retired
    45→38 without inventing YAML rejection entries.
  snapshot_sha256: 021d2cf58f890cf321eef26956fb294bdb50f3f5a11669fcd28295fc348fdb63
- evidence_id: final-proof
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/audit669/final-scoped-verification.json
  accessed_at: '2026-11-01T00:57:10.014126Z'
  support: supports
  summary: All seven final rows differ only in other from their frozen pre-transform
    row; every owner hash is unchanged, all 18 owner rows remain WITHHOLD, and remaining
    38 baseline pairs including seven YAML policy cases persist.
  locator: seven_aliases; exact_remaining_baseline_pairs_preserved
  snapshot_sha256: 4536bdc56695a08d80d7afd04f1cef4007f8064911b58b64f84b98d7870c122c
- evidence_id: regression-receipt
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/audit669/logs/alias_final_code_regressions.json
  accessed_at: '2026-11-01T00:57:10.014126Z'
  support: supports
  summary: All 48 final maintained-code tests passed, including owner changes, missing/duplicate/changed
    selectors, candidate disagreement, byte preservation and receipt/backup collisions.
  snapshot_sha256: e34b2a139a933d22e7997147f299002df4899c3fa1436fc3c97523e88fef7079
- evidence_id: mapping-receipt
  kind: validation
  reference: reports/sssom_completion_20260921/mapping_changes/issue669-1003-scoped-alias-corrections.json
  accessed_at: '2026-11-01T00:57:10.014126Z'
  support: supports
  summary: Native approval-free mapping receipt binds the seven changed rows to unchanged
    owner bytes and preserves withheld status.
  snapshot_sha256: 00049aa1d2b19565020d4ecbec999fc723d2cf5954968ec6bf5cebdc0da73f34
- evidence_id: owner-1
  kind: record_content
  reference: data/ingredients/mapped/4-Methyl-2-oxopentanoic_Acid_Sodium_Salt.yaml
  accessed_at: '2026-11-01T00:57:10.014126Z'
  support: supports
  summary: Maintained record identity/form inspected for this exact alias-scope contrast.
    No other claim is scientifically approved.
  locator: identifier; preferred_term; ontology_mapping; supplied-form and source
    history
  snapshot_sha256: 8d5da3b1c891a79adf823a2ea778b04ef2658cc6bc175469631251c3874a314b
- evidence_id: source-1-1
  kind: database
  reference: reports/sssom_scientific_curation_20261101/audit669/sources/PubChem-CAS-4502-00-5.json
  accessed_at: '2026-11-01T00:57:10.014126Z'
  support: supports
  summary: PubChem CAS 4502-00-5 is sodium 4-methyl-2-oxovalerate, C6H9NaO3; ChEBI:48430
    is the acid C6H10O3. The parent preferred name cannot assert exact substance identity
    for this sodium salt.
  locator: Official response term/properties; source URL and capture time in companion
    manifests
  snapshot_sha256: fbf0e32a45db47198f99697349812100fbb711a8d44c64c91b449af99af3ede7
- evidence_id: source-1-2
  kind: database
  reference: reports/sssom_scientific_curation_20261101/audit669/sources/CHEBI_48430.ols.json
  accessed_at: '2026-11-01T00:57:10.014126Z'
  support: supports
  summary: PubChem CAS 4502-00-5 is sodium 4-methyl-2-oxovalerate, C6H9NaO3; ChEBI:48430
    is the acid C6H10O3. The parent preferred name cannot assert exact substance identity
    for this sodium salt.
  locator: Official response term/properties; source URL and capture time in companion
    manifests
  snapshot_sha256: 9791f4da2a3cdb25de4cfd7cb3990d288735afb7aab155ffca8b070661471f8c
- evidence_id: owner-2
  kind: record_content
  reference: data/ingredients/mapped/84_GL_NaHCO3_Solution.yaml
  accessed_at: '2026-11-01T00:57:10.014126Z'
  support: supports
  summary: Maintained record identity/form inspected for this exact alias-scope contrast.
    No other claim is scientifically approved.
  locator: identifier; preferred_term; ontology_mapping; supplied-form and source
    history
  snapshot_sha256: 1a8f4136f2de11105febf3112e5ca27fd95fcf9266ca1bb2283210267f70a509
- evidence_id: source-2-1
  kind: database
  reference: reports/sssom_scientific_curation_20261101/audit669/sources/CHEBI_32139.ols.json
  accessed_at: '2026-11-01T00:57:10.014126Z'
  support: supports
  summary: The maintained identity is explicitly a stock solution kgmicrobe.ingredient:84_gl_nahco3_solution,
    with concentration and solution curation; the owner NaHCO3 is neat sodium hydrogencarbonate
    CHEBI:32139. This is a mixture/concentration boundary, not merely spelling.
  locator: Official response term/properties; source URL and capture time in companion
    manifests
  snapshot_sha256: 51709e2510736d0b63369147b10ec6ffe80d5d5c3a40605381de9b3ed78634c3
- evidence_id: owner-3
  kind: record_content
  reference: data/ingredients/mapped/Betaine_Hydrochloride.yaml
  accessed_at: '2026-11-01T00:57:10.014126Z'
  support: supports
  summary: Maintained record identity/form inspected for this exact alias-scope contrast.
    No other claim is scientifically approved.
  locator: identifier; preferred_term; ontology_mapping; supplied-form and source
    history
  snapshot_sha256: 77cf04f3fafb04a92080656711b7807ed4e9af7c79f7852ffd31a09fe428f4ac
- evidence_id: source-3-1
  kind: database
  reference: reports/sssom_scientific_curation_20261101/audit669/sources/PubChem-CAS-590-46-5.json
  accessed_at: '2026-11-01T00:57:10.014126Z'
  support: supports
  summary: PubChem CAS 590-46-5 is betaine chloride C5H12ClNO2; the owner ChEBI:91242
    is glycine betaine monohydrate C5H11NO2.H2O (CAS 590-47-6). Chloride and hydrate
    identities differ.
  locator: Official response term/properties; source URL and capture time in companion
    manifests
  snapshot_sha256: 1d7c1f0966a710c1734b09575eb4499b1bb0d9749d91ec5cdbf736e9c0fff0e5
- evidence_id: source-3-2
  kind: database
  reference: reports/sssom_scientific_curation_20261101/audit669/sources/CHEBI_91242.ols.json
  accessed_at: '2026-11-01T00:57:10.014126Z'
  support: supports
  summary: PubChem CAS 590-46-5 is betaine chloride C5H12ClNO2; the owner ChEBI:91242
    is glycine betaine monohydrate C5H11NO2.H2O (CAS 590-47-6). Chloride and hydrate
    identities differ.
  locator: Official response term/properties; source URL and capture time in companion
    manifests
  snapshot_sha256: 245044748707015ad714c1bbb2deae5793806cc83a59a100b847b1357acb5cf2
- evidence_id: owner-4
  kind: record_content
  reference: data/ingredients/mapped/D-Mannose_6-phosphate_Sodium_Salt.yaml
  accessed_at: '2026-11-01T00:57:10.014126Z'
  support: supports
  summary: Maintained record identity/form inspected for this exact alias-scope contrast.
    No other claim is scientifically approved.
  locator: identifier; preferred_term; ontology_mapping; supplied-form and source
    history
  snapshot_sha256: 280c8b5687a3ccd348984cd3b37518d2d1d298a80d1cd0c2b9a911b06f9a0535
- evidence_id: source-4-1
  kind: database
  reference: reports/sssom_scientific_curation_20261101/audit669/sources/PubChem-CAS-70442-25-0.json
  accessed_at: '2026-11-01T00:57:10.014126Z'
  support: supports
  summary: PubChem CAS 70442-25-0 is sodium mannose 6-phosphate C6H12NaO9P; ChEBI:17369
    is D-mannose 6-phosphate C6H13O9P. The sodium counterion is chemically material.
  locator: Official response term/properties; source URL and capture time in companion
    manifests
  snapshot_sha256: d5b3975ada83fe9c6250bbfbc51dd37dd282df434d0d9b4ead4e55a97c023e54
- evidence_id: source-4-2
  kind: database
  reference: reports/sssom_scientific_curation_20261101/audit669/sources/CHEBI_17369.ols.json
  accessed_at: '2026-11-01T00:57:10.014126Z'
  support: supports
  summary: PubChem CAS 70442-25-0 is sodium mannose 6-phosphate C6H12NaO9P; ChEBI:17369
    is D-mannose 6-phosphate C6H13O9P. The sodium counterion is chemically material.
  locator: Official response term/properties; source URL and capture time in companion
    manifests
  snapshot_sha256: d722a50189087d6b8141cc28d7d7ca893e0d97dfb47221dce598de9f3b03396f
- evidence_id: owner-5
  kind: record_content
  reference: data/ingredients/mapped/MES_Hydrat.yaml
  accessed_at: '2026-11-01T00:57:10.014126Z'
  support: supports
  summary: Maintained record identity/form inspected for this exact alias-scope contrast.
    No other claim is scientifically approved.
  locator: identifier; preferred_term; ontology_mapping; supplied-form and source
    history
  snapshot_sha256: 24292497ec7bae482bb3611b8afb9cd1f795332d655be8900f4c59f8d929ebb6
- evidence_id: source-5-1
  kind: database
  reference: reports/sssom_scientific_curation_20261101/audit669/sources/PubChem-CAS-145224-94-8.json
  accessed_at: '2026-11-01T00:57:10.014126Z'
  support: supports
  summary: PubChem CAS 145224-94-8 is MES hydrate C6H15NO5S; ChEBI:39005 is MES C6H13NO4S.
    This evidence supports a form boundary independent of KG alias availability.
  locator: Official response term/properties; source URL and capture time in companion
    manifests
  snapshot_sha256: 0b92fe032b10fa400e8d1a036b35b057dd4ce92e77ab8694650bc672d8c27e46
- evidence_id: source-5-2
  kind: database
  reference: reports/sssom_scientific_curation_20261101/audit669/sources/CHEBI_39005.ols.json
  accessed_at: '2026-11-01T00:57:10.014126Z'
  support: supports
  summary: PubChem CAS 145224-94-8 is MES hydrate C6H15NO5S; ChEBI:39005 is MES C6H13NO4S.
    This evidence supports a form boundary independent of KG alias availability.
  locator: Official response term/properties; source URL and capture time in companion
    manifests
  snapshot_sha256: 0924879ff890ef5624ea83cc42f75ca645247948e1f62270aef5f45cfd487c4c
- evidence_id: owner-6
  kind: record_content
  reference: data/ingredients/mapped/Sn-glycerol_3-phosphate_Bis_Cyclohexylammonium_Salt.yaml
  accessed_at: '2026-11-01T00:57:10.014126Z'
  support: supports
  summary: Maintained record identity/form inspected for this exact alias-scope contrast.
    No other claim is scientifically approved.
  locator: identifier; preferred_term; ontology_mapping; supplied-form and source
    history
  snapshot_sha256: 185d299a1d5a117e5ce42e2826e3f9fb83cba57459c5fc7e09f2dcf263a660f1
- evidence_id: source-6-1
  kind: database
  reference: reports/sssom_scientific_curation_20261101/audit669/sources/PubChem-CAS-29849-82-9.json
  accessed_at: '2026-11-01T00:57:10.014126Z'
  support: supports
  summary: PubChem CAS 29849-82-9 is the bis(cyclohexylammonium) salt C15H35N2O6P;
    ChEBI:15978 is the free acid C3H9O6P. Removing the unqualified parent alias does
    not require guessing the salt identity.
  locator: Official response term/properties; source URL and capture time in companion
    manifests
  snapshot_sha256: 2a1ec78b1a642194de4426cfd207c4986459fc5d78c7b6939db700e83b34c5ef
- evidence_id: source-6-2
  kind: database
  reference: reports/sssom_scientific_curation_20261101/audit669/sources/CHEBI_15978.ols.json
  accessed_at: '2026-11-01T00:57:10.014126Z'
  support: supports
  summary: PubChem CAS 29849-82-9 is the bis(cyclohexylammonium) salt C15H35N2O6P;
    ChEBI:15978 is the free acid C3H9O6P. Removing the unqualified parent alias does
    not require guessing the salt identity.
  locator: Official response term/properties; source URL and capture time in companion
    manifests
  snapshot_sha256: 565d77bfa309af5e1d427dea7d26f7266d815189a470203fd82c4a0cfcf1e3e1
- evidence_id: owner-7
  kind: record_content
  reference: data/ingredients/mapped/Sodium_Perchlorate.yaml
  accessed_at: '2026-11-01T00:57:10.014126Z'
  support: supports
  summary: Maintained record identity/form inspected for this exact alias-scope contrast.
    No other claim is scientifically approved.
  locator: identifier; preferred_term; ontology_mapping; supplied-form and source
    history
  snapshot_sha256: 5b8a68b008ebce2e98c040b9dfff7b5b16f2370b320bb77cf0d3db32e680e0e0
- evidence_id: source-7-1
  kind: database
  reference: reports/sssom_scientific_curation_20261101/audit669/sources/PubChem-CAS-7601-89-0.json
  accessed_at: '2026-11-01T00:57:10.014126Z'
  support: supports
  summary: PubChem CAS 7601-89-0 is sodium perchlorate ClNaO4; CAS 7791-07-3 is monohydrate
    ClH2NaO5. ChEBI:132103 confirms the anhydrous subject.
  locator: Official response term/properties; source URL and capture time in companion
    manifests
  snapshot_sha256: 72b3f22d2373b88510295b51144228c0dcb2a000c67588305579fd349d496ec9
- evidence_id: source-7-2
  kind: database
  reference: reports/sssom_scientific_curation_20261101/audit669/sources/PubChem-CAS-7791-07-3.json
  accessed_at: '2026-11-01T00:57:10.014126Z'
  support: supports
  summary: PubChem CAS 7601-89-0 is sodium perchlorate ClNaO4; CAS 7791-07-3 is monohydrate
    ClH2NaO5. ChEBI:132103 confirms the anhydrous subject.
  locator: Official response term/properties; source URL and capture time in companion
    manifests
  snapshot_sha256: 5da16842ccf25f8fd40b70737d350f3a96e9e65dde797bda446db2df6e6baf24
- evidence_id: source-7-3
  kind: database
  reference: reports/sssom_scientific_curation_20261101/audit669/sources/CHEBI_132103.ols.json
  accessed_at: '2026-11-01T00:57:10.014126Z'
  support: supports
  summary: PubChem CAS 7601-89-0 is sodium perchlorate ClNaO4; CAS 7791-07-3 is monohydrate
    ClH2NaO5. ChEBI:132103 confirms the anhydrous subject.
  locator: Official response term/properties; source URL and capture time in companion
    manifests
  snapshot_sha256: b9c17be4c36719cbf8972e959153772ad12b6efffaba915f6a84d219cf16eb01
assessments:
- assessment_id: alias-ruling-1
  area: nomenclature
  topic: 'Exact token scope: 4-Methyl-2-oxovaleric acid'
  outcome: supported
  summary: PubChem CAS 4502-00-5 is sodium 4-methyl-2-oxovalerate, C6H9NaO3; ChEBI:48430
    is the acid C6H10O3. The parent preferred name cannot assert exact substance identity
    for this sodium salt. The exact selected token is therefore not published as an
    unqualified same-substance alias of this maintained form; other fields, YAML and
    native holds remain unchanged.
  target_ids:
  - generated-alias-1
  evidence_ids:
  - semantics
  - original-claims
  - final-proof
  - migration
  - owner-1
  - source-1-1
  - source-1-2
- assessment_id: alias-ruling-2
  area: nomenclature
  topic: 'Exact token scope: NaHCO3'
  outcome: supported
  summary: The maintained identity is explicitly a stock solution kgmicrobe.ingredient:84_gl_nahco3_solution,
    with concentration and solution curation; the owner NaHCO3 is neat sodium hydrogencarbonate
    CHEBI:32139. This is a mixture/concentration boundary, not merely spelling. The
    exact selected token is therefore not published as an unqualified same-substance
    alias of this maintained form; other fields, YAML and native holds remain unchanged.
  target_ids:
  - generated-alias-2
  evidence_ids:
  - semantics
  - original-claims
  - final-proof
  - migration
  - owner-2
  - source-2-1
- assessment_id: alias-ruling-3
  area: nomenclature
  topic: 'Exact token scope: Betaine x H2O'
  outcome: supported
  summary: PubChem CAS 590-46-5 is betaine chloride C5H12ClNO2; the owner ChEBI:91242
    is glycine betaine monohydrate C5H11NO2.H2O (CAS 590-47-6). Chloride and hydrate
    identities differ. The exact selected token is therefore not published as an unqualified
    same-substance alias of this maintained form; other fields, YAML and native holds
    remain unchanged.
  target_ids:
  - generated-alias-3
  evidence_ids:
  - semantics
  - original-claims
  - final-proof
  - migration
  - owner-3
  - source-3-1
  - source-3-2
- assessment_id: alias-ruling-4
  area: nomenclature
  topic: 'Exact token scope: Mannose-6-Phosphate'
  outcome: supported
  summary: PubChem CAS 70442-25-0 is sodium mannose 6-phosphate C6H12NaO9P; ChEBI:17369
    is D-mannose 6-phosphate C6H13O9P. The sodium counterion is chemically material.
    The exact selected token is therefore not published as an unqualified same-substance
    alias of this maintained form; other fields, YAML and native holds remain unchanged.
  target_ids:
  - generated-alias-4
  evidence_ids:
  - semantics
  - original-claims
  - final-proof
  - migration
  - owner-4
  - source-4-1
  - source-4-2
- assessment_id: alias-ruling-5
  area: nomenclature
  topic: 'Exact token scope: MES [2-(N-morpholino) ethane sulfonic acid]'
  outcome: supported
  summary: PubChem CAS 145224-94-8 is MES hydrate C6H15NO5S; ChEBI:39005 is MES C6H13NO4S.
    This evidence supports a form boundary independent of KG alias availability. The
    exact selected token is therefore not published as an unqualified same-substance
    alias of this maintained form; other fields, YAML and native holds remain unchanged.
  target_ids:
  - generated-alias-5
  evidence_ids:
  - semantics
  - original-claims
  - final-proof
  - migration
  - owner-5
  - source-5-1
  - source-5-2
- assessment_id: alias-ruling-6
  area: nomenclature
  topic: 'Exact token scope: Glycerol 3-phosphate'
  outcome: supported
  summary: PubChem CAS 29849-82-9 is the bis(cyclohexylammonium) salt C15H35N2O6P;
    ChEBI:15978 is the free acid C3H9O6P. Removing the unqualified parent alias does
    not require guessing the salt identity. The exact selected token is therefore
    not published as an unqualified same-substance alias of this maintained form;
    other fields, YAML and native holds remain unchanged.
  target_ids:
  - generated-alias-6
  evidence_ids:
  - semantics
  - original-claims
  - final-proof
  - migration
  - owner-6
  - source-6-1
  - source-6-2
- assessment_id: alias-ruling-7
  area: nomenclature
  topic: 'Exact token scope: Sodium perchlorate monohydrate'
  outcome: supported
  summary: PubChem CAS 7601-89-0 is sodium perchlorate ClNaO4; CAS 7791-07-3 is monohydrate
    ClH2NaO5. ChEBI:132103 confirms the anhydrous subject. The exact selected token
    is therefore not published as an unqualified same-substance alias of this maintained
    form; other fields, YAML and native holds remain unchanged.
  target_ids:
  - generated-alias-7
  evidence_ids:
  - semantics
  - original-claims
  - final-proof
  - migration
  - owner-7
  - source-7-1
  - source-7-2
  - source-7-3
findings: []
actions: []
limitations:
- This is a claim-specific self-review, not independent review or whole-record chemical
  approval.
- Historical validation stamps are retained provenance; no fresh scientific approval
  or role support is inferred.
- Native scientific release holds remain authoritative; a passing scoped review does
  not promote assertions.
- The source record can still contain unrelated incomplete or contradictory scientific
  claims; these are outside this alias-only ruling. In particular, stock concentration/source
  details and full molecular or role assertions are not certified.
- 'The seven YAML generic-name policy cases, 23 pairs overlapping active PR #912,
  and 8 identity/alias-scope cases remain open; no full candidate promotion or family
  merge follows.'
- Source database assertions establish the stated chemical-form contrasts; they are
  not primary experimental studies or evidence of biological roles.
- Whole repository data/release validators and independent review are reported in
  the parent run; this review only states its listed checks.
links:
- https://github.com/CultureBotAI/MediaIngredientMech/issues/669#issuecomment-6551360500
- https://github.com/CultureBotAI/MediaIngredientMech/issues/1004
- https://github.com/CultureBotAI/MediaIngredientMech/issues/1005
```
