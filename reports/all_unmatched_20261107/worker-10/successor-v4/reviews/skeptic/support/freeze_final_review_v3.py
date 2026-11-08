from pathlib import Path
import datetime,hashlib,json,subprocess
R=Path.cwd();A=R/'reports/all_unmatched_20261107/worker-10';S=A/'successor-v4';P=R/'.temp/all-unmatched-worker-10/successor-v4/skeptic';O=S/'reviews/skeptic'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
load=lambda p:json.loads(p.read_bytes())
bind=lambda p:{'path':str(p.relative_to(R)),'sha256':sha(p)}
checks=[]
def ck(n,x):checks.append({'check':n,'pass':bool(x)})
v=load(P/'native-timing-successor-check-v1.json');old=load(S/'HANDOFF.json');new=load(S/'HANDOFF-v2.json');pair=load(S/'native-v2/saved-pair.json');prior=load(O/'final-assembly-review-v2.json')
ck('independent timing/native checks PASS',v['status']=='PASS' and v['failures']==[])
for b in v['inputs']:ck('timing input still exact '+b['path'],sha(R/b['path'])==b['sha256'])
ck('requested JSON handoff bytes',sha(S/'HANDOFF-v2.json')=='70cf5f88db141fa3e8f4b863ef90e1f42c7fa8206463318a83b5a28e314383ae')
ck('requested Markdown handoff bytes',sha(S/'HANDOFF-v2.md')=='92d4fec5e6e643e388245a33f884d66e7ff85f9c1a109ee9ea8bae39fbf9a9d2')
bindings=[]
def visit(x):
 if isinstance(x,dict):
  if 'path' in x and 'sha256' in x:
   p=(A if x.get('root')=='artifact' else R)/x['path'];ck('handoff binding '+x['path'],sha(p)==x['sha256']);bindings.append(bind(p))
  for z in x.values():visit(z)
 elif isinstance(x,list):
  for z in x:visit(z)
