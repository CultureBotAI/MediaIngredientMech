from pathlib import Path
from datetime import datetime,timezone
import json,subprocess,hashlib,concurrent.futures
O=Path(__file__).resolve().parent/'new-captures-v3';O.mkdir(exist_ok=True)
targets={
'mg-nbrc406':'https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=406',
'ferric-togo565':'https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M565',
'ferric-dsmz1145':'https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1145.pdf'
}

def fetch(item):
 n,u=item;p=O/(n+'.body');assert not p.exists();at=datetime.now(timezone.utc).isoformat()
 r=subprocess.run(['curl','--location','--retry','2','--connect-timeout','15','--max-time','50','--silent','--show-error','--dump-header',str(O/(n+'.headers')),'--output',str(p),'--write-out','%{http_code}',u],capture_output=True,text=True)
 (O/(n+'.stderr')).write_text(r.stderr)
 return {'evidence_id':'FINAL-CHEM-'+n,'url':u,'accessed_at':at,'exit_code':r.returncode,'http_status':r.stdout,'capture':{'root':'artifact','path':'final-correction-v1/chemicals/new-captures-v3/'+p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None}}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex: rows=list(ex.map(fetch,targets.items()))
(O/'retrievals.json').write_text(json.dumps(rows,indent=2)+'\n')
print(json.dumps(rows,indent=2))
