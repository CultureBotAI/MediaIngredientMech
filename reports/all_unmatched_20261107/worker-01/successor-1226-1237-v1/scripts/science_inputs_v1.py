"""Read-only input binding and ignored-independent preferred-name check; exclusive receipt."""
from pathlib import Path
import hashlib, json, sys, datetime, subprocess
import yaml
sys.path.insert(0, str(Path.cwd() / 'src'))
from mediaingredientmech.synonym_policy import preferred_term_owners

D=Path('reports/all_unmatched_20261107/worker-01/successor-1226-1237-v1')
C=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107')
I=C/'preflight/final-intake-candidate-v1'
S=C/'queue/preliminary-v5'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p): return json.loads(Path(p).read_text())
def receipt(name,o):
 p=D/'science'/name;p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('x') as f: json.dump(o,f,indent=2,ensure_ascii=False);f.write('\n')
origins=load(D/'inputs/w01-origin-bindings.json')
assert sha(D/'inputs/w01-author-task-DRAFT-v2.md')=='8e4ae5537bd6ae6f33c1da550d9d306f4ca7440ada0f88f4f92024d1536cbbaa'
head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()
assert head=='26445f23b5a905ac26d864acfbd658570c88769c'
bindings=[]
for r in origins:
 p=I/r['payload_path']; local=Path(r['payload_path'].split('snapshot/workers/w01/')[1])
 assert sha(p)==sha(local)==r['payload_sha256']
 assert yaml.safe_load(p.read_text())==r['record']
 bindings.append({'proposal_id':r['proposal_id'],'frozen_path':str(p),'current_path':str(local),'sha256':sha(p),'complete_record_equal_origin':True,'case_bindings':r['case_bindings']})
captures=[]
for r in load(D/'inputs/w01-primary-locators.json'):
 assert sha(r['path'])==r['sha256'];captures.append(r)
E=load('reports/all_unmatched_20261107/worker-01/shard/evidence.json')['evidence']
primary_ids={'NS-P-nbrc-1020','NS-P-nbrc-824','NS-P-jcm-317','NS-P-jcm-1425','CS-P-JCM-1430','CS-P-JCM-1431','CS-P-NBRC-1321','NS-P-nbrc-1257'}
primary=[]
for e in E:
 if e['evidence_id'] not in primary_ids:continue
 p=I/'snapshot/workers/w01/reports/all_unmatched_20261107/worker-01'/e['capture']['path']
 assert sha(p)==e['capture']['sha256']
 primary.append({'frozen_absolute_path':str(p),**e})
recipes=[]
for r in origins:
 for e in r['evidence']:
  c=e['capture']
  if c['root']=='source':
   p=S/c['path'];assert sha(p)==c['sha256'];recipes.append({'proposal_id':r['proposal_id'],'absolute_path':str(p),**e})
tokens=['0.01 M FeSO4·7H2O solution (in 0.02 N HCl)','Bicarbonate solution (1.0 M)***','Bicarbonate solution***']
records={}; inventory=[];name_hits=[]
for p in sorted(Path('data/ingredients').rglob('*.yaml')):
 # Path.rglob includes hidden/ignored files; no gitignore filtering.
 b=p.read_bytes();r=yaml.load(b,Loader=yaml.CSafeLoader)
 inventory.append({'path':str(p),'sha256':hashlib.sha256(b).hexdigest()})
 if p.parent.name=='mapped':records[str(p)]=r
 for token in tokens:
  for field,value in [('preferred_term',r.get('preferred_term')),*[('synonyms',s.get('synonym_text')) for s in r.get('synonyms',[]) or []]]:
   if str(value or '').strip().casefold()==token.casefold(): name_hits.append({'token':token,'path':str(p),'field':field,'identifier':r.get('identifier'),'mapping_status':r.get('mapping_status'),'sha256':inventory[-1]['sha256']})
owners=preferred_term_owners(records)
worker_proposals=load('reports/all_unmatched_20261107/worker-01/shard/proposals.json')['proposals']
proposal_inventory=[];proposal_name_hits=[]
for p in worker_proposals:
 f=Path('reports/all_unmatched_20261107/worker-01')/p['after_capture']['path'];assert sha(f)==p['after_capture']['sha256'];r=yaml.load(f.read_bytes(),Loader=yaml.CSafeLoader)
 proposal_inventory.append({'proposal_id':p['proposal_id'],'path':str(f),'sha256':sha(f)})
 for t in tokens:
  if str(r.get('preferred_term') or '').strip().casefold()==t.casefold():proposal_name_hits.append({'token':t,'proposal_id':p['proposal_id'],'identifier':r['identifier']})
receipt('input-bindings-and-owned-name-check-v1.json',{
 'schema_version':1,'author':'Codex /root/primary_context (worker01)','checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'head':head,
 'scope':'Four assigned successor payloads; current maintained mapped/unmapped directory names and all 76 worker01 selected proposal preferred names. Other workers/successors are not asserted current or globally collision-free.',
 'input_files':[{'path':str(p),'sha256':sha(p)} for p in sorted((D/'inputs').glob('*')) if p.is_file()],
 'payload_bindings':bindings,'primary_locators':captures,'primary_receipts_original_access_times':primary,'complete_frozen_recipe_bindings':recipes,
 'owned_name_search':{'ignored_files_included':True,'enumeration':'Path.rglob over data/ingredients (no ignore filtering); native preferred_term_owners exact stripped casefold; no chemical normalization conflation','tokens':tokens,'mapped_record_count':len(records),'maintained_record_inventory':inventory,'exact_label_and_synonym_hits':name_hits,'native_preferred_owner_hits':{t:sorted(owners.get(t.casefold(),[])) for t in tokens},'selected_worker_proposal_count':len(proposal_inventory),'selected_worker_proposal_inventory':proposal_inventory,'selected_proposal_preferred_hits':proposal_name_hits},
 'limitations':['A missing exact preferred-owner token does not establish substance identity or whole-catalog scientific approval.','This input check supplies no independent review; the author read the complete primary and frozen source records separately.','Original capture accessed_at times are retained; these are readbacks, not new web retrievals.']})
print(json.dumps({'maintained_records':len(inventory),'mapped_records':len(records),'selected_proposals':len(proposal_inventory),'preferred_owner_hits':{t:sorted(owners.get(t.casefold(),[])) for t in tokens},'exact_hits':name_hits,'proposal_preferred_hits':proposal_name_hits},ensure_ascii=False))
