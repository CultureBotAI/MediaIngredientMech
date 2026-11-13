"""2026-11-12 bounded read-only issue deduplication for four named CAS annotations; no writes to GitHub."""
import subprocess,json,hashlib
from pathlib import Path
from datetime import datetime,timezone
D=Path(__file__).parent;outdir=D/'dedup';outdir.mkdir(exist_ok=False);results=[]
queries=['Furaltadone','3759-92-1','Kanamycin','25839-94-0','Methylglyoxal','79-98-8','Oxalic','144-62-1']
for i,query in enumerate(queries,1):
 argv=['gh','search','issues',query,'--repo','CultureBotAI/MediaIngredientMech','--limit','100','--json','number,title,state,url,body']
 start=datetime.now(timezone.utc).isoformat().replace('+00:00','Z');cp=subprocess.run(argv,cwd=D,text=True,capture_output=True,timeout=40)
 p=outdir/f'{i:02d}.json';p.write_text(cp.stdout);(outdir/f'{i:02d}.stderr.txt').write_text(cp.stderr)
 row={'query':query,'started_at':start,'finished_at':datetime.now(timezone.utc).isoformat().replace('+00:00','Z'),'argv':argv,'exit_code':cp.returncode,'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()};results.append(row)
 (D/'DEDUP-RECEIPT.json').write_text(json.dumps(results,indent=2)+'\n')
 print(query,cp.returncode,[(x['number'],x['title'],x['state']) for x in json.loads(cp.stdout)] if cp.returncode==0 else cp.stderr,flush=True)
 if cp.returncode:raise SystemExit(cp.returncode)
