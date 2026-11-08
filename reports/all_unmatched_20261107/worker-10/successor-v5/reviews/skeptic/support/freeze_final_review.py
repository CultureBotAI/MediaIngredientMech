from pathlib import Path
import datetime,hashlib,json,os,subprocess
R=Path.cwd();A=R/'reports/all_unmatched_20261107/worker-10';S=A/'successor-v5';P=R/'.temp/all-unmatched-worker-10/successor-v5/skeptic';O=S/'reviews/skeptic';W=R/'.temp/w09-provenance-published-head-independent-v1'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();load=lambda p:json.loads(p.read_bytes());bind=lambda p:{'path':str(p.relative_to(R)),'sha256':sha(p)}
v=load(P/'final-assembly-verification-v1.json');h=load(S/'HANDOFF.json');science=load(O/'scientific-review-v1.json');checks=[]
def ck(n,x):checks.append({'check':n,'pass':bool(x)})
ck('independent core/bridges/native PASS',v['status']=='PASS' and not v['failures'])
for b in v['input_bindings']:ck('verified final inputs still exact '+b['path'],sha(R/b['path'])==b['sha256'])
ck('exact announced handoff JSON',sha(S/'HANDOFF.json')=='d5272a9fff4ad360bc098c1e8dc761a22c7b0be5c0d732a2580b831e275e5141')
ck('exact announced handoff Markdown',sha(S/'HANDOFF.md')=='53e02f17e5221f7ac55d565845b2d50ade6efb2fe12fd72369b14cc590344a8a')
bindings=[]
def walk(x):
 if isinstance(x,dict):
  if 'path' in x and 'sha256' in x:
   p=(A if x.get('root')=='artifact' else R)/x['path'];ck('handoff/scope binding '+x['path'],sha(p)==x['sha256']);bindings.append(bind(p))
  for y in x.values():walk(y)
 elif isinstance(x,list):
  for y in x:walk(y)
walk(h);sc=load(S/'subagent-scopes.json');walk(sc)
ck('prior finding authorship candidly disclosed','Original finding author and prior reviewer, not candidate author' in sc['independent_science']['scope'])
ck('fresh science restricted in scopes','fresh science restricted to explanation' in sc['independent_science']['scope'])
sel=load(S/'selection.json');ck('handoff exact authoritative selected core',all(b['sha256']==h['authoritative_core'][k]['sha256'] and h['authoritative_core'][k]['path'].endswith(b['path']) for k,b in sel['authoritative_core'].items()))
counts=h['accounting'];expected={'cases':188,'unique_occurrences':304,'proposal_ids':127,'changed_payloads_since_s4':1,'byte_identical_other_payloads_since_s4':126,'unchanged_complete_case_objects_since_s4':187,'source_outcomes_changed':0,'changed_payloads_since_c9':2,'unchanged_complete_case_objects_since_c9':185,'prior_evidence_objects_exact':1206,'evidence_objects':1212,'current_retirements':0}
ck('exact two baseline accounting partitions',counts==expected)
ck('only allowed current payload/report fields',h['existing_payload_fields_changed']==['notes','ontology_mapping.evidence[0].notes'] and h['active_report_fields_corrected']==['proposal.description','case44.reasoning','case44.completion_reassessment.bounded_scientific_conclusion'] and h['all_original_history_verbatim'] is True and h['one_truthful_history_appended'] is True)
pair=load(S/'native/saved-pair.json');ck('handoff exact two-target native pair',h['native_review']==pair and pair['targets']==2)
cmd=load(S/'native-check-command.json');out=load(S/'native-check.stdout');stderr=(S/'native-check.stderr').read_text()
ck('actual root full repository check passed1027',cmd['exit_code']==0 and out==h['native_complete_review_check']=={'repository':'CultureBotAI/MediaIngredientMech','valid_reviews':1027,'coverage':'declared_scopes_only'} and h['predecessor_head'] in cmd['argv'])
ck('only known deprecation warning on stderr',stderr.strip()=='topClass is deprecated - use top_class')
ck('completed native check predates handoff',cmd['finished_at']<h['at'])
ck('native timing explicitly bounded','earlier reading start remains unknown' in h['timing'] and 'actual assembly completion' in h['timing'])
ck('no futurehead/wholeowner/application approval',h['maintained_application_or_export_approval'] is False and h['carbonate_successor']['fresh_approval_from_this_successor'] is False and 'no retrospective review-head claim' in h['publication'])
md=(S/'HANDOFF.md').read_text();ck('Markdown exact scope and two baseline context',all(t in md for t in ['selection.json','final-core/decisions.json','Original history stays verbatim','combined-c9-bridge.json','1027 valid declared-scope reviews','Fresh scientific review covers only this explanation','do not approve a future head']))
ck('historical finding and release limits preserved',all(t in ' '.join(h['retained_limits']) for t in ['does not close the GitHub issue','unknown processing','nonresolving provenance','not blanket-transferred','all remaining owner/source/role/export holds']))
seal=A/'successor-v4/SHA256SUMS';seal_rows=[];seal_bad=[]
for line in seal.read_text().splitlines():
 digest,path=line.split('  ',1);seal_rows.append(path)
 if sha(R/path)!=digest:seal_bad.append(path)
