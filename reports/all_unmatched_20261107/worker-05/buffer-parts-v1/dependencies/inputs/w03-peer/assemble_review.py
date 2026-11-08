"""Assemble source-review accounting only; never write an ingredient candidate."""
from pathlib import Path
import json,hashlib,datetime,sys,collections,csv
R=Path.cwd();O=R/'.temp/peptone-consumer-independent-v1';sha=lambda b:hashlib.sha256(b).hexdigest()
def load(p):return json.loads(p.read_text())
def put(p,x):
 with p.open('x') as f:json.dump(x,f,indent=2,ensure_ascii=False);f.write('\n')
def cap(p):return {'path':str(p.relative_to(R)),'sha256':sha(p.read_bytes())}
skeptic_path=Path(sys.argv[1]).resolve(strict=True);native_handoff=Path(sys.argv[2]).resolve(strict=True)
assert skeptic_path.is_relative_to(O) and native_handoff.is_relative_to(O)
source_paths=[O/'ambiguous/per-claim-scientific-ledger.json',O/'other/per-claim-assessment.json']
source_docs=[load(p) for p in source_paths]
sources={r['claim_key']:(r,p,doc['reviewer']) for p,doc in zip(source_paths,source_docs) for r in doc['claims']}
skeptic_doc=load(skeptic_path);skeptics={r['claim_key']:r for r in skeptic_doc['claims']}
claims=load(O/'context/claims-20.json');owners={r['claim_key']:r for r in load(O/'context/owner-bindings-20.json')};routes={r['claim_key']:r for r in load(O/'route-and-composition-v2.json')['rows']}
keys={r['claim_key'] for r in claims};assert len(keys)==20 and set(sources)==set(skeptics)==set(owners)==set(routes)==keys
rows=[]
for c in claims:
 key=c['claim_key'];source,source_path,author=sources[key];owner=owners[key]
 d=source['scientific_disposition']
 if d.startswith('GENERIC_PEPTONE_SUPPORTED'):
  category='CONDITIONAL_GENERIC_REFERENCE';target='kgmicrobe.ingredient:peptone';action=source['bounded_recommendation'];hold='Final accepted generic owner and exact consumer composition/application phase are required; supplier details are not a prerequisite for this genuinely generic part.'
 elif d=='SOURCE_SPECIFIC_BACTO_PEPTONE_CONFIRMED':
  category='RETAIN_SOURCE_SPECIFIC_BACTO';target='MICRO:0000178';action=source['bounded_recommendation'];hold='Keep source-specific Bacto distinction; no whole Bacto owner, role or export approval.'
 elif d=='GENERIC_WORDING_WITH_EXISTING_UNMAPPED_PRODUCT_WITHDRAWAL':
  category='PRESERVE_EXISTING_MARINE_WITHDRAWAL';target=None;action=source['bounded_recommendation'];hold='W03 alias proposal is author-related; exact combined product payload remains separately reviewed. Preserve W05 withdrawal and nominal reconstitution scope.'
 else:
  assert d=='HOLD_EXACT_COMPONENT_IDENTITY_WITH_REVIEWED_MINIMAL_WITHDRAWAL'
  category='UNRESOLVED_IDENTITY_WITHDRAW_RESOLVING_ID';target=None;action=source['minimal_withdrawal_recommendation'];hold=source['precise_unresolved_fact']
 rows.append({'target_id':c['review_target_id'],'claim_key':key,'beforeimage_binding':owner,'original_plan_disposition':c['disposition'],'scientific_disposition':category,'recommended_reference_id':target,'bounded_recommendation':action,'precise_remaining_requirement':hold,'scientific_unknowns':source.get('remaining_unknowns',[]),'occurrence_bound_support':source.get('supported_occurrence_limit'),'primary_reviewer':author,'primary_assessment_receipt':cap(source_path),'primary_assessment':source,'separate_skeptical_assessment':skeptics[key],'source_origin_and_composition_route':routes[key],'worker03_author_related':key=='data/ingredients/mapped/Marine_Broth_2216.yaml#components[0]','future_exact_child_payload_review_required':True,'candidate_created_or_edited':False,'whole_owner_form_role_or_export_approval':False})
