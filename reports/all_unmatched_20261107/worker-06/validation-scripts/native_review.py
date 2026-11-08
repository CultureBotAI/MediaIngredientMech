from pathlib import Path
import json, hashlib, datetime, subprocess, shutil, yaml

R=Path('reports/all_unmatched_20261107/worker-06')
N=R/'native-inputs'; N.mkdir(exist_ok=True)
PY='/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.venv/bin/python'
Q=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z')
def stamp(s): return datetime.datetime.fromisoformat(s.replace(' UTC','+00:00').replace('Z','+00:00')).astimezone(datetime.timezone.utc).isoformat().replace('+00:00','Z')
def dump(p,o): p.write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n')
for f in ['decisions.json','evidence.json','proposals.json']:
 shutil.copyfile(R/f,N/f)
shutil.copyfile(Q/'shards/shard-06.json',N/'frozen-shard-06.json')
D=json.loads((N/'decisions.json').read_text())['decisions']; E=json.loads((N/'evidence.json').read_text())['evidence']; P=json.loads((N/'proposals.json').read_text())['proposals']
audit=json.loads((R/'structural-audit-final.json').read_text())
invariants=json.loads((R/'logs/final-invariants.json').read_text())
schema_run=json.loads((R/'logs/proposal-schema-command.json').read_text())
assert len(D)==188 and all(d['independent_review']['status']=='complete' for d in D)
assert audit['structural_accounting']=='PASS' and audit['accounted_case_count']==len(D) and audit['proposal_count']==len(P)
assert audit['scientific_adequacy_or_approval_established'] is False
assert invariants['status']=='PASS' and not invariants['errors'] and invariants['proposal_count']==len(P)
assert schema_run['exit_code']==0 and schema_run['proposal_count']==len(P)
assert schema_run['payload_hashes']=={p['proposal_id']:p['after_capture']['sha256'] for p in P}
assert all(invariants['inputs'][str(R/f)]==sha(R/f) for f in ['decisions.json','evidence.json','proposals.json','source-holds.json'])
integration=json.loads((R/'research-b/integration-review/review-final.json').read_text())
assert integration['status']=='complete' and integration['scientific_release_approval'] is False
assert all(integration['input_sha256'][f]==sha(R/f) for f in ['decisions.json','evidence.json','proposals.json','source-holds.json'])
assert all(f['status']=='resolved' for f in integration['findings'])
assert {p['proposal_id']:p['after_capture']['sha256'] for p in integration['payload_bindings']}==schema_run['payload_hashes']
for p in P:
 assert sha(R/p['after_capture']['path'])==p['after_capture']['sha256']
for d in D:
 for eid in d['independent_review']['evidence_ids']:
  e=next(e for e in E if e['evidence_id']==eid)
  assert e['kind']=='independent_review' and e['capture']['root']=='artifact' and sha(R/e['capture']['path'])==e['capture']['sha256']
targets=[]; owners=set()
def ownership(paths):
 return {'owner_paths':[{'repository':'CultureBotAI/MediaIngredientMech','path':p,'role':'Actual frozen maintained owner; a candidate is not an approved source identity'} for p in paths]} if paths else {'ownership_note':'No established maintained MIM owner for this source case/proposed new substance. Future owner path is a proposal only.'}
for d in D:
 paths=sorted({x['path'] for x in d['owner_records']});owners.update(paths)
 targets.append({'target_id':d['case_id'],'path':str(N/'frozen-shard-06.json'),'selector':'cases[case_id='+d['case_id']+']','label':d['source']['raw_source_label'] or d['source']['source_label'] or d['source']['source_case_id'],'kind':'snapshot_row',**ownership(paths)})
for p in P:
 paths=[p['owner_path']] if p['kind']=='edit_existing_owner' else []
 owners.update(paths)
 targets.append({'target_id':p['proposal_id'],'path':str(R/p['after_capture']['path']),'label':p['description'],'kind':'source',**ownership(paths)})
