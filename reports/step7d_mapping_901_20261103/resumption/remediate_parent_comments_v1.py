"""Issue1122: four comments only; rebuild unpublished receipt25, never append26.

Preparation and dry-run write evidence only outside the maintained checkout.
Application requires --apply and the same immutable proposal and native lock.
The original operator/config/canonical/receipt remain immutable archived inputs.
"""
from __future__ import annotations
import argparse, collections, contextlib, copy, csv, difflib, hashlib, importlib.util, io, json, os
from pathlib import Path
import subprocess, sys, tempfile
D=Path(__file__).resolve().parent
RUN=D.parent
W=RUN/'step7d'
sys.path[:0]=[str(W),str(W/'src')]
ORIGINAL=D/'promote_step7d_mapping.py'
ORIGINAL_SHA='9c26101166b25f88f7e0aed8a43c8040b912c2fdb76489cb1a0ffa0911d198e6'
CONFIG=D/'projection-v1/projection-config.json'
CONFIG_SHA='30e7ecd98d42046057b93c8086e1e5d09c1aa9cd60d12059379248407855a537'
CURRENT_SHA='cd7775a22114ea2d5dd324a532e4cc0d1f335504cd3cfe8c4efe93961cc148e4'
CURRENT_RECEIPT_SHA='00165a2a85fc948237bd2502abb6e24f2fc7d3bd22eb426ae6ffd70fb786e0f1'
ISSUE='https://github.com/CultureBotAI/MediaIngredientMech/issues/1122'
FINDING=D/'independent-review/projection-subreview/finding-001-stale-parent-comments.json'
PLAN=D/'owner-plan.json'
BUNDLE=W/'output/step7d-native-candidate-v1'
PRODUCER=RUN/'step7c-claw'
EXPECTED={
 ('MIM:Beta-Glycerophosphate_Disodium_Salt_Hydrate','cas:154804-51-0'):(532,'CHEBI:17270','CHEBI:132089'),
 ('MIM:D-Glucuronic_Acid_Sodium_Salt_Monohydrate','cas:207300-70-7'):(901,'CHEBI:4178','CHEBI:32144'),
 ('MIM:EDTA_Tetrasodium_Tetrahydrate_Salt','cas:13235-36-4'):(1116,'CHEBI:4735','CHEBI:750784'),
 ('MIM:Maltotriose_Hydrate','cas:312693-63-3'):(1792,'CHEBI:61993','CHEBI:140999'),
}
SNAPSHOT={'UNIFIED_INGREDIENT_MAPPING.tsv':'f6a8eb844e578d79da9538abf99c244fc25b2c928c50c64c0477b1218092a0f1',
 'UNIFIED_INGREDIENT_MAPPING.provenance.json':'075fcc6ef6eca25c1e63d65889df37d4893be2b1b9d3630df90704012dc2c831'}
def sha(raw):return hashlib.sha256(raw).hexdigest()
def require(ok,msg):
 if not ok:raise ValueError('Step7d issue1122: '+msg)
require(sha(ORIGINAL.read_bytes())==ORIGINAL_SHA,'original operator changed')
spec=importlib.util.spec_from_file_location('step7d_original_projection',ORIGINAL)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
from mediaingredientmech.ingredient_bundle_refresh import publish_new_files
_CODE=Path(__file__).read_bytes()
def enc(x):return (json.dumps(x,indent=2,ensure_ascii=False)+'\n').encode()
def read(path,inputs):
 path=m.checked(path);raw=m.regular(path);m.bind(inputs,{path:raw});return raw

