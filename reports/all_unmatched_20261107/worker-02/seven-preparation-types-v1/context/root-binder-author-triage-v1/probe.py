from pathlib import Path
import copy,datetime,hashlib,importlib.util,json,subprocess,sys
R=Path.cwd();C=R/'.temp/all-unmatched-20261107';W=C/'workers/w02/worktree';A=W/'reports/all_unmatched_20261107/worker-02';O=C/'preflight/w02-binder-author-triage-v1'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();J=lambda p:json.loads(p.read_text())
def put(p,x):
    with p.open('x')as f:json.dump(x,f,indent=2);f.write('\n')
def load(p,name):
    spec=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(spec);sys.modules[name]=m;spec.loader.exec_module(m);return m
rows=[];pins={};proof_states=[]
for packet,binder,proofname,sub in [('seven-preparation-types-v1','bind_review.py','scientific-review-v1.json','review-input-v1'),('seven-preparation-types-v1','bind_review_v2.py','scientific-review-v1.json','review-input-v1'),('filed-followups-v1','bind_review_v2.py','scientific-review-v2.json','review-input-v2')]:
    P=A/packet;build=P/'build_successor_v2.py';m_path=P/binder;proof_path=P/'independent'/proofname
    b=load(build,'build_successor_v2');m=load(m_path,'probe_'+packet.replace('-','_')+'_'+binder[:-3]);d=J(P/sub/'decisions.json');p=J(P/sub/'proposals.json');proof=J(proof_path)
    for f in [build,m_path,proof_path,P/sub/'decisions.json',P/sub/'proposals.json']:
        pins[str(f.relative_to(W))]=sha(f)
    result=m.validate(d,p,proof);rows.append({'packet':packet,'binder':binder,'control':'actual positive','accepted':True,'case_reviews':len(result[0]),'proposal_reviews':len(result[1])})
    proof_states.append({'packet':packet,'proof':str(proof_path.relative_to(W)),'sha256':sha(proof_path),'rows':[{'kind':k,'id':r.get('case_id',r.get('proposal_id')),'reviewer':r['reviewer'],'current_correction_author':r.get('current_correction_author'),'original_authors':r.get('original_authors'),'authorship_conflict':r['authorship_conflict']}for k in ['case_reviews','proposal_reviews']for r in proof[k]]})
    for k in ['case_reviews','proposal_reviews']:
        choices=['self','missing','unexpected']if packet.startswith('seven')else['self_original','missing_original','empty_original']
        for change in choices:
            x=copy.deepcopy(proof);v=x[k][0]
            if change=='self':v['current_correction_author']=v['reviewer']
            elif change=='missing':v.pop('current_correction_author')
            elif change=='unexpected':v['current_correction_author']='human reviewer'
            elif change=='self_original':v['original_authors']=['worker02 /root/final_reviewer']
            elif change=='missing_original':v.pop('original_authors')
            else:v['original_authors']=[]
            try:m.validate(d,p,x);accepted=True;error=None
            except(ValueError,KeyError)as exc:accepted=False;error=str(exc)
            rows.append({'packet':packet,'binder':binder,'collection':k,'control':change,'accepted':accepted,'error':error})
    if packet.startswith('seven'):
        x=copy.deepcopy(proof);x['proposal_reviews'][0]['original_authors']=['worker02 /root/final_reviewer']
        try:m.validate(d,p,x);accepted=True
        except ValueError:accepted=False
        assert not accepted;rows.append({'packet':packet,'binder':binder,'control':'old explicit original_authors self-negative remains','accepted':accepted})
head=subprocess.check_output(['git','-C',str(W),'rev-parse','HEAD'],text=True).strip()
tracked=subprocess.check_output(['git','-C',str(W),'ls-tree','-r','--name-only',head,'--',str((A/'seven-preparation-types-v1').relative_to(W))],text=True).splitlines()
assert tracked==[]
published=[]
for path in ['filed-followups-v1/bind_review_v2.py','filed-followups-v1/independent/scientific-review-v2.json','final-corrections-v1/bind_independent_review.py']:
    p=A/path;raw=subprocess.check_output(['git','-C',str(W),'show',head+':'+str(p.relative_to(W))]);assert raw==p.read_bytes();dest=O/('published-'+Path(path).name)
    with dest.open('xb')as f:f.write(raw)
    published.append({'head':head,'path':str(p.relative_to(W)),'sha256':sha(p)})
P=A/'seven-preparation-types-v1';selected={}
for n in ['decisions','proposals','evidence']:
    left=P/'selected-v1'/(n+'.json');right=P/'selected-v2'/(n+'.json');assert left.read_bytes()==right.read_bytes();selected[n]=sha(left)
receipts=[J(P/s/'review-binding.json')for s in ['selected-v1','selected-v2']];receipt_diff=[k for k in receipts[0]if receipts[0][k]!=receipts[1][k]];assert receipt_diff==['bound_at']
for path,pin in pins.items():assert sha(W/path)==pin
put(O/'reproduction.json',{'at':datetime.datetime.now(datetime.UTC).isoformat(),'native_scope':'Actual full binder validate() called with actual complete188decision/117proposal documents; only copied proof author fields varied in memory. No binder main/publication invoked.','controls':rows,'proof_author_states':proof_states,'input_hashes':pins,'published_local_head':head,'seven_preparation_paths_in_head':tracked,'published_predecessor_bytes_verified':published,'selected_v1_v2_core_hashes_identical':selected,'receipt_delta_fields':receipt_diff,'actual_proofs_have_conflict':False,'maintained_or_worker_writes':False})
print(json.dumps({'head':head,'controls':len(rows),'published_paths':len(published),'new_draft_tracked_paths':len(tracked),'cores_unchanged':True},indent=2))
