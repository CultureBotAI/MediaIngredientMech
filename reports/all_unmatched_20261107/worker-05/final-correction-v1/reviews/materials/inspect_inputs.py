import pathlib,json,hashlib,datetime,subprocess,html.parser
import yaml
O=pathlib.Path(__file__).parent; P=O.parent/'materials';B=pathlib.Path('reports/all_unmatched_20261107/worker-05')
C=pathlib.Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107')
def load(p):return json.loads(pathlib.Path(p).read_text())
def sha(p):return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def resolve(cap):
 if cap['root']=='source':return C/'queue/preliminary-v5'/cap['path']
 if cap['path'].startswith('final-correction-v1/materials/'):return P/cap['path'].removeprefix('final-correction-v1/materials/')
 return B/cap['path']
O.mkdir(exist_ok=True);(O/'read').mkdir(exist_ok=True)
assert sha(P/'MANIFEST.json')=='daa13098947522038b38cdae3d23369caea4a260db240b1f93ef8f6145c3eb0a'
m=load(P/'MANIFEST.json');print('member shape',m['files'][0])
errors=[];bindings=[]
def bind(path,role,expected=None):
 h=sha(path)
 if expected and h!=expected:errors.append({'path':str(path),'expected':expected,'actual':h})
 v={'path':str(path.resolve()),'sha256':h,'role':role};bindings.append(v);return v
for f in m['files']:
 path=P/f['path'];bind(path,'sealed_packet_member',f['sha256'])
records=[]
for i,p in enumerate(load(P/'proposals.json')['proposals']):
 path=resolve(p['after_capture']);bind(path,'whole_successor_payload',p['after_capture']['sha256']);r=yaml.safe_load(path.read_text())
 prior=resolve(p['predecessor_copy']);bind(prior,'whole_predecessor_payload',p['predecessor_copy']['sha256']);old=yaml.safe_load(prior.read_text());before=None
 if p.get('before_capture'):
  bp=resolve(p['before_capture']);bind(bp,'original_before_owner',p['before_sha256']);before=yaml.safe_load(bp.read_text());assert sha(pathlib.Path(p['owner_path']))==p['before_sha256']
 records.append({'proposal':p,'record':r,'predecessor':old,'before':before})
 for n in ['curation_history','occurrence_statistics']:assert r.get(n,[])[:len(old.get(n,[]))]==old.get(n,[]) if isinstance(old.get(n,[]),list) else r.get(n)==old.get(n)
for start in range(0,len(records),5):
 out=''
 for x in records[start:start+5]:out+='\nPROPOSAL '+x['proposal']['proposal_id']+'\n'+json.dumps(x['record'],ensure_ascii=False,indent=1)+'\n'
 (O/'read'/f'payloads-{start:02}.txt').write_text(out)
class Strip(html.parser.HTMLParser):
 def __init__(self):super().__init__();self.out=[];self.skip=0
 def handle_starttag(self,t,a):
  if t in ['script','style']:self.skip+=1
  if t in ['p','li','tr','br']:self.out.append('\n')
 def handle_endtag(self,t):
  if t in ['script','style'] and self.skip:self.skip-=1
 def handle_data(self,d):
  if not self.skip:self.out.append(d)
sources=[]
for i,e in enumerate(load(P/'evidence.json')['evidence']):
 path=resolve(e['capture']);v=bind(path,'evidence_'+e['kind'],e['capture']['sha256']);v['evidence']=e
 if e['kind'] in ['primary_source','ontology','unsuccessful_search']:
  raw=path.read_bytes();out=O/'read'/f'source-{i:03}.txt'
  if raw.startswith(b'%PDF'):
   r=subprocess.run(['pdftotext','-layout',str(path),'-'],text=True,capture_output=True);t=r.stdout;v['extract_returncode']=r.returncode;v['extract_stderr']=r.stderr
  elif b'<html' in raw[:1000].lower() or raw.lstrip().startswith(b'<!DOCTYPE'):
   parser=Strip();parser.feed(raw.decode('utf8',errors='replace'));t=''.join(parser.out)
  else:t=raw.decode('utf8',errors='replace')
  out.write_text(t);v['read_path']=str(out);v['read_sha256']=sha(out)
 sources.append(v)
for n,x in [('whole-records.json',records),('source-index.json',sources),('input-receipt.json',{'started_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reviewer':'Codex GPT-6 /root/media_research','primary_author':'/root/materials_research','manifest_sha256':sha(P/'MANIFEST.json'),'bindings':bindings,'errors':errors})]:
 assert not (O/n).exists();(O/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not errors,errors
print('Verified',len(m['files']),'members;',len(records),'whole payloads;',len(sources),'evidence records; errors',errors)
