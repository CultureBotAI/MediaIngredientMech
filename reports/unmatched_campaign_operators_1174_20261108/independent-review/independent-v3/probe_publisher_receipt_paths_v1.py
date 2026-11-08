"""Independent #1198 receipt destination counterexample replay, no corpus writes."""
from pathlib import Path
import importlib.util,json,sys,hashlib
import pytest
D=Path(__file__).resolve().parent;S=D/'publisher-snapshot-v2';sys.path.insert(0,str(S/'src'))
def load(n,p):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);sys.modules[n]=m;s.loader.exec_module(m);return m
c=load('mediaingredientmech.campaign_publication',S/'src/mediaingredientmech/campaign_publication.py');t=load('receipt_path_fixture',S/'tests/test_campaign_publication.py');out=[]
for spelling in ['reports/../outside-reports','reports/unused/../publication']:
 d=D/'receipt-path-fixtures-v1'/str(len(out));d.mkdir(parents=True)
 with pytest.MonkeyPatch.context() as monkey:
  case=t.case.__wrapped__(d,monkey);root=case['root'];(root/'outside-reports').mkdir();(root/'reports/unused').mkdir();path=root/spelling;before={p:c.sha((root/p).read_bytes()) for p in (c.SOURCE,c.POLICY,c.SIDECAR,c.BASELINE)};attempts=[]
  for apply in [False,True]:
   try:r=c.publish(root,case['path'],path,apply=apply);result={'returned':r['status']}
   except Exception as e:result={'error':type(e).__name__+': '+str(e)}
   result['apply']=apply;attempts.append(result)
  preserved=all(c.sha((root/p).read_bytes())==h for p,h in before.items());empty=not list((root/'outside-reports').iterdir()) and not list(case['out'].iterdir());assert preserved and empty;assert all('noncanonical' in x.get('error','').lower() for x in attempts);out.append({'spelling':spelling,'attempts':attempts,'all_four_inputs_preserved':preserved,'no_outputs':empty})
report={'publisher_sha256':hashlib.sha256((S/'src/mediaingredientmech/campaign_publication.py').read_bytes()).hexdigest(),'results':out,'scope':'Independent final-source recheck of author-confirmed existing1198 output counterpart. Private synthetic ownerproof/generation fixture; actual preflight before reservation. No production edits.'}
with (D/'publisher-receipt-path-results-v1.json').open('x') as f:json.dump(report,f,indent=2);f.write('\n')
print(json.dumps(report,indent=2))
