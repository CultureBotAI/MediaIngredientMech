from pathlib import Path
import json,hashlib,subprocess,datetime,importlib.util,sys,yaml,copy
W=Path.cwd(); C=W.parents[2]; O=W/'.temp/ebios-no-install-v1/lineage'; A=C/'workers/w08/worktree/.temp/ebios-candidate-independent-v1'; H='0c659aa4c121a5b1832bff699c28e30da577ca08';R=Path('reports/all_unmatched_20261107/worker-02')
sha=lambda b:hashlib.sha256(b).hexdigest()
canon=lambda x:sha(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode())
checks=[];refs=[]
def check(n,ok,detail=None):
 checks.append({'check':n,'passed':bool(ok),'detail':detail})
 if not ok:raise AssertionError(n)
def read(p):
 p=Path(p);b=p.read_bytes();refs.append({'path':str(p),'sha256':sha(b)});return b
def obj(p):return json.loads(read(p))
def dump(n,x):
 p=O/n
 if p.exists():raise RuntimeError('refuse existing '+str(p))
 p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def git(repo,p,h):return subprocess.check_output(['git','-C',str(repo),'show',h+':'+str(p)])
check('current_w02_exact_head',subprocess.check_output(['git','rev-parse','HEAD']).decode().strip()==H)
core={}; coreproof=[]
for f in ['decisions','proposals','evidence']:
 p=R/'seven-preparation-types-v1/selected-v3'/f'{f}.json';b=git(W,p,H);current=read(W/p);check('committed_current_core_'+f,b==current);core[f]=json.loads(b)[f];coreproof.append({'name':f,'path':str(p),'head':H,'sha256':sha(b),'count':len(core[f])})
check('core_counts',[len(core[k]) for k in ['decisions','proposals','evidence']]==[188,117,1830])
frozen=obj(C/'queue/preliminary-v5/shards/shard-02.json')['cases'];check('exact_case_order',[x['case_id'] for x in frozen]==[x['case_id'] for x in core['decisions']])
caseproof=[]
for f,d in zip(frozen,core['decisions']):
 check('case_hash_'+d['case_id'],canon(f)==d['case_input_sha256'])
 ids=[o['occurrence_id'] for o in f.get('occurrences',[])];check('occurrences_'+d['case_id'],ids==d['occurrence_ids'])
 source={k:f[k] for k in ['source','source_case_id','source_label','raw_source_label']};check('raw_source_'+d['case_id'],source==d['source'])
 caseproof.append({'case_id':d['case_id'],'case_input_sha256':canon(f),'decision_sha256':canon(d),'source':source,'occurrence_ids':ids,'full_occurrences_sha256':canon(f.get('occurrences',[]))})
check('occurrence_total',sum(len(x['occurrence_ids']) for x in caseproof)==322)
props=[]
for p in core['proposals']:
 cap=p['after_capture'];check('artifact_payload_'+p['proposal_id'],cap['root']=='artifact');path=R/cap['path'];b=git(W,path,H);c=read(W/path);check('payload_exact_'+p['proposal_id'],b==c and sha(b)==cap['sha256']);props.append({'proposal_id':p['proposal_id'],'proposal_sha256':canon(p),'payload_path':str(path),'payload_sha256':sha(b),'kind':p['kind'],'before_sha256':p.get('before_sha256'),'case_ids':p['case_ids']})
p=next(p for p in core['proposals'] if p['proposal_id']=='a2-proposal-nbrc1132-asahi-ebios-tablets');d=next(d for d in core['decisions'] if d['case_id'] in p['case_ids']);check('exact_retired_proposal',canon(p)=='47b497f7e9b2f764683bddb7479a891be28fa772716d84dd127238033fb34587');check('genuine_new_origin',p['kind']=='new_owner' and p['before_sha256'] is None)
origins=[]
for slot in ['w01','w02','w06']:
 origin=obj(A/f'inputs/origins/{slot}.json');check('origin_object_'+slot,canon(origin['proposal'])==origin['proposal_object_sha256']);origins.append({k:origin[k] for k in ['origin_id','selected_head','proposal_object_sha256','payload_sha256','case_hashes','occurrence_ids']});origins[-1]['kind']=origin['proposal']['kind'];origins[-1]['before_sha256']=origin['proposal'].get('before_sha256')
 if slot=='w02':check('w08_preserved_w02_full_case_and_proposal',origin['proposal']==p and origin['cases']==[d])
manifest=obj(A/'MANIFEST.json'); mproof=[]
for m in manifest['members']:
 path=A/m['path'];check('w08_member_'+m['path'],not path.is_symlink() and sha(path.read_bytes())==m['sha256']);mproof.append(m)
for m in manifest['literal_symlinks_not_followed']:
 path=A/m['path'];check('literal_symlink_'+m['path'],path.is_symlink() and str(path.readlink())==m['target'])
