from pathlib import Path
from datetime import datetime, timezone
import copy, hashlib, json, os, shutil, subprocess
import yaml
from mediaingredientmech.validation.write_validated import validate_ingredient

W=Path.cwd();B=W/'reports/all_unmatched_20261107/worker-05';S=W/'.temp/w05-buffer-parts-v1/tris'
C=W.parents[2];T=C/'preflight/buffer-source-parts-triage-v1';O=B/'tellurium-polypeptone-v1/core'
BASE='0bac12cabfd1f67f212631d8eef9aa46379f6b41';AUTHOR='/root/buffer_tris'
CID='CM_NAME:9558a75c197cfda4c3def53eadc24fd61287448ec78b6642a3835678b80fcfe4'
PIDS=['CHEM-C1193-DSMZ_394_1137-Tris','CHEM-C1193-JCM_1061-Tris']
SHA=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
OBJ=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
J=lambda p:json.loads(p.read_text());AT=datetime.now(timezone.utc).isoformat()
def put(p,x):
 assert not p.exists(),p;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def cp(p,q):
 assert not q.exists(),q;q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q);assert p.read_bytes()==q.read_bytes()
def bind(p):return dict(path=str(p.relative_to(W)),sha256=SHA(p))
assert subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()==BASE
assert SHA(T/'ASSESSMENT.json')=='53e137bc1f567a810258a1d552fa001b5dd10ebffd83f3654695a5053a7b07b0'
assessment=J(T/'ASSESSMENT.json')
for name,sha in assessment['files'].items():assert SHA(T/name)==sha
for name in ['ASSESSMENT.json','new-tris-components-finding-v1.json','primary-capture-index.json','issue1237-comment.md','comment-readback.json','comment-published.json']:
 cp(T/name,S/'inputs'/name)
cp(W/'.temp/w05-buffer-parts-v1/issues/comment6718873227.json',S/'inputs/comment-live.json')
capture_index=J(T/'primary-capture-index.json')
for row in capture_index:
 for name in [row['path'],row.get('text_path',row['name']+'.txt')]:cp(T/name,S/'captures'/name)
put(S/'inputs/primary-integrity.json',dict(at=AT,status='PASS',triage_assessment_sha256=SHA(T/'ASSESSMENT.json'),all_declared_capture_hashes_match=True,exact_copies_retain_original_timestamps=True))
PS=[copy.deepcopy(x) for x in J(O/'proposals.json')['proposals'] if x['proposal_id'] in PIDS];assert len(PS)==2
D=next(copy.deepcopy(x) for x in J(O/'decisions.json')['decisions'] if x['case_id']==CID)
put(S/'inputs/decision-before.json',D);put(S/'inputs/proposals-before.json',dict(proposals=PS))
E0=J(O/'evidence.json')['evidence'];Q=Path(J(B/'contracts/frozen-baseline.json')['queue']['root'])
stock_occ={o for p in PS for o in p['applies_to_occurrence_ids']};assert len(stock_occ)==8
sources=[]
for e in E0:
 if e['evidence_id'].startswith('CHEM-RECIPE-076-') and any(o in e['locator'] for o in stock_occ):
  p=Q/e['capture']['path'];assert SHA(p)==e['capture']['sha256'];r=yaml.safe_load(p.read_text());cp(p,S/'frozen-recipes'/p.name)
  nodekey=e['locator'].split('assigned node=')[1].split(';')[0];node=r
  for k in nodekey.split('/'):node=node[int(k)] if isinstance(node,list) else node[k]
  sources.append(dict(evidence_id=e['evidence_id'],capture=e['capture'],local_copy=bind(S/'frozen-recipes'/p.name),locator=e['locator'],raw_assigned_node=node,source_recipe_id=r['id'],source_recipe_notes=r.get('notes'),source_recipe_reference=r.get('term',r.get('media_term')),inspection='Complete frozen recipe parsed and source/stock occurrence context read; secondary mappings and receiving-medium quantities not approved.'))
