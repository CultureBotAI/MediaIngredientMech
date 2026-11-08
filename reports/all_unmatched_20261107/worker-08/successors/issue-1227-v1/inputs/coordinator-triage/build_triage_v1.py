from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,csv
D=Path(__file__).resolve().parent;C=D.parent.parent;P=C/'workers/w03/worktree/.temp/w08-published-head-independent-review-v1';S=D/'snapshot';R=P/'input-snapshot/reports/all_unmatched_20261107/worker-08'
def sha(b):return hashlib.sha256(b).hexdigest()
def save(n,x):
 p=D/n
 if p.exists():raise RuntimeError('Occupied '+str(p))
 p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
A=json.loads((S/'assessment.json').read_text());F=json.loads((S/'findings.json').read_text())['finding_groups'];T=json.loads((D/'target-verification-v1.json').read_text());assert T['status']=='PASS';props={p['proposal_id']:p for p in A['proposal_accounting']};cases={p['case_id']:p for p in A['case_accounting']}
issuefile=C/'preflight/root-integration-findings-v1/issue1226-readback-v1.json';(D/'issue1226-root-live-readback.json').write_bytes(issuefile.read_bytes());assert json.loads(issuefile.read_text())['number']==1226
complete={'if1201-new-pcr_s11_50mm_nah2po4','if1201-new-pcr_s11_50mm_na2hpo4','if1201-new-allen_m2231_phosphate_stock','if1201-new-mediadive_552_thiosulfate_5g_100ml','if1201-new-jcm_941_solution_c'}
part=json.loads((S/'final/partial-completeness-adjudication.json').read_text());refined=[]
for r in part['rows']:
 p=r['proposal_id'];new={**r,'root_triage_reviewer':'/root/step7d_science_c','root_triage_scope':'Bounded enum advice for literal source-input lists; no final candidate or scientific approval.'}
 if p in complete:
  new.update(root_triage_recommendation='COMPLETE_FOR_LITERAL_PRINTED_INPUT_LIST',root_triage_reason='The cited stock-preparation table/instruction explicitly enumerates the two inputs, and the payload retains both. Unresolved chemical form does not imply unknown membership. Scope COMPLETE to this literal source preparation; do not claim finished molecular composition, final volume, unreported additives or chemistry. Preserve all form/source holds. This refines the external reviewer UNKNOWN recommendation, without disputing its diagnosis that PARTIAL is unsupported.')
 elif r['adjudication']=='confirmed_enum_correction':new.update(root_triage_recommendation='UNKNOWN',root_triage_reason='Agree for this source-limited assertion: the record does not establish complete membership, and no explicit missing constituent justifies PARTIAL. Preserve documented amounts/form uncertainty; no guessed carrier.')
 else:new.update(root_triage_recommendation='KEEP_OUT_OF_AUTOMATIC_ENUM_CHANGE',root_triage_reason='Retain separate assessment of explicitly omitted malformed inputs or pH/CO2 treatment; this triage does not approve a guessed titrant or gas has-part. The two YPS lists actually omit named source inputs. PCR buffer and JCM628/629 need the precise assertion boundary retained.')
 refined.append(new)
save('completeness-adjudication-refinement.json',{'reviewed_head':A['reviewed_head'],'native_contract':{'schema_path':'src/mediaingredientmech/schema/mediaingredientmech.yaml','lines':[774,1520,1529,1533,1535,1537],'schema_sha256':sha((P/'input-snapshot/src/mediaingredientmech/schema/mediaingredientmech.yaml').read_bytes()),'semantics':'Source-relative membership, independent of concentration, molecular form and final volume.'},'counts':{'reviewed_PARTIAL':34,'supported_change_scope':29,'recommend_UNKNOWN':24,'recommend_COMPLETE_for_explicit_two_input_recipe':5,'excluded_from_automatic_change':5},'rows':refined})
# Retain exact source subsections behind the refinement, including the original frozen recipe witness.
texts={r['proposal_id']:r for r in json.loads((S/'final/partial-source-texts.json').read_text())};proof=[]
for pid in sorted(complete):
 r=next(v for v in part['rows'] if v['proposal_id']==pid);item={'proposal_id':pid,'payload':props[pid]['after_capture'],'anchors':r['primary_anchors'],'source_subsections':[]}
 for e in texts[pid]['sources']:
  t=e.get('text','')
  try:j=json.loads(t)
  except json.JSONDecodeError:j=None
  if isinstance(j,dict) and 'components' in j:
   token='K2HPO4' if 'allen' in pid else ('NaH2PO4' if 'nah2' in pid else 'Na2HPO4')
   sub=[q for q in j['components'] if token.lower() in q.get('subcomponent_name','').lower()]
   item['source_subsections'].append({'url':e['url'],'capture':e['capture'],'subcomponents':sub,'comments':[q for q in j.get('comments',[]) if any(w in q.get('comment','').lower() for w in ['prepare two','monosodium','disodium'])]})
  elif isinstance(j,dict) and 'data' in j and isinstance(j['data'],dict) and 'recipe' in j['data']:
   item['source_subsections'].append({'url':e['url'],'capture':e['capture'],'exact_data':j['data']})
  elif 'jcm_941' in pid and 'Solution C:' in t:
   s=t.index('Solution C:');z=t.find('Solution D:',s);item['source_subsections'].append({'url':e['url'],'capture':e['capture'],'literal_subsection':t[s:z]})
 for anchor in r['primary_anchors']:
  if 'source_row' in anchor:
   b=Path(anchor['path']).read_bytes();assert sha(b)==anchor['sha256'];src=json.loads(b)
   def contains(v,w):
    if v==w:return True
    if isinstance(v,dict):return any(contains(a,w) for a in v.values())
    if isinstance(v,list):return any(contains(a,w) for a in v)
    return False
   assert contains(src,anchor['source_row']);item['source_subsections'].append({'source_row':anchor['source_row'],'source_path':anchor['path'],'sha256':anchor['sha256'],'exact_row_verified_in_frozen_shard':True})
 proof.append(item)
