from pathlib import Path
import json,hashlib,sys,datetime,re
A=Path('.temp/w05-final-correction-v1/chemicals');L=Path(__file__).parent
E={e['evidence_id']:e for e in json.loads((A/'evidence-read-ledger-v1.json').read_text())['entries']}
def clean(x):
 if isinstance(x,dict):return {k:clean(v) for k,v in x.items() if k not in ['properties','roles','gmo','gmo_id','_links','links']}
 if isinstance(x,list):return [clean(v) for v in x]
 return x
for n in sys.argv[1:]:
 p=A/'read-text'/f'{n}.txt'
 if not p.exists():p=Path(E[n]['resolved_path'])
 b=p.read_bytes();s=b.decode(errors='replace')
 if b.startswith(b'%PDF'):
  import subprocess
  out=L/(n+'.txt');subprocess.run(['/opt/homebrew/bin/pdftotext','-layout',str(p),str(out)],check=True);s=out.read_text()
 try:s=json.dumps(clean(json.loads(s)),ensure_ascii=False)
 except ValueError:pass
 print('SOURCE',n,s)
 with (L/'read-log.jsonl').open('a') as f:f.write(json.dumps({'evidence_id':n,'read_path':str(p),'read_sha256':hashlib.sha256(b).hexdigest(),'original_capture':E.get(n,{}).get('capture'),'scope':'Source scientific content or extracted body; duplicate navigation and TOGO enrichment roles/properties are not scientific support.','read_at':datetime.datetime.now(datetime.timezone.utc).isoformat()})+'\n')
