from pathlib import Path
from datetime import datetime,timezone
import json,subprocess,hashlib,concurrent.futures
O=Path(__file__).resolve().parent/'new-captures-v2';O.mkdir(exist_ok=True)
targets={
 'riboflavin-dsmz1157':'https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1157.pdf',
 'riboflavin-nbrc1604':'https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1604',
 'hepes-dsmz975':'https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium975.pdf',
 'ki-dsmz792b':'https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium792b.pdf',
 'ferric-citrate-jcm1145':'https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1145',
 'nicotinate-chebi32544':'https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32544',
 'cas13465-05-9-pubchem':'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/13465-05-9/property/MolecularFormula,InChI/JSON',
 'mg-togo1597':'https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1597'
}
def fetch(item):
 n,u=item;p=O/(n+'.body');assert not p.exists();at=datetime.now(timezone.utc).isoformat()
 r=subprocess.run(['curl','--location','--retry','2','--connect-timeout','15','--max-time','50','--silent','--show-error','--dump-header',str(O/(n+'.headers')),'--output',str(p),'--write-out','%{http_code}',u],capture_output=True,text=True)
 (O/(n+'.stderr')).write_text(r.stderr)
 return {'evidence_id':'FINAL-CHEM-'+n,'url':u,'accessed_at':at,'exit_code':r.returncode,'http_status':r.stdout,'capture':{'root':'artifact','path':'final-correction-v1/chemicals/new-captures-v2/'+p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None}}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex: rows=list(ex.map(fetch,targets.items()))
(O/'retrievals.json').write_text(json.dumps(rows,indent=2)+'\n')
print(json.dumps(rows,indent=2))
