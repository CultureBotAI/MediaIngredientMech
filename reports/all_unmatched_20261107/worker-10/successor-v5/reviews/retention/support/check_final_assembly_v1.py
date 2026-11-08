#!/usr/bin/env python3
"""Independent exhaustive retention/final-metadata audit; never edits prior artifacts."""
import datetime,hashlib,importlib.util,json,pathlib,shutil,subprocess,time,yaml
R=pathlib.Path.cwd();A=R/'reports/all_unmatched_20261107/worker-10';S=A/'successor-v5';P=R/'.temp/all-unmatched-worker-10/successor-v5/retention';O=S/'reviews/retention'
Q=pathlib.Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
BASE='82fc29d837a223edb9c436445ec7ea13d2840c7b';C9='c9a96da71a1977014680e5a92e600dfc7e3874db';TARGET='sv1-bio-calf_blood_togo_m2854';CARB='sv1-buffers-carbonate_co2_nominal4percent_togo_m202'
RID='20261108T083730Z-w10-calf-blood-wording-successor';REPORT=O/'final-assembly-metadata-review-v1.json'
now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat();h=lambda b:hashlib.sha256(b).hexdigest();started=now();tick=time.monotonic();checks=[];commands=[]
def rd(p):return json.loads(p.read_text())
def canon(j):return h(json.dumps(j,sort_keys=True,ensure_ascii=False,separators=(',',':'),allow_nan=False).encode())
def dump(p,j):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(j,indent=2,ensure_ascii=False)+'\n')
def bind(p):return {'path':str(p.relative_to(R)) if p.is_relative_to(R) else str(p),'sha256':h(p.read_bytes()),'bytes':p.stat().st_size}
def ck(n,ok,detail=None):checks.append({'check':n,'pass':bool(ok),'detail':detail})
def run(argv):
 t=now();t0=time.monotonic();r=subprocess.run(argv,stdout=subprocess.PIPE,stderr=subprocess.PIPE);commands.append({'argv':argv,'started_at':t,'finished_at':now(),'runtime_seconds':time.monotonic()-t0,'exit_code':r.returncode,'stdout_sha256':h(r.stdout),'stderr':r.stderr.decode()});ck('Command exit '+str(argv),r.returncode==0);return r.stdout

def diff(a,b,p=''):
 if type(a)!=type(b):return [{'pointer':p,'before':a,'after':b}]
 if isinstance(a,dict):return sum((diff(a.get(k),b.get(k),p+'/'+k) for k in sorted(set(a)|set(b))),[])
 if isinstance(a,list):return [] if a==b else [{'pointer':p,'before':a,'after':b}]
 return [] if a==b else [{'pointer':p,'before':a,'after':b}]
def resolve(c):
 p=pathlib.Path(c['path'])
 if p.is_absolute():return p
 if c.get('root')=='artifact' or str(p).startswith('successor-'):return A/p
 if c.get('root')=='source':return Q/p
 return R/p

def bindings(j,tag):
 if isinstance(j,dict):
  if isinstance(j.get('path'),str) and isinstance(j.get('sha256'),str):
   p=resolve(j);ck('Hash binding '+tag+':'+j['path'],p.is_file() and h(p.read_bytes())==j['sha256'])
  for k,v in j.items():bindings(v,tag+'/'+k)
 elif isinstance(j,list):
  for i,v in enumerate(j):bindings(v,tag+'/'+str(i))
if REPORT.exists():raise RuntimeError('Frozen report exists; do not overwrite')
base=rd(P/'baseline-v1.json');nativebase=rd(P/'native-baseline-supplement-v1.json');pres=rd(P/'preservation-baseline-v1.json');authorreview=rd(O/'author-core-retention-review-v1.json');freeze=rd(S/'author-freeze.json')
ck('Prior independent author review unchanged',h((O/'author-core-retention-review-v1.json').read_bytes())=='b59f5174f01b907207c377c77b1f70caeb42a96cc3c847ceef2a37a5f266e4d6')
old={n:rd(P/'frozen/final-core'/f'{n}.json') for n in ['decisions','proposals','evidence']};author={n:rd(S/'author-core'/f'{n}.json') for n in old};final={n:rd(S/'final-core'/f'{n}.json') for n in old}
for n in author:ck('Author freeze retained '+n,h((S/'author-core'/f'{n}.json').read_bytes())==freeze['author_core'][n+'.json']['sha256'])
# Authenticate c9's complete selected objects directly from committed Git blobs, not bridge summaries.
c9selection_bytes=run(['git','show',C9+':'+str(A.relative_to(R))+'/successor-v3/selection.json']);c9selection=json.loads(c9selection_bytes);gitsupport=[]
p=P/'final-c9-baseline/selection.json';p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(c9selection_bytes);gitsupport.append(bind(p));c9={}
for n in old:
 rel=str(A.relative_to(R))+'/successor-v3/'+n+'.json';b=run(['git','show',C9+':'+rel]);ck('c9 authoritative core '+n,h(b)==c9selection['authoritative_core'][n+'.json']);p=P/'final-c9-baseline'/f'{n}.json';p.write_bytes(b);gitsupport.append(bind(p));c9[n]=json.loads(b)
