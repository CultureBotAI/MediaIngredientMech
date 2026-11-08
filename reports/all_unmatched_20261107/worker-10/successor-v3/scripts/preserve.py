from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,subprocess
R=Path.cwd();A=R/'reports/all_unmatched_20261107/worker-10';S=A/'successor-v3';P=R/'.temp/all-unmatched-worker-10/successor-v3';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();load=lambda p:json.loads(p.read_text())
def save(p,d):
 with p.open('x') as f:json.dump(d,f,indent=2,ensure_ascii=False);f.write('\n')
b=load(P/'preservation-baseline.json');counts={}
for key in ['old_artifacts','owners','native_reviews']:
 for name,expected in b[key].items():assert sha(R/name)==expected,name
 counts[key]=len(b[key])
assert subprocess.check_output(['git','diff','--name-only','808ff934f9cdec7ad8fdc8cdcaa583f1ae068d5e'],text=True)==''
ctx=S/'context';ctx.mkdir(exist_ok=True);dest=ctx/'preservation-baseline.json'
with dest.open('xb') as f:f.write((P/'preservation-baseline.json').read_bytes())
# Retain private draft/reviewed helper and all reproduction scripts as immutable report copies.
copies=[]
for source in sorted(P.rglob('*.py')):
 if any(part.startswith('validation') for part in source.relative_to(P).parts):continue
 target=S/'scripts'/source.relative_to(P);target.parent.mkdir(parents=True,exist_ok=True)
 if target.exists():assert sha(target)==sha(source)
 else:
  with target.open('xb') as f:f.write(source.read_bytes())
 copies.append({'source':str(source.relative_to(R)),'copy':str(target.relative_to(R)),'sha256':sha(source)})
# Canonical source/contract/script inputs are included as hashes, never copied over maintained data.
contracts=['MAPPING_SEMANTICS.md','src/mediaingredientmech/schema/mediaingredientmech.yaml','schema/record_review.yaml','docs/record-reviews.md','docs/record-review-profile.md','.claude/skills/add-media/SKILL.md','.claude/skills/manage-identifiers/SKILL.md','src/mediaingredientmech/curate/curation_event.py','src/mediaingredientmech/validation/write_validated.py','src/mediaingredientmech/validation/component_partonomy.py','src/mediaingredientmech/synonym_policy.py','scripts/audit_duplicate_identifiers.py']
save(S/'reproduction-copy-receipt.json',{'at':datetime.now(timezone.utc).isoformat(),'copies':copies,'contracts':{n:sha(R/n) for n in contracts}})
save(S/'preservation.json',{'at':datetime.now(timezone.utc).isoformat(),'status':'PASS','counts':counts,'baseline':{'path':str(dest.relative_to(R)),'sha256':sha(dest)},'tracked_diff_before_staging':[],'old_source_head':'808ff934f9cdec7ad8fdc8cdcaa583f1ae068d5e','scope':'All previous source artifacts, maintained owner files and canonical reviews byte-exact. Current native additions are separate directories. Full tracked source/exports unchanged. No release acceptance.'})
print(json.dumps(counts,indent=2))
