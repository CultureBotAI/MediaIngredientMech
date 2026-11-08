from pathlib import Path
import subprocess,json,hashlib,datetime
O=Path(__file__).resolve().parent;L=O/'live';L.mkdir()
for n in [1176,710,1211,1245,1204,1168,1193]:
 for kind,endpoint in [('issue',f'issues/{n}'),('comments',f'issues/{n}/comments?per_page=100')]:
  cmd=['gh','api','repos/CultureBotAI/MediaIngredientMech/'+endpoint]+(['--paginate','--slurp']if kind=='comments'else[]);at=datetime.datetime.now(datetime.timezone.utc).isoformat();p=subprocess.run(cmd,capture_output=True);name=f'{kind}-{n}'
  (L/(name+'.json')).write_bytes(p.stdout);(L/(name+'.stderr')).write_bytes(p.stderr);(L/(name+'-receipt.json')).write_text(json.dumps({'command':cmd,'at':at,'exit_code':p.returncode,'stdout_sha256':hashlib.sha256(p.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(p.stderr).hexdigest()},indent=2)+'\n');print(name,p.returncode)
  if p.returncode:raise SystemExit(p.returncode)
