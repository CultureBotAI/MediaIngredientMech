from pathlib import Path
import json,hashlib,copy,shutil,datetime,sys
import yaml
sys.path.insert(0,str(Path.cwd()/'src'))
from mediaingredientmech.validation.write_validated import write_validated_ingredient
R=Path.cwd();A=R/'reports/all_unmatched_20261107/worker-10';O=A/'successor-v3/hcl-manual';H=O/'history/initial-author';H.mkdir(parents=True,exist_ok=True)
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def write(p,d):p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
paths=[O/'proposals-fragment.json',O/'decision-fragment.json',O/'evidence-fragment.json',O/'old-new-field-diffs.json',O/'input-hashes.json',O/'validation/guarded-write.json',O/'proposed/hcl_nominal35percent_togo_m3216.yaml']
arch=[]
for p in paths:
 t=H/p.relative_to(O);t.parent.mkdir(parents=True,exist_ok=True);assert not t.exists();shutil.copyfile(p,t);arch.append({'original_path':str(p.relative_to(A)),'archived_path':str(t.relative_to(A)),'sha256':h(p)})
p=O/'proposed/hcl_nominal35percent_togo_m3216.yaml';r=yaml.safe_load(p.read_text());assert r['ontology_mapping']['evidence'][0]['evidence_type']=='MANUAL_CURATION';r['ontology_mapping']['evidence'][0]['evidence_type']='LLM_SUGGESTION';write_validated_ingredient(r,p)
ps=read(O/'proposals-fragment.json');ds=read(O/'old-new-field-diffs.json');guard=read(O/'validation/guarded-write.json')
for x in ps['proposals']:
 if x['after_capture']['path']==str(p.relative_to(A)):x['after_capture']['sha256']=h(p)
for x in ds:
 if x['entry_index']==943:
  x['after_payload']['sha256']=h(p);x['field_changes']['ontology_mapping']['after']=r['ontology_mapping']
for x in guard['targets']:
 if x['payload']['path']==str(p.relative_to(A)):x['payload']['sha256']=h(p)
write(O/'proposals-fragment.json',ps);write(O/'old-new-field-diffs.json',ds);write(O/'validation/guarded-write.json',guard)
cor=[]
oldps={x['proposal_id']:x for x in read(A/'successor-v2/proposals.json')['proposals']}
for x in ps['proposals']:
 old=oldps[x['supersedes']['proposal_id']];oldrec=yaml.safe_load((A/old['after_capture']['path']).read_text());newrec=yaml.safe_load((A/x['after_capture']['path']).read_text());oldclaims=oldrec['ontology_mapping']['evidence'];newclaims=newrec['ontology_mapping']['evidence'];matches=[]
 for i,claim in enumerate(oldclaims):
  newclaim=newclaims[i];matches.append({'original_index':i,'successor_index':i,'original_claim':claim,'successor_claim':newclaim,'unchanged_exact_object':claim==newclaim,'disposition':'preserved exact inherited claim; coordinator may assess its evidence_type'if claim==newclaim else'revised scientific claim; honestly tagged LLM_SUGGESTION by this author'})
 cor.append({'original_proposal_id':old['proposal_id'],'successor_proposal_id':x['proposal_id'],'old_payload':old['after_capture'],'successor_payload':x['after_capture'],'claim_correspondences':matches,'new_claims':[{'successor_index':i,'claim':v}for i,v in enumerate(newclaims)if i>=len(oldclaims)]})
write(O/'mapping-claim-correspondence.json',{'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Full MappingEvidence objects, five payloads. No global enum replacement.','entries':cor})
write(O/'author-revision-receipt.json',{'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'archived_initial_bytes':arch,'reason':'Parent requested honest attribution for any revised MappingEvidence claim. One35% inherited claim had notes corrected; its evidence_type is nowLLM_SUGGESTION. All other inherited claim objects remain exact.','candidate_science_unchanged_from_initial_author':True,'updated_payload_sha256':h(p)})
inputs=read(H/'input-hashes.json');inputs['inputs']=[x for x in inputs['inputs']if x['role']!='new artifact'];inputs['scope']='Immutable input read/copy/hash bindings only. New artifact hashes are bound by author-freeze; initial mixed input/output binding receipt remains archived.';write(O/'input-hashes.json',inputs)
print(json.dumps({'proposal_hash':h(O/'proposals-fragment.json'),'claim_correspondence_hash':h(O/'mapping-claim-correspondence.json'),'revised_payload':h(p)}))