dump(N/'targets.json',{'targets':targets})
context=['MAPPING_SEMANTICS.md','src/mediaingredientmech/schema/mediaingredientmech.yaml','schema/record_review.yaml','conf/record_review.yaml',str(R/'source-holds.json'),str(R/'primary-access-limitations.json'),str(R/'structural-audit-final.json'),str(R/'logs/proposal-schema-final.tsv'),str(R/'logs/final-invariants.json'),str(R/'research-b/integration-review/review-final.json'),*[str(N/f) for f in ['decisions.json','evidence.json','proposals.json']],*sorted(owners)]
cmd=[PY,'scripts/record_review.py','inspect','--targets',str(N/'targets.json')]
for p in context:cmd+=['--input',p]
r=subprocess.run(cmd,capture_output=True,text=True);(R/'logs/native-inspect.log').write_text(r.stdout+r.stderr)
assert r.returncode==0,r.stderr
inspection=json.loads(r.stdout);dump(N/'inspection.json',inspection)
access=now(); evidence=[]; evidence_ids=set()
kindmap={'primary_source':'primary_source','ontology':'authority','source_snapshot':'record_content','independent_review':'prior_review','unsuccessful_search':'search','local_validation':'validation','native_record_review':'prior_review'}
for e in E:
 cap=e['capture']; ref=str(R/cap['path']) if cap['root']=='artifact' else 'frozen-queue:'+cap['path']
 item={'evidence_id':e['evidence_id'],'kind':kindmap[e['kind']],'reference':e.get('url') or ref,'locator':e.get('locator') or ref,'accessed_at':stamp(e['accessed_at']) if e.get('accessed_at') else access,'support':'context_only' if e['kind'] in ['unsuccessful_search','source_snapshot'] else 'partial','summary':e['supports_or_contradicts']+' Exact capture: '+ref+'. Original external retrieval time is retained where recorded; otherwise accessed_at is this local bundle inspection.','snapshot_sha256':cap['sha256']}
 if item['kind']=='search':item['search_scope']=e.get('locator','Exact captured request')+'; failure or bounded negative search is not evidence of global absence.'
 evidence.append(item);evidence_ids.add(e['evidence_id'])
for eid,path,summary in [('N-AUDIT',R/'structural-audit-final.json','Whole-shard structural validation; scientific adequacy is explicitly not assessed by this validator.'),('N-SCHEMA',R/'logs/proposal-schema-final.tsv','All final proposal payloads pass strict closed-schema validation.'),('N-INVARIANTS',R/'logs/final-invariants.json','Exact source holds, baseline owner hashes, case IDs, proposed paths and maintained-file immutability checked.'),('N-INTEGRATION',R/'research-b/integration-review/review-final.json','Separate integration reviewer checked final cross-case links and reviewed payload bindings. This does not replace A review of B-authored science.')]:
 evidence.append({'evidence_id':eid,'kind':'prior_review' if eid=='N-INTEGRATION' else 'validation','reference':str(path),'accessed_at':access,'support':'supports','summary':summary,'snapshot_sha256':sha(path)});evidence_ids.add(eid)
assessments=[];findings=[];actions=[]
for i,d in enumerate(D):
 refs=list(dict.fromkeys(d['evidence_ids']+d['independent_review']['evidence_ids']+['N-INTEGRATION']))
 assert set(refs)<=evidence_ids
 assessments.append({'assessment_id':f'case-{i:03}','area':'identity','topic':d['disposition'],'outcome':'concern' if d.get('missing_requirement') else 'supported','summary':d['reasoning'],'target_ids':[d['case_id']],'evidence_ids':refs,'details':d['applicability']+' Remaining requirement: '+(d.get('missing_requirement') or 'No additional source identity requirement identified within this bounded assessment; source, owner and publication release remain separate.')})
 if d['disposition'] in ['unresolved','malformed_or_nonchemical_token']:
  fid=f'source-{i:03}'
  findings.append({'finding_id':fid,'issue_key':f'w06-20261107-source-{i:03}','category':'identity','severity':'major','status':'open','certainty':'confirmed','title':'Source identity remains bounded: '+d['source']['raw_source_label'],'description':'Confirmed evidence insufficiency within the inspected material; this does not assert an erroneous source identity. '+(d.get('missing_requirement') or d['reasoning']),'target_ids':[d['case_id']],'evidence_ids':refs,**ownership([o['path'] for o in d['owner_records']]),'external_issues':d['issue_refs']})
  actions.append({'action_id':f'resolve-{i:03}','description':d.get('missing_requirement') or d['reasoning'],'finding_ids':[fid],'target_ids':[d['case_id']],**ownership([o['path'] for o in d['owner_records']]),'acceptance_checks':['Obtain version-matched primary evidence for the exact source occurrence and supplied form.','Independently review the proposed identity and all affected owner claims; retain holds until the separate native release gates pass.']})