counts=collections.Counter(r['scientific_disposition'] for r in rows)
assert counts=={'CONDITIONAL_GENERIC_REFERENCE':8,'UNRESOLVED_IDENTITY_WITHDRAW_RESOLVING_ID':10,'RETAIN_SOURCE_SPECIFIC_BACTO':1,'PRESERVE_EXISTING_MARINE_WITHDRAWAL':1}
put(O/'machine-ledger.json',{'schema_version':1,'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'All20 peptone component claims; source-specific scientific recommendations and separately skeptical assessment, not final child-candidate or whole-owner acceptance.','head_preserved':'fe31a02850932a7bdf2fe65c93cb636a86f82a2c','claim_count':20,'counts':dict(counts),'rows':rows,'primary_packets':[cap(p) for p in source_paths],'separate_skeptic':cap(skeptic_path),'native_review_handoff':cap(native_handoff),'new_confirmed_findings':cap(O/'ambiguous/confirmed-findings.json'),'causal_case':cap(O/'context/authentic-causal-case.json'),'route':cap(O/'route-and-composition-v2.json'),'source_holds_preserved':True,'native_structural_pass_is_science_proof':False,'all_candidate_acceptance_withheld':True})
with (O/'claim-table.tsv').open('x',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(['target_id','claim_key','before_sha256','disposition','recommended_reference_id','primary_reviewer','precise_remaining_requirement'])
 for r in rows:w.writerow([r['target_id'],r['claim_key'],r['beforeimage_binding']['before_sha256'] or 'NULL_NEW_OWNER',r['scientific_disposition'],r['recommended_reference_id'] or 'UNMAPPED',r['primary_reviewer'],r['precise_remaining_requirement']])
lines=['# Peptone component source review','','All20 claims have a primary-source assessment and a separate skeptical assessment. This supports bounded child-authoring decisions; no final candidate, whole-owner, form, role or export approval is supplied.','','| Claim | Source disposition | Remaining requirement |','|---|---|---|']
for r in rows:
 label=r['claim_key'].replace('data/ingredients/mapped/','').replace('.yaml','');lines.append('| '+label+' | '+r['scientific_disposition']+' | '+r['precise_remaining_requirement'].replace('|','/')+' |')
lines+=['','The eight generic recommendations do not require supplier or digest details. They do require the exact accepted generic target and final consumer payloads in a reviewed application phase. The ten withdrawals retain the current component text as historical interpretation; they do not turn PY/PYG abbreviations into observed ingredient names.','',
'PY-cellobiose has positive occurrence-level generic support for Eubacterium siraeum, but its separate Clostridium polysaccharolyticum observation remains unresolved. PYG accounts for114 source observations; a single recipe cannot approve that aggregate.','',
'PEPTONE-SOURCE-001 is a newly confirmed source-attribution conflict: Falsen2005 reports Fastidious Anaerobe Broth (Oxoid), while the inherited current assertion uses LabM/Neogen. Exact historical composition remains unresolved. Separate Anaerobe Systems PYG tests cannot supply FAB constituents. The coordinator must deduplicate/file the finding before any source correction. No fix was applied.','',
'Fastidious must compose with its meat-granule withdrawal; PY-glucose-rumen and PYG_Rumen must compose with literal rumen fluid UNMAPPED repairs under204/1204. W05 may use its real generic-peptone causal case for authentic child edits; it must not claim the child recipes were observed in that case. No child origin was manufactured here.','',
'The W03 Marine alias payload retains the old reference. W05 and the combined Marine product candidate supply the UNMAPPED withdrawal. Those versions remain distinct and the W03 origin is author-related.','',
'Original sources, exact capture hashes, access failures, partial reading limits and retained unknown timestamps are recorded in the two primary packets. Raw source bytes and web-tool extractions are distinguished; unread publisher PDFs or manual recipes are not represented as inspected.','']
with (O/'ASSESSMENT.md').open('x') as f:f.write('\n'.join(lines))
finding=load(O/'ambiguous/confirmed-findings.json')['findings'];assert len(finding)==1
put(O/'issue-suggestion-dedup.json',{'finding_id':finding[0]['finding_id'],'finding_capture':cap(O/'ambiguous/confirmed-findings.json'),'status':'CONFIRMED_SOURCE_FINDING_REPORTED_BEFORE_FIX_COORDINATOR_DEDUP_PENDING','existing_related_trackers':finding[0]['dedup_context'],'new_issue_created':False,'github_mutation':False,'fix_applied':False,'routing':'Coordinator determines whether to append to1176/1193 or file a distinct source-attribution issue. W03 does not apply or direct W05 edits.','exact_reproduction_and_bounded_fix':finding[0]})
print(json.dumps({'claims':len(rows),'dispositions':dict(counts),'new_confirmed_findings':1,'machine_ledger_sha256':sha((O/'machine-ledger.json').read_bytes())},indent=2))