indexes={}
for label,core in [('s4',old),('author',author),('final',final),('c9',c9)]:indexes[label]={n:{x[{'decisions':'case_id','proposals':'proposal_id','evidence':'evidence_id'}[n]]:x for x in core[n][n]} for n in core}
op=indexes['s4']['proposals'];np=indexes['final']['proposals'];nd=indexes['final']['decisions'];cid=op[TARGET]['case_ids'][0]
ck('127 proposal identities/order retained',list(op)==list(np) and len(np)==127)
ck('188 case identities/order retained',list(indexes['s4']['decisions'])==list(nd) and len(nd)==188)
occ=[o for d in nd.values() for o in d['occurrence_ids']];ck('304 unique occurrences retained',len(occ)==len(set(occ))==304 and all(d['occurrence_ids']==indexes['s4']['decisions'][k]['occurrence_ids'] for k,d in nd.items()))
ck('126 non-target complete proposals retained',sum(op[k]==np[k] for k in op if k!=TARGET)==126)
ck('187 non-target complete decisions retained',sum(indexes['s4']['decisions'][k]==nd[k] for k in nd if k!=cid)==187)
for n in final:
 ck('Root object metadata retained '+n,{k:v for k,v in author[n].items() if k!=n}=={k:v for k,v in final[n].items() if k!=n})
 ck('All author object IDs retained '+n,set(indexes['author'][n])<=set(indexes['final'][n]))
for k,e in indexes['author']['evidence'].items():ck('Author evidence exact '+k,e==indexes['final']['evidence'][k])
for k,e in indexes['s4']['evidence'].items():ck('Original evidence exact '+k,e==indexes['final']['evidence'][k])
newids=['sv5-independent-wording','sv5-independent-retention','sv5-native-narrow-validation'];ck('Only three final evidence additions',set(indexes['final']['evidence'])-set(indexes['author']['evidence'])==set(newids) and len(indexes['final']['evidence'])==1212)
allowed={'/evidence_ids','/independent_review/evidence_ids','/independent_review/status','/wording_successor/independent_review_bindings','/wording_successor/review_state'};deltas={}
for n,key in [('decisions',cid),('proposals',TARGET)]:
 before=indexes['author'][n][key];after=indexes['final'][n][key];ds=diff(before,after);deltas[n]=ds
 ck('Final '+n+' scoped status/pointers only',set(x['pointer'] for x in ds)<=allowed|({'/review_status_explanation'} if n=='proposals' else set()),[x['pointer'] for x in ds])
 ck('Final '+n+' exact evidence prefix',after['evidence_ids']==before['evidence_ids']+newids)
 ck('Final '+n+' review refs only exact reviewed evidence',after['independent_review']=={'status':'complete','evidence_ids':newids[:2]})
 ck('Final '+n+' no changed other objects',all(indexes['author'][n][k]==v for k,v in indexes['final'][n].items() if k!=key))
 ck('Final '+n+' limits retained',after['wording_successor']['whole_owner_or_export_approval'] is False and after['wording_successor']['identity_or_alias_change'] is False)
for eid in newids:
 e=indexes['final']['evidence'][eid];ck('Final evidence scope/kind '+eid,e['case_ids']==[cid] and e['url'] is None and e['kind']==('local_validation' if eid==newids[-1] else 'independent_review'))
# All payloads and all evidence actual bytes, including original captures and timestamps through object equality.
payloads=[]
for pid,p in np.items():
 actual=h(resolve(p['after_capture']).read_bytes());ck('Selected payload hash '+pid,actual==p['after_capture']['sha256']);ck('Payload unchanged after author '+pid,p['after_capture']==indexes['author']['proposals'][pid]['after_capture']);payloads.append({'proposal_id':pid,'capture':p['after_capture'],'actual_sha256':actual,'same_as_s4':actual==op[pid]['after_capture']['sha256']})
