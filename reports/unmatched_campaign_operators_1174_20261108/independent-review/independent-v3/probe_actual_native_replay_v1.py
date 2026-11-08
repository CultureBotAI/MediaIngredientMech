"""Independent final-code native reconstruction; reads frozen fixture/data only."""
from pathlib import Path
import hashlib,json,socket,sys,time,ast
D=Path(__file__).resolve().parent;C=D.parents[1];I=C/'integration/worktree';S=D/'publisher-snapshot-v2';sys.path.insert(0,str(S/'src'))
from mediaingredientmech import campaign_publication as p
from mediaingredientmech.curate import campaign_owner_apply as owner
A=I/'.temp/campaign-publication-handoff-v1';sha=lambda path:hashlib.sha256(path.read_bytes()).hexdigest();manifest=json.loads((A/'ARTIFACTS.json').read_bytes());verified=[]
for x in manifest:
 path=I/x['path'];actual=sha(path);assert actual==x['sha256'];verified.append({'path':x['path'],'sha256':actual})
controls=I/'.temp/campaign-publication-native-controls-v4';result=json.loads((controls/'results.json').read_bytes());plan=result['results'][0]['plan'];before=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/kgm-unmapped-20261107/worktree/reports/kgm_unmapped_chemicals_20261107/sodium-acetate/publication/canonical-before.tsv').read_bytes();inventory=owner.hashes(owner.inventory(I));attempts=[]
def blocked(*args,**kwargs):attempts.append(str(args[:1]));raise AssertionError('Network is forbidden')
socket.socket.connect=blocked;socket.create_connection=blocked
started=time.monotonic();capture=p.Capture(I);candidate,sidecar,m=p._generation(capture,plan,before,inventory);capture.verify();assert owner.hashes(owner.inventory(I))==inventory;assert not attempts
old=A/'before-package-type-corrections.py';new=S/'src/mediaingredientmech/campaign_publication.py'
def gen(q):return ast.dump(next(n for n in ast.parse(q.read_text()).body if isinstance(n,ast.FunctionDef) and n.name=='_generation'),include_attributes=False)
assert gen(old)==gen(new)
out={'publisher_sha256':sha(new),'owner_sha256':sha(S/'src/mediaingredientmech/curate/campaign_owner_apply.py'),'native_producer_revision':p.PRODUCER_REVISION,'native_rows':len(p.table(candidate)[2]),'candidate_sha256':p.sha(candidate),'sidecar_sha256':p.sha(sidecar),'captured_input_count':len(capture.files),'absent_input_count':len(capture.absent),'owner_count':len(inventory),'whole_owner_inventory_preserved':True,'network_attempts':attempts,'elapsed_seconds':time.monotonic()-started,'author_artifacts_verified':verified,'author_native_controls':{'result_sha256':sha(controls/'results.json'),'count':result['controls'],'results':[{'name':x['name'],'status':x['status'],'error':x.get('error')} for x in result['results']],'generation_ast_equals_final':True},'scope':'Independent execution of final-code _generation and capture.verify against mechanically relocated archived diagnostic triple and exact historical prior canonical. Reads current frozen catalog/KG/Claw only; no corpus edit, real campaign generation, approval or publication.'}
with (D/'actual-native-replay-result-v1.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({k:v for k,v in out.items() if k!='author_artifacts_verified'},indent=2))