def corrections(finding,prior_config):
 require(finding.get('id')=='projection-stale-parent-comments','wrong finding')
 require(finding.get('evidence')=={'projection_config_sha256':CONFIG_SHA,'canonical_sha256':CURRENT_SHA},'finding endpoint differs')
 targets=finding.get('targets');require(isinstance(targets,list)and len(targets)==4,'exact four findings required')
 bykey={};result=[]
 for t in targets:
  key=(t['subject_id'],t['object_id']);require(key in EXPECTED and key not in bykey,'unexpected/duplicate target')
  position,oldparent,newparent=EXPECTED[key]
  prior='Registry/identity row preserving '+key[1]+' alongside parent '+oldparent+'.'
  current='Registry/identity row preserving '+key[1]+' alongside parent '+newparent+'.'
  require(t['output_position']==position and t['native_current_comment']==current and t['comment']==prior+' '+current,'finding comment/position differs')
  items=[x for x in prior_config['rows']if (x['output']['subject_id'],x['output']['object_id'])==key]
  require(len(items)==1,'target missing/ambiguous in original config');item=items[0]
  require(item['output_position']==position and item['output']['comment']==t['comment'] and item['candidate']['comment']==current,'native/config comment disagrees')
  require(t['owner_path']=='data/ingredients/mapped/'+key[0][4:]+'.yaml','wrong target owner')
  after=current+' Historical/superseded parent context: '+prior
  result.append({'subject_id':key[0],'object_id':key[1],'output_position':position,'column':'comment',
   'before':t['comment'],'after':after,'historical_comment_verbatim':prior,'native_current_comment_verbatim':current,'owner_path':t['owner_path'],'issue':ISSUE})
  bykey[key]=t
 require(set(bykey)==set(EXPECTED),'missing target')
 return sorted(result,key=lambda x:x['output_position'])

def table_delta(before,after,changes):
 h,f,a=m.table(before);j,g,b=m.table(after)
 require(h==j and f==g and len(a)==len(b),'header/fields/count/order changed')
 expected={(x['output_position'],x['subject_id'],x['object_id'],'comment'):(x['before'],x['after'])for x in changes}
 require(len(expected)==4,'four distinct cells required');actual={}
 for i,((old,oldraw),(new,newraw))in enumerate(zip(a,b,strict=True),1):
  require((old['subject_id'],old['object_id'])==(new['subject_id'],new['object_id']),'row identity/order changed')
  for field in f:
   if old[field]!=new[field]:actual[(i,old['subject_id'],old['object_id'],field)]=(old[field],new[field])
  if old==new:require(oldraw==newraw,'unaffected raw row bytes changed')
 require(actual==expected,'delta is not exactly the four reviewed comment cells')
 return actual

def revise(before,changes):
 h,f,rows=m.table(before);bypos={x['output_position']:x for x in changes};body=[]
 require(len(bypos)==4,'duplicate/missing comment position')
 for i,(row,raw)in enumerate(rows,1):
  if i in bypos:
   x=bypos[i];require((row['subject_id'],row['object_id'],row['comment'])==(x['subject_id'],x['object_id'],x['before']),'comment preimage differs')
   updated=dict(row,comment=x['after']);raw='\t'.join(updated[k]for k in f)+'\n'
  body.append(raw)
 after=(''.join(h)+''.join(body)).encode();table_delta(before,after,changes);return after

def updated_config(old,changes,after):
 new=copy.deepcopy(old);new['schema_version']=3
 bypos={x['output_position']:x for x in changes}
 for item in new['rows']:
  if item['output_position']in bypos:
   change=bypos[item['output_position']];require(item['output']['comment']==change['before'],'configuration preimage differs')
   item['output']['comment']=change['after']
 new['canonical_after_sha256']=sha(after)
 new['comment_remediation']={'issue':ISSUE,'original_projection_sha256':CONFIG_SHA,'original_operator_sha256':ORIGINAL_SHA,
  'original_canonical_sha256':CURRENT_SHA,'original_receipt25_sha256':CURRENT_RECEIPT_SHA,
  'contract':'Replay unchanged original native projection, then only the four explicit comment substitutions; full old/current text retained; sequence25 remains one unpublished batch.',
  'cells':changes,'scientific_approval_added':False}
 return new

