"""Read-only sealed-input and successor metadata audit; outputs only in this task's directory."""
from pathlib import Path
import json, hashlib, datetime, itertools
import yaml
R=Path.cwd(); A=R/'reports/all_unmatched_20261107/worker-10'; O=A/'successor-v2/comparison-impact'; P=R/'.temp/final-preparation-comparison-v1'; S=R/'.temp/reconciled-stocks-independent-v1'
def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
started=now(); inputs={}; errors=[]
def sha(b):return hashlib.sha256(b).hexdigest()
def bind(p):
 p=Path(p); b=p.read_bytes(); d={'path':str(p),'sha256':sha(b),'bytes':len(b)}; inputs[str(p)]=d;return d

def read(p): bind(p);return json.loads(Path(p).read_text())
def canonical(o):return sha(json.dumps(o,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode())
def check(label,condition,details=None):
 if not condition:errors.append({'check':label,'details':details})
 return condition

def output(name,obj):
 p=O/name
 if p.exists():raise RuntimeError('Append-only output already exists: '+str(p))
 p.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n');return bind(p)

def manifest(root,name,countkey):
 m=read(root/name); rows=[]
 for x in m['files']:
  p=root/x['path']; exists=p.is_file(); got=bind(p) if exists else None
  ok=exists and got['sha256']==x['sha256'] and got['bytes']==x['bytes']
  check('manifest file '+str(p),ok,{'expected':x,'actual':got})
  rows.append({'path':x['path'],'expected_sha256':x['sha256'],'actual_sha256':got['sha256'] if got else None,'bytes':got['bytes'] if got else None,'pass':ok})
 declared={x['path'] for x in m['files']}; actual={str(p.relative_to(root)) for p in root.rglob('*') if p.is_file() and p!=root/name}
 extras=sorted(actual-declared);missing=sorted(declared-actual)
 check('manifest exact file inventory '+str(root),not extras and not missing,{'extras':extras,'missing':missing})
 check('manifest declared count '+str(root),m[countkey]==len(rows))
 return {'manifest':bind(root/name),'declared_count':m[countkey],'tested_files':len(rows),'passing_files':sum(x['pass'] for x in rows),'extras':extras,'missing':missing,'ignored_and_hidden_included':True,'entries':rows}

pm=manifest(P,'MANIFEST.json','file_count');sm=manifest(S,'REVIEW_MANIFEST.json','count')
assignment=read(P/'assignment.json'); pre=read(P/'preflight.json'); I=Path(assignment['intake_root']); families=read(Path(assignment['source'])); all_entries=read(I/'all-active-proposal-entries-v1.json')['entries']; byindex={x['index']:x for x in all_entries}; byid={x['entry_id']:x for x in all_entries}
check('assignment bytes equal original assignment',bind(P/'assignment.json')['sha256']==bind(pre['assignment_path'])['sha256']==pre['assignment_sha256'])
check('family source hash',bind(assignment['source'])['sha256']==assignment['source_sha256']==pre['family_source_sha256'])
allfam={x['family_id']:x for x in families['families']}
selected={}
for f in assignment['families']:
 check('assigned family exact source '+f['family_id'],f==allfam[f['family_id']])
 for e in f['origins']:
  if e['entry_id'] in selected:check('repeated origin exact '+e['entry_id'],selected[e['entry_id']]==e)
  selected[e['entry_id']]=e
  # Families retain selected views of intake entries. Compare every included field.
  check('assigned origin matches full intake '+e['entry_id'],all(byid[e['entry_id']].get(k)==v for k,v in e.items()))
check('author exclusions',assignment['authors_excluded_checked'] and all(x['worker'] not in [9,10] for x in selected.values()))
frozen=[]
for p,expected in pre['frozen_files'].items():
 actual=bind(p) if Path(p).is_file() else None
 ok=actual is not None and actual['sha256']==expected['sha256'] and actual['bytes']==expected['bytes'];check('frozen input '+p,ok)
 frozen.append({'path':p,'role':expected.get('role'),'expected_sha256':expected['sha256'],'actual_sha256':actual['sha256'] if actual else None,'bytes':actual['bytes'] if actual else None,'pass':ok})
snaps=read(P/'selected-payload-snapshots.json'); snapby={x['entry_id']:x for x in snaps['entries']}; bound=read(P/'bound-cases-decisions-proposals.json');boundby={x['entry_id']:x for x in bound['entries']}
check('96 selected sets exact',set(selected)==set(snapby)==set(boundby) and len(selected)==96)
selectedrows=[]
for eid,e in sorted(selected.items(),key=lambda t:t[1]['index']):
 p=I/e['payload_path'];actual=bind(p);s=snapby[eid];b=boundby[eid]
 tests={'frozen_payload_hash':actual['sha256']==e['payload_sha256'],'snapshot_raw_hash':sha(s['raw_utf8'].encode())==e['payload_sha256'],'snapshot_source_path':str(p)==s['source_path'],'snapshot_declared_hash':s['payload_sha256']==e['payload_sha256'],'snapshot_parsed_record':yaml.safe_load(p.read_text())==s['record'],'bound_payload_path_hash':str(p)==b['payload_path'] and b['payload_sha256']==e['payload_sha256'],'source_case_ids':set(b['source_case_ids'])==set(e['case_ids'])}
 check('selected payload bindings '+eid,all(tests.values()),tests)
 selectedrows.append({'index':e['index'],'entry_id':eid,'worker':e['worker'],'head':e['head'],'provisional':e['provisional'],'payload':actual,'owner_path':e['owner_path'],'family_ids':[f['family_id'] for f in assignment['families'] if eid in {x['entry_id'] for x in f['origins']}],'case_ids':e['case_ids'],'assignment_case_bindings':e['case_bindings'],'applicable_occurrence_ids_explicit':b['applicable_occurrence_ids_explicit'],'tests':tests})
casechecks=[];cache={}
for c in bound['cases']:
 sp=c['source_shard'];dp=c['decision_ledger']
 if sp not in cache:cache[sp]=read(sp)
 if dp not in cache:cache[dp]=read(dp)
 originals=[x for x in cache[sp]['cases'] if x['case_id']==c['case_id']]
 decisions=[x for x in cache[dp]['decisions'] if x['case_id']==c['case_id']]
 tests={'source_shard_hash':bind(sp)['sha256']==c['source_shard_sha256'],'original_case_exact':len(originals)==1 and originals[0]==c['original_case'],'canonical_case_hash':canonical(c['original_case'])==c['canonical_case_sha256'],'decision_ledger_hash':bind(dp)['sha256']==c['decision_ledger_sha256'],'selected_decision_exact':len(decisions)==1 and decisions[0]==c['selected_decision']}
 check('original case and decision '+c['case_id'],all(tests.values()),tests);casechecks.append({'case_id':c['case_id'],'case_sha256':c['canonical_case_sha256'],'tests':tests})

oldp=read(A/'successor-v1/proposals.json')['proposals'];newp=read(A/'successor-v2/proposals.json')['proposals'];op={x['proposal_id']:x for x in oldp};np={x['proposal_id']:x for x in newp}
removed=sorted(op.keys()-np.keys());added=sorted(np.keys()-op.keys());changed=[k for k in op.keys()&np.keys() if op[k]!=np[k]];unchanged=[k for k in op.keys()&np.keys() if op[k]==np[k]]
oldid='kg-isp4-remove-salt-parent';newid='sv2-isp4-jcm58-complete-formulation';carbid='sv1-buffers-carbonate_co2_nominal4percent_togo_m202'
check('expected proposal delta',removed==[oldid] and added==[newid] and changed==[carbid] and len(unchanged)==126)
payload_checks=[]
for version,proposals in [('v1',oldp),('v2',newp)]:
 for x in proposals:
  cap=x['after_capture'];actual=bind(A/cap['path']);ok=actual['sha256']==cap['sha256'];check('worker10 '+version+' payload '+x['proposal_id'],ok)
  payload_checks.append({'version':version,'proposal_id':x['proposal_id'],'payload':actual,'expected_sha256':cap['sha256'],'pass':ok})
check('carbonate exact unchanged after_capture',op[carbid]['after_capture']==np[carbid]['after_capture'])
check('pure carbonate proposal unchanged',op['kg-carbonate-buffer-alias']==np['kg-carbonate-buffer-alias'])
pairs=[(k,k)for k in sorted(op.keys()&np.keys())]+[(oldid,newid)]
payload_delta=[{'before_proposal_id':a,'after_proposal_id':b,'before':op[a]['after_capture'],'after':np[b]['after_capture'],'payload_bytes_changed':op[a]['after_capture']['sha256']!=np[b]['after_capture']['sha256']} for a,b in pairs]
check('one payload changed',sum(x['payload_bytes_changed'] for x in payload_delta)==1)
old_dec=read(A/'successor-v1/decisions.json')['decisions'];new_dec=read(A/'successor-v2/decisions.json')['decisions'];od={x['case_id']:x for x in old_dec};nd={x['case_id']:x for x in new_dec}
changedcases=[x for x in nd if x not in od or od[x]!=nd[x]]; case143=new_dec[143]['case_id'];case187=new_dec[187]['case_id'];case21=new_dec[21]['case_id']
check('expected two case changes',len(od)==len(nd)==188 and set(od)==set(nd) and set(changedcases)=={case143,case187})
check('original case21 decision exact',od[case21]==nd[case21])
check('case187 no invented occurrences',nd[case187]['occurrence_ids']==od[case187]['occurrence_ids']==[])
check('carbonate original case21 occurrence retained',np[carbid]['applicable_occurrence_ids']==od[case21]['occurrence_ids'])
check('carbonate case_ids original plus187',set(np[carbid]['case_ids'])==set(op[carbid]['case_ids'])|{case187})
check('case input identities/raw sources preserved',all(od[k]['case_input_sha256']==nd[k]['case_input_sha256'] and od[k]['source']==nd[k]['source'] and od[k]['occurrence_ids']==nd[k]['occurrence_ids'] for k in od))
orig_evi=read(A/'successor-v1/evidence.json')['evidence'];new_evi=read(A/'successor-v2/evidence.json')['evidence'];oe={x['evidence_id']:x for x in orig_evi};ne={x['evidence_id']:x for x in new_evi}
check('all predecessor evidence objects exact',all(k in ne and v==ne[k] for k,v in oe.items()))

focus=[]
for ix in [548,882,888,933]:
 e=byindex[ix];actual=bind(I/e['payload_path']);check('focus frozen payload '+str(ix),actual['sha256']==e['payload_sha256'])
 focus.append({'index':ix,'entry_id':e['entry_id'],'head':e['head'],'provisional':e['provisional'],'payload':actual,'owner_path':e['owner_path'],'case_ids':e['case_ids'],'case_bindings':e['case_bindings'],'assignment_family_ids':[f['family_id'] for f in assignment['families'] if ix in f['entry_indices']],'all67_mechanical_family_ids':[f['family_id'] for f in families['families'] if ix in f['entry_indices']]})
check('all four focus entries outside assigned and all67 families',all(not x['assignment_family_ids'] and not x['all67_mechanical_family_ids'] for x in focus))
changeowners={op[oldid]['owner_path'],np[newid]['owner_path'],np[newid].get('destination_path'),np[carbid]['owner_path'],op['kg-carbonate-buffer-alias']['owner_path'],byindex[548]['owner_path']}-{None}
impacts=[]
for f in assignment['families']:
 ids={x['entry_id'] for x in f['origins']};fcases={c for x in f['origins']for c in x['case_ids']};owns={x['owner_path']for x in f['origins']}; entryhits=sorted(ids&{byindex[i]['entry_id']for i in [548,882,888,933]});casehits=sorted(fcases&{case143,case187,case21});ownerhits=sorted(owns&changeowners)
 check('family outside successor delta '+f['family_id'],not entryhits and not casehits and not ownerhits)
 impacts.append({'family_id':f['family_id'],'entry_indices':f['entry_indices'],'entry_ids':[x['entry_id']for x in f['origins']],'selected_payloads_verified':len(ids),'changed_selected_payloads':0,'affected_entry_ids':entryhits,'affected_case_ids':casehits,'affected_exact_owner_paths':ownerhits,'frozen_w06_entry548_member':548 in f['entry_indices'],'disposition':'Preserve exact frozen conclusions; successor changes are outside this assigned family. No new scientific comparison performed.'})
# Bind contextual reports without extending their scientific approval.
for p in [P/'report.json',P/'reviewer-scopes.json',P/'HANDOFF.json',S/'report-v2.json',S/'reviewer-scopes-v2.json',S/'review-v2.yaml',A/'successor-v2/finalization-binding.json',A/'successor-v2/isp4/nested-stock-overlap-finding.json',A/'successor-v2/isp4/author-assessment.json',A/'successor-v2/carbonate/primary-assessment-v1.json',A/'successor-v2/reviews/skeptic/scientific-review-v1.json']:
 bind(p)
newrecord=yaml.safe_load((A/np[newid]['after_capture']['path']).read_text());trace=[x for x in newrecord['components'] if 'trace' in x['component_name'].lower()]
check('one unresolved trace component',len(trace)==1 and trace[0].get('reference_scope')=='UNMAPPED' and 'component_id' not in trace[0])
check('nine immediate ISP4 input entries',len(newrecord['components'])==9)
oldrecord=yaml.safe_load((A/op[oldid]['after_capture']['path']).read_text());check('prior proposal history prefix retained',newrecord['curation_history'][:len(oldrecord['curation_history'])]==oldrecord['curation_history'])
check('authentic baseline owner hash preserved',np[newid]['before_sha256']==op[oldid]['before_sha256']==bind(R/np[newid]['owner_path'])['sha256'])

manifestreceipt=output('manifest-verification.json',{'audit_started_at':started,'comparison':pm,'stocks':sm})
frozenreceipt=output('frozen-input-verification.json',{'count':len(frozen),'passing':sum(x['pass'] for x in frozen),'entries':frozen})
selectedreceipt=output('selected-96-bindings.json',{'entries':selectedrows,'original_case_and_decision_checks':casechecks,'scope':'Metadata and byte integrity only; source applicability subsets retained separately from complete original case inventories.'})
delta=output('worker10-successor-delta.json',{'old_proposal_count':len(oldp),'new_proposal_count':len(newp),'removed_proposal_ids':removed,'added_proposal_ids':added,'changed_common_proposal_ids':changed,'unchanged_proposal_objects':len(unchanged),'payloads_verified':payload_checks,'payload_deltas':payload_delta,'changed_cases':[{'case_id':k,'source_index':nd[k].get('source_index'),'before_object_sha256':canonical(od[k]),'after_object_sha256':canonical(nd[k]),'changed_fields':sorted(f for f in od[k].keys()|nd[k].keys() if od[k].get(f)!=nd[k].get(f))}for k in changedcases],'unchanged_cases':len(nd)-len(changedcases),'case21_exact_unchanged_sha256':canonical(nd[case21]),'original_evidence_objects_preserved':len(oe),'new_evidence_objects':len(ne)-len(oe),'focus_frozen_entries':focus,'family_impacts':impacts})
# Recheck every sealed manifest-listed byte after all metadata inspection.
for root,m in [(P,pm),(S,sm)]:
 for e in m['entries']:check('end-of-audit sealed preservation '+str(root/e['path']),sha((root/e['path']).read_bytes())==e['actual_sha256'])
inputreceipt=output('input-hashes.json',{'audit_started_at':started,'inputs':sorted(inputs.values(),key=lambda x:x['path'])})
finished=now(); pairsets=[{tuple(sorted(p))for p in itertools.combinations(f['entry_indices'],2)}for f in assignment['families']]
report={'schema_version':1,'report_id':'worker10-successor-v2-comparison-impact','status':'PASS_bounded_metadata_check' if not errors else 'FAIL_requires_review','author':'/root/bio_research','timing':{'actual_review_start_exact':None,'review_start_note':'This metadata reading began before this audit script; exact first-read time was not separately captured. Script runtime is not described as the full review interval.','audit_execution_started_at':started,'audit_execution_finished_at':finished,'completion_observed_at':finished},'scope':'Read-only manifest, frozen assignment/input integrity, proposal/case metadata delta and exact family membership audit. No primary-source scientific re-review or new equivalence verdict.','authorship_and_exclusions':{'this_agent_authored_new_isp4_payload':True,'this_is_independent_scientific_review_of_that_payload':False,'prior_bio_comparison_scope':'40 selected entries in FAM-005/052/063/065/066; preserved as historical report, not repeated here.','original19_family_assignment_workers':sorted({x['worker']for x in selected.values()}),'no_worker9_or_worker10_authored_entry_in_assignment':True,'all_original_author_exclusions_preserved':True,'worker06_entry548_remains_provisional_and_unaccepted':True},'tested_counts':{'sealed_comparison_manifest_files':len(pm['entries']),'sealed_stocks_manifest_files':len(sm['entries']),'frozen_preflight_files':len(frozen),'assigned_families':len(assignment['families']),'selected_unique_entries':len(selected),'family_entry_memberships':sum(len(f['entry_indices'])for f in assignment['families']),'original_cases_rechecked':len(casechecks),'original_occurrence_ids':len({o['occurrence_id']for c in bound['cases']for o in c['original_case'].get('occurrences',[])}),'pair_memberships_preserved':sum(map(len,pairsets)),'unique_pairs_preserved':len(set().union(*pairsets)),'worker10_old_and_new_payload_references_verified':len(payload_checks),'unchanged_worker10_payloads':sum(not x['payload_bytes_changed']for x in payload_delta),'changed_worker10_payloads':sum(x['payload_bytes_changed']for x in payload_delta),'unchanged_worker10_proposal_objects':len(unchanged),'changed_worker10_cases':len(changedcases),'unchanged_worker10_cases':len(nd)-len(changedcases)},'conclusion':'No selected input, assigned family member, source case binding, exact owner path or frozen conclusion changes in the 19-family comparison. All sealed bytes remain exact. Worker10 successor changes are outside the assigned cohort.','impacts':{'isp4':{'case_id':case143,'old_frozen_entry_index':882,'old_proposal_id':oldid,'replacement_proposal_id':newid,'before_owner_sha256':np[newid]['before_sha256'],'old_payload_sha256':op[oldid]['after_capture']['sha256'],'new_payload_sha256':np[newid]['after_capture']['sha256'],'mapped_destination':np[newid].get('destination_path'),'metadata_observations':'One whole-medium candidate replaces the prior invalid-parent-removal proposal. Its nine immediate input entries retain one UNMAPPED trace component without component_id; prior history is an exact prefix. These are structural observations, not new scientific approval.','needed_coordinator_action':'Route this new worker10 candidate and existing recorded overlap with frozen W06 entry548 to separate content-bound review/reconciliation. Do not add it to or retroactively inherit acceptance from the sealed 19-family comparison.'},'case187':{'case_id':case187,'original_pure_carbonate_frozen_entry_index':888,'existing_stock_frozen_entry_index':933,'stock_proposal_id':carbid,'stock_payload_sha256':np[carbid]['after_capture']['sha256'],'owner_payload_unchanged':True,'pure_carbonate_proposal_exact_unchanged':True,'original_case21_decision_exact_unchanged':True,'metadata_effect':'Add exact case187 source association/backlink/evidence to existing source-qualified stock proposal; original case21 occurrence is retained, with no invented KG CM_OCC identifiers and no second stock owner. This is the successor author/reviewer scope, not a new science claim by this audit.'},'w06_entry548':focus[0],'family_impacts':impacts},'review_dependencies':[{'id':'SV2-ISP4-NESTED-OVERLAP-001','status':'Preserved existing successor finding; not resolved by this metadata audit.','record':bind(A/'successor-v2/isp4/nested-stock-overlap-finding.json'),'meaning':'Entry548 occurs in neither the assigned19 nor the complete67 frozen mechanical-family inventories. Its new ISP4 dependency is outside those scopes and must remain explicit. No automatic candidate identifier adoption or whole-medium equivalence.'}],'preservation':{'sealed_report':bind(P/'report.json'),'sealed_comparison_manifest':bind(P/'MANIFEST.json'),'sealed_stock_review_manifest':bind(S/'REVIEW_MANIFEST.json'),'original_timestamp_fields_untouched':True,'scientific_conclusions_recomputed':False,'roles_export_mapping_or_release_approval_inherited':False,'payload_edits':False,'maintained_or_source_writes':False,'git_or_github_mutations':False,'new_external_sessions':False,'absence_search_scope':'All listed manifests and all67 structured family objects examined; directory inventories include ignored and hidden files.'},'supporting_receipts':[manifestreceipt,frozenreceipt,selectedreceipt,delta,inputreceipt],'errors':errors,'limitations':['No claim that the 67 mechanical families exhaust all possible scientific relationships.','No new independent approval of the authored ISP4 payload, case187 source science, W06 candidate or role/export/full owner acceptance.','No broad native validation rerun: only file hashes, exact structured objects, case/occurrence preservation and explicit scope membership checked.']}
rp=A/'successor-v2/comparison-impact.json'
if rp.exists():raise RuntimeError('Append-only report already exists')
rp.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'report':str(rp),'sha256':sha(rp.read_bytes()),'status':report['status'],'counts':report['tested_counts'],'errors':errors},indent=2))