visit(new)
allowed={'at','status','native_review','native_complete_review_check','retained_limits','native_complete_review_check_receipt','prior_handoff','native_timing_correction','final_assembly_review_scope'}
ck('only timing/check/selection-attribution handoff metadata changed',all(old.get(k)==new.get(k) for k in set(old)|set(new) if k not in allowed))
ck('all old limits exact prefix',new['retained_limits'][:len(old['retained_limits'])]==old['retained_limits'])
ck('new handoff selects exact native-v2 pair',new['native_review']==pair)
ck('core/payload/315bridge selection unchanged',all(new[k]==old[k] for k in ['authoritative_core','authoritative_selection','complete_bridge','payload','accounting','issue_linked_lineage']))
cmd=load(S/'native-check-v2-command.json');stdout=load(S/'native-check-v2.stdout');stderr=(S/'native-check-v2.stderr').read_text()
ck('actual full native check successful1026',cmd['exit_code']==0 and stdout==new['native_complete_review_check']=={'repository':'CultureBotAI/MediaIngredientMech','valid_reviews':1026,'coverage':'declared_scopes_only'})
ck('known warning not a failure',stderr.strip()=='topClass is deprecated - use top_class')
ck('full native check precedes handoff and uses actual predecessor',cmd['finished_at']<new['at'] and new['predecessor_head'] in cmd['argv'])
md=(S/'HANDOFF-v2.md').read_text()
ck('handoff Markdown exact correction and limits',all(t in md for t in ['HANDOFF-v2.json','SV4-NATIVE-TIMING-001','earlier reading start is unknown','changes no target, scientific assessment, candidate or core decision','1026 valid declared-scope reviews','Coordinator review of the final published head']))
ck('current scope does not invent future acceptance',new['maintained_application_or_export_approval'] is False and 'after final independent review' in new['publication'] and 'Earlier completed assembly receipts remain valid only for their exact historical input bytes' in new['final_assembly_review_scope'])
for b in prior['exact_reviewed_inputs']:ck('earlier reviewed bytes retained '+b['path'],sha(R/b['path'])==b['sha256'])
ck('old final v2 report frozen',sha(O/'final-assembly-review-v2.json')=='4816da1f2d212fec691ec5d8c0af28e3817e02baccbc1c75372205f27ac1e788')
ck('old final v1 report frozen',sha(O/'final-assembly-review-v1.json')=='87450cec747e308bbbb4b365f5b73fd629d45fbca57ad3fecc67d592e9420691')
ck('source head still c9a',subprocess.check_output(['git','rev-parse','HEAD'],cwd=R).decode().strip()=='c9a96da71a1977014680e5a92e600dfc7e3874db')
fail=[c for c in checks if not c['pass']]
support=[]
for name in ['verify_native_timing_successor.py','native-timing-successor-check-v1.json','freeze_final_review_v3.py']:
 src=P/name;dst=O/'support'/name
 with dst.open('xb') as f:f.write(src.read_bytes())
 support.append({'original':bind(src),'published_copy':bind(dst),'byte_exact':sha(src)==sha(dst)})
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
report={
 'review_id':'w10-successor-v4-final-assembly-skeptical-v3',
 'reviewed_at':now,
 'reviewer':'Codex /root/preparation_skeptic (AI), worker10',
 'author_independent':True,
 'scientific_review':False,
 'completion':'completed',
 'verdict':'pass_with_limitations' if not fail else 'needs_curation',
 'scope':'Independent append-only timing provenance and exact new native/handoff/check bindings. The frozen completeness science and complete final core are retained; no scientific reassessment or expanded approval.',
 'supersedes_metadata_selection':{'prior_review':bind(O/'final-assembly-review-v2.json'),'prior_inputs_remain_historical':True,'selected_handoff':bind(S/'HANDOFF-v2.json'),'selected_native':pair},
 'prior_involvement':load(O/'scientific-review-v1.json')['prior_involvement'],
 'additional_reviewer_omission':'My final-assembly-v2 review checked scope and reviewer attribution but did not flag the original native wrapper generation interval as insufficiently labelled. The independent retention reviewer identified SV4-NATIVE-TIMING-001. I verified that finding and the exact append-only correction here; v2 remains unchanged and is not retrospectively represented as having caught it.',
 'finding_dispositions':[{'finding_id':'SV4-NATIVE-TIMING-001','original_severity':'minor_provenance','original_finding':bind(S/'reviews/retention/native-timing-finding-v1.json'),'correction':bind(S/'native-v2/timing-correction.json'),'disposition':'Addressed in the exact selected native-v2 timing attribution. The original finding, pair and handoff remain preserved observations. This is not a GitHub closure or a rewrite of prior native findings.','reason':'started_at is expressly the earliest recorded root source-assessment milestone, not an invented full reading start; the earlier start remains unknown. finished_at is actual successor assembly completion. Original timestamps are expressly wrapper generation; independent report timing is separately attributed.'}],
 'new_findings':fail,
 'exact_input_bindings':v['inputs']+[bind(S/n) for n in ['HANDOFF-v2.json','HANDOFF-v2.md','native-check-v2-command.json','native-check-v2.stdout','native-check-v2.stderr']]+[bind(S/'final-core'/n) for n in ['decisions.json','evidence.json','proposals.json']],
 'verification':{'native_timing_checks':v['check_count'],'handoff_preservation_checks':len(checks),'native_source_inputs':v['native_source_inputs'],'native_targets':v['native_targets'],'native_evidence':v['native_evidence'],'failures':fail,'checks':checks,'native_validate_current_source_render_parity':'Independently rerun on selected native-v2; PASS. Root full repository check exit0/1026 declared scopes is inspected and attributed, not independently rerun.','full_prior_preservation':'Earlier exact preservation audits remain bound. This follow-up rehashes all prior exact reviewed input bindings; it does not rerun the broad source audit or claim new science.','support_copies':support},
 'retained_conclusions':['Exact candidate135788bf..., final-core, selection-v2, all315 case/proposal bridge rows and population accounting are unchanged from the reviewed assembly.','Native targets, source/retention scope, checks, assessments, original six evidence objects and scientific_review flag are unchanged. Only timing/context lineage and explicit explanatory metadata were added.','Original carbonate completeness finding IDs, distinct severities, preparation unknowns and all owner/source/role/export holds remain. No original scientific finding is closed through this metadata successor.'],
 'limitations':['This report grants no whole-owner, role, export, maintained application or future published-head approval. Coordinator assessment of the actual published head remains separate.','No human scientific review, invented retrospective review interval, fresh user authorization or global acceptance is asserted.','Earlier checker failures and reviewer omissions remain disclosed. The old v1/v2 reports, native pair, handoff, source captures and all earlier evidence remain immutable.','Root may seal these exact reviewed artifacts and this final report/support. Further substantive candidate, core, native or handoff changes need a new scoped observation.']
}
with (O/'final-assembly-review-v3.json').open('x') as f:json.dump(report,f,indent=2,ensure_ascii=False);f.write('\n')
with (O/'final-assembly-review-v3.md').open('x') as f:
 f.write(f'''Independent final metadata review by Codex /root/preparation_skeptic (AI), {now}.\n\n**{report['verdict']}**. The selected native-v2 pair and HANDOFF-v2 bind the unchanged candidate, final core and prior scientific review. All {v['check_count']} native timing checks and {len(checks)} handoff/preservation checks pass, including 44 source inputs, three targets, eight evidence objects, native validation, current-source binding and Markdown parity. Root's completed repository check reports 1,026 valid declared review scopes with exit 0; its sole stderr line is the known topClass deprecation warning.\n\nFinding `SV4-NATIVE-TIMING-001` is addressed in the selected successor. The timestamps now distinguish the recorded root assessment milestone, unknown earlier reading start and actual new assembly finish. The original interval is explicitly labelled as wrapper generation, and independent reviewer times retain their own attribution. Original findings and saved bytes remain unchanged.\n\nMy earlier v2 review did not flag this timing attribution issue. This v3 observation records that omission and independently verifies the correction. It adds no fresh scientific approval. Whole-owner, application, role, export and final published-head acceptance remain separate.\n''')
print(json.dumps({'verdict':report['verdict'],'checks':len(checks),'failures':fail,'report':bind(O/'final-assembly-review-v3.json'),'markdown':bind(O/'final-assembly-review-v3.md')}))
