from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,copy,yaml
from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.validation.write_validated import write_validated_ingredient
W=Path.cwd();S=W/'.temp/w05-buffer-parts-v1';O=S/'media';at=datetime.now(timezone.utc).isoformat();j=lambda p:json.loads(p.read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
parent=next(x for x in j(S/'parents-direct-v1/proposals.json')['proposals'] if x['proposal_id']=='W05-FINAL-MAT-039');cap=parent['after_capture'];f=S/cap['path'].removeprefix('buffer-parts-v1/');assert sha(f)==cap['sha256'];pr=yaml.safe_load(f.read_text());assert pr['identifier']=='mesh:D010461'
D=j(O/'decisions-v2.json');P=j(O/'proposals-v2.json');E=j(O/'evidence-v2.json');M=j(O/'component-assessments-v2.json');p=next(x for x in P['proposals'] if x['proposal_id']=='M1193-P-RCM-182');oldcap=copy.deepcopy(p['after_capture']);old=yaml.safe_load((S/oldcap['path'].removeprefix('buffer-parts-v1/')).read_text());r=copy.deepcopy(old);assert r['components'][0]['component_id']=='kgmicrobe.ingredient:peptone';r['components'][0]['component_id']='mesh:D010461'
a='RCM printed generic Peptone input remains10 g per litre of standard reconstitution. Bind this one previously supported generic material component to the selected actual generic owner mesh:D010461, following exact reviewed W05-FINAL-MAT-039. Native section3 direct unspecified-sense priority supersedes the provisional local parent; no supplier, lot assay, substrate or enzyme inference is added. No other RCM part, quantity, nine-input COMPLETE scope or approximate/performance-adjustment qualification changes. Parent application remains conditional; no global old-ID redirect, named-product equivalence or source/role/export approval.'
r['component_assertion']['evidence'].append(dict(evidence_type='RECIPE_SOURCE',source=old['component_assertion']['evidence'][0]['source'],notes=a+' Agent-assisted applicability assessment of the exact retained complete manufacturer formula; no historical human attribution.'))
record_curation_event(r,curator='Codex W05 /root consolidated exact component continuity',action='CORRECTED',changes=a,previous_status=r['mapping_status'],new_status=r['mapping_status'],llm_assisted=True,llm_model='gpt-6')
f=O/'proposed-v3/Reinforced_Clostridial_Medium.yaml';assert not f.exists();write_validated_ingredient(r,f);assert yaml.safe_load(f.read_text())==r
for k in set(old)|set(r):
 if k not in ['components','component_assertion','curation_history']:assert old.get(k)==r.get(k)
assert r['curation_history'][:-1]==old['curation_history'];assert r['components'][1:]==old['components'][1:]
c0=copy.deepcopy(r['components'][0]);c0['component_id']=old['components'][0]['component_id'];assert c0==old['components'][0]
p['after_capture']=dict(root='artifact',path='buffer-parts-v1/media/proposed-v3/'+f.name,sha256=sha(f));p['description']+=' Final direct-term continuity: '+a;p['component_direct_continuity']=dict(author='/root',at=at,predecessor_capture=oldcap,parent_capture=cap,assessment=a);eid='W05-REMAINING-MEDIA-RCM-DIRECT-PARENT';p['evidence_ids'].append(eid)
row=next(x for x in M['rows'] if x['proposal_id']==p['proposal_id'] and x['index']==0);row['previous_direct_term_assessment']=copy.deepcopy(row);row.update(assessment=a,selected_component=r['components'][0],selected_identifier='mesh:D010461',selected_parent_proposal=parent)
M['at']=at;M['direct_term_predecessor_matrix']=dict(path='component-assessments-v2.json',sha256=sha(O/'component-assessments-v2.json'))
for x in M['payload_reviews']:
 if x['proposal_id']==p['proposal_id']:x['after_capture']=p['after_capture'];x['direct_term_predecessor_capture']=oldcap
for d in D['decisions']:
 if d['case_id'] in p['case_ids']:d['media_component_reassessment']['direct_parent_continuity']=copy.deepcopy(p['component_direct_continuity']);d['evidence_ids'].append(eid)
def put(n,x):
 f=O/n;assert not f.exists();f.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
put('component-assessments-v3.json',M);E['evidence'].append(dict(evidence_id=eid,kind='source_snapshot',capture=dict(root='artifact',path='buffer-parts-v1/media/component-assessments-v3.json',sha256=sha(O/'component-assessments-v3.json')),url=None,accessed_at=at,locator='Exact RCM component0 and generic parent capture; all25 printed parts retained',supports_or_contradicts=a,case_ids=p['case_ids']))
put('proposals-v3.json',P);put('decisions-v3.json',D);put('evidence-v3.json',E);put('direct-continuity-receipt-v3.json',p['component_direct_continuity']);print(json.dumps(p['after_capture']))
