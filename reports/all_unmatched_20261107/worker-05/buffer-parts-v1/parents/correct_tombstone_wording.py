from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,copy
import yaml
from mediaingredientmech.validation.write_validated import write_validated_ingredient

S=Path(__file__).resolve().parent;T=S/'tombstone';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
before=T/'proposed/Bacto_Soytone.yaml';assert sha(before)=='acd8c572a047d9da64cc6805ec79449da11e2fafb612827bd7bb4b1f37add972'
old=yaml.safe_load(before.read_text());new=copy.deepcopy(old);notes=new['ontology_mapping']['evidence'][-1]['notes'];assert notes.count('historical human evidence')==1
new['ontology_mapping']['evidence'][-1]['notes']=notes.replace('historical human evidence','historical evidence')
out=T/'proposed-v2/Bacto_Soytone.yaml';assert not out.exists();write_validated_ingredient(new,out)
check=copy.deepcopy(new);check['ontology_mapping']['evidence'][-1]['notes']=notes;assert check==old
p=json.loads((S/'final/tombstone-proposals.json').read_text());proposal=p['proposals'][0];proposal['wording_predecessor_capture']=copy.deepcopy(proposal['after_capture']);proposal['after_capture']=dict(root='artifact',path='buffer-parts-v1/parents/tombstone/proposed-v2/Bacto_Soytone.yaml',sha256=sha(out))
dest=S/'final/tombstone-proposals-v2.json';assert not dest.exists();dest.write_text(json.dumps(p,indent=2,ensure_ascii=False)+'\n')
finding=S.parent/'review/parents-new-finding-v1.json';assert sha(finding)=='17e72ff4bf099defa115d92c5e960212301607a25dc1be0474c2ec992684f9b7'
receipt=dict(at=datetime.now(timezone.utc).isoformat(),author='/root/buffer_hepes',finding_id='W05-CONSOLIDATED-PARENTS-REVIEW-001',finding_capture=dict(path=str(finding),sha256=sha(finding)),predecessor=dict(path='tombstone/proposed/Bacto_Soytone.yaml',sha256=sha(before)),successor=proposal['after_capture'],changed_field='/ontology_mapping/evidence/2/notes',before_phrase='historical human evidence',after_phrase='historical evidence',all_other_fields_and_history_exactly_preserved=True,additional_history_events=0,reason='Bounded correction to one new provenance phrase in an unselected private candidate after independent report and root referral. Original material curation event and all historical objects remain unchanged.')
dest=T/'wording-erratum.json';assert not dest.exists();dest.write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(dict(after_sha256=sha(out),changed_field=receipt['changed_field'])))