assert len(sources)==8
put(S/'occurrence-routes.json',dict(at=AT,author=AUTHOR,case_id=CID,all_case_occurrence_ids=D['occurrence_ids'],reviewed_stock_occurrence_ids=sorted(stock_occ),untouched_occurrence_ids=[x for x in D['occurrence_ids'] if x not in stock_occ],proposal_routes=[dict(proposal_id=p['proposal_id'],occurrence_ids=p['applies_to_occurrence_ids']) for p in PS],frozen_sources=sources,preservation='Six DSMZ394/1137 routes and two JCM1061 routes retained exactly. Frozen source labels/units/secondary annotations are neither rewritten nor promoted. Other eight case occurrences retain their existing separate solid-salt or receiving-medium handling.'))
bindings=[];guard=[]
for p in PS:
 current=B/p['after_capture']['path'];old=B/p['predecessor_after_capture']['path'];assert SHA(current)==p['after_capture']['sha256'];assert SHA(old)==p['predecessor_after_capture']['sha256']
 r=yaml.safe_load(current.read_text());before=yaml.safe_load(old.read_text())
 assert 'components' not in r and 'component_assertion' not in r
 assert before['components'] and before['component_assertion']['method']=='RECIPE_TRANSCRIPTION'
 assert r['curation_history'][:len(before['curation_history'])]==before['curation_history']
 assert r['ontology_mapping']['evidence'][0]['evidence_type']=='LLM_SUGGESTION'
 for k in ['identifier','preferred_term','mapping_status','ingredient_type','synonyms','solution_type']:assert r[k]==before[k]
 errors=validate_ingredient(r);assert not errors,[x.message for x in errors]
 cp(current,S/'selected-payloads'/current.name);cp(old,S/'historical-before'/old.name)
 commit=subprocess.check_output(['git','log','--diff-filter=A','--format=%H %aI %cI','--',str(current.relative_to(W))],text=True).strip()
 bindings.append(dict(proposal_id=p['proposal_id'],current_capture=p['after_capture'],historical_before_capture=p['predecessor_after_capture'],proposal_object_sha256=OBJ(p),current_payload_unchanged=True,proposal_object_unchanged=True,history_unchanged=True,no_new_event=True,components_absent=True,component_assertion_absent=True,recorded_prior_correction_time=r['curation_history'][-1]['timestamp'],first_commit=commit))
 guard.append(dict(proposal_id=p['proposal_id'],payload_sha256=SHA(current),guarded_validation_errors=0,call='mediaingredientmech.validation.write_validated.validate_ingredient',write_performed=False,reason='Current complete selected payload already contains the bounded correction; no-op writes/events forbidden.'))
