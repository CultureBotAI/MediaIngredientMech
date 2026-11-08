from pathlib import Path
import json,yaml,hashlib,copy,shutil
from mediaingredientmech.validation.write_validated import write_validated_ingredient
W=Path.cwd();R=W/'reports/all_unmatched_20261107/worker-06';S=R/'successor-v5';T=W/'.temp/info004-successor-v1';I=T/'independent-a5';V=T/'author-pre-review-v1-snapshot'
def read(p):return json.loads(p.read_text())
def save(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for rel in ['held-payloads/Trace_Metal_Mix_A5-source-M2499.yaml','held-proposals.json','author-draft/decisions.json','changed-payloads.json']:
 p=V/rel;p.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(S/rel,p)
refs=read(I/'component-identities-v1.json');p=S/'held-payloads/Trace_Metal_Mix_A5-source-M2499.yaml';y=yaml.safe_load(p.read_text());names={x['raw_TOGO_component_name']:x for x in refs['results']}
for c in y['components']:
 if c['component_name'] in names:
  raw=c['component_name'];r=names[raw];owner=yaml.safe_load((W/r['authentic_owner']['path']).read_text());assert owner['identifier']==r['component_id'] and owner['mapping_status']!='REJECTED';assert sha(W/r['authentic_owner']['path'])==r['authentic_owner']['sha256'];c.update(component_name=r['recommended_component_name'],reference_scope='MIM_CATALOG',component_id=r['component_id'])
y['component_assertion']['evidence'][0]['notes']='LLM-assisted literal transcription of all seven immediate printed inputs, retaining source order, amounts and units. COMPLETE is relative only to this source list, not resolved copper identity or whole-owner applicability. Six source-supported names/forms reference current native owners; raw /components/1/items/1 component_name is exactly Na2MoO4 · 2H2O, represented using its explicitly printed label Sodium molybdate dihydrate to match the active native owner; no form inference is added. Other six raw component_name strings are preserved exactly. Literal CuSO2・5H2O remains UNMAPPED without component_id: it contradicts the normalized Copper(II) sulfate pentahydrate label and must not be silently corrected. Distilled water1L is an added input, not measured final stock volume; six solute values explicitly use g/L. These component links do not approve the whole child owners, inherited roles or exports.'
y['notes']=y['notes'].replace('All seven entries are literal ungrounded source inputs at this held stage; this does not assert that the other six chemical/material names are inherently unresolvable.','Six source-supported input forms link to current native owners; raw Na2MoO4 · 2H2O is retained in assertion notes while its explicit source label Sodium molybdate dihydrate names that component. The copper input remains UNMAPPED. Native child links do not clear any inherited whole-owner deficiencies.')
y['curation_history'][-1]['changes']+=' Six literal supported forms reference current native owners; raw molybdate formula is retained in assertion notes, copper stays UNMAPPED.'
write_validated_ingredient(y,p)
h=read(S/'held-proposals.json');h['held_proposals'][0]['after_capture']['sha256']=sha(p);save(S/'held-proposals.json',h)
d=read(S/'author-draft/decisions.json');d['decisions'][112]['no_change_reason']=d['decisions'][112]['no_change_reason'].replace('all child references are retained as literal UNMAPPED entries at this held stage.','six supported input forms reference current native owners with exact raw-form preservation, while copper remains ungrounded.');save(S/'author-draft/decisions.json',d)
x=read(S/'changed-payloads.json');x['held_noninstallable_drafts'][0]['after']['sha256']=sha(p);save(S/'changed-payloads.json',x)
shutil.copytree(I/'component-owner-captures',S/'inputs/a5-component-owners',dirs_exist_ok=True);shutil.copyfile(I/'component-identities-v1.json',S/'inputs/a5-component-identities-v1.json')
print('Native six form links added to held draft; no installable A5 candidate')