ck('Only calf payload changed since S4',[x['proposal_id'] for x in payloads if not x['same_as_s4']]==[TARGET])
for sentinel in base['sentinels']:ck('Explicit unchanged sentinel '+sentinel['proposal_id'],np[sentinel['proposal_id']]==op[sentinel['proposal_id']] and np[sentinel['proposal_id']]['after_capture']==sentinel['after_capture'])
capturechecks=[]
for eid,e in indexes['final']['evidence'].items():
 actual=h(resolve(e['capture']).read_bytes());ck('Evidence actual hash '+eid,actual==e['capture']['sha256']);capturechecks.append({'evidence_id':eid,'capture':e['capture'],'actual_sha256':actual})
# Independently derive every member in both 315-row bridges, not just their totals.
bridge_summaries=[];bridge_checks=[]
identitykeys=['source','source_index','case_id','case_input_sha256','occurrence_ids','owner_records','proposal_ids','disposition','applicability','publication_approval','existing_holds_preserved']
for name,label in [('complete-bridge.json','s4'),('combined-c9-bridge.json','c9')]:
 b=rd(S/name);od=indexes[label]['decisions'];bp=indexes[label]['proposals'];ck(name+' exhaustive unique membership',len(b['all_cases'])==len({x['case_id'] for x in b['all_cases']})==188 and len(b['all_proposals'])==len({x['proposal_id'] for x in b['all_proposals']})==127 and {x['case_id'] for x in b['all_cases']}==set(nd) and {x['proposal_id'] for x in b['all_proposals']}==set(np));changed_cases=[];changed_payloads=[];changed_proposals=[]
 for row in b['all_cases']:
  k=row['case_id'];a=od[k];z=nd[k];expected={'source_index':z['source_index'],'case_id':k,'before_object_sha256':canon(a),'after_object_sha256':canon(z),'complete_object_exact':a==z,'source_identity_occurrence_owner_hashes_exact':all(a.get(x)==z.get(x) for x in identitykeys),'reasoning_exact':a['reasoning']==z['reasoning'],'occurrence_ids':z['occurrence_ids'],'proposal_ids':z['proposal_ids']};ck(name+' exact case row '+k,row==expected);ck(name+' identity/scope retained '+k,expected['source_identity_occurrence_owner_hashes_exact']);bridge_checks.append({'bridge':name,'member_type':'case','key':k,'expected':expected,'actual_matches':row==expected})
  if a!=z:changed_cases.append(z['source_index'])
 for row in b['all_proposals']:
  k=row['proposal_id'];a=bp[k];z=np[k];ab=resolve(a['after_capture']).read_bytes();zb=resolve(z['after_capture']).read_bytes();ck(name+' historical capture actual '+k,h(ab)==a['after_capture']['sha256']);expected={'proposal_id':k,'before_proposal_sha256':canon(a),'after_proposal_sha256':canon(z),'proposal_object_exact':a==z,'old_capture':a['after_capture'],'selected_capture':z['after_capture'],'payload_byte_exact':ab==zb,'owner_path':z['owner_path'],'before_owner_sha256':z['before_sha256'],'case_ids':z['case_ids'],'whole_owner_approval':False};ck(name+' exact proposal row '+k,row==expected);ck(name+' owner preimage/case continuity '+k,all(a.get(x)==z.get(x) for x in ['owner_path','before_sha256','case_ids','kind','destination_path']));bridge_checks.append({'bridge':name,'member_type':'proposal','key':k,'expected':expected,'actual_matches':row==expected})
  if a!=z:changed_proposals.append(k)
  if ab!=zb:changed_payloads.append(k)
 expected_cases=[44] if label=='s4' else [21,44,187];expected_props=[TARGET] if label=='s4' else [TARGET,CARB]
 ck(name+' exact changed cases',sorted(changed_cases)==expected_cases);ck(name+' exact changed payloads',set(changed_payloads)==set(expected_props));ck(name+' exact changed proposals',set(changed_proposals)==set(expected_props));bridge_summaries.append({'bridge':bind(S/name),'member_count':315,'changed_case_indices':changed_cases,'changed_payload_ids':changed_payloads,'changed_proposal_ids':changed_proposals})
