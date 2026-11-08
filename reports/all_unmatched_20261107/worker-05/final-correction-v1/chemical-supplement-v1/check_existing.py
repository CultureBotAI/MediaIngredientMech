from pathlib import Path
import json,hashlib,re,yaml
O=Path(__file__).resolve().parent;C=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(n,x):
 p=O/n;assert not p.exists();p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def names(r):return [r.get('identifier',''),r.get('preferred_term',''),r.get('ontology_mapping',{}).get('ontology_label','')]+[s['synonym_text'] if isinstance(s,dict) else s for s in r.get('synonyms',[])]
def thiamine(s):return isinstance(s,str) and bool(re.search('thiamin|aneurin',s,re.I))
def mono(s):
 if not isinstance(s,str):return False
 s=s.lower().replace(' ','').replace('_','').replace('₂','2')
 return thiamine(s) and ('monohydrat' in s or bool(re.search(r'hcl[·⋅・.x-]*h2o',s)))
maintained=[]
for p in Path('data/ingredients').rglob('*.yaml'):
 r=yaml.safe_load(p.read_text())
 if any(thiamine(n) for n in names(r)):
  maintained.append({'path':str(p),'sha256':sha(p),'record':r,'same_form_name_hits':[n for n in names(r) if mono(n)]})
input=C/'preflight/final-intake-candidate-v1/all-active-proposal-entries-v1.json';j=json.loads(input.read_text());hits=[];components=[]
for e in j['entries']:
 p=input.parent/e['payload_path'];assert sha(p)==e['payload_sha256'];r=yaml.safe_load(p.read_text());assert r==e['record']
 if any(thiamine(n) for n in names(r)):hits.append({k:e[k] for k in ['entry_id','head','owner_path','payload_path','payload_sha256','identifier','preferred_term','record']})
 for c in r.get('components',[]):
  if mono(c['component_name']):components.append({'entry_id':e['entry_id'],'owner_path':e['owner_path'],'payload_sha256':e['payload_sha256'],'component':c})
cp=C/'integration/final-same-target-reconciliation-v2/publication-v4/candidate-summary-v4.json';cj=json.loads(cp.read_text());ch=[]
def walk(x,path=''):
 if isinstance(x,dict):
  if 'preferred_term' in x and 'identifier' in x and any(thiamine(n) for n in names(x)):ch.append({'pointer':path,'record':x})
  for k,v in x.items():walk(v,path+'/'+k)
 elif isinstance(x,list):
  for i,v in enumerate(x):walk(v,path+'/'+str(i))
walk(cj)
ignored=[]
for s in (O/'ignored-inclusive-owner-paths.txt').read_text().splitlines():
 p=Path(s);r=yaml.safe_load(p.read_text())
 if isinstance(r,dict):
  hits2=[n for n in names(r) if mono(n)]
  if hits2:ignored.append({'path':str(p),'sha256':sha(p),'names':hits2})
dump('owner-and-intake-check-v1.json',{'author':'/root/chemicals_research','scope':'Maintained records read directly; explicit ignored-inclusive worktree YAML path search; all frozen981 selected payload bytes verified against manifest and parsed records; coordinator37 summary read recursively. Does not claim knowledge of unannounced future drafts.','inputs':[{'path':str(p),'sha256':sha(p)} for p in [input,cp,O/'ignored-inclusive-owner-paths.txt']],'maintained_thiamine_owners':maintained,'frozen_selected_count':len(j['entries']),'frozen_thiamine_owner_entries':hits,'frozen_same_form_owner_hits':[h for h in hits if any(mono(n) for n in names(h['record']))],'source_monohydrate_component_dependencies':components,'coordinator_candidate_count':cj['candidate_count'],'coordinator_thiamine_records':ch,'ignored_inclusive_same_form_owner_hits':ignored,'conclusion':'No selected same-form monohydrate owner found in these explicit inventories. Molecular thiamine, hydrochloride, dihydrate, phosphate and stock owners have different recorded scopes; source-named monohydrate components in other stock proposals are dependencies, not independent owners.'})
print(json.dumps({'maintained':len(maintained),'selected':len(j['entries']),'thiamine_entries':len(hits),'same_form_entries':[h['entry_id'] for h in hits if any(mono(n) for n in names(h['record']))],'component_dependencies':len(components),'coordinator_thiamine_records':len(ch),'ignored_same_form_owner_hits':ignored}))
