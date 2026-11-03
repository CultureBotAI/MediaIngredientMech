"""External adversarial controls; no maintained files or assertions are edited."""
from pathlib import Path
import collections,copy,hashlib,importlib.util,json,os,tempfile
D=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('step7d_1122_remediation_control',D/'remediate_parent_comments_v2.py');r=importlib.util.module_from_spec(spec);spec.loader.exec_module(r)
m=r.m
passed=[]
def reject(name,fn):
 try:fn()
 except (ValueError,KeyError,FileNotFoundError):passed.append(name)
 else:raise AssertionError('unexpected acceptance: '+name)
config=json.loads(r.CONFIG.read_bytes());finding=json.loads(r.FINDING.read_bytes());before=(r.W/m.SSSOM).read_bytes()
changes=r.corrections(finding,config);after=r.revise(before,changes);r.table_delta(before,after,changes)
assert r.sha(before)==r.CURRENT_SHA and r.sha(after)=='d3030e6385a2659a0dbd2c64ad5581568eecd9c10023f4a58de667e8050f20ef'
assert all(x['native_current_comment_verbatim'] in x['after'] and x['historical_comment_verbatim'] in x['after'] and 'Historical/superseded parent context:' in x['after'] for x in changes)
passed.append('positive: exact four native-current plus explicitly historical comments')
def badfinding(name,edit):
 value=copy.deepcopy(finding);edit(value);reject(name,lambda:r.corrections(value,config))
badfinding('missing target',lambda f:f['targets'].pop())
badfinding('duplicate target',lambda f:f['targets'].__setitem__(1,copy.deepcopy(f['targets'][0])))
badfinding('unreviewed fifth owner',lambda f:f['targets'][0].__setitem__('subject_id','MIM:Other'))
badfinding('wrong CAS row',lambda f:f['targets'][0].__setitem__('object_id','cas:other'))
badfinding('wrong output position',lambda f:f['targets'][0].__setitem__('output_position',533))
badfinding('native comment rewritten',lambda f:f['targets'][0].__setitem__('native_current_comment','approved'))
badfinding('historical comment erased',lambda f:f['targets'][0].__setitem__('comment',f['targets'][0]['native_current_comment']))
badfinding('owner path mismatch',lambda f:f['targets'][0].__setitem__('owner_path','data/ingredients/mapped/Other.yaml'))
badfinding('finding wrong original pin',lambda f:f['evidence'].__setitem__('canonical_sha256','0'*64))
h,fields,rows=m.table(after)
def payload(edited,header=None):return (''.join(header or h)+''.join('\t'.join(row[k]for k in fields)+'\n'for row in edited)).encode()
for field,value in [('source','forged'),('object_id','CHEBI:99999'),('predicate_id','skos:closeMatch'),('mapping_date','2026-11-04'),('confidence','1'),('validation_method','APPROVED'),('other','new alias'),('object_label','fake')]:
 edited=[dict(x)for x,_ in rows];edited[531][field]=value;reject('reject noncomment '+field,lambda edited=edited:r.table_delta(before,payload(edited),changes))
edited=[dict(x)for x,_ in rows];edited[0]['comment']='unrelated';reject('fifth comment cell',lambda:r.table_delta(before,payload(edited),changes))
edited=[dict(x)for x,_ in rows];edited[531]['comment']=changes[0]['native_current_comment_verbatim'];reject('historic provenance lost',lambda:r.table_delta(before,payload(edited),changes))
edited=[dict(x)for x,_ in rows];edited[0],edited[1]=edited[1],edited[0];reject('row reordering',lambda:r.table_delta(before,payload(edited),changes))
reject('row insertion',lambda:r.table_delta(before,payload([x for x,_ in rows]+[dict(rows[0][0])]),changes))
reject('row removal',lambda:r.table_delta(before,payload([x for x,_ in rows][:-1]),changes))
reject('header date change',lambda:r.table_delta(before,after.replace(b'# mapping_date: "2026-11-03"',b'# mapping_date: "2026-11-04"'),changes))
new=r.updated_config(config,changes,after)
oldrows={x['output_position']:x for x in config['rows']};changed=[]
for item in new['rows']:
 original=oldrows[item['output_position']]
 for key in item:
  if key!='output':assert item[key]==original[key]
 for field in fields:
  if item['output'][field]!=original['output'][field]:changed.append((item['output_position'],field))
assert changed==[(x['output_position'],'comment')for x in changes]
assert new['removed']==config['removed']
passed.append('updated projection preserves every candidate, basis, position, science field and removed slot')
proposal=D/'comment-remediation-v2';manifest=json.loads((proposal/'proposal-manifest.json').read_bytes())
inputs={Path(p):Path(p).read_bytes()for p in manifest['input_sha256']};r.execution_contract(manifest,inputs);r.verify_bound(manifest,inputs)
passed.append('positive current bound input and native25 inventory contract')
for key,value in [('sequence',26),('historical_prefix_count',23),('scientific_approval_added',True),('supervisor_binding',{'invented':True}),('issue','https://example.org/other'),('original_canonical_sha256','0'*64),('original_receipt25_sha256','0'*64)]:
 bad=copy.deepcopy(manifest);bad[key]=value;reject('fixed scope '+key,lambda bad=bad:r.execution_contract(bad,inputs))
