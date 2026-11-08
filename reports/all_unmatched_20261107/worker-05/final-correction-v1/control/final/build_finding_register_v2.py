from pathlib import Path
from datetime import datetime,timezone
import argparse,copy,hashlib,json,yaml
W=Path.cwd();S=W/'.temp/w05-final-correction-v1';P=W/'reports/all_unmatched_20261107/worker-05/final-correction-v1'
ap=argparse.ArgumentParser();ap.add_argument('--review-bindings',type=Path,required=True);a=ap.parse_args()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
objsha=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
bindings=json.loads(a.review_bindings.read_text());reviews={k:json.loads((W/v['path']).read_text()) for k,v in bindings.items()}
original=yaml.safe_load((P/'inputs/external-w08-review/native/review.yaml').read_text())
author={}
for p,key in [(P/'chemicals/finding-dispositions-v3.json','findings'),(P/'materials/finding-dispositions.json','dispositions'),(P/'remediation/media-report-v2/finding-dispositions.json','findings')]:
 for row in json.loads(p.read_text())[key]:author[row['finding_id']]=dict(path=str(p.relative_to(W)),sha256=sha(p),entry=row)
routes={
 'W05-CR-F01':[1237,1193],'W05-CR-F02':[1237,1193],'W05-CR-F03':[1237,1193],
 'W05-CR-F04':[1180],'W05-CR-F05':[1193],'W05-CR-F06':[268],'W05-CR-F07':[1193],'W05-CR-F08':[1229,1230],
 'W05-MAT-001':[1212],'W05-MAT-002':[1236],'W05-MAT-003':[1193],'W05-MAT-004':[1176],
 'W05-MAT-005':[1193],'W05-MAT-006':[1193],'W05-MAT-007':[1193],
 'W05-MEDIA-F01':[1208],'W05-MEDIA-F02':[1193],'W05-MEDIA-F03':[1193]}
deferred={
 'W05-CR-F01':'The unsupported source-number/receiving-pH distinction is withdrawn. Two candidate captures remain alternatives under a conditional nominal HEPES-KOH model; no winning identifier or co-installation is authorized. Exact stock formulation/titration and source bridging, or a coordinator-defined common partial scope with all provenance, are prerequisites.',
 'W05-CR-F02':'Unsupported hydrate-omission distinctness is withdrawn. JCM470/DSM792 and the additional ATCC1190/JCM221 comparison remain conditional; absence of hydrate wording is not evidence of difference or equality. Recover exact supplied hydration/formulation or reconcile a bounded nominal preparation while retaining every raw form/quantity/processing/source lineage.',
 'W05-CR-F03':'Unsupported separation by source recipe number is withdrawn. The four 95% ethanol candidate captures preserve all17 occurrence routes but are not approved as four distinct identities or as a fully equivalent formulation. Concentration basis, carrier/denaturant and documented preparation/source bridges constrain a common nominal model; coordinator selects no arbitrary winner.',
 'W05-CR-F08':'The demonstrated literal/form and supplied-stock alias defects have bounded corrections. HEPES10mM is correctly retained as a weighed receiving dose. Six hydration-unspecified magnesium aliases remain historically preserved and conditionally unresolved: recover each exact original source/form before declaring a hydrate identity or rejecting it as different. No missing-hydration inference or source release follows.'}