put(S/'payload-bindings.json',dict(at=AT,author=AUTHOR,base=BASE,payloads=bindings,changed_payloads=0,changed_proposal_objects=0))
put(S/'validation/guarded-read-only.json',dict(at=AT,status='PASS',checks=guard))
env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',PYTHONPATH='src');cmd=[str(W/'.temp/all-unmatched-worker-05/venv/bin/python'),'scripts/validate_strict.py']+[str(B/p['after_capture']['path']) for p in PS]+['--workers','1','--out',str(S/'validation/strict-failures.tsv')]
run=subprocess.run(cmd,text=True,capture_output=True,env=env);(S/'validation/strict.stdout.log').write_text(run.stdout);(S/'validation/strict.stderr.log').write_text(run.stderr)
put(S/'validation/strict-receipt.json',dict(at=datetime.now(timezone.utc).isoformat(),command=cmd,exit_code=run.returncode,scope='Two exact full retained Tris stock payloads',stdout=bind(S/'validation/strict.stdout.log'),stderr=bind(S/'validation/strict.stderr.log')));assert run.returncode==0
comment=J(S/'inputs/comment-live.json');pub=J(S/'inputs/comment-published.json');handoff=W/'.temp/w05-final-correction-v1/HANDOFF.json';h=J(handoff)
chronology=dict(at=AT,author=AUTHOR,original_finding=dict(path=str((B/'final-correction-v1/chemicals/new-tris-components-finding-v1.json').relative_to(W)),sha256=SHA(B/'final-correction-v1/chemicals/new-tris-components-finding-v1.json'),reported_before_fix_field=J(T/'new-tris-components-finding-v1.json')['status'],exact_original_report_time=None,limitation='The immutable original finding has no standalone timestamp; preserve its historical reported-before-fix assertion without inventing an exact report time.'),selected_history_recorded_correction_at='2026-11-08T07:40:53.320531+00:00',coordinator_assessment_at=assessment['at'],github_comment_created_at=comment['created_at'],github_comment_updated_at=comment['updated_at'],coordinator_publication_receipt_at=pub['at'],first_corrected_payload_commit='5156d92bec6bd885ca8bae3c5e18bfdce0069176',first_corrected_payload_commit_time='2026-11-08T08:25:04+00:00',first_publication_handoff=dict(path=str(handoff.relative_to(W)),sha256=SHA(handoff),at=h['at'],published_head=h['published_exact_head']),current_action='Reassess and re-review already corrected published bytes. No repeated removal, no new curation event.',order='Recorded private correction precedes coordinator assessment and formal filing; formal filing precedes ordinary commit and verified publication. This successor does not assert filing preceded that earlier private correction or confer retroactive approval.')
put(S/'chronology.json',chronology)
science=dict(at=AT,scientist=AUTHOR,base=BASE,scope=dict(proposals=PIDS,source_case=CID,full_selected_payloads=2,full_source_decisions=1,stock_occurrences=8,whole_case_occurrences_retained=len(D['occurrence_ids']),primary_tris_recipes=['DSMZ394','DSMZ1137','JCM1061'],context_only_primary_recipes=['NBRC1221','NBRC1474']),conclusion='The two exact current Tris stock payloads already satisfy the filed NEW-03 bounded material-partonomy correction and remain unchanged. Their nominal whole-stock concentrations and pH are supported. No preparation-input/material-component list is supported by these three complete primary recipes.',source_assessments=[
 dict(source='DSMZ394',capture='captures/dsm394.pdf',captured_at=next(x['at'] for x in capture_index if x['name']=='dsm394'),literal='1M Tris-HCl (pH 7.5)',source_amount='20.0 ml in the receiving recipe',assessment='The source explicitly identifies a 1 M, pH 7.5 Tris-HCl stock additive. Distilled water belongs to the receiving recipe; no stock solvent, free HCl, Tris-base input or acid/base ratio is supplied.'),
 dict(source='DSMZ1137',capture='captures/dsm1137.pdf',captured_at=next(x['at'] for x in capture_index if x['name']=='dsm1137'),literal='Tris-HCl (1M, pH 7.5)',source_amount='5.0 ml in the receiving recipe',assessment='The source explicitly identifies the nominal 1 M, pH 7.5 stock description also used in DSMZ394. Different receiving doses do not establish a different stock. Hutner/Metals44/artificial-seawater inputs and pH-adjustment instructions belong to their own named preparation contexts and cannot populate Tris stock components. Shared nominal strength/pH does not prove every unreported formulation detail equal.'),
 dict(source='JCM1061',capture='captures/jcm1061.html',captured_at=next(x['at'] for x in capture_index if x['name']=='jcm1061'),literal='0.5 M Tris-HCl solution (pH 8.0)',source_amount='100.0 ml in the receiving recipe',assessment='Explicit 0.5 M, pH 8.0 supplied stock differs in nominal strength and source pH from the 1 M, pH 7.5 specification. The instruction to bring the medium to 1.0 L with distilled water is for the receiving medium; it supplies no stock solvent or preparation-input list.')],
 mapping_and_identity='Retain existing stock identifiers and FALLBACK_REGISTRY mappings as source proposal continuity. No dry Tris hydrochloride substitution, new owner, union, CAS, ion bridge or mapping-grade change. The separately filed solid-salt #1238 change is outside this scope.',
 material_partonomy='MAPPING_SEMANTICS section6 distinguishes material parts from ionic/speciation descriptions. Total Tris moiety and chloride species were unsupported material components; changing only RECIPE_TRANSCRIPTION would not fix them. Both components and paired assertion are already absent. Unknown material composition remains explicit in notes and source decision; no unknown-completeness orphan assertion is added.',
 history='Complete historical creation and correction events retained byte-for-byte. Original before payloads and finding retain withdrawn component/evidence objects. New MappingEvidence is already LLM_SUGGESTION; historical process/component enums are not rewritten.',
 source_and_release_limits='Frozen case/source occurrence routing, units, raw labels and holds remain exact. No receiving-medium dose, source/material/role/organism admission, owner union or export approval. Existing evidence for the eight other case occurrences is retained with original attribution and is not newly approved.',
 payload_bindings=bindings,remaining_prerequisite='Only explicit stock preparation/formulation evidence could support actual constituent entries, acid/base proportions or solvent. Its absence does not prevent retaining the named whole stock.',new_findings=[])
put(S/'source-assessment.json',science)
add=[]
for name,label in [('dsm394','DSMZ394'),('dsm1137','DSMZ1137'),('jcm1061','JCM1061')]:
 r=next(x for x in capture_index if x['name']==name);match=next(x for x in science['source_assessments'] if x['source']==label)
 add.append(dict(evidence_id='W05-BUFFER-TRIS-PRIMARY-'+label,kind='primary_source',capture=dict(root='artifact',path='buffer-parts-v1/tris/captures/'+r['path'],sha256=r['sha256']),url=r['url'],locator='Complete source recipe; nominal whole Tris stock name/strength/pH and receiving-recipe context.',supports_or_contradicts=match['assessment'],case_ids=[CID],accessed_at=r['at'],reused_capture=True,assessment_author=AUTHOR,assessed_at=AT))
