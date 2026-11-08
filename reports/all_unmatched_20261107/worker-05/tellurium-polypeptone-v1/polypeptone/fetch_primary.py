from pathlib import Path
from datetime import datetime,timezone
import json,subprocess,hashlib,re
S=Path('.temp/w05-tellurium-polypeptone-v1/polypeptone');C=S/'captures';C.mkdir(exist_ok=True)
x=json.loads((S/'input/polypeptone-context-subset.json').read_text());urls={
'wako.pdf':'https://labchem-wako.fujifilm.com/us/catalog/pdf/catalog_0005.pdf',
'wako-japan.html':'https://labchem-wako.fujifilm.com/jp/category/03189.html',
'thermo.pdf':'https://assets.thermofisher.com/TFS-Assets/BPD/brochures/peptones-supplements-feeds-technical-reference-guide.pdf',
'foodon.json':'https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315306',
'mediadive442.json':'https://mediadive.dsmz.de/rest/ingredient/442',
'mediadive2060.json':'https://mediadive.dsmz.de/rest/ingredient/2060'}
for occ in x['japanese_occurrences']:
 if occ['preferred_term'].startswith('Hipoly'):continue
 rec=x['complete_japanese_recipes'][occ['source_path']]['complete_recipe'];txt=json.dumps(rec,ensure_ascii=False)
 for number in re.findall(r'GRMD=(\d+)',txt):urls['jcm'+number+'.html']='https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD='+number
results=[]
for name,url in urls.items():
 p=C/name;assert not p.exists();at=datetime.now(timezone.utc).isoformat();cmd=['curl','-L','--retry','2','--connect-timeout','10','--max-time','45','--silent','--show-error','--output',str(p),'--write-out','%{http_code}',url];r=subprocess.run(cmd,capture_output=True,text=True)
 receipt=dict(url=url,accessed_at=at,completed_at=datetime.now(timezone.utc).isoformat(),command=cmd,exit_code=r.returncode,http_status=r.stdout,stderr=r.stderr,path=name,sha256=hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None,bytes=p.stat().st_size if p.exists() else 0)
 (C/(name+'.receipt.json')).write_text(json.dumps(receipt,indent=2)+'\n');results.append(receipt)
(S/'fetch-receipts.json').write_text(json.dumps(results,indent=2)+'\n');print(json.dumps([dict(path=r['path'],http_status=r['http_status'],exit_code=r['exit_code'],bytes=r['bytes']) for r in results]))
