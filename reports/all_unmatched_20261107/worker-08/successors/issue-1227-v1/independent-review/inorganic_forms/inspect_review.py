from pathlib import Path
import datetime,hashlib,json,re,subprocess,sys
from html import unescape
R=Path('reports/all_unmatched_20261107/worker-08');M=R/'successors/issue-1227-v1/research/inorganic_forms';O=R/'successors/issue-1227-v1/independent-review/inorganic_forms'
P=json.loads((M/'proposals.json').read_text());D=json.loads((M/'decisions.json').read_text())
def log(p,scope):
 with (O/'read-log.jsonl').open('a') as f:f.write(json.dumps(dict(at=datetime.datetime.now(datetime.timezone.utc).isoformat(),path=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),scope=scope))+'\n')
if sys.argv[1]=='payload':
 for i in map(int,sys.argv[2:]):
  p=P[i];f=R/p['after_capture']['path'];assert hashlib.sha256(f.read_bytes()).hexdigest()==p['after_capture']['sha256'];print('\nPAYLOAD',i,p['proposal_id']);print(f.read_text());log(f,'Entire final selected payload')
elif sys.argv[1]=='before':
 for i in map(int,sys.argv[2:]):
  p=P[i]
  if p['before_sha256']:
   f=Path(p['owner_path']);assert hashlib.sha256(f.read_bytes()).hexdigest()==p['before_sha256'];print('\nBEFORE',i,p['proposal_id']);print(f.read_text());log(f,'Entire original maintained beforeimage')
elif sys.argv[1]=='cases':
 lo,hi=map(int,sys.argv[2:]);
 for i,d in list(enumerate(D))[lo:hi]:print('\nCASE',i,d['case_id'],d['source'],'\n',d['reasoning'],'\nAPPLICABILITY',d['applicability'],'\nMISSING',d['missing_requirement'],'\nNOCHANGE',d['no_change_reason'],'\nPROPOSALS',d['proposal_ids'])
 log(M/'decisions.json',f'Individual final outcomes [{lo}:{hi}]')
elif sys.argv[1]=='source':
 es=json.loads((R/'successors/issue-1201-v1/evidence.json').read_text())['evidence'];extra=json.loads((M/'evidence-additions.json').read_text());es+=extra if isinstance(extra,list) else extra['evidence'];E={e['evidence_id']:e for e in es}
 for k in sys.argv[2:]:
  e=E[k];f=R/e['capture']['path'];b=f.read_bytes();assert hashlib.sha256(b).hexdigest()==e['capture']['sha256']
  if b.startswith(b'%PDF'):t=subprocess.run(['pdftotext','-layout',str(f),'-'],text=True,capture_output=True,check=True).stdout
  else:
   t=b.decode();t=re.sub(r'<script\b[^>]*>.*?</script>|<style\b[^>]*>.*?</style>','',t,flags=re.S|re.I);t=unescape(re.sub('<[^>]+>',' ',t));t=re.sub(r'\s+',' ',t)
  print('\nSOURCE',k,e.get('url'),'\n',t);log(f,'Actual captured body read; PDF text where applicable, derivative semantics preserved')