def rebuild_receipt(base,old_receipt,after,inputs):
 maker_raw=read(W/m.MAKER,inputs);require(maker_raw==base[str(m.MAKER)],'native maker differs from base')
 prefix=sorted(n for n in base if n.startswith(m.chain.RECEIPTS_DIR+'/')and n.endswith('.json'))
 require(len(prefix)==24,'historical prefix not24')
 for name in (*prefix,*m.chain.HISTORICAL_CONTEXT):require(read(W/name,inputs)==base[name],'historical prefix/context changed: '+name)
 spec=importlib.util.spec_from_file_location('step7d_1122_native_maker',W/m.MAKER);maker=importlib.util.module_from_spec(spec)
 exec(compile(maker_raw,str(W/m.MAKER),'exec'),maker.__dict__)
 receipt=json.loads(old_receipt);records=receipt['records'];require(len(records)==38,'owner count differs')
 with tempfile.TemporaryDirectory(prefix='step7d-1122-receipt-',dir=D)as td:
  root=Path(td).resolve()
  for name in (*prefix,*m.chain.HISTORICAL_CONTEXT):p=root/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(base[name])
  source=root/m.SSSOM;source.parent.mkdir(parents=True,exist_ok=True);source.write_bytes(base[str(m.SSSOM)])
  proof=m.chain.verify_mapping_chain(root);require(len(proof['receipt_paths'])==24 and proof['reviewed_sha256']==m.BEFORE_SHA,'native historical prefix mismatch')
  before=root/'before.tsv';before.write_bytes(base[str(m.SSSOM)])
  log=root/'original-source-records.json';log.write_bytes(enc({'records':records}))
  for item in records:
   raw=read(W/item['source_record'],inputs);require(sha(raw)==item['after_yaml_sha256'],'source owner endpoint changed')
   p=root/item['source_record'];p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(raw)
  maker.ROOT,maker.SOURCE,maker.HERE=root,source,root/m.chain.RECEIPTS_DIR
  def execute(payload):
   source.write_bytes(payload);argv=sys.argv
   sys.argv=[str(W/m.MAKER),'--batch',m.BATCH,'--sequence','25','--issue',receipt['issue'],'--scope',receipt['scope'],'--before-sssom',str(before),'--apply-log',str(log)]
   try:
    with contextlib.redirect_stdout(io.StringIO()):maker.main()
   finally:sys.argv=argv
   raw=(root/m.RECEIPT).read_bytes();full=m.chain.verify_mapping_chain(root)
   require(len(full['receipt_paths'])==25 and full['receipt_paths'][-1]==str(m.RECEIPT) and full['reviewed_sha256']==sha(payload),'native25 chain differs')
   return raw
  require(execute(inputs[W/m.SSSOM])==old_receipt,'native maker cannot reproduce original batch25 verbatim')
  new=execute(after);a,b=json.loads(old_receipt),json.loads(new)
  allowed={'after_sha256','changes'};require({k:v for k,v in a.items()if k not in allowed}=={k:v for k,v in b.items()if k not in allowed},'batch25 non-endpoint metadata changed')
  require(b['sequence']==25 and b['batch']==m.BATCH and b['approval'].startswith('NONE:'),'batch identity/approval differs')
  return new,proof['receipt_paths']

