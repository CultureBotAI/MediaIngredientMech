from pathlib import Path
import json,hashlib,datetime,copy,importlib.util
R=Path('reports/all_unmatched_20261107/worker-08');S=R/'successors/issue-1227-v1';M=S/'research/vitamins_mixtures';V=M/'final-v2';W=M/'final-v3'
def h(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(Path(p).read_text())
def cap(p):return {'root':'artifact','path':str(Path(p).relative_to(R)),'sha256':h(p)}
def save(n,a):
 p=W/n;assert not p.exists();p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
now=datetime.datetime.now(datetime.timezone.utc).isoformat();allv2={str(p.relative_to(R)):h(p) for p in V.rglob('*') if p.is_file()};routing=S/'COORDINATOR-ASSEMBLY-FINDING-v1.json';assert h(routing)=='0a4e836b89eb224e16e398876cd2296672cc23a35193ed2edf26cc8e39da09da'
old=read(V/'evidence-additions.json');new=copy.deepcopy(old);target='vm1227-v2-dl-ontology';r=next(e for e in new['evidence'] if e['evidence_id']==target);before=copy.deepcopy(r);assert r['kind']=='ontology' and r['url'] is None;r['kind']='local_validation'
assert len(old['evidence'])==len(new['evidence'])
for b,a in zip(old['evidence'],new['evidence']):
 if a['evidence_id']==target:assert {k:v for k,v in a.items() if k!='kind'}=={k:v for k,v in b.items() if k!='kind'}
 else:assert a==b
save('evidence-additions.json',new)
# Narrow application of the unchanged campaign auditor's evidence loop, without pretending to rerun full accounting.
auditor=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/scripts/audit_worker_outcomes_v1.py');spec=importlib.util.spec_from_file_location('native_auditor',auditor);a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
roots={'artifact':R.resolve(),'source':Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5').resolve()};inputs={};ids=set();passed=[]
for e in new['evidence']:
 key=a.string(e.get('evidence_id'),'evidence_id');a.require(key not in ids,'duplicate evidence_id');ids.add(key)
 a.require(e['kind'] in {'primary_source','source_snapshot','ontology','native_record_review','independent_review','unsuccessful_search','local_validation'},'unknown evidence kind');a.string(e.get('locator'),'evidence locator');a.string(e.get('supports_or_contradicts'),'evidence applicability');a.capture(e['capture'],roots,'evidence '+key,inputs)
 url=e.get('url');a.require(url is None or isinstance(url,str) and url.startswith(('https://','http://')),'evidence URL must be HTTP(S) or null')
 if url is not None:a.string(e.get('accessed_at'),'evidence access timestamp')
 if e['kind'] in {'primary_source','ontology'}:a.require(url is not None,'primary/ontology evidence URL required')
 passed.append(key)
assert all(h(R/p)==sha for p,sha in allv2.items())
D=read(V/'decisions.json');P=read(V/'proposals.json')
for p in P:assert h(R/p['after_capture']['path'])==p['after_capture']['sha256']
save('metadata-remediation.json',{'finding_id':'W08-1227-ASSEMBLY-001','coordinator_routing':cap(routing),'at':now,'author':'/root/vitamins','scope':'Metadata only; no scientific assertion, source URL/time, capture bytes, case, proposal or payload changes.','evidence_id':target,'before':before,'after':r,'reason':'The capture is a reproducible read-only local ChEBI/NCIt database query and adjudication receipt. local_validation accurately describes that local provenance. The current official OLS ontology response is separately bound with its original real URL and access time. No URL is invented for this local query.','predecessor_index':cap(V/'evidence-additions.json'),'successor_index':cap(W/'evidence-additions.json'),'all_final_v2_files_preserved':allv2,'selected_decisions':cap(V/'decisions.json'),'selected_proposals':cap(V/'proposals.json'),'case_count':len(D),'payload_count':len(P),'payload_hashes':{p['proposal_id']:p['after_capture']['sha256'] for p in P},'independent_review':'pending metadata successor review by /root/organics'})
save('metadata-validation.json',{'at':now,'status':'PASS','auditor_path':str(auditor),'auditor_sha256':h(auditor),'scope':'Unchanged auditor evidence-field/URL rules and native capture helper applied to all22 successor evidence rows. This is a focused metadata check, not full188 accounting, native schema or scientific review.','entries_checked':len(passed),'evidence_ids':passed,'exact_changed_field':'evidence[evidence_id=vm1227-v2-dl-ontology].kind: ontology -> local_validation','all_other_evidence_fields_unchanged':True,'all_final_v2_files_unchanged':True,'cases_unchanged':57,'payloads_unchanged':47,'full_root_accounting':'required separately after assembly'})
hand={'status':'frozen_metadata_successor_ready_for_peer','author':'/root/vitamins','version':'final-v3-metadata-only','at':now,'cases':57,'proposals':47,'changed_payloads':0,'selected_indices':{'decisions':cap(V/'decisions.json'),'proposals':cap(V/'proposals.json'),'evidence_additions':cap(W/'evidence-additions.json')},'preserved_scientific_handoff':cap(V/'HANDOFF.json'),'preserved_overlay_scope_addendum':cap(V/'validation-scope-addendum.json'),'operative_science_ledgers':'All final-v2 ledgers remain operative and unchanged; metadata-remediation.json changes only one evidence kind.','remediation':cap(W/'metadata-remediation.json'),'validation':cap(W/'metadata-validation.json'),'independent_review':'Full prior57/47 scientific receipt remains bound; /root/organics must inspect the exact metadata-only successor. Root full accounting remains required.'};save('HANDOFF.json',hand)
(W/'HANDOFF.md').write_text('Metadata-only successor for W08-1227-ASSEMBLY-001: vm1227-v2-dl-ontology now has kind local_validation, reflecting its actual local database query provenance. Every other field, original source access time and capture hash is unchanged. Select final-v2 decisions/proposals and final-v3 evidence-additions.json. All57 cases and47 payloads remain unchanged; full prior scientific review is preserved. Focused evidence metadata checks pass; root full accounting and peer metadata review remain required.\n\nHANDOFF.json SHA256: '+h(W/'HANDOFF.json')+'\n')
save('MANIFEST.json',{'files':{str(p.relative_to(W)):h(p) for p in W.rglob('*') if p.is_file() and p.name!='MANIFEST.json'}})
print(json.dumps({'handoff':h(W/'HANDOFF.json'),'evidence':h(W/'evidence-additions.json'),'metadata_validation':h(W/'metadata-validation.json'),'manifest':h(W/'MANIFEST.json')}))
