import hashlib,json,pathlib,subprocess,datetime,yaml
W=pathlib.Path.cwd(); O=W/'.temp/nine-scope-candidates-independent-v1/skeptical'; C=W.parents[2]; P=C/'integration/final-same-target-reconciliation-v2'; I=C/'preflight/final-intake-candidate-v1'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rec(p):return {'path':str(p),'sha256':sha(p),'size':p.stat().st_size}
afile=C/'assignments/w01-nine-scope-candidates-independent-v1.json';a=json.loads(afile.read_text());h=json.loads((P/'HANDOFF.json').read_text());m=json.loads((P/'MANIFEST.json').read_text())
checks=[]
def chk(n,b,detail=None):checks.append({'check':n,'pass':bool(b),'detail':detail})
chk('assignment pinned',sha(afile)=='dbde61cc31a77eb32c1ee7dcc344ed885c462ac99f5cbb233b54f69c3735d033')
chk('summary pinned',sha(P/h['active_summary']['path'])==a['summary_sha256']==h['active_summary']['sha256'])
chk('handoff pinned',sha(P/'HANDOFF.json')=='fb4cb8972c815667e925b056cdb7797d1635b291a9fb3ba936061bdcfa3dac96')
chk('manifest pinned',sha(P/'MANIFEST.json')==h['manifest']['sha256']=='6c89863e292bf1b4333be602bf4a355c0219766456d16e1f574bb5412d956df9')
for p,x in m['files'].items():chk('manifest '+p,sha(P/p)==x['sha256'] and (P/p).stat().st_size==x['size'])
files={str(p.relative_to(P)) for p in P.rglob('*') if p.is_file()};excluded=set(m['excluded_runtime_cache_files'])|{'MANIFEST.json','HANDOFF.json'}
chk('ignored-inclusive packet inventory',files==set(m['files'])|excluded,sorted(files-(set(m['files'])|excluded)))
hc={c['candidate_id']:c for c in h['nine_changed_scientific_candidates']}; candidates=[];ev={};origins={}
for c in a['candidates']:
 cid=c['candidate_id'];p=P/c['candidate']['path'];d=yaml.safe_load(p.read_text());chk(cid+' assigned payload',sha(p)==c['candidate']['sha256']);chk(cid+' handoff candidate',c['candidate']==hc[cid]['candidate'])
 t=P/hc[cid]['trace']['path'];chk(cid+' trace hash',sha(t)==hc[cid]['trace']['sha256']);td=json.loads(t.read_text());chk(cid+' trace assignment',td==c)
 result={'candidate_id':cid,'candidate':rec(p),'trace':rec(t),'operation':c['operation'],'owner_path':c['owner_path'],'cases':c['case_ids'],'occurrences':c['occurrence_ids'],'origin_entries':[]}
 if c['before_capture']:
  b=P/c['before_capture'];before=yaml.safe_load(b.read_text());raw=subprocess.check_output(['git','show','e000d66dd26ab053e9b17ce7bf8d3c873c3dde99:'+c['source_before_path']],cwd=W)
  chk(cid+' authentic before',sha(b)==c['before_sha256']==hashlib.sha256(raw).hexdigest())
  chk(cid+' authentic history prefix',d.get('curation_history',[])[:len(before.get('curation_history',[]))]==before.get('curation_history',[]))
  before_pairs={(s['synonym_text'],s.get('source')) for s in before.get('synonyms',[])};after_pairs={(s['synonym_text'],s.get('source')) for s in d.get('synonyms',[])}
  chk(cid+' original raw source labels preserved',before_pairs<=after_pairs,sorted(before_pairs-after_pairs));result['before']=rec(b)
 else:chk(cid+' new record no fake before',c['operation']=='new' and c['source_before_path'] is None)
 for origin in c['origins']:
  op=I/origin['payload_path'];origins[str(op)]=rec(op);chk(cid+' origin payload '+origin['entry_id'],sha(op)==origin['payload_sha256']);result['origin_entries'].append(origin['entry_id']);od=yaml.safe_load(op.read_text())
  oh=od.get('curation_history',[]);ah=d.get('curation_history',[])
  if c['operation']!='new':chk(cid+' all origin events retained '+origin['entry_id'],all(event in ah for event in oh))
  for e in origin.get('evidence',[]):
   ep=e.get('guarded_capture_path');expect=e.get('capture',{}).get('sha256')
   if ep and expect:
    pp=pathlib.Path(ep);ev[ep]={'path':ep,'expected_sha256':expect,'actual_sha256':sha(pp),'pass':sha(pp)==expect}
 candidates.append(result)
chk('all bound capture hashes',all(x['pass'] for x in ev.values()),{'unique':len(ev)})
for dep in [c for c in a['candidates'] if c['candidate_id'].startswith('DEP-')]:
 d=yaml.safe_load((P/dep['candidate']['path']).read_text());b=yaml.safe_load((P/dep['before_capture']).read_text());r=[x for x in d['components'] if 'rumen' in x['component_name'].lower()];chk(dep['candidate_id']+' plain rumen only',len(r)==1 and r[0]['component_name']=='rumen fluid' and r[0]['reference_scope']=='UNMAPPED' and 'component_id' not in r[0]);chk(dep['candidate_id']+' other parts unchanged',[x for x in b['components'] if 'rumen' not in x['component_name'].lower()]==[x for x in d['components'] if 'rumen' not in x['component_name'].lower()])
report={'reviewer':'/root/skeptical_review','author':'/root/next23_context','independent':True,'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'command':'PYTHONDONTWRITEBYTECODE=1 .temp/all-unmatched-worker-01/shard-venv/bin/python3.13 .temp/nine-scope-candidates-independent-v1/skeptical/verify_inputs_v4.py','script':rec(pathlib.Path(__file__)),'inputs':[rec(afile),rec(P/'HANDOFF.json'),rec(P/'MANIFEST.json')],'candidate_count':len(candidates),'case_union_count':len(set(x for c in candidates for x in c['cases'])),'occurrence_union_count':len(set(x for c in candidates for x in c['occurrences'])),'manifest_member_count':len(m['files']),'origin_payload_count':len(origins),'capture_count':len(ev),'candidates':candidates,'origins':list(origins.values()),'capture_checks':list(ev.values()),'checks':checks,'all_pass':all(x['pass'] for x in checks),'limitations':['Byte/history/source-binding checks do not establish scientific support.','No maintained outputs or Git state changed.','No native structured saver invoked: explicit task restricts all new output to private skeptical directory.','First exploratory listing stopped on missing evidence key of dependency origin; corrected optional evidence handling in this script.']}
p=O/'input-seal-lineage-check-v4.json';p.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'path':str(p),'sha256':sha(p),'checks':len(checks),'failed':[x for x in checks if not x['pass']],'counts':{k:report[k] for k in ['candidate_count','case_union_count','occurrence_union_count','manifest_member_count','origin_payload_count','capture_count']}}))