# Selection and metadata files bind exactly the same final bytes.
sel=rd(S/'selection.json');handoff=rd(S/'HANDOFF.json');fin=rd(S/'finalization-binding.json');pair=rd(S/'native/saved-pair.json')
for n in final:ck('Selection core pointer '+n,resolve(sel['authoritative_core'][n+'.json'])==S/'final-core'/f'{n}.json');ck('Finalization same core '+n,fin['final_core'][n+'.json']==sel['authoritative_core'][n+'.json'])
ck('Selection rows match complete final proposals',len(sel['selected_payloads'])==127 and all(row=={k:p.get(k,p['owner_path'] if k=='destination_path' else None) for k in row} for row in sel['selected_payloads'] for p in [np[row['proposal_id']]]))
metadata=['selection.json','complete-bridge.json','combined-c9-bridge.json','finalization-binding.json','HANDOFF.json','native/saved-pair.json','subagent-scopes.json','issue-linked-correction.json']
for name in metadata:bindings(rd(S/name),name)
ck('Handoff expected frozen bytes',h((S/'HANDOFF.json').read_bytes())=='d5272a9fff4ad360bc098c1e8dc761a22c7b0be5c0d732a2580b831e275e5141' and h((S/'HANDOFF.md').read_bytes())=='53e02f17e5221f7ac55d565845b2d50ade6efb2fe12fd72369b14cc590344a8a')
expectedcounts={'cases':188,'unique_occurrences':304,'proposal_ids':127,'changed_payloads_since_s4':1,'byte_identical_other_payloads_since_s4':126,'unchanged_complete_case_objects_since_s4':187,'source_outcomes_changed':0,'changed_payloads_since_c9':2,'unchanged_complete_case_objects_since_c9':185,'prior_evidence_objects_exact':1206,'evidence_objects':1212,'current_retirements':0};ck('Handoff/count accounting exact',handoff['accounting']==rd(S/'accounting.json')==expectedcounts)
ck('No application/blanket transfer in final metadata',sel['approval'] is False and handoff['maintained_application_or_export_approval'] is False and handoff['carbonate_successor']['fresh_approval_from_this_successor'] is False and handoff['native_review']['owner_role_export_approval'] is False)
# Canonical native pair parity, actual evidence/inputs, exact selector and narrow attribution.
yp=R/'reviews/structured'/RID/'review.yaml';mp=yp.with_suffix('.md');native=yaml.safe_load(yp.read_text());md=mp.read_text();bindings(native['source']['inputs'],'native inputs')
ck('Native pair exactly selected by handoff',pair==handoff['native_review']);ck('Native rendered embedded YAML exact object',yaml.safe_load(md.split('```yaml\n',1)[1].rsplit('```',1)[0])==native)
spec=importlib.util.spec_from_file_location('record_review',R/'scripts/record_review.py');module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);ck('Canonical renderer exact Markdown parity',module.render_markdown(native)==md)
for e in native['evidence']:ck('Native evidence actual '+e['evidence_id'],h((R/e['reference']).read_bytes())==e['snapshot_sha256'])
ck('Native exact targets and selector',native['scope']['population_size']==2 and native['scope']['reviewed_target_ids']==['PROPOSAL:'+TARGET,cid] and native['targets'][0]['path']==str(resolve(np[TARGET]['after_capture']).relative_to(R)) and native['targets'][1]['path']==str((S/'final-core/decisions.json').relative_to(R)) and native['targets'][1]['selector']=='$.decisions[44]' and final['decisions']['decisions'][44]['case_id']==cid)
ck('Native self-review attribution and narrow completed verdict',native['reviewer']['independence']=='self_review' and 'prior serum authorship' in native['reviewer']['independence_basis'] and native['completion']=='completed' and native['verdict']=='pass_with_limitations' and native['scientific_review'] is True and native['findings']==[] and native['actions']==[])
ck('Native timing historical base and limits',native['source']['git_revision']==BASE and native['source']['state']=='working_tree' and native['started_at']==rd(S/'preflight.json')['at'].replace('+00:00','Z') and 'exact start is unknown' in ' '.join(native['limitations']) and 'corrected explanation only' in ' '.join(native['limitations']))
# Read root validation receipts; this independent metadata review does not rerun broad gates.
val=rd(S/'validation/narrow-native.json');struct=rd(S/'structural-audit.json');nc=rd(S/'native-check-command.json');nout=rd(S/'native-check.stdout')
ck('Native narrow actual completed receipt',val['status']=='PASS' and not val['closed_schema_errors'] and val['guarded_scratch_roundtrip_byte_exact'] and all(x['records']==3037 and x['violations']==[] for x in val['partonomy'].values()) and val['native_alias_projection_equal'] and val['native_mapping_projection_before']==val['native_mapping_projection_after'] and val['whole_owner_source_role_export_approval'] is False)
ck('Structural exact denominator/status',struct['structural_accounting']=='PASS' and struct['accounted_case_count']==188 and struct['proposal_count']==127 and struct['evidence_count']==1212 and struct['scientific_adequacy_or_approval_established'] is False)
ck('Full native check exact successful receipt',nc['exit_code']==0 and nout==handoff['native_complete_review_check']=={'repository':'CultureBotAI/MediaIngredientMech','valid_reviews':1027,'coverage':'declared_scopes_only'})
ck('Native check stderr only known deprecation',(S/'native-check.stderr').read_text().strip()=='topClass is deprecated - use top_class')
# Recheck all frozen previous report/source/owner/native files byte-for-byte.
preservation=[]
for category,items in pres.items():
 for item in items:
  path=pathlib.Path(item['path']);path=path if path.is_absolute() else R/path;actual=h(path.read_bytes()) if path.is_file() else None;ok=actual==item['sha256'];ck('Preserved '+category+':'+item['path'],ok);preservation.append({'category':category,'path':item['path'],'expected_sha256':item['sha256'],'actual_sha256':actual,'pass':ok})
