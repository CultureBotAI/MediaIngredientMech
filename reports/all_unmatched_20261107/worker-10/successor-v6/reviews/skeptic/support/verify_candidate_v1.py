"""Independent, read-only S6 candidate verification; writes only this private directory."""
from pathlib import Path
from datetime import datetime, timezone
import copy, hashlib, json, re, subprocess
import yaml

R = Path.cwd()
A = R / 'reports/all_unmatched_20261107/worker-10'
S = A / 'successor-v6'
P = R / '.temp/all-unmatched-worker-10/successor-v6/skeptic'
Q = R.parents[2] / 'preflight/w10-family-residual-triage-v1'
HEAD = '3e190a0f6c5a978ca8ed7e3bc7b6a2d66935548b'
started = datetime.now(timezone.utc).isoformat()
checks = []
def check(label, value):
    checks.append({'check': label, 'pass': bool(value)})
def sha(b):
    return hashlib.sha256(b).hexdigest()
def js(p):
    return json.loads(p.read_text())
def objsha(x):
    return sha(json.dumps(x, sort_keys=True, ensure_ascii=False, separators=(',', ':')).encode())
def capture(p):
    return {'path': str(p.relative_to(R)) if p.is_relative_to(R) else str(p), 'sha256': sha(p.read_bytes())}
def diff(l, r, p=''):
    if type(l) is not type(r): return [{'field':p,'before':l,'after':r}]
    if isinstance(l, dict):
        out=[]
        for k in sorted(l.keys() | r.keys()):
            if k not in l or k not in r: out.append({'field':p+'/'+k,'before':l.get(k),'after':r.get(k)})
            else: out += diff(l[k],r[k],p+'/'+k)
        return out
    if isinstance(l,list):
        if len(l)!=len(r):return [{'field':p,'before':l,'after':r}]
        return [v for i,(x,y) in enumerate(zip(l,r)) for v in diff(x,y,p+'/'+str(i))]
    return [] if l==r else [{'field':p,'before':l,'after':r}]
def history_text(raw):
    match=re.search(r'^curation_history:\n(.*?)(?=^[A-Za-z_]+:|\Z)',raw,re.M|re.S)
    return match.group(1)
def has_historical_marker(x):
    if isinstance(x,dict):
        return x.get('old_completion_reassessment_is_historical') is True or any(has_historical_marker(v) for v in x.values())
    if isinstance(x,list):return any(has_historical_marker(v) for v in x)
    return False
check('source HEAD unchanged',subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()==HEAD)
triage=js(Q/'TRIAGE-v2.json')
for row in js(Q/'MANIFEST.json')['files']:
    p=Q/row['path'];check('triage manifest '+row['path'],sha(p.read_bytes())==row['sha256'] and p.stat().st_size==row['bytes'])
frozen=js(S/'author-freeze.json')
check('author predecessor', frozen['predecessor_head']==HEAD)
def verify_captures(x):
    if isinstance(x,dict):
        if x.get('root')=='artifact' and 'path' in x and 'sha256' in x:
            check('freeze capture '+x['path'],sha((A/x['path']).read_bytes())==x['sha256'])
        for v in x.values():verify_captures(v)
    elif isinstance(x,list):
        for v in x:verify_captures(v)
