from pathlib import Path
import json,yaml,hashlib,subprocess,datetime
O=Path(__file__).parent;B=Path('reports/all_unmatched_20261107/worker-05');P=B/'final-correction-v1';Q=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(n,x):(O/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
p=next(x for x in json.loads((P/'core/proposals.json').read_text())['proposals'] if x['proposal_id']=='M1193-P-MARINE2216');ds=[d for d in json.loads((P/'core/decisions.json').read_text())['decisions'] if d['case_id'] in p['case_ids']];ids=set(p['evidence_ids'])|{e for d in ds for e in d['evidence_ids']};es=[e for e in json.loads((P/'core/evidence.json').read_text())['evidence'] if e['evidence_id'] in ids];assert len(es)==len(ids)
save('input/selected-proposal.json',p);save('input/selected-decisions.json',ds);save('input/selected-evidence.json',es)
source=B/p['after_capture']['path'];assert sha(source)==p['after_capture']['sha256'];(O/'input/Marine_Broth_2216.yaml').write_bytes(source.read_bytes())
ledger=[]
for i,e in enumerate(es):
 c=e['capture'];f=(B if c['root']=='artifact' else Q)/c['path'];assert sha(f)==c['sha256'],(e['evidence_id'],f);raw=f.read_bytes();entry={'evidence':e,'resolved_path':str(f.resolve()),'sha256':sha(f),'local_read_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 if raw.startswith(b'%PDF'):
  dest=O/'input'/f'evidence-{i:02d}.txt';subprocess.run(['pdftotext','-layout',str(f),str(dest)],check=True);entry['read_text']=str(dest.relative_to(O))
 elif e['evidence_id'].startswith(('MEDIA-RECIPE','MEDIA-MARINE','M1193-OWNER')):
  dest=O/'input'/f'evidence-{i:02d}.txt';dest.write_bytes(raw);entry['read_text']=str(dest.relative_to(O))
 elif e['kind']=='primary_source':
  dest=O/'input'/f'evidence-{i:02d}.txt';dest.write_bytes(raw);entry['read_text']=str(dest.relative_to(O))
 ledger.append(entry)
save('input/source-read-ledger.json',ledger)
shard=json.loads((Q/'shards/shard-05.json').read_text());cases=shard['cases'];selected=[x for x in cases if x['case_id'] in p['case_ids']];assert len(selected)==2
save('input/full-frozen-cases.json',selected)
print('Linked evidence',len(es));print(json.dumps(selected,indent=2,ensure_ascii=False))
for x in ledger:
 if x.get('read_text') and x['evidence']['evidence_id'] not in ['M1193-WEB-web-next-3-17','MEDIA-P084','M1193-OWNER-Marine_Broth_2216','MEDIA-MARINE-COMPARISON-0']:
  text=(O/x['read_text']).read_text();print('\n===',x['evidence']['evidence_id']);print(text[:22000])
