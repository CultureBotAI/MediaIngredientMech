from pathlib import Path
import json,hashlib,datetime
r=Path('.temp/w05-tellurium-polypeptone-v1/review');s=r.parent;p=s/'polypeptone';t=s/'tellurium';b=Path('reports/all_unmatched_20261107/worker-05/postseal-source-corrections-v1/core')
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
def osh(v):return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
def read(f):return json.loads(f.read_text())
def bind(f):return {'path':str(f),'sha256':sha(f)}
verified=[]
for d,name in [(p,'MANIFEST.json'),(t,'FINAL-MANIFEST-v1.json')]:
 j=read(d/name);members=j.get('files',j.get('members'))
 for f in members:
  q=d/f['path'];assert sha(q)==f['sha256'],q
 verified.append({'manifest':bind(d/name),'members_verified':len(members)})
a={v['evidence_id']:v for v in read(p/'evidence.json')['evidence']};bb=read(p/'evidence-v2.json')['evidence'];z={v['evidence_id']:v for v in bb};ids={k for k in a if a[k]!=z[k]}
assert ids=={'SUPPLEMENT-POLY-CAP-JCM2-HTML','SUPPLEMENT-POLY-CAP-JCM98-HTML'}
for k in ids:
 assert {x for x in z[k]if z[k][x]!=a[k].get(x)}=={'kind','locator','supports_or_contradicts'};assert z[k]['kind']=='unsuccessful_search'
assert (r/'polypeptone-evidence-before-review001.json').read_bytes()==(p/'evidence.json').read_bytes()
ee=[]
for e in bb:
 f=s/str(Path(e['capture']['path']).relative_to('tellurium-polypeptone-v1'));assert sha(f)==e['capture']['sha256']
 x={'evidence_id':e['evidence_id'],'kind':e['kind'],'object_sha256':osh(e),'capture':e['capture'],'supports_or_contradicts':e['supports_or_contradicts'],'exact_capture_binding':True}
 if e.get('receipt'):
  rf=s/str(Path(e['receipt']['path']).relative_to('tellurium-polypeptone-v1'));assert sha(rf)==e['receipt']['sha256'];rc=read(rf);assert rc['accessed_at']==e['accessed_at'];assert rc['url']==e['url'];x['original_receipt_and_retrieval_time_verified']=True
 ee.append(x)
base={d['case_id']:d for d in read(b/'decisions.json')['decisions']};cases=[]
for d in read(p/'decisions-v2.json')['decisions']:
 o=base[d['case_id']];ks=['case_id','case_input_sha256','source','occurrence_ids','disposition','proposal_ids','owner_records','preserved_downstream_holds','preserved_source_holds'];assert all(d.get(k)==o.get(k)for k in ks)
 assert d['pre_supplement_independent_review']==o['independent_review'];cases.append({'case_id':d['case_id'],'case_index':d['case_index'],'selected_decision_object_sha256':osh(d),'baseline_object_sha256':osh(o),'exact_preserved_fields':ks,'prior_review_preserved_exactly':True})
po=read(p/'proposals-v2.json')['proposals'][0];assert po['after_capture']['sha256']==sha(p/'proposed/Polypeptone.yaml')
native=read(r/'independent-polypeptone-native-v1.json');author=read(p/'native-options.json');assert native['selected_rows']==author['selected_after_rows'];assert native['prior_rows']==author['before_rows']
for k,v in [('foodon_parent_if_source_scope_settled_no_exact_term','conditional_foodon_rows'),('micro_exact_if_BD_blend_scope_established','conditional_micro_rows')]:
 for x,y in zip(native['in_memory_unselected_options'][k],author[v]): assert all(x[f]==y[f]for f in x if f!='source')
o={'reviewer':'/root/final_skeptical','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Exact final scientific input/authentication and report-remedy rereview; scientific assessments are in main-review.json and independently attributed child receipt. Hash equality is not chemical approval.','verified_author_manifests':verified,'selected_fragment_bindings':[bind(p/x)for x in ['proposals-v2.json','decisions-v2.json','evidence-v2.json','proposed/Polypeptone.yaml','context-ledger-v2.json','source-assessment.json','conditional-grounding-matrix.json','findings.json','source-read-ledger.json','native-options.json','review001-remediation.json','HANDOFF.md']],'polypeptone_case_bindings':cases,'polypeptone_proposal_object_sha256':osh(po),'review001_rereview':{'finding_id':'W05-TELLURIUM-POLYPEPTONE-REVIEW-001','status':'resolved_in_exact_report_successor','before':bind(p/'evidence.json'),'after':bind(p/'evidence-v2.json'),'changed_existing_evidence_ids':sorted(ids),'unchanged_existing_objects':len(a)-len(ids),'new_final_report_bindings':len(z)-len(a),'assessment':'Both complete JCM captures explicitly say Nothing found. The successor now types only those endpoints unsuccessful_search and states no identity/formulation support. Same capture bytes, URLs, original timestamps and linked case IDs remain; independent successful TOGO/MediaDive evidence and full payload are unchanged. Eight additive final-report bindings accurately distinguish source-ledger/assessment/native diagnostics/failure receipts. No additional correction required.'},'all_final_evidence_reference_checks':ee,'native_crosscheck':'Main independent selected and predecessor rows equal author output with full shadow owner index; conditional rows agree in every field except deliberate source evidence additions on author options. These remain unselected diagnostics.'}
out=r/'final-science-inputs-rereview-v1.json';assert not out.exists();out.write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n');print(out,sha(out));print('cases',[(d['case_index'],d['selected_decision_object_sha256'])for d in cases]);print('Pobject',osh(po));print('manifests',verified)
