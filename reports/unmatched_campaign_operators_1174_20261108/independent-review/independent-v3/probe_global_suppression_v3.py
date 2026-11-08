"""Original #1200 counterexample and prior-only variant on final captured producer."""
from pathlib import Path
import importlib.util,json,sys,hashlib
import pytest
D=Path(__file__).resolve().parent;S=D/'publisher-snapshot-v2';sys.path.insert(0,str(S/'src'))
def load(n,p):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);sys.modules[n]=m;s.loader.exec_module(m);return m
c=load('mediaingredientmech.campaign_publication',S/'src/mediaingredientmech/campaign_publication.py');t=load('suppression_fixture_v3',S/'tests/test_campaign_publication.py');policy=load('native_alias_policy_v3',D/'native-checks/owned_name_policy.py');results=[]
for name,token,diagnostic in [('diagnostic-impact','B',True),('prior-only-impact','B',False),('unowned-positive','Unowned old alias',False)]:
 directory=D/'global-suppression-fixtures-v3'/name;directory.mkdir(parents=True)
 with pytest.MonkeyPatch.context() as monkey:
  case=t.case.__wrapped__(directory,monkey);root,plan=case['root'],case['plan'];before=t.sssom([t.row('A'),t.row('Unrelated','CHEBI:9',other=token)])
  t.put(root,c.SOURCE,before);t.put(root,plan['before']['canonical']['path'],before);plan['before']['canonical']['sha256']=c.sha(before)
  old=json.loads((root/c.POLICY).read_bytes());old['artifacts'][c.SOURCE]=c.sha(before);t.put(root,c.POLICY,old);t.put(root,plan['before']['policy']['path'],old);plan['before']['policy']['sha256']=c.sha((root/c.POLICY).read_bytes());t.history(root,before)
  plan['native_context']={p:c.sha((root/p).read_bytes()) for p in t.native.HISTORICAL_CONTEXT};case['owner_proof']['checkpoint']['input_sha256']={**plan['native_context'],c.SOURCE:c.sha(before)};case['owner_proof']['protected_snapshot']['input_sha256'][c.POLICY]=plan['before']['policy']['sha256']
  if diagnostic:
   kept,events=policy.filter_owned_aliases('MIM:Unrelated',[policy.AliasCandidate('B','prior_sssom',('fixture-prior',),('fixture-primary',))],policy.build_owner_index({'MIM:B':{'identifier':'CHEBI:2','preferred_term':'B'},'MIM:Unrelated':{'identifier':'CHEBI:9','preferred_term':'Unrelated'}}));assert not kept and len(events)==1
   sidecar=policy.render_suppressed_aliases(events);t.put(root,plan['generation']['sidecar']['path'],sidecar);plan['generation']['sidecar']['sha256']=c.sha(sidecar)
  t.source_snapshots(root,case['owner_proof']);t.save(case)
  def gen(capture,p,old,inv):
   assert old==before;a,b,m=(capture.ref(p['generation'][key]) for key in ('candidate','sidecar','manifest'));return a,b,json.loads(m)
  monkey.setattr(c,'_generation',gen);out={'case':name,'native_diagnostic_present':diagnostic,'attempts':[]};prepolicy=(root/c.POLICY).read_bytes()
  for apply in [False,True]:
   try:r=c.publish(root,case['path'],case['out'],apply=apply);v={'apply':apply,'status':r['status']}
   except Exception as e:v={'apply':apply,'error':type(e).__name__+': '+str(e)}
   out['attempts'].append(v)
  out.update(canonical_unchanged=(root/c.SOURCE).read_bytes()==before,policy_unchanged=(root/c.POLICY).read_bytes()==prepolicy,outputs=[p.name for p in case['out'].iterdir()]);results.append(out)
  if token=='B':
   assert all('global projected Rule K impact' in x.get('error','') for x in out['attempts']);assert out['canonical_unchanged'] and out['policy_unchanged'] and not out['outputs']
  else:assert [x.get('status') for x in out['attempts']]==['dry_run','complete']
report={'publisher_sha256':hashlib.sha256((S/'src/mediaingredientmech/campaign_publication.py').read_bytes()).hexdigest(),'results':results,'scope':'Native captured whole-canonical RuleK and native alias-policy event; synthetic ownerproof/generation boundaries are explicit mocks; actual projection/policy/receipt/filesystem path. No corpus application.','harness_adaptation':'Final publisher requires exact checkpoint/protected snapshot files; refreshed private fixture snapshots after altering its accepted beforeinputs. Original stale-harness refusal is retained separately.'}
with (D/'global-suppression-probe-v3.json').open('x') as f:json.dump(report,f,indent=2);f.write('\n')
print(json.dumps(report,indent=2))