save('complete-list-primary-proof.json',proof)
route={
'001':('1226','Existing cross-campaign mapping-evidence issue; confirmed root readback copied. Do not create a duplicate or replace the different ComponentEvidenceTypeEnum token.'),
'002':('NEW_W08_FINDING_TRACKER','1173 is Worker01 publication lineage and718 is a broad backlog; neither should silently become the tracker for these two W08 pointer-owning payloads.'),
'003':('1201','Append the exact32-payload component follow-up under existing authorized-curation completion issue. Catalog duplicates and withheld roles do not mean an active entity cannot be referenced.'),
'004':('1201','Append these two existing-owner preparation/product promotions under existing incomplete-curation scope; no unknown B12 vitamer or unsupported finished-medium ingredients may be inferred.'),
'005':('NEW_W08_FINDING_TRACKER','1217 is Worker06-specific and1167 concerns atmosphere versus has-part. Link their concepts as context without pretending either currently tracks this NBRC1356 derived-water assertion.'),
'006':('NEW_W08_FINDING_TRACKER','Preserve29 exact affected assertions plus5 exclusions. Do not prescribe blanket UNKNOWN; use the independent five-recipe COMPLETE refinement.'),
'007':('NEW_W08_FINDING_TRACKER','No exact nalidixic source-applicability issue was found in the inspected all-state body inventory; comments were only targeted. Root should perform final live dedup before filing.'),
'008':('811','Existing811 explicitly covers generic Potassium phosphate on CHEBI63036; add exact malformed KH2HPO4/K2HPO/KH PO full-payload scope. Preserve1215 concentration fixes and1216 separate molybdate scope.'),
'009':('NEW_W08_FINDING_TRACKER','317 is a closed historical synonym-grading batch, not evidence that this new proposal is corrected. Exact primary synonym supports identity; change the quality only as justified.'),
'010':('1210','Existing1210 is the same CAS7783-13-3 substantive primary-evidence binding issue. Add W08 batch6→batch7 evidence repair and all three affected case backlinks there.'),
'011':('NEW_W08_FINDING_TRACKER','Bounded source-disposition wording correction; keep the real seven-water uncertainty and separate resolved dose/stock distinction.'),
'012':('NEW_W08_FINDING_TRACKER','Exact NCIT L-hydrate issue not found in inspected all-state bodies.1117 is closed and covers carbonate/maltose, not this owner. Requires exact-term priority review and dependent references; no SMILES stereochemistry invention.')}
triage=[]
for f in F:
 k=f['finding_id'][-3:];r,note=route[k];q={**f,'coordinator_triage':'SUPPORTED_FINDING_WITH_BOUNDED_FIX','issue_route_recommendation':r,'dedup_reason':note,'affected_targets':[{k:p[k] for k in ['proposal_id','owner_path','kind','before_sha256','after_capture','case_ids','review_receipt','review_receipt_sha256']} for p in (props[x] for x in f['proposal_ids'])],'direct_source_cases':[{'case_id':x,'index':cases[x]['index'],'case_input_sha256':cases[x]['case_input_sha256'],'occurrence_ids':cases[x]['occurrence_ids'],'published_missing_requirement':cases[x]['published_missing_requirement']} for x in f['direct_source_case_ids']]}
 if k=='006':q['coordinator_triage']='SUPPORTED_PARTIAL_MISUSE_WITH_SOURCE_SPECIFIC_ENUM_REFINEMENT';q['coordinator_fix_refinement']='See completeness-adjudication-refinement.json:24 UNKNOWN,5 COMPLETE for complete literal two-input recipe,5 exclusions.'
 if k=='003':q['coordinator_fix_refinement']='The43 explicit B component pairs were independently bound to exact active baseline records and selected component indexes; all are MAPPED. A supplies15 candidate records; C supplies seven detailed Hutner candidate assessments and retains Metals44 unresolved. These are source-specific candidates, not blanket permission to ground ambiguous B12/pantothenate/hydrates.'
 triage.append(q)
