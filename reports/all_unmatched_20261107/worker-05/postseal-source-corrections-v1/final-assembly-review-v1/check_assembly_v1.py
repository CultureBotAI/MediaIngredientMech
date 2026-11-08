from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,copy,importlib.util,yaml
S=Path('.temp/w05-postseal-source-corrections-v1');O=S/'final-assembly-review-v1';B=Path('reports/all_unmatched_20261107/worker-05');P=B/'postseal-source-corrections-v1';OLD=B/'final-correction-v1';Q=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5');N=Path('reviews/structured/20261108T084639Z-worker05-postseal-source-corrections')
def j(p):return json.loads(Path(p).read_text())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def obj(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
def rows(p,k):
 x=j(p);return x if isinstance(x,list) else x[k]
def bind(p):return {'path':str(p),'sha256':sha(p)}
D=rows(P/'core/decisions.json','decisions');PS=rows(P/'core/proposals.json','proposals');E=rows(P/'core/evidence.json','evidence');oldD=rows(OLD/'core/decisions.json','decisions');oldP=rows(OLD/'core/proposals.json','proposals');oldE=rows(OLD/'core/evidence.json','evidence');peer=j(P/'review/main-review.json');ds={d['case_id']:d for d in D};ps={p['proposal_id']:p for p in PS};ods={d['case_id']:d for d in oldD};ops={p['proposal_id']:p for p in oldP};fd={};fp={}
for lane in ['materials','media','chemicals']:
 fd.update({d['case_id']:(d,lane) for d in rows(P/lane/'decisions.json','decisions')});fp.update({p['proposal_id']:p for p in rows(P/lane/'proposals.json','proposals')})
assert set(ds)==set(ods);assert set(ps)==set(ops);assert E[:len(oldE)]==oldE;assert len({e['evidence_id'] for e in E})==len(E)
casechecks=[]
for cid,d in ds.items():
 old=ods[cid]
 for k in ['case_input_sha256','source','occurrence_ids','preserved_source_holds','preserved_downstream_holds','owner_records','proposal_ids','disposition']:assert d.get(k)==old.get(k),(cid,k)
 if cid not in fd:assert d==old;continue
 f,lane=fd[cid];r=next(x for x in peer['case_reviews'] if x['case_id']==cid);assert obj(f)==r['selected_decision_object_sha256'];p=d['postseal_assembly_provenance'];assert p['selected_decision_object_sha256']==obj(f);assert p['predecessor_decision_object_sha256']==obj(old);assert sha(p['selected_fragment_path'])==p['selected_fragment_sha256'];assert d['previous_independent_review']==old['independent_review']
 for k,v in f.items():
  if k not in ['independent_review','evidence_ids']:assert d[k]==v,(cid,k)
 assert set(d)-set(f)=={'previous_independent_review','postseal_assembly_provenance'}
 expect=f['evidence_ids']+['POSTSEAL-INDEPENDENT-SCIENTIFIC-REVIEW']
 if d['case_index']==91:expect+=['POSTSEAL-ROOT-FAMILY-LEDGER-SUCCESSOR']
 assert d['evidence_ids']==list(dict.fromkeys(expect));assert d['independent_review']['status']=='complete';assert d['independent_review']['reviewer']=='/root/final_skeptical';casechecks.append({'case_id':cid,'authored_object_sha256':obj(f),'canonical_object_sha256':obj(d),'scientific_fields_equal':True,'assembly_delta':'Independent review receipt/evidence links and explicit predecessor/current provenance only.'})
for p in PS:
 if p['proposal_id'] in fp:assert p==fp[p['proposal_id']]
 else:assert p==ops[p['proposal_id']]
 assert sha(B/p['after_capture']['path'])==p['after_capture']['sha256']
 assert set(p['case_ids'])<=set(ds)
# Every evidence capture: original bytes/retrieval metadata preserved; exact root-relative sources.
capchecks=[]
for e in E:
 c=e['capture'];path=(Q if c['root']=='source' else B)/c['path'];assert sha(path)==c['sha256'],(e['evidence_id'],str(path));capchecks.append({'evidence_id':e['evidence_id'],'capture':c})
# Final checks report exact inputs, not a different earlier proposal set.
vi=j(P/'validation/validated-input-binding.json');assert (P/'core/proposals.json').read_bytes()==Path(vi['validated_input']['path']).read_bytes();assert sha(P/'core/proposals.json')==vi['selected_proposals']['sha256'];nv=j(P/'validation/final-overlay/native-validation.json');strict=j(P/'validation/final-strict/receipt.json');assert nv['status']=='PASS' and nv['candidate_payloads']==len(PS) and nv['overlay_records']==3029;assert not nv['partonomy_violations'];assert not nv['new_identifier_collisions'];assert not nv['filename_case_collisions'];assert not nv['filename_case_drift'];assert strict['exit_code']==0 and strict['payloads']==len(PS);assert nv['inputs']['proposals']['sha256']==sha(P/'core/proposals.json');assert strict['input_proposals_sha256']==sha(P/'core/proposals.json')
# Native exact content and rendered companion; all20 source inputs and all evidence references authenticated.
n=yaml.safe_load((N/'review.yaml').read_text());spec=importlib.util.spec_from_file_location('record_review','scripts/record_review.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);mod.validate_review(n);mod.assert_current_source(Path.cwd(),n);assert mod.render_markdown(n)==(N/'review.md').read_text()
assert len(n['targets'])==15 and n['scope']['population_size']==15;assert n['verdict']=='needs_curation';assert n['reviewer']['independence']=='self_review';targets={x['target_id']:x for x in n['targets']};ass={x['target_ids'][0]:x for x in n['assessments']};assert set(targets)==set(ass)==set(n['scope']['reviewed_target_ids'])
for r in peer['case_reviews']:
 t='CASE-'+str(r['case_index']).zfill(3);assert targets[t]['selector']==r['case_id'];assert ass[t]['summary']==r['assessment'];assert json.loads(ass[t]['details'][ass[t]['details'].index('{'):])==r
for r in peer['payload_reviews']:
 t=r['proposal_id'];assert sha(targets[t]['path'])==r['after_capture']['sha256'];assert ass[t]['summary']==r['assessment'];assert json.loads(ass[t]['details'][ass[t]['details'].index('{'):])==r
child=j(P/'review/family-audit/main-review.json');tr=next(x for x in child['payload_assessments'] if x['proposal_id']=='CHEM-C1193-Tris-HCl-salt');assert tr['read_scope']=='full_record_scientific_review';assert targets['CHEM-C1193-Tris-HCl-salt']['path']==tr['payload']['path'];assert sha(tr['payload']['path'])==tr['payload']['sha256'];assert ass['CHEM-C1193-Tris-HCl-salt']['evidence_ids']==['CHILD','TRIS'];assert sha(targets['FAMILY-TRACKER-APPLICABILITY']['path'])==child['findings'][0]['after']['sha256']
for e in n['evidence']:assert sha(e['reference'])==e['snapshot_sha256']
for x in n['source']['inputs']:assert sha(x['path'])==x['sha256']
# Originalregister preserved withnewscopedaddendum, no historicaldispositionrewrite.
fr=j(P/'finding-register.json');oldfr=j(OLD/'finding-register.json');assert {k:v for k,v in fr.items() if k!='postseal_successor'}==oldfr
# README exact bounded correction.
readme=(P/'README.md').read_text();before=(O/'README-before-finding-001.md').read_text();assert readme==before.replace('UN8','180').replace('UN5','137');assert 'UN8' not in readme and 'UN5' not in readme
counts=j(P/'final-counts.json');assert counts['cases']==len(D)==188;assert counts['candidate_payloads']==len(PS)==142;assert counts['evidence_entries']==len(E)==1551;assert counts['occurrence_memberships']==sum(len(d['occurrence_ids']) for d in D)==388;assert counts['unchanged_cases']==180;assert counts['unchanged_payloads']==137
r={'reviewer':'/root/final_skeptical','at':datetime.now(timezone.utc).isoformat(),'status':'PASS','scope':'Independent exact-byte final core/native/README assembly checks; scientific source/payload judgments remain in sealed peer packet and separately attributed child receipt.','counts':{'decisions':len(D),'proposals':len(PS),'evidence':len(E),'old_evidence_objects_unchanged':len(oldE),'changed_decisions':len(casechecks),'changed_payloads':len(fp),'unchanged_decisions':len(D)-len(casechecks),'unchanged_payloads':len(PS)-len(fp),'occurrence_memberships':sum(len(d['occurrence_ids']) for d in D),'native_targets':len(n['targets']),'native_source_hashes_checked':len(n['source']['inputs']),'evidence_captures_checked':len(capchecks)},'case_assembly_checks':casechecks,'checks':['All canonical scientific fields exactly equal reviewed authored fragments; only declared review/evidence/provenance metadata added.','All137unchangedproposal objects and180unchangeddecision objects equal predecessor. All1551evidence capture bytes rehashed;1537oldobjects including acquisition metadata exactprefix.','Native15targets and summaries/details bind actual8case/5payload review objects plus separateCHILD/TRIS/family scopes. Full nativeYAML/schema/source hashes and exact markdown render pass.','Full142 guarded/schema/strict/3029overlay receipts use canonical proposal bytes. No introduced partonomy/identifier/filename error.','Originalfindingregister remains exact with one additive postseal object; no historical finding disposition revised.','README only corrected two placeholder tokens to independently derived180/137; no scientific/provenance expansion.'],'inputs':[bind(P/'core'/f) for f in ['decisions.json','proposals.json','evidence.json','proposal-lineage.json','assembly-receipt.json']]+[bind(P/f) for f in ['README.md','finding-register.json','final-counts.json','source-ledger.json']]+[bind(N/'review.yaml'),bind(N/'review.md'),bind(P/'review/main-review.json'),bind(P/'review/family-audit/main-review.json')],'finding_rereview':{'finding_id':'W05-POSTSEAL-ASSEMBLY-REVIEW-001','status':'resolved_in_exact_readme_successor','before':bind(O/'README-before-finding-001.md'),'after':bind(P/'README.md'),'remediation':bind(P/'report-remediation-v1/remediation-receipt-v1.json'),'assessment':'Exactly UN8→180 andUN5→137, supportedbyindependentobjectcomparison; core/native/source unchanged.'},'limitations':['Full retained-native bundle check receipt still separately root-owned; final seal awaits its result.','Separate preservation child is auditing full oldpublished history, manifests and source ownership; this receipt does not substitute hashes for its actual scope.','No publishedhead inferred before ordinarycommit/push; no owner/export approval.']};p=O/'assembly-checks-v1.json';assert not p.exists();p.write_text(json.dumps(r,indent=2)+'\n');print(sha(p));print(r['counts'])