verify_captures(frozen)
rows=[];sources=[]
for row in triage['rows']:
    pid=row['proposal_id'];before=R/row['repository_path'];after=S/'proposed'/f'{pid}.yaml'
    braw=before.read_bytes();araw=after.read_bytes();b=yaml.safe_load(braw);a=yaml.safe_load(araw)
    gitraw=subprocess.check_output(['git','show',HEAD+':'+row['repository_path']])
    check(pid+' authentic complete predecessor',braw==gitraw and sha(braw)==row['payload_sha256'] and braw==(Q/'blobs'/row['payload_sha256']).read_bytes())
    check(pid+' frozen final payload',sha(araw)==next(x['capture']['sha256'] for x in frozen['payloads'] if x['proposal_id']==pid))
    difco='difco' in pid
    allowed={'completeness','notes'}|({'method'} if difco else set())
    adiffs=diff(b['component_assertion'],a['component_assertion'])
    check(pid+' exact allowed assertion fields',{x['field'][1:] for x in adiffs}==allowed)
    check(pid+' method',a['component_assertion']['method']==('CURATED_INTERPRETATION' if difco else 'LABEL_ENUMERATION'))
    check(pid+' completeness',a['component_assertion']['completeness']==('COMPLETE' if difco else 'UNKNOWN'))
    check(pid+' full original history prefix',a['curation_history'][:-1]==b['curation_history'] and len(a['curation_history'])==len(b['curation_history'])+1)
    check(pid+' raw historical YAML prefix',history_text(araw.decode()).startswith(history_text(braw.decode())))
    h=a['curation_history'][-1]
    check(pid+' truthful agent attribution',h['curator']=='Codex worker10 /root' and h['llm_assisted'] is True and h['previous_status']==b['mapping_status']==h['new_status'])
    check(pid+' correction finding lineage','W09-W10-SKEPTIC-COMPONENT-CLOSURE' in h['changes'] and ('W09-W10-SKEPTIC-DIFCO-COMPONENT-METHOD' in h['changes'])==difco)
    rollback=copy.deepcopy(a);rollback['curation_history']=b['curation_history'];rollback['component_assertion']=b['component_assertion']
    check(pid+' full object rollback',rollback==b)
    check(pid+' exact component objects',a['components']==b['components'])
    check(pid+' exact assertion evidence',a['component_assertion']['evidence']==b['component_assertion']['evidence'])
    if not difco:
        check(pid+' original unknowns and overlap notes retained',a['component_assertion']['notes'].startswith(b['component_assertion']['notes']+' '))
        check(pid+' one ungrounded acid part',len(a['components'])==1 and a['components'][0]['component_name']=='HCl' and a['components'][0]['reference_scope']=='UNMAPPED' and 'component_id' not in a['components'][0])
    else:
        check(pid+' seven nominal immediate names',len(a['components'])==7)
        check(pid+' no quantitative parts',all(set(x)<= {'component_name','reference_scope','component_id'} for x in a['components']))
        check(pid+' nominal lot and quantitative limitations',all(x in a['component_assertion']['notes'] for x in ['nominal','historical JCM1270 lot','performance-adjustment/supplementation','Component quantities and dry-mass ratios are not asserted','Blood and reconstitution water are not dry-base components','partition']))
    rows.append({'proposal_id':pid,'before':capture(before),'after':capture(after),'before_object_sha256':objsha(b),'after_object_sha256':objsha(a),'assertion_changes':adiffs,'appended_history':h,'original_history_count':len(b['curation_history'])})
    for src in row['primary_evidence']:
        p=R/src['repository_path'];check('primary bytes '+src['sha256'],sha(p.read_bytes())==src['sha256'] and p.read_bytes()==(Q/src['snapshot']).read_bytes())
        sources.append({'proposal_id':pid,**src})
old={n:js(A/'successor-v5/final-core'/f'{n}.json')[n] for n in ['decisions','proposals','evidence']}
new={n:js(S/'author-core'/f'{n}.json')[n] for n in old}
check('188 original cases and stable order',[x['case_id'] for x in old['decisions']]==[x['case_id'] for x in new['decisions']] and len(new['decisions'])==188)
check('127 original proposal IDs and stable order',[x['proposal_id'] for x in old['proposals']]==[x['proposal_id'] for x in new['proposals']] and len(new['proposals'])==127)
case_diffs=[];proposal_diffs=[]
for b,a in zip(old['decisions'],new['decisions']):
    i=b['source_index'];check(f'case {i} immutable occurrences',b['occurrence_ids']==a['occurrence_ids'])
    check(f'case {i} source disposition routing',all(b.get(k)==a.get(k) for k in ['source','case_input_sha256','disposition','applicability','proposal_ids','owner_records','source_index']))
    if b==a:continue
    check(f'case {i} target allowlist',i in [65,87,94,102,125,178])
    changes=diff(b,a);allowed={'component_assertion_successor','evidence_ids','independent_review','issue_refs'}|({'reasoning'} if i==178 else set())
    check(f'case {i} only allowed dependency fields',all(x['field'].split('/')[1] in allowed for x in changes))
    check(f'case {i} evidence append',a['evidence_ids']==b['evidence_ids']+['sv6-source-assertion-assessment','sv6-exact-assertion-diffs','sv6-filed-qualified-findings'])
    check(f'case {i} previous review retained',a['component_assertion_successor']['prior_independent_review']==b['independent_review'])
    check(f'case {i} no inherited exact candidate approval',a['independent_review']=={'status':'pending','evidence_ids':[]} and a['component_assertion_successor']['whole_owner_or_export_approval'] is False)
    if i!=178:
        check(f'case {i} historical completion object exact',a['completion_reassessment']==b['completion_reassessment'] and has_historical_marker(b))
        check(f'case {i} current historical distinction','Current completeness is UNKNOWN' in a['component_assertion_successor']['historical_completion_reassessment_preserved'])
    case_diffs.append({'source_index':i,'case_id':a['case_id'],'before_object_sha256':objsha(b),'after_object_sha256':objsha(a),'changes':changes})
