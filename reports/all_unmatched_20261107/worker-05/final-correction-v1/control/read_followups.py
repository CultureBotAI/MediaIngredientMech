from pathlib import Path
import datetime,hashlib,json,subprocess
out=Path('.temp/w05-final-correction-v1/issues/final-followups-v1')
out.mkdir(exist_ok=False)
receipts=[]
for number in [1236,1237,1238,1226]:
 for suffix in ['', '/comments']:
  endpoint=f'repos/CultureBotAI/MediaIngredientMech/issues/{number}{suffix}'
  cmd=['gh','api',endpoint]+(['--paginate','--slurp'] if suffix else [])
  at=datetime.datetime.now(datetime.timezone.utc).isoformat()
  result=subprocess.run(cmd,capture_output=True)
  name=f'{number}'+('-comments' if suffix else '-issue')
  (out/(name+'.json')).write_bytes(result.stdout)
  (out/(name+'.stderr')).write_bytes(result.stderr)
  receipts.append(dict(endpoint=endpoint,accessed_at=at,exit_code=result.returncode,
    path=name+'.json',sha256=hashlib.sha256(result.stdout).hexdigest()))
  print(number,suffix or 'body',result.returncode)
(out/'receipt.json').write_text(json.dumps(receipts,indent=2)+'\n')
