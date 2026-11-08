import pathlib,json,hashlib,yaml,datetime
W=pathlib.Path.cwd();C=W.parents[2];O=W/'.temp/nine-scope-candidates-independent-v1/skeptical';p=W/'.temp/nine-scope-candidates-independent-v1/science/resolved-complete-inputs-v1.json';d=json.loads(p.read_text());A=json.loads((C/'assignments/w01-nine-scope-candidates-independent-v1.json').read_text());cases={};occs={};edges=[]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for c in d['candidates']:
 for o in c['originals']:
  for x in o['cases']:
   cid=x['case_id'];q=next(q for q in o['decisions'] if q['case_id']==cid)
   cases.setdefault(cid,{'case_id':cid,'raw_label':x['raw_source_label'],'source_case_id':x['source_case_id'],'input_sha256':q['case_input_sha256'],'origin_entry_ids':set(),'candidate_ids':set(),'occurrence_ids':set()});cases[cid]['origin_entry_ids'].add(o['origin']['entry_id']);cases[cid]['candidate_ids'].add(c['candidate_id'])
   assert cases[cid]['input_sha256']==q['case_input_sha256']
   for z in x.get('occurrences',[]):
    rp=C/'queue/preliminary-v5'/z['full_recipe_snapshot'];assert sha(rp)==z['source_file_sha256'];r=yaml.safe_load(rp.read_text());node=r
    for token in z['component_path'].split('/'):node=node[int(token)] if isinstance(node,list) else node[token]
    assert node==z['raw_component'];oid=z['occurrence_id'];cases[cid]['occurrence_ids'].add(oid);occs[oid]={'occurrence_id':oid,'case_id':cid,'recipe_path':str(rp),'sha256':sha(rp),'component_path':z['component_path'],'exact_raw_component_match':True}
for c in A['candidates']:
 present={cid for cid,x in cases.items() if c['candidate_id'] in x['candidate_ids']};assert present==set(c['case_ids']);observed={oid for cid in present for oid in cases[cid]['occurrence_ids']};assert observed==set(c['occurrence_ids']);edges.append({'candidate_id':c['candidate_id'],'case_ids':sorted(present),'occurrence_ids':sorted(observed),'dependency_only':c['candidate_id'].startswith('DEP-')})
for x in cases.values():
 for k in ['origin_entry_ids','candidate_ids','occurrence_ids']:x[k]=sorted(x[k])
r={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reviewer':'/root/skeptical_review','scope':'Independent exact14case/22occurrence check; all raw labels, raw component objects and original source-author decisions inspected in this review. No unrelated recipe chemistry/roles/unit repairs or product membership is approved.','input':{'path':str(p),'sha256':sha(p)},'counts':{'candidates':len(edges),'unique_cases':len(cases),'unique_occurrences':len(occs),'candidate_case_backlinks':sum(len(x['case_ids']) for x in edges),'candidate_occurrence_backlinks':sum(len(x['occurrence_ids']) for x in edges)},'cases':list(cases.values()),'occurrences':list(occs.values()),'candidate_bindings':edges,'all_pass':True,'semantic_limits':['C9322 sourcecase only receives C9322 product annotation; uncatalogued/generic enzyme cases do not.','Oxoid case appears as comparison provenance on the Difco successor and as product scope on NEW-OXOID; it is not counted twice.','Three rumen dependency parents repeat the source-trigger backlink; they are not three new source observations.','KG cases without CM occurrence arrays are not claims of zero source-media usage.','Original worker decisions retain superseded hypotheses as history, including direct-JCM117 and old rumen redirects; final candidate/current review governs successor scope.']}
f=O/'case-coverage-crosscheck-v1.json'
with f.open('x') as out:json.dump(r,out,indent=2);out.write('\n')
print(json.dumps({'path':str(f),'sha256':sha(f),'counts':r['counts']}))
