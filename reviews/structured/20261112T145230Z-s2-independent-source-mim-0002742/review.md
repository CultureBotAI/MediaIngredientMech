# Cerium nitrate MeSH entity-type wording — independent exact S2 correction review

- Review: 20261112T145230Z-s2-independent-source-mim-0002742
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-11-12T14:45:28.503511Z
- Finished UTC: 2026-11-12T14:52:30.709893Z
- Reviewer: /root/invalid_cas_science_skeptic (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Support only the descriptor-to-NLM-Concept wording correction. The hexahydrate identity and asymmetric broader mapping remain unchanged. Support is limited to the exact corrective delta; every residual hold remains and no source binding, role, generated-row or release approval is conferred.

## Scope And Provenance

One exact inspected S2 source-correction snapshot payload, including entire before/after record, declared delta, primary evidence and all inherited/residual holds.

Selection: .temp/cumulative-source-successor-inspected-s2-v1/payloads.json selector MIM:0002742
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base c1cc5b2828068cb49c902e07a1016a5deb83227f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| MIM:0002742 | .temp/cumulative-source-successor-inspected-s2-v1/payloads.json # MIM:0002742 | snapshot_row | CeNO33_X_6_H2O exact proposed correction |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native current source and target inspection | passed | True | MIM:0002742 | Actual S2 native inspect completed with exact current HEAD, all source/evidence pins and snapshot-row target. |
| Native strict LinkML validation | passed | True | MIM:0002742 | All 11 exact proposed records passed; zero files or rows with errors. |
| Independent exact delta and provenance audit | passed | True | MIM:0002742 | 149 bounded checks across 11 owners passed; this owner retains its permanent ID, original history and exact inherited holds. Ignored files included in 2957-owner duplicate check. |
| Independent source/form/method assessment | passed | True | MIM:0002742 | Support only the descriptor-to-NLM-Concept wording correction. The hexahydrate identity and asymmetric broader mapping remain unchanged. |
| Post-application full data/release gates | not_applicable | False | MIM:0002742 | No source application or generated export is being reviewed here. Full qc, SSSOM synchronization, supported KGX and final-row review remain parent-owned prerequisites after actual native application. |
| iModulon structured adapters | not_applicable | False | MIM:0002742 | No gene, locus, expression module or transcriptomic identity claim is part of this chemical/material correction. |
| Native Engine-A canonical term label gate | passed | True | MIM:0002742 | Canonical label validator exited zero. |

## Scientific And Domain Assessments

### Bounded source correction with permanent identity and retained scientific holds

identity: supported. Targets: MIM:0002742.

Support only the descriptor-to-NLM-Concept wording correction. The hexahydrate identity and asymmetric broader mapping remain unchanged.

The captured authoritative M0319657 JSON explicitly types the target as mesh vocab Concept, labels it cerium nitrate (Ce(+3)), and identifies its preferred term. I checked that the exact proposed text substitution is the only ontology evidence change. The current source specifies Ce(NO3)3 x 6 H2O/CAS 10294-41-4; the proposal preserves the six waters, hydrate formula, supplied form and NARROW_MATCH. Calling this Concept an exact hydrate would be wrong, but the afterimage explicitly denies that and preserves the separate CAS identity.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| exact-proposal | .temp/cumulative-source-successor-inputs-s2-v1/proposals/MIM-0002742.yaml | supports | Complete current afterimage read and compared against the entire current owner and declared delta. |
| current-owner | data/ingredients/mapped/CeNO33_X_6_H2O.yaml | context_only | Entire current beforeimage, including all history, mapping, aliases, properties and remaining claim restrictions. |
| mapping-semantics | MAPPING_SEMANTICS.md | supports | Native permanent-ID, form-specific identity, method provenance, rejection and typed-mapping requirements. |
| primary-1 | .temp/cumulative-source-successor-inputs-s2-v1/evidence/955fd9aa39af3a86c3a6457e55cc544140df52f5ba7a196a572e2a71a563338e/cerium-meshM0319657.json | supports | Inspected cerium-meshM0319657.json for the specific identity/form/method conclusion; scope and limits stated in the independent assessment. |
| own-science | .temp/s2-eleven-skeptic-native-v1/SCIENTIFIC-ASSESSMENTS.json; assessments.MIM:0002742 | supports | The captured authoritative M0319657 JSON explicitly types the target as mesh vocab Concept, labels it cerium nitrate (Ce(+3)), and identifies its preferred term. I checked that the exact proposed text substitution is the only ontology evidence change. The current source specifies Ce(NO3)3 x 6 H2O/CAS 10294-41-4; the proposal preserves the six waters, hydrate formula, supplied form and NARROW_MATCH. Calling this Concept an exact hydrate would be wrong, but the afterimage explicitly denies that and preserves the separate CAS identity. |
| exact-delta-audit | .temp/s2-eleven-skeptic-native-v1/PROPOSAL-AUDIT.json; owners[mim_id=MIM:0002742] | supports | Actual independent audit: source pins, delta values, persistent identity, old history, aliases, holds and unchanged claim fields. |
| strict-validation | .temp/s2-eleven-skeptic-native-v1/strict-result.json | supports | Native strict schema check: 11 exact proposals; zero error rows. |
| term-validation | .temp/s2-eleven-skeptic-native-v1/term-results.json; target_id=MIM:0002742 | supports | Actual documented Engine-A check or native non-OBO safety skip; no guessed adapter result. |
| current-context | .temp/cumulative-source-successor-inspected-s2-v1/context.json | context_only | Complete inspected source-successor context with original 1879 cases, 1022 origin-accounting entries, current inventory and all historical obligations. |
| residual-holds | .temp/cumulative-source-successor-inspected-s2-v1/payloads.json; MIM:0002742 | context_only | Exact inherited equals residual holds remain binding; this review does not close earlier scientific findings. |

## Limits And Additional Notes

- No new hydrate identity, SNOMED adoption, actual supplier attribution, broadMatch-to-subclass inference, role or publication support is granted. Existing source/form and all prior release restrictions remain.
- All exact residual_holds_json entries remain binding, including original worker reviews, source/origin context, suppression obligations and prior full-row dispositions. Empty findings means no newly identified blocker in this corrective delta, not that inherited findings are resolved.
- This is an assessment of a frozen source-correction payload before application, not a complete-record publication pass. Full corpus synchronization, scientific source-binding reviews, actual revised SSSOM/companion exports and content-bound release gates remain pending.
- Prior draft observations and old S reviews are retained as history; this bundle is tied to the inspected current S2 head and exact bytes. No paid provider query, GitHub mutation, source edit, generation or native apply was performed.
- Maintained owner before: data/ingredients/mapped/CeNO33_X_6_H2O.yaml; declared after location: data/ingredients/mapped/CeNO33_X_6_H2O.yaml. Future application belongs to the reviewed native curation-successor writer; do not hand-edit aggregates or generated products.
- The seven admission dimensions use stable_id_adoption.encoded for structured JSON; hashes use the native canonical payload/delta digest.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261112T145230Z-s2-independent-source-mim-0002742
kind: record
repository: CultureBotAI/MediaIngredientMech
title: Cerium nitrate MeSH entity-type wording — independent exact S2 correction review
started_at: '2026-11-12T14:45:28.503511Z'
finished_at: '2026-11-12T14:52:30.709893Z'
reviewer:
  identity: /root/invalid_cas_science_skeptic
  kind: agent
  independence: independent
  independence_basis: Separate skeptical agent from the proposal author /root/actual_candidate_science_primary
    and the implementation/coordinator. I personally read actual current beforeimages,
    exact afterimage changes, primary captures and inherited restrictions, challenged
    chemical scope and evidence method, and authored these conclusions. Earlier drafts
    are groundwork, not copied positive votes.
skill: review-yaml-record
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Support only the descriptor-to-NLM-Concept wording correction. The hexahydrate
  identity and asymmetric broader mapping remain unchanged. Support is limited to
  the exact corrective delta; every residual hold remains and no source binding, role,
  generated-row or release approval is conferred.
source:
  git_revision: c1cc5b2828068cb49c902e07a1016a5deb83227f
  state: working_tree
  inputs:
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 4f3142cc2c7e8884ffc049ad81fd9b6fcf076bd40579b43d80d8652679630bd1
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/0b5fc3b58b79396b37ba97c1d16ecf11307002f0e2c4074241b97c9c566e2f00/CONFIGURED-ONTOLOGY-LOOKUP.json
    sha256: 0b5fc3b58b79396b37ba97c1d16ecf11307002f0e2c4074241b97c9c566e2f00
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/126a8e112f71c0b692a9e60a1d2663555864ac49104a8af242769ed56b5f9614/HISTORY-OBLIGATIONS.json
    sha256: 126a8e112f71c0b692a9e60a1d2663555864ac49104a8af242769ed56b5f9614
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/13ee219495257a22e816d3c621fa723de868152b71477cd2f96656819e6e9ae0/PRIMARY-IDENTITY-CONCLUSION.json
    sha256: 13ee219495257a22e816d3c621fa723de868152b71477cd2f96656819e6e9ae0
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/149eda7e851924447adcbfaf8a97b89479fc9db4c8bbbf00592827b47c38a9a9/Lysozyme.yaml
    sha256: 149eda7e851924447adcbfaf8a97b89479fc9db4c8bbbf00592827b47c38a9a9
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/185a1586629a83078a8e6178bea27f729c37359ee63bac42c6f578f738da8773/1229.json
    sha256: 185a1586629a83078a8e6178bea27f729c37359ee63bac42c6f578f738da8773
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/20222f9e374f29ad8a9ddac518236e8f6aca275c8395730b08c0e2588426dbac/SUPPRESSION-OBLIGATIONS.json
    sha256: 20222f9e374f29ad8a9ddac518236e8f6aca275c8395730b08c0e2588426dbac
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/26e1e00060055037cb37b633b1ea445c548aabd2ae66fa73d3a001eb3f01a13e/D-limonene.historical-review.md
    sha256: 26e1e00060055037cb37b633b1ea445c548aabd2ae66fa73d3a001eb3f01a13e
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/299204d51c81d2c02e4b0d5704d8dffe8d3b966fafb1344a383fd53e0d2859e5/CACHED-ISSUE-HISTORY.json
    sha256: 299204d51c81d2c02e4b0d5704d8dffe8d3b966fafb1344a383fd53e0d2859e5
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/2e7da2023168a61581b6cbdf2cac9243e4b46073301dc6f35937aee308888677/D-limonene.diff
    sha256: 2e7da2023168a61581b6cbdf2cac9243e4b46073301dc6f35937aee308888677
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/307b17477f423085720997a2c8dfe8dcd7ad8abcb304469e79505998a672d336/primary-retrieval-v1.json
    sha256: 307b17477f423085720997a2c8dfe8dcd7ad8abcb304469e79505998a672d336
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/33cf55a9b07832e45af2458741aa1dc6ce5669400bd446bf531f48667f261339/HANDOFF.json
    sha256: 33cf55a9b07832e45af2458741aa1dc6ce5669400bd446bf531f48667f261339
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/35658dc81876bedbc0b621d9575ef9088006fecc8252a551eb9ece5f202e9c97/INPUT-PINS.json
    sha256: 35658dc81876bedbc0b621d9575ef9088006fecc8252a551eb9ece5f202e9c97
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/3d2b7216e0a7099bb9274feb2cb8a45b6db64234a26f0f5f0d58744bbf231dd1/CeNO33_X_6_H2O.yaml
    sha256: 3d2b7216e0a7099bb9274feb2cb8a45b6db64234a26f0f5f0d58744bbf231dd1
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/3d93354758569e5f8f882711c63c5f89951c699a72f9f3aa414ded2e3ca10c3f/mapping-evidence.json
    sha256: 3d93354758569e5f8f882711c63c5f89951c699a72f9f3aa414ded2e3ca10c3f
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/3e587ecd29cfb9e4bd2567a03d27c0fd75aa6f5344b2178e6bdfc2aebb7a4978/D-limonene.before.yaml
    sha256: 3e587ecd29cfb9e4bd2567a03d27c0fd75aa6f5344b2178e6bdfc2aebb7a4978
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/3e587ecd29cfb9e4bd2567a03d27c0fd75aa6f5344b2178e6bdfc2aebb7a4978/D-limonene.yaml
    sha256: 3e587ecd29cfb9e4bd2567a03d27c0fd75aa6f5344b2178e6bdfc2aebb7a4978
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/452c95a2a6aa09f695951170b4d15bf03c6a6a7fd16459a513b2fb42eeb033b1/EXACT-CORPUS-SEARCH.json
    sha256: 452c95a2a6aa09f695951170b4d15bf03c6a6a7fd16459a513b2fb42eeb033b1
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/4556f26a7a1c27256993f5b0346939cdbcd0a2a5a8b6714842575021ccdd5b9d/AUTHOR-ATTESTATION.json
    sha256: 4556f26a7a1c27256993f5b0346939cdbcd0a2a5a8b6714842575021ccdd5b9d
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/4d84bfbb010966647860e5b203cc6003f9ac02f3b87951f99f3b842613bb42c6/sorbitan-recipe-occurrences.json
    sha256: 4d84bfbb010966647860e5b203cc6003f9ac02f3b87951f99f3b842613bb42c6
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/4e2853c22b8ed58d171c48c1853014b412b435506da2cef08c87a1344be76a11/DRAFT-HANDOFF-v2.json
    sha256: 4e2853c22b8ed58d171c48c1853014b412b435506da2cef08c87a1344be76a11
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/4e3c3b691aac234d837d187100d0cea546210c3205e9a5cd78c4e43b39b4159c/chemical-scope-ontology-evidence.json
    sha256: 4e3c3b691aac234d837d187100d0cea546210c3205e9a5cd78c4e43b39b4159c
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/4e951f39e1c8890eb0f6f260dcb7e28edfd18a5b57a191fcb6ef0290507c3be2/L-alpha-Phosphatidylcholine.yaml
    sha256: 4e951f39e1c8890eb0f6f260dcb7e28edfd18a5b57a191fcb6ef0290507c3be2
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/4e971cec7029a881832201d2bd17bfd4c797e00030341d6dfe457cf539aba1c8/Rifamycin.yaml
    sha256: 4e971cec7029a881832201d2bd17bfd4c797e00030341d6dfe457cf539aba1c8
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/515170be9297b049e5a2e3ae8335e7d2290ffeedd17c12b050708db9cb512c99/Sorbitan_Monooleate.yaml
    sha256: 515170be9297b049e5a2e3ae8335e7d2290ffeedd17c12b050708db9cb512c99
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/529bb71759b79adc40e8a15767221679731004eb289486adb36a4e8965cc06dd/mapping-evidence.json
    sha256: 529bb71759b79adc40e8a15767221679731004eb289486adb36a4e8965cc06dd
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/5c10db580fcabb79ebbbbf70b42a20aad95bedebe89669ff5c9506a558b8020b/chebi-4735-live-v1.json
    sha256: 5c10db580fcabb79ebbbbf70b42a20aad95bedebe89669ff5c9506a558b8020b
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/5fe480cd1bb7828c6cefd7ae56397b6a7a86200093f5a83c85dea833650cfb42/web-cas-check-digit-and-pdf-screenshot.txt
    sha256: 5fe480cd1bb7828c6cefd7ae56397b6a7a86200093f5a83c85dea833650cfb42
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/674fc6c1dc380bcd5e9d9f7d61fc9a40b83b2081612399124e4d6501e0683fc3/primary-http-approved.json
    sha256: 674fc6c1dc380bcd5e9d9f7d61fc9a40b83b2081612399124e4d6501e0683fc3
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/6e11b28aaa317fe7fc1451caa1b3618199d9b32dbc5aa340cd3768979be14b69/chebi-748872.json
    sha256: 6e11b28aaa317fe7fc1451caa1b3618199d9b32dbc5aa340cd3768979be14b69
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/7308046f959eb69f34ad9a6235ca9801370120b514421e777d6a65fc5753bda7/ATTRIBUTION.json
    sha256: 7308046f959eb69f34ad9a6235ca9801370120b514421e777d6a65fc5753bda7
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/7443959e8a809fff4635f6dd50705417b4f9b20911a7be272f502bcd45d0c62c/HANDOFF.json
    sha256: 7443959e8a809fff4635f6dd50705417b4f9b20911a7be272f502bcd45d0c62c
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/74d47599347441a8ebc853eb5dc139fde9daedc4001a8c246b5028dea2bc3da8/HISTORICAL-HOLDS.json
    sha256: 74d47599347441a8ebc853eb5dc139fde9daedc4001a8c246b5028dea2bc3da8
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/758571566f4bdb29350beea32d25b0a0d9aa40a27ec4de159bc3619e615b3886/chebi-86658.json
    sha256: 758571566f4bdb29350beea32d25b0a0d9aa40a27ec4de159bc3619e615b3886
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/76b70a1836b25de431c4f5cc27c72bb6b06a223ce33911e93b7681d4fcdb28f9/compounds_to_cas.csv
    sha256: 76b70a1836b25de431c4f5cc27c72bb6b06a223ce33911e93b7681d4fcdb28f9
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/78253121be0cfff808a99ae8a7a14509441cbd982fc70b2a6415507e06b0b0b4/EXPANDED-PRIMARY-NAME-COLLISION-PREFLIGHT.json
    sha256: 78253121be0cfff808a99ae8a7a14509441cbd982fc70b2a6415507e06b0b0b4
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/7b1e4d986e6b75ce2793c747b7f5e2ed3d6f3f2c7c2e6f85d2db8659511318c2/PROPOSAL.json
    sha256: 7b1e4d986e6b75ce2793c747b7f5e2ed3d6f3f2c7c2e6f85d2db8659511318c2
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/7b2fdb24dc57dc9f86cf2bf7a8bdec1044d5e94c53b796e8146080cc5dae9520/HANDOFF.json
    sha256: 7b2fdb24dc57dc9f86cf2bf7a8bdec1044d5e94c53b796e8146080cc5dae9520
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/7cdc5e23cfb6a41e7be888367ac5fb82c11ad39169bff9da05551a57309023e8/PROPOSALS.json
    sha256: 7cdc5e23cfb6a41e7be888367ac5fb82c11ad39169bff9da05551a57309023e8
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/80e9c3e8c9d78e884fb82f4f325053d02555306e6bc2b5fc03872c93d432460e/INPUT-PINS.json
    sha256: 80e9c3e8c9d78e884fb82f4f325053d02555306e6bc2b5fc03872c93d432460e
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/815f2beb80987b9a22710e87db4426ce1bb3db8bf35896b7b5ab0ac080728b55/web-additional-primary.txt
    sha256: 815f2beb80987b9a22710e87db4426ce1bb3db8bf35896b7b5ab0ac080728b55
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/82640104cc81615d472f4250e2a6a8093075320f4049bffe36739f161b13e61c/ISSUE-HISTORY.json
    sha256: 82640104cc81615d472f4250e2a6a8093075320f4049bffe36739f161b13e61c
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/84afdd2b6ff2743586f1ec3dffa8e807e52800380e7f864c1184e386d690f67e/chebi-15382.json
    sha256: 84afdd2b6ff2743586f1ec3dffa8e807e52800380e7f864c1184e386d690f67e
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/8796271876ee635de3a49a57ff422e5e8e69cd3489ac64897f8b93efe91eb631/web-chebi-comparison.txt
    sha256: 8796271876ee635de3a49a57ff422e5e8e69cd3489ac64897f8b93efe91eb631
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/87cd46449f62e42f69aa118928795188c39827ac744b5a20ba39d25791ca8957/SUPPLIER-WEB-CAPTURE.json
    sha256: 87cd46449f62e42f69aa118928795188c39827ac744b5a20ba39d25791ca8957
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/8c1ffe0ef93f240ba16016a182b6a0f371707c62e9709235e1111b4d9e876b6f/HANDOFF.json
    sha256: 8c1ffe0ef93f240ba16016a182b6a0f371707c62e9709235e1111b4d9e876b6f
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/8c4ee701beb896cd893306dd9fde08fbc78bb49fccc16772b4b34a735650aa3f/PROPOSALS.json
    sha256: 8c4ee701beb896cd893306dd9fde08fbc78bb49fccc16772b4b34a735650aa3f
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/91b5ec6848614c33216ec0a37fbbbbf8c067588732bc19a03089fa3ddc32411d/CURRENT-OWNER-AND-ROWS.json
    sha256: 91b5ec6848614c33216ec0a37fbbbbf8c067588732bc19a03089fa3ddc32411d
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/93777a551761d68f52b542798c9ddbb6286f1190924944ad3a39e4e3ac1068f9/source-records.json
    sha256: 93777a551761d68f52b542798c9ddbb6286f1190924944ad3a39e4e3ac1068f9
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/93f1e8e488c304502990bbaef6718edde547553068fc791db69b357a400a42c7/HISTORICAL-HOLDS.json
    sha256: 93f1e8e488c304502990bbaef6718edde547553068fc791db69b357a400a42c7
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/9434df8e748141f1066a5b3fd1e30aeebc7fb23d96deba0e05ec2a00dd51697b/DUPLICATE-AND-BEFOREIMAGE-PREFLIGHT.json
    sha256: 9434df8e748141f1066a5b3fd1e30aeebc7fb23d96deba0e05ec2a00dd51697b
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/955fd9aa39af3a86c3a6457e55cc544140df52f5ba7a196a572e2a71a563338e/cerium-meshM0319657.json
    sha256: 955fd9aa39af3a86c3a6457e55cc544140df52f5ba7a196a572e2a71a563338e
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/9fb5e074cc0f093922be16555ff427fc7b59ef1a7f29f001fc20e7fd823b8cbd/rifamycin-source-occurrences.json
    sha256: 9fb5e074cc0f093922be16555ff427fc7b59ef1a7f29f001fc20e7fd823b8cbd
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/a0655391a8d902565c5effa99c5f4504a0b3335550c8aeac5b722b5ee12f6c2f/primary-http-default.json
    sha256: a0655391a8d902565c5effa99c5f4504a0b3335550c8aeac5b722b5ee12f6c2f
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/a15f9bf206383b6cdb044e657b827b72e063db5eae3f0642dc4907f86f190e19/web-primary.txt
    sha256: a15f9bf206383b6cdb044e657b827b72e063db5eae3f0642dc4907f86f190e19
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/a84aab45aef8d33cd8c87dbb584c4f496806b81ec324b5ab748bbf2ce6bf83a6/Nicotinic_Acid.yaml
    sha256: a84aab45aef8d33cd8c87dbb584c4f496806b81ec324b5ab748bbf2ce6bf83a6
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/aa7d3fae930a6962f6464939d71cd21e6abb128a2cfeb6c29d2b24cabea27bdb/web-primary.txt
    sha256: aa7d3fae930a6962f6464939d71cd21e6abb128a2cfeb6c29d2b24cabea27bdb
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/ab3d1c3947b0ad9933d2722804967208869b6c380b928132e1f7f0e476eca1f9/context.json
    sha256: ab3d1c3947b0ad9933d2722804967208869b6c380b928132e1f7f0e476eca1f9
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/ae8f309c243483a6834d72b935752c20be9f07fe622608dc986b661e8e3ea046/S-adenosyl_Homocysteine.historical-review.md
    sha256: ae8f309c243483a6834d72b935752c20be9f07fe622608dc986b661e8e3ea046
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/b225c6748723ef60a68819b7d759d3417651239d0a2e38d7d50e02686e21edcb/Dl-alpha-lipoic_Acid.yaml
    sha256: b225c6748723ef60a68819b7d759d3417651239d0a2e38d7d50e02686e21edcb
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/b3595888c7200413fc38ca4b40e8103025af637073d518456aeaf39fc544906d/PROPOSALS.json
    sha256: b3595888c7200413fc38ca4b40e8103025af637073d518456aeaf39fc544906d
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/b9e5fc027dd3707d8f6f7a777de5961106c6a085fe074c45e131301a4dfe9784/PROPOSAL.json
    sha256: b9e5fc027dd3707d8f6f7a777de5961106c6a085fe074c45e131301a4dfe9784
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/be23a8b1370b44a7b3578e0d2395a6f85ee7da30b99906511d6088e055bc4c61/mediadive-2082.json
    sha256: be23a8b1370b44a7b3578e0d2395a6f85ee7da30b99906511d6088e055bc4c61
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/bf81e2ade7155f293aa1b2f72c974e27cf6998d0bb36b0a779e760769ff33cf9/facts.json
    sha256: bf81e2ade7155f293aa1b2f72c974e27cf6998d0bb36b0a779e760769ff33cf9
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/c151e85978ba8a6a57c1c145929b16f003821a1975b5e8979e2f95214d6ed74f/Edta.yaml
    sha256: c151e85978ba8a6a57c1c145929b16f003821a1975b5e8979e2f95214d6ed74f
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/c2b512c1babb3435fa548d704aae973545a3805bd333527712fa68f11f881c82/chebi-16680.json
    sha256: c2b512c1babb3435fa548d704aae973545a3805bd333527712fa68f11f881c82
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/c2e84d8f2c7e95839d3ac9d3b18118dc43f5131a0f539d1c30e8936f76ce05b8/mapping-review.json
    sha256: c2e84d8f2c7e95839d3ac9d3b18118dc43f5131a0f539d1c30e8936f76ce05b8
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/c681dcf52b338aa2171a76034b7615413ab936afd3b203a2b7ffdf63d61e7428/RESOLUTION.json
    sha256: c681dcf52b338aa2171a76034b7615413ab936afd3b203a2b7ffdf63d61e7428
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/c6b5cad8f6ad4e6abe910403647cc16bca9cbe224eed2d316cc6dd7ab0f4bb28/APIDAECIN-NLM-CONCEPTS.json
    sha256: c6b5cad8f6ad4e6abe910403647cc16bca9cbe224eed2d316cc6dd7ab0f4bb28
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/c71d4604d146eeac558cbce58e89b2b71118e2ade9db3bbe1b0bfd9c6c3e6b08/HANDOFF.json
    sha256: c71d4604d146eeac558cbce58e89b2b71118e2ade9db3bbe1b0bfd9c6c3e6b08
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/c98c6d029679208f55d05a5d7493a24bdac4b6c27a0c68daf4de3440d7093db9/MANIFEST.json
    sha256: c98c6d029679208f55d05a5d7493a24bdac4b6c27a0c68daf4de3440d7093db9
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/cc488b5b9a36c8a87d3cbb46d2bf5013677f2adbf4c7b9d41bc1cee45eada31c/S-adenosyl_Homocysteine.diff
    sha256: cc488b5b9a36c8a87d3cbb46d2bf5013677f2adbf4c7b9d41bc1cee45eada31c
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/cf4ceeebda243c0d83971e135a33de54ab2409b780d77d55ee781dbd4a8bc1f8/CURRENT-OWNER-AND-ROWS.json
    sha256: cf4ceeebda243c0d83971e135a33de54ab2409b780d77d55ee781dbd4a8bc1f8
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/cfcb341feb80f4da7b947955103c185017a3c48142288048d5a5a4f563d6bd61/PER-TARGET-PLAN.json
    sha256: cfcb341feb80f4da7b947955103c185017a3c48142288048d5a5a4f563d6bd61
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/d27dd801defc6f5b5a16339d2df6d2a72911b7aa98cef1f3870237be7d743e53/chebi-64755-live-v1.json
    sha256: d27dd801defc6f5b5a16339d2df6d2a72911b7aa98cef1f3870237be7d743e53
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/d8bc0897311f0fc1372eb419ce39d88713327a9771a5f559909d4619c9588d98/ASSEMBLY-ATTEMPT-1.json
    sha256: d8bc0897311f0fc1372eb419ce39d88713327a9771a5f559909d4619c9588d98
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/d90d3030a8395b294d674cfeb324b58082c8d99c4f985fc88813417e6eb622bf/PRIMARY-IDENTITY-CONCLUSION.json
    sha256: d90d3030a8395b294d674cfeb324b58082c8d99c4f985fc88813417e6eb622bf
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/dac2bd72743518ee6bb30beeeae508bab9badcc62ce9b70f1baeaeeec3bdc97c/Apidaecin_IB.yaml
    sha256: dac2bd72743518ee6bb30beeeae508bab9badcc62ce9b70f1baeaeeec3bdc97c
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/e3fd7795b63efa9e8bfc9b12f03179a6653cb8ac673a419a6e187a214481666b/historical-PC-import.yaml
    sha256: e3fd7795b63efa9e8bfc9b12f03179a6653cb8ac673a419a6e187a214481666b
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/e804bc8fb9cf73c0c182b5b70ace0c719a760dd72743c8c99b7d1e0d633c805f/S-adenosyl_Homocysteine.before.yaml
    sha256: e804bc8fb9cf73c0c182b5b70ace0c719a760dd72743c8c99b7d1e0d633c805f
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/e804bc8fb9cf73c0c182b5b70ace0c719a760dd72743c8c99b7d1e0d633c805f/S-adenosyl_Homocysteine.yaml
    sha256: e804bc8fb9cf73c0c182b5b70ace0c719a760dd72743c8c99b7d1e0d633c805f
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/e8f4693cac31a2ca29019ff0f9c8ad41af05650685ef47a8bb16a771ce2a6ee9/primary-http.json
    sha256: e8f4693cac31a2ca29019ff0f9c8ad41af05650685ef47a8bb16a771ce2a6ee9
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/ebff56ee94ecac6f2af01a948b654f0a5f16323680b25643d1f233227c58241e/HANDOFF.json
    sha256: ebff56ee94ecac6f2af01a948b654f0a5f16323680b25643d1f233227c58241e
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/eda05dab469af0663c0945f865f38f3422c7033ab6106ed5db1447c58adfa1af/CURRENT-ISSUE-HISTORY.json
    sha256: eda05dab469af0663c0945f865f38f3422c7033ab6106ed5db1447c58adfa1af
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/f4279df46a0e4094aa934b8adeab2cc953cdcf46b48134a7d72f6444be91e3af/EXACT-CORPUS-SEARCH.json
    sha256: f4279df46a0e4094aa934b8adeab2cc953cdcf46b48134a7d72f6444be91e3af
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/evidence/f92dfa94d02598131e558422f9ee1fb636ffb40aa09237375e48afdfae97762f/ADDITIONAL-SCOPE-DATABASE.json
    sha256: f92dfa94d02598131e558422f9ee1fb636ffb40aa09237375e48afdfae97762f
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/proposals/MIM-0000359.yaml
    sha256: 394f350bd3efbe725f05acdb8f767eff44a945bf8922b5849b62fe1d1252bd05
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/proposals/MIM-0000862.yaml
    sha256: 30795b5e4f80ed6f88821c5532a64ecc8c883f8133bef86c024d637479340751
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/proposals/MIM-0000967.yaml
    sha256: 36bc365db85015a4656a05a7cf128fc84e0ad21432c579d501fc5b4fcec859fd
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/proposals/MIM-0001002.yaml
    sha256: 6048b6b334c7781366bab0d7af636ee8f1785201fb9c26af6578f0c7e9558cdb
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/proposals/MIM-0001438.yaml
    sha256: 4a0a3a11a53a36eca399af556aefaaae8ffdd271db0cd3222e8e465500ac6d41
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/proposals/MIM-0001555.yaml
    sha256: 0ab2786149cfa31d10acb4de135c78f63b0fe389850bcec6e9cb3573bc8c2361
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/proposals/MIM-0001893.yaml
    sha256: 32209c557dc9c75f82cf1b4f50494cae238db320da4a42ea348c3e7d8868b7c7
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/proposals/MIM-0002202.yaml
    sha256: 95de5c13d56b7bc6d3629a193f41565c81e23941e4cdc68e143973db0b86f38a
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/proposals/MIM-0002227.yaml
    sha256: 87f6cae9492263adda19083a21fc6143705371eeab0875d105a00199c0778dff
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/proposals/MIM-0002360.yaml
    sha256: 4d55a929a33438edd39c798ba107aa2e2d9ada5c8ac6b365f186fae2eed4f4e6
    role: context
  - path: .temp/cumulative-source-successor-inputs-s2-v1/proposals/MIM-0002742.yaml
    sha256: 1400bb2872017770fe969285660ebc8a959761459d1d5a169e268106f25d2cc3
    role: context
  - path: .temp/cumulative-source-successor-inspected-s2-v1/context.json
    sha256: 4b702e0946e37e1ab319f2db9a963895151fc85aa999c06249f1d4d1605a123a
    role: context
  - path: .temp/cumulative-source-successor-inspected-s2-v1/payloads.json
    sha256: 492371a14a2ddfe9d53d87462f8c0761911d4471e165700e1f22d7eef9a45a85
    role: target
  - path: .temp/s2-eleven-skeptic-native-v1/PROPOSAL-AUDIT.json
    sha256: 33f93735cf30c7498f2b29c71ca008ebe436677bc879fd1f478d6e9c3360af1c
    role: context
  - path: .temp/s2-eleven-skeptic-native-v1/SCIENTIFIC-ASSESSMENTS.json
    sha256: 614f2c388dee3862158d25ecd8b3b7e9e25ed63732d6d88abb5005461a30095d
    role: context
  - path: .temp/s2-eleven-skeptic-native-v1/audit_current_proposals.py
    sha256: db27d4f41365e7c73a8ffb6e7594b5c11e4ddc47af134181f8bfe141e8d229da
    role: context
  - path: .temp/s2-eleven-skeptic-native-v1/primary-web-observation.json
    sha256: f283c6f0d4185649cd46982960c0bd770ab810ac9d5bb8ec0b094a9ed056cea4
    role: context
  - path: .temp/s2-eleven-skeptic-native-v1/run_strict.py
    sha256: ed8646dba9229e1171067e58ca89bca57133efb9b61a5c8bf89b76163ae180a7
    role: context
  - path: .temp/s2-eleven-skeptic-native-v1/run_term_checks.py
    sha256: fef5dee97e5c3defd582249de9e61f8d51545e0e813a90e67bff33a8fd9770f0
    role: context
  - path: .temp/s2-eleven-skeptic-native-v1/strict-failures.tsv
    sha256: 4ccba8b77ce80cf210105b5284b5953747729aba576ccdeecb81f7db84eb721b
    role: context
  - path: .temp/s2-eleven-skeptic-native-v1/strict-result.json
    sha256: 33fef740b7bf47da42054779a3230c9483330a43387779cf09a852d16e85a150
    role: context
  - path: .temp/s2-eleven-skeptic-native-v1/term-results.json
    sha256: c6da4ef80bc66b89d968f851ea21464bd8cd11e0b981a168de064019a752c6b4
    role: context
  - path: .temp/stable-adoption1303-canary-operational-policy-v1/CANARY-POLICY.json
    sha256: 9201981938cbf239841340d3324d5496b6112edf620e04fbe72511f947bf1773
    role: context
  - path: .temp/stable-adoption1303-real-canary-inputs-v1/inspection/context.json
    sha256: ab3d1c3947b0ad9933d2722804967208869b6c380b928132e1f7f0e476eca1f9
    role: context
  - path: AGENTS.md
    sha256: f16340060be37e57186ff8be31c8b9cb930c0b5229413a338db4c40aa18632a3
    role: context
  - path: MAPPING_SEMANTICS.md
    sha256: ba63481d6d61e011cdc1ae02885c3cf239de5d5932162003165126c0141926d3
    role: context
  - path: data/ingredients/mapped/Apidaecin_IB.yaml
    sha256: dac2bd72743518ee6bb30beeeae508bab9badcc62ce9b70f1baeaeeec3bdc97c
    role: context
  - path: data/ingredients/mapped/CeNO33_X_6_H2O.yaml
    sha256: 3d2b7216e0a7099bb9274feb2cb8a45b6db64234a26f0f5f0d58744bbf231dd1
    role: context
  - path: data/ingredients/mapped/D-limonene.yaml
    sha256: 3e587ecd29cfb9e4bd2567a03d27c0fd75aa6f5344b2178e6bdfc2aebb7a4978
    role: context
  - path: data/ingredients/mapped/Dl-alpha-lipoic_Acid.yaml
    sha256: b225c6748723ef60a68819b7d759d3417651239d0a2e38d7d50e02686e21edcb
    role: context
  - path: data/ingredients/mapped/Edta.yaml
    sha256: c151e85978ba8a6a57c1c145929b16f003821a1975b5e8979e2f95214d6ed74f
    role: context
  - path: data/ingredients/mapped/L-alpha-Phosphatidylcholine.yaml
    sha256: 4e951f39e1c8890eb0f6f260dcb7e28edfd18a5b57a191fcb6ef0290507c3be2
    role: context
  - path: data/ingredients/mapped/Lysozyme.yaml
    sha256: 149eda7e851924447adcbfaf8a97b89479fc9db4c8bbbf00592827b47c38a9a9
    role: context
  - path: data/ingredients/mapped/Nicotinic_Acid.yaml
    sha256: a84aab45aef8d33cd8c87dbb584c4f496806b81ec324b5ab748bbf2ce6bf83a6
    role: context
  - path: data/ingredients/mapped/Rifamycin.yaml
    sha256: 4e971cec7029a881832201d2bd17bfd4c797e00030341d6dfe457cf539aba1c8
    role: context
  - path: data/ingredients/mapped/S-adenosyl_Homocysteine.yaml
    sha256: e804bc8fb9cf73c0c182b5b70ace0c719a760dd72743c8c99b7d1e0d633c805f
    role: context
  - path: data/ingredients/mapped/Sorbitan_Monooleate.yaml
    sha256: 515170be9297b049e5a2e3ae8335e7d2290ffeedd17c12b050708db9cb512c99
    role: context
  - path: docs/record-review-profile.md
    sha256: da17e2048a13514a422bc94bd2f8d48943cffc5689b96e3f07da26423248d1a7
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: src/mediaingredientmech/curate/curation_successor.py
    sha256: 6b34ede05a681531d07715ea68a847692b90c51f25a0884d6f8a577eecd13766
    role: context
  - path: src/mediaingredientmech/curate/stable_id_adoption.py
    sha256: bdcbb9c7cd639f7d0cc27e6e57ce6317b390c1924591cd23bc8a68481242a404
    role: context
  - path: src/mediaingredientmech/schema/mediaingredientmech.yaml
    sha256: 77a57aaaa1a968dec077b13851b28350701b0952d672417f26e514bebfd0f392
    role: context
scope:
  description: One exact inspected S2 source-correction snapshot payload, including
    entire before/after record, declared delta, primary evidence and all inherited/residual
    holds.
  selection: .temp/cumulative-source-successor-inspected-s2-v1/payloads.json selector
    MIM:0002742
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - MIM:0002742
  exclusions:
  - target: Final generated rows, 7 historical CAS diagnostic dispositions and source-to-MIM
      bindings
    reason: Different native phases and scientific decisions; not assessed or approved
      by this source-delta review.
  - target: Other owners and unresolved claims outside this declared delta
    reason: Preserved exactly in the inherited/residual holds; no closure or status
      promotion.
targets:
- target_id: MIM:0002742
  path: .temp/cumulative-source-successor-inspected-s2-v1/payloads.json
  selector: MIM:0002742
  label: CeNO33_X_6_H2O exact proposed correction
  kind: snapshot_row
  semantic_digest:
    algorithm: sha256-canonical-json-v1
    sha256: 1d9084d41c248185d269801a8a230735b617ebcbdf24da0ecc51c675d92e5015
    description: Exact reviewed source correction; permanent identity and residual
      holds retained
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: .temp/cumulative-source-successor-inspected-s2-v1/payloads.json
    role: proposed source correction
checks:
- check_id: native-inspect
  name: Native current source and target inspection
  status: passed
  required: true
  summary: Actual S2 native inspect completed with exact current HEAD, all source/evidence
    pins and snapshot-row target.
  target_ids:
  - MIM:0002742
  command: /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/integration/stable-campaign-adoption-worktree/.venv/bin/python3
    scripts/record_review.py inspect --targets .temp/s2-eleven-skeptic-native-v1/targets.json
    --input .claude/skills/review-yaml-record/SKILL.md --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/0b5fc3b58b79396b37ba97c1d16ecf11307002f0e2c4074241b97c9c566e2f00/CONFIGURED-ONTOLOGY-LOOKUP.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/126a8e112f71c0b692a9e60a1d2663555864ac49104a8af242769ed56b5f9614/HISTORY-OBLIGATIONS.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/13ee219495257a22e816d3c621fa723de868152b71477cd2f96656819e6e9ae0/PRIMARY-IDENTITY-CONCLUSION.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/149eda7e851924447adcbfaf8a97b89479fc9db4c8bbbf00592827b47c38a9a9/Lysozyme.yaml
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/185a1586629a83078a8e6178bea27f729c37359ee63bac42c6f578f738da8773/1229.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/20222f9e374f29ad8a9ddac518236e8f6aca275c8395730b08c0e2588426dbac/SUPPRESSION-OBLIGATIONS.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/26e1e00060055037cb37b633b1ea445c548aabd2ae66fa73d3a001eb3f01a13e/D-limonene.historical-review.md
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/299204d51c81d2c02e4b0d5704d8dffe8d3b966fafb1344a383fd53e0d2859e5/CACHED-ISSUE-HISTORY.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/2e7da2023168a61581b6cbdf2cac9243e4b46073301dc6f35937aee308888677/D-limonene.diff
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/307b17477f423085720997a2c8dfe8dcd7ad8abcb304469e79505998a672d336/primary-retrieval-v1.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/33cf55a9b07832e45af2458741aa1dc6ce5669400bd446bf531f48667f261339/HANDOFF.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/35658dc81876bedbc0b621d9575ef9088006fecc8252a551eb9ece5f202e9c97/INPUT-PINS.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/3d2b7216e0a7099bb9274feb2cb8a45b6db64234a26f0f5f0d58744bbf231dd1/CeNO33_X_6_H2O.yaml
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/3d93354758569e5f8f882711c63c5f89951c699a72f9f3aa414ded2e3ca10c3f/mapping-evidence.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/3e587ecd29cfb9e4bd2567a03d27c0fd75aa6f5344b2178e6bdfc2aebb7a4978/D-limonene.before.yaml
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/3e587ecd29cfb9e4bd2567a03d27c0fd75aa6f5344b2178e6bdfc2aebb7a4978/D-limonene.yaml
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/452c95a2a6aa09f695951170b4d15bf03c6a6a7fd16459a513b2fb42eeb033b1/EXACT-CORPUS-SEARCH.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/4556f26a7a1c27256993f5b0346939cdbcd0a2a5a8b6714842575021ccdd5b9d/AUTHOR-ATTESTATION.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/4d84bfbb010966647860e5b203cc6003f9ac02f3b87951f99f3b842613bb42c6/sorbitan-recipe-occurrences.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/4e2853c22b8ed58d171c48c1853014b412b435506da2cef08c87a1344be76a11/DRAFT-HANDOFF-v2.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/4e3c3b691aac234d837d187100d0cea546210c3205e9a5cd78c4e43b39b4159c/chemical-scope-ontology-evidence.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/4e951f39e1c8890eb0f6f260dcb7e28edfd18a5b57a191fcb6ef0290507c3be2/L-alpha-Phosphatidylcholine.yaml
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/4e971cec7029a881832201d2bd17bfd4c797e00030341d6dfe457cf539aba1c8/Rifamycin.yaml
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/515170be9297b049e5a2e3ae8335e7d2290ffeedd17c12b050708db9cb512c99/Sorbitan_Monooleate.yaml
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/529bb71759b79adc40e8a15767221679731004eb289486adb36a4e8965cc06dd/mapping-evidence.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/5c10db580fcabb79ebbbbf70b42a20aad95bedebe89669ff5c9506a558b8020b/chebi-4735-live-v1.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/5fe480cd1bb7828c6cefd7ae56397b6a7a86200093f5a83c85dea833650cfb42/web-cas-check-digit-and-pdf-screenshot.txt
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/674fc6c1dc380bcd5e9d9f7d61fc9a40b83b2081612399124e4d6501e0683fc3/primary-http-approved.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/6e11b28aaa317fe7fc1451caa1b3618199d9b32dbc5aa340cd3768979be14b69/chebi-748872.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/7308046f959eb69f34ad9a6235ca9801370120b514421e777d6a65fc5753bda7/ATTRIBUTION.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/7443959e8a809fff4635f6dd50705417b4f9b20911a7be272f502bcd45d0c62c/HANDOFF.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/74d47599347441a8ebc853eb5dc139fde9daedc4001a8c246b5028dea2bc3da8/HISTORICAL-HOLDS.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/758571566f4bdb29350beea32d25b0a0d9aa40a27ec4de159bc3619e615b3886/chebi-86658.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/76b70a1836b25de431c4f5cc27c72bb6b06a223ce33911e93b7681d4fcdb28f9/compounds_to_cas.csv
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/78253121be0cfff808a99ae8a7a14509441cbd982fc70b2a6415507e06b0b0b4/EXPANDED-PRIMARY-NAME-COLLISION-PREFLIGHT.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/7b1e4d986e6b75ce2793c747b7f5e2ed3d6f3f2c7c2e6f85d2db8659511318c2/PROPOSAL.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/7b2fdb24dc57dc9f86cf2bf7a8bdec1044d5e94c53b796e8146080cc5dae9520/HANDOFF.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/7cdc5e23cfb6a41e7be888367ac5fb82c11ad39169bff9da05551a57309023e8/PROPOSALS.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/80e9c3e8c9d78e884fb82f4f325053d02555306e6bc2b5fc03872c93d432460e/INPUT-PINS.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/815f2beb80987b9a22710e87db4426ce1bb3db8bf35896b7b5ab0ac080728b55/web-additional-primary.txt
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/82640104cc81615d472f4250e2a6a8093075320f4049bffe36739f161b13e61c/ISSUE-HISTORY.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/84afdd2b6ff2743586f1ec3dffa8e807e52800380e7f864c1184e386d690f67e/chebi-15382.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/8796271876ee635de3a49a57ff422e5e8e69cd3489ac64897f8b93efe91eb631/web-chebi-comparison.txt
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/87cd46449f62e42f69aa118928795188c39827ac744b5a20ba39d25791ca8957/SUPPLIER-WEB-CAPTURE.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/8c1ffe0ef93f240ba16016a182b6a0f371707c62e9709235e1111b4d9e876b6f/HANDOFF.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/8c4ee701beb896cd893306dd9fde08fbc78bb49fccc16772b4b34a735650aa3f/PROPOSALS.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/91b5ec6848614c33216ec0a37fbbbbf8c067588732bc19a03089fa3ddc32411d/CURRENT-OWNER-AND-ROWS.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/93777a551761d68f52b542798c9ddbb6286f1190924944ad3a39e4e3ac1068f9/source-records.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/93f1e8e488c304502990bbaef6718edde547553068fc791db69b357a400a42c7/HISTORICAL-HOLDS.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/9434df8e748141f1066a5b3fd1e30aeebc7fb23d96deba0e05ec2a00dd51697b/DUPLICATE-AND-BEFOREIMAGE-PREFLIGHT.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/955fd9aa39af3a86c3a6457e55cc544140df52f5ba7a196a572e2a71a563338e/cerium-meshM0319657.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/9fb5e074cc0f093922be16555ff427fc7b59ef1a7f29f001fc20e7fd823b8cbd/rifamycin-source-occurrences.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/a0655391a8d902565c5effa99c5f4504a0b3335550c8aeac5b722b5ee12f6c2f/primary-http-default.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/a15f9bf206383b6cdb044e657b827b72e063db5eae3f0642dc4907f86f190e19/web-primary.txt
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/a84aab45aef8d33cd8c87dbb584c4f496806b81ec324b5ab748bbf2ce6bf83a6/Nicotinic_Acid.yaml
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/aa7d3fae930a6962f6464939d71cd21e6abb128a2cfeb6c29d2b24cabea27bdb/web-primary.txt
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/ab3d1c3947b0ad9933d2722804967208869b6c380b928132e1f7f0e476eca1f9/context.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/ae8f309c243483a6834d72b935752c20be9f07fe622608dc986b661e8e3ea046/S-adenosyl_Homocysteine.historical-review.md
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/b225c6748723ef60a68819b7d759d3417651239d0a2e38d7d50e02686e21edcb/Dl-alpha-lipoic_Acid.yaml
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/b3595888c7200413fc38ca4b40e8103025af637073d518456aeaf39fc544906d/PROPOSALS.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/b9e5fc027dd3707d8f6f7a777de5961106c6a085fe074c45e131301a4dfe9784/PROPOSAL.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/be23a8b1370b44a7b3578e0d2395a6f85ee7da30b99906511d6088e055bc4c61/mediadive-2082.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/bf81e2ade7155f293aa1b2f72c974e27cf6998d0bb36b0a779e760769ff33cf9/facts.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/c151e85978ba8a6a57c1c145929b16f003821a1975b5e8979e2f95214d6ed74f/Edta.yaml
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/c2b512c1babb3435fa548d704aae973545a3805bd333527712fa68f11f881c82/chebi-16680.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/c2e84d8f2c7e95839d3ac9d3b18118dc43f5131a0f539d1c30e8936f76ce05b8/mapping-review.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/c681dcf52b338aa2171a76034b7615413ab936afd3b203a2b7ffdf63d61e7428/RESOLUTION.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/c6b5cad8f6ad4e6abe910403647cc16bca9cbe224eed2d316cc6dd7ab0f4bb28/APIDAECIN-NLM-CONCEPTS.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/c71d4604d146eeac558cbce58e89b2b71118e2ade9db3bbe1b0bfd9c6c3e6b08/HANDOFF.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/c98c6d029679208f55d05a5d7493a24bdac4b6c27a0c68daf4de3440d7093db9/MANIFEST.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/cc488b5b9a36c8a87d3cbb46d2bf5013677f2adbf4c7b9d41bc1cee45eada31c/S-adenosyl_Homocysteine.diff
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/cf4ceeebda243c0d83971e135a33de54ab2409b780d77d55ee781dbd4a8bc1f8/CURRENT-OWNER-AND-ROWS.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/cfcb341feb80f4da7b947955103c185017a3c48142288048d5a5a4f563d6bd61/PER-TARGET-PLAN.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/d27dd801defc6f5b5a16339d2df6d2a72911b7aa98cef1f3870237be7d743e53/chebi-64755-live-v1.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/d8bc0897311f0fc1372eb419ce39d88713327a9771a5f559909d4619c9588d98/ASSEMBLY-ATTEMPT-1.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/d90d3030a8395b294d674cfeb324b58082c8d99c4f985fc88813417e6eb622bf/PRIMARY-IDENTITY-CONCLUSION.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/dac2bd72743518ee6bb30beeeae508bab9badcc62ce9b70f1baeaeeec3bdc97c/Apidaecin_IB.yaml
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/e3fd7795b63efa9e8bfc9b12f03179a6653cb8ac673a419a6e187a214481666b/historical-PC-import.yaml
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/e804bc8fb9cf73c0c182b5b70ace0c719a760dd72743c8c99b7d1e0d633c805f/S-adenosyl_Homocysteine.before.yaml
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/e804bc8fb9cf73c0c182b5b70ace0c719a760dd72743c8c99b7d1e0d633c805f/S-adenosyl_Homocysteine.yaml
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/e8f4693cac31a2ca29019ff0f9c8ad41af05650685ef47a8bb16a771ce2a6ee9/primary-http.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/ebff56ee94ecac6f2af01a948b654f0a5f16323680b25643d1f233227c58241e/HANDOFF.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/eda05dab469af0663c0945f865f38f3422c7033ab6106ed5db1447c58adfa1af/CURRENT-ISSUE-HISTORY.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/f4279df46a0e4094aa934b8adeab2cc953cdcf46b48134a7d72f6444be91e3af/EXACT-CORPUS-SEARCH.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/evidence/f92dfa94d02598131e558422f9ee1fb636ffb40aa09237375e48afdfae97762f/ADDITIONAL-SCOPE-DATABASE.json
    --input .temp/cumulative-source-successor-inputs-s2-v1/proposals/MIM-0000359.yaml
    --input .temp/cumulative-source-successor-inputs-s2-v1/proposals/MIM-0000862.yaml
    --input .temp/cumulative-source-successor-inputs-s2-v1/proposals/MIM-0000967.yaml
    --input .temp/cumulative-source-successor-inputs-s2-v1/proposals/MIM-0001002.yaml
    --input .temp/cumulative-source-successor-inputs-s2-v1/proposals/MIM-0001438.yaml
    --input .temp/cumulative-source-successor-inputs-s2-v1/proposals/MIM-0001555.yaml
    --input .temp/cumulative-source-successor-inputs-s2-v1/proposals/MIM-0001893.yaml
    --input .temp/cumulative-source-successor-inputs-s2-v1/proposals/MIM-0002202.yaml
    --input .temp/cumulative-source-successor-inputs-s2-v1/proposals/MIM-0002227.yaml
    --input .temp/cumulative-source-successor-inputs-s2-v1/proposals/MIM-0002360.yaml
    --input .temp/cumulative-source-successor-inputs-s2-v1/proposals/MIM-0002742.yaml
    --input .temp/cumulative-source-successor-inspected-s2-v1/context.json --input
    .temp/cumulative-source-successor-inspected-s2-v1/payloads.json --input .temp/s2-eleven-skeptic-native-v1/PROPOSAL-AUDIT.json
    --input .temp/s2-eleven-skeptic-native-v1/SCIENTIFIC-ASSESSMENTS.json --input
    .temp/s2-eleven-skeptic-native-v1/audit_current_proposals.py --input .temp/s2-eleven-skeptic-native-v1/primary-web-observation.json
    --input .temp/s2-eleven-skeptic-native-v1/run_strict.py --input .temp/s2-eleven-skeptic-native-v1/run_term_checks.py
    --input .temp/s2-eleven-skeptic-native-v1/strict-failures.tsv --input .temp/s2-eleven-skeptic-native-v1/strict-result.json
    --input .temp/s2-eleven-skeptic-native-v1/term-results.json --input .temp/stable-adoption1303-canary-operational-policy-v1/CANARY-POLICY.json
    --input .temp/stable-adoption1303-real-canary-inputs-v1/inspection/context.json
    --input AGENTS.md --input MAPPING_SEMANTICS.md --input data/ingredients/mapped/Apidaecin_IB.yaml
    --input data/ingredients/mapped/CeNO33_X_6_H2O.yaml --input data/ingredients/mapped/D-limonene.yaml
    --input data/ingredients/mapped/Dl-alpha-lipoic_Acid.yaml --input data/ingredients/mapped/Edta.yaml
    --input data/ingredients/mapped/L-alpha-Phosphatidylcholine.yaml --input data/ingredients/mapped/Lysozyme.yaml
    --input data/ingredients/mapped/Nicotinic_Acid.yaml --input data/ingredients/mapped/Rifamycin.yaml
    --input data/ingredients/mapped/S-adenosyl_Homocysteine.yaml --input data/ingredients/mapped/Sorbitan_Monooleate.yaml
    --input docs/record-review-profile.md --input docs/record-reviews.md --input schema/record_review.yaml
    --input src/mediaingredientmech/curate/curation_successor.py --input src/mediaingredientmech/curate/stable_id_adoption.py
    --input src/mediaingredientmech/schema/mediaingredientmech.yaml
  exit_code: 0
  evidence_ids:
  - current-context
  - exact-proposal
- check_id: strict-schema
  name: Native strict LinkML validation
  status: passed
  required: true
  summary: All 11 exact proposed records passed; zero files or rows with errors.
  target_ids:
  - MIM:0002742
  command: /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/integration/stable-campaign-adoption-worktree/.venv/bin/python3
    scripts/validate_strict.py .temp/cumulative-source-successor-inputs-s2-v1/proposals/MIM-0002202.yaml
    .temp/cumulative-source-successor-inputs-s2-v1/proposals/MIM-0001555.yaml .temp/cumulative-source-successor-inputs-s2-v1/proposals/MIM-0002360.yaml
    .temp/cumulative-source-successor-inputs-s2-v1/proposals/MIM-0002742.yaml .temp/cumulative-source-successor-inputs-s2-v1/proposals/MIM-0001438.yaml
    .temp/cumulative-source-successor-inputs-s2-v1/proposals/MIM-0001002.yaml .temp/cumulative-source-successor-inputs-s2-v1/proposals/MIM-0000967.yaml
    .temp/cumulative-source-successor-inputs-s2-v1/proposals/MIM-0001893.yaml .temp/cumulative-source-successor-inputs-s2-v1/proposals/MIM-0000359.yaml
    .temp/cumulative-source-successor-inputs-s2-v1/proposals/MIM-0000862.yaml .temp/cumulative-source-successor-inputs-s2-v1/proposals/MIM-0002227.yaml
    --out .temp/s2-eleven-skeptic-native-v1/strict-failures.tsv --workers 1
  exit_code: 0
  evidence_ids:
  - strict-validation
- check_id: exact-payload-and-holds
  name: Independent exact delta and provenance audit
  status: passed
  required: true
  summary: 149 bounded checks across 11 owners passed; this owner retains its permanent
    ID, original history and exact inherited holds. Ignored files included in 2957-owner
    duplicate check.
  target_ids:
  - MIM:0002742
  command: PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/integration/stable-cumulative-source-canary-target/src
    /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/integration/stable-campaign-adoption-worktree/.venv/bin/python3
    .temp/s2-eleven-skeptic-native-v1/audit_current_proposals.py
  exit_code: 0
  evidence_ids:
  - exact-delta-audit
- check_id: scientific-corrective-review
  name: Independent source/form/method assessment
  status: passed
  required: true
  summary: Support only the descriptor-to-NLM-Concept wording correction. The hexahydrate
    identity and asymmetric broader mapping remain unchanged.
  target_ids:
  - MIM:0002742
  evidence_ids:
  - exact-proposal
  - current-owner
  - mapping-semantics
  - primary-1
  - own-science
  - exact-delta-audit
  - strict-validation
  - term-validation
  - current-context
  - residual-holds
  scope_note: Human-readable scientific judgment by the named separate skeptical agent;
    deterministic checks are not its evidence substitute.
- check_id: release-checks
  name: Post-application full data/release gates
  status: not_applicable
  required: false
  summary: No source application or generated export is being reviewed here. Full
    qc, SSSOM synchronization, supported KGX and final-row review remain parent-owned
    prerequisites after actual native application.
  target_ids:
  - MIM:0002742
- check_id: expression-adapters
  name: iModulon structured adapters
  status: not_applicable
  required: false
  summary: No gene, locus, expression module or transcriptomic identity claim is part
    of this chemical/material correction.
  target_ids:
  - MIM:0002742
- check_id: engine-a-terms
  name: Native Engine-A canonical term label gate
  status: passed
  required: true
  summary: Canonical label validator exited zero.
  target_ids:
  - MIM:0002742
  command: /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/integration/stable-campaign-adoption-worktree/.venv/bin/linkml-term-validator
    validate-data .temp/cumulative-source-successor-inputs-s2-v1/proposals/MIM-0002742.yaml
    -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord
    --labels
  exit_code: 0
  evidence_ids:
  - term-validation
  scope_note: The native non-OBO guard skips registry-only ontology targets. For an
    ungrounded afterimage the term validator has no ontology target to check.
evidence:
- evidence_id: exact-proposal
  kind: record_content
  reference: .temp/cumulative-source-successor-inputs-s2-v1/proposals/MIM-0002742.yaml
  accessed_at: '2026-11-12T14:52:30.709893Z'
  support: supports
  summary: Complete current afterimage read and compared against the entire current
    owner and declared delta.
  snapshot_sha256: 1400bb2872017770fe969285660ebc8a959761459d1d5a169e268106f25d2cc3
- evidence_id: current-owner
  kind: record_content
  reference: data/ingredients/mapped/CeNO33_X_6_H2O.yaml
  accessed_at: '2026-11-12T14:52:30.709893Z'
  support: context_only
  summary: Entire current beforeimage, including all history, mapping, aliases, properties
    and remaining claim restrictions.
  snapshot_sha256: 3d2b7216e0a7099bb9274feb2cb8a45b6db64234a26f0f5f0d58744bbf231dd1
- evidence_id: mapping-semantics
  kind: authority
  reference: MAPPING_SEMANTICS.md
  accessed_at: '2026-11-12T14:52:30.709893Z'
  support: supports
  summary: Native permanent-ID, form-specific identity, method provenance, rejection
    and typed-mapping requirements.
  snapshot_sha256: ba63481d6d61e011cdc1ae02885c3cf239de5d5932162003165126c0141926d3
- evidence_id: primary-1
  kind: primary_source
  reference: .temp/cumulative-source-successor-inputs-s2-v1/evidence/955fd9aa39af3a86c3a6457e55cc544140df52f5ba7a196a572e2a71a563338e/cerium-meshM0319657.json
  accessed_at: '2026-11-12T14:52:30.709893Z'
  support: supports
  summary: Inspected cerium-meshM0319657.json for the specific identity/form/method
    conclusion; scope and limits stated in the independent assessment.
  snapshot_sha256: 955fd9aa39af3a86c3a6457e55cc544140df52f5ba7a196a572e2a71a563338e
- evidence_id: own-science
  kind: record_content
  reference: .temp/s2-eleven-skeptic-native-v1/SCIENTIFIC-ASSESSMENTS.json
  accessed_at: '2026-11-12T14:52:30.709893Z'
  support: supports
  summary: The captured authoritative M0319657 JSON explicitly types the target as
    mesh vocab Concept, labels it cerium nitrate (Ce(+3)), and identifies its preferred
    term. I checked that the exact proposed text substitution is the only ontology
    evidence change. The current source specifies Ce(NO3)3 x 6 H2O/CAS 10294-41-4;
    the proposal preserves the six waters, hydrate formula, supplied form and NARROW_MATCH.
    Calling this Concept an exact hydrate would be wrong, but the afterimage explicitly
    denies that and preserves the separate CAS identity.
  snapshot_sha256: 614f2c388dee3862158d25ecd8b3b7e9e25ed63732d6d88abb5005461a30095d
  locator: assessments.MIM:0002742
- evidence_id: exact-delta-audit
  kind: validation
  reference: .temp/s2-eleven-skeptic-native-v1/PROPOSAL-AUDIT.json
  accessed_at: '2026-11-12T14:52:30.709893Z'
  support: supports
  summary: 'Actual independent audit: source pins, delta values, persistent identity,
    old history, aliases, holds and unchanged claim fields.'
  snapshot_sha256: 33f93735cf30c7498f2b29c71ca008ebe436677bc879fd1f478d6e9c3360af1c
  locator: owners[mim_id=MIM:0002742]
- evidence_id: strict-validation
  kind: validation
  reference: .temp/s2-eleven-skeptic-native-v1/strict-result.json
  accessed_at: '2026-11-12T14:52:30.709893Z'
  support: supports
  summary: 'Native strict schema check: 11 exact proposals; zero error rows.'
  snapshot_sha256: 33fef740b7bf47da42054779a3230c9483330a43387779cf09a852d16e85a150
- evidence_id: term-validation
  kind: validation
  reference: .temp/s2-eleven-skeptic-native-v1/term-results.json
  accessed_at: '2026-11-12T14:52:30.709893Z'
  support: supports
  summary: Actual documented Engine-A check or native non-OBO safety skip; no guessed
    adapter result.
  snapshot_sha256: c6da4ef80bc66b89d968f851ea21464bd8cd11e0b981a168de064019a752c6b4
  locator: target_id=MIM:0002742
- evidence_id: current-context
  kind: record_content
  reference: .temp/cumulative-source-successor-inspected-s2-v1/context.json
  accessed_at: '2026-11-12T14:52:30.709893Z'
  support: context_only
  summary: Complete inspected source-successor context with original 1879 cases, 1022
    origin-accounting entries, current inventory and all historical obligations.
  snapshot_sha256: 4b702e0946e37e1ab319f2db9a963895151fc85aa999c06249f1d4d1605a123a
- evidence_id: residual-holds
  kind: record_content
  reference: .temp/cumulative-source-successor-inspected-s2-v1/payloads.json
  accessed_at: '2026-11-12T14:52:30.709893Z'
  support: context_only
  summary: Exact inherited equals residual holds remain binding; this review does
    not close earlier scientific findings.
  snapshot_sha256: 492371a14a2ddfe9d53d87462f8c0761911d4471e165700e1f22d7eef9a45a85
  locator: MIM:0002742
assessments:
- assessment_id: exact-source-delta
  area: identity
  topic: Bounded source correction with permanent identity and retained scientific
    holds
  outcome: supported
  summary: Support only the descriptor-to-NLM-Concept wording correction. The hexahydrate
    identity and asymmetric broader mapping remain unchanged.
  details: The captured authoritative M0319657 JSON explicitly types the target as
    mesh vocab Concept, labels it cerium nitrate (Ce(+3)), and identifies its preferred
    term. I checked that the exact proposed text substitution is the only ontology
    evidence change. The current source specifies Ce(NO3)3 x 6 H2O/CAS 10294-41-4;
    the proposal preserves the six waters, hydrate formula, supplied form and NARROW_MATCH.
    Calling this Concept an exact hydrate would be wrong, but the afterimage explicitly
    denies that and preserves the separate CAS identity.
  target_ids:
  - MIM:0002742
  evidence_ids:
  - exact-proposal
  - current-owner
  - mapping-semantics
  - primary-1
  - own-science
  - exact-delta-audit
  - strict-validation
  - term-validation
  - current-context
  - residual-holds
  dimensions:
  - name: curation_action
    value: apply_exact_source_delta
    definition: Exact native source-correction admission value; no authority outside
      this reviewed delta.
    evidence_ids:
    - exact-proposal
    - current-context
    - residual-holds
  - name: delta_sha256
    value: 459d8190af58b2ff54766078b75e085a85388414f92cc08ed638e2be6f2d29bf
    definition: Exact native source-correction admission value; no authority outside
      this reviewed delta.
    evidence_ids:
    - exact-proposal
    - current-context
    - residual-holds
  - name: permanent_mim_id
    value: MIM:0002742
    definition: Exact native source-correction admission value; no authority outside
      this reviewed delta.
    evidence_ids:
    - exact-proposal
    - current-context
    - residual-holds
  - name: residual_holds_json
    value: "[\n  {\n    \"hold_kind\": \"entire_original_source_and_origin_context\"\
      ,\n    \"reference\": {\n      \"path\": \"/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/integration/stable-adoption-real-canary-target/.temp/stable-adoption1303-real-canary-inputs-v1/inspection/context.json\"\
      ,\n      \"sha256\": \"ab3d1c3947b0ad9933d2722804967208869b6c380b928132e1f7f0e476eca1f9\"\
      ,\n      \"bytes\": 38130190\n    },\n    \"selector\": \"/\",\n    \"retention\"\
      : \"Byte-identical original 1879-case,1022-origin context, including source\
      \ evidence, origin accounting and holds; no status reclassification.\"\n  },\n\
      \  {\n    \"hold_kind\": \"original_worker_history_obligations\",\n    \"reference\"\
      : {\n      \"path\": \"/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/preflight/actual-candidate-science-primary-v1/HISTORY-OBLIGATIONS.json\"\
      ,\n      \"sha256\": \"126a8e112f71c0b692a9e60a1d2663555864ac49104a8af242769ed56b5f9614\"\
      ,\n      \"bytes\": 170445\n    },\n    \"selector\": \"/\",\n    \"retention\"\
      : \"Preserve original W01 13-item and W09 8-row historical findings/decisions\
      \ exactly, with their original review identities.\"\n  },\n  {\n    \"hold_kind\"\
      : \"original_suppression_obligations\",\n    \"reference\": {\n      \"path\"\
      : \"/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/preflight/actual-candidate-science-primary-v1/SUPPRESSION-OBLIGATIONS.json\"\
      ,\n      \"sha256\": \"20222f9e374f29ad8a9ddac518236e8f6aca275c8395730b08c0e2588426dbac\"\
      ,\n      \"bytes\": 71268\n    },\n    \"selector\": \"/\",\n    \"retention\"\
      : \"No suppression-history retirement or blanket synonym approval by a source\
      \ delta.\"\n  },\n  {\n    \"hold_kind\": \"exact_owner_scope_and_prior_review_restrictions\"\
      ,\n    \"reference\": {\n      \"path\": \"/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/integration/stable-adoption-real-canary-target/data/ingredients/mapped/CeNO33_X_6_H2O.yaml\"\
      ,\n      \"sha256\": \"3d2b7216e0a7099bb9274feb2cb8a45b6db64234a26f0f5f0d58744bbf231dd1\"\
      ,\n      \"bytes\": 5576\n    },\n    \"values\": {\n      \"notes\": \"Imported\
      \ from mim-queue (source_id=mediadive.ingredient:1587); no CAS-RN or CHEBI/NCIT\
      \ match. Curator review needed. Reviewed on 2026-05-11 as a formula shorthand\
      \ for a cerium nitrate hydrate; left unmapped pending exact formula/CAS evidence.\
      \ The 2026-11-08 source review resolves the former formula/CAS gap with independent\
      \ primary evidence. The exact hydrate CAS is distinct from the broader MeSH\
      \ family; see campaign proposal and retained historical notes.\",\n      \"\
      occurrence_statistics\": {\n        \"total_occurrences\": 0,\n        \"media_count\"\
      : 0\n      },\n      \"supplied_form\": [\n        {\n          \"name\": \"\
      cerium(III) nitrate hexahydrate\",\n          \"cas_rn\": \"10294-41-4\",\n\
      \          \"form\": \"hexahydrate\",\n          \"notes\": \"Source-specific\
      \ formula and CAS establish six waters; no supplier or catalogue is attributed\
      \ to the original recipe. Independent supplier comparison: Sigma-Aldrich238538.\"\
      \n        }\n      ],\n      \"ontology_mapping.evidence\": [\n        {\n \
      \         \"evidence_type\": \"DATABASE_MATCH\",\n          \"source\": \"https://mediadive.dsmz.de/rest/ingredient/1587\"\
      ,\n          \"notes\": \"Exact raw formula Ce(NO3)3 x 6 H2O and CAS10294-41-4\
      \ support the hexahydrate; independent supplier and PubChem exact-form evidence\
      \ is captured in the worker02 campaign.\"\n        },\n        {\n         \
      \ \"evidence_type\": \"CURATOR_JUDGMENT\",\n          \"source\": \"https://id.nlm.nih.gov/mesh/M0319657.json\"\
      ,\n          \"notes\": \"Closest verified eligible broader nitrate family in\
      \ the captured name/CAS search. NARROW_MATCH emits skos:broadMatch; descriptor\
      \ is not exact hydrate identity. Registry/identity row retains cas:10294-41-4.\
      \ An exact SNOMED substance search hit exists but SNOMED is outside the frozen\
      \ schema OntologySourceEnum.\"\n        }\n      ]\n    },\n    \"interpretation\"\
      : \"These exact source/preparation/role/occurrence restrictions remain; changing\
      \ a mapping assertion or rejecting a label does not approve the unresolved material\
      \ or source claims.\"\n  },\n  {\n    \"hold_kind\": \"qualified_historical_full_row_dispositions\"\
      ,\n    \"reference\": {\n      \"path\": \"/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/preflight/actual-candidate-science-primary-v1/PER-TARGET-PLAN.json\"\
      ,\n      \"sha256\": \"cfcb341feb80f4da7b947955103c185017a3c48142288048d5a5a4f563d6bd61\"\
      ,\n      \"bytes\": 14675533\n    },\n    \"values\": [\n      {\n        \"\
      entry_id\": \"row-000680\",\n        \"prior_disposition\": null,\n        \"\
      prior_row_reason\": null,\n        \"original_evidence_basis\": null,\n    \
      \    \"applicable_worker_history_targets\": []\n      },\n      {\n        \"\
      entry_id\": \"row-000681\",\n        \"prior_disposition\": null,\n        \"\
      prior_row_reason\": null,\n        \"original_evidence_basis\": null,\n    \
      \    \"applicable_worker_history_targets\": []\n      }\n    ],\n    \"interpretation\"\
      : \"Historical row decisions remain evidence/history; proposed corrective support\
      \ does not itself promote the regenerated full row.\"\n  }\n]"
    definition: Exact native source-correction admission value; no authority outside
      this reviewed delta.
    evidence_ids:
    - exact-proposal
    - current-context
    - residual-holds
  - name: rejected_identifiers_json
    value: '[]'
    definition: Exact native source-correction admission value; no authority outside
      this reviewed delta.
    evidence_ids:
    - exact-proposal
    - current-context
    - residual-holds
  - name: corrective_delta_findings
    value: none
    definition: Exact native source-correction admission value; no authority outside
      this reviewed delta.
    evidence_ids:
    - exact-proposal
    - current-context
    - residual-holds
  - name: residual_findings_json
    value: '[]'
    definition: Exact native source-correction admission value; no authority outside
      this reviewed delta.
    evidence_ids:
    - exact-proposal
    - current-context
    - residual-holds
findings: []
actions: []
limitations:
- No new hydrate identity, SNOMED adoption, actual supplier attribution, broadMatch-to-subclass
  inference, role or publication support is granted. Existing source/form and all
  prior release restrictions remain.
- All exact residual_holds_json entries remain binding, including original worker
  reviews, source/origin context, suppression obligations and prior full-row dispositions.
  Empty findings means no newly identified blocker in this corrective delta, not that
  inherited findings are resolved.
- This is an assessment of a frozen source-correction payload before application,
  not a complete-record publication pass. Full corpus synchronization, scientific
  source-binding reviews, actual revised SSSOM/companion exports and content-bound
  release gates remain pending.
- Prior draft observations and old S reviews are retained as history; this bundle
  is tied to the inspected current S2 head and exact bytes. No paid provider query,
  GitHub mutation, source edit, generation or native apply was performed.
notes:
- 'Maintained owner before: data/ingredients/mapped/CeNO33_X_6_H2O.yaml; declared
  after location: data/ingredients/mapped/CeNO33_X_6_H2O.yaml. Future application
  belongs to the reviewed native curation-successor writer; do not hand-edit aggregates
  or generated products.'
- The seven admission dimensions use stable_id_adoption.encoded for structured JSON;
  hashes use the native canonical payload/delta digest.
links: []
```
