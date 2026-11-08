from pathlib import Path
import sys,json,hashlib,copy,importlib.util,datetime
C=Path(__file__).resolve().parents[2];O=Path(__file__).resolve().parent;W=C/'workers/w02/worktree';A=W/'reports/all_unmatched_20261107/worker-02';P=C/'workers/w04/worktree/.temp/w02-published-head-independent-review-v1'
import yaml
from mediaingredientmech.validation.write_validated import write_validated_ingredient
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
from mediaingredientmech.synonym_policy import is_resolving_synonym
from mediaingredientmech.validation.semantic_release import evidence_gaps
sh=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
claw=C.parent/'kgm-unmapped-20261107/claw/scripts/build_mim_ingredient_sssom.py';spec=importlib.util.spec_from_file_location('claw_w02_triage',claw);m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m)
props=json.load(open(A/'continuation-1201-v1/proposals.json'))['proposals'];F=O/'native-private-fixtures';F.mkdir(exist_ok=False)
cat={str(p.relative_to(W)):yaml.safe_load(p.read_text()) for p in (W/'data/ingredients').glob('*/*.yaml')};ov=copy.deepcopy(cat);rows=[]
for p in props:
 q=A/p['after_capture']['path'];assert sh(q)==p['after_capture']['sha256'];x=yaml.safe_load(q.read_text());dest=F/(hashlib.sha256(p['proposal_id'].encode()).hexdigest()+'.yaml');write_validated_ingredient(x,dest);assert yaml.safe_load(dest.read_text())==x
 ov[p['owner_path']]=x;rows.append({'proposal_id':p['proposal_id'],'owner_path':p['owner_path'],'after_sha256':sh(q),'native_guarded_write':'PASS'})
base=validate_component_partonomy(cat.values());after=validate_component_partonomy(ov.values());assert not base and not after
# Evaluate listed fields against selected overlay, never substitute baseline defects.
ad=json.load(open(P/'assembly-v2/root-adjudication.json'));targets=ad['findings'][4]['originals'][0]['original']['targets'];aliases=[]
for t in targets:
 path=t['owner_path'];before=cat[path];current=ov[path]
 for ix,syn in enumerate(current.get('synonyms',[])):
  text=syn['synonym_text']
  if any(k in text.lower() for k in ['role:','properties:','h o','cl4','malate','water','fe(nh4)','ammonium sulfate hydrate','0.1%']):
   aliases.append({'owner_path':path,'selected_changed':current!=before,'mapping_status':current.get('mapping_status'),'synonym_index':ix,'synonym':syn,'native_mim_eligible':is_resolving_synonym(syn),'native_claw_eligible':m._is_publishable_mim_synonym(syn)})
meta=[x for x in aliases if x['synonym']['synonym_text'].lower().startswith(('role:','properties:'))];assert meta and all(not x['native_mim_eligible'] and not x['native_claw_eligible'] for x in meta)
for text in ['Na SiO .9H O','ZnSO .7H O']:
 s=next(s for s in ov['data/ingredients/mapped/Alk_So42.yaml']['synonyms'] if s['synonym_text']==text);assert s['synonym_type']=='REJECTED_LABEL' and not is_resolving_synonym(s)
report={'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Native structural and literal-policy triage; no scientific or export approval','payload_count':len(rows),'payloads':rows,'baseline_owner_count':len(cat),'baseline_partonomy':[],'overlay_partonomy':[],'native_metadata_excluded':len(meta),'alias_probes':aliases,'selected_role_evidence_gaps':evidence_gaps({p['owner_path']:ov[p['owner_path']] for p in props}),'producer_sha256':{'claw':sh(claw),'schema':sh(W/'src/mediaingredientmech/schema/mediaingredientmech.yaml'),'synonym_policy':sh(W/'src/mediaingredientmech/synonym_policy.py')},'qualification':'Per-synonym eligibility is not a rebuilt downstream index; tombstone routing and credited representatives remain separate. Predicted roles are provisional, not falsity findings.'}
(O/'native-scope-verification.json').open('x').write(json.dumps(report,indent=2)+'\n');print(json.dumps({k:report[k] for k in ['payload_count','baseline_owner_count','native_metadata_excluded','selected_role_evidence_gaps']}))
