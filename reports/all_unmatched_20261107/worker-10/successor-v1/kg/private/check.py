import dataclasses,hashlib,json,pathlib,subprocess,sys,yaml
from datetime import datetime,timezone
sys.path.insert(0,str(pathlib.Path('src').resolve()))
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
from mediaingredientmech.validation.write_validated import validate_ingredient
R=pathlib.Path('reports/all_unmatched_20261107/worker-10');K=R/'successor-v1/kg';S=pathlib.Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
sha=lambda p:hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
C=json.loads((S/'shards/shard-10.json').read_text())['cases'];D=json.loads((K/'decisions.json').read_text())['decisions'];E=json.loads((K/'evidence.json').read_text())['evidence'];P=json.loads((K/'proposals.json').read_text())['proposals'];OE=json.loads((R/'evidence.json').read_text())['evidence'];ed={e['evidence_id']:e for e in OE+E};pd={p['proposal_id']:p for p in P};dd={d['case_id']:d for d in D};ix=json.loads((R/'successor-v1/assigned-no-proposal-cohort.json').read_text())['partitions']['kg']
assert len(D)==len(dd)==38 and set(dd)=={C[i]['case_id'] for i in ix}
assert len(E)==len({e['evidence_id'] for e in E}) and not {e['evidence_id'] for e in E}&{e['evidence_id'] for e in OE}
assert len(P)==len(pd)
for d in D:
 c=C[d['source_index']];assert d['case_input_sha256']==hashlib.sha256(json.dumps(c,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest();assert d['source']=={k:c[k] for k in ['source','source_case_id','source_label','raw_source_label']}
 assert set(d['evidence_ids'])<=set(ed) and set(d['proposal_ids'])<=set(pd)
 if not d['proposal_ids']:assert d['no_change_reason']
 if d['disposition']=='unresolved':assert d['missing_requirement']
 assert d['completion_reassessment']['owner_lookup_complete'] and not d['completion_reassessment']['ordinary_curation_deferred']
 for o in d['owner_records']:assert sha(o['path'])==o['sha256']
for e in E+[ed[i] for d in D for i in d['evidence_ids'] if i not in {x['evidence_id'] for x in E}]:
 cap=e['capture'];assert sha((R if cap['root']=='artifact' else S)/cap['path'])==cap['sha256'],e['evidence_id']
 if e['kind'] in ['primary_source','ontology']:assert e['url'] and e['accessed_at']
files=subprocess.check_output(['rg','--files','--no-ignore','--hidden','data/ingredients'],text=True).splitlines();cat={p:yaml.safe_load(pathlib.Path(p).read_text()) for p in files if p.endswith('.yaml')};baseline=validate_component_partonomy(cat.values());identifiers=[]
for p in P:
 assert set(p['evidence_ids'])<=set(ed)
 path=pathlib.Path(p['owner_path']);after=R/p['after_capture']['path'];assert sha(after)==p['after_capture']['sha256'];v=yaml.safe_load(after.read_text());assert not validate_ingredient(v)
 if p['kind']=='edit_existing_owner':assert sha(path)==p['before_sha256']
 else:assert not path.exists() and p['before_sha256'] is None
 hits=[{'path':f,'sha256':sha(f),'mapping_status':x.get('mapping_status')} for f,x in cat.items() if x.get('identifier')==v['identifier']]
 identifiers.append({'proposal_id':p['proposal_id'],'identifier':v['identifier'],'ignored_files_included':True,'held_by':hits})
 assert not any(x['path']!=p['owner_path'] and x['mapping_status']!='REJECTED' for x in hits),(p['proposal_id'],hits)
 cat[p['owner_path']]=v
 for cid in p['case_ids']:assert p['proposal_id'] in dd[cid]['proposal_ids']
 for d in D:
  if p['proposal_id'] in d['proposal_ids']:assert d['case_id'] in p['case_ids']
violations=validate_component_partonomy(cat.values());result={'status':'PASS' if not violations else 'FAIL','checked_at':datetime.now(timezone.utc).isoformat(),'case_count':len(D),'new_evidence_count':len(E),'proposal_count':len(P),'proposed_closed_schema_errors':0,'catalog_baseline_partonomy_violations':len(baseline),'catalog_with_proposals_partonomy_violations':[dataclasses.asdict(x) for x in violations],'complete_catalog_count_with_proposals':len(cat),'input_hashes':{n:sha(K/n) for n in ['decisions.json','evidence.json','proposals.json']},'independent_review_status':'pending','scientific_approval_established':False,'checks':['all38exact case digests and labels','oldandnew evidence hashes','all actual ownerpreimages','guarded payload hashes and strictshape','bidirectional proposalbacklinks','complete maintainedcatalog nativepartonomy withproposals in memory','ignoredinclusive proposedidentifier collision search']}
(K/'identifier-lookup.json').write_text(json.dumps(identifiers,indent=2)+'\n');(K/'validation.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2));assert not violations
