"""Bounded corrections from A's independent final review; preserve prior freeze."""
from pathlib import Path
import json, hashlib, datetime, shutil
import yaml
from mediaingredientmech.validation.write_validated import write_validated_ingredient, validate_ingredient
from mediaingredientmech.validation.component_partonomy import load_curated_records, validate_component_partonomy
R=Path(__file__).resolve().parents[1]
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
files=['parts/b-decisions.json','parts/b-evidence.json','parts/b-proposals.json','parts/b-final-freeze-remediated.json','parts/b-proposal-validation-final.json','parts/b-remediation.py','proposed_owners/b-jcm_706_l_cysteine_hcl_monohydrate_5_percent.yaml','proposed_owners/b-jcm_1422_l_cysteine_hcl_monohydrate_5_percent.yaml']
archive=R/'parts/b-pre-dose-correction'
archive.mkdir(exist_ok=False)
manifest=[]
for f in files:
 dest=archive/Path(f).name;shutil.copyfile(R/f,dest)
 manifest.append({'original':f,'copy':dest.relative_to(R).as_posix(),'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()})
(archive/'manifest.json').write_text(json.dumps({'preserved_at':now,'artifacts':manifest},indent=2)+'\n')
D=json.loads((R/'parts/b-decisions.json').read_text());E=json.loads((R/'parts/b-evidence.json').read_text());P=json.loads((R/'parts/b-proposals.json').read_text())
def decision(i):return D['decisions'][i-70]
fixes={
 'B-PROPOSAL-jcm_706_l_cysteine_hcl_monohydrate_5_percent':('0.05ml per10ml medium','0.05ml per4.7ml medium','Concentration5% belongs to added stock; final10ml culture concentration is not asserted.','Concentration5% belongs to added stock; the original dosing denominator is4.7ml of medium before the listed stock additions, not10ml and not an asserted final volume.'),
 'B-PROPOSAL-jcm_1422_l_cysteine_hcl_monohydrate_5_percent':('Original JCM1422 specifies4ml of5% monohydrate stock.','Current captured JCM1422 specifies4ml per liter of5% monohydrate stock. The frozen JCM_J1422 occurrence instead retains10.0ml/L: this current-versus-frozen dose discrepancy is preserved explicitly, without changing the frozen value or asserting the two recipe versions are identical.','','')
}
changed=[]
for p in P['proposals']:
 if p['proposal_id'] not in fixes:continue
 f=R/p['after_capture']['path'];x=yaml.safe_load(f.read_text());a,b,c,d=fixes[p['proposal_id']]
 def correction(s):
  assert a in s
  s=s.replace(a,b)
  if c:s=s.replace(c,d)
  return s
 x['notes']=correction(x['notes'])
 for e in x['component_assertion']['evidence']:e['notes']=correction(e['notes'])
 p['limitations']=correction(p['limitations'])
 x['curation_history'].append({'timestamp':now,'curator':'all-unmatched-20261107-worker07-primary_b','action':'SOURCE_DOSE_CONTEXT_CORRECTION','changes':b+' '+d+' Independent reviewer A identified the discrepancy; only this proposed payload is corrected.','llm_assisted':True})
 write_validated_ingredient(x,f,yaml_kwargs={'width':100})
 p['after_capture']['sha256']=hashlib.sha256(f.read_bytes()).hexdigest();changed.append(p['proposal_id'])
for i,tail in [
 (95,' Concrete source-qualified nominal stock proposals preserve three separate DSMZ source families110,78 and110a. UNKNOWN component-list completeness retains unreported stock solvent and preparation details without deferring the whole stock.'),
 (121,' Concrete source-qualified nominal stock proposals preserve thirteen primary JCM stock families; JCM1463 explicitly inherits JCM1462 with only NaCl changed. Current JCM1422 specifies4ml/L stock, whereas its frozen occurrence retains10.0ml/L; this version/context discrepancy is preserved without changing either source value. UNKNOWN component-list completeness retains unreported solvent and percentage basis.'),
 (134,' Concrete source-qualified nominal stock proposals preserve six primary JCM stock families; TogoM708 explicitly inherits medium687 with only methanol solution replaced by formate solution. Original JCM706 gives0.05ml stock per4.7ml of medium before stock additions, not per10ml. UNKNOWN component-list completeness retains unreported solvent and percentage basis.')]:
 d=decision(i);d['reasoning']=d['reasoning'].split(' Concrete source-qualified nominal stock proposals')[0]+tail
 d['applicability']='Applies only to the exact frozen raw label, occurrence IDs and full captured source contexts enumerated in this decision. Source-scoped subset refinements and proposal occurrence_ids take precedence over generic labels. '+d['reasoning']
for i,suffix,path,url,locator,support in [
 (121,'JCM1422','captures/b-primary-3682c3134ce76822.html','https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1422','Final stock-addition table, prior to inoculation','Current primary gives5% L-cysteine hydrochloride monohydrate stock4.0ml per liter. Frozen exact JCM1422 component instead records10.0ml/L. Both values retained; nominal5% stock identity is supported without asserting unchanged dosing between source versions.'),
 (134,'JCM706','captures/b-primary-3f852a56428bf9b0.html','https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=706','Sentence immediately preceding stock-addition table: per4.7ml of medium','Primary specifies0.05ml of5% L-cysteine hydrochloride monohydrate stock per4.7ml of medium before the listed additions. Prior proposed10ml denominator was a transcription error and is corrected; frozen source values remain untouched.')]:
 prior=next(e for e in E['evidence'] if e.get('url')==url and e['capture']['path']==path)
 eid='B-FINAL-DOSE-'+suffix
 E['evidence'].append({'evidence_id':eid,'kind':'primary_source','capture':{'root':'artifact','path':path,'sha256':hashlib.sha256((R/path).read_bytes()).hexdigest()},'url':url,'accessed_at':prior['accessed_at'],'locator':locator,'supports_or_contradicts':support,'case_ids':[decision(i)['case_id']]})
 decision(i)['evidence_ids'].append(eid)
 for p in P['proposals']:
  if decision(i)['case_id']in p['case_ids']:p['evidence_ids'].append(eid)
for stem,obj in [('decisions',D),('evidence',E),('proposals',P)]:
 (R/f'parts/b-{stem}.json').write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
# Keep the materializer aligned; do not re-render unaffected draft histories.
f=R/'parts/b-remediation.py';s=f.read_text().replace("'0.05ml per10ml medium'","'0.05ml per4.7ml medium'").replace('final10ml culture concentration is not asserted.','the original denominator is4.7ml before stock additions, not10ml or finalvolume.').replace('Autoclaved and stored under N2; added prior to inoculation.','Autoclaved and stored under N2; added prior to inoculation. Current primary dose4ml/L differs from frozenJCM1422 dose10.0ml/L; preserve both source versions without changing frozen quantities.')
s=s.replace(" decision(i)['reasoning']+=' Concrete source-qualified nominal stock proposals now preserve each distinct primary recipe family; explicit source inheritance is recorded for1463→1462 andM708→687. UNKNOWN component-list completeness retains unreported solvent and preparation basis without deferring the whole stock.'", " decision(i)['reasoning']+=' Concrete source-qualified nominal stock proposals preserve each distinct primary recipe family. '+({95:'DSMZ110,78 and110a stocks remain separately scoped.',121:'JCM1463 explicitly inherits1462; currentJCM1422 dose4ml/L differs from frozen10.0ml/L, with both retained.',134:'M708 explicitly inherits687 replacing methanol only; JCM706 dose0.05ml refers to4.7ml medium before stock additions.'}[i])+' UNKNOWN component-list completeness retains unreported solvent and preparation basis without deferring the whole stock.'")
f.write_text(s)
catalog=load_curated_records(Path('data/curated'));out=[]
for p in P['proposals']:
 f=R/p['after_capture']['path'];x=yaml.safe_load(f.read_text());errors=validate_ingredient(x);violations=validate_component_partonomy([r for r in catalog if r.get('identifier')!=x['identifier']]+[x])
 out.append({'proposal_id':p['proposal_id'],'path':p['after_capture']['path'],'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'schema_errors':[e.message for e in errors],'partonomy_violations':[str(v)for v in violations]})
assert not any(x['schema_errors']or x['partonomy_violations']for x in out)
(R/'parts/b-proposal-validation-final.json').write_text(json.dumps({'validated_at':now,'method':'Native closed IngredientRecord schema plus complete maintained catalogue partonomy with each exact draft substituted. Two corrected payloads written through guarded native writer; no maintained write.','proposals':out},indent=2)+'\n')
names=['parts/b-decisions.json','parts/b-evidence.json','parts/b-proposals.json','parts/b-family-review.json','parts/b-proposal-validation-final.json']
freeze={'frozen_at':now,'status':'primary_frozen_pending_independent_delta_review','supersedes':'parts/b-pre-dose-correction/b-final-freeze-remediated.json','artifacts':[{'path':p,'sha256':hashlib.sha256((R/p).read_bytes()).hexdigest()}for p in names],'changed_payloads':changed,'changes':['JCM706 dose denominator corrected to4.7ml from primary','JCM1422 current4ml/L versus frozen10ml/L discrepancy explicitly preserved','B95/121/134 inheritance commentary scoped individually','66 exact payloads pass native schema and fullcatalogue partonomy again']}
(R/'parts/b-final-freeze-remediated.json').write_text(json.dumps(freeze,indent=2)+'\n')
print(json.dumps(freeze,indent=2));print('counts',len(D['decisions']),len(E['evidence']),len(P['proposals']))