for p in P:
 scientific_review_ids=[eid for d in D if d['case_id'] in p['case_ids'] for eid in d['independent_review']['evidence_ids']]
 refs=list(dict.fromkeys(p['evidence_ids']+scientific_review_ids+['N-SCHEMA','N-INTEGRATION']))
 assessments.append({'assessment_id':p['proposal_id'],'area':'representation','topic':'Exact isolated curation proposal','outcome':'supported','summary':p['description'],'target_ids':[p['proposal_id']],'evidence_ids':refs,'details':'Exact proposed payload SHA256: '+p['after_capture']['sha256']+'. '+p.get('identity_predicate_alias_consequences','Source-specific identity/form boundaries remain as documented in the exact payload.')+' '+p.get('application_scope','')+' '+p.get('publication_review_obligations',' '.join(p.get('integration_constraints',[])))})
finish=now();ids=[t['target_id'] for t in targets]
review={'schema_version':'1.0.0','review_id':finish.replace('-','').replace(':','')+'-w06-source-shard','kind':'batch','repository':'CultureBotAI/MediaIngredientMech','title':'Worker 06 bounded source identity review and isolated proposals','started_at':'2026-11-08T05:05:57Z','finished_at':finish,'reviewer':{'identity':'Codex worker06 /root with research_a, research_b, research_c; actual author/reviewer scopes in agent-scopes.json','kind':'agent','independence':'self_review','independence_basis':'This is the team-authored native synthesis. Separate skeptical reviews are durable evidence: root reviewed A47; A reviewed B47; B reviewed C51; C reviewed root43. Integration review is distinct from B science approval.'},'skill':'.claude/skills/review-sssom-output/SKILL.md','completion':'completed','verdict':'needs_curation','scientific_review':True,'summary':f'All 188 frozen source cases have an evidence-backed assessment and separate skeptical review after primary-source research; unavailable primary recipes remain explicit in primary-access-limitations.json; {len(P)} exact isolated proposals are represented. Review completion does not assert all identities resolved. Maintained sources and all source/owner/export holds remain unchanged.','source':inspection['source'],'scope':{'description':'Bounded supplied-substance, formulation, alias, mapping and source-occurrence assessment; inherited full-owner roles and downstream publication are outside this review.','selection':'Exact frozen shard06 cases plus each final unique proposed owner payload; no other worker cases are scientifically claimed.','coverage':'full','population_size':len(targets),'reviewed_target_ids':ids,'exclusions':[{'target':'All other worker source cases','reason':'Read-only collision routing is not their scientific review.'},{'target':'Full maintained owner payload release and downstream exports','reason':'Coordinator integration requires fresh content-bound native approval after guarded edits; no release approval is conferred here.'}]},'targets':targets,'checks':[{'check_id':'whole-shard','name':'Frozen whole-shard structural audit','status':'passed','required':True,'summary':'188 exact cases, evidence captures, owner hashes and proposal backlinks validated.','target_ids':ids,'command':'audit_worker_outcomes_v1.py with explicit shard/artifact/source/mim roots; see structural-audit-final.json','exit_code':0,'evidence_ids':['N-AUDIT']},{'check_id':'proposal-schema','name':'Strict proposal schema validation','status':'passed','required':True,'summary':f'{len(P)} final proposal payloads, zero reported errors.','target_ids':[p['proposal_id'] for p in P],'command':'scripts/validate_strict.py final payload paths --workers 1; exact command in logs/proposal-schema-command.json','exit_code':0,'evidence_ids':['N-SCHEMA']},{'check_id':'source-holds','name':'Source holds and frozen owner integrity','status':'passed','required':True,'summary':'No maintained source mutation or source hold release; exact original owner hashes retained.','target_ids':ids,'command':'Final invariant script recorded in logs/final-invariants.json','exit_code':0,'evidence_ids':['N-INVARIANTS']}],'evidence':evidence,'assessments':assessments,'findings':findings,'actions':actions,'limitations':['A source access failure or bounded negative ontology search is preserved as an unresolved requirement, never converted into positive identity or global absence evidence.','Current supplier recipes do not establish historical lot invariance; ATCC MD-TMS and Merck108339 remain version-qualified.','The frozen assignment depends on PR1158 candidate base e000d66; no claim that this base is merged or current main.','No maintained YAML/SSSOM, publication selectors, downstream builds or release ledgers were modified. Structural and schema validity do not establish scientific truth.'],'links':['https://github.com/CultureBotAI/MediaIngredientMech/issues/1179','https://github.com/CultureBotAI/MediaIngredientMech/issues/1202'],'tags':['worker06','source-review','proposal-only']}
dump(R/'native-review-content.json',review)
print('Prepared native review',review['review_id'],len(targets),'targets;',len(findings),'open bounded source findings')
