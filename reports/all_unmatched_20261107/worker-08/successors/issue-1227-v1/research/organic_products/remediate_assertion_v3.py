"""Immutable, peer-routed assertion-method correction; no maintained writes."""
import copy,datetime,hashlib,json,pathlib,yaml
from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.validation.write_validated import write_validated_ingredient,validate_ingredient
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
B=pathlib.Path('reports/all_unmatched_20261107/worker-08');O=B/'successors/issue-1227-v1/research/organic_products'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(p):return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def dg(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
def save(n,x):
 p=O/n;assert not p.exists();p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
P=json.loads((O/'proposals-v2.json').read_text());D=json.loads((O/'decisions-v2.json').read_text());E=json.loads((O/'evidence-additions-v2.json').read_text())
p=next(x for x in P['proposals'] if x['proposal_id']=='op1201-r2a-medium');old=copy.deepcopy(p['after_capture']);q=B/old['path'];assert sha(q)==old['sha256'];x=yaml.safe_load(q.read_text());prior=copy.deepcopy(x)
assert x['component_assertion']['method']=='LABEL_ENUMERATION'
x['component_assertion']['method']='CURATED_INTERPRETATION'
x['component_assertion']['evidence'][0]['evidence_type']='MANUAL_CURATION'
x['component_assertion']['evidence'][0]['notes']+=' The agent curator interprets the ontology definition as a one-level constituent list. ComponentEvidenceTypeEnum.MANUAL_CURATION records this explicit rationale; it is a distinct enum from human-supplied mapping evidence and does not assert human approval. The source label itself does not enumerate these parts.'
record_curation_event(x,curator='worker08 /root/organics issue1227 peer remediation',action='REVIEW_CORRECTION',changes='Resolve independently reported IF-OP1227-F1 (root alias W08-1227-PEER-OP-001): change component method LABEL_ENUMERATION to definition-derived CURATED_INTERPRETATION and use the native component evidence category MANUAL_CURATION with an explicit agent-authored rationale. Preserve all six constituents, identifiers, quantities, UNKNOWN closure, source boundaries and holds. No human approval or full formulation is asserted.',previous_status=x['mapping_status'],new_status=x['mapping_status'],llm_assisted=True,llm_model='GPT-6',timestamp=now)
out=O/'proposed_owners_v3/R2A_Medium.yaml';assert not out.exists();out.parent.mkdir(parents=True,exist_ok=True);write_validated_ingredient(x,out)
p['after_capture']={'root':'artifact','path':str(out.relative_to(B)),'sha256':sha(out)}
eid='op1227-peer-r2a-assertion-v3'
reason='The six named parts derive from an interpreted ontology definition, not enumeration in the source label. Component MANUAL_CURATION is the native curator-rationale category; the mapping evidence remains DATABASE_MATCH. The history explicitly records LLM assistance.'
save('peer-remediation-v3.json',{'at':now,'finding_id':'IF-OP1227-F1','root_alias':'W08-1227-PEER-OP-001','route_before_fix':'successors/issue-1227-v1/COORDINATOR-NEW-FINDINGS-v2.json','proposal_id':p['proposal_id'],'old_capture':old,'new_capture':p['after_capture'],'before_sha256':p['before_sha256'],'reason':reason,'preserved_components':x['components']==prior['components'],'preserved_unknown_completeness':x['component_assertion']['completeness']==prior['component_assertion']['completeness']=='UNKNOWN','mapping_evidence_unchanged':x['ontology_mapping']==prior['ontology_mapping'],'independent_review':'pending exact successor re-review'})
E['evidence'].append({'evidence_id':eid,'kind':'local_validation','capture':{'root':'artifact','path':str((O/'peer-remediation-v3.json').relative_to(B)),'sha256':sha(O/'peer-remediation-v3.json')},'locator':'reason, preserved_components and exact old/new captures','supports_or_contradicts':reason,'url':None})
p['evidence_ids'].append(eid)
for d in D['decisions']:
 if p['proposal_id'] in d['proposal_ids']:d['evidence_ids'].append(eid)
save('decisions-v3.json',D);save('proposals-v3.json',P);save('evidence-additions-v3.json',E)
base={str(f):yaml.safe_load(f.read_text())for f in pathlib.Path('data/ingredients').rglob('*.yaml')};assert not validate_component_partonomy(base.values());overlay=copy.deepcopy(base)
pm={v['proposal_id']:v for v in P['proposals']};count=0
for f in (B/'successors/issue-1227-v1/research').glob('*/assignment.json'):
 for v in json.loads(f.read_text())['proposals']:
  a=pm.get(v['proposal_id'],v);r=yaml.safe_load((B/a['after_capture']['path']).read_text());assert sha(B/a['after_capture']['path'])==a['after_capture']['sha256'];assert not validate_ingredient(r);overlay[a['owner_path']]=r;count+=1
assert not validate_component_partonomy(overlay.values())
assert len(D['decisions'])==51 and len(P['proposals'])==31
assert all(sha(B/v['after_capture']['path'])==v['after_capture']['sha256']for v in json.loads((O/'proposals-v2.json').read_text())['proposals'])
save('validation-v3.json',{'at':now,'status':'PASS','guard':'write_validated_ingredient','changed_payload_count':1,'cases':51,'payloads':31,'all_selected_schema_pass':True,'combined_overlay_proposal_count':count,'partonomy_errors':[],'v2_payload_bytes_unchanged':True,'unchanged_component_bytes_semantics':x['components']==prior['components'],'scientific_approval':False})
H=json.loads((O/'PRIMARY-HANDOFF.json').read_text());H['frozen_at']=now;H['supersedes']='PRIMARY-HANDOFF.json; all prior files remain immutable';H['final_selection']={'decisions':'decisions-v3.json','proposals':'proposals-v3.json','evidence_additions':'evidence-additions-v3.json'}
H['files'].update({n:sha(O/n)for n in ['decisions-v3.json','proposals-v3.json','evidence-additions-v3.json','peer-remediation-v3.json','validation-v3.json']});H['payload_hashes']={v['proposal_id']:v['after_capture']['sha256']for v in P['proposals']};H['case_hashes']={d['case_id']:dg(d)for d in D['decisions']};H['validation']='v3 guarded write and native schema pass; all113 assignment-overlay payloads pass schema and partonomy; earlier full source and immutability checks remain bound to v2, with this single documented assertion-method delta. No self approval.';H['independent_review']='PENDING exact v3 re-review by /root/inorganics.'
save('PRIMARY-HANDOFF-v3.json',H)
print(json.dumps({'handoff':sha(O/'PRIMARY-HANDOFF-v3.json'),'payload':p['after_capture'],'files':{n:sha(O/n)for n in ['decisions-v3.json','proposals-v3.json','evidence-additions-v3.json']}}))
