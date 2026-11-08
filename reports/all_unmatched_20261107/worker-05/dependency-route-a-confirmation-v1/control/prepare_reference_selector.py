from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,shutil,yaml
W=Path.cwd();C=W.parents[2];B=W/'reports/all_unmatched_20261107/worker-05';P=B/'buffer-parts-v1';Q=B/'dependency-route-a-confirmation-v1';S=W/'.temp/w05-dependency-route-a-confirmation-v1'
j=lambda p:json.loads(p.read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def bind(p):return dict(path=str(p.relative_to(W)) if p.is_relative_to(W) else str(p),sha256=sha(p))
def put(p,d):
 assert not p.exists(),p
 p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,indent=2,ensure_ascii=False,default=str)+'\n')
def cp(src,dst):
 assert not dst.exists(),dst
 dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst);assert sha(src)==sha(dst)
ps=j(P/'core/proposals.json')['proposals'];pi={p['proposal_id']:p for p in ps};deps=j(P/'dependencies-direct-v1/proposals.json')['proposals'];nc=j(S/'validation/route-a-negative-controls.json');pres=j(S/'validation/preservation.json')
now=datetime.now(timezone.utc).isoformat();selected=[]
for d in deps:
 p=pi[d['proposal_id']];r=p['dependency_reassessment'];selected.append(dict(proposal_id=p['proposal_id'],owner_path=p['owner_path'],before_sha256=p['before_sha256'],after_capture=p['after_capture'],canonical_proposal_object_sha256=hashlib.sha256(json.dumps(p,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest(),canonical_selector='core/proposals.json from predecessor reference',component_claim=r['claim_key'],source_case_ids=p['case_ids'],causal_parent_case=r['causal_parent_case_id'],causal_parent_case_input_sha256=r['case_input_sha256'],child_recipe_observed_in_causal_source_case=False,existing_origin_type='new child origin already published at108e' if p['proposal_id'].startswith('W05-DEP-PEPTONE-') else 'original existing child origin composed at108e',payload_author=r['author'],original_metadata_preserved=True))
put(Q/'selector.json',dict(schema_version=1,at=now,compiler='/root',type='reference_only_successor',source_head='108e213e96f7d423ee345ce265d692e79063127c',publication_head='See final Git commit and private HANDOFF; self-referential commit hashes are not embedded.',predecessor_selector=bind(P/'selected-origin-bindings.json'),canonical_core=pres['canonical_core'],counts=pres['counts'],dependency_proposals=selected,conditional_generic_parent=dict(proposal_id='W05-FINAL-MAT-039',after_capture=pi['W05-FINAL-MAT-039']['after_capture'],identifier='mesh:D010461',condition='Co-apply only with the exact scientifically reviewed and coordinator-accepted generic owner; reassess references if its identity bytes change.'),source_membership='All188 frozen cases,388 occurrence memberships and138 original proposal lineages remain exactly in predecessor core. These15 child edits are causal consequences, not newly assigned recipes.',new_cases=0,new_proposals=0,payload_changes=0,old_plan_target='kgmicrobe.ingredient:peptone is a frozen earlier fallback; the later reviewed exact MeSH target is selected without rewriting the plan.',root_integration_obligations=nc['other_worker_generic_dependencies'],authority='This selector preserves the complete prior155 proposals by reference. It adds fresh scoped review evidence only; source, owner, role, export and whole-union approval remain separate.'))
old=j(P/'dependencies-direct-v1/source-assessment.json');rows=[]
for r in old['rows']:
 rows.append({k:r[k] for k in ['target_id','claim_key','owner_path','authentic_before_sha256','after_capture','proposal_id','source_ids','scientific_assessment','disposition','precise_remaining_requirement','prior_primary_author','prior_skeptical_author']})
put(Q/'source-scope-ledger.json',dict(at=now,compiler='/root',exact_existing_source_assessment=bind(P/'dependencies-direct-v1/source-assessment.json'),source_observations=bind(P/'dependencies-direct-v1/source-observations.json'),source_read_ledger=bind(P/'dependencies-direct-v1/source-read-ledger.json'),rows=rows,remaining_plan_claims=old['out_of_lane_context'],scientific_attribution='The retained assessment text is copied unchanged with actual earlier authors. New primary reassessments are in generic-audit and ambiguous-audit; the separate final skeptical review owns its own conclusions. Original primary acquisition timestamps are not replaced.',holds='The seven new and three composed unknown part identities remain UNMAPPED pending each specified source fact. Named parts, quantities and history remain. Whole-owner uncertainty, inferred component text and inherited method/completeness are not converted into new recipe evidence.'))
for f in (S/'inputs').iterdir():cp(f,Q/'inputs'/f.name)
for name in ['route-a-negative-controls.json','preservation.json','full-overlay.receipt.json','strict-dependencies.receipt.json','strict-dependencies.stdout.log','strict-dependencies.stderr.log']:
 cp(S/'validation'/name,Q/'validation'/name)
cp(S/'validation/full-overlay/native-validation.json',Q/'validation/full-overlay/native-validation.json')
cp(S/'validation/full-overlay/overlay-paths.json',Q/'validation/full-overlay/overlay-paths.json')
for name in ['exact-accounting.receipt.json','exact-accounting.stdout.log','exact-accounting.stderr.log']:
 cp(S/'validation'/name,Q/'diagnostics/private-output-attempt'/name)
put(Q/'diagnostics/private-output-attempt/DISPOSITION.json',dict(at=now,status='resolved_harness_output_location',description='First accounting invocation selected a private output outside the explicit worker artifact root. The unchanged native auditor rejected that destination before scientific accounting. The second invocation writes under this public artifact root and passes. No source, gate or constructor change; original command and failure retained.'))
for f in (S/'generic-audit').rglob('*'):
 if f.is_file():cp(f,Q/'generic-audit'/f.relative_to(S/'generic-audit'))
for f in (S/'control').glob('*.py'):cp(f,Q/'control'/f.name)
readme='''# W05 route-A dependent-origin confirmation

This ordinary report-only successor confirms that the queued twelve missing-origin routes were already implemented and independently reviewed in source head `108e213e96f7d423ee345ce265d692e79063127c`, under the prior authorization to consolidate queued work. It creates no duplicate child proposal or source case and changes no selected payload. `selector.json` is authoritative by exact reference to the complete predecessor core: 188 cases, 388 occurrence memberships, 155 proposals and all 138 original lineages.

The twelve authentic child origins comprise five supported generic references and seven withdrawals of unsupported resolving identifiers. Three existing Fastidious/PY-glucose-rumen/PYG_Rumen origins already compose the peptone correction with the prior meat/rumen correction against their real beforeimages. Their original authors and histories remain intact. The causal generic-Peptone case is context for dependent edits, not a claim that these child recipes were observed in the W05 source shard.

The five generic references are conditional on the exact reviewed `mesh:D010461` Peptone parent (SHA256 `c083794668a362203de6430eaa2609c34cd8ef78574a1230aa25b4a64fb55fd7`). The frozen plan's earlier local target is preserved as history. Source-unspecified supplier, animal and digest scope is retained. Ten ambiguous part references, including the three composed origins, remain UNMAPPED with their literal or explicitly inherited interpreted names, quantities and provenance. Each precise source prerequisite remains in `source-scope-ledger.json` and the fresh scientific audits.

GYPS's evidenced Bacto reference remains unchanged. Marine Broth 2216's existing withdrawal is retained. Marine agar 2216, PYGS and the TOGO M2491 MRSSi base have authentic other-origin generic dependencies for coordinator composition; this packet neither creates competing origins nor claims their latest cross-worker payloads approved. All twenty peptone claims are explicitly accounted for.

Fresh disjoint primary confirmation is by `/root/buffer_hepes` (five generic children) and `/root/buffer_tris` (seven ambiguous children, three composed children and the five other-scope controls). `/root/final_skeptical` independently reviews the exact fifteen full payloads and source applicability. `/root/assembly_audit` separately checks assembly/preservation. Root compiles the selector and runs native checks; it is not its own independent scientific reviewer. Earlier source searches/captures keep their actual original attribution and timestamps. No new paid research or external session was used.

The full candidate replay checks guarded writes/schema and partonomy against the entire substituted baseline. Strict closed-schema checks cover all fifteen dependent payloads; fresh accounting checks all 188 cases and 138 original lineages. Focused source controls distinguish structurally valid but scientifically unsupported Bacto references. The original native mapping projections remain bound to unchanged payload and baseline bytes. Native structured review remains scoped and does not grant maintained-owner, role, source-case or export approval.

Original reports, rejected drafts, captures, manifests, native reviews and the sealed 22-family comparison remain unchanged. The existing five chemical finding dispositions remain in the preserved late coordination addendum. No maintained record, aggregate, input source, gate, constructor, pin, workflow, downstream export or GitHub message is changed. Root coordinator owns final composition/application and acceptance.
'''
q=Q/'README.md';assert not q.exists();q.write_text(readme)
print(json.dumps(dict(status='PREPARED_FOR_FINAL_REVIEW',selector=bind(Q/'selector.json'),dependent_proposals=len(selected))))
