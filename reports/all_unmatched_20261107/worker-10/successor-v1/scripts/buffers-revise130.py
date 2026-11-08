from pathlib import Path
import json,yaml,copy,hashlib,datetime,shutil
from mediaingredientmech.validation.write_validated import write_validated_ingredient
from mediaingredientmech.curate.curation_event import record_curation_event
B=Path('reports/all_unmatched_20261107/worker-10');O=B/'successor-v1/buffers';H=O/'history/author-v1';H.mkdir(parents=True,exist_ok=True);sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();now=datetime.datetime.now(datetime.timezone.utc).isoformat()
for name in ['decisions.json','evidence.json','proposals.json','guarded-validation.json','partition-integrity.json']:
 assert not (H/name).exists();shutil.copyfile(O/name,H/name)
d=json.loads((O/'decisions.json').read_text());e=json.loads((O/'evidence.json').read_text());ps=json.loads((O/'proposals.json').read_text());p=next(p for p in ps['proposals'] if p['proposal_id']=='sv1-buffers-carbonate_1m_ph10_jcm1452');f=B/p['after_capture']['path'];(H/'proposed_owners').mkdir(exist_ok=True);shutil.copyfile(f,H/'proposed_owners'/f.name);old=sha(f)
addition=' JCM 1452 explicitly directs separate autoclaving of this buffer followed by aseptic addition to the medium. No stock-specific time or temperature is asserted from the page-wide medium default.'
r=yaml.safe_load(f.read_text());r['notes']+=addition
for z in r['ontology_mapping']['evidence']:z['notes']+=addition
for z in r['component_assertion']['evidence']:z['notes']+=addition
record_curation_event(r,curator='all_unmatched_worker10_successor_buffers',action='ANNOTATED',changes='Independent review correction: retain JCM1452 separate stock autoclaving and aseptic addition explicitly, without inventing a stock sterilization schedule.',llm_assisted=True,timestamp=now)
write_validated_ingredient(r,f);p['after_capture']['sha256']=sha(f);p['description']+=addition
case=next(x for x in d['decisions'] if x['completion_reassessment']['source_index']==130);case['reasoning']+=addition;case['applicability']+=addition
receipt={'checked_at':now,'reviewer_request':'/root/bio_research','source_evidence_id':'buffers-primary-947e5eff24deb387','fix':'Retain explicit separate autoclaving and subsequent aseptic addition; no schedule inference.','before_sha256':old,'after_capture':p['after_capture'],'guarded_writer':'mediaingredientmech.validation.write_validated.write_validated_ingredient','initial_author_snapshot':'successor-v1/buffers/history/author-v1','unchanged_payloads':27,'initial_guarded_and_strict_receipts_scope':'Author-v1 payloads; case130 is superseded by this guarded revision and its separate strict validation.'}
(O/'revision-v2.json').write_text(json.dumps(receipt,indent=2)+'\n')
eid='sv1-buffers-revision-v2';e['evidence'].append({'evidence_id':eid,'capture':{'root':'artifact','path':str((O/'revision-v2.json').relative_to(B)),'sha256':sha(O/'revision-v2.json')},'kind':'local_validation','locator':'case130 process retention and exact revised guarded payload','supports_or_contradicts':receipt['fix'],'url':None,'case_ids':[case['case_id']]});case['evidence_ids'].append(eid);p['evidence_ids'].append(eid)
for name,data in [('decisions',d),('evidence',e),('proposals',ps)]:f=O/(name+'.json');f.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n');print(name,sha(f))
print('payload',p['after_capture'])