for item in nativebase['tracked_canonical_review_files']:ck('Preserved canonical native '+item['path'],h((R/item['path']).read_bytes())==item['sha256'])
head=run(['git','rev-parse','HEAD']).decode().strip();status=run(['git','status','--porcelain=v1','--untracked-files=all']).decode();ck('Published predecessor HEAD unchanged',head==BASE)
statusrows=[{'status':line[:2],'path':line[3:]} for line in status.splitlines()];ck('Only new allowed successor/native artifacts visible',all(x['status'] in ['??','A '] and (x['path'].startswith(str(S.relative_to(R))+'/') or x['path'].startswith('reviews/structured/'+RID+'/')) for x in statusrows),statusrows)
# Exact manual metadata assessment is distinct from automated equality checks and primary science.
manual=[{'topic':'Scope and independence','assessment':'Read complete native YAML/Markdown and HANDOFF JSON/Markdown. Root is explicitly self-review author/assembler; separate skeptic is author-independent but disclosed original finder/prior reviewer. This reviewer previously authored serum/buffer work and performs retention only. No scientific renewal of those bytes or new whole-owner/role/export authority.'},{'topic':'Historical selection text','assessment':'Selection retains S4 carbonate two_case_successor/completeness context, explicitly links previous authoritative S4 selection and adds the bounded S5 wording marker. HANDOFF and combined c9 bridge distinguish the retained prior carbonate correction from the only new S5 calf change. Historical S4 metadata correction and selection-v2 remain authoritative and unmodified.'},{'topic':'Time and publication','assessment':'Native start is expressly an earliest recorded preflight milestone, with unknown earlier reading start; end is assembly completion. Local evidence read times do not overwrite original primary retrieval timestamps. Final handoff requires later seal/publication and exact private completion receipt; it does not claim approval of a future published head.'},{'topic':'Limits and routing','assessment':'Both calf and carbonate remain bounded unapplied proposals. Existing source/owner/role/export holds, pure-carbonate alias rejection, ISP4 and all source occurrence routing remain intact. No inherited W09 c9 approval is transferred. Root remains responsible for final published-head and integration assessment.'}]
failed=[x for x in checks if not x['pass']]
private=P/'final-assembly-checks-v1.json';dump(private,{'script_started_at':started,'script_completed_at':now(),'script_runtime_seconds':time.monotonic()-tick,'commands':commands,'checks':checks,'delta_author_to_final':deltas,'bridge_summaries':bridge_summaries,'bridge_member_checks':bridge_checks,'payload_checks':payloads,'evidence_capture_checks':capturechecks,'preservation_checks':preservation,'c9_git_baseline_copies':gitsupport,'git_status':statusrows})
support=[]
for src in [pathlib.Path(__file__).resolve(),private]:
 dst=O/'support'/src.name;ck('Support destination new '+str(dst),not dst.exists());shutil.copyfile(src,dst);support.append({'original':bind(src),'published':bind(dst),'byte_exact':src.read_bytes()==dst.read_bytes()})