def collect():
 inputs={};read(Path(__file__),inputs);require(inputs[Path(__file__)]==_CODE,'executed operator changed')
 oldconfig=read(CONFIG,inputs);require(sha(oldconfig)==CONFIG_SHA,'old projection changed')
 require(sha(read(ORIGINAL,inputs))==ORIGINAL_SHA,'old operator changed')
 finding=json.loads(read(FINDING,inputs));plan=json.loads(read(PLAN,inputs));config=json.loads(oldconfig)
 require(sha(inputs[PLAN])==config['owner_plan_sha256'],'owner plan changed')
 old=read(W/m.SSSOM,inputs);require(sha(old)==CURRENT_SHA,'canonical changed')
 oldreceipt=read(W/m.RECEIPT,inputs);require(sha(oldreceipt)==CURRENT_RECEIPT_SHA,'current batch25 changed')
 proof=m.chain.verify_mapping_chain(W);require(len(proof['receipt_paths'])==25 and proof['receipt_paths'][-1]==str(m.RECEIPT),'current receipt inventory differs')
 base=m.baseline(W);candidate=read(BUNDLE/'candidate.sssom.tsv',inputs);require(sha(candidate)==config['candidate_sha256'],'native candidate changed')
 deferred=m.deferred_pairs(base['mappings/other_cross_record_baseline.tsv'])
 require(m.projection(base[str(m.SSSOM)],candidate,config,plan,deferred)==old,'original projection replay differs')
 changes=corrections(finding,config);after=revise(old,changes)
 for path in m.policy.ingredient_paths(W):
  name=str(path.relative_to(W));raw=read(path,inputs);expected=plan['owners'][name]['after_sha256']if name in plan['owners']else plan['all_owner_sha256'][name]
  require(sha(raw)==expected,'owner inventory/hash changed: '+name)
 require({str(p.relative_to(W))for p in m.policy.ingredient_paths(W)}==set(plan['all_owner_sha256']),'owner membership changed')
 for name,expected in SNAPSHOT.items():require(sha(read(W/name,inputs))==expected,'reviewed snapshot changed')
 for name,stages in plan['auxiliary'].items():require(sha(read(W/name,inputs))==stages[-1]['after_sha256'],'auxiliary endpoint changed')
 # Freeze every tracked test, workflow and maintained source/runtime contract.
 names=m.native.git(W,'ls-files','-z').decode().split('\0')
 for name in names:
  if name and (name.startswith(('src/','scripts/','tests/','.github/workflows/'))or name in ['justfile','pyproject.toml','uv.lock','.python-version','MAPPING_SEMANTICS.md']):read(W/name,inputs)
 for path,raw in m._EXECUTED.items():require(read(path,inputs)==raw,'original executed helper changed')
 original_log=json.loads(read(D/'mapping-apply-v1.json',inputs))
 require(original_log['state']=='complete'and original_log['applied']is True and original_log['receipt_sha256']==CURRENT_RECEIPT_SHA and original_log['records']==json.loads(oldreceipt)['records'],'original application receipt differs')
 journal=read(Path(original_log['transaction']['journal']),inputs);require(sha(journal)==original_log['journal_sha256'],'original journal changed')
 beforebackup=read(D/'mapping-apply-v1.before-canonical.tsv',inputs);require(beforebackup==base[str(m.SSSOM)],'original canonical backup changed')
 # Verify and replay captured native inputs; original prior stamps are a scratch copy.
 manifest_raw=read(BUNDLE/'candidate.sssom.tsv.manifest.json',inputs);require(sha(manifest_raw)==config['generation_manifest_sha256'],'native manifest changed')
 manifest=json.loads(manifest_raw);require(manifest['source_revisions']['claw']==m.PRODUCER,'native producer revision differs')
 require(m.native.git(PRODUCER,'rev-parse','HEAD').decode().strip()==m.PRODUCER and not m.native.git(PRODUCER,'status','--porcelain','--untracked-files=all'),'producer dirty or moved')
 absent=[]
 for item in manifest['source_inputs']:
  path=m.checked(item['path'])
  if item['sha256']is None:require(not os.path.lexists(path),'absent native input appeared');absent.append(path)
  elif path==W/m.SSSOM:require(sha(base[str(m.SSSOM)])==item['sha256'],'native historical stamps differ')
  else:require(sha(read(path,inputs))==item['sha256'],'native input changed: '+str(path))
 generation=json.loads(read(BUNDLE/'generation-receipt.json',inputs))
 for name,digest in generation['label_maps'].items():require(sha(read(BUNDLE/name,inputs))==digest,'native label capture changed')
 require(set(BUNDLE.glob('label-input-*.json'))=={BUNDLE/n for n in generation['label_maps']},'label inventory changed')
 require(sha(read(BUNDLE/'suppressed_aliases.tsv',inputs))==generation['sidecar_sha256'],'native sidecar changed')
 with tempfile.TemporaryDirectory(prefix='step7d-1122-native-replay-',dir=D)as td:
  prior=Path(td)/'prior.tsv';prior.write_bytes(base[str(m.SSSOM)])
  run=subprocess.run([sys.executable,'-I','-c',m.native._REPLAY,str(PRODUCER),str(BUNDLE),str(prior)],capture_output=True,text=True)
  require(run.returncode==0,'native replay failed: '+run.stderr[-3000:]);replay=json.loads(run.stdout)
 newreceipt,prefix=rebuild_receipt(base,oldreceipt,after,inputs)
 newconfig=updated_config(config,changes,after)
 scope={'issue':ISSUE,'approval':'NONE: four explanatory comment cells only; no scientific/role/release approval',
  'scientific_approval_added':False,'supervisor_binding':None,'base_revision':m.BASE,'observed_head':m.native.git(W,'rev-parse','HEAD').decode().strip(),
  'original_canonical_sha256':CURRENT_SHA,'canonical_after_sha256':sha(after),'original_receipt25_sha256':CURRENT_RECEIPT_SHA,
  'receipt25_after_sha256':sha(newreceipt),'sequence':25,'historical_prefix_count':len(prefix),'historical_prefix_sha256':{n:sha(inputs[W/n])for n in prefix},
  'canonical_changed_cells':4,'canonical_changed_columns':['comment'],'canonical_row_count':len(m.table(after)[2]),
  'native_offline_replay':replay,'native_original_receipt25_reproduced':True,'native_corrected25_chain_replayed':True,
  'receipt25_unchanged_metadata':True,'owner_records_unchanged':True,'snapshot_unchanged':SNAPSHOT,'input_sha256':{str(p):sha(b)for p,b in inputs.items()},
  'absent_inputs':[str(p)for p in absent],'owner_paths':sorted(plan['all_owner_sha256']),
  'label_paths':sorted(str(BUNDLE/n)for n in generation['label_maps']),'producer_paths':sorted(map(str,m.native.producer_paths(PRODUCER)))}
 return inputs,scope,changes,after,newreceipt,enc(newconfig)