check('w08_manifest_expected',sha((A/'MANIFEST.json').read_bytes())=='afa45f56ebe1b4eea86a8dde3597bd1f9f156b497ea1275c1a91a12158398b96')
reviewfiles=['HANDOFF.json','science/review.json','science/source-read-ledger.json','skeptic/review-v2.json','skeptic/source-read-ledger.json','technical/review.json','technical/final-assembly.json','native-validation.json']
reviews={n:obj(A/n) for n in reviewfiles}
base=C/'integration/ebios-reconciliation-v1';candidate=yaml.safe_load(read(base/'publication-v1/candidates/EBIOS.yaml'));before=yaml.safe_load(read(base/'inputs/before/EBIOS.yaml'));check('authentic_three_history_prefix',len(before['curation_history'])==3 and candidate['curation_history'][:3]==before['curation_history']);check('w02_event_preserved',yaml.safe_load((W/R/p['after_capture']['path']).read_bytes())['curation_history'][0] in candidate['curation_history']);check('all_nine_history_events',len(candidate['curation_history'])==9)
for n in ['SELECTOR.json','publication-v1/trace.json','HANDOFF.json']:obj(base/n)
conf=obj(C/'integration/final-native-intake-v1/native-origin-kind-preimage-conflicts.json');check('conflict_expected',sha((C/'integration/final-native-intake-v1/native-origin-kind-preimage-conflicts.json').read_bytes())=='2b691533c6ee0f394af8cbcf70b785879ff09b43610e67fc837fdfa26c2f885b')
for n in ['issue1237-comment6720520960.json','issue-comment-read-receipt.json','issue-comment-read-receipt-retry-v1.json']:obj(O.parent/'inputs'/n)
# Native pair: actual complete data read, exact renderer/schema/parser; no saver and no root override.
AW=A.parents[1]; ny=A/'native/reviews/structured/20261108T104110Z-w08-ebios-candidate-independent/review.yaml';nm=ny.with_suffix('.md'); raw=read(ny);md=read(nm);n=yaml.safe_load(raw)
spec=importlib.util.spec_from_file_location('ebios_lineage_native',AW/'scripts/record_review.py');mod=importlib.util.module_from_spec(spec);sys.modules[spec.name]=mod;spec.loader.exec_module(mod)
mod.validate_review(n);check('native_render_exact',mod.render_markdown(n).encode()==md);mod.parse_review_bundle('reviews/structured/'+n['review_id']+'/review.yaml',raw,md)
ninputs=[]
for item in n['source']['inputs']:
 b=(AW/item['path']).read_bytes();check('native_input_'+item['path'],sha(b)==item['sha256']);ninputs.append(item)
mod.assert_current_source(AW,n);check('native_current_source_pass',True)
for label,mut in [('render_mismatch',lambda:mod.parse_review_bundle('reviews/structured/'+n['review_id']+'/review.yaml',raw,md+b'bad')),('input_hash_mismatch',None)]:
 try:
  if mut:mut()
  else:
   altered=copy.deepcopy(n);altered['source']['inputs'][0]['sha256']='0'*64;mod.assert_current_source(AW,altered)
 except Exception as e:check('negative_'+label,True,str(e))
 else:check('negative_'+label,False)
for doc in [reviews['science/review.json'],reviews['skeptic/review-v2.json']]:check('review_candidate_'+doc.get('reviewer_identity',doc['reviewer']),doc['candidate']['sha256']==sha((base/'publication-v1/candidates/EBIOS.yaml').read_bytes()))
check('native_single_candidate',len(n['targets'])==1 and n['scope']['population_size']==1)
check('no_install_context_only',n['scientific_review'] is True and reviews['technical/final-assembly.json']['scientific_review'] is False)
dump('cohort-continuity-v1.json',{'head':H,'core':coreproof,'cases':caseproof,'proposals':props,'evidence':[{'evidence_id':e['evidence_id'],'complete_object_sha256':canon(e),'accessed_at':e.get('accessed_at')} for e in core['evidence']],'scope':'Complete byte/accounting continuity only; no scientific reassessment.'})
dump('original-ebios-binding-v1.json',{'proposal':p,'proposal_sha256':canon(p),'decision':d,'decision_sha256':canon(d),'frozen_case':next(f for f in frozen if f['case_id']==d['case_id']),'origins_context_only':origins})
dump('family-chain-verification-v1.json',{'candidate_sha256':sha((base/'publication-v1/candidates/EBIOS.yaml').read_bytes()),'before_sha256':sha((base/'inputs/before/EBIOS.yaml').read_bytes()),'manifest_members':mproof,'native_inputs':ninputs,'native_pair':{'yaml_sha256':sha(raw),'markdown_sha256':sha(md)},'actual_methods':['validate_review','render_markdown','parse_review_bundle','direct_all_input_hashes','assert_current_source'],'new_science':False,'fresh_remote_check':False})
dump('intake-checks-v1.json',{'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reviewer':'worker02:/root/research_c','checks':checks,'passed':sum(x['passed'] for x in checks),'input_hash_manifest':list({x['path']:x for x in refs}.values()),'scope':'Native metadata/lineage and full W02 continuity; not new source or chemical review.'})
print(json.dumps({'checks':len(checks),'passed':sum(x['passed'] for x in checks),'w08_manifest_members':len(mproof),'native_inputs':len(ninputs),'output':str(O)}))
