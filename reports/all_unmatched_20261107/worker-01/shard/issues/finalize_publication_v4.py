"""Bind reviewed publication bodies to one actual pushed commit; no GitHub writes."""
from pathlib import Path
import json,re,hashlib,datetime,subprocess,sys
I=Path('reports/all_unmatched_20261107/worker-01/shard/issues');A=I/'publication-v3';O=I/'publication-v4';commit=sys.argv[1];assert re.fullmatch('[0-9a-f]{40}',commit),commit
assert subprocess.check_output(['git','rev-parse',commit],text=True).strip()==commit
old='https://github.com/CultureBotAI/MediaIngredientMech/blob/review/all-unmatched-w01-source-review-20261107/'
new='https://github.com/CultureBotAI/MediaIngredientMech/blob/'+commit+'/'
rp=I.parent/'independent_review/publication-artifact-rereview-v2.json';review=json.loads(rp.read_text());plan=json.loads((A/'issue-plan.json').read_text());assert hashlib.sha256((A/'issue-plan.json').read_bytes()).hexdigest()==review['plan_sha256']
for b in review['bodies']:assert hashlib.sha256(Path(b['path']).read_bytes()).hexdigest()==b['sha256']
O.mkdir();links={}
for p in A.glob('*.md'):
 s=p.read_text()
 if '1159' in p.name:
  s=s.replace('independent publication rereview is pending.','the [independent publication rereview]('+old+str(rp)+') confirms both corrections across all ten bodies.')
 s=s.replace(old,new)
 for rel in re.findall(re.escape(new)+r'([^\s)]+)',s):
  blob=subprocess.check_output(['git','show',commit+':'+rel]);local=Path(rel);assert local.is_file();links[rel]={'committed_sha256':hashlib.sha256(blob).hexdigest(),'current_file_sha256':hashlib.sha256(local.read_bytes()).hexdigest(),'matches_current_file':blob==local.read_bytes()}
 (O/p.name).write_text(s)
plan['created_at']=datetime.datetime.now(datetime.UTC).isoformat();plan['state']='reviewed publication bodies with verified immutable evidence links; root owns authorized GitHub posting and readback';plan['supersedes']=str(A/'issue-plan.json');plan['evidence_commit']=commit;plan['publication_review']={'path':str(rp),'sha256':hashlib.sha256(rp.read_bytes()).hexdigest(),'scope':review['scope'],'verdict':review['verdict']}
for a in plan['actions']:
 a['body_file']=str(O/Path(a['body_file']).name)
 if a.get('issue')==1159:a['dedup']='Existing worker01 artifact tracker; continuation findings IR-SHARD-ARTIFACT-1 through12 and publication findings1/2 remain separate from the three canary findings. Cross-source duplicate scope is also tracked in1166.'
plan['body_sha256']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in O.glob('*.md')};plan['unfinalized_items']=['Root performs authorized GitHub posting and verifies exact published body readback.','Final branch/PR-head attestation and coordinator verification remain separate.','No GitHub mutation performed by this agent.']
(O/'issue-plan.json').write_text(json.dumps(plan,indent=2)+'\n')
receipt={'at':datetime.datetime.now(datetime.UTC).isoformat(),'evidence_commit':commit,'source_review_plan_sha256':review['plan_sha256'],'publication_review_sha256':hashlib.sha256(rp.read_bytes()).hexdigest(),'changes_from_reviewed_v3':['Replace branch artifact URLs with exact reviewed pushed commit','Replace1159 publication-rereview pending sentence with actual independent receipt','Correct obsolete internal dedup count wording'],'all_link_targets_exist_at_commit':True,'links':links,'github_mutations_performed':False}
(O/'immutable-link-verification.json').write_text(json.dumps(receipt,indent=2)+'\n');print('Prepared',len(plan['actions']),'publication bodies;',len(links),'committed artifact targets verified')
