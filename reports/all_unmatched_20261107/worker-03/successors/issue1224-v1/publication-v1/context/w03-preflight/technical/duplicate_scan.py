"""Bounded gitignore-independent inventory; no identity decisions or source edits."""
from pathlib import Path
import hashlib,json,re,datetime
import yaml
ROOT=Path.cwd();C=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107')
OUT=ROOT/'.temp/w03-oxoid-successor-v1/technical';INTAKE=C/'preflight/final-intake-candidate-v1';V4=C/'integration/final-same-target-reconciliation-v2/publication-v4'
PAT=re.compile(r'cm0?149|reinforced[ _-]*clostridial|\brcm\b',re.I)
IDENT='kgmicrobe.ingredient:reinforced_clostridial_medium_oxoid_cm0149';DEST='data/ingredients/mapped/reinforced_clostridial_medium_oxoid_cm0149.yaml'
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
files=[];hits=[];skipped=[]
for tree in [ROOT/'data/ingredients',ROOT/'data/curated']:
 for p in sorted(tree.rglob('*')):
  if p.is_symlink():skipped.append({'path':str(p),'reason':'symlink not traversed'});continue
  if not p.is_file():continue
  b=p.read_bytes();files.append({'path':str(p),'sha256':h(p),'bytes':len(b)})
  try:t=b.decode('utf-8')
  except UnicodeDecodeError:skipped.append({'path':str(p),'reason':'non-UTF8 bytes hashed but not lexical-searched'});continue
  found=[{'line':i+1,'text':line} for i,line in enumerate(t.splitlines()) if PAT.search(line) or IDENT in line or DEST in line]
  if found:
   native=p.parent in [ROOT/'data/ingredients/mapped',ROOT/'data/ingredients/unmapped'] and p.suffix=='.yaml'
   rec=yaml.safe_load(t) if native else None
   hits.append({'path':str(p.relative_to(ROOT)),'sha256':h(p),'classification':'native_direct_child_owner' if native else 'maintained_surface_or_nonowner_context','identifier':rec.get('identifier') if rec else None,'preferred_term':rec.get('preferred_term') if rec else None,'mapping_status':rec.get('mapping_status') if rec else None,'matches':found})
p=ROOT/'docs/data/label_index.csv';files.append({'path':str(p),'sha256':h(p),'bytes':p.stat().st_size});hits.append({'path':str(p.relative_to(ROOT)),'sha256':h(p),'classification':'derived_label_index_context','matches':[{'line':i+1,'text':line} for i,line in enumerate(p.read_text().splitlines()) if PAT.search(line) or IDENT in line or DEST in line]})
f=INTAKE/'all-active-proposal-entries-v1.json';j=json.loads(f.read_text());files.append({'path':str(f),'sha256':h(f),'bytes':f.stat().st_size});intakehits=[];fail=[]
for row in j['entries']:
 p=INTAKE/row['payload_path'];actual=h(p);files.append({'path':str(p),'sha256':actual,'bytes':p.stat().st_size})
 if actual!=row['payload_sha256']:fail.append(str(p))
 if PAT.search(p.read_text()) or IDENT in p.read_text() or DEST in row['owner_path']:
  intakehits.append({'entry_id':row['entry_id'],'head':row['head'],'kind':row['kind'],'owner_path':row['owner_path'],'identifier':row['identifier'],'preferred_term':row['preferred_term'],'payload_path':str(p),'payload_sha256':actual,'case_ids':row['case_ids'],'matches':[{'line':i+1,'text':line} for i,line in enumerate(p.read_text().splitlines()) if PAT.search(line) or IDENT in line]})
v4hits=[]
for p in sorted((V4/'candidates').rglob('*.yaml')):
 files.append({'path':str(p),'sha256':h(p),'bytes':p.stat().st_size})
 if PAT.search(p.read_text()) or IDENT in p.read_text():
  r=yaml.safe_load(p.read_text());v4hits.append({'path':str(p),'sha256':h(p),'identifier':r['identifier'],'preferred_term':r['preferred_term'],'matches':[{'line':i+1,'text':line} for i,line in enumerate(p.read_text().splitlines()) if PAT.search(line) or IDENT in line]})
exact=[]
for folder in ['mapped','unmapped']:
 for p in sorted((ROOT/'data/ingredients'/folder).glob('*.yaml')):
  r=yaml.safe_load(p.read_text())
  if r.get('identifier')==IDENT:exact.append({'path':str(p),'sha256':h(p),'mapping_status':r.get('mapping_status')})
result={'reviewer':'/root/oxoid_contract','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'search_method':'Path.rglob filesystem traversal independent of gitignore/ignore; all regular files including hidden/ignored under data/ingredients and data/curated; explicit derived label_index; exact payload paths of every frozen intake entry; v4 candidates only. No credentials/private unrelated roots. Symlinks not traversed.','lexical_pattern':PAT.pattern,'boundaries':['data/ingredients/**','data/curated/**','docs/data/label_index.csv',str(f)+' entries[*].payload_path',str(V4/'candidates/**/*.yaml')],'native_direct_child_definition':'*.yaml immediately beneath data/ingredients/mapped or unmapped; nested research/backups are not owner identities.','scanned_file_count_including_repeated_paths':len(files),'files':files,'skipped':skipped,'maintained_and_derived_hits':hits,'frozen_intake_proposal_count':len(j['entries']),'frozen_intake_hash_mismatches':fail,'frozen_intake_hits':intakehits,'v4_candidate_yaml_count':len(list((V4/'candidates').rglob('*.yaml'))),'v4_hits':v4hits,'exact_identifier_native_owners':exact,'prospective_path_exists':(ROOT/DEST).exists(),'scope_caution':'Lexical hits are leads, not equality; authentic old mixed RCM owner retains Oxoid CM149 historical alias and W05 Difco source proposal. New Oxoid identity/path found in coordinator proposal packet is intended origin, not maintained-existing-owner. No assertion about arbitrary historical/private files outside boundaries; no scientific selection/approval.'}
(OUT/'duplicate-scan.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'scanned_files':len(files),'nativehits':[r['path'] for r in hits if r['classification']=='native_direct_child_owner'],'intakehits':[r['entry_id'] for r in intakehits],'v4hits':[r['path'] for r in v4hits],'exact_identifier_native_owners':exact,'prospective_path_exists':result['prospective_path_exists'],'hash_failures':fail,'skipped':skipped},indent=2))
