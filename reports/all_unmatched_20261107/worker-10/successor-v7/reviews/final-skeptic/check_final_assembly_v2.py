"""Read-only final S7 metadata/native closure audit; writes only beside this script."""
from pathlib import Path
from datetime import datetime, timezone
import copy, hashlib, importlib.util, json, subprocess, time

R = Path.cwd()
O = Path(__file__).resolve().parent
A = R / 'reports/all_unmatched_20261107/worker-10'
S = A / 'successor-v7'
C = R.parents[2] / 'queue/preliminary-v5'
start = datetime.now(timezone.utc).isoformat()
clock = time.monotonic()
checks, inputs, commands, diffs = [], {}, [], {}

def sha(b): return hashlib.sha256(b).hexdigest()
def raw(p):
    p = Path(p); b = p.read_bytes(); inputs[str(p)] = sha(b); return b
def read(p): return json.loads(raw(p))
def canon(x): return sha(json.dumps(x, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode())
def ck(label, value):
    checks.append({'check': label, 'passed': bool(value)})
    if not value: raise AssertionError(label)
def cap(ref):
    p = {'artifact': A, 'source': C}.get(ref.get('root'), R) / ref['path']
    ck('capture ' + str(p), sha(raw(p)) == ref['sha256'])
    return p
def delta(a,b,path=''):
    if type(a) is not type(b): return [(path,a,b)]
    if isinstance(a,dict):
        out=[]
        for k in sorted(set(a)|set(b)):
            p=path+'.'+k if path else k
            out.extend([(p,a.get(k),b.get(k))] if k not in a or k not in b else delta(a[k],b[k],p))
        return out
    if isinstance(a,list):
        if len(a)!=len(b): return [] if a==b else [(path,a,b)]
        return [v for i,(x,y) in enumerate(zip(a,b)) for v in delta(x,y,f'{path}[{i}]')]
    return [] if a==b else [(path,a,b)]
def cmd(args):
    r=subprocess.run(args,cwd=R,capture_output=True)
    commands.append({'argv':args,'exit_code':r.returncode,'stdout':r.stdout.decode(),'stderr':r.stderr.decode()})
    ck('command exit '+str(args),r.returncode==0)
    return r.stdout.decode().strip()

BASE=read(O.parent/'technical/baseline-v1.json')
ck('frozen independent baseline',sha(raw(O.parent/'technical/baseline-v1.json'))=='d9a7fdba82cda06cd8a376421ee5a5139659b6b218727c39bc001960831a2fec')
sel=read(S/'selection.json')
ck('selector sealed exact',sha(raw(S/'selection.json'))=='cb5c0eef5787728757aa0d7e2d2e56adc3a634af95d83b7ff23b81bacf11b38e')
f3=read(S/'author-freeze-v3.json')
final={k:read(cap(v)) for k,v in sel['authoritative_core'].items()}
author={k:read(cap(v)) for k,v in f3['core'].items()}
old={k:v['object'] for k,v in BASE['selected_core'].items()}
D,P,E=final['decisions.json']['decisions'],final['proposals.json']['proposals'],final['evidence.json']['evidence']
AD,AP,AE=author['decisions.json']['decisions'],author['proposals.json']['proposals'],author['evidence.json']['evidence']
OD,OP,OE=old['decisions.json']['decisions'],old['proposals.json']['proposals'],old['evidence.json']['evidence']
ck('188 cases 128 proposals 1229 evidence 304 CM occurrences',(len(D),len(P),len(E),sum(len(d['occurrence_ids']) for d in D))==(188,128,1229,304))
ck('all author evidence exact prefix',E[:1224]==AE and len(AE)==1224)
ck('all c66 evidence exact prefix',E[:1218]==OE and len(OE)==1218)
ck('unique full case/proposal/evidence IDs',len({d['case_id'] for d in D})==188 and len({p['proposal_id'] for p in P})==128 and len({e['evidence_id'] for e in E})==1229)
for e in E: cap(e['capture'])
new_eids=[e['evidence_id'] for e in E[1224:]]
ck('five exact final evidence IDs',new_eids==['sv7-independent-science','sv7-independent-lineage','sv7-independent-technical','sv7-reviewed-source-routing','sv7-reviewed-external-origin-bindings'])
case_indices=[80,118,135,178]
caseids=[D[i]['case_id'] for i in case_indices]
for j,e in enumerate(E[1224:]):
    ck('new evidence bounded case set '+e['evidence_id'],e['case_ids']==(caseids if j<3 else [D[i]['case_id'] for i in [118,178]]))
    ck('new evidence kind '+e['evidence_id'],e['kind']==('independent_review' if j<3 else 'local_validation'))
eidset={e['evidence_id'] for e in E}
pm={p['proposal_id']:p for p in P}; om={p['proposal_id']:p for p in OP}
selected={p['proposal_id']:p for p in sel['selected_payloads']}
ck('selection all128 exact IDs',set(selected)==set(pm))
for p in P:
    s=selected[p['proposal_id']]
    for k in ['proposal_id','owner_path','before_sha256','after_capture','case_ids']:
        ck('selected field '+p['proposal_id']+' '+k,s[k]==p[k])
    ck('selected destination '+p['proposal_id'],s['destination_path']==p.get('destination_path',p['owner_path']))
    cap(p['after_capture'])
    ck('proposal evidence closure '+p['proposal_id'],set(p['evidence_ids'])<=eidset)
    ck('proposal case closure '+p['proposal_id'],set(p['case_ids'])<={d['case_id'] for d in D})
for d in D:
    ck('case evidence closure '+d['case_id'],set(d['evidence_ids'])<=eidset)
    ck('case proposal closure '+d['case_id'],set(d['proposal_ids'])<=set(pm))
    for pid in d['proposal_ids']:ck('bidirectional proposal link '+d['case_id']+' '+pid,d['case_id'] in pm[pid]['case_ids'])
common={'evidence_ids','independent_review.evidence_ids','independent_review.status','source_successor_v7.actual_review_receipts','source_successor_v7.review_state','source_successor_v7.scope'}
extra={'source_successor_v7.historical_enum_finding.correction_state','source_successor_v7.historical_enum_finding.recheck_receipts','source_successor_v7.routing.path','source_successor_v7.routing.sha256','source_successor_v7.same_owner_dependency.exact_review_receipts','source_successor_v7.same_owner_dependency.review_state'}
for name,aa,bb,idkey,allowed_indices in [('decisions',AD,D,'case_id',case_indices),('proposals',AP,P,'proposal_id',[68,88,102,126,127])]:
    ck(name+' ordered membership retained',[x[idkey] for x in aa]==[x[idkey] for x in bb])
    actual_changed=[]
    for i,(a,b) in enumerate(zip(aa,bb)):
        dd=delta(a,b)
        if dd:
            actual_changed.append(i); diffs[name+':'+str(i)] = dd
            allowed=common|extra|({'review_status_explanation'} if name=='proposals' else set())
            ck('allowed final metadata paths '+name+str(i),{x[0] for x in dd}<=allowed)
            ck('review marked complete '+name+str(i),b['independent_review']['status']=='complete')
            ck('actual review evidence only '+name+str(i),b['independent_review']['evidence_ids']==new_eids[:3])
            ck('prior case/proposal evidence retained '+name+str(i),b['evidence_ids'][:len(a['evidence_ids'])]==a['evidence_ids'])
    ck(name+' exact final changed index set',actual_changed==allowed_indices)
for k in final:
    ck('non-row core metadata retained '+k,{x:y for x,y in final[k].items() if x not in ['decisions','proposals','evidence']}=={x:y for x,y in author[k].items() if x not in ['decisions','proposals','evidence']})
bridge=read(cap(sel['complete_bridge']))
ck('316 complete bridge rows',len(bridge['case_rows'])==188 and len(bridge['proposal_rows'])==128)
for i,row in enumerate(bridge['case_rows']):
    a,b=OD[i],D[i]
    ck('bridge case index '+str(i),row['index']==i)
    for k in ['case_id','source','case_input_sha256','occurrence_ids','owner_records']:ck('bridge case '+str(i)+' '+k,row[k]==a[k]==b[k])
    ck('bridge case before/after canonical '+str(i),row['before_object_sha256']==canon(a) and row['after_object_sha256']==canon(b))
    ck('bridge case retained flag '+str(i),row['whole_object_unchanged']==(a==b))
    ck('bridge case proposal IDs '+str(i),row['previous_proposal_ids']==a['proposal_ids'] and row['selected_proposal_ids']==b['proposal_ids'])
for row in bridge['proposal_rows']:
    pid=row['proposal_id']; p=pm[pid]; prior=om.get(pid)
    ck('bridge proposal full canonical '+pid,row['after_object_sha256']==canon(p) and row['before_object_sha256']==(canon(prior) if prior else None))
    ck('bridge proposal captures '+pid,row['selected_capture']==p['after_capture'] and row['previous_capture']==(prior['after_capture'] if prior else None))
    ck('bridge maintained preimage/case scope '+pid,row['maintained_before_sha256']==p['before_sha256'] and row['owner_path']==p['owner_path'] and row['case_ids']==p['case_ids'])
    ck('bridge proposal unchanged flag '+pid,row['payload_unchanged']==(bool(prior) and prior['after_capture']==p['after_capture']))
counts=read(S/'accounting.json')
calc={'cases':len(D),'occurrences':sum(len(d['occurrence_ids']) for d in D),'proposals':len(P),'evidence':len(E),'original_proposal_ids_retained':len(set(om)&set(pm)),'new_dependent_existing_owner_proposals':len(set(pm)-set(om)),'new_vendor_identities':0,'changed_original_payloads':sum(p['after_capture']!=pm[p['proposal_id']]['after_capture'] for p in OP),'unchanged_original_payloads':sum(p['after_capture']==pm[p['proposal_id']]['after_capture'] for p in OP),'changed_original_proposal_metadata':sum(p!=pm[p['proposal_id']] for p in OP),'unchanged_original_proposal_objects':sum(p==pm[p['proposal_id']] for p in OP),'changed_case_objects':sum(a!=b for a,b in zip(OD,D)),'unchanged_case_objects':sum(a==b for a,b in zip(OD,D)),'retained_original_evidence_objects':len(OE),'foreign_read_only_origins':1,'additional_context_rows_not_assigned_occurrences':7,'supported_Difco_context_routes':3,'held_prepared_Oxoid_context_routes':4}
ck('all recalculated accounting',counts==calc==sel['counts']==bridge['counts'])
for name in ['source-routing','cross-worker-dependencies']:
    a=read(S/(name+'.json'));b=read(S/(name+'-final.json'));dd=delta(a,b);diffs[name]=dd
    ck('routing only finalization/review receipts '+name,all(p=='finalization' or p.endswith('.review_state') or p.endswith('.exact_review_receipts') for p,_,_ in dd))
    ck('routing original attestation pinned '+name,b['finalization']['author_ledger']['sha256']==sha(raw(S/(name+'.json'))))
route=read(cap(sel['source_routing']));foreign=read(cap(sel['foreign_read_only_origins']))
ck('prepared holds retained',len(route['seven_context_rows'])==7 and sum(x['route_supported'] for x in route['seven_context_rows'])==3 and all(x['target_proposal_id'] is None for x in route['seven_context_rows'] if not x['route_supported']))
ck('no new context membership',all(x['assigned_W10_case_added'] is False and x['assigned_W10_occurrence_added'] is False and x['global_generic_label_or_provider_mapping'] is False for x in route['seven_context_rows']))
newpid='sv7-dependent-columbia-unmapped0118-partition';new=pm[newpid]
ck('only genuine dependent new origin',set(pm)-set(om)=={newpid} and new['kind']=='edit_existing_owner' and new['before_sha256']=='29ed63a00d3f4f7a1652beee549526d625eef231f29b40691bd128d2f7608324' and new['after_capture']['sha256']=='0bbcb8bd4d35c877569958065243479c868d92b77c741435101add857c2eceaa')
for dep in [route['same_owner_dependency'],route['Oxoid_origin_routes']['owner_dependency'],foreign['owner_dependency']]+[x['same_owner_dependency'] for x in route['seven_context_rows']]:
    ck('actual dependent bytes '+str(len(checks)),all(dep[k]==new[k] for k in ['proposal_id','kind','owner_path','before_sha256','after_capture','case_ids']))
    ck('dependent reviewed bounded/not applied '+str(len(checks)),dep['review_state']=='complete_bounded_full_payload_review_application_not_approved' and dep['application_state']=='not_applied')
ck('no final combined external owner or release',foreign['combined_payload_authored_here'] is False and foreign['W04_payload_changed'] is False and foreign['W10_payload_changed'] is False and sel['external_Oxoid_combination_installable_here'] is False and sel['application_or_release_approval'] is False)
for pid in ['sv3-hm-difco-columbia1270','sv1-bio-columbia_blood_agar_oxoid_m2224']:ck('vendor null maintained before '+pid,pm[pid]['before_sha256'] is None)
for k,v in BASE['maintained_owner_hashes'].items():ck('maintained owner exact '+k,sha(raw(R/k))==v)
for k,v in BASE['contract_hashes'].items():ck('contract exact '+k,sha(raw(R/k))==v)
ck('HEAD still actual prepublication',cmd(['git','rev-parse','HEAD'])==BASE['head']==sel['predecessor_head'])
ck('no tracked source mutation',cmd(['git','diff','--name-only','HEAD'])=='')
manifest=read(O.parent/'technical/AUTHOR_REVIEW_MANIFEST.json')
for x in manifest['files']:
    p=Path(x['path']);ck('frozen own technical exact '+str(p),sha(raw(p))==x['sha256'])
    relative=p.relative_to(O.parent/'technical');cp=S/'reviews/technical'/relative
    ck('canonical technical exact '+str(relative),raw(cp)==raw(p))
finalbind=read(S/'finalization-binding.json');scopes=read(S/'subagent-scopes.json')
for ref in finalbind['review_receipts']:cap(ref)
science=read(S/'reviews/science/scientific-review-v1.json');lineage=read(S/'reviews/lineage/author-v3-lineage-review.json');tech=read(S/'reviews/technical/author-technical-review-v1.json')
ck('actual scientist independent of candidate authorship',science['scientific_review'] is True and science['author_independent'] is True and science['reviewer']=='worker10:/root/preparation_skeptic (AI)')
ck('actual lineage technical scopes not science',lineage['scientific_review'] is False and tech['scientific_review'] is False and scopes['root_wrapper_is_self_review'] is True and scopes['not_human_review'] is True)
for tag in ['scientist','lineage_reviewer','technical_reviewer']:cap(scopes[tag]['report'])
for p in [S/'reviews/final-lineage/final-core-lineage-review-v1.json',S/'issue-linked-correction.json',S/'structural-audit.json']:read(p)

spec=importlib.util.spec_from_file_location('native_review',R/'scripts/record_review.py');native=importlib.util.module_from_spec(spec);spec.loader.exec_module(native)
pair=read(S/'native-v3/saved-pair.json')
for ref in pair['files']:cap(ref)
yp=R/pair['files'][0]['path'];mp=R/pair['files'][1]['path']
N=native.load_document(raw(yp));native.validate_review(N);ck('native closed schema semantic validation',True)
ck('actual native render exact Markdown',native.render_markdown(N).encode()==raw(mp))
ck('native actual c66 working tree',N['source']['git_revision']==BASE['head'] and N['source']['state']=='working_tree')
ck('root native wrapper self review',N['reviewer']['independence']=='self_review' and 'authored original941/955' in N['reviewer']['independence_basis'])
ck('native shape325/325/1053',len(N['targets'])==325 and len(N['assessments'])==325 and len(N['source']['inputs'])==1053 and N['scope']['population_size']==325)
tid={t['target_id'] for t in N['targets']}; ck('native exact declared coverage',set(N['scope']['reviewed_target_ids'])==tid and len(tid)==325)
ck('native each target exactly once assessed',sorted(t for a in N['assessments'] for t in a['target_ids'])==sorted(tid))
native_inputs={x['path']:x['sha256'] for x in N['source']['inputs']}
ck('native unique input paths',len(native_inputs)==1053)
for x in N['source']['inputs']:ck('native actual input '+x['path'],sha(raw(R/x['path']))==x['sha256'])
targets={t['target_id']:t for t in N['targets']}
for p in P:
    t=targets['PROPOSAL:'+p['proposal_id']];path=str((A/p['after_capture']['path']).relative_to(R))
    ck('native exact selected payload target '+p['proposal_id'],t['path']==path and native_inputs[path]==p['after_capture']['sha256'])
for i,d in enumerate(D):
    t=targets[d['case_id']];ck('native exact case target '+str(i),t['selector']==f'$.decisions[{i}]' and t['path']==str((S/'final-core/decisions.json').relative_to(R)))
for e in N['evidence']:ck('native evidence bytes '+e['evidence_id'],sha(raw(R/e['reference']))==e['snapshot_sha256'])
for a in N['assessments']:
    if a['topic']=='Separate current-owner source occurrence routing':
        row=json.loads(a['details']);ck('native exact full route detail '+row['context_id'],row==next(x for x in route['seven_context_rows'] if x['context_id']==row['context_id']))
    elif a['topic']=='Full source case and occurrence membership':
        row=json.loads(a['details']);d=D[row['source_index']]
        ck('native case retained source detail '+d['case_id'],row['case_input_sha256']==d['case_input_sha256'] and row['occurrence_ids']==d['occurrence_ids'] and row['proposal_ids']==d['proposal_ids'] and row['fresh_whole_case_acceptance'] is False)
sciencecheck=next(c for c in N['checks'] if c['check_id']=='PRIMARY-SCIENCE')
expectedscience={'PROPOSAL:'+r['proposal_id'] for r in f3['unchanged_four_payloads']}|{'PROPOSAL:sv1-bio-columbia_blood_agar_oxoid_m2224','FOREIGN:W04-OXOID','CONTEXT:OXOID-PROTOTYPE'}|{'CONTEXT:'+r['context_id'] for r in route['seven_context_rows']}
ck('native science check only actual14targets',set(sciencecheck['target_ids'])==expectedscience and len(expectedscience)==14)
ck('native qualified scope no new findings/actions',N['verdict']=='pass_with_limitations' and N['findings']==[] and N['actions']==[] and N['completion']=='completed')
for attempt in ['native','native-v2']:read(S/attempt/'attempt-failure.json')
for fname in ['inspection-command.json','validate-command.json','save-command.json']:
    r=read(S/'native-v3'/fname);ck('actual native command success '+fname,r['exit_code']==0)
v2=native.load_document(raw(S/'native-v2/review-input.yaml'));v3=native.load_document(raw(S/'native-v3/review-input.yaml'))
diffs['native-v2-to-v3']=delta(v2,v3)
def instant(x): return datetime.fromisoformat(x.replace('Z','+00:00'))
for p,a,b in diffs['native-v2-to-v3']:
    if p.startswith('evidence['):
        i=int(p.split('[')[1].split(']')[0]);field=p.rsplit('.',1)[1]
        if i>=10 and field=='accessed_at':
            ck('same original primary timestamp instant '+p,instant(a)==instant(b))
        elif i>=10 and field=='summary':
            ck('original primary timestamp string preserved '+p,b==a.replace(' ; reused exact original capture',' ; original timestamp '+v2['evidence'][i]['accessed_at']+' ; reused exact original capture'))
        elif i<10 and field=='accessed_at':
            ck('later actual local report access '+p,instant(a)<=instant(b)<=instant(v3['finished_at']))
        else:ck('unexpected native evidence change '+p,False)
    elif p=='finished_at': ck('later actual native completion',instant(a)<=instant(b))
    elif p=='review_id': ck('new actual native review ID',b=='20261108T102744Z-w10-columbia-controls-successor')
    else:ck('only native science target limit additional delta '+p,p=='checks[2].target_ids')
handoff=read(S/'HANDOFF-author.json')
ck('handoff author exact seal',sha(raw(S/'HANDOFF-author.json'))=='f9caf91b71231ce7281a5b26588a3f33806c9286e96068b318b55cfa8f720702')
ck('handoff core counts native exact',handoff['effective_core']==sel['authoritative_core'] and handoff['counts']==counts and handoff['native_pair']==pair)
def walkrefs(x):
    if isinstance(x,dict):
        if {'path','sha256'}<=set(x):cap(x)
        else:
            for v in x.values():walkrefs(v)
    elif isinstance(x,list):
        for v in x:walkrefs(v)
walkrefs(handoff)
ck('handoff no invented future head',handoff['predecessor_head']==BASE['head'] and handoff['status']=='candidate_complete_reviewed_pending_final_assembly_and_publication' and 'No future commit invented' in handoff['publication'])
ck('Handoff keeps coordinator composition',any('Coordinator must independently compose' in x for x in handoff['limits']))

result={'status':'PASS','scientific_review':False,'reviewer':'worker10:/root/buffers_research','started_at':start,'finished_at':datetime.now(timezone.utc).isoformat(),'runtime_seconds':time.monotonic()-clock,'script_sha256':sha(raw(Path(__file__))),'checks':checks,'counts':counts,'commands':commands,'input_hashes':inputs,'exact_author_to_final_diffs':diffs,'native_science_targets':sorted(expectedscience),'native_input_count':len(native_inputs),'final_selector_sha256':sha(raw(S/'selection.json')),'native_pair':pair,'handoff_sha256':sha(raw(S/'HANDOFF-author.json')),'scope':'Metadata/native integrity and preservation only; prior buffers authorship disclosed. No fresh source science, no application/release/whole-owner approval, no future published-head review.'}
with (O/'final-assembly-checks-v2.json').open('x') as f:json.dump(result,f,indent=2,ensure_ascii=False);f.write('\n')
print(json.dumps({'status':'PASS','checks':len(checks),'input_paths':len(inputs),'report_sha256':sha((O/'final-assembly-checks-v2.json').read_bytes())},indent=2))
