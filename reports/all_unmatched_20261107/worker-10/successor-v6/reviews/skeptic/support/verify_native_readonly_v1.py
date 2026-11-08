from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,yaml
from mediaingredientmech.validation.write_validated import validate_ingredient
R=Path.cwd();A=R/'reports/all_unmatched_20261107/worker-10';S=A/'successor-v6';P=R/'.temp/all-unmatched-worker-10/successor-v6/skeptic'
rows=[]
for x in json.loads((S/'author-freeze.json').read_text())['payloads']:
 p=A/x['capture']['path'];errors=validate_ingredient(yaml.safe_load(p.read_text()))
 rows.append({'proposal_id':x['proposal_id'],'path':str(p.relative_to(R)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'errors':[str(e) for e in errors]})
out={'at':datetime.now(timezone.utc).isoformat(),'reviewer':'OpenAI Codex /root/preparation_skeptic','scope':'Independent in-memory closed-schema validation of the five complete final YAML records; no writer, overlay, export, provider or network invoked.','status':'PASS' if all(not x['errors'] for x in rows) else 'FAIL','rows':rows}
p=P/'native-readonly-verification-v1.json'
with p.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps(out,indent=2))
