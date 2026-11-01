# Approved Step3 carnitine hydrochloride migration: independent bounded source, product and approval-withdrawal review

- Review: 20261101T094737Z-approved-step3-carnitine-hydrochloride-review
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-11-01T09:45:40.686039Z
- Finished UTC: 2026-11-01T09:47:37.639444Z
- Reviewer: Codex independent reviewer /root/step1_independent_review (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

The12selected maintained/generated targets satisfy the bounded approved DL-carnitine hydrochloride migration and strict approval-withdrawal contract. Three individual records change; all2952others are byte-identical. Canonical2982rows and unified4170names/209330occurrences preserve unrelated scope. All69NLDMapprovals are withdrawn; both changed mappings remain WITHHOLD. The staged-fixture omission#1040 is corrected and182native capture tests pass. No unresolved in-scope finding remains; existing full scientific-release FAIL and access/coverage limits are retained.

## Scope And Provenance

The approved #1004 exact hydrochloride identity correction, rejected duplicate, NLDM reference, guarded writer/router, bounded canonical/unified/membership products and unchanged companion dependencies.

Selection: Twelve exact targets chosen from three changed owners and their direct maintained/generated dependencies; all selected targets reviewed in full at the declared selectors. Corpus-wide counts/byte comparisons are structural scope checks, not scientific approval of all records.
Coverage: full; 12 reviewed / 12 in the declared population.
Source: working_tree at Git base 99fe4b44d78126d78041a69eeb366c52bedf0caa.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| MIM:Carnitine_Hydrochloride | data/ingredients/mapped/Carnitine_Hydrochloride.yaml | maintained | Active DL-carnitine hydrochloride owner |
| MIM:Carnitine_Dl_Hydrochloride | data/ingredients/mapped/Carnitine_Dl_Hydrochloride.yaml | maintained | Rejected duplicate with corrected hydrochloride identity |
| MIM:NLDM_metabolites | data/ingredients/mapped/NLDM_metabolites.yaml | maintained | NLDM component 59 reference and inherited approval withdrawal |
| step3:sssom-ncit | mappings/ingredient_mappings.sssom.tsv # subject_id=MIM:Carnitine_Hydrochloride; predicate_id=skos:exactMatch; object_id=NCIT:C216679 | snapshot_row | Exact NCIT salt claim remains withheld |
| step3:sssom-nldm | mappings/ingredient_mappings.sssom.tsv # subject_id=MIM:NLDM_metabolites; predicate_id=skos:exactMatch; object_id=kgmicrobe.ingredient:nldm_metabolites | snapshot_row | NLDM identity row with historical validation and withdrawn approval |
| step3:unified-salt | UNIFIED_INGREDIENT_MAPPING.tsv # ingredient_name=Carnitine Hydrochloride | snapshot_row | One changed unified salt row |
| step3:guarded-writer | scripts/merge_carnitine_hydrochloride.py | maintained | Hash-bound source and canonical migration |
| step3:finite-source-router | src/mediaingredientmech/utils/culturemech_occurrences.py | maintained | Two normalized source labels route to the corrected salt |
| step3:rejection-pair | mappings/unified_mapping_rejections.tsv # ingredient_name=Carnitine Hydrochloride; mim_id=NCIT:C216679; rejected_id in [CHEBI:91318,CHEBI:48601] | snapshot_row | Source-bound acylcarnitine and amide rejections |
| step3:membership-migration | mappings/culturemech_recipe_membership.tsv # mim_identifier=NCIT:C216679; recipe_id in [CultureMech:015654,CultureMech:015655,CultureMech:015656,CultureMech:015665,CultureMech:015666,CultureMech:015667,CultureMech:015668,CultureMech:015669,CultureMech:015670,CultureMech:015671,CultureMech:015740,CultureMech:015741,CultureMech:015742,CultureMech:015749] | snapshot_row | Fourteen preserved recipe/count pairs |
| step3:nldm-assertion-withdrawal | reports/semantic_review_20260921/resolution/assertion-dispositions.tsv # source_record=data/ingredients/mapped/NLDM_metabolites.yaml; assertion_type in [component,nutritional_roles] | snapshot_row | All 68 NLDM component and role approvals withdrawn |
| step3:unchanged-companion | reports/ingredient_bundle_20261101_carnitine1004/review.json | generated | 51 claims and 20 owners preserve prior explicit decisions |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Actual durable source capture | passed | True | MIM:Carnitine_Hydrochloride, MIM:Carnitine_Dl_Hydrochloride, MIM:NLDM_metabolites, step3:sssom-ncit, step3:sssom-nldm, step3:unified-salt, step3:guarded-writer, step3:finite-source-router, step3:rejection-pair, step3:membership-migration, step3:nldm-assertion-withdrawal, step3:unchanged-companion | Actual detached HEAD99fe4b44; staged treeb3084fcb matches feature;522staged paths,601native input hashes and102current references match. All four frozen manifests and indexed files verified. |
| Independent clean-capture writer and dependency tests | passed | True | MIM:Carnitine_Hydrochloride, MIM:Carnitine_Dl_Hydrochloride, MIM:NLDM_metabolites, step3:sssom-ncit, step3:sssom-nldm, step3:unified-salt, step3:guarded-writer, step3:finite-source-router, step3:rejection-pair, step3:membership-migration, step3:nldm-assertion-withdrawal, step3:unchanged-companion | 182passed,13warnings,0skips; includes the previously failing historical migration test, all132writer tests and50routing/dependency tests. |
| Independent applied source/product/withdrawal checks | passed | True | MIM:Carnitine_Hydrochloride, MIM:Carnitine_Dl_Hydrochloride, MIM:NLDM_metabolites, step3:sssom-ncit, step3:sssom-nldm, step3:unified-salt, step3:guarded-writer, step3:finite-source-router, step3:rejection-pair, step3:membership-migration, step3:nldm-assertion-withdrawal, step3:unchanged-companion | Source and generated deltas match exact approved scope; no unrelated record, mapping decision, assertion payload/approval or companion owner change. |
| Independent native boundary probes and fixed findings | passed | True | MIM:Carnitine_Hydrochloride, MIM:Carnitine_Dl_Hydrochloride, MIM:NLDM_metabolites, step3:sssom-ncit, step3:sssom-nldm, step3:unified-salt, step3:guarded-writer, step3:finite-source-router, step3:rejection-pair, step3:membership-migration, step3:nldm-assertion-withdrawal, step3:unchanged-companion | Previously reproduced receipt no-op, proposal/input-set races, prior-stamp and diagnostic-parser failures are now refused or handled by the narrowly corrected implementation. Historical author mutation runs remain credited to their authors. |
| Native complete QC | passed | True | MIM:Carnitine_Hydrochloride, MIM:Carnitine_Dl_Hydrochloride, MIM:NLDM_metabolites, step3:sssom-ncit, step3:sssom-nldm, step3:unified-salt, step3:guarded-writer, step3:finite-source-router, step3:rejection-pair, step3:membership-migration, step3:nldm-assertion-withdrawal, step3:unchanged-companion | just qc passes schema/evidence, SSSOM, roundtrip, indexes, visualization and flat coverage. |
| Native broad focused regressions | passed | True | MIM:Carnitine_Hydrochloride, MIM:Carnitine_Dl_Hydrochloride, MIM:NLDM_metabolites, step3:sssom-ncit, step3:sssom-nldm, step3:unified-salt, step3:guarded-writer, step3:finite-source-router, step3:rejection-pair, step3:membership-migration, step3:nldm-assertion-withdrawal, step3:unchanged-companion | 484focused regression tests pass. |
| Maintained full Python3.13 suite | passed | True | MIM:Carnitine_Hydrochloride, MIM:Carnitine_Dl_Hydrochloride, MIM:NLDM_metabolites, step3:sssom-ncit, step3:sssom-nldm, step3:unified-salt, step3:guarded-writer, step3:finite-source-router, step3:rejection-pair, step3:membership-migration, step3:nldm-assertion-withdrawal, step3:unchanged-companion | 3693passed,1skipped,27warnings; local coverage was not measured. |
| CURIE and product label checks | passed | True | MIM:Carnitine_Hydrochloride, MIM:Carnitine_Dl_Hydrochloride, MIM:NLDM_metabolites, step3:sssom-ncit, step3:sssom-nldm, step3:unified-salt, step3:guarded-writer, step3:finite-source-router, step3:rejection-pair, step3:membership-migration, step3:nldm-assertion-withdrawal, step3:unchanged-companion | Checks pass;101non-blocking product warnings retained. |
| Unified rejection and freshness gates | passed | True | MIM:Carnitine_Hydrochloride, MIM:Carnitine_Dl_Hydrochloride, MIM:NLDM_metabolites, step3:sssom-ncit, step3:sssom-nldm, step3:unified-salt, step3:guarded-writer, step3:finite-source-router, step3:rejection-pair, step3:membership-migration, step3:nldm-assertion-withdrawal, step3:unchanged-companion | Both gates pass on the exact current unified artifact/provenance. |
| Native mapping, semantic, reviewed SSSOM, supported KGX and companion chain | passed | True | MIM:Carnitine_Hydrochloride, MIM:Carnitine_Dl_Hydrochloride, MIM:NLDM_metabolites, step3:sssom-ncit, step3:sssom-nldm, step3:unified-salt, step3:guarded-writer, step3:finite-source-router, step3:rejection-pair, step3:membership-migration, step3:nldm-assertion-withdrawal, step3:unchanged-companion | Receipt17 replay and content-bound integrity/export gates pass; all prior16receipts are retained. Both changed mappings remain WITHHOLD; no scientific approval is added. |
| Native canonical actual-KG invariants | passed | True | MIM:Carnitine_Hydrochloride, MIM:Carnitine_Dl_Hydrochloride, MIM:NLDM_metabolites, step3:sssom-ncit, step3:sssom-nldm, step3:unified-salt, step3:guarded-writer, step3:finite-source-router, step3:rejection-pair, step3:membership-migration, step3:nldm-assertion-withdrawal, step3:unchanged-companion | Canonical2982rows pass native invariants with available transforms; unavailable BTO/MICRO coverage is separately declared. |
| BTO/MICRO actual-transform coverage | unavailable | False | MIM:Carnitine_Hydrochloride, MIM:Carnitine_Dl_Hydrochloride, MIM:NLDM_metabolites, step3:sssom-ncit, step3:sssom-nldm, step3:unified-salt, step3:guarded-writer, step3:finite-source-router, step3:rejection-pair, step3:membership-migration, step3:nldm-assertion-withdrawal, step3:unchanged-companion | Those two external transformed ontology inputs were unavailable; no validation of their B4 coverage is claimed. |
| Whole-corpus scientific release | failed | False | MIM:Carnitine_Hydrochloride, MIM:Carnitine_Dl_Hydrochloride, MIM:NLDM_metabolites, step3:sssom-ncit, step3:sssom-nldm, step3:unified-salt, step3:guarded-writer, step3:finite-source-router, step3:rejection-pair, step3:membership-migration, step3:nldm-assertion-withdrawal, step3:unchanged-companion | Existing full-release verdict remains FAIL:1732blocking findings and2336OPEN assertions. Integrity/supported-subset success is not full-release approval. |
| Organism-expression source adapter | not_applicable | False | MIM:Carnitine_Hydrochloride, MIM:Carnitine_Dl_Hydrochloride, MIM:NLDM_metabolites, step3:sssom-ncit, step3:sssom-nldm, step3:unified-salt, step3:guarded-writer, step3:finite-source-router, step3:rejection-pair, step3:membership-migration, step3:nldm-assertion-withdrawal, step3:unchanged-companion | The selected question is exact chemical form and publication provenance; expression-module membership is not evidence for this identity. |

## Scientific And Domain Assessments

### Approved exact salt identity and chloride chemistry

identity: supported. Targets: MIM:Carnitine_Hydrochloride.

The maintained survivor now denotes DL-carnitine hydrochloride with NCIT:C216679/CAS461-05-2 and CID5970chloride chemistry. Raw source spelling is preserved; free-substance and amide names remain attributed REJECTED_LABEL entries. This is conformance to the inspected approved identity decision, not a new native scientific approval.

NCI label/status/CAS/UNII and PubChem structure/formula agree at this salt scope. Source evidence, history and LLM assistance are explicit. Free and L-specific sibling records remain unchanged controls; roles and biological mechanisms are not newly assessed.

### Retired duplicate keeps correct identity and provenance

representation: supported. Targets: MIM:Carnitine_Dl_Hydrochloride.

The rejected duplicate has identifier, ontology and representative NCIT:C216679, zero counts and no current free-carnitine chemical_properties. Exact prior wrong CAS/chemistry survives in append-only history and immutable preimages, avoiding publication of free-form chemistry as current salt assertions.

Only one active owner exists. Browser and label rows resolve the raw name to the same NCIT identity. The REJECTED preferred-term row may precede the active synonym row; this review does not claim active-owner-first ordering.

### Mixture component reference migrates without broad mixture curation

consistency: supported. Targets: MIM:NLDM_metabolites.

Only NLDM component59 identity plus audit history changes; component name,17.5UM amount, mixture identity, other components and role payloads are retained. NLDM remains a distinct formulation, not an alias of its carnitine component.

### Bounded exact salt mapping replaces wrong and redundant claims

grounding: supported. Targets: step3:sssom-ncit.

Five former salt-subject claims become one exact NCIT:C216679 claim. The exact free CAS, broad free-parent and redundant registry rows retire; unsafe free-substance aliases are withheld from other. The new row has no inherited validation stamp and remains WITHHOLD.

Canonical2986→2982 means two changed/four removed/zero added rows; unrelated row/header bytes remain exact. The2975-row full producer candidate is diagnostic, never a blanket canonical replacement.

### Historical validation is distinct from scientific approval

provenance: supported. Targets: step3:sssom-nldm.

NLDM canonical source and mapping_date change while its exact original manual:promote_resolved_unmapped&#124;PROMOTED&#124;2026-08-06annotation and old source tokens remain. Its changed owner forces WITHHOLD; retained historical annotation grants no approval.

### One native unified row changes with every occurrence retained

consistency: supported. Targets: step3:unified-salt.

Only Carnitine Hydrochloride changes mim_id, cas_rn and two accepted salt spellings. All4170names/209330occurrences remain;4169other raw rows and every occurrence cell are unchanged. Four hash-prefixed names remain real data.

Current source-label rejection policy excludes the reviewed acylcarnitine/amide IDs in every identity column. No generic CHEBI ban or invented replacement is introduced.

### Guarded exact-preimage migration and refusal boundaries

provenance: supported. Targets: step3:guarded-writer.

The writer binds original inputs, source evidence, exact proposed bytes, unique destination ownership and reservation identity at native commit. Completed source no-ops bind the original regular complete receipt, timestamps, outputs and all seven preimages; promotion accepts only bounded subject changes and native historical stamp behavior.

Native race tests cover receipt/backup regular-file and symlink substitution and late valid owner insertion. A failed or conflicting publication cannot be reported complete. Guarantees apply at cooperative lock/native validation boundaries, not arbitrary later external writes.

### Finite source resolution and future-cohort behavior

quantity: supported. Targets: step3:finite-source-router.

Exactly the two reviewed normalized hydrochloride source names route to NCIT:C216679. Native15/15new-recipe and14/15repeated-listing controls pass; current fourteen memberships are a historical migration fixture, not a permanent live count quota. Free/L/amide and unrelated labels retain their existing behavior.

### Scoped wrong-source identities remain excluded

identity: supported. Targets: step3:rejection-pair.

The existing CHEBI:91318hold moves to the corrected owner and one preventive CHEBI:48601hold is appended with exact source label/owner attribution. Other ledger bytes are preserved; a conflicting CAS xref is not treated as salt identity.

### Historical recipe pairs migrate without loss

quantity: supported. Targets: step3:membership-migration.

Fourteen exact recipe IDs and listing counts move from the retired local identity to NCIT:C216679; headers and all unrelated membership bytes remain. Dynamic native producer tests permit legitimate future source evolution.

### Changed NLDM owner invalidates all inherited approvals

ownership: supported. Targets: step3:nldm-assertion-withdrawal.

All64component and4role approvals become OPEN because the full NLDM owner hash changed, even though67nonmapping payload hashes are identical. The separate mapping becomes WITHHOLD, totaling69withdrawals. No section-equivalence, unchanged-payload or approval-model bypass is introduced.

### Unchanged explicit companion decisions remain byte-bound

ownership: supported. Targets: step3:unchanged-companion.

The companion refresh preserves all51claim decisions and20owner hashes;17mapping locators relocate under the existing strict comparator. The exact workflow selector points to this new bundle. Protected qc-evidence, vendored pin and Intel review files remain unchanged.

No changed carnitine or NLDM owner is introduced into the approved companion cohort. This structural refresh preserves existing approvals and grants none.

### Primary source conflicts and access boundaries remain visible

evidence: supported. Targets: MIM:Carnitine_Hydrochloride, MIM:Carnitine_Dl_Hydrochloride, step3:rejection-pair.

The frozen source package retains exact primary bytes and receipt provenance with honest limitations. ChEBI conflicting CAS evidence is explicitly preserved rather than erased; no PubChem-to-CHEBI:48601xref claim is made.

Sigma is a selected extraction from the retained rendered response, not recovered full HTML. The raw ignored CultureBotHT CSV is not represented as committed source content. Direct CAS Registry access was unavailable; no CAS Registry verification is claimed. Existing exact upstream correction consumption is scoped to the separately merged maintained Claw intake.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- lump: MIM:Carnitine_Hydrochloride, MIM:Carnitine_Dl_Hydrochloride. Inspected approved source evidence identifies these two source spellings as the same DL-carnitine hydrochloride supplied form. Consolidation retains one active owner and an explicit rejected representative-linked provenance record; neither is equated with free carnitine, L-specific siblings or carnitinamide.
- retain: MIM:NLDM_metabolites. NLDM is a distinct mixture that contains the salt; component-reference repair never merges mixture identity with a component.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| semantics | MAPPING_SEMANTICS.md; Sections 0 and 3; relevant synonym/SSSOM rules | supports | Exact supplied-form identity, same-substance aliases, rejected-label separation, registry and SSSOM rules govern this bounded migration. |
| approved-decision | reports/carnitine_hydrochloride_1004_20261101/sources/approved-decision.md | supports | Preserved approved #1004 decision selects NCIT:C216679 before consolidation; it does not confer native mapping/assertion approval. |
| nci | reports/carnitine_hydrochloride_1004_20261101/sources/ncit-c216679.json; code, name, status and properties | supports | NCI EVS reports active NCIT:C216679, DL-Carnitine Hydrochloride, CAS461-05-2 and UNII F64264D63N in the captured26.10d response. |
| pubchem-salt | reports/carnitine_hydrochloride_1004_20261101/sources/pubchem-5970-properties.json; PropertyTable.Properties[0] | supports | CID5970 is the chloride-containing salt: C7H16ClNO3,197.66g/mol and explicit chloride-bearing SMILES/InChI. |
| pubchem-free | reports/carnitine_hydrochloride_1004_20261101/sources/pubchem-288-properties.json; PropertyTable.Properties[0] | refutes | CID288 represents free carnitine with C7H15NO3 and161.20g/mol; it cannot supply the salt chemistry. |
| amide-conflict | reports/carnitine_hydrochloride_1004_20261101/sources/chebi-48601-primary.json; CHEBI:48601 label, formula and xrefs | refutes | CHEBI:48601 denotes carnitinamide chloride with a distinct nitrogen-containing formula; its conflicting CAS xref is retained as a conflict, not used to equate it with carnitine hydrochloride. |
| sigma-extract | reports/carnitine_hydrochloride_1004_20261101/sources/sigma-c9500-facts.json; source URL, actual access time, extracted product/CAS/formula and response hash | supports | Selected facts from the retained successful independent rendered Sigma C9500 page support the exact salt form. This is a factual extraction with retained response binding, not a successful raw HTML capture. |
| raw-source | reports/carnitine_hydrochloride_1004_20261101/sources/selected-source-rows.json; selected rows96 and787 | supports | Two original CultureBotHT rows retain their raw Compound/CAS fields. The ignored rawCSV is an exact local snapshot associated with its checkout; its bytes are not claimed to be a tracked Git blob. |
| upstream-overlay | reports/carnitine_hydrochloride_1004_20261101/sources/compound_cas_corrections.tsv | supports | Existing tracked upstream correction is preserved as source evidence. MIM migration itself performs no source ingestion; separately merged Claw#700 applies only its bounded intake correction. |
| source-application | reports/carnitine_hydrochloride_1004_20261101/implementation/independent/step3-mim-independent/actual-source-application/receipt.json; actual application receipt and per-surface comparisons | supports | Independent actual-application check binds all three changed owners, original history prefixes and beforeimages, exact14recipe/count pairs, unchanged other2952individual records and synchronized changed aggregate entries. Eight unrelated inherited discussions omissions are unchanged. |
| writer-audit | reports/carnitine_hydrochloride_1004_20261101/implementation/independent/step3-mim-independent/implementation-preapplication/receipt.json; native boundary evidence and frozen source hashes | supports | Independent preapplication probes tested native guarded publication, reservation replacement, valid competing-owner races, no-op receipt binding and run-wrapper checked-byte/input-set guards. Its earlier promotion readiness is historical and superseded by the actual native prior-stamp replay review. |
| prior-stamp-fix | reports/carnitine_hydrochloride_1004_20261101/implementation/independent/step3-mim-independent/revision-1038/receipt.json; actual-candidate replay, dry-run and negative controls | supports | Independent actual native candidate replay confirms exact old NLDM validation stamp retention and empty new NCIT stamp; wrong/empty/foreign stamps are refused. Writer2ec6a4af and132author tests plus37independent focused tests are bound; author mutations retain attribution. |
| implementation-package | reports/carnitine_hydrochloride_1004_20261101/implementation/manifest.json; files; corresponding readonly verifier and selector-binding-1037/ | supports | 264indexed files retain original failures and repairs, exact application journals and independent checkpoints; current102repository references match this capture. The original selector-binding package is preserved in its separate checkpoint. |
| generation-package | reports/carnitine_hydrochloride_1004_20261101/generation/manifest.json; files and captured_sources; independent readonly verifier --originals passed | supports | 124indexed files bind the native2975-row diagnostic candidate, bounded canonical promotion, actual receipt-chain executions, unified build, producer inputs and corrected analyzer. |
| validation-package | reports/carnitine_hydrochloride_1004_20261101/validation/manifest.json; files | supports | 49indexed files bind completed gates and independent actual-product/package checks. Original diagnostic failures remain explicitly distinguished from corrected successful checks. |
| products | reports/carnitine_hydrochloride_1004_20261101/validation/evidence/step3-mim-independent/final-state/product-audit.json; complete actual final-state audit | supports | Independent final product audit verifies canonical2982rows, receipt17 and preceding16receipt preservation, exact1unified-row change/4169unchanged, all4170names/209330occurrences, NLDM69withdrawals, companion51claims/20owners/17relocations, generated browser/labels and protected files. |
| analyzer-fix | reports/carnitine_hydrochloride_1004_20261101/validation/evidence/step3-mim-independent/final-state/1039-parser-proof.json; original4166/209323 versus corrected4170/209330 | supports | Independent original/fixed parser comparison demonstrates why plain TSV must preserve four hash-prefixed names and seven occurrences. Actual mapping bytes were correct; only the old diagnostic count was wrong. |
| receipt17 | reports/sssom_completion_20260921/mapping_changes/issue1004-carnitine-hydrochloride-merge.json; sequence17; owner and SSSOM input/output hashes; row changes | supports | Native receipt17 binds the three changed owners and exact two changed/four removed/zero added canonical rows without approving new claims. |
| current-release | reports/carnitine_hydrochloride_1004_20261101/generation/native-chain/build/verified-output.json; mapping_counts; full_scientific_release; semantic_status_counts | supports | Native chain has1739SUPPORTED/1243WITHHOLD mappings and2151approved-subset assertions; the full scientific release remains FAIL with1732blocking findings and2336OPEN assertions. NLDM loses69approvals, including67unchanged nonmapping payloads. |
| companion | reports/ingredient_bundle_20261101_carnitine1004/dependency-refresh.json; source/owner/decision bindings and relocation audit | supports | Native unchanged-cohort refresh preserves51claim decisions and20owner hashes;17mapping references relocate. Changed carnitine/NLDM owners gain no companion approval. |
| current-canonical | mappings/ingredient_mappings.sssom.tsv; exact target selectors and all unrelated line/header comparisons | supports | Current canonical bytes are d5cd812a8c44c85438d73c68c7a8c3067a505765e4cd54e3a64cef029f2d8ed6. Only the selected salt and NLDM subject groups change. |
| current-unified | UNIFIED_INGREDIENT_MAPPING.tsv; ingredient_name=Carnitine Hydrochloride | supports | Current unified bytes are ca62e2f031ebe0f9e6185efc7816207912095beef9799a04634c889cc27196b5. Only salt mim_id, cas_rn and accepted salt synonyms change; every occurrence cell is retained. |
| kg-boundary | reports/carnitine_hydrochloride_1004_20261101/generation/canonical-validation/receipt.json; exit_code0; missing_b4_transforms | supports | Unmodified native canonical invariant validator passes with actual read-only KG transforms. BTO and MICRO transform inputs are explicitly unavailable; no claim of checking those B4 surfaces is made. |
| writer-source | scripts/merge_carnitine_hydrochloride.py; apply_sources, completed source receipt checks, promote and native publication scope | supports | Current hash2ec6a4afdd97d580e36471467fa884fe87caa6a76f0a3f7fa9756d00b1fc720e retains hash-bound input/candidate scope, existing receipt and regular preimage binding, reservation checks and native precommit destination uniqueness. |
| router-source | src/mediaingredientmech/utils/culturemech_occurrences.py; source override table and collection path | supports | Only the two reviewed normalized carnitine-hydrochloride source names route to NCIT:C216679; free, L-form and unrelated source identities retain native behavior. |
| fixture-manifest | tests/fixtures/issue1004-before/manifest.json; culturemech_recipe_membership.tsv.gz and ingredient_mappings.sssom.tsv.gz | supports | Original historical migration preimages are immutable fixture inputs, not permanent live-cohort quotas. Both gzip fixtures omitted from the first staging are now present with exactly the already-declared hashes. |
| capture-tests | /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/approved-plan-20261101T031134Z/logs/step3-independent-capture-v2-writer-dependencies.json; Actual durable capture-v2; Python3.13;182passed,13warnings,0skips; logSHA715ebe680798fe0f5e62925f99b48f5b99d813a17318af1fabd384498e2b0ed1 | supports | Independently reran complete writer, occurrence routing and dependency suites in the exact staged capture after explicit inclusion of the two immutable gzip fixtures. Native race, stamp, historical migration and future15/15 or14/15cohort controls pass. |
| staging-finding | https://github.com/CultureBotAI/MediaIngredientMech/issues/1040; Original tree4779e87c; native historical-membership test exited1 with FileNotFoundError. LogSHAa76f72ff3ddd8e7a57f3ce2f19e1261c9d859c47b98aa8ef2cbd41abd41f0af6; corrected treeb3084fcb includes exact two archives. | supports | Issue filed before correction. Gitignore-independent filesystem reads found originals; git index omitted both due *.tsv.gz. No implementation or data byte changed to repair staging. Both archives are included in this review source hashes and complete native rerun passes. |
| gate-full-qc | reports/carnitine_hydrochloride_1004_20261101/validation/evidence/logs/step3-chain-final-v1-full-qc.json; argv, actual UTC execution, exit_code and log_sha256 | supports | just qc passes schema/evidence, SSSOM, roundtrip, indexes, visualization and flat coverage. |
| gate-focused | reports/carnitine_hydrochloride_1004_20261101/validation/evidence/logs/step3-chain-final-v1-receipt-regression-tests.json; argv, actual UTC execution, exit_code and log_sha256 | supports | 484focused regression tests pass. |
| gate-suite | reports/carnitine_hydrochloride_1004_20261101/validation/evidence/logs/step3-chain-final-v1-full-suite.json; argv, actual UTC execution, exit_code and log_sha256 | supports | 3693passed,1skipped,27warnings; local coverage was not measured. |
| gate-labels | reports/carnitine_hydrochloride_1004_20261101/validation/evidence/logs/step3-chain-final-v1-curies-and-product-labels.json; argv, actual UTC execution, exit_code and log_sha256 | supports | Checks pass;101non-blocking product warnings retained. |
| gate-unified | reports/carnitine_hydrochloride_1004_20261101/validation/evidence/logs/step3-chain-final-v1-unified-gates.json; argv, actual UTC execution, exit_code and log_sha256 | supports | Both gates pass on the exact current unified artifact/provenance. |

## Limits And Additional Notes

- scientific_review is false. This bounded implementation, provenance and approved-identity conformance review does not promote native mapping/assertion status, grant scientific release approval or certify the full corpus.
- Full semantic scientific release remains FAIL with1732blocking findings and2336OPEN assertions;2151approved-subset assertions and1739SUPPORTED mappings are retained existing scope. Both changed mappings remain WITHHOLD.
- Scientific source checks cover the selected salt identity and rejection boundaries only. Roles, mechanisms, every NLDM component, and all other corpus identities were not independently scientifically re-reviewed.
- BTO and MICRO transformed ontology inputs were unavailable. Native invariant passes apply only to available actual-KG surfaces; no unavailable B4 coverage is implied.
- The Sigma evidence is a factual extraction from a retained successful rendered response. Failed raw HTML capture is not relabeled as success. Direct CAS Registry lookup was not available; raw CultureBotHT CSV bytes are an ignored local snapshot, not a tracked Git revision.
- Eight unrelated aggregate discussions omissions predate this work and remain unchanged. Successful native QC does not establish complete corpus-wide semantic equality of individual and aggregate surfaces.
- Corrected tombstone and active survivor resolve to the same NCIT identity in label products; this does not establish active-owner-first label-index ordering.
- Local full-suite coverage was not measured; CI and merge-group checks have not been evaluated for a future committed head. Exact committed-head and integration review remain separate.
- This source.state is working_tree at the actual durable main commit99fe4b44, with staged overlay treeb3084fcb. It does not claim those601input bytes were already committed.
- Original pre-fix failures and unsuccessful reviewer harness diagnostics remain historical evidence. Only corrected controls and current final source/product checks support this verdict.
- Pre-fix findings#1036,#1037,#1038,#1039 and#1040were reported/filed before fixes. Original failures, fixed controls and exact current hashes are retained. They are referenced as workflow evidence, not fabricated previous structured finding occurrences. Empty findings means no unresolved defect in this exact bounded review, not closure of all historical issues.
- The original520-path capture omitted two ignored gzip preimages and failed the native historical membership test. The preserved original capture is not the review source. The corrected actual522-path capture adds only the exact already-manifested archives, with no production code/data byte change; all102repository references now exist.
- Source capture601input hashes include522changed staged paths, current maintained dependencies, immutable prior receipts, primary evidence, native schema/contract and sibling controls. Native inspection preceded these assessments; actual UTC timestamps are used.
- The independent capture test receipt and first-failure log are run-owned external evidence and are referenced as such, never relabeled as repository inputs. Their command, result and immutable hashes are preserved in this bundle.
- Run-owned orchestration scripts and candidate generation were reviewed as execution evidence; they are not newly introduced general repository APIs. Existing protected workflow/pin bytes were checked against durable base.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261101T094737Z-approved-step3-carnitine-hydrochloride-review
kind: category
repository: CultureBotAI/MediaIngredientMech
title: 'Approved Step3 carnitine hydrochloride migration: independent bounded source,
  product and approval-withdrawal review'
started_at: '2026-11-01T09:45:40.686039Z'
finished_at: '2026-11-01T09:47:37.639444Z'
reviewer:
  identity: Codex independent reviewer /root/step1_independent_review
  kind: agent
  independence: independent
  independence_basis: Separate review agent; authored no production writer, routing
    code, record, canonical mapping, execution harness or curation approval. Ran read-only
    native/adversarial probes, inspected primary evidence and actual outputs, and
    reported findings to the supervisor before fixes. A separate read-only package-check
    subagent supplied explicitly attributed package checks.
skill: .claude/skills/review-yaml-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: false
summary: The12selected maintained/generated targets satisfy the bounded approved DL-carnitine
  hydrochloride migration and strict approval-withdrawal contract. Three individual
  records change; all2952others are byte-identical. Canonical2982rows and unified4170names/209330occurrences
  preserve unrelated scope. All69NLDMapprovals are withdrawn; both changed mappings
  remain WITHHOLD. The staged-fixture omission#1040 is corrected and182native capture
  tests pass. No unresolved in-scope finding remains; existing full scientific-release
  FAIL and access/coverage limits are retained.
source:
  git_revision: 99fe4b44d78126d78041a69eeb366c52bedf0caa
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: d4df94935abfd922e84c3512e9a9b7735240f8e266d9a3ae23bb4933926b04eb
    role: context
  - path: .claude/skills/review-ingredients/reference/integrations.md
    sha256: 81426d9c27b1392592e5b7e1d8daf45c5048ebe176f9c751123e2f8cf2ffcb6a
    role: context
  - path: .claude/skills/review-ingredients/reference/validation-rules.md
    sha256: c9bbbd618dfc57363581aaf1aa757230acde0548e689e61fb059fb031a5b4a21
    role: context
  - path: .claude/skills/review-sssom-output/SKILL.md
    sha256: 2e05b30eefce620fbb78196386e476c330b81e36738f2461b4be64391a61ecd5
    role: context
  - path: .claude/skills/review-yaml-category/SKILL.md
    sha256: 154758ee4b3bd401e19c89d488ff648014c5ec4282c6c1b710de5093ce36c101
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 4f3142cc2c7e8884ffc049ad81fd9b6fcf076bd40579b43d80d8652679630bd1
    role: context
  - path: .github/workflows/qc-evidence.yaml
    sha256: 288ef1795582105763952c4104d1455c1fef273a65528949f1e558d39c7306f3
    role: context
  - path: .github/workflows/qc-reviewed-sssom.yaml
    sha256: 9b6d2b4afba2998a3a9bae3e6b2964fc1e92b7708a06385623dbbef51ebb3600
    role: context
  - path: AGENTS.md
    sha256: fc7728986d82b43359a9055ae233bcf0d4ebaef8bb657ef1b4bb4aa87b2cbaaf
    role: context
  - path: MAPPING_SEMANTICS.md
    sha256: 94aad13ea0fc3df82a37383f388f41432b607b04cac61ae5792ce1a381aef805
    role: context
  - path: UNIFIED_INGREDIENT_MAPPING.provenance.json
    sha256: 30449d7221332dd72ce1fcc1d244375bd3ea8f4c6961b7eb7ac6e92b8501c2c6
    role: context
  - path: UNIFIED_INGREDIENT_MAPPING.tsv
    sha256: ca62e2f031ebe0f9e6185efc7816207912095beef9799a04634c889cc27196b5
    role: target
  - path: conf/record_review.yaml
    sha256: 07a8fa6d17ee664c7a2bc2d5b5821bd106f6aa454299b4f3e0440176876cd82e
    role: context
  - path: data/curated/ALL_INGREDIENTS.md
    sha256: 57b8f203b4aa686b8220deff0d6cf0da18e033ba69fd3e80d1c31a13c81ca8fe
    role: context
  - path: data/curated/MAPPED_INGREDIENTS.md
    sha256: 1e0bf71ab9fe8bb4b409bd87fcf610143f4488b3190f19808f3c4f65f3de9292
    role: context
  - path: data/curated/all_ingredients_index.csv
    sha256: 99ab5c0e367240413f944c481103345606fa1f3ec472fad8d7cbd5dc91af9ab7
    role: context
  - path: data/curated/all_ingredients_index.json
    sha256: 4a53de65968c934dae5c616b88e8f16e509b7090ce8acb22349e9929653073e1
    role: context
  - path: data/curated/mapped_ingredients.yaml
    sha256: 13cbb00b7122e8252b9749d3d6b10eae4bb9cc324778e71ec3c6cb76f38fe314
    role: context
  - path: data/curated/mapped_ingredients_index.csv
    sha256: 371870cbdf68600a35dd9d99d0ba5bbf8717208c4d07d7fd474afee23a6da0d9
    role: context
  - path: data/curated/mapped_ingredients_index.json
    sha256: dbe1b5b060336cdee64e5f19c587df68be3c2b693e6ab3992688929a1af3243a
    role: context
  - path: data/curated/unmapped_ingredients.yaml
    sha256: 556b8d3db52ccffc7e8fe091ac892182e2a102bc24c2130e729238d32bf8c898
    role: context
  - path: data/ingredients/mapped/Acriflavine.yaml
    sha256: d8ec8d8d5d56bfde012c54709bd80b33dff64660df7ce111d28de40707e9824e
    role: context
  - path: data/ingredients/mapped/Anabasine_Hydrochloride.yaml
    sha256: c9c693f7bc5354b5c472efaf4472f66b56e5c4e8d3a814490982da1d94810215
    role: context
  - path: data/ingredients/mapped/Bovine_Serum_Albumin.yaml
    sha256: 43ceecb07d1bfa49f863a4c9d2618c79f8ab93385a8752ea88f07a6924b0f094
    role: context
  - path: data/ingredients/mapped/Carnitine_Dl_Hydrochloride.yaml
    sha256: 7df72255729f730fcea0308fa125e0cf826de55e62bf5152f40bf303f33719c0
    role: target
  - path: data/ingredients/mapped/Carnitine_Hydrochloride.yaml
    sha256: 25b57cd832a1a4f85de99d32ba2c38fb6ee69f30848afbc0b3014f38ab42210f
    role: target
  - path: data/ingredients/mapped/Cotarnine_Chloride.yaml
    sha256: 821fd7dd0dd3c8308727c3e6a4999c860eb6be69a42d6bb996b6d3a94b2a4860
    role: context
  - path: data/ingredients/mapped/L-Carnitine.yaml
    sha256: 83717e970a478ac8248672c11d82a8d91f5732ea5e520bd388f2060e3632e754
    role: context
  - path: data/ingredients/mapped/L-Carnitine_Hydrochloride.yaml
    sha256: 516a885435fc23a3c3c1842783d8ba0d03b60eb8e227687468df45038006c5ff
    role: context
  - path: data/ingredients/mapped/Locust_Bean_Gum.yaml
    sha256: 973e02f8ba4ad966f8fc9acf5174d47f9aa6cc17c9f45afb632c6e9776276cfd
    role: context
  - path: data/ingredients/mapped/Lysozyme.yaml
    sha256: 797929d4ebcbf1c034daeaf8f45bc28c4de79196fff8e30e926a087f0afdff2f
    role: context
  - path: data/ingredients/mapped/NLDM_metabolites.yaml
    sha256: 457be6fa945786e0f6fbbb29755ac42e069a56fe5eb2d754e9b880fa4063ab10
    role: target
  - path: data/ingredients/mapped/Polymyxin_B.yaml
    sha256: d722a6e60a46c79b843b9a1c539b989d9a066619792dcebaa0167aaab20d5bb2
    role: context
  - path: data/ingredients/mapped/Pretomanid.yaml
    sha256: 7b02eca54a257804e1203999faede7e6fade61657d201fa2fd0f21f1a7ee89af
    role: context
  - path: data/ingredients/mapped/Proteose_Peptone_No_2.yaml
    sha256: 67ca4baee47a98b1ccd293403503a20d1ed757055d179658689f9ab7a6a17533
    role: context
  - path: data/ingredients/mapped/Rabbit_Serum.yaml
    sha256: 031bddb1376c30e284b08ab91209ff3c5465cc5a0b49a82b70a4758aae0a0f7c
    role: context
  - path: data/ingredients/mapped/Rifamycin.yaml
    sha256: 0319c48944ab91a2af53000f5e7488646224cf4683c327a2839ba6d56c8a2a8e
    role: context
  - path: data/ingredients/mapped/Rifamycin_Sv.yaml
    sha256: 7e2cf0690eb1c0e345eed29f9f69a339bb53a5e14f69ebd230c6e86174db77e2
    role: context
  - path: data/ingredients/mapped/Sodium_Adipate.yaml
    sha256: 0699b67ffbcc35d3566ff531350c753d93b677718cb4e550bdfa6257ba35886d
    role: context
  - path: data/ingredients/mapped/Sorbitan_Monooleate.yaml
    sha256: 09a88638de346c0f2cb44d3c09fd751b03f6266c9abdf7b6b927dec56c17d083
    role: context
  - path: data/ingredients/mapped/Sunflower_Oil.yaml
    sha256: b6c22eaea1a8bd7c243b5eb9da1b4c6c36c6b9de1e3ac25768283684d1dc9e03
    role: context
  - path: data/ingredients/mapped/Sutezolid.yaml
    sha256: 61bda78a8cb9a9d96639219d4ef514a4ed7de658d0fe1b373edf20a9f1cebf7b
    role: context
  - path: data/ingredients/mapped/Tara_Gum.yaml
    sha256: d52f83dbd41f5fac0215e6d47bbf9d9b46ee39aa2a7c78a5552cb7ccdebe693b
    role: context
  - path: data/ingredients/mapped/V-8_Juice.yaml
    sha256: 44229e30128f51e28f1b117122f0f7f6bf405ba52b6b38cf3eaf0a66a129798f
    role: context
  - path: data/ingredients/mapped/Xanthine.yaml
    sha256: c72c948fb793dd36ba53def8a77230d0ac337bec0962369f01c6e29848bccd22
    role: context
  - path: data/ingredients/mapped/Zymosan.yaml
    sha256: a445e9bbdf842cd2a732fd2fe999014ddbffe7b9ace8f6bf0c273d7981f80662
    role: context
  - path: docs/INGREDIENT_BUNDLE.md
    sha256: cff26766071434207a743c845bbf9b1a293de9f45a98f364e50a743fae9ca5f2
    role: context
  - path: docs/SSSOM_RELEASE.md
    sha256: ecbb62e39c90f3ed79b57de89950530b7b4896fec151396e8b93b5e703661c4c
    role: context
  - path: docs/data/all_ingredients.csv
    sha256: 48ed9b9f11cb9bee28419f3259d662020da5d95b2e388ffbc38d0d78a2bc98f3
    role: context
  - path: docs/data/all_ingredients.json
    sha256: 3ecd4324fbeefde08c81bad72d3f2067e9b64d1f4ec718f3516f54a50ac506f2
    role: context
  - path: docs/data/all_ingredients.md
    sha256: b2b05150e1a4946899bc18d1267c93d816c5ef1b53b10a91f39c1977a22ce3d6
    role: context
  - path: docs/data/ingredient_graph.json
    sha256: f2b6f69ad9e627078b17eac97ede82176b1a98b6a25017034c293dda79eda48f
    role: context
  - path: docs/data/ingredient_umap.json
    sha256: fdc00aca2c659151d358bee5523f829b0045a3632f8c9cc25d47e9387a214dc3
    role: context
  - path: docs/data/ingredients.json
    sha256: 81dbfced5a95a00a3f8dd75c68739c393a98fb57479f3b54cd882609749b7ed4
    role: context
  - path: docs/data/label_index.csv
    sha256: 5817a62f4d76e39fcca493f25065a890b344b89424d64366d690dfb1b25851fa
    role: context
  - path: docs/data/mapped_ingredients.csv
    sha256: 630bd7aabfeddbb4a666aa87043a2c115dd1b24ee7755d3be086ad669edbef75
    role: context
  - path: docs/data/mapped_ingredients.json
    sha256: d73d52866abdf15bf88e1129f7f0404153f2d4897b6fed6ea42b163817f0490d
    role: context
  - path: docs/data/mapped_ingredients.md
    sha256: a421a6700b195c4df785d2e88bde20aaa215591a4579fd317775edbc5b4f16b1
    role: context
  - path: docs/data/unmapped_ingredients.md
    sha256: 36cfe298592839c500a936718b9b70a0286fd95a04ac85cfdb898e4f034a7eb5
    role: context
  - path: docs/record-review-profile.md
    sha256: da17e2048a13514a422bc94bd2f8d48943cffc5689b96e3f07da26423248d1a7
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: justfile
    sha256: a1237b64f4a5e11a473e99b34ed88b4a0d3a7f23e701bca649248325d83ba57a
    role: context
  - path: mappings/culturemech_recipe_membership.tsv
    sha256: 777effdf97560aae1f266eb47770b3144947f5ad4f764a6dfe12845b8455ff75
    role: target
  - path: mappings/ingredient_mappings.sssom.tsv
    sha256: d5cd812a8c44c85438d73c68c7a8c3067a505765e4cd54e3a64cef029f2d8ed6
    role: target
  - path: mappings/other_cross_record_baseline.tsv
    sha256: c5b74bd950417baf7f96632f03154e26ef29bb909dfd19560f8460ba5378bfd4
    role: context
  - path: mappings/unified_mapping_rejections.tsv
    sha256: 110a0a71c9126348cdb2ed49a210ecf37be46b6492c56329d78ae76bbb5c19e9
    role: target
  - path: reports/carnitine_hydrochloride_1004_20261101/README.md
    sha256: f8c53173700cda4bc348c66c1bdabf707a9edde47e9cef0225e63ca3219961a2
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/README.md
    sha256: 30766c5d367485ac66685dff8ee65c20f45870f21bd9f891bfcf383f5c373225
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/analyzer-1039/README.md
    sha256: 50dcdd9b1c398c4bdc0c8a52c147b518c8c00cbf02761a23d4a2a1cd74344ae8
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/analyzer-1039/evidence-index.json
    sha256: 273a9a71718b8f15b8cb407f7967c5533a156d9b67bc39d56cafec627edd2535
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/analyzer-1039/fixed/analyze_step3_final.py
    sha256: fb887535cc5f4e244d1830aa5576e74dc672535fe802fa786f18792e7e29926e
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/analyzer-1039/fixture-manifest.json
    sha256: d63128d21873b2dfa3428ed8cbad2edc4567febfd2ff36ec8d5876aaccc5ce70
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/analyzer-1039/fixtures/canonical-after.sssom.tsv.gz
    sha256: c3e7d80d166b31bb6faf283da51f01751ae97c53717707e409dfcb457f73cdf1
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/analyzer-1039/fixtures/salt-owner-after.yaml.gz
    sha256: 4c79482112d22e7d69640b34e58c45603768790881ee184c650416f13e750705
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/analyzer-1039/fixtures/unified-after.tsv.gz
    sha256: 4beb7092d54792bc5a52c0a381c3932280036fe7b8909d6e7e55ebfb68ee39fe
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/analyzer-1039/fixtures/unified-before.tsv.gz
    sha256: 2bbc779fc1b80cce0b89896166b7f0b4e50a569d3b49f9fb11d9c51822d2b76c
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/analyzer-1039/logs/step3-analyzer-1039-negative-controls.json
    sha256: 2e8938e5b471500b93d20cc7a9bcb15faf34ce56dfd7fa55d31813181e10a5d0
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/analyzer-1039/logs/step3-analyzer-1039-negative-controls.log
    sha256: b00b79f73a4931ea03ed6a7cc88e82d5c548d795f963c852de0006c393c7f552
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/analyzer-1039/logs/step3-analyzer-1039-regressions.json
    sha256: b7e248331febc5cbb4e9c0ba12dbd5429c35ba1527d3f5b3bebcd651d170f163
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/analyzer-1039/logs/step3-analyzer-1039-regressions.log
    sha256: b6c43919df176dfdd25a61c9ed422ab132a8b2bf019b11f28633403cda5923d7
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/analyzer-1039/negative-controls/mutant-tests.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/analyzer-1039/negative-controls/mutant-tests.stdout
    sha256: bb0b7ac5d1c0d483a9ee1f11fd4b66dfedf5f2920618dd8df1b31669c4e867d6
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/analyzer-1039/negative-controls/old-parser-with-current-api.py
    sha256: c4dce55394325993b0d7a944b818710ef9879e14d45d5e6112b872800b52b483
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/analyzer-1039/negative-controls/original-parser.stderr
    sha256: cac18e2b11b9aa9dedbacfd3df9e9a0ce1880b3f2c8c2f5c85eb5577494310ff
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/analyzer-1039/negative-controls/original-parser.stdout
    sha256: 7d339f9e680f13f5f5a7e1c39c8625d6dba6795947dfca488819340d0fdf5a94
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/analyzer-1039/negative-controls/receipt.json
    sha256: b00b79f73a4931ea03ed6a7cc88e82d5c548d795f963c852de0006c393c7f552
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/analyzer-1039/negative_controls.py
    sha256: 9183cf8d1fddf9ce4e10361bdf4f60988590cb9d282b8ff17a0b467606b9a8d5
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/analyzer-1039/original/analyze_step3_final.py
    sha256: 38790edcb9f5a8fb6439827ed74905a7b1aaaa0fda1c3c32ed5749bb5b66958a
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/analyzer-1039/original/analyzer-hash-prefixed-row-finding.json
    sha256: 14b9fd46c5d9bb1b9fd3671ee7c30f906fef03ab5572425962abd84883b44787
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/analyzer-1039/original/analyzer-hash-prefixed-row-finding.md
    sha256: f742bb9908ac5fcfdf9e709666257e5a13c755a711df1b93157416387fd12838
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/analyzer-1039/original/step3-final-data-comparison.json
    sha256: b0b0287d86d30f6055b7288a70964cdd3abc995d40cddfd4d8a9e9b5af8bc314
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/analyzer-1039/original/step3-final-data-comparison.log
    sha256: a2998024ecec71f75f340fe2d804a0882ac53c4d770391feca919efce6cc6277
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/analyzer-1039/receipt.json
    sha256: 7cedcab32916d1dbf8e6ec22465e910a20276572eab65efea1cbb3d141e156dd
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/analyzer-1039/source.diff
    sha256: 14b1bec038dc05eeb1e3c37504dab9af61290988f8cce21d82a6f9813fa97d60
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/analyzer-1039/test_analyzer_parser.py
    sha256: b01d90b378c8bc73275e783e8355539079f722af4d1140effc8cac1bb16a7379
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/canonical-validation/receipt.json
    sha256: ed3addbe4d069614ef6a9d1a9573085d13aa455e937fedeca8b7c3a9f00b785c
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/canonical-validation/rejects.tsv
    sha256: 9401ca51a25ee4f9a0aadafa73cc8f9266d0ffc60df7f037d1727e482367fc7f
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/command-index.json
    sha256: 0a90ba1f95ebcd7363a252786a388aa42722d0f9c2d2ea2d98b26c460612cb3a
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-candidate-curies.json
    sha256: d8c10f6ea0cd1058e96048a2a156397b19b29a7737155ed5d63a93faaec64765
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-candidate-curies.log
    sha256: 3f0dd1df23eab087aeff85f7cee6710a86aaf0401c9d75f2e64843578a6e4808
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-candidate-invariants.json
    sha256: ab1c039bc069d951f6cc038b44713292d43a3dd30ec5c622e68712ef38281b23
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-candidate-invariants.log
    sha256: 6dfa19d7311ba5b4b53678257c4a71bb79c1b80508c2be83299d2d00f2893fb3
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-candidate-labels.json
    sha256: 8eaaeb39b49d940b73cda465454ee8608060419e6e4c3161ba24fc7da427fccf
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-candidate-labels.log
    sha256: 8fde12342103d0a40af494c54a7f37a5aa67a79ac89596580617c5508c57261c
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-canonical-actual-kg-invariants.json
    sha256: dc7b57e7e8339fefdfbaaa2df5ed076afad1f79a7a533a87d648a4a9ca0318a3
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-canonical-actual-kg-invariants.log
    sha256: a269aa4924953047bb57046424dfc5cad8ec76fc79c5b419adc99318fed99184
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-chain-final-v1-full-qc.json
    sha256: 9750eb2d50f53d8a715d791191b5652f75bf8b0ee542301b1ca19df9adf9741c
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-chain-final-v1-full-qc.log.gz
    sha256: 642eb7b66ecebaec57eb0a13a4f0451027b779767e601461282d38bcfadc47d3
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-chain-final-v1-receipt-regression-tests.json
    sha256: f682f221fbcf704c8e60698515f49db64e891e42b51374a122976aae892b0239
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-chain-final-v1-receipt-regression-tests.log
    sha256: 03da613e6b96eca933559d8dadf27bd4a0139bb499d47c99d1ae807d4002e3b7
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-chain-v1-assemble-review.json
    sha256: a22c5e69864d1773aeecd04c69daecfc3be7ad34304ffa120219e916e35a4b99
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-chain-v1-assemble-review.log
    sha256: bce6f4f82775bdfb36067fc26af9fc1190d60f7f0414f83490798dced581e0f7
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-chain-v1-canonical-qc.json
    sha256: 9e79cd2aca4c6c19ebc08445b594f787efb14caf80a4908d407d323ca813b8b0
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-chain-v1-canonical-qc.log
    sha256: 9d5099bdc133d1f5f4ba5884b8ba485b3e49c6f651c56ef97c0e117cb1671172
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-chain-v1-companion-export.json
    sha256: fa6f07cdaa9d7ab004aabedaa94508b82db333f7b7170f3bd070f3319561b492
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-chain-v1-companion-export.log
    sha256: 3cfaf36112cf75cdc0c32b4f9596d9675f2ac6748bf7aa76ea9a71ec619d76fc
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-chain-v1-companion-refresh.json
    sha256: 82083c3c0cf2079e7b77e4bfa35d3a65c9424e99ba1b0e29ec159977e99ccadd
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-chain-v1-companion-refresh.log
    sha256: e43ec48f32429bde041698342b5e378b1e0927a62b15fb27d37ffd7deb557877
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-chain-v1-companion-validate.json
    sha256: 24e5616030b4307051a57ffd40d459340d0d5340402ff768876cb5bff8160f4b
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-chain-v1-companion-validate.log
    sha256: 3b39954204810314888d89ac178d31e65c9f7018ccf5a0adf2a15ae4bdcf047f
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-chain-v1-full-kgx.json
    sha256: 72cd53846063e626df552345518ea7411368e474f562f2b6ac8bb2cb5d94afae
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-chain-v1-full-kgx.log
    sha256: 142c7d26ca5024d730d8fc1b82828766e1f22de9c9530d17772e1ae0bf191541
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-chain-v1-reviewed-export.json
    sha256: 50c0855812a5137413566d35766107d4f8ce0520e4340b2b59b9356f172a7bb5
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-chain-v1-reviewed-export.log
    sha256: d410d7e15415b04368b6c0ab87a949790f6e73667063936c7ea1e2e68161ff67
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-chain-v1-reviewed-qc.json
    sha256: 603bdd172e36982e9a72ffc6ecab8681de1df316fa5d2c8536e108d7b9f67585
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-chain-v1-reviewed-qc.log
    sha256: aaad5769b7148169db4ea3fbde47c5d434eb83f1b5d81466ebc96c080183f35e
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-chain-v1-semantic-build.json
    sha256: 245d3f1e99b55b0c13bed60369d4a9568e2ce6a2a378e6bea21303fecc981ab7
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-chain-v1-semantic-build.log
    sha256: 9a58101cfe81fc0a8db19b102121a0e31275af5493e7bc486ab0727159933c74
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-chain-v1-semantic-integrity.json
    sha256: 59ea8a60011e0b43f61fa4ef3bc3746c72761e1a9359900d3dfc69e9bec90e20
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-chain-v1-semantic-integrity.log
    sha256: dee543f4580877b9c6bc34e25e841ff8cc1feab9cb7d4ce6f05dba45997c6421
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-chain-v1-supported-export.json
    sha256: 9acf0b5b36d5a1a8075cac0dcd6c119b9831446f83b97be8d5521bbc784b4c95
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-chain-v1-supported-export.log
    sha256: 263fb9d18c6b651bcbfe1f457504848ef4999a5c270870dde6343758193e8fa3
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-chain-v1-supported-qc.json
    sha256: 776d26b2ead136c9f4d62424cc76abd22a870e0024d2c8c9d5683f40cad60afc
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-chain-v1-supported-qc.log
    sha256: 91c1bb6d9c3c85681f8b9fa583c8b30ed74eecd11fe88cfa97284286aa971afe
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-chain-v1-supported-sssom-schema.json
    sha256: 07251cfe3b32ffddee99771bbf02b51e3329c0ea8ee9894751b857535f04916d
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-chain-v1-supported-sssom-schema.log
    sha256: a54431e28e5bde91514875adc222f6fd4828ab17e420f921fa6d98df73ef1ac7
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-final-data-comparison-after-1039.json
    sha256: 15cc73f090ddda839bfb2b5478c49296221262eb2d4f3cdcf51c532ad0cfe3f4
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-final-data-comparison-after-1039.log
    sha256: b77138fb5e21541b2d3511aeadd1be7931ecf0cb3d5d4b6cd48d978302fed769
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-mapping-promotion-after-1038.json
    sha256: 513de392312814a6e5a43fa8aaf648cf22dfd20820eb61549cf13cc9f90a149d
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-mapping-promotion-after-1038.log
    sha256: 42df9d33ce1e55f82fa8530e3f71c36ef7e13b7b895530e9a72c2e5352572fdd
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-native-candidate.json
    sha256: e178e68ebafa148674e7a60873380e7d514f724fa9b9f61511b566a3f9a25ab3
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-native-candidate.log
    sha256: 582f6b8ffa9939337dfe0fb41653b52a645a78af146b3395ba88e8b692d4f44c
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-promotion-dry-run.json
    sha256: e06152def39792039d04cf55e60c66d8257a082ea4b463b00a4dffffe3f9d736
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-promotion-dry-run.log
    sha256: 23bd121fbd29bf5c6fff455a08ce92673480156298df94a685a40228700acdb9
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-unified-generation-v2.json
    sha256: 9a97f67f7bfbf0e0bd02fd88804f90404721abd1924d1b3ad77083b5a928a633
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-unified-generation-v2.log
    sha256: 780e7eaca4cf8a1649f67008f8dea341b335300582891dc9fa8fb11d5ad1cd5c
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-unified-generation.json
    sha256: 5f710b107642b7181d7e787cdee8afb95f6e9857960c199f37e35da6f4e2b67d
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-unified-generation.log
    sha256: 33d0911438eed01438b254827eef223413c23de1f0da4dc757d4607176b90343
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-unified-stamp-and-visual-check.json
    sha256: 57be35e31bed23a9f62838d381f9951cbfe32c2227112db4efbd8689b8e73551
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/commands/step3-unified-stamp-and-visual-check.log
    sha256: 5f693f49b3cc9c9cd6152ae5e272bcdee89396090c5721b79163f1d0c1180693
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/harnesses/analyze_step3_final.py
    sha256: fb887535cc5f4e244d1830aa5576e74dc672535fe802fa786f18792e7e29926e
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/harnesses/generate_candidate.py
    sha256: d8e7a2299eb593c9aa1c341bafd6dcd5d2f6a71c6e4aaeff3f3ce325a04981bc
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/harnesses/guarded_unified_carnitine.py
    sha256: 9ebeb9ce10dd432ac5767c82f24a6d245a71189b83289f19f92507bfe1230710
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/harnesses/run_step3_mim.py
    sha256: 83ac79a164ef8d9756445356136e5abd800f3173d9ce165d40fd10e725e9691d
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/harnesses/validate_candidate.py
    sha256: bbb919eedc990552445af562ab5cb7b0ea06ce95ab18d614cd5cba80e4b6ca5f
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/manifest.json
    sha256: 29f25c513667b0d2f1ec8f7482cb14b96e8d607d7b72252e621ec945e4ecd4b4
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/native-candidate/candidate.sssom.tsv.gz
    sha256: 570c671bd810fc5a800aaa3c1fb8522bafea2bdb229ebb66d5bd83100809ec15
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/native-candidate/comparison-inputs.json
    sha256: 37f6b3bb4efecb31ef0932ca1d4c81f31b871d0a1f460bd3b244b8abd382236f
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/native-candidate/generation-receipt.json
    sha256: 1476f014b3b51988012609517bdf1fe2f4116a626f1466de4f1ef36af1675424
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/native-candidate/inputs-after.json.gz
    sha256: 603970efa88341b1a410e8722e58ddb523c7ecba76184ed2837c11ded916bcae
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/native-candidate/label-config.yaml
    sha256: d0c240d4a48be00df7341082e7764ef31df1e6fb223739f6d8a35a47e6c0bcfd
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/native-candidate/label-input-01.json
    sha256: ea72f093492dac72c8aa6edaaaad01a4d8df258197e8d8b33bd71a94f1dfab82
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/native-candidate/label-input-02.json
    sha256: b2ebec7ddb8aec9b3b8556244d1045833b01454c27a0bd3412b78f407baed761
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/native-candidate/label-input-03.json
    sha256: f0ae86b5c40bb6b8310e47c6800074ca08a399e2ff2ad5d29f9c018e76f72bf9
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/native-candidate/label-input-04.json
    sha256: 4e560b30727e589808558eb1bbcef9846ea1fe8bfe2fbd3c8e017fef838d25b9
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/native-candidate/label-report.tsv
    sha256: 1b8dfc04bcc2e2b0f654c2115bf40d64a3e1fe4830c86afc3bf65a12cc08a691
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/native-candidate/native-invariants/receipt.json
    sha256: a2d8b64a67eb751d4bc8df52984414d01866361f92bceccc525edc2ae0c5d720
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/native-candidate/native-invariants/rejects.tsv
    sha256: 9912547da4ff594c686b21a13cd11d06997878514645162518fa712f99d13cea
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/native-candidate/repository-context.json
    sha256: 65f4a143740c47bb2c2fcee31455c34ec0818ee02c5b9538465421587ee5c3de
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/native-chain/build/commands.jsonl
    sha256: 6a2bdc5607bc9483c1ddc68cfb1ca8ade6fe37cebeedc81f352b38ed353462ad
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/native-chain/build/complete.json
    sha256: 5b5ceb7c839d42b5ec9c4fc0d137551e53bb195977f1cb9cbeadac58e05b6ca6
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/native-chain/build/start.json
    sha256: a73639769209ed0057c4776c48b4561d1c40f4ee1aa9e4183d5c8b509a4cb5eb
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/native-chain/build/verified-output.json
    sha256: 3fb11b27841976ce0c23bc9ee64b7e1be15075c2183d3f8d2ac86a1653f06d41
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/native-chain/plan/README.md
    sha256: 0650c8d38c171ce2a72c4d7e05b121d59d48bf4b0c9c9416ec8352f7a7c65f91
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/native-chain/plan/evidence-index.json
    sha256: f2eda11287dc8b5e5bb56be74ab19a3ce670e859073fbf93801dcaf1bb2b7ebd
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/native-chain/plan/native_chain.py
    sha256: 722bc35c30dd8a13bf2fe4b187a5cfde4f94ecfbc799c9135b4b08d04ce57640
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/native-chain/plan/nldm-before.json
    sha256: 47d77e1a52b0d043afcccaac9735a07303b9862e7ff8f8fc82d3179045005336
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/native-chain/plan/planned-repository-paths.json
    sha256: 1acd4816929e5180007334746bbd01d089d1a2f6ce5debdf763d3f084f7b8f86
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/native-chain/plan/preparation-receipt.json
    sha256: 0802fc5070ce8f85aeaf2a93e2e9e8bb573fc00268df5aac9e2bb6c69235e1d7
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/native-chain/plan/prepared-inputs.json
    sha256: c3b46ecc9f182871a2c20e698a76b8afb2e25c668452fbfa631f7ebba333a19f
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/native-chain/plan/step2-command-basis.json
    sha256: 631c87ae44075572011f7a59464aac4742658f502a0ecfcb08a422e719588b7d
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/prior-failures/1038-prior-stamp-finding.md
    sha256: ca80c92fc337f6e90c23e184f64311bf457d67061048ebca23d4d1b5517e4de5
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/rebuildable-output-manifests/companion.json
    sha256: 1534bc1cef2f995deabb6e7c725bc02c62fb5e6ee4edc762def85b509c0ccd49
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/rebuildable-output-manifests/complete-kgx.json.gz
    sha256: 99cc7c4850f47a4c55036ceee12356a80cf02ebaee98a94b3ea3c5099805ca6a
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/rebuildable-output-manifests/reviewed-sssom.json
    sha256: dc989f9ba4368bcb711107b1fa5db9d28cad9221f97732a70576f5a0859d0c6f
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/rebuildable-output-manifests/supported-kgx.json
    sha256: 7bdc3dae9036295c82a4dc45cf7ff8513781e2405eeba7d244b778577e6bacd3
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/summary.json
    sha256: e2291020e73a96c50b24e986fc777126af6e50b6954807162804676b0bf9c592
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/unified/unified-before.tsv.gz
    sha256: 2bbc779fc1b80cce0b89896166b7f0b4e50a569d3b49f9fb11d9c51822d2b76c
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/unified/unified-candidate.tsv.gz
    sha256: 4beb7092d54792bc5a52c0a381c3932280036fe7b8909d6e7e55ebfb68ee39fe
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/unified/unified-generation-receipt-journal/write-f6hm90e8.json.gz
    sha256: fb5d6630e8e04b825be22ed6e73d11074b603c285e1d5eec0e4e83c868ed81bf
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/unified/unified-generation-receipt.json.gz
    sha256: f7e4ab5fb35e96f62ed830ed441530b6b3ecec859ff3534ee3e30e415e24828b
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/generation/verify.py
    sha256: 3e4f8c7264e3badc841e0b737df8c74855c06f610711d3e0a74ab43765e5b369
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/README.md
    sha256: d70b89432f3e98526c52735838ee58f1b2ee7ec259354b756a962d1eacee9ee1
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/application/after-sync-proof.json
    sha256: 917aceefd573945a4e7789851a3272775508239c3acb055d156f62e06f21fbbb
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/application/logs/step3-mapping-promotion-after-1038.json
    sha256: 513de392312814a6e5a43fa8aaf648cf22dfd20820eb61549cf13cc9f90a149d
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/application/logs/step3-mapping-promotion-after-1038.log
    sha256: 42df9d33ce1e55f82fa8530e3f71c36ef7e13b7b895530e9a72c2e5352572fdd
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/application/logs/step3-native-mapping-receipt.json
    sha256: 49245ef4a4e338be335af56fda960464b511ab54b799221a30e5e761a7bd1fb1
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/application/logs/step3-native-mapping-receipt.log
    sha256: 94dcbbc45b944dc29e6e4d51bfc31e3f274ece38bd1e268550ecc092d2834f2c
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/application/logs/step3-promotion-dry-run.json
    sha256: e06152def39792039d04cf55e60c66d8257a082ea4b463b00a4dffffe3f9d736
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/application/logs/step3-promotion-dry-run.log
    sha256: 23bd121fbd29bf5c6fff455a08ce92673480156298df94a685a40228700acdb9
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/application/logs/step3-source-apply.json
    sha256: ba712fdc92dac213b4bac930aa5f898f653aa72f4b764543cd2b31b532cca54c
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/application/logs/step3-source-apply.log
    sha256: 102d6f53324b4cf61d9c45f4f5d4b6beb39bbf6694fa3459689b4fe2189a8ff4
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/application/logs/step3-source-dry-run.json
    sha256: 21d3a18ad102bb1ce3057f41f01a36dc8a431df6405e97c67fc53acc03171f88
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/application/logs/step3-source-dry-run.log
    sha256: 0d1d8c7e43fe219ff30ec55a2a5e941a445db45b690197ac0e7d8a64ad9f6d99
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/application/mapping-promotion-native-journal.json.gz
    sha256: 73a10180ae03466c815777d853d6575af1335120f4b5d9158301c09c388a6523
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/application/mapping-promotion.json
    sha256: ee15f7c4ec2e8f7b94d2ad17d257d96fb52b058248f012d30dda61494d108389
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/application/native-mapping-receipt-17.json
    sha256: e14ab50d5b981f2e003d755644ffcb98c901519fc0e8324658900ada1ae12e1c
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/application/preimage-references.json
    sha256: 24bc7408b7e38ad05e42bed81d8898dd85404b1498aff4641c20cdbe14771611
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/application/preimages/mapping-promotion.before-other_cross_record_baseline.tsv
    sha256: 170368983e4105773348122d44da5417745e675dfa9151f72270f19da7a26008
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/application/preimages/source-apply.before-Carnitine_Dl_Hydrochloride.yaml
    sha256: 8a7e0ac23a72c403bf9cce38a20abe817ee83e0231b558f2ca07ed05d134d190
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/application/preimages/source-apply.before-Carnitine_Hydrochloride.yaml
    sha256: c03c1c66b9e70436da2e841d1edf2a700f05830674c715fc265ac7fde9705722
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/application/preimages/source-apply.before-NLDM_metabolites.yaml
    sha256: 7332021e0d760384bc0381f5e00e3a87bd4dfe4b7c5b2eb1140853f7c17d78a0
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/application/preimages/source-apply.before-other_cross_record_baseline.tsv
    sha256: 170368983e4105773348122d44da5417745e675dfa9151f72270f19da7a26008
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/application/preimages/source-apply.before-unified_mapping_rejections.tsv
    sha256: 717289ca0e45046dcb96f6839b843838a6636fd8e120cf4d9b9ac48de3d9016d
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/application/promotion-preimage-references.json
    sha256: ff9c98ef1726126c3cee398d74d0a070b01f8121e05aa4a629033ffa4b62f221
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/application/receipt-publication.json
    sha256: f51d154d64566630c4141b7d47ecd1923e401a81eeadd55fd9e9dd3c3da08643
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/application/source-apply-native-journal.json.gz
    sha256: 26f39b60d3849ed3fd5f2b855a6e4317633d13b30a049735e86e3d036227a196
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/application/source-apply.json
    sha256: 8e031dc9d823b904dbbd3cab07d5dffa8411d7a4c59661d96ad8da6217743533
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/dependency/HANDOFF.md
    sha256: 9275effe6f9436abcf2ff3515494ad135890b9e7b9c1163aa4f924411f5ed8b4
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/dependency/capture_fixtures.py
    sha256: d190ea349c8b958984c785f198e23b76f38ebf438227276c909880b064aaaa9c
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/dependency/logs/step3-dependency-lint.json
    sha256: 77e248d5676677c41d0de26fcd6a3e39411d8b6743fdcb65c8781ba562212ecc
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/dependency/logs/step3-dependency-lint.log
    sha256: 82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/dependency/logs/step3-dependency-mutations.json
    sha256: 35ae750479240afb717de58a5e9ff716708d7e98d6476bff605f061c9d558401
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/dependency/logs/step3-dependency-mutations.log
    sha256: eefaf7e232b78bcafd244e86eb738b36c486e26858e1e5b5eee10a6e50904f15
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/dependency/logs/step3-dependency-stable.json
    sha256: 9cc05e4a20b7a131ac9e16810c15028df95ecc8991d670e4dc68ba4f4562bdd8
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/dependency/logs/step3-dependency-stable.log
    sha256: 7f48df68848e62c96af1903a25a815d7c97f86479f0c8cd17fb73d8ea47e5213
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/dependency/mutations/allow_changed_owner_approval/pytest.log
    sha256: 1f55b67bf2160c81430314ec62ddcd11f1162cef29dee03bd4125a26c94c3774
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/dependency/mutations/allow_mapping_approval_carry/pytest.log
    sha256: 4f1fab9de4baa26880e9c18f3e5357410b8a8d931fb9444c121d4fde74515e4d
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/dependency/mutations/broaden_old_id_group/pytest.log
    sha256: 78aff33f11c5883e5094a9a85abdd23465d4a552fa5c5b22e6ad5b300389aa94
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/dependency/mutations/count_rejected_tombstone/pytest.log
    sha256: e6f0586b833c11e1773aa754a67e77a6b31c8ef6b1bbadf1febbf8cd65e90603
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/dependency/mutations/receipt.json
    sha256: f63694c5d76c8a04348370a21e611b9c2612951615d5f8595292b6a2bcdec965
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/dependency/mutations/remove_salt_routing/pytest.log
    sha256: 45ee5bfbfb24590c8a4a02af8ae3f0d5eb4c1a5469fda2ef53f95b52ac3578c7
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/dependency/mutations/skip_explicit_plan_validation/pytest.log
    sha256: 0758b907cbdb79f04846a5346155dff690fce977b7db3007d5bc3d35c9ecb3fa
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/dependency/replay_unified.py
    sha256: b90a46efa9eee5ec6eb6ba548f7fe52fa307c85b8561d23423998b2feb111209
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/dependency/run_mutations.py
    sha256: 14efd1030ec564bf056d83960d023636769bc0fe424208eb6c48044853add13e
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/dependency/source-stable.json
    sha256: 97a6c783cb715270c5414d6096e075b359faacd8398fe179f91621e2974a4be5
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/dependency/source/src/mediaingredientmech/utils/culturemech_occurrences.py
    sha256: d8b5b0ea02bf6c885d9627357dba04c2ba59626ca9bf12062ac70e7d6bed8c68
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/dependency/source/tests/fixtures/issue1004-routing-dependencies.json.gz
    sha256: 45e583e9168ee45124d59543dfd371d3919b359435e652e5fb948ff9557c3811
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/dependency/source/tests/fixtures/issue1004-routing-manifest.json
    sha256: 6d999758413f6b6bb42db709c1b97a08c313cff10bbfa3a987aa15f61b1860a9
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/dependency/source/tests/fixtures/issue1004-routing-occurrences.tsv
    sha256: e7fdbba52261189a462da2e4ada8f80f99c5b047dbb3d2627c29b545478f2c35
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/dependency/source/tests/test_carnitine_merge_dependencies.py
    sha256: 89c37f67ef98c0e96b8c359df8138ceb579d1962bae0d7f52290219b2d9da042
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/dependency/source/tests/test_carnitine_occurrence_routing.py
    sha256: 886042936835d7a5cd92aa566d7e8107f40047ee136aa23063891bfc5a2e3443
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/dependency/unified-replay/receipt.json
    sha256: a50b25004a9a3fdf6326a7e18416a81275491bbbf64d62794bff837c3f49e124
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/logs/step3-independent-1038-actual-native-probe.json
    sha256: b2f44a5ccc040af084956c8051c074d1d70dc6c3cc452c04835e6892dec8f36d
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/logs/step3-independent-1038-actual-native-probe.log
    sha256: deda343f3f487194680f3dcea98a337d0a7b2e295ff337fa85d4bb644d346217
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/logs/step3-independent-1038-focused-tests.json
    sha256: 42166a38748a9976872f9c716e54a898892fc1c25b37d4377ccadc041021f5ca
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/logs/step3-independent-1038-focused-tests.log
    sha256: f8b8f13278f6d4986708c6b59ffd502303b8c87df4b9fe8fccf8c596fbc5ba5e
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/logs/step3-independent-actual-source-application-v2.json
    sha256: 672e55ac462e4d27fe1730ff59105eeab312e8f9557aba5be1be03e346d79a53
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/logs/step3-independent-actual-source-application-v2.log
    sha256: f9de3451f5d6f0ebed29e33b2d3d4424d2b35599ca242d3f3f234bffa27e226a
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/logs/step3-independent-actual-source-application-v3.json
    sha256: de89df89f8ce5d8578b2d008e73da52df27ac451a35c9e95641b02810fb0fe83
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/logs/step3-independent-actual-source-application-v3.log
    sha256: 98d9304f8bdac0a51b4b077f4fe6cb9ed21df478963aafc4d6d819a7ef90d11f
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/logs/step3-independent-actual-source-application.json
    sha256: 96aa112ec8909ef2534c7d64039b18d4bfec7ebfcfe7cc5dcfbf0e3cfa1bf338
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/logs/step3-independent-actual-source-application.log
    sha256: 48adb03b95a63489aa574fa66a820ddf1ed64157e952400aa014394ea1d5a6c7
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/logs/step3-independent-final-writer-dependency-tests.json
    sha256: 746327d2c9e57ff63041007b2900d082a4d1143c655de011dd93280f22efffbb
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/logs/step3-independent-final-writer-dependency-tests.log
    sha256: 46c805aeb3b6a808328629fe1077c79546246411d10dfad55d740c6354613971
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/logs/step3-independent-native-boundaries.json
    sha256: c705d020800795dde54d7bbdf323e2fc86cf30cffdf45007d99b5bd199c2d198
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/logs/step3-independent-native-boundaries.log
    sha256: 24ec8afa9843745519e045ee48295627d50a667f74488a71ab8194e9f3d8c317
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/logs/step3-independent-receipt-orchestration-original.json
    sha256: d239989235f0ebd3bf5852ff3b29bcedb9ba7456a35b083b08c1affcd272142f
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/logs/step3-independent-receipt-orchestration-original.log
    sha256: 5994928e229c85eee7f61f0fc6c3906bf97f1d75f52774702b4d88578a0ebd50
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/logs/step3-independent-receipt-orchestration-recheck.json
    sha256: 713983fae3cb12f326c6e0a3b95524e0088ac43bb798d6bb940a29fa1d21f23f
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/logs/step3-independent-receipt-orchestration-recheck.log
    sha256: e565f2eae03c4cdd2da749bfe975c62bd801593437ea31c8fcdacb11adcec84c
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/logs/step3-independent-unified-orchestration-original.json
    sha256: 15ded9d76dd550c113cbfd1b1ef8538a34f9432d3315c7dd296c25df0a47d25e
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/logs/step3-independent-unified-orchestration-original.log
    sha256: bdeced93750184482f3cb0867f23da561940e7007b0762de73f4f033ca6691e9
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/logs/step3-independent-unified-orchestration-recheck-v2.json
    sha256: 00afafbbc990c0521742ee83cc63660f6b16043690a33d1f03c4b8051b9d046a
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/logs/step3-independent-unified-orchestration-recheck-v2.log
    sha256: e9b86be21d36072dbf337c6328e4824c594d48362c596e46d5ad33154fb7994e
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/logs/step3-independent-unified-orchestration-recheck.json
    sha256: 3c6315c6f6b3a9c2196c0c5dbc2e01cf9dcf6226ae7ba7157b0bb6b17b22c431
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/logs/step3-independent-unified-orchestration-recheck.log
    sha256: 5912a3c62e1a7fba1326fe0db8b7dee7af4fe2d03824e8f69d7c4bbb7724ac98
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/logs/step3-independent-unified-orchestration-v2.json
    sha256: 1faf6b34f9be9efd0fd72fe73e56d8673a36f881ac2e4a4fbb59ccb9b1945ce4
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/logs/step3-independent-unified-orchestration-v2.log
    sha256: 4c02de5c997e41d07ae0ed44982c96bf772b99716eb2b0e500b2de3e1d58e62f
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/step3-mim-independent/actual-source-application/check.py
    sha256: aeba6323eb7936c64eea88e8a5131cbf5c6f10ab29180d570a9b23a2e61d9a92
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/step3-mim-independent/actual-source-application/check_v2.py
    sha256: f9111b5b95db6396c8911773484c75540d15edf08bf1352f708a93dca9a873c0
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/step3-mim-independent/actual-source-application/check_v3.py
    sha256: 3022258a5778fc5daf541db17aaf2005bf684f4939589e471c0d3a36e462032f
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/step3-mim-independent/actual-source-application/inventory.json
    sha256: 1ef753541ae0ff70605ea3be551077b098b41f5720435f4464364e5127c6c2ce
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/step3-mim-independent/actual-source-application/native-candidate-inputs-recheck-index.json
    sha256: c17b0a90f0046aaa00f217ac91a247b264598b96eb882121628738c95a72d569
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/step3-mim-independent/actual-source-application/native-candidate-inputs-recheck.json
    sha256: bbe43bf2e3b402d55d2b391fd53edd158250ca268c4849b1f2b042970fbf3c72
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/step3-mim-independent/actual-source-application/native-candidate-inputs-recheck.md
    sha256: 6925cd141db5c11e500589d8aa69d946001cac8c267fc736267f58ad37a9d692
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/step3-mim-independent/actual-source-application/receipt.json
    sha256: 98d9304f8bdac0a51b4b077f4fe6cb9ed21df478963aafc4d6d819a7ef90d11f
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/step3-mim-independent/actual-source-application/review.md
    sha256: 630462f72aee98811f30a2460873ad40922ac5e34da4c7130d8516ae1f34ca54
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/step3-mim-independent/implementation-preapplication/freeze_review.py
    sha256: 7f63433edb15cba0528b013732f6789d3d3d56c5b8dc7230a3490d2ca2526b4f
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/step3-mim-independent/implementation-preapplication/inventory.json
    sha256: 330b17f3f1202cdb32525ca06738a012b1be53084cec857e09388d84f99e04ce
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/step3-mim-independent/implementation-preapplication/receipt.json
    sha256: 8d7144972abe9d4e0e9469a972518f0b52a20ef9ddace8e753d8156ec758bab8
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/step3-mim-independent/implementation-preapplication/review.md
    sha256: 619f34b9467eb8ce537e820375895b2db821e31cb5c08641054f28a06ef41cb9
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/step3-mim-independent/native-boundaries/probe.py
    sha256: fef7c3433cc605ed833d61be0eef57669f6154768d75e32ca0deafcec49da1d9
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/step3-mim-independent/native-boundaries/results.json
    sha256: 24ec8afa9843745519e045ee48295627d50a667f74488a71ab8194e9f3d8c317
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/step3-mim-independent/orchestration-preliminary/probe_receipt.py
    sha256: 63ee9719229d13a56fb8e696070f32aba26a4cfd7c319e7d37e8ec823a69a7de
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/step3-mim-independent/orchestration-preliminary/probe_unified.py
    sha256: da4ca4ab06f7ae172e4289f5638887555658a0c16fd3c7d46efaa0cb20f66759
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/step3-mim-independent/orchestration-preliminary/receipt-probe-results.json
    sha256: 38705d44518c910a285cb47bf0aef1ef98f0477d3b992305861efa03dd929d60
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/step3-mim-independent/orchestration-preliminary/unified-probe-results.json
    sha256: c04ec786a7452e3c5698ecf76e2a16c8347b0f768816cf6e10328d2a348e6137
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/step3-mim-independent/orchestration-recheck/probe_receipt.py
    sha256: 914a02acc5f54eafcdcbade266edb15e5c0026048209aec236219cf527d5cb2f
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/step3-mim-independent/orchestration-recheck/probe_unified.py
    sha256: 1c01f503d4f3baa1dd7f16d39d0692fdcffc28b819295c0ef21d4ae368eda986
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/step3-mim-independent/orchestration-recheck/receipt-probe-results.json
    sha256: cdc599682f4fd9b185d1679d9886cce4ebb9b922ec73c856909e9f3b235fa6bd
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/step3-mim-independent/orchestration-recheck/unified-probe-results.json
    sha256: 55f890aaa5d2ecbd9b437e8f1b389726ab48bb0b03c2e91e8d955633340584b9
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/step3-mim-independent/revision-1038/freeze_review.py
    sha256: 93f87affb2b6006fca6c2b3071992787b69ec5a20ce7b3fdc3f1545641d91d10
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/step3-mim-independent/revision-1038/inventory.json
    sha256: 3e2229ee7cded10650d8cb43f9fade1325115e1b3d5938481fd6aa2460eb7c47
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/step3-mim-independent/revision-1038/probe.py
    sha256: dbb17d6b09c2c23a0619a2a6f18120a02bf5088554e70391e93bd06c0e09f777
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/step3-mim-independent/revision-1038/receipt.json
    sha256: e92603d0ccc8a6aafd22d1bdab2b9ce1d7f4e87b9f6dbbae02537aca96bae2ee
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/step3-mim-independent/revision-1038/results.json
    sha256: deda343f3f487194680f3dcea98a337d0a7b2e295ff337fa85d4bb644d346217
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/step3-mim-independent/revision-1038/review.md
    sha256: d84e87ec1dd40931fb7eacdb4b62d9eb32bfe3efe70737d5bb97b5f2ea238572
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/maintained-source-references.json
    sha256: c89d275317f15f35c65bae50ec3711aa48d601f035a34f0556a79825502570b0
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/manifest.json
    sha256: 89dd30961cc14cb1dfa8926133d263779685c2a6cdf74428a1c8a9adb6d65baf
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/original-paths-supplement.json
    sha256: b2a3fe79b76a5f85a05efcf9ade012559d34b2e8df4a13e5a0f21d82689703c3
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/original-paths.json
    sha256: 2517bb2597c98ef93c69b2c3b3adc19efee9cf551bc6e5b3a950ff1f8420c057
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/repository-references.json
    sha256: fbd5d9132bf9b997d5d684f661aef2696b4a5ff0d1d01d6ab3420840a0ba1d41
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/root-execution-snapshots/generate_candidate.py
    sha256: d8e7a2299eb593c9aa1c341bafd6dcd5d2f6a71c6e4aaeff3f3ce325a04981bc
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/root-execution-snapshots/guarded_unified_carnitine.py
    sha256: 9ebeb9ce10dd432ac5767c82f24a6d245a71189b83289f19f92507bfe1230710
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/root-execution-snapshots/make_step3_receipt.py
    sha256: 066c666c180ce559c7ac19c85707e8251045bb5e52a145d602dce4096bafae21
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/root-execution-snapshots/run_step3_mim.py
    sha256: 83ac79a164ef8d9756445356136e5abd800f3173d9ce165d40fd10e725e9691d
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/root-execution-snapshots/step3-mim-context.json
    sha256: af9e62ee3ac8cee476ee4b7feb824a2b7d14acac2b5686973b3135211a448b7c
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/selector-binding-1037/change-proof.json
    sha256: 8e5351bd75f28c0645dbbb544a2174a590be74b907a563319c2490ff4becd675
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/selector-binding-1037/control-original-paths.json
    sha256: baa8575e07a9657b54556538322e23bd728cfe5a471bbc6cd2a7cfcf5e09d488
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/selector-binding-1037/controls/arbitrary_selector.log
    sha256: b5ba9d67d8b814054eb03394fb66e0e99d6a3737c20722b5017d55dbe2fb3863
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/selector-binding-1037/controls/baseline.log
    sha256: ad971089ae603c8582ba8fd3184a356691fdb38f25e10f45db675d4e9f8a8846
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/selector-binding-1037/controls/negative-controls.json
    sha256: 99d4f0b0f09b44a6f669be9a5448f3a0aa8fc627d732e6beb1d3fed3dc9257d6
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/selector-binding-1037/controls/protected_qc_evidence.log
    sha256: d5689af353ecdd837cea37a378a8015f0e3e10ac4cdbb31d12962b187e850fe4
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/selector-binding-1037/controls/provisional-manifest.json
    sha256: f1c547f260a4500f681d4126df114b89a273031ba3ea73d47bfcbef159a50199
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/selector-binding-1037/finding.md
    sha256: 0f7d0c2340e9dc922b4291821cec5b6bfcdb8f04a0fc0468879aa72c10d731a2
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/selector-binding-1037/logs/step3-chain-v1-companion-export.json
    sha256: fa6f07cdaa9d7ab004aabedaa94508b82db333f7b7170f3bd070f3319561b492
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/selector-binding-1037/logs/step3-chain-v1-companion-export.log
    sha256: 3cfaf36112cf75cdc0c32b4f9596d9675f2ac6748bf7aa76ea9a71ec619d76fc
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/selector-binding-1037/logs/step3-chain-v1-companion-refresh.json
    sha256: 82083c3c0cf2079e7b77e4bfa35d3a65c9424e99ba1b0e29ec159977e99ccadd
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/selector-binding-1037/logs/step3-chain-v1-companion-refresh.log
    sha256: e43ec48f32429bde041698342b5e378b1e0927a62b15fb27d37ffd7deb557877
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/selector-binding-1037/logs/step3-chain-v1-companion-validate.json
    sha256: 24e5616030b4307051a57ffd40d459340d0d5340402ff768876cb5bff8160f4b
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/selector-binding-1037/logs/step3-chain-v1-companion-validate.log
    sha256: 3b39954204810314888d89ac178d31e65c9f7018ccf5a0adf2a15ae4bdcf047f
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/selector-binding-1037/logs/step3-package-after-selector-check.json
    sha256: a3ae870fabd5b051013556474e99169bb07c3a0abf01e6810cc8c710fa13714d
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/selector-binding-1037/logs/step3-package-after-selector-check.log
    sha256: 7726be62b564bc959c09f3bc2bf2b157bf7b7bbf4d58042196190a36d2b0dd9c
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/selector-binding-1037/logs/step3-selector-binding-controls.json
    sha256: fce4c4d7f6491adc40362a579954065360e29710a1c85b159b82317de5cd7147
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/selector-binding-1037/logs/step3-selector-binding-controls.log
    sha256: 4877f0ffd29dbc8290de61e70c3fa7eed459569721e9aa14b9d8953f332fa643
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/selector-binding-1037/native-companion/dependency-refresh.json
    sha256: a431e7347efd4f4ec3823b723edb4099318c4b7c41e287e0b8bcec8ca08cc059
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/selector-binding-1037/native-companion/export-manifest.json
    sha256: 1534bc1cef2f995deabb6e7c725bc02c62fb5e6ee4edc762def85b509c0ccd49
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/selector-binding-1037/native-companion/prior-review.json
    sha256: 7ea74db32bcc33b464a39101e9d81319729dcc73ffd2eba997fa8c99cfb735f5
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/selector-binding-1037/native-companion/review.json
    sha256: 1d208eef5d6a250a37df4928d21aea477bec96ddb7cf7ebdacce1e370dcbed4c
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/selector-binding-1037/original-maintained-source-references.json
    sha256: c028129f93927f7368b3f687c10a14c8bc97b85d249355ceeee7fa0ceb74dcd2
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/selector-binding-1037/original-manifest.json
    sha256: ebabc64251b29f0008a53f88a750c7c586ed4dfbefc2f2a556f8d0ac1bb58eaf
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/selector-binding-1037/original-package-preservation.json
    sha256: dfbe828a93b93ff6eb6b78891a657af74fa9080f6be9cf629019166e37c1729a
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/selector-binding-1037/original-paths.json
    sha256: f5c96b6a7b5e3666d1f37d7d4ff7a12ffccd3dfbc73a924ce5c3e6b88cc216e6
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/selector-binding-1037/qc-reviewed-sssom.after.yaml
    sha256: 9b6d2b4afba2998a3a9bae3e6b2964fc1e92b7708a06385623dbbef51ebb3600
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/selector-binding-1037/qc-reviewed-sssom.before.yaml
    sha256: 70a6cf78722adb6f29630c8c032403641026b7bb2554578cd91fafdcd0a82321
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/selector-binding-1037/run_negative_controls.py
    sha256: 42f738e2bc8e387f4011f8588e7d8f267b459a402eb334af2412c47468c151b8
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/verify.py
    sha256: a00ddeecdf381243222b01d94ac7b4aa449b7ec097e5cdb2857de32ab77b93ac
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/README.md
    sha256: 9c1d10959e7452ff0c6d52aea4029c6f6327521ccb9a7ba7a33e38fa98b314e3
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/completed-receipt-binding-probe.json
    sha256: d10d06cc776fcdc15575a4828aa746a724c55599018ce1e33d366b8d302799d7
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/initial-stable-source/merge_carnitine_hydrochloride.py
    sha256: cc83d006402bf44db0ea6311f5b341b53e7c8fb8b7bbd35d71cb8533f767cd1c
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/initial-stable-source/test_merge_carnitine_hydrochloride.py
    sha256: 3c224ec2438b2011500ef837fd17c6f1ac54ba57367190dbc9803c0de4d420d4
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/inventory.json
    sha256: 9d2b75b925039a1eedff43825affdc5cc4c926c83b68ae30c42283d4a427c0c5
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/logs/step3-writer-1036-green.json
    sha256: 851c702f37ad8fd037e6ead28ad69516837c802993e81d94ac9e9e9014f6eb77
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/logs/step3-writer-1036-green.log
    sha256: 37721f94670f1e0cff43f7021d1a9521f547c5c1940521762b3dc1f083e1deb5
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/logs/step3-writer-1036-lint.json
    sha256: 2a1c9d6a22117e66026f1eb84be2363b18964060fce8e8af1160f5f2cbcd6224
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/logs/step3-writer-1036-lint.log
    sha256: 82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/logs/step3-writer-1036-mutations.json
    sha256: 24893c944def8a60d4323058e8652251f04eb457799c4931b093017d01b14c90
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/logs/step3-writer-1036-mutations.log
    sha256: 636beadb033217e53e4fcb164954b1607037b19fabafebfc6b086def23b3b89a
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/logs/step3-writer-1036-red.json
    sha256: 4308f843ef99d379dda769cd19d00fb3bf843d6ccfa25407757213ab0cb57f50
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/logs/step3-writer-1036-red.log
    sha256: 59eb57fc522e713f2d0e4067ae30ccd195709ad09b91a0b93815d1f12624eff4
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/logs/step3-writer-completed-receipt-probe.json
    sha256: cd3b3808dd44c55de660608afa9bfe3da8fb054c63ef687098a561f284cd9f2a
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/logs/step3-writer-completed-receipt-probe.log
    sha256: d10d06cc776fcdc15575a4828aa746a724c55599018ce1e33d366b8d302799d7
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/logs/step3-writer-exact-stable-green.json
    sha256: 762a1202af17c2214878e739514880e1abb913e0863d77c1663a4d92b6cba480
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/logs/step3-writer-exact-stable-green.log
    sha256: 096c52c21c386a94d129276cfa954fdcdad30ebd38cd013324329e93b74fc116
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/logs/step3-writer-focused-final.json
    sha256: 2009420c7e0b737ebadd17b2e0f3ef975428ae019c754f25f66941e006a0f9ee
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/logs/step3-writer-focused-final.log
    sha256: 996157ac81d6e9634b2921884e6d9a20ab754af4339ce5ba54d45a80e695542e
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/logs/step3-writer-focused-initial.json
    sha256: dc025de7b08c21c2d5afbeb8c2355e1f0cfb4bac42bb69dbd5e94aacda199de8
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/logs/step3-writer-focused-initial.log
    sha256: 330b3e2b8ed8c91cb1beb5734eb95b59ec3401b7f4b3bc7cd6a6ede3fc04a235
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/logs/step3-writer-focused-v2.json
    sha256: cfd4881590ebb5c410f5052089ac4a5147058f14d23d2941d7611d53b85f6b25
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/logs/step3-writer-focused-v2.log
    sha256: 18f516fb8bb7751461aa23cf4bebd02ab309e49c7d4ce4cee4c7a3d2f012a579
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/logs/step3-writer-lint-final.json
    sha256: 49354faee8b7dc63ff199cdcaf3df4a4dfadbf0967a1b0ec9f295abc8bed79c3
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/logs/step3-writer-lint-final.log
    sha256: 82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/logs/step3-writer-lint.json
    sha256: e89bf6ff441c43bc7ac8ab5308a245418f8b4e8aeb0284ee91751c02a0ce3a31
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/logs/step3-writer-lint.log
    sha256: f56581021b0e835a0c4725bd16722fbbde418d4a0934af21a59bbea74f90c746
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/logs/step3-writer-mutations.json
    sha256: aeab4fd29f552aad6edb5c5a67239faf38d618915779e54aa72883f7082e9f84
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/logs/step3-writer-mutations.log
    sha256: 215705713d9ab720eef5f65be2d8f94e3f3b191546d69b0c0ee8334400b40aa1
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/mutation-results.json
    sha256: e9b10b5a46e20155cc70949e57a6eef521f27c11cffc2304cf8d858704d633a0
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/mutations/amide_ledger_rejection_omitted.json
    sha256: 99b1a1df59e97962bf7c08f2508ab8f95875ba0f1d00e76ba97bd83db96895eb
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/mutations/amide_ledger_rejection_omitted.log
    sha256: bdf9fb2cde046f627c7f854702b94c7cbca3e189e1d2888512ddd70b98e262b2
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/mutations/callback_removed.json
    sha256: 1a062bd108dd4c92ce290f357ac7aa71c4f608461174b544ab33886de12b8a37
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/mutations/callback_removed.log
    sha256: 6e9d7c8eec6ec19ddb2010fbbb0ced2862902cd1515168623c7f14214967a348
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/mutations/candidate_claim_checks_removed.json
    sha256: 21655d67125bab49d9296657417f52c32552587a082a23ad0456650fc2308f6e
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/mutations/candidate_claim_checks_removed.log
    sha256: 396771b6a07066d10c75380b4f4f5bf931b0cc65d5d4a90ab5c5a6fe907d0a12
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/mutations/completed_anchor_check_removed.json
    sha256: 1c5c1691e93f925981250b9149baf036bbe9eb3fba0d26708593cfbe7051153a
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/mutations/completed_anchor_check_removed.log
    sha256: 2ac1d49d7bc28de1c4a81945e5a0d9f43141464a9f7ddc377f6f4f09d09adc12
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/mutations/free_chemistry_retained.json
    sha256: e72d665577835a654120286ca4b074535de609c60112e0043504873fb13253df
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/mutations/free_chemistry_retained.log
    sha256: 6463fe3b7678a20905bf6a2dc239f12f8f091a49b8aff3185f3a5fb4abc03a52
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/mutations/history_erased.json
    sha256: e8dc243aa0833ca0776472b743b68ab05bc7ca80099d931111c88eb64c42b3ad
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/mutations/history_erased.log
    sha256: 0731a37daa14d24bdb8e87642c15c8216580c7291939636f3f02b5cf5cfdc324
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/mutations/membership_migration_omitted.json
    sha256: d48218687e01d2a7d8f957ed1837e85680a96bcadb851a14d472298da3257716
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/mutations/membership_migration_omitted.log
    sha256: f4b751b75297217ada3300ac2be0210406cebf693bcdb05cb9905937f749fb2a
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/mutations/reservation_rechecks_removed.json
    sha256: 9337b81f857730fbc14ab30a25e8dcd5ed2ec9334a85399636faecc4e0c9940f
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/mutations/reservation_rechecks_removed.log
    sha256: 3fc83819ec45b5c62fe713628023b2e3082669454a4c6a92ce40ab937939c2ac
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/probe_completed_receipt_binding.py
    sha256: 27961555a82cb416dec1533b6cc95d112298cd988b93872e5623f95f230983ec
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/production-preservation-before-review.json
    sha256: 1f807747961c4d3c2e57cdc768e030e9dca290c849ebdf5de269d434fc79a27e
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/receipt-binding-issue.md
    sha256: 43680ed5bdac01db2f5565e5f1f90d027577b08e4b8f61ed8412946f7eb97447
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1036/merge_carnitine_hydrochloride.py
    sha256: 2598d9390087071fcff2a188bd4d4312a935576b8ae4fa15a9239dede7529158
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1036/mutation-results.json
    sha256: b9784e070e97f14dd25b063a5253287b266ec7fef970f35205a719be848573b7
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1036/mutations/amide_ledger_rejection_omitted.json
    sha256: a2409486651df6e00e11a0334916c8a89fbf093251f80e975479c2472fcac78a
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1036/mutations/amide_ledger_rejection_omitted.log
    sha256: 051878834ec9b530a1fd17e10c3bb83a6b8c2c784bf6c31c0abbf72c62275615
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1036/mutations/callback_removed.json
    sha256: cfab4300420e6b4131d395c0528958be80a28b3a97a962d640b07d6eddce4d6d
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1036/mutations/callback_removed.log
    sha256: 1c755fed902bb279eb8d10d6d651e260beb16ba941ebf72e58d443fbee808d02
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1036/mutations/candidate_claim_checks_removed.json
    sha256: e49704a3c3b18b9b58c79af19ec807ea96e2bd3e865f871c88e801d19d55cfc8
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1036/mutations/candidate_claim_checks_removed.log
    sha256: 7618256a86ba02e2ca64d3fe36ac655f38948bc7908eb45651028f12397d28ac
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1036/mutations/completed_anchor_check_removed.json
    sha256: fa1b94df512b68c4f482391f53371687ccacf10e0293c020623c3d4b3b78298a
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1036/mutations/completed_anchor_check_removed.log
    sha256: 5e334059155c7fc435571afd2ed3e9df604b08c6185bb4929b81e9633a8bea1f
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1036/mutations/completed_receipt_binding_removed.json
    sha256: 3e1cdbe3ac91004be17d2c8f95bf3a57d06f6c4176d0d167c385cc3c1c50dde1
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1036/mutations/completed_receipt_binding_removed.log
    sha256: 90da81f1e6841c23a89263781299e9c99a4a91101638a2df579867788aaa219a
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1036/mutations/free_chemistry_retained.json
    sha256: 88ac7a524e0adbee299857bc6d08ac7847a756977a6c654db627fd7582b48d1b
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1036/mutations/free_chemistry_retained.log
    sha256: a21da71bc121d135fc7a41d6aadec2f788f0f3b30bc28ad5d405e952ee7da354
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1036/mutations/history_erased.json
    sha256: 544ecd383ea6d1c68b3bf733325df20c4346b6efc90754349c09ebac84522502
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1036/mutations/history_erased.log
    sha256: 01b25affdbb5da53461f655e4a3766f847a7a9760fecd55b6b822da56494e1bf
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1036/mutations/membership_migration_omitted.json
    sha256: 308d6b800285ee0928940f527ed44bc2f1c5bc2afbec6bdc102a71ab6f953ccb
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1036/mutations/membership_migration_omitted.log
    sha256: 992aa7785f6e9f638bde53594fbbdaf31522f9472ed9e20467359e3e5a871938
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1036/mutations/reservation_rechecks_removed.json
    sha256: 8f8a57453ba5882bd9087419d7b227adb2d1cb61486da23e4be5db51f392c983
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1036/mutations/reservation_rechecks_removed.log
    sha256: d17536e0cb6f5cdc9fce9ed340aab4ebf8f64314101883c41888ea6a828cd97c
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1036/production-preservation.json
    sha256: 565c4e5978e3239fe4b6d60060ca26736aeecc3b5ea2895d09522f1d877fc22b
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1036/run_mutations.py
    sha256: eccf16970d569a8a99893640cff6985ff35c63121563ca0579f4d355c3b5f856
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1036/stable-source.json
    sha256: 52d6678a8b7868ae11c904193fdc99d46cb704fa596b276d9e6fd5822fb0d804
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1036/test_merge_carnitine_hydrochloride.py
    sha256: 75c18a469d6056972ee5a60ec3d46d2c219c7980111c85af7bc42b663df20a60
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1038/README.md
    sha256: fded5ad8b0d81386884ba222cc9a68c96efba7a570923fe8d80e524bf7dbe613
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1038/actual-candidate-replay.json
    sha256: cf7972f7925a3c89f5d4043b00d02ef5eaa7d762eb025f56ed4090d5f20502fb
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1038/inventory.json
    sha256: caf5004846b8e6b3617a0cda8ff5d79524ce29a4f8db125cf9949899000a2b34
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1038/logs/step3-writer-1038-actual-candidate.json
    sha256: cc7b78309d26bef424829d63a3010c63ad8688e0ca951677b5310daeeb3c951a
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1038/logs/step3-writer-1038-actual-candidate.log
    sha256: b0079b0880c22eefb3fc113891b666cd7133c16a3711bea1bb1b129c3050c737
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1038/logs/step3-writer-1038-green.json
    sha256: 086455e5d6541138e8cc66a22b32e91fbb03a3b921d94d82956da2e3fbe585e7
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1038/logs/step3-writer-1038-green.log
    sha256: e345e12aa550c72fab341661b6e97b0a6ece61e0f06e86fb844fbb3c625a6eb3
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1038/logs/step3-writer-1038-lint.json
    sha256: 06d1afd82c71b74d2744797e2c033dd9fb2920d8526483dcc52042ae17c49248
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1038/logs/step3-writer-1038-lint.log
    sha256: 82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1038/logs/step3-writer-1038-merged-native.json
    sha256: 495c1401824fb55060da74d900ecd614ca9ce563e90a12a3767adb76513d7508
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1038/logs/step3-writer-1038-merged-native.log
    sha256: 3d747809c04fb8c75bddaff7e2d6d50a34dd3b55a23bb217d7865b02e53185c5
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1038/logs/step3-writer-1038-mutations.json
    sha256: 794e7e9c81f8b41b5f2c40db8ee263db9b448eda05aa99e93ae4f8bc39d46266
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1038/logs/step3-writer-1038-mutations.log
    sha256: 099791572823b6b267bf25cf91d2eeed89b537d2d11fb6e868bf91f910a77fde
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1038/logs/step3-writer-1038-red.json
    sha256: 0abdda975837ad8db93c632ae68b3b10a5ea50bc1582a77c9a6326e2501fe677
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1038/logs/step3-writer-1038-red.log
    sha256: cf5a28c6a2f4d081b0a370d0e0fabfdd4ce1a2dd3b7941666b01e0c7a0f4e6e0
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1038/merge_carnitine_hydrochloride.py
    sha256: 2ec6a4afdd97d580e36471467fa884fe87caa6a76f0a3f7fa9756d00b1fc720e
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1038/mutation-results.json
    sha256: e5be9c23dc91785900eb741eda1747693814fbad9854063ff036393646a38513
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1038/mutations/accept_arbitrary_nldm_stamp.json
    sha256: 7ecd02e6863a0bdb1f8c29b76019e3b78a3bd77981f054ca52ae32da643bdca3
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1038/mutations/accept_arbitrary_nldm_stamp.log
    sha256: 29f509d218cabdb2906c91f3f976e6813b22314f1f9da5fae912c06db4c42c8d
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1038/mutations/amide_ledger_rejection_omitted.json
    sha256: 6503ef3f074a7acdea57c5b51314e2bd6f2fe549f481457de4b4f87938e09a03
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1038/mutations/amide_ledger_rejection_omitted.log
    sha256: 59422fb9ff191a21dc9b93ef7b6873687ae98bd18e020ef1779d026f67999e1e
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1038/mutations/blank_nldm_stamp_regression.json
    sha256: 378d2d109f24fea86bda5ff1d44259abf3712ab645a3c86a4656dd716c79f008
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1038/mutations/blank_nldm_stamp_regression.log
    sha256: f010bef58c05f672335cc71f4c0f05cbf953dd83004180bed62d5812302cea23
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1038/mutations/callback_removed.json
    sha256: e10878c9b55601e6f9cfefe2c2fbae06f41e33f0209c00fd38bcff72c94365e6
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1038/mutations/callback_removed.log
    sha256: 12274aeb9aecbf912f4172f2bb534e72a54c14da0dffa56fcc62cff84c0ab2fa
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1038/mutations/candidate_claim_checks_removed.json
    sha256: 48649dfb5f5b085795fed49b8529912e123987bd9f8aa43bbebc7f6498a2b41b
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1038/mutations/candidate_claim_checks_removed.log
    sha256: 54534a98e20e25ae8f2e60d2b798d6082f9bda745966ffa5c14fa1fbefde584d
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1038/mutations/completed_anchor_check_removed.json
    sha256: d8d4e3055ca1dabce5f88a0544aac8ba0a616852e426c21375198443f5b45e2f
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1038/mutations/completed_anchor_check_removed.log
    sha256: 54845e388887874adce9e6d7e8c5afbab4b224f37a9c17330403fb00aef8377d
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1038/mutations/completed_receipt_binding_removed.json
    sha256: 2184251b009524ed69b37ff750077107163e80e93d8abcfea054dffb665aa59c
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1038/mutations/completed_receipt_binding_removed.log
    sha256: dcf2dafe072e384c58cc9e3f94dded8bb277ce92e12a291b00f700da1c73cb7c
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1038/mutations/free_chemistry_retained.json
    sha256: 0676bc9bc83b1f633de2db69566e013afdfa135932101247de3cfd0207d244fc
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1038/mutations/free_chemistry_retained.log
    sha256: 3aff77fbd9c40bb0fb6c1b9320f8c01e00ddf7fb61bbdce68c78f8bd315c182e
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1038/mutations/history_erased.json
    sha256: e691aa9991d01f6550a367f3fb14507a4da7418a0e2d8914f976295f7077753d
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1038/mutations/history_erased.log
    sha256: 2c5a19421680844e3f5ccf6eb84dc2d0a060d1cc40022fb697b5d5b5a41209bd
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1038/mutations/membership_migration_omitted.json
    sha256: 87966ee683790e17bd01a7ce75cd78529d14a1961d6e7cf7c14dc5a81830c086
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1038/mutations/membership_migration_omitted.log
    sha256: cda6c52c224774077ddec2edc76e9645b03a14d46ff9c87626d8e23c3f5f85e5
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1038/mutations/reservation_rechecks_removed.json
    sha256: 7b0bb8e0819964a6749455ba3f43226024f94cc5622a649565e48c020e868fe4
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1038/mutations/reservation_rechecks_removed.log
    sha256: f152d1f2baae740970e2d1f62f0b0b773237934a4c11b9b71332ea886e39f7f2
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1038/prior-stamp-finding.md
    sha256: ca80c92fc337f6e90c23e184f64311bf457d67061048ebca23d4d1b5517e4de5
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1038/run_mutations.py
    sha256: 41a6524ea64d5f5a9a439622bb59942a63ea9e8ec83fa5a9cd1e96b43b90e3d8
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1038/stable-source.json
    sha256: 3213693b097811bedfeee718df19e0c6267f9b438446a8029264402c6cff9873
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1038/test_merge_carnitine_hydrochloride.py
    sha256: 5d3296736e0549371680c5f3847d639015769f766384ac0147d1e3c840e12d34
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/revision-1038/verify_actual_candidate.py
    sha256: d26e1da56528e8b9c7061d5e7b8574e5202280446ca5cc3ec1533ab5d887e37f
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/run_mutations.py
    sha256: a65510b5c5f6cda502eb61beeb2ab1f77d673541fee5faf2b04a158d086de9aa
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/implementation/writer/stable-source.json
    sha256: 459a0c6f27736c9faa2c2e969c178e5003ce889c4edafc8640fdc67f6ebf44a6
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/sources/approved-decision.md
    sha256: aee19d779a2980d1b2f9cb65eae352c3519ddd76d177db46db82186721342805
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/sources/chebi-48601-primary.json
    sha256: b2ccf5a651f0b3aa875440c5caee4c03eeb78e02e82b344a3278b6b4f935d6cd
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/sources/chebi-48601-primary.json.receipt.json
    sha256: a37c32754843862073e8833c9278d11ea26af4f5c505ce4119934af586f04c2f
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/sources/compound_cas_corrections.tsv
    sha256: 10147dabecb0da6c50ca35445faafc514719a7cd3e25bf7b7bebe3c4b8685b27
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/sources/manifest.json
    sha256: d5bf100092c4a16d29552e79475b1a8a8891a797c046377365a46f0fb85ce911
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/sources/ncit-c216679.json
    sha256: 3c2bbdefd80f43e183e5710bc34afcd24d4af9769cbbd966b8387b90d72a7db0
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/sources/ncit-c216679.json.receipt.json
    sha256: 724418e5f5fab7a63ea9cc61df436580eca791bd79659461a0aefb9a432d7927
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/sources/pubchem-288-properties.json
    sha256: 37e10b81d61f327bad86e2367d8d5f2b2d053f2f841941c3159814fff53570f0
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/sources/pubchem-288-properties.json.receipt.json
    sha256: 2541b0bfd1eb44bd17a4b16f2c74c4326bb5ab920f350828ff56a2b116c05b27
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/sources/pubchem-5970-properties.json
    sha256: deccda58718bdec8e08efcd641918524dd5c8ed5cc05bfb7fbc3c1ccbec2064c
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/sources/pubchem-5970-properties.json.receipt.json
    sha256: 2a865a973b9d6550e9f14e12b4ec61c34c7cb621dd474a053346768de31d0c79
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/sources/pubchem-5970-synonyms.json
    sha256: 6687dc9bf22813e53e3db3bf8d41cfb17ebf347ff3632aed9e86fbc6251b4e80
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/sources/pubchem-5970-synonyms.json.receipt.json
    sha256: defac89b19c1d3038632c59630b3f6210231b2e1d3d1810326c5631ad11b9b12
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/sources/pubchem-cas-461-05-2.json
    sha256: d7760ddfaff2de1febd179fbb96b0e384920cbf78ab910bec3e722059cb649df
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/sources/pubchem-cas-461-05-2.json.receipt.json
    sha256: 2f8a49420d0b8edc0387d06c4d59cce2534f47ead20101a3ca3a0c6ceecf81e0
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/sources/pubchem-cas-461-06-3.json
    sha256: b9a1509861112a8e100a7edf2a83a14e1dfc9f3d6d2ab93c1e959a105773c4ea
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/sources/pubchem-cas-461-06-3.json.receipt.json
    sha256: a05518f1a84e4b7e36290aae5e68da1c2ad9f6fdef16316306a1613fb45651ae
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/sources/routing-decision.md
    sha256: e2d6f4a0ffde1ca0f8291aacc2b2b7759b31ef30d8df438b0d1efd14e638072e
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/sources/selected-source-rows.json
    sha256: 7c36a19ccd5562abf7ef533df5251a35cfeaf23dbbd2ef78fe5d733093b2f50c
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/sources/sigma-c9500-facts.json
    sha256: 28efc0cdd5b8538d4f51730b4344ac20829b8903eb8ef42c2b6216e4c08293b6
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/README.md
    sha256: e55bc81df9c61b2480553d6eabb61e55bab3f7280aaa1e5a59740c6f921a1cce
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/logs/step3-chain-final-v1-curies-and-product-labels.json
    sha256: 12381c190b6f6c4016472f5d33e8df294bf9d1007c343eb42abae482bc97c7a1
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/logs/step3-chain-final-v1-curies-and-product-labels.log
    sha256: 1ad08700968fa56c138dd1f7cf3f569f1acdde85e12b052efb473c747e41e304
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/logs/step3-chain-final-v1-full-qc.json
    sha256: 9750eb2d50f53d8a715d791191b5652f75bf8b0ee542301b1ca19df9adf9741c
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/logs/step3-chain-final-v1-full-qc.log
    sha256: 92e058e306c36b6389421f76a66ff26ea2e094819ee25c95e8cca287330e2c02
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/logs/step3-chain-final-v1-full-suite.json
    sha256: 1c20adbac11f34a61b1f9c29861e91b3dab9951904b9858b98567df87349fc47
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/logs/step3-chain-final-v1-full-suite.log
    sha256: a0e5e336ef8bdab510a284f7055cb2b3b63ab4810c83f8d1042742ed2c67846a
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/logs/step3-chain-final-v1-receipt-regression-tests.json
    sha256: f682f221fbcf704c8e60698515f49db64e891e42b51374a122976aae892b0239
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/logs/step3-chain-final-v1-receipt-regression-tests.log
    sha256: 03da613e6b96eca933559d8dadf27bd4a0139bb499d47c99d1ae807d4002e3b7
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/logs/step3-chain-final-v1-unified-gates.json
    sha256: 895a291b7a306e41daf901b3ce1daa4ed8b245b5537714bbaefb263fc8a62f52
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/logs/step3-chain-final-v1-unified-gates.log
    sha256: 1b460ced48db7f99a526afe938bf8a09e84af240ffda8ebb7ff5ecac67f7b10a
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/logs/step3-independent-1039-parser-proof.json
    sha256: d8dcbc49a901d82dbaed2045fec4a773bb2d1170ab5a9e36d8401f8de56bc974
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/logs/step3-independent-1039-parser-proof.log
    sha256: 787524f2b14ec4e9d8fe6f09ba21986b1897c657ab6db041869dbce6333ee453
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/logs/step3-independent-1039-regressions.json
    sha256: f720d0a0261619e1f663fc2d07f749097703d8b16b4f1011e628c483a151974e
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/logs/step3-independent-1039-regressions.log
    sha256: b6c43919df176dfdd25a61c9ed422ab132a8b2bf019b11f28633403cda5923d7
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/logs/step3-independent-final-products-v2.json
    sha256: 7d36dfbc05e7d84b0a9a15c18393e58d873b463613325a981670c7dde63ce27a
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/logs/step3-independent-final-products-v2.log
    sha256: b06ad48b29f782d2d95103a430199b41157ffdf5a0d7de43da9843f5ccbb033f
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/logs/step3-independent-final-products-v3.json
    sha256: 615ba33b51a4c088933810918503a01b9c4d997422086d053e1f6a54ee7a59fc
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/logs/step3-independent-final-products-v3.log
    sha256: 3a1449dd4935432c32ebae6346005b9a93badb065953019fc02cac391e9c8545
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/logs/step3-independent-final-products.json
    sha256: 0dbe8b8d33831f89bcf845a500881598b71eab321195489314f63cbad398be32
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/logs/step3-independent-final-products.log
    sha256: 68b25da922ee0901a396f4131d62ee11bfea42d7ccabfb0bf036058cfa3f2c2e
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/step3-mim-independent/final-state/1039-parser-proof.json
    sha256: 787524f2b14ec4e9d8fe6f09ba21986b1897c657ab6db041869dbce6333ee453
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/step3-mim-independent/final-state/audit_products.py
    sha256: d62efe2d3b67df2bf0d96c0d263767c5f6cd2f8220dde1106bd5994303b7aad9
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/step3-mim-independent/final-state/audit_products_v2.py
    sha256: ebdd9c4601d058265842f2f8af6dc604abd58e3f64aef44927b3434fa5a42a62
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/step3-mim-independent/final-state/audit_products_v3.py
    sha256: e9bcfe37c0a31762d237f0e96fceef53b524d282aa8a2862f8911ff3bc359eec
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/step3-mim-independent/final-state/freeze_checkpoint.py
    sha256: 5bfcd72733f74316144f4f6e6f9fc495948d3d4ddb24eca85deb0b8e33cd2986
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/step3-mim-independent/final-state/inventory.json
    sha256: 5cc82ccffd89de7aee6d5b15c1bdf683e575dc6adabbc6a989f210e12057a8c6
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/step3-mim-independent/final-state/package-independent/arbitrary-selector-refused.json
    sha256: 67f1f05221f27c94d393392e13616f4db1e00103ef2329165b6c8c44bc779f0b
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/step3-mim-independent/final-state/package-independent/arbitrary-selector-refused.log
    sha256: cd91eca965d5e104eae8b89cfa4d0208a5e5d6f900118b8ef481256beafdddc8
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/step3-mim-independent/final-state/package-independent/audit.py
    sha256: 5580e1e2cf2b25e021d9ae7fb294ec10c744dd0c3dd32599ccb959f74d2802dc
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/step3-mim-independent/final-state/package-independent/audit_v2.py
    sha256: 15837bbc221582b46e4abd4678609e07ea1fab757c0058d23b50cebb0cfe407b
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/step3-mim-independent/final-state/package-independent/copied-baseline.json
    sha256: c376579c40b94b1740fd97729cf3d33d275b1a293ccb0a87d0d01b9a97c0137b
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/step3-mim-independent/final-state/package-independent/copied-baseline.log
    sha256: 50818d9c036d22eb31372c1fd0a02b263dff465d138c46fa7e4555f0b03c17cb
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/step3-mim-independent/final-state/package-independent/current-native-verifier.json
    sha256: b9a5acc08335ee6a906406bef78a03d5f1b759af3970cae5e38a746ff618201c
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/step3-mim-independent/final-state/package-independent/current-native-verifier.log
    sha256: 50818d9c036d22eb31372c1fd0a02b263dff465d138c46fa7e4555f0b03c17cb
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/step3-mim-independent/final-state/package-independent/inventory.json
    sha256: 3d13930a7c6f79914a83f368db1a645090a29de3107036f1a047d247c0f34679
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/step3-mim-independent/final-state/package-independent/protected-evidence-refused.json
    sha256: e0506ddcd256b7318a7d3524cc1eaa8df63c92285cb1082b37a7297dc16ae448
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/step3-mim-independent/final-state/package-independent/protected-evidence-refused.log
    sha256: 7fbe36096c8befdd0d483f9e61e3798f2021b228f89beca4587fa0f6b39ab43c
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/step3-mim-independent/final-state/package-independent/receipt.json
    sha256: 20f6648c2f21b9f5617ba610708e4a6f77ec9c1d61466c4a90ab0b0f319f0522
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/step3-mim-independent/final-state/package-independent/review.md
    sha256: f9d053987b45632a1e025202c47783f0739d016ba0a0f9984c19ea5f4ee3f748
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/step3-mim-independent/final-state/probe_1039.py
    sha256: 5ecd2eaa551f73e55812c8ff5999fbe4f32f5d401030c345919c1aea3c296add
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/step3-mim-independent/final-state/product-audit.json
    sha256: 3a1449dd4935432c32ebae6346005b9a93badb065953019fc02cac391e9c8545
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/step3-mim-independent/final-state/receipt.json
    sha256: b341fb6756c76b2d83e1f0872f55caa5330a7a6b1ef4526c7d0181786e4bac3c
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/step3-mim-independent/final-state/review.md
    sha256: cc4b0f4579f27196d8ae36e0aeb5dbee7a46b6ca13cb44b9b687c52abab57a20
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/step3-native-chain-plan/executions/step3-chain-final-v1-gates/commands.jsonl
    sha256: b289d73762185bcd56485fa5841ac99e464b3d024e504cdcea545b34bc4e8d01
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/step3-native-chain-plan/executions/step3-chain-final-v1-gates/complete.json
    sha256: 3390063330b938e8441305e54459d681ff9597116f75cfb5063df3e1e467c99d
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/step3-native-chain-plan/executions/step3-chain-final-v1-gates/start.json
    sha256: ba37c434b75e8cfa7f75ddf501f1fe18dbb0e3e20ea8fef08701f36cbae73be9
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/step3-native-chain-plan/executions/step3-chain-final-v1-gates/verified-output.json
    sha256: 3fb11b27841976ce0c23bc9ee64b7e1be15075c2183d3f8d2ac86a1653f06d41
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/manifest.json
    sha256: a3a53d77405eecddcc3f7fb58a168fed56989f5fa7b68f55aadb710fb497eb7b
    role: context
  - path: reports/carnitine_hydrochloride_1004_20261101/validation/summary.json
    sha256: 26066fb525cd8526c0593ca7189704c91e98efeb8234146b44ea6ace13d70db0
    role: context
  - path: reports/ingredient_bundle_20260924/claims.json
    sha256: 52c5c0e9938725524ed9680c736e1015b74dba1c603c2b76da62b7cc17175a8b
    role: context
  - path: reports/ingredient_bundle_20260924/review-evidence.json
    sha256: 34e8e6575bb4e80fd09234661a0c6a8db0c061d449b9529bb9dd74aad4a4e6d1
    role: context
  - path: reports/ingredient_bundle_20260924/scope-rulings.json
    sha256: 3ae5d5a6a5b82ab6890a110c154cf602701282f25ee18f9a1f0f609869106555
    role: context
  - path: reports/ingredient_bundle_20261101_carnitine1004/README.md
    sha256: 801b608279b6c4c4abbd6db3aecd8bc7e16aeb4b019e029a060e436f4a7a48f1
    role: context
  - path: reports/ingredient_bundle_20261101_carnitine1004/dependency-refresh.json
    sha256: a431e7347efd4f4ec3823b723edb4099318c4b7c41e287e0b8bcec8ca08cc059
    role: context
  - path: reports/ingredient_bundle_20261101_carnitine1004/prior-review.json
    sha256: 7ea74db32bcc33b464a39101e9d81319729dcc73ffd2eba997fa8c99cfb735f5
    role: context
  - path: reports/ingredient_bundle_20261101_carnitine1004/review.json
    sha256: 1d208eef5d6a250a37df4928d21aea477bec96ddb7cf7ebdacce1e370dcbed4c
    role: target
  - path: reports/ingredient_bundle_20261101_ncit875/review.json
    sha256: 7ea74db32bcc33b464a39101e9d81319729dcc73ffd2eba997fa8c99cfb735f5
    role: context
  - path: reports/semantic_review_20260921/resolution/assertion-dispositions.tsv
    sha256: 7872a46d7cec8fb21d6b024922107092d61240f23341b41c0c972f4fb5ae3a04
    role: target
  - path: reports/semantic_review_20260921/resolution/build_review.py
    sha256: 84a955e55929c5ae8dc6df6e813aaddd13dc4dfd38d81bc63a8172067c00fd59
    role: context
  - path: reports/semantic_review_20260921/resolution/current-review.json
    sha256: d829ff771598ddd4bdf09b931ddeea820eaf868a2dc2ed616bf8a5cb7d482900
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: 05c2447e61c246cc81afe34c86c131ace37c835f8a01d01fe9f7d52ec09a360d
    role: context
  - path: reports/sssom_completion_20260921/README.md
    sha256: fc172e43dcbb8c3876db6cf587e896ac3984ba246b9209400a8ffa997cc1e2f4
    role: context
  - path: reports/sssom_completion_20260921/assemble_review.py
    sha256: e4deb1708ba7dc46ebeb7f6b35dcf685f4d2c7e0758597377329aa1d1b0fad87
    role: context
  - path: reports/sssom_completion_20260921/mapping-evidence.json
    sha256: d1bcc536c7520fd4f9fb43f0a885a705df4d6bfb50d091122636c8ae5687846d
    role: context
  - path: reports/sssom_completion_20260921/mapping_changes/chemical-scopes-20260923.json
    sha256: a31d5bae53211a7cdc008008b4eb8dd49d9e2ec3a62773c912dbdab8d0d0b7ae
    role: context
  - path: reports/sssom_completion_20260921/mapping_changes/claw571-hydrate-parent-identities.json
    sha256: 2eeb7e2b9da164403cc715e6cc1b3a8c36f6f35d173bc1d740f8b90f7ce3d762
    role: context
  - path: reports/sssom_completion_20260921/mapping_changes/data-license-20261001.json
    sha256: 6d89e96b3560bb2b237fc9a358b1ef68986f1361dc536a4e5872661aaf459403
    role: context
  - path: reports/sssom_completion_20260921/mapping_changes/ingredient-identities-20260924.json
    sha256: 1cf4c94c4ff4704c642297aafbc48d05b1978fcd67cbe88ff076e4def9c4be5b
    role: context
  - path: reports/sssom_completion_20260921/mapping_changes/issue1004-carnitine-hydrochloride-merge.json
    sha256: e14ab50d5b981f2e003d755644ffcb98c901519fc0e8324658900ada1ae12e1c
    role: context
  - path: reports/sssom_completion_20260921/mapping_changes/issue1014-provenance-restoration.json
    sha256: fbeec3fbfee71be85541353683df135f96dc1d0021c6bfb3877bcc5eca8813d0
    role: context
  - path: reports/sssom_completion_20260921/mapping_changes/issue232-wrong-form-names.json
    sha256: a94aab0d6d9e5cbf6fec1c6d3829981630bd2c40434b868a8d20526f4a7db985
    role: context
  - path: reports/sssom_completion_20260921/mapping_changes/issue312-batch1.json
    sha256: 0554d4d32924eec4c9909d3c0ff36c8dd9d44ce426011ba42f0122d9172a41a0
    role: context
  - path: reports/sssom_completion_20260921/mapping_changes/issue312-batch2.json
    sha256: c10ef0d7f577190f0d97a95c0482011d6abfaaf03fba2c509f98eec66694c373
    role: context
  - path: reports/sssom_completion_20260921/mapping_changes/issue312-batch3.json
    sha256: aff24cdc08d1cb979795ffad227c03e9622733438ec7f94c5669ea05da6bfe88
    role: context
  - path: reports/sssom_completion_20260921/mapping_changes/issue312-batch4.json
    sha256: 2779f46e8ff8a2d0429fa382ce67dec6f7b2b43b02be3c316c5a7bdcf2138409
    role: context
  - path: reports/sssom_completion_20260921/mapping_changes/issue669-1003-scoped-alias-corrections.json
    sha256: 00049aa1d2b19565020d4ecbec999fc723d2cf5954968ec6bf5cebdc0da73f34
    role: context
  - path: reports/sssom_completion_20260921/mapping_changes/issue669-704-rulings.json
    sha256: 0870e436e4f03a1ef2377a957fedab70b42d201b6f9b8935478c40ac647c90d8
    role: context
  - path: reports/sssom_completion_20260921/mapping_changes/issue759-micro-source.json
    sha256: 75008d33a173155a6bdccafb64bbee96b0a457f9da5b761bd7ee2aa9b74100aa
    role: context
  - path: reports/sssom_completion_20260921/mapping_changes/issue875-ncit-exact-heptahydrate.json
    sha256: 28bd529e14104cfbf9160e9532b3d859dbe6259dbac00a9d877bac1daec8a2b8
    role: context
  - path: reports/sssom_completion_20260921/mapping_changes/issue878-hydrate-contradictions.json
    sha256: cdd362a5f2d34ebf6676a098869995ce41a8059285cbffc2f92bbc3e49c86ec3
    role: context
  - path: reports/sssom_completion_20260921/mapping_changes/make_receipt.py
    sha256: 2d007139f3cea26df86217807c263fd3580771034719fb1fd79361d884b5a121
    role: context
  - path: reports/sssom_completion_20260921/mapping_changes/review-record-issues-20261003.json
    sha256: 9b578f6c25c1ebabb8e58c5a59d6188b7c1f2dd3c8c70ed021b35144c6da1226
    role: context
  - path: reports/sssom_completion_20260921/mapping_review/chemical-scope-ontology-evidence.json
    sha256: 4e3c3b691aac234d837d187100d0cea546210c3205e9a5cd78c4e43b39b4159c
    role: context
  - path: reports/sssom_completion_20260921/mapping_review/identity-review-20260924/README.md
    sha256: e4bd4d79f81294606439007d1c8d6be56c61f41b0adfdb26f727cf1264e5a157
    role: context
  - path: reports/sssom_completion_20260921/mapping_review/identity-review-20260924/bsa-recipe-occurrences.json
    sha256: 91da2d86f8359520bfb70a3ef411de9c64f068d623ded3c2c9159435d67911c7
    role: context
  - path: reports/sssom_completion_20260921/mapping_review/identity-review-20260924/fda-gsrs.json
    sha256: 157f6fee0e7131f8bee16c695650405f87b6583add87dc6f576531c8ffe38057
    role: context
  - path: reports/sssom_completion_20260921/mapping_review/identity-review-20260924/native-authorities.json
    sha256: af3b0fc5ef0200eff82694d1811b9444b56f1751a2e5b956e0edf50a78afc76e
    role: context
  - path: reports/sssom_completion_20260921/mapping_review/identity-review-20260924/source-records.json
    sha256: 93777a551761d68f52b542798c9ddbb6286f1190924944ad3a39e4e3ac1068f9
    role: context
  - path: reports/sssom_completion_20260921/mapping_review/micro-source-review.md
    sha256: e2f70e3950362dbb9fee47de191f8db1ca26eff9a3951f1021eed14c8b3fda71
    role: context
  - path: reports/sssom_completion_20260921/mapping_review/rifamycin-source-occurrences.json
    sha256: 9fb5e074cc0f093922be16555ff427fc7b59ef1a7f29f001fc20e7fd823b8cbd
    role: context
  - path: reports/sssom_completion_20260921/mapping_review/sorbitan-recipe-occurrences.json
    sha256: 4d84bfbb010966647860e5b203cc6003f9ac02f3b87951f99f3b842613bb42c6
    role: context
  - path: reports/sssom_completion_20260921/review.json
    sha256: 3614442a6b265f641598df7cd33e2c41cb9e708b2b4f4866f6990e5d87a98f81
    role: context
  - path: reviews/workflow/mech-goal-sequence-20261019/cycle-000013/stage-03/revision-0001/coverage_report.md
    sha256: 4f771f03988e940c0f926c114eb9b57c332d15b62562e1d84e08c6f31eed6104
    role: context
  - path: reviews/workflow/mech-goal-sequence-20261019/cycle-000013/stage-03/revision-0001/validation.md
    sha256: 0ad7742eae1360bf2a4ed93e5f490a28c780e04e15d28fdf240ad9075bdff81d
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/.vendored_canon_ref
    sha256: ecbdb08d2094917a5ed8147086f46579e976df869eaea3942060c552d2e2015c
    role: context
  - path: scripts/check_unified_freshness.py
    sha256: 95efa627ea1cc0e6ee2d055815f54a9e121971b1ac843d4be3453176f13d2c90
    role: context
  - path: scripts/check_unified_rejections.py
    sha256: 4f7faf1f103f50be1a59e826b0238061d1a9214afcec9d1cf0b029237e71238c
    role: context
  - path: scripts/merge_carnitine_hydrochloride.py
    sha256: 2ec6a4afdd97d580e36471467fa884fe87caa6a76f0a3f7fa9756d00b1fc720e
    role: target
  - path: scripts/promote_heptahydrate_ncit.py
    sha256: 768166cfb726e3a751b451a89bebfa30c8dea7e22f05ba085cf4fb9db96550ee
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: src/mediaingredientmech/ingredient_bundle_refresh.py
    sha256: 58193f16b7231aba75932bf7316c1bf8394709bc7cff96687accb11eb6963946
    role: context
  - path: src/mediaingredientmech/ontology_sources/micro/manifest.json
    sha256: 9e3ee88942aafbf0687bbbfc08c3e653b0ad0d104e7ea80efd07b1f0a4350feb
    role: context
  - path: src/mediaingredientmech/profiles/ingredient_bundle_v1.schema.json
    sha256: c0faabc0870bdcb3f03847f5e6597bbe4e245ccc775fc398f536c7c3f0ea4ab2
    role: context
  - path: src/mediaingredientmech/profiles/ingredient_scope_v1.yaml
    sha256: dd2f78e6b6fcbdf8a715bebcec14e0f86c1e431bf28e5b9d7f3524a62e5bce3a
    role: context
  - path: src/mediaingredientmech/schema/mediaingredientmech.yaml
    sha256: bb43dee29b21fdee72a48022456e733e49e95824c4c09674f9b3165c290fe012
    role: context
  - path: src/mediaingredientmech/utils/culturemech_occurrences.py
    sha256: d8b5b0ea02bf6c885d9627357dba04c2ba59626ca9bf12062ac70e7d6bed8c68
    role: target
  - path: tests/fixtures/issue1004-before/Carnitine_Dl_Hydrochloride.yaml
    sha256: 8a7e0ac23a72c403bf9cce38a20abe817ee83e0231b558f2ca07ed05d134d190
    role: context
  - path: tests/fixtures/issue1004-before/Carnitine_Hydrochloride.yaml
    sha256: c03c1c66b9e70436da2e841d1edf2a700f05830674c715fc265ac7fde9705722
    role: context
  - path: tests/fixtures/issue1004-before/NLDM_metabolites.yaml
    sha256: 7332021e0d760384bc0381f5e00e3a87bd4dfe4b7c5b2eb1140853f7c17d78a0
    role: context
  - path: tests/fixtures/issue1004-before/README.md
    sha256: 44579559d365e73919bd576ca9b4f6d3f97c1a6a86949b59730b4ec1495b1746
    role: context
  - path: tests/fixtures/issue1004-before/culturemech_recipe_membership.tsv.gz
    sha256: f9633b52c6550c3fdf7c454dc37836be6efe66712860ee885d58c387463b424c
    role: context
  - path: tests/fixtures/issue1004-before/ingredient_mappings.sssom.tsv.gz
    sha256: 8c09a86e5b41d2c9a585660397028352f8d9eb66458fd4e1a5568ff5e3a2ef46
    role: context
  - path: tests/fixtures/issue1004-before/manifest.json
    sha256: 7c36e370a593bb7063670e2fa44484e576d1bc25a05c1a7e5f9fa57402f33d93
    role: context
  - path: tests/fixtures/issue1004-before/other_cross_record_baseline.tsv
    sha256: 170368983e4105773348122d44da5417745e675dfa9151f72270f19da7a26008
    role: context
  - path: tests/fixtures/issue1004-before/unified_mapping_rejections.tsv
    sha256: 717289ca0e45046dcb96f6839b843838a6636fd8e120cf4d9b9ac48de3d9016d
    role: context
  - path: tests/fixtures/issue1004-routing-dependencies.json.gz
    sha256: 45e583e9168ee45124d59543dfd371d3919b359435e652e5fb948ff9557c3811
    role: context
  - path: tests/fixtures/issue1004-routing-manifest.json
    sha256: 6d999758413f6b6bb42db709c1b97a08c313cff10bbfa3a987aa15f61b1860a9
    role: context
  - path: tests/fixtures/issue1004-routing-occurrences.tsv
    sha256: e7fdbba52261189a462da2e4ada8f80f99c5b047dbb3d2627c29b545478f2c35
    role: context
  - path: tests/test_carnitine_merge_dependencies.py
    sha256: 89c37f67ef98c0e96b8c359df8138ceb579d1962bae0d7f52290219b2d9da042
    role: context
  - path: tests/test_carnitine_occurrence_routing.py
    sha256: 886042936835d7a5cd92aa566d7e8107f40047ee136aa23063891bfc5a2e3443
    role: context
  - path: tests/test_ingredient_bundle.py
    sha256: 46d6de216047393d15258d2d2cde4c97371cfd586912fa16135460ed7aebcef8
    role: context
  - path: tests/test_merge_carnitine_hydrochloride.py
    sha256: 5d3296736e0549371680c5f3847d639015769f766384ac0147d1e3c840e12d34
    role: context
scope:
  description: 'The approved #1004 exact hydrochloride identity correction, rejected
    duplicate, NLDM reference, guarded writer/router, bounded canonical/unified/membership
    products and unchanged companion dependencies.'
  selection: Twelve exact targets chosen from three changed owners and their direct
    maintained/generated dependencies; all selected targets reviewed in full at the
    declared selectors. Corpus-wide counts/byte comparisons are structural scope checks,
    not scientific approval of all records.
  coverage: full
  population_size: 12
  reviewed_target_ids:
  - MIM:Carnitine_Hydrochloride
  - MIM:Carnitine_Dl_Hydrochloride
  - MIM:NLDM_metabolites
  - step3:sssom-ncit
  - step3:sssom-nldm
  - step3:unified-salt
  - step3:guarded-writer
  - step3:finite-source-router
  - step3:rejection-pair
  - step3:membership-migration
  - step3:nldm-assertion-withdrawal
  - step3:unchanged-companion
  exclusions:
  - target: All other2952individual records and unrelated mapping/semantic claims
    reason: Verified byte or semantic-decision preservation as appropriate; not newly
      scientifically reviewed.
  - target: Complete NLDM formulation, roles and biological mechanisms
    reason: Only component59reference/history and strict whole-owner approval withdrawal
      are in scope.
  - target: Future steps, active-owner-first index policy and approval-model redesign
    reason: Not implemented or approved by this bounded migration.
  - target: Future committed head, remote CI, merge-group and publication state
    reason: This report is a truthful working-tree capture; subsequent exact-head
      checks remain mandatory.
targets:
- target_id: MIM:Carnitine_Hydrochloride
  path: data/ingredients/mapped/Carnitine_Hydrochloride.yaml
  label: Active DL-carnitine hydrochloride owner
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Carnitine_Hydrochloride.yaml
    role: maintained input
  - repository: CultureBotAI/MediaIngredientMech
    path: data/curated/mapped_ingredients.yaml
    role: synchronized collection entry
- target_id: MIM:Carnitine_Dl_Hydrochloride
  path: data/ingredients/mapped/Carnitine_Dl_Hydrochloride.yaml
  label: Rejected duplicate with corrected hydrochloride identity
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Carnitine_Dl_Hydrochloride.yaml
    role: maintained input
  - repository: CultureBotAI/MediaIngredientMech
    path: data/curated/mapped_ingredients.yaml
    role: synchronized collection entry
- target_id: MIM:NLDM_metabolites
  path: data/ingredients/mapped/NLDM_metabolites.yaml
  label: NLDM component 59 reference and inherited approval withdrawal
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/NLDM_metabolites.yaml
    role: maintained input
  - repository: CultureBotAI/MediaIngredientMech
    path: data/curated/mapped_ingredients.yaml
    role: synchronized collection entry
- target_id: step3:sssom-ncit
  path: mappings/ingredient_mappings.sssom.tsv
  label: Exact NCIT salt claim remains withheld
  kind: snapshot_row
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Carnitine_Hydrochloride.yaml
    role: maintained input
  - repository: CultureBotAI/MediaIngredientMech
    path: scripts/merge_carnitine_hydrochloride.py
    role: bounded candidate promoter
  - repository: CultureBotAI/culturebotai-claw
    path: scripts/build_mim_ingredient_sssom.py
    role: native row producer
  selector: subject_id=MIM:Carnitine_Hydrochloride; predicate_id=skos:exactMatch;
    object_id=NCIT:C216679
- target_id: step3:sssom-nldm
  path: mappings/ingredient_mappings.sssom.tsv
  label: NLDM identity row with historical validation and withdrawn approval
  kind: snapshot_row
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/NLDM_metabolites.yaml
    role: maintained input
  - repository: CultureBotAI/MediaIngredientMech
    path: scripts/merge_carnitine_hydrochloride.py
    role: bounded candidate promoter
  selector: subject_id=MIM:NLDM_metabolites; predicate_id=skos:exactMatch; object_id=kgmicrobe.ingredient:nldm_metabolites
- target_id: step3:unified-salt
  path: UNIFIED_INGREDIENT_MAPPING.tsv
  label: One changed unified salt row
  kind: snapshot_row
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Carnitine_Hydrochloride.yaml
    role: maintained input
  - repository: CultureBotAI/MediaIngredientMech
    path: mappings/unified_mapping_rejections.tsv
    role: source identity holds
  - repository: CultureBotAI/culturebotai-claw
    path: scripts/build_unified_ingredient_mapping.py
    role: native unified producer
  selector: ingredient_name=Carnitine Hydrochloride
- target_id: step3:guarded-writer
  path: scripts/merge_carnitine_hydrochloride.py
  label: Hash-bound source and canonical migration
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: scripts/merge_carnitine_hydrochloride.py
    role: maintained input
- target_id: step3:finite-source-router
  path: src/mediaingredientmech/utils/culturemech_occurrences.py
  label: Two normalized source labels route to the corrected salt
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: src/mediaingredientmech/utils/culturemech_occurrences.py
    role: maintained input
- target_id: step3:rejection-pair
  path: mappings/unified_mapping_rejections.tsv
  label: Source-bound acylcarnitine and amide rejections
  kind: snapshot_row
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: scripts/merge_carnitine_hydrochloride.py
    role: maintained input
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Carnitine_Hydrochloride.yaml
    role: maintained input
  selector: ingredient_name=Carnitine Hydrochloride; mim_id=NCIT:C216679; rejected_id
    in [CHEBI:91318,CHEBI:48601]
- target_id: step3:membership-migration
  path: mappings/culturemech_recipe_membership.tsv
  label: Fourteen preserved recipe/count pairs
  kind: snapshot_row
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Carnitine_Hydrochloride.yaml
    role: maintained input
  - repository: CultureBotAI/MediaIngredientMech
    path: src/mediaingredientmech/utils/culturemech_occurrences.py
    role: maintained input
  - repository: CultureBotAI/MediaIngredientMech
    path: scripts/merge_carnitine_hydrochloride.py
    role: maintained input
  selector: mim_identifier=NCIT:C216679; recipe_id in [CultureMech:015654,CultureMech:015655,CultureMech:015656,CultureMech:015665,CultureMech:015666,CultureMech:015667,CultureMech:015668,CultureMech:015669,CultureMech:015670,CultureMech:015671,CultureMech:015740,CultureMech:015741,CultureMech:015742,CultureMech:015749]
- target_id: step3:nldm-assertion-withdrawal
  path: reports/semantic_review_20260921/resolution/assertion-dispositions.tsv
  label: All 68 NLDM component and role approvals withdrawn
  kind: snapshot_row
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/NLDM_metabolites.yaml
    role: maintained input
  - repository: CultureBotAI/MediaIngredientMech
    path: reports/semantic_review_20260921/resolution/build_review.py
    role: native assertion disposition builder
  selector: source_record=data/ingredients/mapped/NLDM_metabolites.yaml; assertion_type
    in [component,nutritional_roles]
- target_id: step3:unchanged-companion
  path: reports/ingredient_bundle_20261101_carnitine1004/review.json
  label: 51 claims and 20 owners preserve prior explicit decisions
  kind: generated
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: reports/ingredient_bundle_20261101_ncit875/review.json
    role: immutable prior companion review
  - repository: CultureBotAI/MediaIngredientMech
    path: src/mediaingredientmech/ingredient_bundle_refresh.py
    role: native unchanged-cohort refresher
  - repository: CultureBotAI/MediaIngredientMech
    path: reports/ingredient_bundle_20260924/claims.json
    role: maintained claim cohort
checks:
- check_id: capture
  name: Actual durable source capture
  status: passed
  required: true
  summary: Actual detached HEAD99fe4b44; staged treeb3084fcb matches feature;522staged
    paths,601native input hashes and102current references match. All four frozen manifests
    and indexed files verified.
  target_ids:
  - MIM:Carnitine_Hydrochloride
  - MIM:Carnitine_Dl_Hydrochloride
  - MIM:NLDM_metabolites
  - step3:sssom-ncit
  - step3:sssom-nldm
  - step3:unified-salt
  - step3:guarded-writer
  - step3:finite-source-router
  - step3:rejection-pair
  - step3:membership-migration
  - step3:nldm-assertion-withdrawal
  - step3:unchanged-companion
  evidence_ids:
  - implementation-package
  - generation-package
  - validation-package
  - fixture-manifest
  command: python /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/approved-plan-20261101T031134Z/step3-mim-independent/native-preparation/capture-v2/prepare_capture.py
  exit_code: 0
  scope_note: Source is the actual working tree on durable main, not a manually relabeled
    feature revision. The new review pair is not one of its own inputs.
- check_id: native-tests
  name: Independent clean-capture writer and dependency tests
  status: passed
  required: true
  summary: 182passed,13warnings,0skips; includes the previously failing historical
    migration test, all132writer tests and50routing/dependency tests.
  target_ids:
  - MIM:Carnitine_Hydrochloride
  - MIM:Carnitine_Dl_Hydrochloride
  - MIM:NLDM_metabolites
  - step3:sssom-ncit
  - step3:sssom-nldm
  - step3:unified-salt
  - step3:guarded-writer
  - step3:finite-source-router
  - step3:rejection-pair
  - step3:membership-migration
  - step3:nldm-assertion-withdrawal
  - step3:unchanged-companion
  evidence_ids:
  - capture-tests
  - staging-finding
  command: python -m pytest -q -o addopts= -p no:cacheprovider tests/test_merge_carnitine_hydrochloride.py
    tests/test_carnitine_occurrence_routing.py tests/test_carnitine_merge_dependencies.py
  exit_code: 0
  scope_note: Executed independently in step3-review-capture-v2 using the maintained
    Python3.13 environment.
- check_id: source-products
  name: Independent applied source/product/withdrawal checks
  status: passed
  required: true
  summary: Source and generated deltas match exact approved scope; no unrelated record,
    mapping decision, assertion payload/approval or companion owner change.
  target_ids:
  - MIM:Carnitine_Hydrochloride
  - MIM:Carnitine_Dl_Hydrochloride
  - MIM:NLDM_metabolites
  - step3:sssom-ncit
  - step3:sssom-nldm
  - step3:unified-salt
  - step3:guarded-writer
  - step3:finite-source-router
  - step3:rejection-pair
  - step3:membership-migration
  - step3:nldm-assertion-withdrawal
  - step3:unchanged-companion
  evidence_ids:
  - source-application
  - products
  - receipt17
  command: python /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/approved-plan-20261101T031134Z/step3-mim-independent/final-state/audit_products_v3.py
  exit_code: 0
  scope_note: Earlier v1/v2 reviewer harness diagnostic mistakes are retained; v3
    is the corrected completed comparison. Actual raw TSV is parsed without stripping
    hash-prefixed names.
- check_id: adversarial
  name: Independent native boundary probes and fixed findings
  status: passed
  required: true
  summary: Previously reproduced receipt no-op, proposal/input-set races, prior-stamp
    and diagnostic-parser failures are now refused or handled by the narrowly corrected
    implementation. Historical author mutation runs remain credited to their authors.
  target_ids:
  - MIM:Carnitine_Hydrochloride
  - MIM:Carnitine_Dl_Hydrochloride
  - MIM:NLDM_metabolites
  - step3:sssom-ncit
  - step3:sssom-nldm
  - step3:unified-salt
  - step3:guarded-writer
  - step3:finite-source-router
  - step3:rejection-pair
  - step3:membership-migration
  - step3:nldm-assertion-withdrawal
  - step3:unchanged-companion
  evidence_ids:
  - writer-audit
  - prior-stamp-fix
  - analyzer-fix
  - implementation-package
  - capture-tests
  scope_note: Independent native probes are retained in exact portable receipts. No
    broad scientific approval is inferred from negative controls.
- check_id: full-qc
  name: Native complete QC
  status: passed
  required: true
  summary: just qc passes schema/evidence, SSSOM, roundtrip, indexes, visualization
    and flat coverage.
  target_ids:
  - MIM:Carnitine_Hydrochloride
  - MIM:Carnitine_Dl_Hydrochloride
  - MIM:NLDM_metabolites
  - step3:sssom-ncit
  - step3:sssom-nldm
  - step3:unified-salt
  - step3:guarded-writer
  - step3:finite-source-router
  - step3:rejection-pair
  - step3:membership-migration
  - step3:nldm-assertion-withdrawal
  - step3:unchanged-companion
  evidence_ids:
  - gate-full-qc
  command: just qc
  exit_code: 0
  scope_note: Supervisor executed this recorded native command; independent review
    verified receipt/log hashes and unchanged reviewed source/product bytes. It was
    not rerun merely to duplicate a completed broad suite.
- check_id: focused
  name: Native broad focused regressions
  status: passed
  required: true
  summary: 484focused regression tests pass.
  target_ids:
  - MIM:Carnitine_Hydrochloride
  - MIM:Carnitine_Dl_Hydrochloride
  - MIM:NLDM_metabolites
  - step3:sssom-ncit
  - step3:sssom-nldm
  - step3:unified-salt
  - step3:guarded-writer
  - step3:finite-source-router
  - step3:rejection-pair
  - step3:membership-migration
  - step3:nldm-assertion-withdrawal
  - step3:unchanged-companion
  evidence_ids:
  - gate-focused
  command: uv run --frozen python -m pytest -q -o addopts= -p no:cacheprovider tests/test_merge_carnitine_hydrochloride.py
    tests/test_carnitine_occurrence_routing.py tests/test_carnitine_merge_dependencies.py
    tests/test_mapping_change_receipt.py tests/test_reviewed_sssom.py tests/test_semantic_review_builder.py
    tests/test_semantic_mapping_review.py tests/test_ingredient_bundle.py tests/test_ingredient_bundle_dependency_refresh.py
    tests/test_unified_rejections.py tests/test_unified_source_holds.py
  exit_code: 0
  scope_note: Supervisor executed this recorded native command; independent review
    verified receipt/log hashes and unchanged reviewed source/product bytes. It was
    not rerun merely to duplicate a completed broad suite.
- check_id: suite
  name: Maintained full Python3.13 suite
  status: passed
  required: true
  summary: 3693passed,1skipped,27warnings; local coverage was not measured.
  target_ids:
  - MIM:Carnitine_Hydrochloride
  - MIM:Carnitine_Dl_Hydrochloride
  - MIM:NLDM_metabolites
  - step3:sssom-ncit
  - step3:sssom-nldm
  - step3:unified-salt
  - step3:guarded-writer
  - step3:finite-source-router
  - step3:rejection-pair
  - step3:membership-migration
  - step3:nldm-assertion-withdrawal
  - step3:unchanged-companion
  evidence_ids:
  - gate-suite
  command: uv run --frozen python -m pytest -q -o addopts= -p no:cacheprovider
  exit_code: 0
  scope_note: Supervisor executed this recorded native command; independent review
    verified receipt/log hashes and unchanged reviewed source/product bytes. It was
    not rerun merely to duplicate a completed broad suite.
- check_id: labels
  name: CURIE and product label checks
  status: passed
  required: true
  summary: Checks pass;101non-blocking product warnings retained.
  target_ids:
  - MIM:Carnitine_Hydrochloride
  - MIM:Carnitine_Dl_Hydrochloride
  - MIM:NLDM_metabolites
  - step3:sssom-ncit
  - step3:sssom-nldm
  - step3:unified-salt
  - step3:guarded-writer
  - step3:finite-source-router
  - step3:rejection-pair
  - step3:membership-migration
  - step3:nldm-assertion-withdrawal
  - step3:unchanged-companion
  evidence_ids:
  - gate-labels
  command: just curie-validate validate-products
  exit_code: 0
  scope_note: Supervisor executed this recorded native command; independent review
    verified receipt/log hashes and unchanged reviewed source/product bytes. It was
    not rerun merely to duplicate a completed broad suite.
- check_id: unified
  name: Unified rejection and freshness gates
  status: passed
  required: true
  summary: Both gates pass on the exact current unified artifact/provenance.
  target_ids:
  - MIM:Carnitine_Hydrochloride
  - MIM:Carnitine_Dl_Hydrochloride
  - MIM:NLDM_metabolites
  - step3:sssom-ncit
  - step3:sssom-nldm
  - step3:unified-salt
  - step3:guarded-writer
  - step3:finite-source-router
  - step3:rejection-pair
  - step3:membership-migration
  - step3:nldm-assertion-withdrawal
  - step3:unchanged-companion
  evidence_ids:
  - gate-unified
  command: just check-unified-rejections check-unified-freshness
  exit_code: 0
  scope_note: Supervisor executed this recorded native command; independent review
    verified receipt/log hashes and unchanged reviewed source/product bytes. It was
    not rerun merely to duplicate a completed broad suite.
- check_id: chain
  name: Native mapping, semantic, reviewed SSSOM, supported KGX and companion chain
  status: passed
  required: true
  summary: Receipt17 replay and content-bound integrity/export gates pass; all prior16receipts
    are retained. Both changed mappings remain WITHHOLD; no scientific approval is
    added.
  target_ids:
  - MIM:Carnitine_Hydrochloride
  - MIM:Carnitine_Dl_Hydrochloride
  - MIM:NLDM_metabolites
  - step3:sssom-ncit
  - step3:sssom-nldm
  - step3:unified-salt
  - step3:guarded-writer
  - step3:finite-source-router
  - step3:rejection-pair
  - step3:membership-migration
  - step3:nldm-assertion-withdrawal
  - step3:unchanged-companion
  evidence_ids:
  - receipt17
  - current-release
  - products
  - companion
  scope_note: Commands and exact exit codes are retained under generation/native-chain
    and validation gate execution manifests.
- check_id: kg-invariants
  name: Native canonical actual-KG invariants
  status: passed
  required: true
  summary: Canonical2982rows pass native invariants with available transforms; unavailable
    BTO/MICRO coverage is separately declared.
  target_ids:
  - MIM:Carnitine_Hydrochloride
  - MIM:Carnitine_Dl_Hydrochloride
  - MIM:NLDM_metabolites
  - step3:sssom-ncit
  - step3:sssom-nldm
  - step3:unified-salt
  - step3:guarded-writer
  - step3:finite-source-router
  - step3:rejection-pair
  - step3:membership-migration
  - step3:nldm-assertion-withdrawal
  - step3:unchanged-companion
  evidence_ids:
  - kg-boundary
  exit_code: 0
- check_id: missing-transforms
  name: BTO/MICRO actual-transform coverage
  status: unavailable
  required: false
  summary: Those two external transformed ontology inputs were unavailable; no validation
    of their B4 coverage is claimed.
  target_ids:
  - MIM:Carnitine_Hydrochloride
  - MIM:Carnitine_Dl_Hydrochloride
  - MIM:NLDM_metabolites
  - step3:sssom-ncit
  - step3:sssom-nldm
  - step3:unified-salt
  - step3:guarded-writer
  - step3:finite-source-router
  - step3:rejection-pair
  - step3:membership-migration
  - step3:nldm-assertion-withdrawal
  - step3:unchanged-companion
  evidence_ids:
  - kg-boundary
- check_id: full-scientific-release
  name: Whole-corpus scientific release
  status: failed
  required: false
  summary: Existing full-release verdict remains FAIL:1732blocking findings and2336OPEN
    assertions. Integrity/supported-subset success is not full-release approval.
  target_ids:
  - MIM:Carnitine_Hydrochloride
  - MIM:Carnitine_Dl_Hydrochloride
  - MIM:NLDM_metabolites
  - step3:sssom-ncit
  - step3:sssom-nldm
  - step3:unified-salt
  - step3:guarded-writer
  - step3:finite-source-router
  - step3:rejection-pair
  - step3:membership-migration
  - step3:nldm-assertion-withdrawal
  - step3:unchanged-companion
  evidence_ids:
  - current-release
  scope_note: This review verifies preservation and correct withdrawal of native approvals;
    it neither undertakes nor grants full scientific release.
- check_id: imodulon
  name: Organism-expression source adapter
  status: not_applicable
  required: false
  summary: The selected question is exact chemical form and publication provenance;
    expression-module membership is not evidence for this identity.
  target_ids:
  - MIM:Carnitine_Hydrochloride
  - MIM:Carnitine_Dl_Hydrochloride
  - MIM:NLDM_metabolites
  - step3:sssom-ncit
  - step3:sssom-nldm
  - step3:unified-salt
  - step3:guarded-writer
  - step3:finite-source-router
  - step3:rejection-pair
  - step3:membership-migration
  - step3:nldm-assertion-withdrawal
  - step3:unchanged-companion
  evidence_ids:
  - semantics
evidence:
- evidence_id: semantics
  kind: authority
  reference: MAPPING_SEMANTICS.md
  accessed_at: '2026-11-01T09:47:37.639444Z'
  support: supports
  summary: Exact supplied-form identity, same-substance aliases, rejected-label separation,
    registry and SSSOM rules govern this bounded migration.
  snapshot_sha256: 94aad13ea0fc3df82a37383f388f41432b607b04cac61ae5792ce1a381aef805
  locator: Sections 0 and 3; relevant synonym/SSSOM rules
- evidence_id: approved-decision
  kind: authority
  reference: reports/carnitine_hydrochloride_1004_20261101/sources/approved-decision.md
  accessed_at: '2026-11-01T09:47:37.639444Z'
  support: supports
  summary: 'Preserved approved #1004 decision selects NCIT:C216679 before consolidation;
    it does not confer native mapping/assertion approval.'
  snapshot_sha256: aee19d779a2980d1b2f9cb65eae352c3519ddd76d177db46db82186721342805
- evidence_id: nci
  kind: primary_source
  reference: reports/carnitine_hydrochloride_1004_20261101/sources/ncit-c216679.json
  accessed_at: '2026-11-01T09:47:37.639444Z'
  support: supports
  summary: NCI EVS reports active NCIT:C216679, DL-Carnitine Hydrochloride, CAS461-05-2
    and UNII F64264D63N in the captured26.10d response.
  snapshot_sha256: 3c2bbdefd80f43e183e5710bc34afcd24d4af9769cbbd966b8387b90d72a7db0
  locator: code, name, status and properties
- evidence_id: pubchem-salt
  kind: database
  reference: reports/carnitine_hydrochloride_1004_20261101/sources/pubchem-5970-properties.json
  accessed_at: '2026-11-01T09:47:37.639444Z'
  support: supports
  summary: 'CID5970 is the chloride-containing salt: C7H16ClNO3,197.66g/mol and explicit
    chloride-bearing SMILES/InChI.'
  snapshot_sha256: deccda58718bdec8e08efcd641918524dd5c8ed5cc05bfb7fbc3c1ccbec2064c
  locator: PropertyTable.Properties[0]
- evidence_id: pubchem-free
  kind: database
  reference: reports/carnitine_hydrochloride_1004_20261101/sources/pubchem-288-properties.json
  accessed_at: '2026-11-01T09:47:37.639444Z'
  support: refutes
  summary: CID288 represents free carnitine with C7H15NO3 and161.20g/mol; it cannot
    supply the salt chemistry.
  snapshot_sha256: 37e10b81d61f327bad86e2367d8d5f2b2d053f2f841941c3159814fff53570f0
  locator: PropertyTable.Properties[0]
- evidence_id: amide-conflict
  kind: primary_source
  reference: reports/carnitine_hydrochloride_1004_20261101/sources/chebi-48601-primary.json
  accessed_at: '2026-11-01T09:47:37.639444Z'
  support: refutes
  summary: CHEBI:48601 denotes carnitinamide chloride with a distinct nitrogen-containing
    formula; its conflicting CAS xref is retained as a conflict, not used to equate
    it with carnitine hydrochloride.
  snapshot_sha256: b2ccf5a651f0b3aa875440c5caee4c03eeb78e02e82b344a3278b6b4f935d6cd
  locator: CHEBI:48601 label, formula and xrefs
- evidence_id: sigma-extract
  kind: primary_source
  reference: reports/carnitine_hydrochloride_1004_20261101/sources/sigma-c9500-facts.json
  accessed_at: '2026-11-01T09:47:37.639444Z'
  support: supports
  summary: Selected facts from the retained successful independent rendered Sigma
    C9500 page support the exact salt form. This is a factual extraction with retained
    response binding, not a successful raw HTML capture.
  snapshot_sha256: 28efc0cdd5b8538d4f51730b4344ac20829b8903eb8ef42c2b6216e4c08293b6
  locator: source URL, actual access time, extracted product/CAS/formula and response
    hash
- evidence_id: raw-source
  kind: record_content
  reference: reports/carnitine_hydrochloride_1004_20261101/sources/selected-source-rows.json
  accessed_at: '2026-11-01T09:47:37.639444Z'
  support: supports
  summary: Two original CultureBotHT rows retain their raw Compound/CAS fields. The
    ignored rawCSV is an exact local snapshot associated with its checkout; its bytes
    are not claimed to be a tracked Git blob.
  snapshot_sha256: 7c36a19ccd5562abf7ef533df5251a35cfeaf23dbbd2ef78fe5d733093b2f50c
  locator: selected rows96 and787
- evidence_id: upstream-overlay
  kind: record_content
  reference: reports/carnitine_hydrochloride_1004_20261101/sources/compound_cas_corrections.tsv
  accessed_at: '2026-11-01T09:47:37.639444Z'
  support: supports
  summary: Existing tracked upstream correction is preserved as source evidence. MIM
    migration itself performs no source ingestion; separately merged Claw#700 applies
    only its bounded intake correction.
  snapshot_sha256: 10147dabecb0da6c50ca35445faafc514719a7cd3e25bf7b7bebe3c4b8685b27
- evidence_id: source-application
  kind: validation
  reference: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/step3-mim-independent/actual-source-application/receipt.json
  accessed_at: '2026-11-01T09:47:37.639444Z'
  support: supports
  summary: Independent actual-application check binds all three changed owners, original
    history prefixes and beforeimages, exact14recipe/count pairs, unchanged other2952individual
    records and synchronized changed aggregate entries. Eight unrelated inherited
    discussions omissions are unchanged.
  snapshot_sha256: 98d9304f8bdac0a51b4b077f4fe6cb9ed21df478963aafc4d6d819a7ef90d11f
  locator: actual application receipt and per-surface comparisons
- evidence_id: writer-audit
  kind: validation
  reference: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/step3-mim-independent/implementation-preapplication/receipt.json
  accessed_at: '2026-11-01T09:47:37.639444Z'
  support: supports
  summary: Independent preapplication probes tested native guarded publication, reservation
    replacement, valid competing-owner races, no-op receipt binding and run-wrapper
    checked-byte/input-set guards. Its earlier promotion readiness is historical and
    superseded by the actual native prior-stamp replay review.
  snapshot_sha256: 8d7144972abe9d4e0e9469a972518f0b52a20ef9ddace8e753d8156ec758bab8
  locator: native boundary evidence and frozen source hashes
- evidence_id: prior-stamp-fix
  kind: validation
  reference: reports/carnitine_hydrochloride_1004_20261101/implementation/independent/step3-mim-independent/revision-1038/receipt.json
  accessed_at: '2026-11-01T09:47:37.639444Z'
  support: supports
  summary: Independent actual native candidate replay confirms exact old NLDM validation
    stamp retention and empty new NCIT stamp; wrong/empty/foreign stamps are refused.
    Writer2ec6a4af and132author tests plus37independent focused tests are bound; author
    mutations retain attribution.
  snapshot_sha256: e92603d0ccc8a6aafd22d1bdab2b9ce1d7f4e87b9f6dbbae02537aca96bae2ee
  locator: actual-candidate replay, dry-run and negative controls
- evidence_id: implementation-package
  kind: validation
  reference: reports/carnitine_hydrochloride_1004_20261101/implementation/manifest.json
  accessed_at: '2026-11-01T09:47:37.639444Z'
  support: supports
  summary: 264indexed files retain original failures and repairs, exact application
    journals and independent checkpoints; current102repository references match this
    capture. The original selector-binding package is preserved in its separate checkpoint.
  snapshot_sha256: 89dd30961cc14cb1dfa8926133d263779685c2a6cdf74428a1c8a9adb6d65baf
  locator: files; corresponding readonly verifier and selector-binding-1037/
- evidence_id: generation-package
  kind: validation
  reference: reports/carnitine_hydrochloride_1004_20261101/generation/manifest.json
  accessed_at: '2026-11-01T09:47:37.639444Z'
  support: supports
  summary: 124indexed files bind the native2975-row diagnostic candidate, bounded
    canonical promotion, actual receipt-chain executions, unified build, producer
    inputs and corrected analyzer.
  snapshot_sha256: 29f25c513667b0d2f1ec8f7482cb14b96e8d607d7b72252e621ec945e4ecd4b4
  locator: files and captured_sources; independent readonly verifier --originals passed
- evidence_id: validation-package
  kind: validation
  reference: reports/carnitine_hydrochloride_1004_20261101/validation/manifest.json
  accessed_at: '2026-11-01T09:47:37.639444Z'
  support: supports
  summary: 49indexed files bind completed gates and independent actual-product/package
    checks. Original diagnostic failures remain explicitly distinguished from corrected
    successful checks.
  snapshot_sha256: a3a53d77405eecddcc3f7fb58a168fed56989f5fa7b68f55aadb710fb497eb7b
  locator: files
- evidence_id: products
  kind: validation
  reference: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/step3-mim-independent/final-state/product-audit.json
  accessed_at: '2026-11-01T09:47:37.639444Z'
  support: supports
  summary: Independent final product audit verifies canonical2982rows, receipt17 and
    preceding16receipt preservation, exact1unified-row change/4169unchanged, all4170names/209330occurrences,
    NLDM69withdrawals, companion51claims/20owners/17relocations, generated browser/labels
    and protected files.
  snapshot_sha256: 3a1449dd4935432c32ebae6346005b9a93badb065953019fc02cac391e9c8545
  locator: complete actual final-state audit
- evidence_id: analyzer-fix
  kind: validation
  reference: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/step3-mim-independent/final-state/1039-parser-proof.json
  accessed_at: '2026-11-01T09:47:37.639444Z'
  support: supports
  summary: Independent original/fixed parser comparison demonstrates why plain TSV
    must preserve four hash-prefixed names and seven occurrences. Actual mapping bytes
    were correct; only the old diagnostic count was wrong.
  snapshot_sha256: 787524f2b14ec4e9d8fe6f09ba21986b1897c657ab6db041869dbce6333ee453
  locator: original4166/209323 versus corrected4170/209330
- evidence_id: receipt17
  kind: record_content
  reference: reports/sssom_completion_20260921/mapping_changes/issue1004-carnitine-hydrochloride-merge.json
  accessed_at: '2026-11-01T09:47:37.639444Z'
  support: supports
  summary: Native receipt17 binds the three changed owners and exact two changed/four
    removed/zero added canonical rows without approving new claims.
  snapshot_sha256: e14ab50d5b981f2e003d755644ffcb98c901519fc0e8324658900ada1ae12e1c
  locator: sequence17; owner and SSSOM input/output hashes; row changes
- evidence_id: current-release
  kind: validation
  reference: reports/carnitine_hydrochloride_1004_20261101/generation/native-chain/build/verified-output.json
  accessed_at: '2026-11-01T09:47:37.639444Z'
  support: supports
  summary: Native chain has1739SUPPORTED/1243WITHHOLD mappings and2151approved-subset
    assertions; the full scientific release remains FAIL with1732blocking findings
    and2336OPEN assertions. NLDM loses69approvals, including67unchanged nonmapping
    payloads.
  snapshot_sha256: 3fb11b27841976ce0c23bc9ee64b7e1be15075c2183d3f8d2ac86a1653f06d41
  locator: mapping_counts; full_scientific_release; semantic_status_counts
- evidence_id: companion
  kind: record_content
  reference: reports/ingredient_bundle_20261101_carnitine1004/dependency-refresh.json
  accessed_at: '2026-11-01T09:47:37.639444Z'
  support: supports
  summary: Native unchanged-cohort refresh preserves51claim decisions and20owner hashes;17mapping
    references relocate. Changed carnitine/NLDM owners gain no companion approval.
  snapshot_sha256: a431e7347efd4f4ec3823b723edb4099318c4b7c41e287e0b8bcec8ca08cc059
  locator: source/owner/decision bindings and relocation audit
- evidence_id: current-canonical
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  accessed_at: '2026-11-01T09:47:37.639444Z'
  support: supports
  summary: Current canonical bytes are d5cd812a8c44c85438d73c68c7a8c3067a505765e4cd54e3a64cef029f2d8ed6.
    Only the selected salt and NLDM subject groups change.
  snapshot_sha256: d5cd812a8c44c85438d73c68c7a8c3067a505765e4cd54e3a64cef029f2d8ed6
  locator: exact target selectors and all unrelated line/header comparisons
- evidence_id: current-unified
  kind: record_content
  reference: UNIFIED_INGREDIENT_MAPPING.tsv
  accessed_at: '2026-11-01T09:47:37.639444Z'
  support: supports
  summary: Current unified bytes are ca62e2f031ebe0f9e6185efc7816207912095beef9799a04634c889cc27196b5.
    Only salt mim_id, cas_rn and accepted salt synonyms change; every occurrence cell
    is retained.
  snapshot_sha256: ca62e2f031ebe0f9e6185efc7816207912095beef9799a04634c889cc27196b5
  locator: ingredient_name=Carnitine Hydrochloride
- evidence_id: kg-boundary
  kind: validation
  reference: reports/carnitine_hydrochloride_1004_20261101/generation/canonical-validation/receipt.json
  accessed_at: '2026-11-01T09:47:37.639444Z'
  support: supports
  summary: Unmodified native canonical invariant validator passes with actual read-only
    KG transforms. BTO and MICRO transform inputs are explicitly unavailable; no claim
    of checking those B4 surfaces is made.
  snapshot_sha256: ed3addbe4d069614ef6a9d1a9573085d13aa455e937fedeca8b7c3a9f00b785c
  locator: exit_code0; missing_b4_transforms
- evidence_id: writer-source
  kind: record_content
  reference: scripts/merge_carnitine_hydrochloride.py
  accessed_at: '2026-11-01T09:47:37.639444Z'
  support: supports
  summary: Current hash2ec6a4afdd97d580e36471467fa884fe87caa6a76f0a3f7fa9756d00b1fc720e
    retains hash-bound input/candidate scope, existing receipt and regular preimage
    binding, reservation checks and native precommit destination uniqueness.
  snapshot_sha256: 2ec6a4afdd97d580e36471467fa884fe87caa6a76f0a3f7fa9756d00b1fc720e
  locator: apply_sources, completed source receipt checks, promote and native publication
    scope
- evidence_id: router-source
  kind: record_content
  reference: src/mediaingredientmech/utils/culturemech_occurrences.py
  accessed_at: '2026-11-01T09:47:37.639444Z'
  support: supports
  summary: Only the two reviewed normalized carnitine-hydrochloride source names route
    to NCIT:C216679; free, L-form and unrelated source identities retain native behavior.
  snapshot_sha256: d8b5b0ea02bf6c885d9627357dba04c2ba59626ca9bf12062ac70e7d6bed8c68
  locator: source override table and collection path
- evidence_id: fixture-manifest
  kind: record_content
  reference: tests/fixtures/issue1004-before/manifest.json
  accessed_at: '2026-11-01T09:47:37.639444Z'
  support: supports
  summary: Original historical migration preimages are immutable fixture inputs, not
    permanent live-cohort quotas. Both gzip fixtures omitted from the first staging
    are now present with exactly the already-declared hashes.
  snapshot_sha256: 7c36e370a593bb7063670e2fa44484e576d1bc25a05c1a7e5f9fa57402f33d93
  locator: culturemech_recipe_membership.tsv.gz and ingredient_mappings.sssom.tsv.gz
- evidence_id: capture-tests
  kind: validation
  reference: /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/approved-plan-20261101T031134Z/logs/step3-independent-capture-v2-writer-dependencies.json
  locator: Actual durable capture-v2; Python3.13;182passed,13warnings,0skips; logSHA715ebe680798fe0f5e62925f99b48f5b99d813a17318af1fabd384498e2b0ed1
  accessed_at: '2026-11-01T09:47:37.639444Z'
  support: supports
  summary: Independently reran complete writer, occurrence routing and dependency
    suites in the exact staged capture after explicit inclusion of the two immutable
    gzip fixtures. Native race, stamp, historical migration and future15/15 or14/15cohort
    controls pass.
  snapshot_sha256: 725d5499dabec95229f790b03f3453fda4ea278507cb7fff0c0290a320454860
- evidence_id: staging-finding
  kind: validation
  reference: https://github.com/CultureBotAI/MediaIngredientMech/issues/1040
  locator: Original tree4779e87c; native historical-membership test exited1 with FileNotFoundError.
    LogSHAa76f72ff3ddd8e7a57f3ce2f19e1261c9d859c47b98aa8ef2cbd41abd41f0af6; corrected
    treeb3084fcb includes exact two archives.
  accessed_at: '2026-11-01T09:47:37.639444Z'
  support: supports
  summary: Issue filed before correction. Gitignore-independent filesystem reads found
    originals; git index omitted both due *.tsv.gz. No implementation or data byte
    changed to repair staging. Both archives are included in this review source hashes
    and complete native rerun passes.
- evidence_id: gate-full-qc
  kind: validation
  reference: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/logs/step3-chain-final-v1-full-qc.json
  accessed_at: '2026-11-01T09:47:37.639444Z'
  support: supports
  summary: just qc passes schema/evidence, SSSOM, roundtrip, indexes, visualization
    and flat coverage.
  snapshot_sha256: 9750eb2d50f53d8a715d791191b5652f75bf8b0ee542301b1ca19df9adf9741c
  locator: argv, actual UTC execution, exit_code and log_sha256
- evidence_id: gate-focused
  kind: validation
  reference: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/logs/step3-chain-final-v1-receipt-regression-tests.json
  accessed_at: '2026-11-01T09:47:37.639444Z'
  support: supports
  summary: 484focused regression tests pass.
  snapshot_sha256: f682f221fbcf704c8e60698515f49db64e891e42b51374a122976aae892b0239
  locator: argv, actual UTC execution, exit_code and log_sha256
- evidence_id: gate-suite
  kind: validation
  reference: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/logs/step3-chain-final-v1-full-suite.json
  accessed_at: '2026-11-01T09:47:37.639444Z'
  support: supports
  summary: 3693passed,1skipped,27warnings; local coverage was not measured.
  snapshot_sha256: 1c20adbac11f34a61b1f9c29861e91b3dab9951904b9858b98567df87349fc47
  locator: argv, actual UTC execution, exit_code and log_sha256
- evidence_id: gate-labels
  kind: validation
  reference: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/logs/step3-chain-final-v1-curies-and-product-labels.json
  accessed_at: '2026-11-01T09:47:37.639444Z'
  support: supports
  summary: Checks pass;101non-blocking product warnings retained.
  snapshot_sha256: 12381c190b6f6c4016472f5d33e8df294bf9d1007c343eb42abae482bc97c7a1
  locator: argv, actual UTC execution, exit_code and log_sha256
- evidence_id: gate-unified
  kind: validation
  reference: reports/carnitine_hydrochloride_1004_20261101/validation/evidence/logs/step3-chain-final-v1-unified-gates.json
  accessed_at: '2026-11-01T09:47:37.639444Z'
  support: supports
  summary: Both gates pass on the exact current unified artifact/provenance.
  snapshot_sha256: 895a291b7a306e41daf901b3ce1daa4ed8b245b5537714bbaefb263fc8a62f52
  locator: argv, actual UTC execution, exit_code and log_sha256
assessments:
- assessment_id: active-identity
  area: identity
  topic: Approved exact salt identity and chloride chemistry
  outcome: supported
  summary: The maintained survivor now denotes DL-carnitine hydrochloride with NCIT:C216679/CAS461-05-2
    and CID5970chloride chemistry. Raw source spelling is preserved; free-substance
    and amide names remain attributed REJECTED_LABEL entries. This is conformance
    to the inspected approved identity decision, not a new native scientific approval.
  target_ids:
  - MIM:Carnitine_Hydrochloride
  evidence_ids:
  - semantics
  - approved-decision
  - nci
  - pubchem-salt
  - sigma-extract
  - source-application
  details: NCI label/status/CAS/UNII and PubChem structure/formula agree at this salt
    scope. Source evidence, history and LLM assistance are explicit. Free and L-specific
    sibling records remain unchanged controls; roles and biological mechanisms are
    not newly assessed.
- assessment_id: tombstone
  area: representation
  topic: Retired duplicate keeps correct identity and provenance
  outcome: supported
  summary: The rejected duplicate has identifier, ontology and representative NCIT:C216679,
    zero counts and no current free-carnitine chemical_properties. Exact prior wrong
    CAS/chemistry survives in append-only history and immutable preimages, avoiding
    publication of free-form chemistry as current salt assertions.
  target_ids:
  - MIM:Carnitine_Dl_Hydrochloride
  evidence_ids:
  - source-application
  - pubchem-free
  - nci
  - products
  details: Only one active owner exists. Browser and label rows resolve the raw name
    to the same NCIT identity. The REJECTED preferred-term row may precede the active
    synonym row; this review does not claim active-owner-first ordering.
- assessment_id: nldm-reference
  area: consistency
  topic: Mixture component reference migrates without broad mixture curation
  outcome: supported
  summary: Only NLDM component59 identity plus audit history changes; component name,17.5UM
    amount, mixture identity, other components and role payloads are retained. NLDM
    remains a distinct formulation, not an alias of its carnitine component.
  target_ids:
  - MIM:NLDM_metabolites
  evidence_ids:
  - source-application
  - products
  - receipt17
- assessment_id: canonical-salt
  area: grounding
  topic: Bounded exact salt mapping replaces wrong and redundant claims
  outcome: supported
  summary: Five former salt-subject claims become one exact NCIT:C216679 claim. The
    exact free CAS, broad free-parent and redundant registry rows retire; unsafe free-substance
    aliases are withheld from other. The new row has no inherited validation stamp
    and remains WITHHOLD.
  target_ids:
  - step3:sssom-ncit
  evidence_ids:
  - current-canonical
  - receipt17
  - products
  - nci
  - amide-conflict
  details: Canonical2986→2982 means two changed/four removed/zero added rows; unrelated
    row/header bytes remain exact. The2975-row full producer candidate is diagnostic,
    never a blanket canonical replacement.
- assessment_id: canonical-nldm
  area: provenance
  topic: Historical validation is distinct from scientific approval
  outcome: supported
  summary: NLDM canonical source and mapping_date change while its exact original
    manual:promote_resolved_unmapped|PROMOTED|2026-08-06annotation and old source
    tokens remain. Its changed owner forces WITHHOLD; retained historical annotation
    grants no approval.
  target_ids:
  - step3:sssom-nldm
  evidence_ids:
  - prior-stamp-fix
  - current-canonical
  - receipt17
  - current-release
- assessment_id: unified-salt
  area: consistency
  topic: One native unified row changes with every occurrence retained
  outcome: supported
  summary: Only Carnitine Hydrochloride changes mim_id, cas_rn and two accepted salt
    spellings. All4170names/209330occurrences remain;4169other raw rows and every
    occurrence cell are unchanged. Four hash-prefixed names remain real data.
  target_ids:
  - step3:unified-salt
  evidence_ids:
  - current-unified
  - products
  - analyzer-fix
  details: Current source-label rejection policy excludes the reviewed acylcarnitine/amide
    IDs in every identity column. No generic CHEBI ban or invented replacement is
    introduced.
- assessment_id: writer
  area: provenance
  topic: Guarded exact-preimage migration and refusal boundaries
  outcome: supported
  summary: The writer binds original inputs, source evidence, exact proposed bytes,
    unique destination ownership and reservation identity at native commit. Completed
    source no-ops bind the original regular complete receipt, timestamps, outputs
    and all seven preimages; promotion accepts only bounded subject changes and native
    historical stamp behavior.
  target_ids:
  - step3:guarded-writer
  evidence_ids:
  - writer-source
  - writer-audit
  - prior-stamp-fix
  - capture-tests
  - fixture-manifest
  details: Native race tests cover receipt/backup regular-file and symlink substitution
    and late valid owner insertion. A failed or conflicting publication cannot be
    reported complete. Guarantees apply at cooperative lock/native validation boundaries,
    not arbitrary later external writes.
- assessment_id: routing
  area: quantity
  topic: Finite source resolution and future-cohort behavior
  outcome: supported
  summary: Exactly the two reviewed normalized hydrochloride source names route to
    NCIT:C216679. Native15/15new-recipe and14/15repeated-listing controls pass; current
    fourteen memberships are a historical migration fixture, not a permanent live
    count quota. Free/L/amide and unrelated labels retain their existing behavior.
  target_ids:
  - step3:finite-source-router
  evidence_ids:
  - router-source
  - capture-tests
  - raw-source
- assessment_id: rejections
  area: identity
  topic: Scoped wrong-source identities remain excluded
  outcome: supported
  summary: The existing CHEBI:91318hold moves to the corrected owner and one preventive
    CHEBI:48601hold is appended with exact source label/owner attribution. Other ledger
    bytes are preserved; a conflicting CAS xref is not treated as salt identity.
  target_ids:
  - step3:rejection-pair
  evidence_ids:
  - amide-conflict
  - nci
  - products
  - source-application
- assessment_id: memberships
  area: quantity
  topic: Historical recipe pairs migrate without loss
  outcome: supported
  summary: Fourteen exact recipe IDs and listing counts move from the retired local
    identity to NCIT:C216679; headers and all unrelated membership bytes remain. Dynamic
    native producer tests permit legitimate future source evolution.
  target_ids:
  - step3:membership-migration
  evidence_ids:
  - source-application
  - products
  - capture-tests
  - fixture-manifest
- assessment_id: withdrawal
  area: ownership
  topic: Changed NLDM owner invalidates all inherited approvals
  outcome: supported
  summary: All64component and4role approvals become OPEN because the full NLDM owner
    hash changed, even though67nonmapping payload hashes are identical. The separate
    mapping becomes WITHHOLD, totaling69withdrawals. No section-equivalence, unchanged-payload
    or approval-model bypass is introduced.
  target_ids:
  - step3:nldm-assertion-withdrawal
  evidence_ids:
  - current-release
  - products
  - receipt17
- assessment_id: companion-preservation
  area: ownership
  topic: Unchanged explicit companion decisions remain byte-bound
  outcome: supported
  summary: The companion refresh preserves all51claim decisions and20owner hashes;17mapping
    locators relocate under the existing strict comparator. The exact workflow selector
    points to this new bundle. Protected qc-evidence, vendored pin and Intel review
    files remain unchanged.
  target_ids:
  - step3:unchanged-companion
  evidence_ids:
  - companion
  - products
  - implementation-package
  details: No changed carnitine or NLDM owner is introduced into the approved companion
    cohort. This structural refresh preserves existing approvals and grants none.
- assessment_id: evidence-limits
  area: evidence
  topic: Primary source conflicts and access boundaries remain visible
  outcome: supported
  summary: The frozen source package retains exact primary bytes and receipt provenance
    with honest limitations. ChEBI conflicting CAS evidence is explicitly preserved
    rather than erased; no PubChem-to-CHEBI:48601xref claim is made.
  target_ids:
  - MIM:Carnitine_Hydrochloride
  - MIM:Carnitine_Dl_Hydrochloride
  - step3:rejection-pair
  evidence_ids:
  - nci
  - pubchem-salt
  - pubchem-free
  - amide-conflict
  - sigma-extract
  - raw-source
  - upstream-overlay
  details: Sigma is a selected extraction from the retained rendered response, not
    recovered full HTML. The raw ignored CultureBotHT CSV is not represented as committed
    source content. Direct CAS Registry access was unavailable; no CAS Registry verification
    is claimed. Existing exact upstream correction consumption is scoped to the separately
    merged maintained Claw intake.
findings: []
actions: []
boundary_decisions:
- action: lump
  target_ids:
  - MIM:Carnitine_Hydrochloride
  - MIM:Carnitine_Dl_Hydrochloride
  rationale: Inspected approved source evidence identifies these two source spellings
    as the same DL-carnitine hydrochloride supplied form. Consolidation retains one
    active owner and an explicit rejected representative-linked provenance record;
    neither is equated with free carnitine, L-specific siblings or carnitinamide.
  evidence_ids:
  - semantics
  - approved-decision
  - nci
  - pubchem-salt
  - sigma-extract
  - source-application
  proposed_groups:
  - label: One active NCIT:C216679salt identity with historical rejected duplicate
      retained
    target_ids:
    - MIM:Carnitine_Hydrochloride
    - MIM:Carnitine_Dl_Hydrochloride
- action: retain
  target_ids:
  - MIM:NLDM_metabolites
  rationale: NLDM is a distinct mixture that contains the salt; component-reference
    repair never merges mixture identity with a component.
  evidence_ids:
  - semantics
  - source-application
  - products
limitations:
- scientific_review is false. This bounded implementation, provenance and approved-identity
  conformance review does not promote native mapping/assertion status, grant scientific
  release approval or certify the full corpus.
- Full semantic scientific release remains FAIL with1732blocking findings and2336OPEN
  assertions;2151approved-subset assertions and1739SUPPORTED mappings are retained
  existing scope. Both changed mappings remain WITHHOLD.
- Scientific source checks cover the selected salt identity and rejection boundaries
  only. Roles, mechanisms, every NLDM component, and all other corpus identities were
  not independently scientifically re-reviewed.
- BTO and MICRO transformed ontology inputs were unavailable. Native invariant passes
  apply only to available actual-KG surfaces; no unavailable B4 coverage is implied.
- The Sigma evidence is a factual extraction from a retained successful rendered response.
  Failed raw HTML capture is not relabeled as success. Direct CAS Registry lookup
  was not available; raw CultureBotHT CSV bytes are an ignored local snapshot, not
  a tracked Git revision.
- Eight unrelated aggregate discussions omissions predate this work and remain unchanged.
  Successful native QC does not establish complete corpus-wide semantic equality of
  individual and aggregate surfaces.
- Corrected tombstone and active survivor resolve to the same NCIT identity in label
  products; this does not establish active-owner-first label-index ordering.
- Local full-suite coverage was not measured; CI and merge-group checks have not been
  evaluated for a future committed head. Exact committed-head and integration review
  remain separate.
- This source.state is working_tree at the actual durable main commit99fe4b44, with
  staged overlay treeb3084fcb. It does not claim those601input bytes were already
  committed.
- Original pre-fix failures and unsuccessful reviewer harness diagnostics remain historical
  evidence. Only corrected controls and current final source/product checks support
  this verdict.
notes:
- Pre-fix findings#1036,#1037,#1038,#1039 and#1040were reported/filed before fixes.
  Original failures, fixed controls and exact current hashes are retained. They are
  referenced as workflow evidence, not fabricated previous structured finding occurrences.
  Empty findings means no unresolved defect in this exact bounded review, not closure
  of all historical issues.
- The original520-path capture omitted two ignored gzip preimages and failed the native
  historical membership test. The preserved original capture is not the review source.
  The corrected actual522-path capture adds only the exact already-manifested archives,
  with no production code/data byte change; all102repository references now exist.
- Source capture601input hashes include522changed staged paths, current maintained
  dependencies, immutable prior receipts, primary evidence, native schema/contract
  and sibling controls. Native inspection preceded these assessments; actual UTC timestamps
  are used.
- The independent capture test receipt and first-failure log are run-owned external
  evidence and are referenced as such, never relabeled as repository inputs. Their
  command, result and immutable hashes are preserved in this bundle.
- Run-owned orchestration scripts and candidate generation were reviewed as execution
  evidence; they are not newly introduced general repository APIs. Existing protected
  workflow/pin bytes were checked against durable base.
links:
- https://github.com/CultureBotAI/MediaIngredientMech/issues/1004
- https://github.com/CultureBotAI/MediaIngredientMech/issues/1036
- https://github.com/CultureBotAI/MediaIngredientMech/issues/1037
- https://github.com/CultureBotAI/MediaIngredientMech/issues/1038
- https://github.com/CultureBotAI/MediaIngredientMech/issues/1039
- https://github.com/CultureBotAI/MediaIngredientMech/issues/1040
- https://github.com/CultureBotAI/culturebotai-claw/pull/700
tags:
- approved-step3
- carnitine-hydrochloride
- independent-review
- bounded-migration
- no-scientific-approval
```
