"""#1131 deterministic private completion-boundary controls; no real publication."""
from pathlib import Path
import copy
import hashlib
import importlib.util
import json
import os
import sys

os.environ['GIT_OPTIONAL_LOCKS']='0'  # All private Git metadata reads remain read-only.
C=Path(__file__).resolve().parent
D=next(p for p in C.parents if (p/'promote_deferred_aliases_v2.py').is_file())
RUN=D.parent;W=RUN/'step8-aliases';OP=D/'promote_deferred_aliases_v2.py'
spec=importlib.util.spec_from_file_location('late1131_operator',OP)
op=importlib.util.module_from_spec(spec);sys.modules[spec.name]=op
exec(compile(OP.read_bytes(),str(OP),'exec'),op.__dict__)

def put(path,raw):
 path.parent.mkdir(parents=True,exist_ok=True)
 with path.open('xb') as stream:stream.write(raw)

def main():
 assert not (C/'results.json').exists()
 p=op.prepare(W,W/'output/next23-native-candidate-v1',RUN/'step7c-claw','112e2303176db3530f88469f220367f14041d7ae9a84d879efe8623255e6fa34')
 native,publication,context,chain=p['modules']
 actual_inputs={path:op.digest(raw) for path,raw in p['inputs'].items()}
 actual_outputs={name:op.digest(op.regular(W/name)) for name in p['before']}
 actual_membership=context.source_inventory(W)
 results=[]
 def fixture(name):
  root=C/name;root.mkdir()
  def remap(path):return root/path.relative_to(W) if path.is_relative_to(W) else path
  f=dict(p);f['root']=root;f['bundle']=remap(p['bundle'])
  f['inputs']={remap(path):raw for path,raw in p['inputs'].items()}
  g=dict(p['generation']);f['generation']=g
  g['archive']=remap(g['archive'])
  for key in ('original_files','archive_files','label_paths'):g[key]={remap(path) for path in g[key]}
  # Private absent-input analogues retain a frozen absence set without touching sibling inputs.
  g['absent']={root/'captured-absence'/str(i)/path.name for i,path in enumerate(sorted(g['absent']))}
  for path,raw in f['inputs'].items():
   if path.is_relative_to(root):put(path,raw)
  for name,raw in p['before'].items():put(root/name,raw)
  (root/op.LOG).parent.mkdir(parents=True)
  return f
 def reject(name,call,substring):
  try:call()
  except Exception as error:
   assert substring in str(error),(name,substring,repr(error))
   results.append({'name':name,'outcome':'rejected','exception':type(error).__name__,'message':str(error)})
  else:raise AssertionError(name+' unexpectedly certified completion')
 def after_publish_case(name,inject,substring):
  f=fixture(name);original=publication.publish;called=[]
  def hook(*args,**kwargs):
   answer=original(*args,**kwargs);assert args[0]==f['root'] and kwargs['apply'] is True
   inject(f);called.append(True);return answer
  publication.publish=hook
  try:reject(name,lambda:op.publish_prepared(f,apply=True),substring)
  finally:publication.publish=original
  assert called==[True]
  # Native transaction itself succeeded; failure is accurately at completion verification.
  saved=op.read_json(op.regular(f['root']/op.LOG))
  assert saved['state']=='complete' and all(op.regular(f['root']/name)==raw for name,raw in f['outputs'].items())
  put(C/(name+'-rejection.json'),op.encoded({'fault_after_native_publication':True,'immediate_completion_rejected':True,
      'native_transaction_log':str(f['root']/op.LOG),'native_transaction_log_sha256':op.digest(op.regular(f['root']/op.LOG)),
      'fault_is_not_a_scientific_mapping_change':True,'result':results[-1]}))
  return f
 def add(f):put(f['root']/'data/ingredients/mapped/.late-1131-owner.yaml',b'preferred_term: late private owner\n')
 def remove(f):
  name=f['source_paths']['data/ingredients'][0];(f['root']/name).rename(C/(f['root'].name+'-removed-owner.yaml'))
 def alias(f):
  name=f['source_paths']['data/ingredients'][0];path=f['root']/name;target=C/(f['root'].name+'-alias-original.yaml')
  path.rename(target);path.symlink_to(target)
 after_publish_case('late-hidden-owner-addition',add,'completed source membership changed')
 after_publish_case('late-owner-removal',remove,'completed source membership changed')
 after_publish_case('late-owner-symlink-alias',alias,'aliased source inventory member')
 positive=fixture('positive-private-publication')
 answer=op.publish_prepared(positive,apply=True)
 assert answer['completed_verification']['state']=='verified-complete'
 results.append({'name':'ordinary-private-publication','outcome':'passed','detail':answer['completed_verification']})
 root=positive['root'];g=positive['generation']
 # Each following late fault is injected into a completed private fixture and preserved separately.
 def created_case(name,path,raw,expected):
  put(path,raw);reject(name,lambda:op.verify_completed(positive,root/op.LOG),expected)
  path.rename(C/(name+'-injected-file'))
 created_case('late-aggregate-addition',root/'data/curated/.late-1131.yaml',b'ingredients: []\n','completed source membership changed')
 created_case('late-original-generation-addition',positive['bundle']/'.late-1131.json',b'{}\n','completed generation membership changed')
 created_case('late-label-addition',positive['bundle']/'label-input-99.json',b'{}\n','completed generation membership changed')
 path=next(iter(sorted(g['archive_files'])));saved_path=C/'late-archive-removal-original';path.rename(saved_path)
 reject('late-archive-removal',lambda:op.verify_completed(positive,root/op.LOG),'completed generation membership changed')
 saved_path.rename(path)
 label=next(iter(sorted(g['label_paths'])));saved_label=C/'late-label-removal-original';label.rename(saved_label)
 reject('late-label-removal',lambda:op.verify_completed(positive,root/op.LOG),'completed generation membership changed')
 saved_label.rename(label)
 archive_path=next(iter(sorted(g['archive_files'])));target=C/'late-archive-alias-original';archive_path.rename(target);archive_path.symlink_to(target)
 reject('late-generation-symlink-alias',lambda:op.verify_completed(positive,root/op.LOG),'aliased path')
 archive_path.unlink();target.rename(archive_path)
 absent=next(iter(g['absent']))
 created_case('late-absent-input-appearance',absent,b'{}\n','completed absent generation input appeared')
 absent.parent.mkdir(parents=True,exist_ok=True);absent.symlink_to(C/'nonexistent-private-target')
 reject('late-absent-input-broken-alias',lambda:op.verify_completed(positive,root/op.LOG),'aliased path')
 absent.unlink()
 # Capture exact producer paths into a private read-only-Git-metadata fixture.
 producer=C/'private-producer';producer.mkdir()
 for path in g['producer_files']:put(producer/path.relative_to(p['producer']),op.regular(path))
 gitdir=op.git(p['producer'],'rev-parse','--absolute-git-dir').decode().strip()
 put(producer/'.git',('gitdir: '+gitdir+'\n').encode())
 private=dict(positive);private['producer']=producer;private['generation']=dict(g)
 private['generation']['producer_files']={producer/path.relative_to(p['producer']) for path in g['producer_files']}
 extra=producer/'src/kg_microbe_utils/.late-1131.py';put(extra,b'# private added producer source\n')
 reject('late-producer-source-addition',lambda:op.recheck_completion_inputs(private),'completed producer membership changed');extra.rename(C/'late-producer-addition.py')
 removed=next(path for path in sorted(private['generation']['producer_files']) if path.is_relative_to(producer/'src/kg_microbe_utils'));removed.rename(C/'late-producer-removed.py')
 reject('late-producer-source-removal',lambda:op.recheck_completion_inputs(private),'completed producer membership changed')
 (C/'late-producer-removed.py').rename(removed)
 alias_path=producer/'src/kg_microbe_utils/owned_name_policy.py';target=C/'late-producer-alias-original.py';alias_path.rename(target);alias_path.symlink_to(target)
 reject('late-producer-source-alias',lambda:op.recheck_completion_inputs(private),'Producer directory alias')
 alias_path.unlink();target.rename(alias_path)
 # Point only the PRIVATE .git file at an existing different repository's metadata; Git reads only.
 (producer/'.git').write_text('gitdir: '+op.git(W,'rev-parse','--absolute-git-dir').decode().strip()+'\n')
 original_git=op.git;git_calls=[]
 def record_git(*args):
  git_calls.append(tuple(args[1:]));return original_git(*args)
 op.git=record_git
 try:reject('late-producer-revision-drift',lambda:op.recheck_completion_inputs(private),'completed producer revision/context changed')
 finally:op.git=original_git
 assert git_calls==[('rev-parse','HEAD')],git_calls
 # A captured-byte change with identical membership is independently rejected.
 captured=positive['inputs'][root/'docs/data/label_index.csv'];path=root/'docs/data/label_index.csv';path.write_bytes(captured+b'\n')
 reject('late-captured-byte-change',lambda:op.verify_completed(positive,root/op.LOG),'completed captured input changed');path.write_bytes(captured)
 # The second enumeration rejects drift introduced while the native receipt chain is read.
 original_chain=chain.verify_mapping_chain;late=root/'data/ingredients/mapped/.late-during-chain.yaml';calls=[]
 def chain_hook(*args,**kwargs):
  answer=original_chain(*args,**kwargs);put(late,b'preferred_term: late during chain\n');calls.append(True);return answer
 chain.verify_mapping_chain=chain_hook
 try:reject('late-addition-during-chain-verification',lambda:op.verify_completed(positive,root/op.LOG),'completed source membership changed')
 finally:chain.verify_mapping_chain=original_chain
 assert calls==[True];late.rename(C/'late-during-chain-preserved.yaml')
 final=op.verify_completed(positive,root/op.LOG);results.append({'name':'restored-private-completion','outcome':'passed','detail':final})
 assert context.source_inventory(W)==actual_membership
 assert all(op.digest(op.regular(path))==expected for path,expected in actual_inputs.items())
 assert all(op.digest(op.regular(W/name))==expected for name,expected in actual_outputs.items())
 assert not os.path.lexists(W/op.RECEIPT) and not os.path.lexists(W/op.LOG)
 result={'issue':'https://github.com/CultureBotAI/MediaIngredientMech/issues/1131','operator_sha256':op.digest(OP.read_bytes()),
   'test_sha256':op.digest(Path(__file__).read_bytes()),'controls':results,'control_count':len(results),
   'real_inputs_outputs_and_membership_unchanged':True,'positive_application':str(root/op.LOG),
   'positive_application_sha256':op.digest(op.regular(root/op.LOG)),'output_sha256':{str(k):op.digest(v) for k,v in p['outputs'].items()}}
 put(C/'results.json',op.encoded(result));print(json.dumps(result,indent=2))

if __name__=='__main__':main()
