from pathlib import Path
from datetime import datetime,timezone
import subprocess,json,hashlib,urllib.parse
R=Path.cwd();O=R/'reports/all_unmatched_20261107/worker-10/successor-v2/inputs';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();rows=[]
for n in [1201,1188]:
 args=['gh','api',f'repos/CultureBotAI/MediaIngredientMech/issues/{n}'];a=subprocess.run(args,capture_output=True,text=True);bargs=['gh','api','--paginate','--slurp',f'repos/CultureBotAI/MediaIngredientMech/issues/{n}/comments'];b=subprocess.run(bargs,capture_output=True,text=True)
 assert a.returncode==b.returncode==0,(a.stderr,b.stderr)
 d={'at':datetime.now(timezone.utc).isoformat(),'issue':json.loads(a.stdout),'comments_pages':json.loads(b.stdout),'commands':[args,bargs],'exit_codes':[a.returncode,b.returncode]};p=O/f'issue{n}-live.json'
 with p.open('x') as f:json.dump(d,f,indent=2);f.write('\n')
 rows.append({'path':str(p.relative_to(R)),'sha256':sha(p)})
 if n==1201:
  exact=(O/'coordinator-issue1201-comment.md').read_text().strip();matches=[c for page in d['comments_pages'] for c in page if c['body'].strip()==exact];assert len(matches)==1,'Exact coordinator body not found live'
  rows.append({'coordinator_comment_url':matches[0]['html_url'],'body_sha256':hashlib.sha256(matches[0]['body'].encode()).hexdigest(),'exact_local_body_matches_live':True})
br=subprocess.check_output(['git','branch','--show-current'],text=True).strip();args=['gh','api','repos/CultureBotAI/MediaIngredientMech/branches/'+urllib.parse.quote(br,safe='')];p=subprocess.run(args,capture_output=True,text=True);assert p.returncode==0;d=json.loads(p.stdout);assert d['commit']['sha']=='468766d941e35a74eb2de3c95096660987277d9b';rows.append({'remote_branch':br,'remote_head':d['commit']['sha'],'command':args,'exit_code':p.returncode,'at':datetime.now(timezone.utc).isoformat()})
with (O/'live-read-receipt.json').open('x') as f:json.dump(rows,f,indent=2);f.write('\n')
print(json.dumps(rows[-2:],indent=2))