rows=[]
for f in original['findings']:
 fid=f['finding_id'];lane='chemicals' if fid.startswith('W05-CR') else ('materials' if fid.startswith('W05-MAT-') else 'media')
 rv=reviews[lane];fr=rv.get('finding_dispositions',rv.get('original_finding_dispositions',[]))
 peer=next(x for x in fr if x['finding_id']==fid)
 assessment=peer.get('assessment') or peer.get('conclusion') or peer.get('resolution') or peer.get('disposition')
 assert isinstance(assessment,str) and assessment,(fid,'reviewer finding assessment missing')
 status='deferred' if fid in deferred else 'resolved'
 disposition=(deferred[fid] if fid in deferred else assessment)+ ' Bounded isolated-successor disposition only; all other source, owner, role, component-dependency and export holds remain. No GitHub issue was closed.'
 rows.append(dict(finding_id=fid,issue_key=f['issue_key'],original_review_id=original['review_id'],original_finding_object_sha256=objsha(f),
  original_target_ids=f['target_ids'],original_finding=f,author_correction=author[fid],independent_reviewer=bindings[lane]['reviewer'],
  independent_review=dict(path=bindings[lane]['path'],sha256=bindings[lane]['sha256'],entry=peer),native_status=status,
  final_disposition=disposition,remaining_prerequisite=deferred.get(fid,'No prerequisite remains for this bounded report correction. Separate maintained integration and inherited holds remain.'),
  issue_refs=[f'https://github.com/CultureBotAI/MediaIngredientMech/issues/{n}' for n in routes[fid]],
  optional_nonblocking=fid in ['W05-MAT-005','W05-MAT-006']))
newscience=[]
for name,issue in [('new-tellurium-grade-finding-v1.json','https://github.com/CultureBotAI/MediaIngredientMech/issues/1240'),
 ('new-hepes-components-finding-v1.json','https://github.com/CultureBotAI/MediaIngredientMech/issues/1237#issuecomment-6718873227'),
 ('new-tris-components-finding-v1.json','https://github.com/CultureBotAI/MediaIngredientMech/issues/1237#issuecomment-6718873227')]:
 p=P/'chemicals'/name;x=json.loads(p.read_text());newscience.append(dict(finding_id=x['finding_id'],original_reproduction=dict(path=str(p.relative_to(W)),sha256=sha(p)),
   issue_ref=issue,full_original_finding=x,independent_review=bindings['chemicals'],
   disposition='Exact successor independently reviewed; complete payload and native-row/partonomy obligations retained. This is not root integration or release approval.'))
p=P/'reviews/chemicals/finding-003-initial.json';x=json.loads(p.read_text())
newscience.append(dict(finding_id=x['finding_id'],original_reproduction=dict(path=str(p.relative_to(W)),sha256=sha(p)),
 issue_ref='https://github.com/CultureBotAI/MediaIngredientMech/issues/1193',full_original_finding=x,reported_to_coordinator_before_fix=True,
 independent_review=bindings['chemicals'],bounded_fix=dict(proposal_id='FINAL-CHEM-P-thiamine-hcl-monohydrate',
  source_case_count=2,occurrence_count=6,scope='One registry-only source-defined monohydrate material; no guessed CAS, formula, chloride stoichiometry or parent. All raw forms and source holds preserved.'),
 disposition='Feasible bounded local material curation completed after six primary NBRC recipe reads and duplicate-owner checks; exact new payload and both selected decisions independently rereviewed. No maintained application or export approval.'))
report_findings=[]
for lane,name in [('media','new-findings-v1.json'),('media','new-findings-v2.json'),('chemicals','finding-001-initial.json'),('chemicals','finding-002-initial.json'),('chemicals','finding-004-initial.json'),('chemicals','finding-005-initial.json'),('chemicals','finding-006-initial.json')]:
 p=P/'reviews'/lane/name;x=json.loads(p.read_text());items=x.get('findings',x.get('additional_findings',[x]))
 for item in items:
  report_findings.append(dict(finding_id=item['finding_id'],original_reproduction=dict(path=str(p.relative_to(W)),sha256=sha(p)),
   original_finding=item,reported_to_coordinator_before_fix=True,independent_review=bindings[lane],
   disposition='Corrected in the selected immutable report amendment and independently rereviewed. The earlier report and correct payload/source bytes remain preserved.'))
for sub,name in [('chemical-report-v1','assembly-finding-001.json'),('chemical-report-v2','assembly-finding-002.json')]:
 p=P/'remediation'/sub/name;x=json.loads(p.read_text());report_findings.append(dict(finding_id=x['finding_id'],original_reproduction=dict(path=str(p.relative_to(W)),sha256=sha(p)),
  original_finding=x,reported_to_coordinator_before_fix=True,independent_review=bindings['chemicals'],
  disposition='Bounded report-envelope correction independently rereviewed; unchanged native campaign auditor passes. No scientific identity, payload or gate changed.'))
