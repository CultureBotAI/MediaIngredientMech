from pathlib import Path
import json,hashlib,copy,shutil,yaml
from datetime import datetime,timezone
from mediaingredientmech.validation.write_validated import write_validated_ingredient
P=Path('reports/all_unmatched_20261107/worker-10');K=P/'successor-v1/chemicals';H=K/'history/author-v1';H.mkdir(parents=True,exist_ok=False)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for n in ['decisions.json','evidence.json','proposals.json','guarded-write-receipt.json']:shutil.copyfile(K/n,H/n)
shutil.copytree(K/'proposed',H/'proposed')
fixes={'Neither the free-acid owner nor':'Neither the existing benzylpenicillin-sodium owner (CHEBI:51765) nor','explicitly uses EDTA-Na2 dihydrate':'prints EDTA-Na x 2 H2O (sodium-EDTA dihydrate notation; sodium stoichiometry is not explicit)'}
def fix(x):
 if isinstance(x,str):
  for a,b in fixes.items():x=x.replace(a,b)
  return x
 if isinstance(x,list):return [fix(v) for v in x]
 if isinstance(x,dict):return {k:fix(v) for k,v in x.items()}
 return x
D=fix(json.loads((K/'decisions.json').read_text()));E=json.loads((K/'evidence.json').read_text());PR=fix(json.loads((K/'proposals.json').read_text()))
base=next(e for e in E['evidence'] if e['evidence_id']=='sv1-chem-supplier-web-open');web=json.loads((K/'supplier-web-open.json').read_text());E['evidence'].remove(base)
for j,key in enumerate(['aspartate','vanadate']):
 e=copy.deepcopy(base);e.update(evidence_id=base['evidence_id']+'-'+key,url=web['urls'][j],accessed_at=web['at'],locator=('First response (S)-2-Aminosuccinic acid, sodium salt: lines20-45,63-69' if j==0 else 'Second response Sodium metavanadate xhydrate: product heading, CAS, formula, mass and InChI fields'));E['evidence'].append(e)
for d in D['decisions']:
 key='vanadate' if 'sv1-chem-atcc-cens' in d['evidence_ids'] else 'aspartate'
 for seq in [d['evidence_ids'],d['completion_reassessment']['actual_primary_search_evidence_ids']]:
  for i,x in enumerate(seq):
   if x==base['evidence_id']:seq[i]=x+'-'+key
for e in E['evidence']:
 if e['evidence_id']=='sv1-chem-huber-1986-pdf':e.update(kind='unsuccessful_search',locator='Attempted publisher PDF URL returned HTML article abstract/access page, not PDF recipe text',supports_or_contradicts='Full-text retrieval did not establish MMS nickel-reagent hydration. Exact returned HTML retained; no primary full-recipe evidence claimed.')
 if e['evidence_id']=='sv1-chem-huber-1986':e['locator']='Publisher HTML title and abstract; no MMS composition available in inspected abstract'
changes=[]
for p in PR['proposals']:
 f=P/p['after_capture']['path'];before=sha(f);o=yaml.safe_load(f.read_text());r=fix(o)
 if r!=o:
  scratch=Path('.temp/all-unmatched-worker-10/successor-v1/chemicals-guarded')/f.name;write_validated_ingredient(r,scratch);f.write_bytes(scratch.read_bytes());p['after_capture']['sha256']=sha(f);changes.append({'proposal_id':p['proposal_id'],'before':before,'after':sha(f)})
for n,o in [('decisions',D),('evidence',E),('proposals',PR)]: (K/(n+'.json')).write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n')
r={'at':datetime.now(timezone.utc).isoformat(),'initial_archive':str(H),'changes':changes,'fixes':fixes,'evidence_corrections':['Supplier capture retains exact bytes and original at; two response-specific URL entries','Huber PDF attempt classified as unsuccessful full-text retrieval'], 'current_hashes':{n:sha(K/n) for n in ['decisions.json','evidence.json','proposals.json']}}
(K/'revision-v2.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
