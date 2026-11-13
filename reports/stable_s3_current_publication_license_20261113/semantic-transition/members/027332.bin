"""2026-11-12: guarded private copy of the existing diagnostic retirement input.

Only path qualification, the current policy pin, and explicit copy provenance
change. Exact canonical, sodium-stock owner, row and historical evidence must
match original pins. Uses existing native PreparationTree; no scientific approval,
generator, source application, native process, HEAD/index/review mutation or tests.
"""
import copy, csv, datetime, hashlib, io, json, subprocess, sys, types
from pathlib import Path
sys.dont_write_bytecode=True
OUT=Path(__file__).resolve().parent;C=OUT.parent.parent
S=C/'integration/stable-source-successor-real-canary-target'
TC=C/'integration/stable-adoption-real-canary-target'
CC=C/'integration/stable-cas-preservation-claw-worktree'
OLD='.temp/stable-registry-retirement1189-proposal-v1'
NEW='.temp/stable-registry-retirement1189-proposal-source-successor-v1'
HEAD='c65da18a098842f4bb4c2bd57fc572d2771ccc81'
CCHEAD='f604127114146320f5a92529cc62f190d0a0c25f'
sys.path.insert(0,str(S/'src'))
from mediaingredientmech.curate.stable_id_adoption import PreparationTree
from mediaingredientmech.curate.publication_guard import FrozenFile
def sha(b):return hashlib.sha256(b).hexdigest()
def encoded(x):return (json.dumps(x,sort_keys=True,indent=2,ensure_ascii=False)+'\n').encode()
def git(root,*args):return subprocess.check_output(['git',*args],cwd=root).decode().strip()
def pin(p):
 b=p.read_bytes();return {'path':str(p),'sha256':sha(b),'bytes':len(b)}
def differences(a,b,path=''):
 if isinstance(a,dict) and isinstance(b,dict):
  return [x for k in sorted(a.keys()|b.keys()) for x in (differences(a[k],b[k],path+'/'+k) if k in a and k in b else [{'path':path+'/'+k,'before_present':k in a,'before':a.get(k),'after_present':k in b,'after':b.get(k)}])]
 if isinstance(a,list) and isinstance(b,list) and len(a)==len(b):return [x for i,(u,v) in enumerate(zip(a,b)) for x in differences(u,v,path+'/'+str(i))]
 return [] if a==b else [{'path':path,'before':a,'after':b}]
