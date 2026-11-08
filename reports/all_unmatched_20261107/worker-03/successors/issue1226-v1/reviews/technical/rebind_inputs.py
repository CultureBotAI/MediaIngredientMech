"""Independent read-only exact input audit for the bounded W03 provenance repair."""
from pathlib import Path
import json,hashlib,subprocess,collections,datetime
import yaml
R=Path.cwd();C=R.parents[2];P=C/'preflight/w03-current-provenance-allowlist-v1';O=R/'.temp/w03-provenance-successor-v1/technical';F=R/'reports/all_unmatched_20261107/worker-03/successors/issue1224-v1/publication-v1';A=R/'reports/all_unmatched_20261107/worker-03';HEAD='f6bfbf3c185f705484aa106405f813209146c766'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def canon(v):return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
def dump(name,v):
 with (O/name).open('x') as f:json.dump(v,f,indent=2);f.write('\n')
assert subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()==HEAD
manifest=json.loads((P/'MANIFEST.json').read_text());errors=[]
for x in manifest['files']:
 if sha(P/x['path'])!=x['sha256']:errors.append(x['path'])
assert not errors and len(manifest['files'])==122
allow=json.loads((P/'repair-allowlist.json').read_text());rows=allow['rows'];assert len(rows)==49 and len({x['proposal_id'] for x in rows})==49
core={n:json.loads((F/n).read_text()) for n in ['decisions.json','proposals.json','evidence.json']}
for n in core:
 assert (F/n).read_bytes()==(P/('current-'+n)).read_bytes()
 assert subprocess.check_output(['git','show',HEAD+':'+str((F/n).relative_to(R))])==(F/n).read_bytes()
decisions={x['case_id']:x for x in core['decisions.json']['decisions']};proposals={x['proposal_id']:x for x in core['proposals.json']['proposals']}
assert len(decisions)==188 and len(proposals)==74 and len(core['evidence.json']['evidence'])==863
records={};before={};payload_checks=[];new_manual=[];inherited_manual=[]
for pid,pr in proposals.items():
 cap=pr['after_capture'];p=A/cap['path'];assert cap['root']=='artifact' and sha(p)==cap['sha256'];raw=subprocess.check_output(['git','show',HEAD+':'+str(p.relative_to(R))]);assert hashlib.sha256(raw).hexdigest()==cap['sha256'];record=yaml.safe_load(raw);records[pid]=record
 bp=R/pr['owner_path'];b=yaml.safe_load(bp.read_text()) if pr['kind']=='edit_existing_owner' else {};before[pid]=b
 if b:assert sha(bp)==pr['before_sha256']
 else:assert pr['before_sha256'] is None
 remaining=collections.Counter(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False) for x in b.get('ontology_mapping',{}).get('evidence',[]))
 for i,x in enumerate(record.get('ontology_mapping',{}).get('evidence',[])):
  s=json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False);inherited=remaining[s]>0
  if inherited:remaining[s]-=1
  if x.get('evidence_type')=='MANUAL_CURATION':(inherited_manual if inherited else new_manual).append({'proposal_id':pid,'index':i,'object_sha256':canon(x),'object':x})
 payload_checks.append({'proposal_id':pid,'path':str(p.relative_to(R)),'sha256':sha(p),'kind':pr['kind'],'before_sha256':pr['before_sha256']})
assert {(x['proposal_id'],x['index']) for x in new_manual}=={(r['proposal_id'],0) for r in rows}
assert {(x['proposal_id'],x['index']) for x in inherited_manual}=={('b-proposal-marine-aliases',0),('c-copper-trihydrate-alias',4),('m-arabinan_source_alias',2)}
checks=[]
for row in rows:
 pid=row['proposal_id'];pr=proposals[pid];record=records[pid];b=before[pid];mapping=record['ontology_mapping'];obj=mapping['evidence'][0];parent={k:v for k,v in mapping.items() if k!='evidence'}
 assert row['published_payload_path']==str((A/pr['after_capture']['path']).relative_to(R))
 assert sha(P/row['payload']['path'])==row['payload']['sha256']==pr['after_capture']['sha256']
 assert row['complete_mapping_evidence_object']==obj and row['complete_object_canonical_sha256']==canon(obj)
 assert row['parent_context']==parent and row['parent_context_sha256']==canon(parent)
 assert row['history_prefix_sha256']==canon(record.get('curation_history',[]))
 assert row['current_identifier']==record['identifier'] and row['current_mapping_status']==record['mapping_status']
 assert row['field']=='ontology_mapping.evidence[0].evidence_type' and row['change']=={'from':'MANUAL_CURATION','to':'LLM_SUGGESTION'}
 assert row['case_ids']==pr['case_ids'] and all(decisions[c]['case_input_sha256']==h for c,h in row['case_input_sha256'].items())
 assert row['proposal_kind']==pr['kind'] and row['owner_path']==pr['owner_path']
 if row['authentic_before']:
  assert sha(P/row['authentic_before']['path'])==row['authentic_before']['sha256']==pr['before_sha256']
  assert yaml.safe_load((P/row['authentic_before']['path']).read_text())==b
 else:assert not b and row['authentic_before_path'] is None
 assert row['before_parent_context']=={k:v for k,v in b.get('ontology_mapping',{}).items() if k!='evidence'}
 assert obj not in b.get('ontology_mapping',{}).get('evidence',[])
 authored=row['author_evidence']['added_curation_history'];assert all(x in record.get('curation_history',[]) for x in authored)
 assert any(x.get('llm_assisted') is True for x in authored)
 checks.append({'proposal_id':pid,'object_sha256':canon(obj),'parent_sha256':canon(parent),'history_prefix_sha256':canon(record.get('curation_history',[])),'payload_sha256':pr['after_capture']['sha256'],'before_sha256':pr['before_sha256'],'case_ids':pr['case_ids'],'agent_history_present':True,'exact_current_bindings_match':True})
ox=records['w03-oxoid-cm0149-product-1224-v1'];assert proposals['w03-oxoid-cm0149-product-1224-v1']['after_capture']['sha256']=='1ec7554da19d5a6ab2259ee79d178a95511a923e611f4fc176af498248ab76ae';assert [x['evidence_type'] for x in ox['ontology_mapping']['evidence']]==['LLM_SUGGESTION','LLM_SUGGESTION'];assert 'b-proposal-cm0149-form' not in proposals
result={'reviewer':'/root/provenance_controls','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'head':HEAD,'status':'PASS_EXACT_CURRENT_INPUT_AND_EXCLUSION_BINDINGS','manifest_sha256':sha(P/'MANIFEST.json'),'manifest_members':122,'manifest_errors':errors,'counts':{'cases':188,'proposals':74,'current_evidence':863,'allowlisted_objects':49,'new_owner_allowlisted':sum(r['proposal_kind']=='new_owner' for r in rows),'existing_owner_allowlisted':sum(r['proposal_kind']=='edit_existing_owner' for r in rows),'inherited_manual_excluded':3,'correct_oxoid_excluded':2},'core_hashes':{n:sha(F/n) for n in core},'payload_checks':payload_checks,'allowlist_checks':checks,'inherited_manual_objects':inherited_manual,'retired_origin_active':False,'scientific_approval':False,'scope':'Exact metadata object and parent/current-before/authorship binding only; no primary chemical/source truth renewed.'}
dump('current-input-verification.json',result)
print(json.dumps({k:v for k,v in result.items() if k not in ['payload_checks','allowlist_checks','inherited_manual_objects']},indent=2))