check('exact six changed cases',sorted(x['source_index'] for x in case_diffs)==[65,87,94,102,125,178])
for b,a in zip(old['proposals'],new['proposals']):
    pid=b['proposal_id'];check(pid+' source case backlinks',b['case_ids']==a['case_ids'])
    if b==a:
        check(pid+' retained payload bytes',sha((A/a['after_capture']['path']).read_bytes())==a['after_capture']['sha256'])
        continue
    check(pid+' proposal target allowlist',pid in [x['proposal_id'] for x in rows])
    changes=diff(b,a);allowed={'component_assertion_successor','evidence_ids','independent_review','review_status_explanation','after_capture'}|({'description','publication_holds'} if 'difco' not in pid else set())
    check(pid+' exact dependency field allowlist',all(x['field'].split('/')[1] in allowed for x in changes))
    if 'difco' not in pid:
        check(pid+' exact description correction',a['description']==b['description'].replace('partial source-supported components','source-named components with unknown list completeness'))
        check(pid+' exact active hold correction',a['publication_holds']==[x.replace('PARTIAL components','components with UNKNOWN completeness') for x in b['publication_holds']])
    check(pid+' preserved previous review',a['component_assertion_successor']['prior_independent_review']==b['independent_review'])
    check(pid+' no owner approval',a['component_assertion_successor']['whole_owner_or_export_approval'] is False)
    proposal_diffs.append({'proposal_id':pid,'before_object_sha256':objsha(b),'after_object_sha256':objsha(a),'changes':changes})
check('exact five changed proposals',len(proposal_diffs)==5)
check('all old evidence exact ordered prefix',new['evidence'][:len(old['evidence'])]==old['evidence'])
check('exact three new evidence IDs',[x['evidence_id'] for x in new['evidence'][len(old['evidence']):]]==['sv6-source-assertion-assessment','sv6-exact-assertion-diffs','sv6-filed-qualified-findings'])
for x in new['evidence'][len(old['evidence']):]:verify_captures(x)
check('304 unique CM occurrence IDs',len({o for x in new['decisions'] for o in x['occurrence_ids'] if o.startswith('CM_OCC:')})==304)
check('12 retained target CM occurrence IDs',len({o for x in new['decisions'] if x['source_index'] in [65,87,94,102,125,178] for o in x['occurrence_ids'] if o.startswith('CM_OCC:')})==12)
check('source HEAD still unchanged',subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()==HEAD)
out={'reviewer':'OpenAI Codex /root/preparation_skeptic','checks_started_at':started,'checks_finished_at':datetime.now(timezone.utc).isoformat(),'earlier_source_read_start':'Not separately timestamped; these are checker execution times, not total reading duration.','head':HEAD,'checks':checks,'check_count':len(checks),'failures':[x for x in checks if not x['pass']],'payloads':rows,'primary_bindings':sources,'case_diffs':case_diffs,'proposal_diffs':proposal_diffs,'counts':{'selected_payloads':len(new['proposals']),'changed_payloads':5,'retained_payloads':122,'cases':188,'changed_cases':len(case_diffs),'retained_cases':188-len(case_diffs),'old_evidence':len(old['evidence']),'new_evidence':len(new['evidence'])-len(old['evidence'])},'bindings':[capture(S/'author-freeze.json'),capture(S/'source-assessment.json'),capture(S/'payload-change-proof.json')]+[capture(S/'author-core'/f'{n}.json') for n in old]}
dest=P/'candidate-verification-v1.json'
with dest.open('x') as f:json.dump(out,f,ensure_ascii=False,indent=2);f.write('\n')
print(json.dumps({'path':str(dest),'sha256':sha(dest.read_bytes()),'checks':len(checks),'failures':out['failures'],'counts':out['counts']},indent=2))