def main():
 assert git(S,'rev-parse','HEAD')==HEAD and git(CC,'rev-parse','HEAD')==CCHEAD
 index_before=git(S,'diff','--cached','--binary','HEAD')
 source=FrozenFile.capture(TC/OLD/'PROPOSAL.json');old=json.loads(source.content)
 captured=[source];original_files={}
 for name,expected in old['evidence_inputs'].items():
  f=FrozenFile.capture(TC/name);assert sha(f.content)==expected;captured.append(f);original_files[name]=f
 current={}
 for ref in [old['canonical'],*[e['owner'] for e in old['entries']]]:
  f=FrozenFile.capture(S/ref['path']);assert sha(f.content)==ref['sha256'],'Changed current canonical/owner: '+ref['path'];captured.append(f);current[ref['path']]=f
 current_policy=FrozenFile.capture(S/'MAPPING_SEMANTICS.md');captured.append(current_policy)
 loader_file=FrozenFile.capture(CC/'src/kg_microbe_utils/stable_mim.py');captured.append(loader_file)
 native_writer=[FrozenFile.capture(S/name) for name in ['src/mediaingredientmech/curate/stable_id_adoption.py','src/mediaingredientmech/curate/adoption_filesystem.py','src/mediaingredientmech/curate/publication_guard.py']];captured.extend(native_writer)
 rows=list(csv.DictReader(io.StringIO(''.join(x for x in current[old['canonical']['path']].content.decode().splitlines(True) if not x.startswith('#'))),delimiter='\t'))
 assert len(old['entries'])==1
 for entry in old['entries']:assert rows[entry['row_position']-1]==entry['row']
 tree=PreparationTree(S,S/NEW)
 copied=[];mapping={}
 for name,f in original_files.items():
  relative='evidence/original-MAPPING_SEMANTICS.md' if name=='MAPPING_SEMANTICS.md' else str(Path(name).relative_to(OLD))
  result=tree.put(relative,f.content);copied.append({'source':pin(f.path),'destination':pin(result.path)})
  if name!='MAPPING_SEMANTICS.md':mapping[name]=NEW+'/'+relative
 result=tree.put('ORIGINAL-PROPOSAL.json',source.content);copied.append({'source':pin(source.path),'destination':pin(result.path)})
 provenance={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'purpose':'Exact diagnostic proposal copy to source-successor target, not scientific approval','original_root':str(TC),'target_root':str(S),'target_head':HEAD,'selected_claw_root':str(CC),'selected_claw_head':CCHEAD,'original_proposal':pin(source.path),'copies':copied,'current_policy':pin(current_policy.path),'original_policy':pin(TC/'MAPPING_SEMANTICS.md'),'unchanged_current_canonical':pin(current[old['canonical']['path']].path),'unchanged_current_owner':[pin(current[e['owner']['path']].path) for e in old['entries']],'allowed_adaptation':['Qualify copied evidence paths under the new private target directory.','Bind MAPPING_SEMANTICS.md to actual current S bytes; preserve the complete previous policy as historical evidence.','Add this copy provenance and byte-identical original proposal to the existing evidence list.'],'scientific_approval':False,'row_owner_canonical_reason_author_unchanged':True,'native_generation':False,'script':pin(Path(__file__)),'guarded_writers':[pin(x.path) for x in native_writer]}
 provenance_ref=tree.put('ADAPTATION-PROVENANCE.json',encoded(provenance))
 new=copy.deepcopy(old)
 new['evidence_inputs']={mapping.get(n,n):(sha(current_policy.content) if n=='MAPPING_SEMANTICS.md' else h) for n,h in old['evidence_inputs'].items()}
 extras={NEW+'/evidence/original-MAPPING_SEMANTICS.md':old['evidence_inputs']['MAPPING_SEMANTICS.md'],NEW+'/ORIGINAL-PROPOSAL.json':sha(source.content),NEW+'/ADAPTATION-PROVENANCE.json':sha(provenance_ref.content)}
 new['evidence_inputs'].update(extras)
 for entry in new['entries']:entry['evidence']=[mapping.get(n,n) for n in entry['evidence']]+list(extras)
 for k in set(old)-{'evidence_inputs','entries'}:assert old[k]==new[k]
 for a,b in zip(old['entries'],new['entries']):
  for k in set(a)-{'evidence'}:assert a[k]==b[k]
 proposal_raw=encoded(new);proposal_path=S/NEW/'PROPOSAL.json'
 module=types.ModuleType('captured_claw_diagnostic_proposal_loader');module.__file__=str(loader_file.path)
 exec(compile(loader_file.content,str(loader_file.path),'exec'),module.__dict__)
 paths,parsed=module.registry_retirement_inputs(S,proposal_path,proposal_raw,sha(proposal_raw));assert parsed==new
 snapshot={p:(proposal_raw if p==proposal_path else FrozenFile.capture(p).content) for p in paths}
 proof=module.registry_retirement_evidence(S,proposal_path,proposal_raw,sha(proposal_raw),snapshot)
 assert proof['scientific_approval_added'] is False
 for f in captured:f.verify()
 assert git(S,'rev-parse','HEAD')==HEAD and git(CC,'rev-parse','HEAD')==CCHEAD
 assert git(S,'diff','--cached','--binary','HEAD')==index_before
 tree.put('PROPOSAL.json',proposal_raw)
 diff=differences(old,new)
 tree.put('ADAPTATION-DIFF.json',encoded({'original':pin(source.path),'adapted':pin(proposal_path),'differences':diff,'only_path_policy_and_copy_provenance_adaptation':True,'unchanged':['schema_version','capability','scope','author','canonical','scientific_approval','entries[*].row_position','entries[*].row','entries[*].owner','entries[*].reason'],'new_scientific_decision':False}))
 for f in captured:f.verify()
 tree.check()
 result={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'DIAGNOSTIC_PROPOSAL_COPY_READY_FOR_INDEPENDENT_READBACK_NOT_APPROVAL','proposal':pin(proposal_path),'adaptation_diff':pin(S/NEW/'ADAPTATION-DIFF.json'),'copy_provenance':pin(S/NEW/'ADAPTATION-PROVENANCE.json'),'original_proposal':pin(source.path),'original_policy_sha256':old['evidence_inputs']['MAPPING_SEMANTICS.md'],'current_policy_sha256':sha(current_policy.content),'claw_loader':pin(loader_file.path),'claw_head':CCHEAD,'native_loader_closed_shape_and_complete_evidence_check':'PASS','original_evidence_bytes_unchanged':True,'canonical_owner_row_unchanged':True,'source_or_index_or_head_mutation':False,'scientific_approval':False,'generation_run':False,'next':'Separate skeptical readback; coordinator may then bind this diagnostic input to actual native generation. Full-row installation/removal and release review remain mandatory.'}
 with (OUT/'RETIREMENT-ADAPTATION-HANDOFF.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
 print(json.dumps({'handoff':pin(OUT/'RETIREMENT-ADAPTATION-HANDOFF.json'),'proposal':pin(proposal_path),'diff':result['adaptation_diff']}))
if __name__=='__main__':main()
