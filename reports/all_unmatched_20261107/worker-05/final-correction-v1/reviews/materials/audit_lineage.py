from pathlib import Path
import json,hashlib,yaml
O=Path(__file__).parent;P=O.parent/'materials';B=Path('reports/all_unmatched_20261107/worker-05');C=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107');Q=C/'queue/preliminary-v5'
def read(p):return json.loads(Path(p).read_text())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
D=read(P/'decisions.json')['decisions'];DP={d['case_id']:d for d in read(B/'correction-1193-v1/materials/decisions.json')['decisions']};PP={p['proposal_id']:p for p in read(B/'correction-1193-v1/materials/proposals.json')['proposals']};P2=read(P/'proposals.json')['proposals'];A=read(O.parent/'control/materials-assignment.json');S={d['case_id']:d for d in read(Q/'shards/shard-05.json')['cases']};E={e['evidence_id']:e for e in read(P/'evidence.json')['evidence']}
lineage=[];seen=set();assert set(A['case_ids'])==set(DP)=={d['case_id'] for d in D}
for p in P2:
 prior=[x for x in p['replaces_proposal_ids'] if x in PP];assert len(prior)==1 and prior[0] not in seen;seen.add(prior[0]);old=PP[prior[0]]
 for k in ['case_ids','owner_path','before_sha256']:assert p[k]==old[k],(p['proposal_id'],k)
 assert p['predecessor_capture']==old['after_capture']
 lineage.append({'proposal_id':p['proposal_id'],'predecessor_id':old['proposal_id'],'case_ids':p['case_ids'],'owner_path':p['owner_path'],'before_sha256':p['before_sha256'],'predecessor_capture':p['predecessor_capture'],'after_capture':p['after_capture']})
assert seen==set(PP)==set(A['proposal_ids'])
contexts=[];frozen=[]
for d in D:
 old=DP[d['case_id']];raw=S[d['case_id']]
 for k in ['case_input_sha256','source','occurrence_ids','owner_records','preserved_downstream_holds']:assert d.get(k)==old.get(k),(d['case_index'],k)
 assert {k:v for k,v in d['preserved_source_holds'].items() if k!='policy'}=={k:v for k,v in old['preserved_source_holds'].items() if k!='policy'}
 frozen.append(raw)
 rr=[]
 for occ in raw.get('occurrences',[]):
  rp=Q/occ['full_recipe_snapshot'];assert sha(rp)==occ['source_file_sha256'];recipe=yaml.safe_load(rp.read_text());rr.append({'occurrence':occ,'recipe':recipe,'capture':{'root':'source','path':occ['full_recipe_snapshot'],'sha256':sha(rp)}})
 contexts.append({'case_index':d['case_index'],'case_id':d['case_id'],'raw_case':raw,'recipes':rr})
for n,x in [('proposal-lineage-audit.json',{'status':'pass','one_to_one':True,'original_count':len(PP),'successor_count':len(P2),'entries':lineage}),('frozen-contexts.json',contexts)]:assert not(O/n).exists();(O/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
for start in range(0,len(contexts),10):
 out=[]
 for c in contexts[start:start+10]:
  r=c['raw_case'];out.append('CASE '+str(c['case_index'])+' '+json.dumps(r,ensure_ascii=False,separators=(',',':')))
  # All full recipe bytes are parsed and retained; a second full semantic rendering is available in frozen-contexts.
 (O/'read'/f'cases-{start:02}.txt').write_text('\n'.join(out))
print('Exact39-to39 lineage PASS; case sources/counts/holds unchanged; full contexts',len(contexts),'occurrences',sum(len(x['recipes']) for x in contexts))
