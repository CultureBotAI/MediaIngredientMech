from pathlib import Path
import json,hashlib,subprocess,collections,datetime,yaml
ROOT=Path.cwd(); OUT=ROOT/'.temp/worker07-issues1226-1237-v1/skeptic'; BASE='e000d66dd26ab053e9b17ce7bf8d3c873c3dde99'; HEAD='ddef7355bf7814bd3b1a23b9d61327bea3ac75fe'; ART=ROOT/'reports/all_unmatched_20261107/worker-07'; AUD=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/workers/w02/worktree/.temp/campaign-evidence-provenance-audit-v1')
def sha(x):return hashlib.sha256(x).hexdigest()
def canon(x):return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False)
def write(n,x):
 p=OUT/n;assert not p.exists();p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def bind(p):return {'path':str(p.relative_to(ROOT)) if p.is_relative_to(ROOT) else str(p),'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size}
def gitblob(rev,p):return subprocess.run(['git','show',rev+':'+p],stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True).stdout
errs=[]; records=[]; inh=[]; added=[]; comps=[]
proposals=json.loads((ART/'successors/issue1203-v1/proposals.json').read_text())['proposals']; audit=[x for x in json.loads((AUD/'provenance/entry-provenance-ledger-v1.json').read_text())['rows'] if x['worker']==7]
for prop in proposals:
 p=ART/prop['after_capture']['path'];raw=p.read_bytes(); after=yaml.safe_load(raw);before={};bp=prop['owner_path']
 assert sha(raw)==prop['after_capture']['sha256'];assert gitblob(HEAD,str(p.relative_to(ROOT)))==raw
 if prop['kind']=='edit_existing_owner':
  old=gitblob(BASE,bp);assert sha(old)==prop['before_sha256'];before=yaml.safe_load(old)
 oldev=(before.get('ontology_mapping') or {}).get('evidence') or [];newev=(after.get('ontology_mapping') or {}).get('evidence') or [];oldcounts=collections.Counter(canon(v) for v in oldev);seen=collections.Counter()
 for i,v in enumerate(newev):
  if v.get('evidence_type')!='MANUAL_CURATION':continue
  k=canon(v);seen[k]+=1;reused=seen[k]<=oldcounts[k];row={'proposal_id':prop['proposal_id'],'payload':bind(p),'owner_path':bp,'pointer':f'/ontology_mapping/evidence/{i}','duplicate_ordinal_1based':seen[k],'complete_object':v,'complete_object_sha256_canonical_json':sha(k.encode()),'historical_full_object_match':reused}
  if reused:inh.append(row)
  else:
   matches=[x for x in audit if x['proposal_id']==prop['proposal_id'] and x['full_value']==v and x['field']==f'ontology_mapping.evidence[{i}]']; assert len(matches)==1,(prop['proposal_id'],i,len(matches));m=matches[0];assert m['payload_sha256']==sha(raw);assert m['full_value']==v;row['frozen_audit_id']=m['audit_row_id'];row['confirmed_agent_events']=m['author_evidence']['added_curation_history'];assert all(h in (after.get('curation_history') or []) for h in row['confirmed_agent_events']);row['suggested_type']='LLM_SUGGESTION';row['independent_basis']='Complete notes make a source-qualified applicability, substance/formulation, parent-identity or nominal-stock interpretation; current exact author events and preserved peer attribution establish campaign agent authorship. A primary URL alone does not make this a human-supplied MIM evidence assertion.';added.append(row)
 def walk(v,path):
  if isinstance(v,dict):
   for k,z in v.items():
    if k=='evidence_type' and z=='MANUAL_CURATION' and not path.startswith('/ontology_mapping/evidence'):comps.append({'proposal_id':prop['proposal_id'],'pointer':path+'/'+k,'complete_parent':v,'preserve':True})
    walk(z,path+'/'+k)
  elif isinstance(v,list):
   for i,z in enumerate(v):walk(z,path+'/'+str(i))
 walk(after,'')
 records.append({'proposal_id':prop['proposal_id'],'payload':bind(p),'owner_path':bp,'kind':prop['kind'],'before_sha256':prop.get('before_sha256'),'fields':list(after)})
assert len(added)==len(audit);assert {x['frozen_audit_id'] for x in added}=={x['audit_row_id'] for x in audit}
cores=[]
for n,key in [('decisions.json','decisions'),('evidence.json','evidence'),('proposals.json','proposals')]:
 p=ART/'successors/issue1203-v1'/n;x=json.loads(p.read_text());cores.append({**bind(p),'count':len(x[key]),'equals_HEAD_blob':gitblob(HEAD,str(p.relative_to(ROOT)))==p.read_bytes()})
packets=[]
for rel in ['.temp/fac-polypeptone-independent-v1','reports/all_unmatched_20261107/worker-07/successors/issue1223-v1']:
 d=ROOT/rel; mf=d/'MANIFEST.json'; m=json.loads(mf.read_text());rows=[]
 for f in m['files']:
  p=d/f['path'];actual=sha(p.read_bytes());assert actual==f['sha256'];assert p.stat().st_size==f['bytes'];rows.append(f)
 actualset={str(p.relative_to(d)) for p in d.rglob('*') if p.is_file() and not str(p.relative_to(d)).startswith('native-repo/.git/')};exclude={'MANIFEST.json','SEAL.json'} if 'fac-polypeptone' in rel else {'MANIFEST.json'};listed={r['path'] for r in rows}; assert actualset-exclude==listed,(rel,actualset-exclude-listed,listed-actualset)
 packets.append({'root':rel,'manifest':bind(mf),'count':len(rows),'all_hashes_sizes_match':True,'exact_ignored_inclusive_fileset':True,'seal':bind(d/'SEAL.json') if (d/'SEAL.json').exists() else None})
d=ROOT/'.temp/w10-published-head-independent-review-v1';rows=[]
for line in (d/'SHA256SUMS').read_text().splitlines():
 digest,name=line.split('  ',1);p=d/name;assert sha(p.read_bytes())==digest;rows.append(name)
assert {str(p.relative_to(d)) for p in d.rglob('*') if p.is_file()}-{'SEAL.json','SHA256SUMS'}==set(rows)
packets.append({'root':str(d.relative_to(ROOT)),'manifest':bind(d/'SHA256SUMS'),'seal':bind(d/'SEAL.json'),'count':len(rows),'all_hashes_match':True,'exact_ignored_inclusive_fileset':True})
tracked=[]
for name in subprocess.check_output(['git','ls-tree','-r','-z','--name-only',HEAD,'--','reports/all_unmatched_20261107/worker-07','reviews/structured','data','mappings','src','scripts','schema','justfile','MAPPING_SEMANTICS.md','AGENTS.md']).decode().rstrip('\0').split('\0'):
 p=ROOT/name;raw=p.read_bytes();expected=gitblob(HEAD,name);assert raw==expected,name;tracked.append({'path':name,'sha256':sha(raw)})
write('baseline-byte-proof-v1.json',{'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reviewer':'/root/successor1226_1237_skeptic','head':HEAD,'scientific_base':BASE,'core_ledgers':cores,'selected_payloads':records,'protected_packets':packets,'tracked_inputs_identical_to_head':tracked,'tracked_inputs_checked':len(tracked),'scientific_approval':False})
write('independent-provenance-recomputation-v1.json',{'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reviewer':'/root/successor1226_1237_skeptic','audit_handoff':bind(AUD/'HANDOFF.md'),'scope':'Independent duplicate-aware current complete MappingEvidence comparison against authentic frozen base; all100selected payloads, author events and full notes; not independent primary science renewal of all chemical claims.','selected_payload_count':len(records),'confirmed_new_agent_mapping_entries':len(added),'affected_proposal_count':len({x['proposal_id'] for x in added}),'rows':added,'inherited_manual_objects':inh,'separate_component_enum_exclusions':comps,'errors':errs})
print(json.dumps({'selected':len(records),'new_mapping_entries':len(added),'affected_proposals':len({x['proposal_id'] for x in added}),'inherited_mapping':len(inh),'component_exclusions':len(comps),'tracked_inputs':len(tracked),'protected':packets},indent=2))