def verify_bound(scope,inputs):
 require(all(m.regular(p)==b for p,b in inputs.items()),'frozen input changed')
 require(all(not os.path.lexists(p)for p in scope['absent_inputs']),'absent input appeared')
 require(sorted(str(p.relative_to(W))for p in m.policy.ingredient_paths(W))==scope['owner_paths'],'owner inventory changed')
 require(sorted(map(str,m.native.producer_paths(PRODUCER)))==scope['producer_paths'],'producer inventory changed')
 require(sorted(map(str,BUNDLE.glob('label-input-*.json')))==scope['label_paths'],'label inventory changed')
 require(m.native.git(PRODUCER,'rev-parse','HEAD').decode().strip()==m.PRODUCER and not m.native.git(PRODUCER,'status','--porcelain','--untracked-files=all'),'producer context changed')
 require(m.chain.receipt_paths(W)==list(scope['historical_prefix_sha256'])+[str(m.RECEIPT)],'receipt inventory changed')

def prepare(out):
 out=m.checked(out);require(out.parent==D and not os.path.lexists(out),'new direct external directory required')
 inputs,scope,changes,after,receipt,config=collect();verify_bound(scope,inputs)
 artifacts={'canonical-proposal.sssom.tsv':after,'receipt25-proposal.json':receipt,'projection-config-v3.json':config,
  'original-canonical.tsv':inputs[W/m.SSSOM],'original-receipt25.json':inputs[W/m.RECEIPT],
  'original-projection-config.json':inputs[CONFIG],'original-projection-operator.py':inputs[ORIGINAL],
  'native-maker.py':inputs[W/m.MAKER],'finding.json':inputs[FINDING],'comment-corrections.json':enc(changes)}
 scope['artifact_sha256']={n:sha(b)for n,b in artifacts.items()};scope['operator_sha256']=sha(_CODE)
 artifacts['proposal-manifest.json']=enc(scope)
 out.mkdir(mode=0o700);publish_new_files([(out/n,b)for n,b in artifacts.items()],lambda:verify_bound(scope,inputs))
 return scope

