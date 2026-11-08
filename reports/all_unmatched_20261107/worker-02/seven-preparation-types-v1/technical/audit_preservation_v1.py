"""Read-only independent seven-category exact preservation audit.
Does not import the author's builder or assert scientific category approval.
"""
from pathlib import Path
from datetime import datetime,timezone
import argparse,copy,hashlib,json,yaml
HERE=Path(__file__).resolve().parent;R=HERE.parent;A=R.parent;W=R.parents[3]
def sha(raw):return hashlib.sha256(raw).hexdigest()
def canonical(x):return sha(json.dumps(x,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode())
def raw_objects(raw,key):
    text=raw.decode();pos=text.index('[',text.index(json.dumps(key)+':'))+1;decoder=json.JSONDecoder();rows=[]
    while True:
        while text[pos].isspace() or text[pos]==',':pos+=1
        if text[pos]==']':return rows
        _,end=decoder.raw_decode(text,pos);rows.append(text[pos:end].encode());pos=end

def main():
    ap=argparse.ArgumentParser();ap.add_argument('selection');ap.add_argument('output');ap.add_argument('--review-complete',action='store_true');args=ap.parse_args()
    if '/' in args.selection or '/' in args.output or '..' in args.selection or '..' in args.output:raise ValueError('Require simple private names')
    out=HERE/args.output
    if out.exists():raise FileExistsError(out)
    inputs=[]
    def read(p,kind='json'):
        raw=p.read_bytes();inputs.append({'path':str(p.relative_to(W)) if p.is_relative_to(W) else str(p),'sha256':sha(raw)})
        return (json.loads(raw) if kind=='json' else yaml.safe_load(raw)),raw
    intake,_=read(HERE/'intake-v1.json');old=W/intake['selected_predecessor'];new=R/args.selection
    before={};after={};br={};ar={}
    for name in ['decisions','proposals','evidence']:
        before[name],br[name]=read(old/(name+'.json'));after[name],ar[name]=read(new/(name+'.json'))
        assert {k:v for k,v in before[name].items() if k!=name}=={k:v for k,v in after[name].items() if k!=name}
    ds=before['decisions']['decisions'];ns=after['decisions']['decisions'];assert len(ds)==len(ns)==188
    frozen,_=read(A/'context/frozen-shard-02.json');cases=frozen['cases'];assert len(cases)==188
    db=raw_objects(br['decisions'],'decisions');nb=raw_objects(ar['decisions'],'decisions');case_rows=[]
    for i,(b,n,c) in enumerate(zip(ds,ns,cases,strict=True)):
        assert b['case_id']==n['case_id']==c['case_id'];assert b['case_input_sha256']==n['case_input_sha256']==canonical(c)
        assert n['occurrence_ids']==[x['occurrence_id'] for x in c.get('occurrences',[])]
        assert n['source']=={k:c[k] for k in ['source','source_case_id','source_label','raw_source_label']}
        delta=sorted(k for k in set(b)|set(n) if b.get(k)!=n.get(k))
        assert delta==(['independent_review'] if i==58 else []),(i,delta)
        if i==58:
            assert len(n['occurrence_ids'])==24
            expected='complete' if args.review_complete else 'pending'
            assert n['independent_review']['status']==expected
            if not args.review_complete:assert n['independent_review']=={'status':'pending','evidence_ids':[]}
        else:assert db[i]==nb[i]
        case_rows.append({'index':i,'case_id':n['case_id'],'before_canonical_sha256':canonical(b),'after_canonical_sha256':canonical(n),'case_input_sha256':canonical(c),'changed_fields':delta,'raw_object_bytes_equal':db[i]==nb[i]})
    ps=before['proposals']['proposals'];qs=after['proposals']['proposals'];assert len(ps)==len(qs)==117
    targets={x['proposal_id']:x for x in intake['targets']};assert len(targets)==7
    pb=raw_objects(br['proposals'],'proposals');qb=raw_objects(ar['proposals'],'proposals');rows=[];changed=[]
    for i,(b,n) in enumerate(zip(ps,qs,strict=True)):
        pid=b['proposal_id'];assert pid==n['proposal_id'];bv,bb=read(A/b['after_capture']['path'],'yaml');nv,nn=read(A/n['after_capture']['path'],'yaml')
        assert sha(bb)==b['after_capture']['sha256'];assert sha(nn)==n['after_capture']['sha256']
        if pid in targets:
            changed.append(pid);assert sha(bb)==targets[pid]['payload']['sha256'];assert b['kind']==n['kind']=='new_owner' and b['before_sha256'] is n['before_sha256'] is None
            p=copy.deepcopy(b);p['after_capture']=n['after_capture'];assert p==n
            assert bv['solution_type']=='MINERAL_STOCK' and nv['solution_type']=='OTHER'
            assert len(bv['curation_history'])==targets[pid]['history_length'];assert canonical(bv['curation_history'])==targets[pid]['history_canonical_sha256']
            assert len(nv['curation_history'])==len(bv['curation_history'])+1 and nv['curation_history'][:-1]==bv['curation_history']
            clean=copy.deepcopy(nv);clean['solution_type']=bv['solution_type'];clean['curation_history']=bv['curation_history'];assert clean==bv
            ev=nv['curation_history'][-1];assert ev['curator']=='worker02 /root' and ev['action']=='CORRECTED' and ev['llm_assisted'] is True
            assert 'W01-W02-PREP-TYPE-001' in ev['changes'] and 'OTHER' in ev['changes'] and 'MINERAL_STOCK' in ev['changes']
            stamp=datetime.fromisoformat(ev['timestamp']);assert stamp.utcoffset() is not None and stamp<=datetime.now(timezone.utc)
        else:assert b==n and bb==nn and pb[i]==qb[i]
        rows.append({'proposal_id':pid,'before_capture':b['after_capture'],'after_capture':n['after_capture'],'changed':pid in targets,'old_history_length':len(bv.get('curation_history',[])),'new_history_length':len(nv.get('curation_history',[])),'old_history_canonical_sha256':canonical(bv.get('curation_history',[])),'payload_bytes_equal':bb==nn,'proposal_raw_object_bytes_equal':pb[i]==qb[i]})
    assert set(changed)==set(targets)
    boundary=intake['untouched_boundary'];newboundary=next(x for x in qs if x['proposal_id']==boundary['proposal_id']);assert boundary==newboundary
    olde=before['evidence']['evidence'];newe=after['evidence']['evidence'];assert newe[:len(olde)]==olde;assert len({x['evidence_id'] for x in newe})==len(newe)
    # Confirm each additive capture, while leaving source interpretation to the scientific reviewer.
    for e in newe[len(olde):]:
        cap=e['capture'];assert cap['root']=='artifact';p=A/cap['path'];assert sha(p.read_bytes())==cap['sha256'];inputs.append({'path':str(p.relative_to(W)),'sha256':cap['sha256']})
    receipt={'reviewer':'/root/research_b','reviewed_at':datetime.now(timezone.utc).isoformat(),'status':'PASS','scope':'Technical full-ledger/payload/source-binding preservation only; no chemistry approval','selection':str(new.relative_to(W)),'input_bindings':inputs,'counts':{'cases':188,'occurrences':sum(len(d['occurrence_ids']) for d in ns),'proposals':117,'target_whole_case_occurrences':24,'changed_payloads':7,'unchanged_payloads':110,'unchanged_full_case_objects':187,'case_scientific_fields_unchanged':188,'new_evidence_entries':len(newe)-len(olde)},'case_rows':case_rows,'proposal_rows':rows,'untouched_boundary_proposal_id':boundary['proposal_id'],'untouched_boundary_sha256':boundary['after_capture']['sha256'],'old_history_preserved_every_payload':True,'no_scientific_approval':True}
    with out.open('x') as f:json.dump(receipt,f,indent=2);f.write('\n')
    print(json.dumps({'status':'PASS','output':str(out.relative_to(W)),'sha256':sha(out.read_bytes()),'counts':receipt['counts']}))
if __name__=='__main__':main()
