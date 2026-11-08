import pathlib,json,hashlib,datetime,subprocess,html.parser,copy
import yaml
O=pathlib.Path('.temp/w05-final-correction-v1/media');O.mkdir(parents=True,exist_ok=True)
C=pathlib.Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107')
B=pathlib.Path('reports/all_unmatched_20261107/worker-05')
def read(p):return json.loads(pathlib.Path(p).read_text())
def sha(p):return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def save(n,v):
 p=O/n;p.parent.mkdir(parents=True,exist_ok=True)
 if p.exists():raise RuntimeError('Output exists: '+str(p))
 p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n')
assignment=read(O.parent/'control/media-assignment.json')
assert subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()==assignment['base_head']
P=read(B/'correction-1193-v1/media/proposals.json')['proposals']
D=read(B/'correction-1193-v1/media/decisions.json')['decisions']
E=read(B/'correction-1193-v1/media/evidence.json')['evidence']
assert set(assignment['case_ids'])=={x['case_id']for x in D}
assert set(assignment['proposal_ids'])=={x['proposal_id']for x in P}
inputs=[];errors=[]
def bind(p,role,expected=None):
 actual=sha(p)
 if expected and actual!=expected:errors.append({'path':str(p),'expected':expected,'actual':actual})
 x={'path':str(pathlib.Path(p).resolve()),'sha256':actual,'role':role};inputs.append(x);return x
for n in ['decisions','proposals','evidence']:bind(B/f'correction-1193-v1/media/{n}.json','predecessor_group_'+n)
for n in ['decisions','proposals','evidence']:bind(B/f'correction-1193-v1/{n}.json','predecessor_canonical_'+n)
for n in ['MAPPING_SEMANTICS.md','src/mediaingredientmech/schema/mediaingredientmech.yaml','.claude/skills/add-media/SKILL.md','.claude/skills/curate-yaml-record/SKILL.md','docs/record-reviews.md','docs/record-review-profile.md']:bind(n,'native_contract')
payloads=[]
for p in P:
 path=B/p['after_capture']['path'];x=bind(path,'selected_predecessor_payload',p['after_capture']['sha256'])
 rec=yaml.safe_load(path.read_text());before=None
 if p.get('before_sha256'):
  bp=pathlib.Path(p['owner_path']);before=bind(bp,'unchanged_maintained_before_owner',p['before_sha256']);before['record']=yaml.safe_load(bp.read_text())
 payloads.append({'proposal':p,'payload_binding':x,'record':rec,'before':before})
for start in range(0,len(payloads),5):
 text=''
 for item in payloads[start:start+5]:
  text+='\n### '+item['proposal']['proposal_id']+'\n'+pathlib.Path(item['payload_binding']['path']).read_text()+'\n'
 (O/f'read/payloads-{start:02d}.txt').parent.mkdir(parents=True,exist_ok=True)
 (O/f'read/payloads-{start:02d}.txt').write_text(text)
class Strip(html.parser.HTMLParser):
 def __init__(self):super().__init__();self.out=[];self.skip=0
 def handle_starttag(self,t,a):
  if t in ['script','style']:self.skip+=1
  if t in ['p','tr','li','h1','h2','h3','br','table']:self.out.append('\n')
 def handle_endtag(self,t):
  if t in ['script','style'] and self.skip:self.skip-=1
  if t in ['td','th']:self.out.append(' | ')
 def handle_data(self,d):
  if not self.skip:self.out.append(d)
captures=[]
for i,e in enumerate(E):
 cap=e['capture'];p=B/cap['path'] if cap['root']=='artifact' else C/'queue/preliminary-v5'/cap['path']
 x=bind(p,'original_'+e['kind'],cap['sha256']);x.update(evidence=e)
 if e['kind'] in ['primary_source','ontology','unsuccessful_search']:
  raw=p.read_bytes();q=O/f'read/capture-{i:03d}.txt'
  if raw.startswith(b'%PDF'):
   proc=subprocess.run(['pdftotext','-layout',str(p),'-'],capture_output=True,text=True);txt=proc.stdout;x['extraction_returncode']=proc.returncode;x['extraction_stderr']=proc.stderr
  elif b'<html' in raw[:1000].lower() or raw.lstrip().startswith((b'<!DOCTYPE',b'<HTML')):
   parser=Strip();parser.feed(raw.decode('utf8',errors='replace'));txt=''.join(parser.out)
  else:txt=raw.decode('utf8',errors='replace')
  q.write_text(txt);x['read_path']=str(q);x['read_sha256']=sha(q);x['extracted_characters']=len(txt)
 captures.append(x)
prov=C/'workers/w02/worktree/.temp/campaign-evidence-provenance-audit-v1/provenance'
typing=read(prov/'native-type-suggestions-v1.json');pr=read(prov/'entry-provenance-ledger-v1.json')
rows=[x for x in typing['rows'] if x['worker']==5 and x['proposal_id'] in assignment['proposal_ids']]
save('typing-audit-suggestions.json',{'source':bind(prov/'native-type-suggestions-v1.json','independent_full_campaign_typing_matrix'),'rows':rows,'provenance_ledger':bind(prov/'entry-provenance-ledger-v1.json','independent_full_campaign_provenance_ledger')})
save('predecessor-payloads.json',payloads);save('predecessor-decisions.json',D);save('capture-index.json',captures)
save('input-manifest.json',{'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scientist':'Codex GPT-6 /root/media_research','assignment':assignment,'inputs':inputs,'hash_errors':errors,'counts':{'cases':len(D),'proposals':len(P),'evidence_entries':len(E),'new_mapping_typing_rows':len(rows)}})
assert not errors,errors
print('Prepared',len(D),'cases,',len(P),'full payloads,',len(E),'capture bindings,',len(rows),'claim-specific typing rows; zero hash errors.')
