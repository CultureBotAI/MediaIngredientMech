from pathlib import Path
import json,hashlib,subprocess,sys,yaml
R=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech');C=R/'.temp/all-unmatched-20261107';D=C/'integration/final-application-accounting-v1';O=Path(__file__).resolve().parent;I=C/'integration/worktree';sys.path.insert(0,str(I/'src'))
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
sha=lambda b:hashlib.sha256(b).hexdigest();conf=json.loads((D/'observer-config-v4.json').read_text());inv=json.loads((D/'materialized-v4/before-owner-inventory.json').read_text())['owners'];base={}
for p,h in inv.items():
 b=(Path(conf['baseline_owner_root'])/p).read_bytes();assert sha(b)==h;base[p]=yaml.safe_load(b)
origins={x['origin_id']:x for x in json.loads((D/'materialized-v4/origins.json').read_text())};workers={x['worker_slot']:x for x in conf['workers']}
def prop(k):
 x=origins[k];w=workers[x['worker_slot']];b=subprocess.check_output(['git','-C',w['worktree'],'show',x['published_head']+':'+w['artifact_prefix']+'/'+x['proposal']['after_capture']['path']]);assert sha(b)==x['payload_sha256'];return yaml.safe_load(b)
def check(name,replace):
 state=base|replace;vs=validate_component_partonomy(state.values());return {'name':name,'errors':len(vs),'violations':[{'code':x.code,'record_id':x.record_id,'message':x.message}for x in vs]}
rows=[check('baseline',{})];assert rows[0]['errors']==0
for name,k in [('borax-owner-alone','w01::KG26-PROP-175-STRUCTURAL-IDENTITY'),('generic-peptone-owner-alone','w05::MATERIALS-C1193-peptone-identity'),('clarified-rumen-owner-alone','w05::R1193-P-clarifiedrumen266'),('cooked-meat-owner-alone','w05::M1193-P-COOKED-MEAT')]:
 x=origins[k];row=check(name,{x['before_preflight']['before_path']:prop(k)});rows.append(row)
assert [r['errors']for r in rows]==[0,3,0,3,2]
boraxkeys=['w01::KG26-PROP-175-STRUCTURAL-IDENTITY','w01::KG26-PROP-175-UW-CONCENTRATED-BASE','w01::KG26-PROP-175-UW-CONCENTRATED-BASE-NO-MO','w01::KG26-PROP-175-UW-CONCENTRATED-BASE-NO-SULFUR'];replace={origins[k]['proposal']['owner_path']:prop(k)for k in boraxkeys};rows.append(check('borax-with-exact-three-coupled-payloads',replace));assert rows[-1]['errors']==0
record={'status':'PASS','native_module':str(I/'src/mediaingredientmech/validation/component_partonomy.py'),'native_module_sha256':sha((I/'src/mediaingredientmech/validation/component_partonomy.py').read_bytes()),'baseline_records':len(base),'scope':'Private in-memory exact-byte counterfactuals only, not corpus application or scientific approval','cases':rows,'semantic_limit':'Peptone owner-only transition is structurally green because Bacto Peptone remains at MICRO:0000178. This does not prove the19 inherited generic references are source-valid Bacto references. Exact source-specific dispositions remain mandatory.'}
with(O/'native-dependency-probe.json').open('x')as f:json.dump(record,f,indent=2);f.write('\n')
print(json.dumps({'native_module_sha256':record['native_module_sha256'],'cases':[(x['name'],x['errors'])for x in rows]}))
