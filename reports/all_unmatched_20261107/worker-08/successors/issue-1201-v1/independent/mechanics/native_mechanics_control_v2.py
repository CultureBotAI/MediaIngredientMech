from pathlib import Path
import json,hashlib,datetime,yaml,copy
P=Path('.temp/all-unmatched-worker-08/issue-1201-v1').resolve()
F=P/'vitamins_mixtures/native-author-controls-v2';F.mkdir(exist_ok=False)
R=Path('reports/all_unmatched_20261107/worker-08/successors/issue-1201-v1/independent/mechanics')
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,x):p.write_text(json.dumps(x,sort_keys=True)+'\n')
def run(name,mutation=None):
 root=F/name;out=root/'reports/all_unmatched_20261107/worker-08/successors/issue-1201-v1';v=out/'validation';v.mkdir(parents=True);priv=root/'.temp/all-unmatched-worker-08/issue-1201-v1';priv.mkdir(parents=True);art=out.parents[1]
 payload=out/'fixture.yaml';payload.write_text('identifier: fixture\npreferred_term: Fixture\n')
 peer=out/'peer.json';write(peer,{'status':'accepted','scope':'synthetic mechanism only'})
 prop={'proposal_id':'fixture-proposal','case_ids':['fixture-case'],'description':'Synthetic mechanism fixture','evidence_ids':[],'after_capture':{'path':str(payload.relative_to(art)),'sha256':sha(payload)}}
 write(out/'proposals.json',{'proposals':[prop]});write(out/'decisions.json',{'decisions':[{'case_id':'fixture-case','reasoning':'Synthetic fixture'}]})
 for n in ['evidence.json','reassessments.json','assembly-provenance.json']:write(out/n,{})
 config={'parent_commit':'7efd3f8b98f9e822431dcb510c2c242a2569cfc7','groups':[{'name':'fixture','review':{'path':str(peer.relative_to(art)),'sha256':sha(peer)},'reviewer':'independent-fixture','primary_author':'primary-fixture','reviewed_case_ids':['fixture-case']}]};write(priv/'final-selection.json',config)
 ih={str((out/n).relative_to(root)):sha(out/n) for n in ['decisions.json','evidence.json','proposals.json','reassessments.json','assembly-provenance.json']}
 proof={'status':'PASS','final_input_hashes':ih,'configuration_sha256':sha(priv/'final-selection.json')};write(v/'peer-receipt-verification.json',proof)
 structural={'structural_accounting':'PASS','phase':'shard','accounted_case_count':188,'assigned_shard_case_count':188,'out_of_scope_shard_case_ids':[],'independent_review_status_counts':{'complete':188},'input_hashes':{str(out/n):sha(out/n) for n in ['decisions.json','evidence.json','proposals.json']}};write(out/'structural-audit.json',structural)
 combined={'strict_exit_code':0,'baseline_partonomy_violations':[],'overlay_partonomy_violations':[],'maintained_changed':[],'maintained_added':[],'maintained_removed':[],'published_mismatches':[],'maintained_surfaces_unchanged':True,'proposal_count':1,'guarded_replay_count':1,'parent_head':config['parent_commit'],'input_hashes':ih,'proposals':[{'proposal_id':'fixture-proposal','after_sha256':sha(payload)}],'baseline_record_count':1,'overlay_record_count':2,'maintained_files_checked':1};write(v/'combined-validation.json',combined)
 ins={'targets':[{'target_id':'fixture-proposal'}],'source':{'inputs':[{'path':str((v/n).relative_to(root)),'sha256':sha(v/n)} for n in ['combined-validation.json','peer-receipt-verification.json']]}};write(priv/'native-inspection.json',ins)
 if mutation:mutation(root,out,priv,v)
 script=(P/'save_native_review.py').read_text().replace('ROOT=Path(__file__).resolve().parents[3]','ROOT=Path('+repr(str(root))+')')
 error=None
 try:exec(compile(script,str(P/'save_native_review.py'),'exec'),{'__file__':str(P/'save_native_review.py')})
 except Exception as e:error=type(e).__name__+': '+str(e)
 exists=(priv/'native-review.yaml').exists()
 return {'control':name,'generated_passing_review':exists,'rejection':error,'inputs':{str(p.relative_to(root)):sha(p) for p in root.rglob('*.json')}}
def field(rel,key,value):
 def change(root,out,priv,v):
  p=out/rel;d=json.loads(p.read_text());d[key]=value;write(p,d)
 return change
controls=[run('positive')]
assert controls[0]['generated_passing_review'] and controls[0]['rejection'] is None
for name,rel,key,value in [
 ('structural-fail','structural-audit.json','structural_accounting','FAIL'),
 ('partial-shard','structural-audit.json','accounted_case_count',187),
 ('pending-peer','structural-audit.json','independent_review_status_counts',{'complete':187,'pending':1}),
 ('strict-fail','validation/combined-validation.json','strict_exit_code',1),
 ('partonomy-fail','validation/combined-validation.json','overlay_partonomy_violations',['fixture']),
 ('maintained-change','validation/combined-validation.json','maintained_changed',['fixture']),
 ('maintained-false','validation/combined-validation.json','maintained_surfaces_unchanged',False),
 ('published-change','validation/combined-validation.json','published_mismatches',['fixture']),
 ('guarded-count','validation/combined-validation.json','guarded_replay_count',0),
 ('stale-combined','validation/combined-validation.json','input_hashes',{}),
 ('stale-proof','validation/peer-receipt-verification.json','final_input_hashes',{}),
 ('stale-config','validation/peer-receipt-verification.json','configuration_sha256','bad')]:
  c=run(name,field(rel,key,value));assert not c['generated_passing_review'] and c['rejection'],c;controls.append(c)
def stale_payload(root,out,priv,v):(out/'fixture.yaml').write_text('changed\n')
controls.append(run('stale-payload',stale_payload));assert not controls[-1]['generated_passing_review']
def stale_inspection(root,out,priv,v):
 p=priv/'native-inspection.json';d=json.loads(p.read_text());d['source']['inputs'][0]['sha256']='bad';write(p,d)
controls.append(run('stale-native-inspection',stale_inspection));assert not controls[-1]['generated_passing_review']
report={'reviewer':'/root/vitamins','scope':'Independent mechanical recheck of native helpers only, using synthetic private fixtures; no actual native bundle was generated and no scientific approval is established.','reviewed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'helper_hashes':{n:sha(P/n) for n in ['save_native_review.py','prepare_native_inspection.py','validate_final_bundle.py','manifest.py']},'finding_id':'MECH-NATIVE-001','status':'resolved','controls':controls,'positive_controls':1,'rejected_negative_controls':len(controls)-1,'script_sha256':sha(Path(__file__)),'qualifications':['The positive fixture is a mechanical stub, not 188 scientifically reviewed cases; it only exercises authoring gates. Actual receipt contents must still be independently inspected by root.','prepare_native_inspection now includes peer-receipt-verification.json as exact context input. Existing-owner preimages and new-owner source-only targets remain distinct.','The manifest helper remains limited to the new successor subtree and named new native review; predecessor bytes are not rewritten.','Native authoring trusts the target list generated by prepare_native_inspection; independent final scope inspection must confirm exact selected proposal population.']}
o=R/'native-helpers-review-vitamins-v2.json';assert not o.exists();o.write_text(json.dumps(report,indent=2)+'\n');print(o,sha(o))
