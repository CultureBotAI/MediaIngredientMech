"""2026-11-12 independent read-only CAS hold-context qualification. Inputs: GitHub MIM issues 887/753 and all comments. Outputs: exact JSON/stdout/stderr, command/time/hash receipt in this directory. No GitHub or source mutations."""
from pathlib import Path
from datetime import datetime,timezone
import subprocess,json,hashlib
D=Path(__file__).parent
now=lambda:datetime.now(timezone.utc).isoformat().replace('+00:00','Z')
rows=[]
for number in [902]:
 for kind in ['issue','comments']:
  endpoint=f'repos/CultureBotAI/MediaIngredientMech/issues/{number}'+('/comments' if kind=='comments' else '')
  argv=['gh','api',endpoint]+(['--paginate','--slurp'] if kind=='comments' else [])
  started=now()
  cp=subprocess.run(argv,cwd=D,text=True,capture_output=True,timeout=45)
  out=D/f'{number}-{kind}.json';err=D/f'{number}-{kind}.stderr.txt'
  out.write_text(cp.stdout);err.write_text(cp.stderr)
  row={'issue':number,'kind':kind,'started_at':started,'finished_at':now(),'argv':argv,'cwd':str(D),'exit_code':cp.returncode,'stdout_path':str(out),'stdout_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'stderr_path':str(err),'stderr_sha256':hashlib.sha256(err.read_bytes()).hexdigest()}
  rows.append(row);(D/'LIVE-READ-RECEIPT-902.json').write_text(json.dumps(rows,indent=2)+'\n')
  print(json.dumps({'issue':number,'kind':kind,'exit_code':cp.returncode,'bytes':len(cp.stdout.encode())}),flush=True)
  if cp.returncode:print(cp.stderr);raise SystemExit(cp.returncode)