failed=[x for x in checks if not x['pass']]
report={'schema_version':1,'reviewer':'Codex /root/buffers_research','verdict':'pass_with_limitations' if not failed else 'findings_open','findings':failed,'scope':'Independent exhaustive final-core retention, both 315-member bridges, actual selected/evidence bytes, canonical native pair and final handoff metadata. No fresh primary-science reassessment or future-head acceptance.','independence':'Independent of root-authored calf correction and wrapper. Prior buffer and serum authorship and broad integration reviews are disclosed; retained authored content receives byte comparison only. Target scientific correction is separately reviewed by preparation_skeptic, whose actual prior-finder involvement remains disclosed.','scientific_review':False,'actual_review_start_exact':None,'timing_note':'Final metadata reading began before the script; exact start was not recorded. Script times below measure the mechanical audit only, not full reading or previous author-core review.','script_started_at':started,'script_completed_at':now(),'script_runtime_seconds':time.monotonic()-tick,'review_completed_at':now(),'predecessor_head_observed':head,'counts':{**expectedcounts,'bridges':2,'members_per_bridge':315,'native_source_inputs':len(native['source']['inputs']),'native_evidence_entries':len(native['evidence']),'old_artifact_files':len(pres['old_artifact_files']),'old_s4_files':len(pres['old_s4_files']),'maintained_owner_files':len(pres['maintained_owner_files']),'source_snapshot_files':len(pres['source_snapshot_files']),'prior_canonical_review_files':len(nativebase['tracked_canonical_review_files']),'checks':len(checks)},'input_bindings':[bind(S/x) for x in metadata+['HANDOFF.md','author-freeze.json','reviews/retention/author-core-retention-review-v1.json','reviews/skeptic/scientific-review-v1.json','validation/narrow-native.json','native-check-command.json','native-check.stdout','native-check.stderr','structural-audit.json']]+[bind(S/'final-core'/f'{n}.json') for n in final]+[bind(yp),bind(mp)],'author_to_final_delta_pointers':{k:[x['pointer'] for x in v] for k,v in deltas.items()},'bridge_assessment':bridge_summaries,'manual_metadata_assessments':manual,'native_receipt_disposition':'Full native check read as successful exit0/1027 declared scopes only, one deprecation notice. Narrow validation read as two3037-record overlays with no violations, exact guarded byte roundtrip and unchanged native projections. These receipts are inspected, not broadly rerun by this reviewer.','retained_sentinels':base['sentinels'],'support_copies':support,'limitations':['Only final working-tree artifacts at these exact hashes are bound. No future commit/head/remote or final manifest is approved.','Root must preserve these bytes through final sealing and assess the published head separately.','No maintained application, owner merge, source mutation, export, paid research or Git/GitHub mutation is authorized or performed by this review.'],'approval':{'fresh_science':False,'whole_owner':False,'role':False,'export':False,'maintained_application':False,'future_published_head':False}}
dump(REPORT,report)
(REPORT.with_suffix('.md')).write_text('Independent final assembly metadata review: **'+report['verdict']+'**.\n\nAll 127 selected proposals, 188 cases and 304 unique occurrences remain accounted for. Both 315-member bridges match independently read source objects; the S4 bridge changes only calf44, while the c9 bridge records the retained carbonate and new calf payloads with cases21,44,187. All 126 other S4 payloads and 187 other complete decisions remain exact. Finalization changes only scoped reviewer/validation dependencies and status.\n\nAll 1212 evidence captures and selected payload hashes were checked. The old 2623 artifact files,147 S4 files,2956 owner files,244 source snapshots and2052 canonical review files remain exact. Native YAML/Markdown agree, with two exact targets,36 source inputs and6 evidence bindings. The full native receipt reports exit0 and1027 valid declared-scope reviews.\n\nComplete handoff/native wording preserves actual authorship, narrow calf explanation scope, unchanged carbonate scope, timing limits and all owner/role/export holds. Prior serum/buffer authorship is disclosed; this review provides no renewed science or future-head approval. Root retains publication and integration responsibility. Exact checks, runtime and commands are in the bound support receipt.\n')
print(json.dumps({'verdict':report['verdict'],'report':bind(REPORT),'checks':len(checks),'findings':failed},indent=2))