for path,name in [(r.W/m.SSSOM,'canonical'),(r.W/m.RECEIPT,'receipt25'),(r.CONFIG,'original config'),(r.ORIGINAL,'original projection operator'),(r.W/'UNIFIED_INGREDIENT_MAPPING.tsv','snapshot'),(r.W/'UNIFIED_INGREDIENT_MAPPING.provenance.json','native sidecar'),(r.W/'tests/test_ingredient_bundle.py','test assertion file'),(r.W/'.github/workflows/qc-reviewed-sssom.yaml','paired selector workflow'),(r.W/'scripts/.vendored_canon_ref','pin'),(r.W/'data/ingredients/mapped/Maltotriose_Hydrate.yaml','source owner')]:
 bad=dict(inputs);bad.pop(path);reject('missing protected '+name,lambda bad=bad:r.execution_contract(manifest,bad))
for path,name in [(r.W/m.SSSOM,'canonical'),(r.W/m.RECEIPT,'receipt25'),(r.CONFIG,'original config'),(r.W/'UNIFIED_INGREDIENT_MAPPING.tsv','snapshot'),(r.W/'data/ingredients/mapped/Maltotriose_Hydrate.yaml','owner')]:
 bad=dict(inputs);bad[path]=bad[path]+b' ';reject('changed protected '+name,lambda bad=bad:r.execution_contract(manifest,bad))
bad=dict(inputs);bad[r.W/'tests/test_ingredient_bundle.py']=bad[r.W/'tests/test_ingredient_bundle.py']+b'\n';reject('concurrent test bytes changed',lambda:r.verify_bound(manifest,bad))
bad=copy.deepcopy(manifest);bad['owner_paths'].pop();reject('owner membership omission',lambda:r.verify_bound(bad,inputs))
bad=copy.deepcopy(manifest);bad['producer_paths'].pop();reject('producer inventory omission',lambda:r.verify_bound(bad,inputs))
with tempfile.TemporaryDirectory(prefix='step7d-1122-controls-',dir=D)as td:
 temp=Path(td).resolve();source=temp/'source';source.write_bytes(b'original');alias=temp/'alias';alias.symlink_to(source)
 reject('symlink input alias',lambda:m.regular(alias));hard=temp/'hard';os.link(source,hard);reject('hardlinked input alias',lambda:m.regular(hard))
 log=D/'comments-1122-control-collision.json';require_absent=not os.path.lexists(log);assert require_absent
 # No files are created at a production-log path; scratch basename is rejected by parent confinement.
 outside=temp/'outside.json';reject('nested log destination is confined',lambda:r.execute(proposal,r.sha((proposal/'proposal-manifest.json').read_bytes()),outside))
 # Replay a private clone; corruption cannot affect maintained historical evidence.
 for name in [*m.chain.HISTORICAL_CONTEXT,*m.chain.receipt_paths(r.W)]:
  p=temp/'chain'/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes((r.W/name).read_bytes())
 p=temp/'chain'/m.SSSOM;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(before)
 full=m.chain.verify_mapping_chain(temp/'chain');assert len(full['receipt_paths'])==25
 last=temp/'chain'/m.RECEIPT;old=last.read_bytes();obj=json.loads(old);obj['sequence']=26;last.write_bytes(r.enc(obj));reject('native chain rejects sequence26',lambda:m.chain.verify_mapping_chain(temp/'chain'));last.write_bytes(old)
 obj=json.loads(old);obj['changes'][0]['before']['comment']='forged historical text';last.write_bytes(r.enc(obj));reject('native chain rejects forged batch preimage',lambda:m.chain.verify_mapping_chain(temp/'chain'));last.write_bytes(old)
 first=temp/'chain'/full['receipt_paths'][0];prior=first.read_bytes();obj=json.loads(prior);obj['after_sha256']='0'*64;first.write_bytes(r.enc(obj));reject('native chain rejects historical prefix mutation',lambda:m.chain.verify_mapping_chain(temp/'chain'));first.write_bytes(prior)
 p.write_bytes(after);last.write_bytes((proposal/'receipt25-proposal.json').read_bytes());full=m.chain.verify_mapping_chain(temp/'chain');assert len(full['receipt_paths'])==25 and full['reviewed_sha256']==r.sha(after)
 passed.append('positive corrected native25 chain with all24 historical raw receipts')
result={'controls_passed':len(passed),'controls':passed,'operator_sha256':r.sha(Path(r.__file__).read_bytes()),'proposal_manifest_sha256':r.sha((proposal/'proposal-manifest.json').read_bytes()),'maintained_writes':False,'github_mutations':False,'scientific_approval_added':False,'full_suite_run':False}
print(json.dumps(result,indent=2))
