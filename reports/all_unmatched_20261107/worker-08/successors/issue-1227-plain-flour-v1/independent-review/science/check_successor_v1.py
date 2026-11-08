import pathlib, json, hashlib, sqlite3, datetime, yaml
R=pathlib.Path('.').resolve(); A=R/'reports/all_unmatched_20261107/worker-08'; N=A/'successors/issue-1227-plain-flour-v1'; O=R/'.temp/all-unmatched-worker-08/plain-flour-method-v1/independent/science'; checks=[]
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def check(n,v,detail=None):
 checks.append({'check':n,'passed':bool(v),'detail':detail})
 assert v,n
oldp=A/'successors/issue-1227-v1/research/organic_products/proposed_owners/Plain_Flour.yaml'; newp=N/'payloads/Plain_Flour.yaml'; old=yaml.safe_load(oldp.read_text()); new=yaml.safe_load(newp.read_text())
check('exact predecessor payload',h(oldp)=='aa8390f17f1ed9f9c083fd6b487ee1c40228e754072b7e390b97dfb2fd6eae83')
check('exact successor payload',h(newp)=='884fee1ea6a5082a51b8769f2a827199b1703972ad80fa48e1bb8d2d09ab3873')
check('exact authored assessment',h(N/'author/assessment.json')=='8b1a52dd7f6c592ec7894b77a7f8dad455dbc663dfe81d56cf33b8ea99339331')
for k in set(old)|set(new):
 if k not in ['preferred_term','notes','ontology_mapping','curation_history']:check('unchanged whole top-level field '+k,old.get(k)==new.get(k))
check('old five history events preserved exactly and one event added',len(new['curation_history'])==len(old['curation_history'])+1 and new['curation_history'][:-1]==old['curation_history'])
check('new event honestly LLM assisted and dated',new['curation_history'][-1]['llm_assisted'] is True and new['curation_history'][-1]['timestamp']=='2026-11-08T08:38:45.690887+00:00')
check('old notes retained as prefix',new['notes'].startswith(old['notes']))
for k in set(old['ontology_mapping'])|set(new['ontology_mapping']):
 if k!='evidence':check('unchanged ontology field '+k,old['ontology_mapping'].get(k)==new['ontology_mapping'].get(k))
check('original evidence source and category preserved',[(k,v) for k,v in new['ontology_mapping']['evidence'][0].items() if k!='notes']==[(k,v) for k,v in old['ontology_mapping']['evidence'][0].items() if k!='notes'])
check('interpretive mapping support separately typed',len(new['ontology_mapping']['evidence'])==2 and new['ontology_mapping']['evidence'][1]['evidence_type']=='LLM_SUGGESTION')
ols=json.loads((A/'successors/issue-1201-v1/shared-primary/ols-foodon-00004510.json').read_text())['_embedded']['terms'];check('unique active captured term primary label equality',len(ols)==1 and ols[0]['obo_id']==new['identifier'] and ols[0]['is_obsolete'] is False and new['preferred_term']==new['ontology_mapping']['ontology_label']==ols[0]['label']=='flour')
check('raw source label not represented as ontology synonym', 'Plain flour'.lower() not in [s.lower() for s in ols[0]['synonyms']])
lookup=json.loads((N/'research/primary-label-resolution.json').read_text());db=pathlib.Path(lookup['database']['path']);check('exact local ontology bytes',h(db)==lookup['database']['sha256'])
con=sqlite3.connect(db.as_uri()+'?mode=ro',uri=True);con.row_factory=sqlite3.Row; rows=[dict(r) for r in con.execute(lookup['sql'])];con.close();check('independent read-only native label/synonym query matches recorded rows',rows==lookup['rows'],rows)
olddec=json.loads((A/'successors/issue-1227-v1/final-v2/decisions.json').read_text()); oldprop=json.loads((A/'successors/issue-1227-v1/final-v2/proposals.json').read_text());
olddec=next(x for x in olddec['decisions'] if x['case_id']=='KG_CASE:b9a6261315d83792bc02bfbe425cda2032c8833c7a3b6de3aa665fa62a7fc03e');oldprop=next(x for x in oldprop['proposals'] if x['proposal_id']=='op1201-plain-flour'); nd=json.loads((N/'author/decision.json').read_text());np=json.loads((N/'author/proposal.json').read_text())
allowed_d={'reasoning','evidence_ids','issue_refs','independent_review','prior_independent_reviews','primary_reviewer'}
allowed_p={'description','evidence_ids','after_capture','publication_review_obligations'}
check('case changes limited to declared method provenance and review metadata',all(olddec.get(k)==nd.get(k) for k in (set(olddec)|set(nd))-allowed_d))
check('proposal changes limited to declared method provenance and obligations',all(oldprop.get(k)==np.get(k) for k in (set(oldprop)|set(np))-allowed_p))
check('original proposal obligations exact prefix',np['publication_review_obligations'][:len(oldprop['publication_review_obligations'])]==oldprop['publication_review_obligations'])
check('predecessor evidence references retained',nd['evidence_ids'][:len(olddec['evidence_ids'])]==olddec['evidence_ids'] and np['evidence_ids'][:len(oldprop['evidence_ids'])]==oldprop['evidence_ids'])
check('maintained beforeimage hash preserved',h(R/np['owner_path'])==np['before_sha256']=='becb2e4860868161607a709d6c4b5cbef56c2b4a3e06c9a4fc9214e35e4e9a8e')
check('successor after binding exact',np['after_capture']['sha256']==h(newp) and A/np['after_capture']['path']==newp)
paths=[oldp,newp,N/'author/assessment.json',N/'author/decision.json',N/'author/proposal.json',N/'research/primary-label-resolution.json',A/'successors/issue-1227-v1/final-v2/decisions.json',A/'successors/issue-1227-v1/final-v2/proposals.json',A/'successors/issue-1201-v1/shared-primary/ols-foodon-00001056.json',pathlib.Path(__file__).resolve()]
receipt={'reviewer':'worker08:/root/vitamins','author':'worker08:/root','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checks':checks,'all_passed':all(x['passed'] for x in checks),'input_hashes':{str(p.relative_to(R)):h(p) for p in paths},'limit':'These checks verify bounded changes and ontology lookup provenance. Source and material interpretation are assessed separately in the independent scientific review; this does not run or waive native admission/export gates.'}
p=O/'successor-exact-checks-v1.json';assert not p.exists();p.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'checks':len(checks),'all_passed':True,'path':str(p.relative_to(R)),'sha256':h(p)}))
