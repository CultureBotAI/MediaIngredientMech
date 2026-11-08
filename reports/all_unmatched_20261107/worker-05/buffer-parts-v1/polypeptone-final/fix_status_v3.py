from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,copy
O=Path('.temp/w05-buffer-parts-v1/polypeptone-final');j=lambda p:json.loads(p.read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();at=datetime.now(timezone.utc).isoformat()
def put(n,x):
 q=O/n;assert not q.exists();q.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
P=j(O/'proposals-v2.json');D=j(O/'decisions-v2.json');E=j(O/'evidence-v2.json');p=P['proposals'][0]
put('status-finding-before-fix.json',dict(finding_id='W05-CONSOLIDATED-POLYPEPTONE-METADATA-001',at=at,reporter='/root',status='confirmed_before_fix',reproduction=dict(path=str(O/'proposals-v2.json'),sha256=sha(O/'proposals-v2.json'),field='proposals[0].final_grounding_status',value=p['final_grounding_status']),bounded_fix='Preserve authentic inherited status under historical field; set current status to supported named local identity/broader MeSH grounding with coordinator source/owner acceptance separate. YAML and source cases unchanged.',deduplication='New final selector metadata mismatch; not a new chemical finding or historical POLYPEPTONE-001 closure.'))
p['previous_final_grounding_status']=p['final_grounding_status'];p['final_grounding_status']='SUPPORTED_SOURCE_PROPOSAL: named kgmicrobe.ingredient:polypeptone with NARROW_MATCH mesh:D010461; self-only grounding superseded. Exact source-association/quantity/coupled-owner/role/export holds remain; no terminal closure of historical review or coordinator acceptance.'
p['predicate_consequence']='Native broadMatch to mesh:D010461 and exact registry row kgmicrobe.ingredient:polypeptone. Coordinator regeneration/application remains separate; no SSSOM mutation here.'
p['metadata_correction']=dict(finding_id='W05-CONSOLIDATED-POLYPEPTONE-METADATA-001',author='/root',at=at,predecessor_proposals_sha256=sha(O/'proposals-v2.json'))
eid='W05-REMAINING-POLYPEPTONE-STATUS-CONSISTENCY';p['evidence_ids'].append(eid)
for d in D['decisions']:
 d['polypeptone_final_reassessment']['active_grounding_status']=p['final_grounding_status'];d['evidence_ids'].append(eid)
E['evidence'].append(dict(evidence_id=eid,kind='source_snapshot',capture=dict(root='artifact',path='buffer-parts-v1/polypeptone-final/status-finding-before-fix.json',sha256=sha(O/'status-finding-before-fix.json')),url=None,accessed_at=at,locator='Exact proposal status/grounding consistency; old status preserved',supports_or_contradicts=p['final_grounding_status'],case_ids=p['case_ids']))
put('proposals-v3.json',P);put('decisions-v3.json',D);put('evidence-v3.json',E);print('Metadata successor; exact reviewed YAML unchanged')
