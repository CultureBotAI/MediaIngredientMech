from pathlib import Path
import datetime,hashlib,json,subprocess
R=Path.cwd();A=R/'reports/all_unmatched_20261107/worker-10';S=A/'successor-v2';P=R/'.temp/all-unmatched-worker-10/successor-v2/skeptic';O=S/'reviews/skeptic';H=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();J=lambda p:json.loads(Path(p).read_text())
f=J(S/'HANDOFF.json');d=J(S/'HANDOFF-draft-v1.json');checks=[];bound=[]
def ck(n,b):checks.append({'check':n,'pass':bool(b)})
def walk(x):
 if isinstance(x,dict):
  if 'path' in x and 'sha256' in x:
   p=Path(x['path']);p=p if p.is_absolute() else R/p;ck('exact binding '+str(p),H(p)==x['sha256']);bound.append({'path':str(p),'sha256':H(p)})
  for y in x.values():walk(y)
 elif isinstance(x,list):
  for y in x:walk(y)
walk(f)
ck('exact final handoff json',H(S/'HANDOFF.json')=='d3c4ec70240424bc24b0dcb58c376f4409248254e95dc73e243cfc974104e230')
ck('exact final handoff markdown',H(S/'HANDOFF.md')=='24d1fb79872d8c050540df241731f895d86b77c584dff23b07d2dda86f739f87')
allowed={'at','status','draft_reviewed','independent_final_assembly','final_preservation','final_handoff_review_path','manifest_path','post_publication_receipt_path','publication_note','validation'}
changed={k for k in set(d)|set(f) if d.get(k)!=f.get(k)};ck('only allowed final handoff metadata fields changed',changed<=allowed)
ck('all old validation pointers unchanged',all(f['validation'][k]==x for k,x in d['validation'].items() if k!='full_native_check_after_metadata_successor'))
cmd=J(S/'native-check-v2-command.json');res=J(S/'native-check-v2.stdout');ck('actual full native check1023 declared scopes',cmd['exit_code']==0 and res['valid_reviews']==1023 and res['coverage']=='declared_scopes_only')
ck('original authorization attribution retained',J(A/'issue-publication-receipts.json')['new_user_approval'] is False and 'No fresh user approval was supplied.' in (A/'HANDOFF.md').read_text() and 'no fresh user approval is invented' in (S/'HANDOFF.md').read_text())
ck('immutable core and native same as assembly review',f['selected_core']==d['selected_core'] and f['validation']['native_selected_pair']==d['validation']['native_selected_pair'])
ck('no future publication approval claim','not a claim of coordinator acceptance' in f['publication_note'] and f['remaining_conditions']==d['remaining_conditions'])
ck('precommit HEAD unchanged',subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()=='468766d941e35a74eb2de3c95096660987277d9b')
assert all(x['pass'] for x in checks),checks
now=datetime.datetime.now(datetime.timezone.utc).isoformat();out=O/'final-handoff-review-v1.json';assert not out.exists()
receipt={'schema_version':1,'reviewer':'/root/preparation_skeptic (AI; author-independent scientific and assembly reviewer)','at':now,'completion':'completed','verdict':'PASS_final_prepublication_handoff_binding','handoff_json_sha256':H(S/'HANDOFF.json'),'handoff_md_sha256':H(S/'HANDOFF.md'),'assembly_review_sha256':H(O/'assembly-review-v1.json'),'scientific_review_sha256':H(O/'scientific-review-v1.json'),'selected_native_yaml_sha256':f['validation']['native_selected_pair']['files'][0]['sha256'],'core_hashes':{k:f['selected_core'][k]['sha256'] for k in ['decisions.json','proposals.json','evidence.json']},'checks':checks,'failures':[],'bound_files':bound,'metadata_change_fields':sorted(changed),'observations':['Final handoff adds the exact completed assembly review and actual native repository check1023, with final preservation receipt and later-seal/publication receipt paths. Selected core, payloads, scientific limits, source scope and native-v2 are unchanged.','Historical original rejection and coordinator verification of pre-existing authorization remain exact; no fresh user approval is claimed. Current task created no issue/comment mutation.','All original scientific and integration holds remain. Nested548 stock dependency is unresolved, while the bounded source parent is complete.','Manifest and publication receipt are future outputs at this checkpoint; their path declarations are not proof of a seal, push or remote state. Final published-head/union/owner/role/export acceptance remains coordinator responsibility.'],'freeze':'This is the last public skeptical-review write for successor-v2. Any later staged-manifest check will be private-only and will not silently update this report.','reproduction_script':{'path':str(Path(__file__).relative_to(R)),'sha256':H(Path(__file__))}}
out.write_text(json.dumps(receipt,indent=2)+'\n')
support=O/'support';copies=[]
for src in sorted(P.iterdir()):
 if not src.is_file():continue
 dst=support/src.name
 if dst.exists():assert dst.read_bytes()==src.read_bytes()
 else:dst.write_bytes(src.read_bytes())
 copies.append({'original_path':str(src.relative_to(R)),'public_path':str(dst.relative_to(R)),'sha256':H(src)})
copy=O/'support-copy-receipt-v3.json';assert not copy.exists();copy.write_text(json.dumps({'at':now,'copies':copies,'unchanged_exact_original_bindings':True,'public_support_frozen_after_this_copy':True},indent=2)+'\n')
print(json.dumps({'review_sha256':H(out),'copy_receipt_sha256':H(copy),'checks':len(checks),'public_support_files':len(copies),'public_writes_frozen':True}))
