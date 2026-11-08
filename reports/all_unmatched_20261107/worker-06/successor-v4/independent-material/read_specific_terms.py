from pathlib import Path
import datetime,hashlib,json,subprocess,urllib.parse
O=Path(__file__).resolve().parent;D=O/'live-specific-terms';D.mkdir(exist_ok=False)
queries=[('ols-ncit-C84042','https://www.ebi.ac.uk/ols4/api/ontologies/ncit/terms?obo_id=NCIT%3AC84042'),('nci-evs-C84042','https://api-evsrest.nci.nih.gov/api/v1/concept/ncit/C84042?include=full'),('ols-dron-apple','https://www.ebi.ac.uk/ols4/api/ontologies/dron/terms?obo_id=DRON%3A00020291')]
receipts=[]
for name,url in queries:
 p=D/(name+'.body');h=D/(name+'.headers');at=datetime.datetime.now(datetime.timezone.utc).isoformat();cmd=['curl','--fail','--location','--retry','2','--connect-timeout','15','--max-time','45','--silent','--show-error','--dump-header',str(h),'--output',str(p),url]
 r=subprocess.run(cmd,capture_output=True,text=True);(D/(name+'.stderr')).write_text(r.stderr)
 receipts.append({'name':name,'url':url,'accessed_at':at,'command':cmd,'exit_code':r.returncode,'body_path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()if p.exists()else None})
with (D/'receipts.json').open('x')as f:json.dump(receipts,f,indent=2);f.write('\n')
print(json.dumps(receipts,indent=2))