p=P/'chemical-supplement-v1/binding-lineage-disposition-v1.json';x=json.loads(p.read_text())
report_findings.append(dict(finding_id=x['finding_id'],original_reproduction=dict(path=str(p.relative_to(W)),sha256=sha(p)),
 original_finding=x,reported_to_coordinator_before_fix=True,independent_review=bindings['chemicals'],
 disposition='Historical conclusion hashes retain their exact historical/serialization basis. The additive index binds every current selected chemical decision with one canonical algorithm; independently rereviewed. This dependent binding occurrence is deduplicated to ASSEMBLY002, with no source or payload change.'))
p=P/'remediation/assembly-report-v1/new-findings-v1.json';x=json.loads(p.read_text())
for item in x.get('findings',[x]):
 report_findings.append(dict(finding_id=item['finding_id'],original_reproduction=dict(path=str(p.relative_to(W)),sha256=sha(p)),
 original_finding=item,reported_to_coordinator_before_fix=True,deduplicate_to='W05-FINAL-SKEPTIC-CHEM-004',
 independent_review='Separate final assembly review exact-byte receipt under reviews/assembly',
 disposition='Corrected final README generator: eleven flat occurrences plus one DSMZ212a occurrence. Prior generator preserved. No payload, source route or scientific conclusion changed.'))
p=P/'remediation/assembly-report-v2/new-findings-v2.json';x=json.loads(p.read_text());x=x['additional_findings'][0]
report_findings.append(dict(finding_id=x['finding_id'],original_reproduction=dict(path=str(p.relative_to(W)),sha256=sha(p)),original_finding=x,
 reported_to_coordinator_before_fix=True,deduplicate_to='W05-CR-F06',independent_review='Separate final assembly review exact-byte receipt under reviews/assembly',
 disposition='Corrected final README description to CAS property/alias and projected other-token withdrawal, preserving exact CHEBI row. All earlier generators remain; no payload or projection changed.'))
assert len({r['finding_id'] for r in rows})==18
assert len({r['finding_id'] for r in report_findings})==len(report_findings)
out=P/'finding-register.json';assert not out.exists()
out.write_text(json.dumps(dict(at=datetime.now(timezone.utc).isoformat(),compiler='/root',original_findings=rows,
 new_scientific_findings=newscience,additional_filed_scope=dict(finding_id='W01-PREP-B-003',issue_ref='https://github.com/CultureBotAI/MediaIngredientMech/issues/1238',
  target_proposal_id='CHEM-C1193-Tris-HCl-salt',scope='Externally reported solid-salt parent-grade defect, separately corrected and independently reviewed; complete three-row native output verified.'),
 report_findings=report_findings,deduplication='CHEM006 is a second occurrence of the native disposition enum cause recorded in ASSEMBLY002; both exact reproductions remain. CHEM004/005 correct only the independent reviewer prose. Original18 IDs/issue keys/targets retained. NEW02/03 share a buffer partonomy cause but retain both IDs. Media attribution repetitions share MEDIA-REVIEW-01. These are report dispositions, not issue closures or source-owner/export approvals.',
 conditional_matrices=dict(path=str((P/'chemicals/conditional-family-matrix-v1.json').relative_to(W)),sha256=sha(P/'chemicals/conditional-family-matrix-v1.json')),
 source_and_owner_dependencies=dict(path=str((P/'materials/integration-dependencies.json').relative_to(W)),sha256=sha(P/'materials/integration-dependencies.json'))),indent=2,ensure_ascii=False)+'\n')
print(json.dumps(dict(original=len(rows),deferred=sum(r['native_status']=='deferred' for r in rows),new_scientific=len(newscience),report_findings=len(report_findings))))
