from pathlib import Path
import json,hashlib,datetime,subprocess,yaml,shlex,importlib.util
W=Path.cwd();C=W.parents[2];B=W/'reports/all_unmatched_20261107/worker-05';P=B/'buffer-parts-v1';Q=B/'dependency-route-a-confirmation-v1';S=W/'.temp/w05-dependency-route-a-confirmation-v1';R=S/'assembly-audit'
j=lambda p:json.loads(p.read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();oh=lambda v:hashlib.sha256(json.dumps(v,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
checks=[];bindings=[];manifest_checks=[]
def ck(n,v):
 assert v,n;checks.append(n)
def bind(p):
 r=dict(path=str(p.relative_to(W)) if p.is_relative_to(W) else str(p),sha256=sha(p));bindings.append(r);return r
def ref(r):
 p=W/r['path'];ck('exact reference '+r['path'],sha(p)==r['sha256']);return p
def manifest(p):
 m=j(p);members=m.get('members',m.get('files'));assert isinstance(members,list)
 for r in members:ck('manifest member '+str(p)+' '+r['path'],sha(p.parent/r['path'])==r['sha256'])
 for r in m.get('native_review',[]):ref(r)
 manifest_checks.append(dict(**bind(p),members=len(members),native_pair_members=len(m.get('native_review',[]))))
prior=j(R/'source-lineage-preservation-v1.json');prepub=j(R/'public-selector-and-receipts-v1.json')
for r in prior['manifest_verification']:manifest(Path(r['path']))
for r in prepub['public_artifacts']:ref(r)
sel=j(Q/'selector.json');ps=j(P/'core/proposals.json')['proposals'];pi={p['proposal_id']:p for p in ps};ds=j(P/'core/decisions.json')['decisions'];deps={p['proposal_id']:p for p in sel['dependency_proposals']}
for p in ps:ck('all155 selected payload exact '+p['proposal_id'],sha(B/p['after_capture']['path'])==p['after_capture']['sha256'])
ck('all188 cases155 proposals138lineages',len(ds)==188 and len(ps)==155 and j(P/'core/proposal-lineage.json')['original_count']==138 and len(deps)==15)
for r in prior['shards']:ck('all frozen campaign shards preserved '+r['shard'],sha(Path(r['path']))==r['sha256'])
ck('all1879 ownership count',sum(r['cases'] for r in prior['shards'])==1879)
inv=j(W/'.temp/w05-final-correction-v1/control/maintained-baseline-preservation-start.json');ck('full maintained filename set preserved',{str(f.relative_to(W)) for f in (W/'data/ingredients').rglob('*.yaml')}=={r['path'] for r in inv['records']})
for r in inv['records']:ref(r)
manifest(Q/'review/FINAL-MANIFEST-v1.json');manifest(Q/'ambiguous-audit/MANIFEST.json')
for lane in ['generic-audit','ambiguous-audit','review']:
 source={str(f.relative_to(S/lane)):f for f in (S/lane).rglob('*') if f.is_file()};copied={str(f.relative_to(Q/lane)):f for f in (Q/lane).rglob('*') if f.is_file()};ck('complete public science lane '+lane,set(source)==set(copied))
 for name,p in source.items():ck('exact scientist public copy '+lane+'/'+name,sha(p)==sha(copied[name]))
peer=j(Q/'review/main-review.json');pri={r['proposal_id']:r for r in peer['payload_reviews']};ck('actual separate peer and complete scope',peer['reviewer']=='/root/final_skeptical' and set(pri)==set(deps) and len(peer['case_reviews'])==3 and len(peer['all20_claim_reviews'])==20 and not peer['findings'] and peer['source_owner_export_approval'] is False)
ck('actual disjoint primary authors',{r['identity'] for r in peer['primary_authors']}=={'/root/buffer_hepes','/root/buffer_tris'})
for pid,r in pri.items():ck('full exact scientific reviewed object '+pid,r['after_capture']==pi[pid]['after_capture'] and r['selected_proposal_object_sha256']==oh(pi[pid]) and r['complete_payload_content_read'] is True and r['new_payload_required'] is False and r['source_owner_export_approval'] is False)
native=j(Q/'native-review-preparation/review-content.json');rid=native['review_id'];N=W/'reviews/structured'/rid;saved=yaml.safe_load((N/'review.yaml').read_text());spec=importlib.util.spec_from_file_location('native_review',W/'scripts/record_review.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);mod.validate_review(saved);mod.assert_current_source(W,saved);ck('native saved YAML equals content',saved==native);ck('native markdown is exact renderer',(N/'review.md').read_text()==mod.render_markdown(saved));ck('scope exact15 native targets',len(native['targets'])==15 and {t['target_id'] for t in native['targets']}==set(deps) and set(native['scope']['reviewed_target_ids'])==set(deps));ck('native wrapper self-review truthfully attributed',native['reviewer']['independence']=='self_review' and '/root/final_skeptical' in native['reviewer']['identity'] and native['verdict']=='needs_curation' and not native['findings'] and not native['actions'])
for t in native['targets']:ck('native exact target path '+t['target_id'],W/t['path']==B/deps[t['target_id']]['after_capture']['path'])
for a in native['assessments']:
 pid=a['target_ids'][0];d=json.loads(a['details']);ck('native exact current peer summary and condition '+pid,a['summary']==pri[pid]['assessment'] and d['remaining_source_prerequisite']==pri[pid]['missing_fact_or_application_condition'] and d['after_capture']==pri[pid]['after_capture'] and d['authentic_before']==pri[pid]['before_sha256'] and d['causal_not_observed_recipe'] is True)
for e in native['evidence']:ck('native evidence snapshot '+e['evidence_id'],sha(W/e['reference'])==e['snapshot_sha256'])
for r in native['source']['inputs']:ref(r)
for check in native['checks']:
 if check['check_id']=='SCIENCE':ck('science is separate noncommand evidence','command' not in check and check['evidence_ids']==['PEER'])
 else:
  mapping={'OVERLAY':'full-overlay','STRICT':'strict-dependencies','ACCOUNTING':'exact-accounting','LINEAGE':'lineage'};r=j(Q/'validation'/f"{mapping[check['check_id']]}.receipt.json");ck('native actual command '+check['check_id'],check['command']==shlex.join(r['command']) and check['exit_code']==r['exit_code']==0)
for stem in ['native-content-validation','native-save']:
 r=j(Q/'validation'/f'{stem}.receipt.json');ck('native completed command '+stem,r['exit_code']==0 and bool(r['command']));bind(Q/'validation'/f'{stem}.receipt.json')
head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip();ck('source HEAD still108e before publication',head==sel['source_head']=='108e213e96f7d423ee345ce265d692e79063127c')
allowed=[str(Q.relative_to(W))+'/',str(N.relative_to(W))+'/'];staged_raw=subprocess.check_output(['git','diff','--cached','--name-status','-z']).decode().split('\0');staged=[]
for ix in range(0,len(staged_raw)-1,2):
 status,path=staged_raw[ix:ix+2];ck('only additive authorized staged report '+path,status=='A' and any(path.startswith(prefix) for prefix in allowed));ck('index exact current report byte '+path,hashlib.sha256(subprocess.check_output(['git','show',':'+path])).hexdigest()==sha(W/path));staged.append(dict(status=status,path=path,sha256=sha(W/path)))
ck('no unstaged tracked edits',not subprocess.check_output(['git','diff','--name-only'],text=True).strip())
for p in [R/'source-lineage-preservation-v1.json',R/'public-selector-and-receipts-v1.json',Q/'selector.json',Q/'source-scope-ledger.json',Q/'README.md',Q/'review/main-review.json',Q/'review/reference-wrapper-review-v1.json',Q/'native-review-preparation/review-content.json',Q/'control/build_native_review_v2.py',N/'review.yaml',N/'review.md']:bind(p)
x=dict(at=datetime.datetime.now(datetime.timezone.utc).isoformat(),reviewer='/root/assembly_audit',status='PASS_FINAL_MECHANICAL_WRAPPER_PENDING_GLOBAL_NATIVE_GATE',scope='Independent exact-byte assembly, lineage, source-accounting and native-wrapper mechanical review. Scientific findings and approval remain authored by separately named scientists/reviewer; no new chemistry or release approval.',source_head=head,counts=dict(cases188=188,proposals155=155,original_lineages138=138,campaign_cases1879=1879,maintained_records2956=len(inv['records']),route_A_existing_payloads15=15,science_packet_members21=21,native_targets15=15),native_review_id=rid,bindings=bindings,preserved_manifests=manifest_checks,checks=checks,check_count=len(checks),staging_at_review=staged,staging_limit='Snapshot before final root manifest/staging/publication; final staging must remain under the same additive report/native-pair whitelist.',findings=[],scope_limits=['Original188 cases and138 original lineages remain in the full155 predecessor core; source snapshots/captures are unchanged.','All15 route-A proposals already existed at108e; no child recipes or cases were invented.','Marine agar2216/PYGS/TOGO M2491 remain other-origin coordinator dependencies, not W05 fixed claims.','Historical precise_remaining_requirement is preserved with original attribution; current native assessments use fresh peer summaries/conditions.','Owner/role/source-case/export application remains unapproved and whole-owner historical findings are not closed.','Fresh global retained-review check and later independent science-wrapper addendum require their exact separate receipts; outer manifest not yet sealed.'],ignored_files_included=True)
f=R/'final-wrapper-mechanical-v1.json';assert not f.exists();f.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n');print(json.dumps(dict(status=x['status'],checks=len(checks),sha256=sha(f))))
