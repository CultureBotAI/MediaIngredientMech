from pathlib import Path
import importlib.util,copy,json,hashlib,datetime,yaml
S=Path('.temp/worker07-issues1226-1237-v1/skeptic');root=Path('reports/all_unmatched_20261107/worker-07');script=root/'successors/issues1226-1237-v1/parts/build-correction.py';spec=importlib.util.spec_from_file_location('guarded',script);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
rows=json.loads(Path('.temp/worker07-issues1226-1237-v1/provenance-author/allowlist-v1.json').read_text())['rows'];r=copy.deepcopy(rows[0]);p=Path(r['payload']['path']);old=yaml.safe_load(p.read_text());digest=hashlib.sha256(p.read_bytes()).hexdigest();results=[]
def attempt(name,obj,sha,row,accept):
 try:m.rebind(obj,sha,row)
 except Exception as e:
  assert not accept,(name,str(e));results.append({'name':name,'result':'PASS_REFUSED','exception':type(e).__name__,'message':str(e)})
 else:
  assert accept,name;results.append({'name':name,'result':'PASS_ACCEPTED'})
attempt('actual exact current owner and complete evidence object',old,digest,r,True)
attempt('stale owner hash',old,'0'*64,r,False)
x=copy.deepcopy(old);x['ontology_mapping']['evidence'][0]['notes']+=' unsupported broadened applicability';attempt('same source but changed complete assertion',x,digest,r,False)
x=copy.deepcopy(old);x['ontology_mapping']['ontology_id']='CHEBI:31795';attempt('changed mapping attachment toward component identity',x,digest,r,False)
x=copy.deepcopy(r);x['enum']='ComponentEvidenceTypeEnum';x['type_pointer']='/component_assertion/evidence/0/evidence_type';attempt('same enum spelling in ComponentEvidence context',old,digest,x,False)
x=copy.deepcopy(r);x['duplicate_ordinal_1based']=2;attempt('wrong duplicate ordinal',old,digest,x,False)
x=copy.deepcopy(r);x['baseline_match_index']=0;attempt('historical full object excluded',old,digest,x,False)
x=copy.deepcopy(old);x['ontology_mapping']['evidence'].append(copy.deepcopy(x['ontology_mapping']['evidence'][0]));attempt('ambiguous added duplicate multiplicity',x,digest,r,False)
x=copy.deepcopy(old);x['invented_property']='must fail';errs=m.validate_ingredient(x);assert errs;results.append({'name':'native closed schema rejects unknown property','result':'PASS_REFUSED','errors':str(errs)})
x=copy.deepcopy(old);x['components'][0]['reference_scope']='invented';errs=m.validate_ingredient(x);assert errs;results.append({'name':'native schema rejects invalid component enum','result':'PASS_REFUSED','errors':str(errs)})
res={'reviewer':'/root/successor1226_1237_skeptic','created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'script':str(script),'script_sha256':hashlib.sha256(script.read_bytes()).hexdigest(),'actual_native_imports':'mediaingredientmech.validation.write_validated.validate_ingredient; production helper unchanged; no output writer invoked by controls','controls':results,'passed':len(results),'failed':0,'limitations':'Bounded in-memory mutation controls; no hostile concurrency, atomicity or universal guard claims.'};(S/'independent-guard-controls-v1.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
