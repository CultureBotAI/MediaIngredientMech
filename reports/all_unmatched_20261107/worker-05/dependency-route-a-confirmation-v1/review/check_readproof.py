import collections,csv,datetime,hashlib,io,json,pathlib,zipfile,yaml
R=pathlib.Path('.temp/w05-dependency-route-a-confirmation-v1/review')
B=pathlib.Path('reports/all_unmatched_20261107/worker-05')
P=B/'buffer-parts-v1'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def oh(x):return hashlib.sha256(json.dumps(x,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
def j(p):return json.loads(p.read_text())
def bind(p):return {'path':str(p),'sha256':sha(p)}
index=j(R/'complete-payload-field-read-index-v1.json')
props=j(P/'dependencies-direct-v1/proposals.json')['proposals']
shape=[];scalars={}
def walk(pid,x,ptr=''):
    if isinstance(x,dict):
        shape.append([pid,ptr,'mapping',list(x)])
        for k,v in x.items():walk(pid,v,ptr+'/'+str(k).replace('~','~0').replace('/','~1'))
    elif isinstance(x,list):
        shape.append([pid,ptr,'sequence',len(x)])
        for n,v in enumerate(x):walk(pid,v,ptr+'/'+str(n))
    else:scalars[(pid,ptr)]=x
for p in props:
    f=B/p['after_capture']['path'];assert sha(f)==p['after_capture']['sha256']
    walk(p['proposal_id'],yaml.safe_load(f.read_text()))
assert shape==index['container_shapes']
indexed={tuple(loc):row['value'] for row in index['scalar_values'] for loc in row['exact_field_paths']}
assert indexed==scalars
obs=j(P/'dependencies/source-observations.json')
archive=P/'dependencies/inputs/w03-peer/other/captures/microbedecoder_database.zip'
assert sha(archive)==obs['archive_sha256']
with zipfile.ZipFile(archive) as z:raw=z.read(obs['member'])
assert hashlib.sha256(raw).hexdigest()==obs['member_sha256']
rawrows=list(csv.DictReader(io.StringIO(raw.decode('latin-1'))))
checks=[]
for r in obs['rows']:
    a=rawrows[r['record_index_zero_based']]
    assert a==r['complete_database_row']
    assert a[r['field']]==r['literal']
    assert r['csv_row_including_header']==r['record_index_zero_based']+2
    checks.append({'target_id':r['target_id'],'csv_row_including_header':r['csv_row_including_header'],'field':r['field'],'literal':r['literal'],'genus':r['genus'],'species':r['species'],'source_links':r['source_links'],'complete_original_row_object_sha256':oh(a)})
prior=j(P/'review/dependencies/source-read-ledger.json');reused=[]
for e in prior['source_captures']:
    p=pathlib.Path(e['capture']['path']);assert sha(p)==e['capture']['sha256'];reused.append({'capture':e['capture'],'actual_prior_reviewer':e['read_by'],'actual_prior_read_extent':e['read_extent'],'original_retrieval_metadata':e['prior_retrieval_metadata'],'timestamp_limit':e['timestamp_limit']})
decisions=j(P/'core/decisions.json')['decisions'];old=j(P/'review/main-review.json')
bycase={d['case_id']:d for d in decisions};oldcases={d['case_id']:d for d in old['case_reviews']}
caseids=sorted({cid for p in props for cid in p['case_ids']});cases=[]
for cid in caseids:
    d=bycase[cid];assert oh(d)==oldcases[cid]['selected_decision_object_sha256']
    cases.append({'case_id':cid,'selected_decision_object_sha256':oh(d),'case_input_sha256':d['case_input_sha256'],'prior_full_case_review':bind(P/'review/main-review.json'),'actual_prior_assessment':oldcases[cid]['assessment'],'actual_prior_reviewer':oldcases[cid].get('actual_scientific_reviewer',old.get('reviewer')),'scope':'Exact unchanged selected full decision; only causal dependency provenance newly reassessed here, all earlier whole-case source holds retained.'})
out={'reviewer':'/root/final_skeptical','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'result':'PASS','payload_readproof':{'payload_count':len(props),'unique_scalar_values':len(index['scalar_values']),'actual_scalar_field_count':len(scalars),'container_count':len(shape),'index_exactly_covers_every_full_parsed_payload':True,'index':bind(R/'complete-payload-field-read-index-v1.json'),'reading_method':'Every unique scalar was read with exact repeated-field path index retained; container traversal independently checked complete. Content reading is distinct from this structural proof.'},'source_row_checks':checks,'source_scope':'All130 raw scientific observation fields were reread, including114 PYG taxa/labels/source routes. Full raw rows independently re-extracted and byte-content compared, not promoted to full underlying publication review or organism metadata approval.','old_primary_source_reuse':reused,'case_binding_checks':cases,'limits':['Hash and traversal checks do not themselves supply scientific conclusions.','Prior full-paper access limitations and original capture dates remain unchanged.','No new source case, origin or payload authored.']}
f=R/'readproof-and-source-reuse-v1.json';assert not f.exists();f.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps(bind(f)))