save('actionable-findings-matrix.json',{'reviewed_head':A['reviewed_head'],'at':datetime.now(timezone.utc).isoformat(),'status':'AUTHOR_CORRECTIONS_REQUIRED','reviewer_packet_manifest_sha256':json.loads((D/'manifest-verification.json').read_text())['manifest_sha256'],'counts':T['counts'],'findings':triage,'remaining_approval':'All corrected candidate bytes require authorship-separated full successor review. No data/application/role/export/merge approval.'})
rows=[]
for p in A['proposal_accounting']:
 ids=p['payload_findings'];rows.append({**p,'action_rows':[{'finding_id':i,'issue_route':route[i[-3:]][0],'required_action':next(f['proposed_bounded_fix'] for f in F if f['finding_id']==i),'completeness_override':next((r['root_triage_recommendation'] for r in refined if r['proposal_id']==p['proposal_id']),None)} for i in ids]})
save('all113-payload-action-matrix.json',rows)
with (D/'all113-payload-action-matrix.tsv').open('w') as out:
 w=csv.writer(out,delimiter='\t');w.writerow(['proposal_id','owner_path','before_sha256','after_sha256','case_ids','finding_ids','issue_routes','planning_disposition'])
 for p in rows:w.writerow([p['proposal_id'],p['owner_path'],p['before_sha256'] or '',p['after_capture']['sha256'],'|'.join(p['case_ids']),'|'.join(p['payload_findings']),'|'.join(dict.fromkeys(route[i[-3:]][0] for i in p['payload_findings'])),p['complete_payload_planning_disposition']])
summary=['# W08 exact-head finding triage','','Exact reviewed head: `'+A['reviewed_head']+'`. All5,070 review-manifest members were rehashed, with exact membership and no mismatch. All113 selected payloads were independently compared to their committed Git bytes and original beforeimages. No source data was edited.','','The twelve finding groups are actionable. The94 affected payloads are a union, not94 chemical refutations:88 payloads need95 truthful mapping-evidence provenance corrections tracked by1226. Nine source dispositions/evidence bindings need correction. Eighteen payloads retain bounded planning acceptance; the shared W03 owner still requires separate coordinator acceptance.','','| Finding | Scope | Suggested issue route |','|---|---|---|']
for f in triage:summary.append('| '+f['finding_id']+' | '+f['title']+' ('+str(len(f['proposal_ids']))+' payloads) | '+f['issue_route_recommendation']+' |')
summary+=['','The confirmed completeness defect is misuse of PARTIAL, not permission to change every assertion to UNKNOWN. I recommend UNKNOWN for24 uncertain lists; COMPLETE for the five literal two-input preparations whose source tables/instructions and payloads explicitly retain both inputs; and separate treatment of the five excluded assertions. These recommendations concern source-relative input membership, never guessed chemical form, final volume or physical composition. Exact tables and original hashes are in complete-list-primary-proof.json.','', 'The native synonym function resolves all six JCM403 pointers and the four named phosphate aliases. The43 explicitly listed B component pairs bind to actual active MAPPED entities and exact component indexes; native MIM_CATALOG does not require one physical file or release/role approval. Complete source-form review is still required before authoring references.','', 'Deduplication suggestions use the complete captured all-state title/body inventory plus the external reviewer’s targeted full comment captures. They are not a claim that every issue comment was searched. A direct GET for1226 failed with a GitHub connection error; the coordinator’s successful readback was independently read and copied instead. No retry, approval failure, GitHub mutation or worker input occurred.','', 'Use actionable-findings-matrix.json for all12 exact scopes, all113-payload-action-matrix.tsv/json for every owner/case/hash, and target-verification-v1.json for direct reproductions. Correct only the supported bounded fields, preserve original packets and holds, and independently review the successor.']
(D/'ASSESSMENT.md').write_text('\n'.join(summary)+'\n')
# Pin native contracts and dedup capture actually used; do not copy the large full inventory.
refs=[]
for p in [C/'integration/worktree/src/mediaingredientmech/schema/mediaingredientmech.yaml',C/'integration/worktree/MAPPING_SEMANTICS.md',C/'integration/worktree/src/mediaingredientmech/synonym_policy.py',C/'preflight/final-scientific-issue-dependencies-v1/all-state-issue-pr-bodies-v1.json',issuefile]:refs.append({'path':str(p),'sha256':sha(p.read_bytes())})
save('context-input-bindings.json',{'inputs':refs,'comments_scope':'External W03 review live-issue-context-index.json and supplement index bind targeted comment captures, all verified via full manifest; not universal comment coverage.'})
print(json.dumps({'groups':len(triage),'payloads':len(rows),'completeness':{'UNKNOWN':24,'COMPLETE_source_input_lists':5,'separate':5},'matrix_sha256':sha((D/'actionable-findings-matrix.json').read_bytes()),'all_payloads_sha256':sha((D/'all113-payload-action-matrix.json').read_bytes())},indent=2))
