import json,pathlib,hashlib,datetime,collections,subprocess
R=pathlib.Path('reports/all_unmatched_20261107/worker-02');B=R/'b';SRC=pathlib.Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
sha=lambda b:hashlib.sha256(b).hexdigest();canon=lambda x:sha(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode())
CS=json.loads(pathlib.Path('.temp/all-unmatched-worker-02/cases-b.json').read_text());D=json.loads((B/'decisions.json').read_text())['decisions'];E=json.loads((B/'evidence.json').read_text())['evidence'];P=json.loads((B/'proposals.json').read_text())['proposals'];EI={e['evidence_id']:e for e in E};PI={p['proposal_id']:p for p in P};errors=[]
for c,d in zip(CS,D):
 assert c['case_id']==d['case_id'] and canon(c)==d['case_input_sha256'];assert d['occurrence_ids']==[o['occurrence_id'] for o in c['occurrences']]
 for o in c['occurrences']:assert sha((SRC/o['full_recipe_snapshot']).read_bytes())==o['source_file_sha256']
 for eid in d['evidence_ids']:assert eid in EI
 for pid in d['proposal_ids']:assert pid in PI
for e in E:
 cp=e['capture'];p=(R if cp['root']=='artifact' else SRC)/cp['path'];assert sha(p.read_bytes())==cp['sha256'],e['evidence_id']
for p in P:
 assert sha((R/p['after_capture']['path']).read_bytes())==p['after_capture']['sha256']
 if p.get('before_sha256'):assert sha(subprocess.check_output(['git','show','e000d66:'+p['owner_path']]))==p['before_sha256']
 for eid in p['evidence_ids']:assert eid in EI
 assert all(c in {d['case_id'] for d in D} for c in p['case_ids'])
report={'status':'PASS','checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'decisions':len(D),'occurrences':sum(len(c['occurrences']) for c in CS),'evidence':len(E),'active_proposals':len(P),'dispositions':dict(collections.Counter(d['disposition'] for d in D)),'checks':['Each decision exact canonical frozen case SHA','Every original occurrence ID preserved in order','Every complete frozen recipe snapshot raw SHA','Every linked evidence/proposal ID resolves','Every evidence capture raw SHA','Every active proposed owner after SHA','Each existing-owner before SHA compared with git e000d66 baseline'],'errors':errors,'inputs':{n:sha((B/n).read_bytes()) for n in ['decisions.json','evidence.json','proposals.json']}}
(B/'final-integrity.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
