from pathlib import Path
import json,hashlib,datetime,shutil,sys,subprocess
import yaml
sys.path.insert(0,str(Path.cwd()/'src'))
from mediaingredientmech.validation.component_partonomy import load_ingredient_records,validate_component_partonomy
R=Path.cwd();A=R/'reports/all_unmatched_20261107/worker-10';O=A/'successor-v3/hcl-manual';H=O/'history/report-edition-correction';H.mkdir(parents=True,exist_ok=True)
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rd(p):return json.loads(p.read_text())
def wr(p,d):p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
def can(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
archive=[]
for name in ['primary-review.json','evidence-fragment.json']:
 p=O/name;t=H/name;assert not t.exists();shutil.copyfile(p,t);archive.append({'path':str(t.relative_to(A)),'sha256':h(t)})
p=O/'primary-review.json';d=rd(p);old=d['manufacturer_review']['older_edition'];assert 'BeefHeartInfusion3g'in old;d['manufacturer_review']['older_edition']=old.replace('BeefHeartInfusion3g','Beef Heart Digest3g');d['science_frozen_at']=now();wr(p,d)
e=rd(O/'evidence-fragment.json');next(x for x in e['evidence']if x['evidence_id']=='sv3-hm-primary-review')['capture']['sha256']=h(p);wr(O/'evidence-fragment.json',e)
wr(O/'report-edition-correction.json',{'at':now(),'archived_pre_correction_bytes':archive,'field':'manufacturer_review.older_edition','before':old,'after':d['manufacturer_review']['older_edition'],'basis':'Actual older PDF page151 text reads Beef Heart Digest3.0g.2009PDF page158 reads BeefHeart,Infusion from500g3.0g.','payloads_unchanged':True,'source_capture_bytes_unchanged':True,'scientific_scope_unchanged':True})
oldps={x['proposal_id']:x for x in rd(A/'successor-v2/proposals.json')['proposals']};old_ds={x['case_id']:x for x in rd(A/'successor-v2/decisions.json')['decisions']};ps=rd(O/'proposals-fragment.json')['proposals'];ds=rd(O/'decision-fragment.json')['decisions'];ev=rd(O/'evidence-fragment.json')['evidence'];old_ev={x['evidence_id']:x for x in rd(A/'successor-v2/evidence.json')['evidence']};new_ev={x['evidence_id']:x for x in ev};all_ev=old_ev|new_ev
ledgerdiff={'proposals':[],'decisions':[]}
for p in ps:
 old=oldps[p['supersedes']['proposal_id']];ledgerdiff['proposals'].append({'old_id':old['proposal_id'],'new_id':p['proposal_id'],'old_sha256':can(old),'new_sha256':can(p),'fields':{k:{'before':old.get(k),'after':p.get(k)}for k in old.keys()|p.keys()if old.get(k)!=p.get(k)}})
for d in ds:
 old=old_ds[d['case_id']];ledgerdiff['decisions'].append({'case_id':d['case_id'],'old_sha256':can(old),'new_sha256':can(d),'fields':{k:{'before':old.get(k),'after':d.get(k)}for k in old.keys()|d.keys()if old.get(k)!=d.get(k)}})
wr(O/'ledger-field-diffs.json',ledgerdiff)
errors=[];checks=[]
def ck(name,val):checks.append({'check':name,'pass':val}); errors.extend([]if val else[name])
for p in ps:
 ck(p['proposal_id']+' payload hash',h(A/p['after_capture']['path'])==p['after_capture']['sha256']);r=yaml.safe_load((A/p['after_capture']['path']).read_text());old=oldps[p['supersedes']['proposal_id']];orig=yaml.safe_load((A/old['after_capture']['path']).read_text());ck(p['proposal_id']+' full historical prefix',r['curation_history'][:-1]==orig['curation_history']);ck(p['proposal_id']+' components exact unchanged',r['components']==orig['components']);ck(p['proposal_id']+' ID and owner continuity',r['identifier']==orig['identifier']and p['owner_path']==old['owner_path']);ck(p['proposal_id']+' no old wrapper active','sv1-kg-bd-manual-browser'not in p['evidence_ids']);ck(p['proposal_id']+' evidence all exists',all(k in all_ev for k in p['evidence_ids']))
for d in ds:
 old=old_ds[d['case_id']];ck(d['case_id']+' complete raw identity/occurrence preserved',all(d[k]==old[k]for k in ['case_id','case_input_sha256','source','occurrence_ids','owner_records']));ck(d['case_id']+' no old wrapper active','sv1-kg-bd-manual-browser'not in d['evidence_ids']);ck(d['case_id']+' evidence all exists',all(k in all_ev for k in d['evidence_ids']))
for e in ev:ck(e['evidence_id']+' capture hash',h(A/e['capture']['path'])==e['capture']['sha256'])
lookup=rd(O/'inputs/native-owner-lookup.json');ck('all maintained owner bytes unchanged',all(h(Path(x['path']))==x['sha256']for x in lookup['inventory']))
records=load_ingredient_records(R/'data/ingredients');proposed=[yaml.safe_load((A/p['after_capture']['path']).read_text())for p in ps];v=validate_component_partonomy(records+proposed);ck('final overlay component partonomy',not v)
strict=(O/'validation/strict.stderr').read_text();ck('strict5zero','files scanned:      5'in strict and 'total ERROR rows:   0'in strict)
ck('exact6decisions5proposals27evidence',len(ds)==6 and len(ps)==5 and len(ev)==27)
wr(O/'validation/final-integrity.json',{'at':now(),'checks':checks,'errors':errors,'counts':{'decisions':len(ds),'proposals':len(ps),'new_evidence':len(ev),'original_occurrences':sum(len(x['occurrence_ids'])for x in ds),'native_owners':len(records),'proposed_payloads':len(proposed)},'native_guard_errors':0,'native_strict_errors':0,'final_partonomy_violations':[vars(x)for x in v]})
assert not errors,errors
wr(O/'HANDOFF.json',{'author':'/root/bio_research','science_frozen_at':now(),'scope':'CHEM-COMP-004 HCl939/943/944/946, readonlyW02entry106; BIO-F07Difco980 only.','case_indices':[65,87,94,102,125,178],'proposal_ids':[p['proposal_id']for p in ps],'counts':{'decisions':6,'proposals':5,'new_evidence':27,'hcl_pairs':10},'claims':'HCl literal strengths/source scope retained; exact relations unresolved. Actual BD2009PDF replaces wrapper as positive support. No newhistorical lot/composition/role/export approval.','mapping_evidence':'11 unchanged inherited MANUAL claim objects remain for root claim-specific1226pass; one revised35%claim and five new claims are honestlyLLM_SUGGESTION. Full correspondence file included.','candidate_destinations_and_hashes':[{'owner_path':p['owner_path'],'proposal_id':p['proposal_id'],'after_capture':p['after_capture'],'before_sha256':p['before_sha256']}for p in ps],'independent_review':'pending separate skeptic; root final head/enum pass may change bytes and requires rebinding','validation':'guard5 strict5 errors0; corpus2956+5partonomy0, subject to exact receipt count; all original components/history prefixes/case/occurrences preserved','authorship':'Not originalHCl/KG980author; prior buffer skeptical review acknowledged. Author of separateOxoid921 is not its independent reviewer here.','no_git_or_maintained_changes':True})
# Bind exact final author bytes, excluding only this forthcoming manifest.
files=[{'path':str(p.relative_to(A)),'sha256':h(p),'bytes':p.stat().st_size}for p in sorted(O.rglob('*'))if p.is_file()and p.name!='author-freeze.json']
freeze={'at':now(),'status':'frozen_for_separate_skeptical_review','files':files,'count':len(files),'core':{n:h(O/n)for n in ['primary-review.json','decision-fragment.json','proposals-fragment.json','evidence-fragment.json','mapping-claim-correspondence.json','validation/final-integrity.json']},'scope':'Author scientific payloads/metadata only. Root claim-specific enum successor and independent review remain separate.','unclaimed':'No wholeowner/role/export/source release or merge approval.'};wr(O/'author-freeze.json',freeze)
print(json.dumps({'freeze_sha256':h(O/'author-freeze.json'),'core':freeze['core'],'files':len(files),'counts':rd(O/'validation/final-integrity.json')['counts']},indent=2))
