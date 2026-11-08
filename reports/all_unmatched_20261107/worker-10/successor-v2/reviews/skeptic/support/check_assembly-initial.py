import datetime,hashlib,json,sys
from pathlib import Path

R=Path.cwd(); A=R/'reports/all_unmatched_20261107/worker-10'; S=A/'successor-v2'; C=R.parents[2]; Q=C/'queue/preliminary-v5'; P=R/'.temp/all-unmatched-worker-10/successor-v2/skeptic'
core=S/sys.argv[1]; out=P/sys.argv[2]
assert not out.exists(),out
J=lambda p:json.loads(Path(p).read_text())
H=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
CH=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
checks=[]
def ck(name,ok,detail=None):checks.append({'check':name,'pass':bool(ok),'detail':detail})
cases=J(Q/'shards/shard-10.json')['cases']
new={k:J(core/(k+'.json'))[k] for k in ['decisions','proposals','evidence']}
old={k:J(A/'successor-v1'/(k+'.json'))[k] for k in new}
keys={'decisions':'case_id','proposals':'proposal_id','evidence':'evidence_id'}
nd={k:{x[keys[k]]:x for x in v} for k,v in new.items()}; od={k:{x[keys[k]]:x for x in v} for k,v in old.items()}
for k in new:ck('unique '+k,len(nd[k])==len(new[k]))
changed=[i for i,x in enumerate(cases) if od['decisions'][x['case_id']]!=nd['decisions'].get(x['case_id'])]
ck('same188case IDs',len(new['decisions'])==188 and set(nd['decisions'])==set(od['decisions'])=={x['case_id'] for x in cases})
ck('onlycase143187 changed',changed==[143,187],changed)
ck('all188fullsourcecase digests',all(x['case_input_sha256']==CH(cases[x['source_index']]) for x in new['decisions']))
ck('case21 exact preserved',nd['decisions'][cases[21]['case_id']]==od['decisions'][cases[21]['case_id']])
occold={v for x in old['decisions'] for v in x['occurrence_ids']};occnew={v for x in new['decisions'] for v in x['occurrence_ids']}
ck('304wholecaseoccurrencespreserved',occold==occnew and len(occnew)==304,len(occnew))
for d in new['decisions']:
 ck('decision proof and no release '+d['case_id'],set(d['evidence_ids'])<=set(nd['evidence']) and set(d['proposal_ids'])<=set(nd['proposals']) and d.get('release_authorization') is False)
for i,g in [(143,'isp4'),(187,'carbonate')]:
 frag=J(S/g/'decision-fragment.json');fin=nd['decisions'][cases[i]['case_id']]
 diff=[k for k in set(frag)|set(fin) if frag.get(k)!=fin.get(k)]
 ck('root changes only review/evidence/issue metadata for'+str(i),set(diff)<={'independent_review','evidence_ids','issue_refs'},diff)
 ck('prior evidence preserved'+str(i),set(frag['evidence_ids'])<=set(fin['evidence_ids']))
 ck('prior issue refs preserved'+str(i),set(frag['issue_refs'])<=set(fin['issue_refs']))
ip='sv2-isp4-jcm58-complete-formulation'; prior='kg-isp4-remove-salt-parent'; cp='sv1-buffers-carbonate_co2_nominal4percent_togo_m202'
ck('128selectedproposals oldISP replaced once',len(new['proposals'])==128 and set(nd['proposals'])==set(od['proposals'])-{prior}|{ip})
preserved=[k for k in od['proposals'] if k!=prior and nd['proposals'][k]==od['proposals'][k]]
ck('126otherproposalobjectsexact',len(preserved)==126 and cp not in preserved,len(preserved))
samepayload=[k for k in od['proposals'] if k!=prior and nd['proposals'][k]['after_capture']==od['proposals'][k]['after_capture']]
ck('127otherpayloadbindingsunchanged',len(samepayload)==127,len(samepayload))
for frag in [J(S/'isp4/proposals-fragment.json')['proposals'][0],J(S/'carbonate/proposal-fragment.json')]:
 fin=nd['proposals'][frag['proposal_id']];diff=[k for k in set(frag)|set(fin) if frag.get(k)!=fin.get(k)]
 ck('root changes only proposal review/evidence metadata '+frag['proposal_id'],set(diff)<={'independent_review','evidence_ids'},diff)
 ck('proposal original evidence retained '+frag['proposal_id'],set(frag['evidence_ids'])<=set(fin['evidence_ids']))
for p in new['proposals']:
 ck('proposal backlinks '+p['proposal_id'],set(p['case_ids'])<=set(nd['decisions']) and all(p['proposal_id'] in nd['decisions'][i]['proposal_ids'] for i in p['case_ids']) and set(p['evidence_ids'])<=set(nd['evidence']))
ck('1140 original evidence exact',len(od['evidence'])==1140 and all(nd['evidence'].get(k)==v for k,v in od['evidence'].items()))
frags=J(S/'isp4/evidence-fragment.json')['evidence']+J(S/'carbonate/evidence-fragment.json')['evidence']
ck('19primaryfragment evidence exact',len(frags)==19 and all(nd['evidence'].get(x['evidence_id'])==x for x in frags))
capture_bindings={}
for x in new['evidence']+new['proposals']:
 capt=x.get('capture',x.get('after_capture'))
 if not capt:continue
 root={'artifact':A,'source':Q,'repository':R,'repo':R}[capt['root']];p=root/capt['path']
 try:sha=H(p)
 except Exception as e:sha=repr(e)
 ck('exact capture '+x.get('evidence_id',x.get('proposal_id')),sha==capt['sha256'],None if sha==capt['sha256'] else {'path':str(p),'expected':capt['sha256'],'actual':sha})
 capture_bindings[str(p)]=sha
owners={x['path']:x['sha256'] for d in new['decisions'] for x in d.get('owner_records',[])}
ck('273uniqueauthenticowners',len(owners)==273,len(owners))
for p,h in owners.items():ck('owner preimage '+p,H(R/p)==h)
receipt={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'core_directory':str(core),'core_hashes':{k:H(core/(k+'.json')) for k in new},'old_core_hashes':{k:H(A/'successor-v1'/(k+'.json')) for k in old},'check_count':len(checks),'checks':checks,'failures':[x for x in checks if not x['pass']],'counts':{'cases':len(new['decisions']),'changed_decisions':len(changed),'unchanged_decisions':len(new['decisions'])-len(changed),'proposals':len(new['proposals']),'unchanged_proposal_objects':len(preserved),'unchanged_payloads':len(samepayload),'evidence_objects':len(new['evidence']),'original_evidence_objects':len(old['evidence']),'new_evidence_objects':len(new['evidence'])-len(old['evidence']),'case_occurrence_ids':len(occnew),'owner_preimages':len(owners),'distinct_capture_files_rehashed':len(capture_bindings)},'capture_bindings':capture_bindings,'unchanged_decision_ids':[k for k in od['decisions'] if od['decisions'][k]==nd['decisions'][k]],'changed_decision_object_hashes':{cases[i]['case_id']:CH(nd['decisions'][cases[i]['case_id']]) for i in changed},'limitation':'Full accounting is deterministic preservation/referential verification, not renewed science approval of unchanged cases/payloads.'}
out.write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'sha256':H(out),'checks':len(checks),'failures':receipt['failures'],'counts':receipt['counts']}))
