import datetime,hashlib,importlib.util,json,sys,collections
from pathlib import Path
import yaml
R=Path.cwd();A=R/'reports/all_unmatched_20261107/worker-10';S=A/'successor-v2';P=R/'.temp/all-unmatched-worker-10/successor-v2/skeptic';n=R/sys.argv[1];out=P/sys.argv[2];assert not out.exists()
H=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
J=lambda p:json.loads(Path(p).read_text())
CH=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
v=yaml.safe_load(n.read_text());D=J(S/'decisions.json')['decisions'];PL=J(S/'proposals.json')['proposals'];E={x['evidence_id']:x for x in J(S/'evidence.json')['evidence']}; cases=J(R.parents[2]/'queue/preliminary-v5/shards/shard-10.json')['cases']; ds={x['case_id']:x for x in D};ps={x['proposal_id']:x for x in PL};ts={x['target_id']:x for x in v['targets']};es={x['evidence_id']:x for x in v['evidence']};checks=[]
def ck(name,ok,detail=None):checks.append({'check':name,'pass':bool(ok),'detail':detail})
ck('316unique native targets',len(ts)==len(v['targets'])==316)
ck('complete188case and128payloadtarget IDs',set(ts)==set(ds)|{'PROPOSAL:'+x for x in ps})
for i,c in enumerate(cases):
 t=ts[c['case_id']];path=R/t['path']; content=J(path)
 ck('exact native source selector '+str(i),t['selector']=='$.cases['+str(i)+']' and content['cases'][i]==c and CH(content['cases'][i])==ds[c['case_id']]['case_input_sha256'])
for pid,p in ps.items():
 t=ts['PROPOSAL:'+pid]
 ck('exact native payload target '+pid,(R/t['path']).resolve()==(A/p['after_capture']['path']).resolve() and H(R/t['path'])==p['after_capture']['sha256'])
 if p['kind']=='new_owner':ck('new-owner note does not claim preimage '+pid,'Authentic owner' not in t['ownership_note'] and p['before_sha256'] is None)
 else:ck('authentic existing-owner note '+pid,p['owner_path'] in t['ownership_note'] and p['before_sha256'] in t['ownership_note'])
for x in v['source']['inputs']:ck('native current input hash '+x['path'],H(R/x['path'])==x['sha256'])
ck('native evidence includes core1160 unique',len(es)==len(v['evidence']) and set(E)<=set(es))
for eid,e in E.items():
 x=es[eid];ck('native evidence capture hash '+eid,x['snapshot_sha256']==e['capture']['sha256'])
 if e.get('accessed_at'):
  a=datetime.datetime.fromisoformat(e['accessed_at'].replace('Z','+00:00').replace(' UTC','+00:00'));b=datetime.datetime.fromisoformat(x['accessed_at'].replace('Z','+00:00'))
  ck('native original capture time '+eid,a==b)
 else:ck('native local-access disclaimer '+eid,'timestamp denotes local wrapper inspection; no new primary retrieval claimed.' in x['locator'])
counts=collections.Counter((x['area'],x['topic']) for x in v['assessments']); base_assessments=[x for x in v['assessments'] if x['assessment_id']!='native-new-owner-note-correction']; assessed=[z for x in base_assessments for z in x['target_ids']]
ck('316base one-to-one assessments plus one explicit metadata assessment',len(v['assessments'])==317 and len(base_assessments)==316 and collections.Counter(assessed)==collections.Counter(ts))
ck('2freshidentity cases',sum(x['area']=='identity' for x in v['assessments'])==2)
ck('3freshrepresentationpayloads',sum(x['area']=='representation' for x in v['assessments'])==3)
ck('311base preservationassessments',sum(x['area']=='provenance' for x in base_assessments)==311)
extra=next(x for x in v['assessments'] if x['assessment_id']=='native-new-owner-note-correction')
ck('83newowner metadata correction targets exact',set(extra['target_ids'])=={'PROPOSAL:'+pid for pid,p in ps.items() if p['kind']=='new_owner'} and extra['area']=='provenance' and 'No ingredient field, proposal core, source decision, or review scope changed.' in extra['summary'])
for a in v['assessments']:
 ck('native assessment references '+a['assessment_id'],set(a['target_ids'])<=set(ts) and set(a['evidence_ids'])<=set(es))
 if a['area']=='provenance' and a['assessment_id']!='native-new-owner-note-correction':ck('retained science not newly claimed '+a['assessment_id'],'no renewed primary science' in a['summary'] or 'prior science is not reauthored or promoted' in a['summary'])
ck('nonapproval native review verdict',v['completion']=='completed' and v['verdict']=='needs_curation' and v['reviewer']['independence']=='self_review')
ck('one retained open nested overlap',len(v['findings'])==1 and v['findings'][0]['status']=='open' and v['findings'][0]['issue_key']=='w10-jcm58-nbrc268-trace-stock-integration')
ck('failed ontology attempts only context',es['sv2-isp4-ontology-attempts']['kind']=='search' and es['sv2-isp4-ontology-attempts']['support']=='context_only')
sp=importlib.util.spec_from_file_location('native_review_checker',R/'scripts/record_review.py');m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
try:m.validate_review(v);validation='PASS'
except Exception as e:validation=repr(e)
ck('native schema/reference validation',validation=='PASS',validation)
try:m.assert_current_source(R,v);current='PASS'
except Exception as e:current=repr(e)
ck('native current-source verification',current=='PASS',current)
ck('Markdown exact native render',m.render_markdown(v)==n.with_suffix('.md').read_text())
receipt={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'native_path':str(n.relative_to(R)),'native_sha256':H(n),'markdown_sha256':H(n.with_suffix('.md')),'script_sha256':H(Path(__file__)),'core_hashes':{k:H(S/(k+'.json')) for k in ['decisions','proposals','evidence']},'counts':{'targets':len(ts),'assessments':len(v['assessments']),'inputs':len(v['source']['inputs']),'evidence':len(es),'findings':len(v['findings']),'native_checks':len(v['checks'])},'assessment_classes':[{'area':k[0],'topic':k[1],'count':c} for k,c in counts.items()],'checks':checks,'failures':[x for x in checks if not x['pass']]}
out.write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps({'sha256':H(out),'checks':len(checks),'failures':receipt['failures'],'counts':receipt['counts']}))
