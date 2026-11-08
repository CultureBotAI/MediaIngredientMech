"""Compile attributed scientific reviews into the unchanged native review contract."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,copy,hashlib,importlib.util,json,yaml
W=Path.cwd();S=W/'.temp/w05-final-correction-v1';B=W/'reports/all_unmatched_20261107/worker-05';P=B/'final-correction-v1'
ap=argparse.ArgumentParser();ap.add_argument('--review-bindings',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args()
out=a.out;out.mkdir(parents=True,exist_ok=False)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
objsha=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
put=lambda n,x:(out/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
R=json.loads(a.review_bindings.read_text())
review_data={k:json.loads((W/v['path']).read_text()) for k,v in R.items()}
for k,v in R.items():assert sha(W/v['path'])==v['sha256']
D=json.loads((P/'core/decisions.json').read_text())['decisions'];PS=json.loads((P/'core/proposals.json').read_text())['proposals']
L=json.loads((P/'core/proposal-lineage.json').read_text())['rows'];receipt=json.loads((P/'core/assembly-receipt.json').read_text())
original=yaml.safe_load((P/'inputs/external-w08-review/native/review.yaml').read_text())
lineage={x['proposal_id']:x for x in L};stable={p['proposal_id']:lineage[p['proposal_id']]['predecessor_proposal_id'] or p['proposal_id'] for p in PS}
targets=[];assessments=[];case_target={};all_peer_checks=[]
for i,d in enumerate(D):
 tid=f'CASE-{i+1:03d}';case_target[d['case_id']]=tid;lane=receipt['case_lane'][d['case_id']]
 peer=next(x for x in review_data[lane]['case_reviews'] if x['case_id']==d['case_id'])
 assert peer['case_input_sha256']==d['case_input_sha256']
 exact_peer=peer.get('selected_decision_object_sha256',peer.get('decision_object_sha256'))
 expected=d['final_assembly_provenance']['selected_decision_object_sha256']
 assert exact_peer is not None and exact_peer==expected,(lane,d['case_id'],exact_peer,expected)
 targets.append(dict(target_id=tid,path=str((P/'core/decisions.json').relative_to(W)),label=d['source']['raw_source_label'] or d['case_id'],kind='snapshot_row',
   record_class='SourceCaseDisposition',selector=d['case_id'],ownership_note='Exact frozen source-case scope; report-only successor, no maintained owner application or source/export approval.'))
 assessments.append(dict(assessment_id='A-'+tid,area='identity',topic='Exact source disposition and primary applicability',
   outcome='concern' if d.get('missing_requirement') else 'supported',summary=peer['assessment'],target_ids=[tid],evidence_ids=[R[lane]['evidence_id']],
   details='Attributed independent reviewer: '+R[lane]['reviewer']+'. Full exact review entry: '+json.dumps(peer,sort_keys=True,ensure_ascii=False)+'. Review completion does not release inherited source, role, owner or export holds.'))
 all_peer_checks.append(dict(target_id=tid,lane=lane,reviewer=R[lane]['reviewer'],exact_source_hash=d['case_input_sha256'],fragment_decision_hash=expected))
for p in PS:
 pid=p['proposal_id'];tid=stable[pid];lane=receipt['proposal_lane'][pid];peer=next(x for x in review_data[lane]['payload_reviews'] if x['proposal_id']==pid)
 capture=peer.get('after_capture') or peer.get('selected_after_capture') or peer.get('lineage',{}).get('after_capture')
 assert capture and capture['sha256']==p['after_capture']['sha256'],(pid,'peer binding missing/different')
 path=B/p['after_capture']['path'];assert sha(path)==p['after_capture']['sha256'];record=yaml.safe_load(path.read_text())
 paths=[dict(repository='CultureBotAI/MediaIngredientMech',path=p['owner_path'],role='Authentic proposal owner continuity; no maintained application.')]
 if p.get('destination_owner_path') and p['destination_owner_path']!=p['owner_path']:
  paths.append(dict(repository='CultureBotAI/MediaIngredientMech',path=p['destination_owner_path'],role='Proposed promoted destination only; no maintained write.'))
 targets.append(dict(target_id=tid,path=str(path.relative_to(W)),label=record['preferred_term'],kind='source',record_class='IngredientRecord',
  selector='Entire selected payload, all fields and retained limits; current proposal ID '+pid,owner_paths=paths))
 assessments.append(dict(assessment_id='A-P-'+str(len(assessments)+1),area='identity',topic='Complete isolated payload, supplied form, components, provenance and inherited limits',
  outcome='concern' if p.get('integration_disposition')=='PENDING_COORDINATOR_FAMILY_DECISION' else 'supported',summary=peer['assessment'],
  target_ids=[tid],evidence_ids=[R[lane]['evidence_id']],details='Attributed independent reviewer: '+R[lane]['reviewer']+'. Full exact review entry: '+json.dumps(peer,sort_keys=True,ensure_ascii=False)+'. This is not whole-owner, role or export approval.'))
 all_peer_checks.append(dict(target_id=tid,current_proposal_id=pid,lane=lane,reviewer=R[lane]['reviewer'],selected_capture=p['after_capture']))
alltargets=[t['target_id'] for t in targets]
assert len(alltargets)==len(set(alltargets))==len(D)+len(PS)
evidence=[]
for lane,r in R.items():
 evidence.append(dict(evidence_id=r['evidence_id'],kind='prior_review',reference=r['path'],accessed_at=r['completed_at'].replace('+00:00','Z'),support='supports',
  summary='Authorship-separated full disjoint scientific review, exact primary source applicability, complete candidate fields and source-specific limitations. No blanket owner or export approval.',snapshot_sha256=r['sha256']))
context=[('ORIGINAL-W08','prior_review',P/'inputs/external-w08-review/native/review.yaml','Exact original 18 findings, targets and issue lineage; preserved unchanged.'),
 ('FULL-NATIVE','validation',P/'validation/final-overlay/native-validation.json','All selected payload guarded/schema checks and complete path-keyed substitution, filenames and identifiers; structural evidence only.'),
 ('LINEAGE','validation',P/'validation/final-lineage.json','Exact original proposal ancestry, historical negatives/events and 103 provenance typing changes; not scientific renewal.'),
 ('ACCOUNTING','validation',P/'validation/final-structural-audit.json','Unchanged campaign outcome auditor exact 188 source cases and all candidate/evidence backlinks.'),
 ('ROWS','validation',P/'validation/final-native-row-replay.json','Complete isolated native rows with final overlay owner index; no generated export or downstream rebuild.'),
 ('CORRECTIONS','record_content',P/'finding-register.json','All original findings and separately attributed new findings, exact before-fix reproductions, issue routes, immutable fixes and independent rereviews.')]
finished=datetime.now(timezone.utc).replace(microsecond=0)
now=finished.strftime('%Y-%m-%dT%H:%M:%SZ');stamp=finished.strftime('%Y%m%dT%H%M%SZ')
for eid,kind,path,summary in context:
 evidence.append(dict(evidence_id=eid,kind=kind,reference=str(path.relative_to(W)),accessed_at=now,support='supports',summary=summary,snapshot_sha256=sha(path)))
register=json.loads((P/'finding-register.json').read_text());regs={f['finding_id']:f for f in register['original_findings']}
findings=[];actions=[]
for old in original['findings']:
 f=copy.deepcopy(old);fid=f['finding_id'];entry=regs[fid];lane='chemicals' if fid.startswith('W05-CR') else ('materials' if fid.startswith('W05-MAT-') else 'media')
 f['status']=entry['native_status'];f['disposition_reason']=entry['final_disposition']
 f['description']=old['description']+' Current successor assessment: '+entry['final_disposition']
 f['evidence_ids']=[R[lane]['evidence_id'],'CORRECTIONS','ORIGINAL-W08']
 f['previous_occurrences']=[dict(repository=original['repository'],review_id=original['review_id'],finding_id=fid)]
 f['external_issues']=list(dict.fromkeys(f.get('external_issues',[])+entry['issue_refs']))
 if fid=='W05-CR-F06':f['target_ids'].append('FINAL-CHEM-P-thiamine-dihydrate-cas')
 if fid=='W05-CR-F08':f['target_ids']+=['FINAL-CHEM-P-ki-stock-alias','FINAL-CHEM-P-ferric-stock-alias']
 if fid=='W05-CR-F02':f['target_ids']+=['R1193-P-wolfe1190','R1193-P-wolfe221']
 f['target_ids']=list(dict.fromkeys(f['target_ids']));assert set(f['target_ids'])<=set(alltargets)
 findings.append(f)
 if f['status']=='deferred':
  actions.append(dict(action_id='ACTION-'+fid,description=entry['remaining_prerequisite'],finding_ids=[fid],target_ids=f['target_ids'],
   owner_paths=f.get('owner_paths',[]),ownership_note='Coordinator owns reconciliation and any maintained application; this report selects no winning identifier.',
   acceptance_checks=['Obtain the exact missing formulation/source fact or choose a justified bounded nominal model with all origin/occurrence/component obligations.',
     'Independently review exact combined bytes; preserve source-specific uncertainty rather than infer equality or difference from omitted qualifiers.',
     'Revalidate native guarded schema, authentic owner continuity, full component/identifier dependencies and release holds before separate integration.']))
checks=[dict(check_id='CASE-PAYLOAD-SCIENCE',name='Three disjoint authorship-separated full scientific reviews',status='passed',required=True,
 summary='All 188 case scopes and every selected complete payload have an independently authored assessment and exact primary/candidate bindings.',target_ids=alltargets,evidence_ids=[r['evidence_id'] for r in R.values()]),
 dict(check_id='ACCOUNTING',name='Frozen source ownership and exact outcome accounting',status='passed',required=True,summary='Campaign native outcome auditor passes; full 1879 assignment boundaries retained.',target_ids=alltargets,evidence_ids=['ACCOUNTING','LINEAGE']),
 dict(check_id='SCHEMA-PARTONOMY',name='Guarded closed schema and full substituted baseline checks',status='passed',required=True,summary='All candidate guarded writes and full path overlay partonomy, filenames and no introduced identifier collision; structural pass is not owner approval.',target_ids=alltargets,evidence_ids=['FULL-NATIVE']),
 dict(check_id='NATIVE-ROWS',name='Four full native row projections',status='passed',required=True,summary='Tris salt and tellurium dioxide each preserve parent plus two exact registry rows; thiamine dihydrate false CAS removed while exact CHEBI row remains; monohydrate emits only its local registry identity.',target_ids=['CHEM-C1193-Tris-HCl-salt','CHEM-C1193-tellurium-dioxide','FINAL-CHEM-P-thiamine-dihydrate-cas','FINAL-CHEM-P-thiamine-hcl-monohydrate'],evidence_ids=['ROWS'])]
extra=[str((P/n).relative_to(W)) for n in ['core/evidence.json','core/proposals.json','core/proposal-lineage.json','finding-register.json']]
extra += [r['path'] for r in R.values()]+[str(path.relative_to(W)) for _,_,path,_ in context]
put('targets.json',dict(targets=targets))
spec=importlib.util.spec_from_file_location('native_record_review',W/'scripts/record_review.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
inspection=mod.inspect_source(W,targets,extra);put('inspection.json',inspection)
review=dict(schema_version='1.0.0',review_id=stamp+'-worker05-final-scientific-correction',kind='batch',repository='CultureBotAI/MediaIngredientMech',
 title='W05 full report-only scientific correction successor: 188 cases and exact final candidates',started_at='2026-11-08T07:28:00Z',finished_at=now,
 reviewer=dict(identity='Codex W05 /root, compiler and report-metadata author; disjoint independent scientists /root/materials_research (chemicals), /root/media_research (materials), /root/final_skeptical (media)',kind='agent',independence='self_review',
  independence_basis='The compiler is part of W05 and authored report metadata corrections. Scientific assessments are attributed verbatim to three disjoint reviewers who did not author their assigned successor payloads. Chemical reviewer independently delegated 28 source-case scopes/16 payload field sets to /root/materials_research/chemical_primary_crosscheck; the main reviewer owns full chemical review. Separate final assembly review follows. No claim that compiler self-review supplies independent chemical approval.'),
 skill='review-yaml-category; add-media; map-media-ingredients; review-sssom-output',completion='completed',verdict='needs_curation',scientific_review=True,
 summary='Complete successor review with exact original source/payload lineage and all 18 original finding IDs retained. Bounded corrections are supported in isolated candidates; four original finding scopes retain conditional family/alias prerequisites. Source, whole-owner, role and export approval remain separate.',
 source=inspection['source'],scope=dict(description='Full source-specific scientific decisions, complete selected payloads, primary applicability, supplied forms, aliases, partonomy, provenance and remaining identity facts.',
  selection='All 188 frozen W05 cases; every original 138 proposal retained through one-to-one successor lineage plus explicitly bounded existing-owner follow-ons and the source-supported monohydrate form candidate.',coverage='full',population_size=len(targets),reviewed_target_ids=alltargets),
 targets=targets,checks=checks,evidence=evidence,assessments=assessments,findings=findings,actions=actions,
 limitations=['No maintained ingredient, aggregate, export, schema, workflow, gate or pin changed. No downstream rebuild or release was performed.',
  'Conditional HEPES/Wolfe/ethanol scopes and six hydration-unspecified magnesium aliases remain unresolved as detailed; missing facts establish neither equivalence nor distinction.',
  'Peptone historical inbound references, current component coupling, shared-owner candidate unions and coordinator origin obligations remain separate integration work.',
  'Historical inherited evidence enums do not authenticate a human supplier. Claim-specific type correction does not renew scientific mapping approval.',
  'Native structural and row checks concern isolated candidate bytes; they do not constitute global owner, source-role or export approval.'],
 links=[str((P/'finding-register.json').relative_to(W)),str((P/'core/proposal-lineage.json').relative_to(W))])
mod.validate_review(review);mod.assert_current_source(W,review)
put('review-content.json',review);put('peer-binding-receipt.json',dict(targets=all_peer_checks,status='PASS',original_findings=len(findings),target_count=len(targets)))
print(json.dumps(dict(review_id=review['review_id'],targets=len(targets),findings=len(findings),verdict=review['verdict'])))