def execute(proposal,manifest_sha,log,*,apply=False):
 proposal=m.checked(proposal);log=m.checked(log)
 require(proposal.parent==D and log.parent==D and log.suffix=='.json','external proposal/log required')
 require(not os.path.lexists(log),'log already exists')
 raw=m.regular(proposal/'proposal-manifest.json');require(sha(raw)==manifest_sha,'proposal manifest pin differs');scope=json.loads(raw)
 require(scope['operator_sha256']==sha(_CODE),'operator differs from frozen proposal')
 inputs={Path(p):m.regular(Path(p))for p in scope['input_sha256']}
 require(all(sha(b)==scope['input_sha256'][str(p)]for p,b in inputs.items()),'proposal input bytes changed')
 m.bind(inputs,{proposal/'proposal-manifest.json':raw})
 for name,digest in scope['artifact_sha256'].items():
  require(Path(name).name==name,'unsafe proposal artifact');b=m.regular(proposal/name);require(sha(b)==digest,'proposal artifact changed');m.bind(inputs,{proposal/name:b})
 old=inputs[W/m.SSSOM];after=inputs[proposal/'canonical-proposal.sssom.tsv'];changes=json.loads(inputs[proposal/'comment-corrections.json'])
 require(changes==corrections(json.loads(inputs[FINDING]),json.loads(inputs[CONFIG])),'correction declaration changed')
 table_delta(old,after,changes)
 require(inputs[proposal/'projection-config-v3.json']==enc(updated_config(json.loads(inputs[CONFIG]),changes,after)),'updated config replay differs')
 base=m.baseline(W);receipt,prefix=rebuild_receipt(base,inputs[W/m.RECEIPT],after,inputs)
 require(receipt==inputs[proposal/'receipt25-proposal.json'],'receipt25 proposal replay differs')
 outputs={m.SSSOM:after,m.RECEIPT:receipt};result={k:v for k,v in scope.items()if k not in {'owner_paths','producer_paths','label_paths'}}
 result.update(phase='issue1122-four-comments-single-unpublished-batch25',proposal=str(proposal),proposal_manifest_sha256=manifest_sha,
  output_sha256={str(p):sha(b)for p,b in outputs.items()})
 backups={log.with_name(log.stem+'.before-canonical.tsv'):old,log.with_name(log.stem+'.before-receipt25.json'):inputs[W/m.RECEIPT]}
 validate=lambda:verify_bound(scope,inputs)
 validate();answer=m.publication.publish(W,outputs,inputs,log,backups,result,apply=apply,validate_scope=validate)
 if apply:
  require(all(m.regular(W/p)==b for p,b in outputs.items()),'applied output mismatch')
  require(all(m.regular(p)==b for p,b in inputs.items()if p not in {W/m.SSSOM,W/m.RECEIPT}),'nonoutput input changed during publication')
  proof=m.chain.verify_mapping_chain(W);require(len(proof['receipt_paths'])==25 and proof['reviewed_sha256']==sha(after),'published chain differs')
  saved=json.loads(m.regular(log));m.publication.completed_journal(W,log,saved,previous={m.SSSOM:old,m.RECEIPT:inputs[W/m.RECEIPT]})
 return {k:v for k,v in answer.items()if k not in {'input_sha256','artifact_sha256','historical_prefix_sha256'}}

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--proposal',type=Path,required=True);ap.add_argument('--manifest-sha256');ap.add_argument('--log',type=Path,required=True)
 modes=ap.add_mutually_exclusive_group();modes.add_argument('--prepare',action='store_true');modes.add_argument('--apply',action='store_true');modes.add_argument('--dry-run',action='store_true');a=ap.parse_args()
 from plugins.lock_manager import LockManager
 from plugins.repository_settings import RepositorySettings
 target=RepositorySettings.from_environment().get_target('mediaingredientmech');require(target.path.resolve()==W,'configured root differs');target.open()
 with LockManager().lock('mediaingredientmech','Step7d issue1122 four comments and existing receipt25'):
  if a.prepare:prepare(a.proposal);pin=sha(m.regular(a.proposal/'proposal-manifest.json'))
  else:require(a.manifest_sha256,'manifest sha required');pin=a.manifest_sha256
  result=execute(a.proposal,pin,a.log,apply=a.apply)
 print(json.dumps({'proposal_manifest_sha256':pin,**result},indent=2))
if __name__=='__main__':main()
