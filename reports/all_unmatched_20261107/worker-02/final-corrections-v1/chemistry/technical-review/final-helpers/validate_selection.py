"""Native strict writer/roundtrip and full projected catalog validation.

Read-only maintained inputs, exclusive private diagnostic output; no export.
"""
import argparse,hashlib,json,sys
from collections import Counter,defaultdict
from datetime import datetime,timezone
from pathlib import Path
W=Path(__file__).resolve().parents[4];R=Path(__file__).resolve().parent;A=R.parent
sys.path.insert(0,str(W/'src'))
import yaml
from mediaingredientmech.curate.publication_guard import FrozenFile,no_alias
from mediaingredientmech.validation.write_validated import write_validated_ingredient,ValidationFailedError
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def confined(path,root):
 if '..' in path.parts or '..' in root.parts:raise ValueError('Traversal in output path')
 path=path.absolute();root=root.absolute();no_alias(root);no_alias(path)
 if path!=path.resolve() or root!=root.resolve() or not path.resolve().is_relative_to(root.resolve()):raise ValueError('Output outside private review root')
 return path
def verify_proposals(proposals,catalog,hashes):
 owners=set();ids=set();values={};snapshots=[]
 for p in proposals:
  if p['proposal_id'] in ids or p['owner_path'] in owners:raise ValueError('Duplicate proposal or owner')
  ids.add(p['proposal_id']);owners.add(p['owner_path']);owner=p['owner_path']
  rel=Path(owner)
  if rel.parts[:2]!=('data','ingredients') or len(rel.parts)!=4 or rel.parts[2] not in ['mapped','unmapped'] or rel.suffix!='.yaml':raise ValueError('Invalid owner target')
  if p['kind']=='edit_existing_owner':
   if owner not in hashes or hashes[owner]!=p['before_sha256']:raise ValueError('Stale authentic owner preimage')
  elif p['kind']=='new_owner':
   if owner in catalog or p['before_sha256'] is not None:raise ValueError('New owner collides with current path')
  else:raise ValueError('Unknown proposal kind')
  cap=p['after_capture'];relative=Path(cap['path'])
  if cap['root']!='artifact' or relative.is_absolute() or '..' in relative.parts:raise ValueError('Invalid payload path')
  path=A/relative;frozen=FrozenFile.capture(path)
  if hashlib.sha256(frozen.content).hexdigest()!=cap['sha256']:raise ValueError('Stale payload hash')
  value=yaml.safe_load(frozen.content);history=(catalog.get(owner) or {}).get('curation_history',[])
  if value.get('curation_history',[])[:len(history)]!=history:raise ValueError('Authentic curation history changed')
  if len(value.get('curation_history',[]))<=len(history):raise ValueError('Missing new event')
  if not all(e.get('llm_assisted') is True for e in value['curation_history'][len(history):]):raise ValueError('Missing truthful agent history')
  snapshots.append(frozen);values[owner]=value
 return values,snapshots
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--selection',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);args=ap.parse_args()
 output=confined(args.out,W/'.temp/w02-final-corrections-v1');output.mkdir(parents=True,exist_ok=False)
 props_path=args.selection/'proposals.json';held=FrozenFile.capture(props_path);props=json.loads(held.content)['proposals']
 catalog={str(p.relative_to(W)):yaml.safe_load(p.read_text()) for p in sorted((W/'data/ingredients').glob('*/*.yaml'))}
 hashes={p:sha(W/p) for p in catalog};catalog_snapshots=[FrozenFile.capture(W/p) for p in catalog]
 baseline=validate_component_partonomy(catalog.values());values,snapshots=verify_proposals(props,catalog,hashes)
 results=[]
 for i,p in enumerate(props):
  path=output/'native-roundtrip'/f'{i:03d}.yaml';value=values[p['owner_path']]
  write_validated_ingredient(value,path)
  if yaml.safe_load(path.read_text())!=value:raise ValueError('Native roundtrip changed record')
  results.append({'proposal_id':p['proposal_id'],'after_capture':p['after_capture'],'owner_path':p['owner_path'],'roundtrip_path':str(path),'roundtrip_sha256':sha(path),'status':'passed'})
 overlay=catalog|values;violations=validate_component_partonomy(overlay.values())
 before=defaultdict(list);after=defaultdict(list)
 for p,v in catalog.items():before[v['identifier']].append(p)
 for p,v in overlay.items():after[v['identifier']].append(p)
 collisions=[{'identifier':i,'baseline_paths':before[i],'projected_paths':paths,'new_collision':set(paths)!=set(before[i])} for i,paths in after.items() if len(paths)>1 and any(p in values for p in paths)]
 probe=dict(next(iter(values.values())));probe['unexpected_worker_probe']=True;bad=output/'invalid-probe.yaml'
 try:write_validated_ingredient(probe,bad)
 except ValidationFailedError:negative=not bad.exists()
 else:negative=False
 assert negative,'Native invalid-field write accepted'
 for frozen in [held,*snapshots,*catalog_snapshots]:frozen.verify()
 receipt={'checked_at':datetime.now(timezone.utc).isoformat(),'command':sys.argv,'selection':str(args.selection),'proposal_ledger_sha256':sha(props_path),'catalog_count':len(catalog),'catalog_hashes':hashes,'payload_count':len(props),'payloads':results,'baseline_partonomy_violations':[str(x) for x in baseline],'projected_partonomy_violations':[str(x) for x in violations],'identifier_collisions':collisions,'negative_unknown_field_rejected':negative,'all_snapshot_inputs_unchanged':True,'scientific_or_release_approval':False,'limits':'Native schema/partonomy and exact file/content assertions only; historical collisions retained, source-local components do not establish global equivalence. No canonical data or exports are written.'}
 with (output/'receipt.json').open('x') as f:json.dump(receipt,f,indent=2);f.write('\n')
 print(json.dumps({'payloads':len(props),'baseline_partonomy':len(baseline),'projected_partonomy':len(violations),'new_collisions':sum(x['new_collision'] for x in collisions),'invalid_write_rejected':negative}))
 return bool(violations or any(x['new_collision'] for x in collisions))
if __name__=='__main__':raise SystemExit(main())