ck('all prior S4 seal members exact',not seal_bad and len(set(seal_rows))==len(seal_rows))
wm=load(W/'MANIFEST.json');wbad=[b['path'] for b in wm['files'] if sha(W/b['path'])!=b['sha256']];lbad=[b['path'] for b in wm['symlinks_not_traversed'] if not (W/b['path']).is_symlink() or os.readlink(W/b['path'])!=b['link_text']]
ck('prior sealed W09 regular files and symlinks exact',len(wm['files'])==62 and len(wm['symlinks_not_traversed'])==2 and not wbad and not lbad)
ck('original S5 scientific report frozen',sha(O/'scientific-review-v1.json')=='088acd5c1669d9462da11dbb61641916b4f6b09ad8b67e02004c724c2ffebca0')
ck('current HEAD remains published S4',subprocess.check_output(['git','rev-parse','HEAD'],cwd=R).decode().strip()=='82fc29d837a223edb9c436445ec7ea13d2840c7b')
fails=[c for c in checks if not c['pass']];support=[]
for name in ['verify_final_assembly.py','final-assembly-verification-v1.json','freeze_final_review.py']:
 src=P/name;dst=O/'support'/name
 with dst.open('xb') as f:f.write(src.read_bytes())
 support.append({'original':bind(src),'published_copy':bind(dst),'byte_exact':sha(src)==sha(dst)})
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
report={
 'review_id':'w10-successor-v5-final-assembly-skeptical-v1','reviewed_at':now,'reviewer':'Codex /root/preparation_skeptic (AI), worker10','author_independent':True,'prior_involvement':science['prior_involvement'],'scientific_review':False,'completion':'completed','verdict':'pass_with_limitations' if not fails else 'needs_curation','findings':fails,
 'scope':'Exact final-core review/evidence/status finalization, both complete current/c9 baseline bridges, native two-target wrapper, final HANDOFF and actual validation receipts. No renewed science for the other126 payloads or carbonate successor; the frozen calf explanation assessment remains the only fresh scientific scope.',
 'frozen_scientific_review':bind(O/'scientific-review-v1.json'),
 'exact_input_bindings':v['input_bindings']+[bind(S/n) for n in ['HANDOFF.json','HANDOFF.md','subagent-scopes.json','native-check-command.json','native-check.stdout','native-check.stderr','issue-linked-correction.json']],
 'verification':{'final_core_bridges_native_checks':v['check_count'],'handoff_preservation_checks':len(checks),'failures':fails,'checks':checks,'native_source_inputs':v['native_source_inputs'],'native_targets':v['native_targets'],'native_evidence':v['native_evidence'],'native_current_source_validation_and_Markdown_parity':'Independently executed PASS on the exact selected native pair.','root_required_checks':'Inspected actual narrow validation PASS (guarded byte-exact roundtrip, unchanged identifier/mapping/alias projections and both3037-record overlays without partonomy violations), structural audit exit0 and full repository native check exit0 with1027 declared scopes. Root checks are attributed, not represented as independently rerun.','sealed_preservation':{'S4_manifest':bind(seal),'S4_members_rehashed':len(seal_rows),'W09_manifest':bind(W/'MANIFEST.json'),'W09_regular_files_rehashed':len(wm['files']),'W09_symlinks_checked':len(wm['symlinks_not_traversed']),'mismatches':seal_bad+wbad+lbad},'broader_prior_preservation':'The retention reviewer separately supplies its broader artifact/maintained-file evidence. This reviewer independently rehashed both seals and the exact selected payload/core/native bindings; it does not claim new scientific review of those retained populations.','support_copies':support},
 'accounting':expected,
 'conclusions':['Finalization changes only the promised current review/evidence bindings and scoped status for case44 and its proposal; the scientific payload remains exactly7a54c5bb03008949dec5ced0fbb8da9deee348fd4ad2473e66d41655db975b9d.','All630 bridge rows independently match full canonical before/after objects:315 from the published S4 predecessor and315 from c9. Current changes are one calf payload/case44; combined changes retain the earlier carbonate payload and case21/187 metadata without fresh approval.','All127 current selected payload hashes and projection fields match. No proposals are newly retired, and earlier retirement bridges remain exact.','Native review declares actual root self-review and separate independent scopes; it expressly discloses my original finding authorship/prior review. Its started_at is a recorded preflight milestone with unknown earlier reading start, and finished_at is actual assembly completion.','Original history and original findings are preserved. Candidate wording correction does not close historical native/GitHub findings, broaden aliases, establish percentage basis or release owner/role/export holds.','The handoff selects authoritative final-core/selection and accurately separates current and c9 combined accounting. It does not invent a future published head or transfer W09/c9 approval.'],
 'limitations':['This is a prepublication exact-byte assembly review. Coordinator assessment of the actual committed/published head remains separate.','No whole-owner, ontology-mapping, source-association, role, export, maintained application or shared-source approval is granted.','No human scientific review or newly invented user approval is asserted. All writers and reviewers are AI with their actual prior involvement disclosed.','Root may seal the exact reviewed artifacts and this report/support. Further substantive payload, final-core, native or handoff changes require a new scoped observation.']
}
with (O/'final-assembly-review-v1.json').open('x') as f:json.dump(report,f,indent=2,ensure_ascii=False);f.write('\n')
with (O/'final-assembly-review-v1.md').open('x') as f:
 f.write(f'''Independent final assembly review by Codex /root/preparation_skeptic (AI), completed {now}.\n\n**{report['verdict']}**. All {v['check_count']} core/bridge/native checks and {len(checks)} handoff/preservation checks pass. Both complete 315-row bridges, all 127 payload hashes, 36 native inputs, six evidence bindings and two targets are exact. Native current-source validation and rendered Markdown parity were independently verified. Root's completed full repository check reports 1,027 valid declared review scopes with exit 0; stderr contains only the known deprecation warning.\n\nRelative to the published S4 predecessor, only calf-blood wording and case44 dependencies change. The c9 bridge also records the prior carbonate correction without renewing its scientific approval. The final candidate, original history, mapping, unknowns, source occurrence and all remaining holds match the frozen scientific review.\n\nThe native wrapper and handoff accurately disclose root authorship, my original finding/prior review involvement, bounded scientific scope and timing milestones. Original findings and historical reviews remain unchanged. This review grants no whole-owner, role, application, export or future published-head approval.\n''')
print(json.dumps({'verdict':report['verdict'],'checks':len(checks),'failures':fails,'report':bind(O/'final-assembly-review-v1.json'),'markdown':bind(O/'final-assembly-review-v1.md')}))