for eid,name,kind,note in [
 ('W05-BUFFER-TRIS-ASSESSMENT','source-assessment.json','source_review','Complete current source-qualified assessment of both Tris stock payloads and eight frozen stock occurrence routes; existing bounded removal verified, no new payload change.'),
 ('W05-BUFFER-TRIS-CHRONOLOGY','chronology.json','provenance_review','Honest recorded-private-fix, formal filing, commit and publication chronology; no retroactive approval or fabricated timestamp.'),
 ('W05-BUFFER-TRIS-FILING','inputs/comment-live.json','issue_context','Filed NEW-03 bounded correction and coordinator source-context limits; filing is not scientific approval.')]:
 add.append(dict(evidence_id=eid,kind=kind,capture=dict(root='artifact',path='buffer-parts-v1/tris/'+name,sha256=SHA(S/name)),url=comment['html_url'] if eid.endswith('FILING') else None,locator=note,supports_or_contradicts=note,case_ids=[CID],accessed_at=AT,author=AUTHOR))
D['evidence_ids']=list(dict.fromkeys(D['evidence_ids']+[x['evidence_id'] for x in add]));D['issue_refs']=list(dict.fromkeys(D['issue_refs']+[comment['html_url']]))
D['buffer_parts_reassessment']=dict(author=AUTHOR,at=AT,base=BASE,finding_id='W05-FINAL-CHEM-NEW-03',outcome='Exact current published payloads already corrected; retained unchanged and freshly assessed.',reviewed_proposal_ids=PIDS,current_payload_bindings=bindings,source_assessment_evidence_id='W05-BUFFER-TRIS-ASSESSMENT',chronology_evidence_id='W05-BUFFER-TRIS-CHRONOLOGY',preserved_scope='All16 case occurrence IDs, their exact source routing, owner references, inherited source holds and independent historical reviews remain. Scientific reassessment is bounded to the two prepared buffer payloads/eight stock routes; dry salt and remaining contexts are unchanged.',no_new_payload_change=True,no_whole_owner_or_release_approval=True)
put(S/'decisions.json',dict(decisions=[D]));put(S/'proposals.json',dict(proposals=PS));put(S/'evidence.json',dict(evidence=add))
ledger=[]
for p in [W/'MAPPING_SEMANTICS.md',W/'.claude/skills/add-media/SKILL.md',W/'.claude/skills/curate-yaml-record/SKILL.md',W/'.claude/skills/curate-yaml-record/references/review-checklist.md',W/'src/mediaingredientmech/schema/mediaingredientmech.yaml',W/'src/mediaingredientmech/validation/write_validated.py',B/'final-correction-v1/chemicals/new-tris-components-finding-v1.json',T/'ASSESSMENT.json',T/'new-tris-components-finding-v1.json']:
 ledger.append(dict(**bind(p),scope='Applicable native contract or complete finding/assessment; schema native validation performed.'))
for p in sorted((S/'captures').glob('*')):ledger.append(dict(**bind(p),scope='Complete Tris primary source/text read; NBRC sources context-only, no HEPES authorship.'))
for p in sorted((S/'selected-payloads').glob('*')):ledger.append(dict(**bind(p),scope='Complete current selected payload read; no fields mutated.'))
for p in sorted((S/'historical-before').glob('*')):ledger.append(dict(**bind(p),scope='Complete historical before payload read and compared; original component objects preserved.'))
put(S/'source-read-ledger.json',dict(at=AT,scientist=AUTHOR,reads=ledger,frozen_recipe_contexts=sources,capture_acquisition_times=capture_index,scope='Scientific source applicability and current complete-payload assessment; parsing/validation is distinct from science, and counts imply no release.'))
put(S/'summary.json',dict(at=datetime.now(timezone.utc).isoformat(),author=AUTHOR,status='READY_FOR_INDEPENDENT_REVIEW',base=BASE,selected=dict(decisions=bind(S/'decisions.json'),proposals=bind(S/'proposals.json'),evidence=bind(S/'evidence.json')),case_reviews=[dict(case_id=CID,selected_decision_object_sha256=OBJ(D),assessment=science['conclusion'])],payload_reviews=[dict(proposal_id=p['proposal_id'],after_capture=p['after_capture'],selected_proposal_object_sha256=OBJ(p),assessment='Full current source-defined Tris stock payload already omits unsupported material components/assertion and preserves nominal stock specification, original history and claim-specific LLM provenance; retained byte-identical.') for p in PS],changed_payloads=0,changed_proposal_objects=0,changed_decisions=1,additive_evidence=len(add),guarded_validation='PASS',strict_validation='PASS',new_findings=[],chronology=bind(S/'chronology.json')))
print(json.dumps(dict(status='READY_FOR_INDEPENDENT_REVIEW',case_count=1,proposals=2,changed_payloads=0,evidence=len(add),summary_sha256=SHA(S/'summary.json'))))
