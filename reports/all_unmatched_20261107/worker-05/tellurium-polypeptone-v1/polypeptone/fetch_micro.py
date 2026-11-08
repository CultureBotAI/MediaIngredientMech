from pathlib import Path
from datetime import datetime,timezone
import json,subprocess,hashlib
S=Path('.temp/w05-tellurium-polypeptone-v1/polypeptone');C=S/'captures'
urls={'micro-polypeptone.json':'https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000179','micro-polypeptone-parents.json':'https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FMICRO_0000179/parents'}
res=[]
for name,url in urls.items():
 p=C/name;assert not p.exists();at=datetime.now(timezone.utc).isoformat();cmd=['curl','-L','--retry','2','--connect-timeout','10','--max-time','45','--silent','--show-error','--output',str(p),'--write-out','%{http_code}',url];r=subprocess.run(cmd,capture_output=True,text=True);o=dict(url=url,accessed_at=at,completed_at=datetime.now(timezone.utc).isoformat(),command=cmd,exit_code=r.returncode,http_status=r.stdout,stderr=r.stderr,path=name,sha256=hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None,bytes=p.stat().st_size if p.exists() else 0);(C/(name+'.receipt.json')).write_text(json.dumps(o,indent=2)+'\n');res.append(o)
(S/'micro-fetch-receipts.json').write_text(json.dumps(res,indent=2)+'\n')
