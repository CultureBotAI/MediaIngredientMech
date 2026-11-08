from pathlib import Path
from datetime import datetime,timezone
import json,subprocess,hashlib
S=Path('.temp/w05-tellurium-polypeptone-v1/polypeptone');C=S/'captures'
urls={'togoM2.json':'https://togomedium.org/sparqlist/api/medium/M2','togoM90.json':'https://togomedium.org/sparqlist/api/medium/M90','mediadiveJ2.json':'https://mediadive.dsmz.de/rest/medium/J2','mediadiveJ98.json':'https://mediadive.dsmz.de/rest/medium/J98','labology.html':'https://www.labology.co.jp/culture-medium/baiyou-1/','foodon-polypeptone-search.json':'https://www.ebi.ac.uk/ols4/api/search?q=polypeptone&ontology=foodon&exact=true','foodon-peptone-search.json':'https://www.ebi.ac.uk/ols4/api/search?q=peptone&ontology=foodon&exact=true'}
results=[]
for name,url in urls.items():
 p=C/name;assert not p.exists();at=datetime.now(timezone.utc).isoformat();cmd=['curl','-L','--retry','2','--connect-timeout','10','--max-time','45','--silent','--show-error','--output',str(p),'--write-out','%{http_code}',url];r=subprocess.run(cmd,capture_output=True,text=True);o=dict(url=url,accessed_at=at,completed_at=datetime.now(timezone.utc).isoformat(),command=cmd,exit_code=r.returncode,http_status=r.stdout,stderr=r.stderr,path=name,sha256=hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None,bytes=p.stat().st_size if p.exists() else 0);(C/(name+'.receipt.json')).write_text(json.dumps(o,indent=2)+'\n');results.append(o)
(S/'followup-fetch-receipts.json').write_text(json.dumps(results,indent=2)+'\n');print(json.dumps([dict(path=r['path'],http_status=r['http_status'],exit_code=r['exit_code']) for r in results]))
