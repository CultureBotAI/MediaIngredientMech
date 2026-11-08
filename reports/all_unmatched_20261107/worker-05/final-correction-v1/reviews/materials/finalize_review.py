from pathlib import Path
import json,hashlib,datetime,collections,yaml
from mediaingredientmech.synonym_policy import is_resolving_synonym
O=Path(__file__).parent;P=O.parent/'materials';B=Path('reports/all_unmatched_20261107/worker-05')
def load(p):return json.loads(Path(p).read_text())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ch(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
def save(n,x):
 p=O/n;assert not p.exists(),p;p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
now=datetime.datetime.now(datetime.timezone.utc).isoformat();R=load(O/'whole-records.json');S=load(O/'source-index.json');D=load(P/'decisions.json')['decisions'];A=load(O/'field-and-structural-audit.json')
def binding(i):
 s=S[i];e=s['evidence'];return {'evidence_id':e['evidence_id'],'source_index':i,'capture':e['capture'],'url':e.get('url'),'original_accessed_at':e.get('accessed_at'),'locator':e.get('locator')}
# Editorial precision: archive entries share identical aggregate bytes but have distinct per-record locators.
cr=load(O/'case-reviews.json');pr=load(O/'payload-reviews.json')
for r in cr['case_reviews']:
 i=r['case_index'];replace={119:[254,316,353,354],120:[355,356],125:[357],133:[294,254,353,354]}.get(i)
 if replace:r['primary_evidence']=[binding(x) for x in replace]
 d=next(d for d in D if d['case_id']==r['case_id']);r['all_decision_evidence_ids']=d['evidence_ids']
for r in pr['payload_reviews']:
 i=int(r['proposal_id'].split('-')[-1]);replace={7:[196,197,200,242,253,355,356],27:[254,316,353,354,294]}.get(i)
 if replace:r['primary_evidence']=[binding(x) for x in replace]
cr['supersedes']={'path':'case-reviews.json','sha256':sha(O/'case-reviews.json'),'reason':'Precise per-record archive evidence locators for the same already-read aggregate bytes; full decision evidence bindings added. No scientific verdict changed.'}
pr['supersedes']={'path':'payload-reviews.json','sha256':sha(O/'payload-reviews.json'),'reason':'Precise per-record archive evidence locators for the same already-read aggregate bytes. No scientific verdict changed.'}
save('case-reviews-v2.json',cr);save('payload-reviews-v2.json',pr)
# Reproduce all baseline and original-published-overlay identifier groups, including ignored files.
base={str(p):yaml.safe_load(p.read_text()) for area in ['mapped','unmapped'] for p in Path('data/ingredients',area).glob('*.yaml')}
assert set(base)==set(A['baseline_file_hashes']);assert all(sha(p)==h for p,h in A['baseline_file_hashes'].items())
overlay=dict(base)
for p in load(B/'correction-1193-v1/proposals.json')['proposals']:
 overlay.pop(p['owner_path'],None);overlay[p.get('destination_owner_path') or p['owner_path']]=yaml.safe_load((B/p['after_capture']['path']).read_text())
for r in R:
 p=r['proposal'];overlay.pop(p['owner_path'],None);overlay[p.get('destination_owner_path') or p['owner_path']]=r['record']
def groups(cat):
 g=collections.defaultdict(set)
 for p,r in cat.items():
  if r.get('mapping_status')!='REJECTED':g[r['identifier']].add(p)
 return g
bg=groups(base);og=groups(overlay);scope=[]
for id in ['MICRO:0001363','FOODON:03315720','MICRO:0000178']:
 scope.append({'identifier':id,'baseline_members':[{'path':p,'sha256':sha(p)} for p in sorted(bg[id])],'reviewed_overlay_members':sorted(og[id]),'added_members':sorted(og[id]-bg[id]),'removed_members':sorted(bg[id]-og[id]),'assessment':'Removal of selected owners from a historically duplicated identifier group is not a new collision. Remaining owners retain their own historical scope and unresolved claims; this audit does not approve their equivalence or authorize merging.'})
# Optional metadata rows are already nonresolving by native policy in predecessor, independently probed.
probes=[]
for r in R:
 for a in (r['record'].get('synonyms') or []):
  if a.get('synonym_text','').lower().startswith('properties:'):
   old=[x for x in r['predecessor'].get('synonyms',[]) if x.get('synonym_text')==a['synonym_text']]
   assert len(old)==1 and not is_resolving_synonym(old[0]) and not is_resolving_synonym(a)
   probes.append({'proposal_id':r['proposal']['proposal_id'],'predecessor':old[0],'final':a,'predecessor_resolves':False,'final_resolves':False})
assert len(probes)==3
save('dependency-and-optional-policy-review.json',{'reviewer':'/root/media_research','at':now,'scope':A['partonomy_scope'],'baseline_count':len(base),'duplicate_families':scope,'peptone_baseline_inbound':A['baseline_peptone_inbound'],'peptone_overlay_inbound':A['overlay_peptone_inbound'],'peptone_dependency_assessment':'Nineteen baseline references become eighteen in the original published overlay because the separate Marine correction removes one reference. Every remaining historical reference is preserved, not automatically retargeted to generic Peptone. MIM_CATALOG resolution is a structural check and does not establish the source digest or approve these component claims. Current cross-shard coupling remains coordinator work.','optional_metadata_probes':probes,'native_synonym_policy':{'path':'src/mediaingredientmech/synonym_policy.py','sha256':sha('src/mediaingredientmech/synonym_policy.py')}})
used={x['source_index'] for r in cr['case_reviews'] for x in r['primary_evidence']}|{x['source_index'] for r in pr['payload_reviews'] for x in r['primary_evidence']}
ledger=[]
for i,s in enumerate(S):
 e=s['evidence'];mode='Hash and context binding checked; auxiliary or historical evidence is not independently approved merely by inclusion.'
 if i in used:mode='Claim-specific source content read against the complete payload and raw source context; locator in case/payload review.'
 if i==281:mode='Full PDF bytes verified; relevant manufacturer sections inspected: printed pages 13, 33, 48–50 and catalog listings around 92. Not a claim to read every unrelated product page.'
 if i==404:mode='Full catalog PDF bytes verified; the Hipolypepton family rows were inspected, including unqualified casein product versus soy S/N/NS. Not a whole-catalog scientific endorsement.'
 if e['kind']=='unsuccessful_search':mode='Unsuccessful retrieval or discovery evidence only; no primary identity claim inferred.'
 ledger.append({'evidence_id':e['evidence_id'],'capture':e['capture'],'url':e.get('url'),'original_accessed_at':e.get('accessed_at'),'timestamp_precision':e.get('timestamp_precision'),'local_review_at':now,'original_bytes_sha256':s['sha256'],'independent_extracted_text':({'path':str(Path(s['read_path']).relative_to(O)),'sha256':sha(s['read_path'])} if s.get('read_path') else None),'read_scope':mode})
contractfiles=['MAPPING_SEMANTICS.md','.claude/skills/add-media/SKILL.md','.claude/skills/review-yaml-category/SKILL.md','docs/record-reviews.md','src/mediaingredientmech/schema/mediaingredientmech.yaml','src/mediaingredientmech/validation/write_validated.py','src/mediaingredientmech/validation/component_partonomy.py','src/mediaingredientmech/synonym_policy.py']
contractfiles += [str(p) for p in (P/'context').glob('*') if p.is_file()]
save('scientific-read-ledger.json',{'reviewer':'Codex GPT-6 /root/media_research','primary_author':'Codex /root/materials_research','at':now,'independence':'This is an authorship-separated review of the materials lane. This reviewer authored the separate media lane, not these materials successor payloads. Historical reviews retain their original attribution and are not transferred to final bytes.','whole_payload_and_before_ledger':{'path':'whole-records.json','sha256':sha(O/'whole-records.json')},'full_raw_case_and_recipe_ledger':{'path':'frozen-contexts.json','sha256':sha(O/'frozen-contexts.json')},'source_entries':ledger,'contract_and_context_bindings':[{'path':p,'sha256':sha(p)} for p in contractfiles],'primary_capture_policy':'Existing exact bytes and original timestamps were reused. No new network retrieval is claimed. Search snippets, failed responses and GMO enrichment do not independently establish a product identity. The archived TOGO batch has a batch timestamp only, not an invented per-row retrieval time.','scientific_limits':'All 61 complete case objects, 191 frozen recipe context records and all 39 whole payloads/before/predecessors were inspected. Long manufacturer documents were read at the relevant constituent/product sections, not every unrelated page. Owner catalogs were parsed completely with explicit mapped/unmapped globs including ignored files; unselected owner claims are not approved.'})
# End verification: sealed primary packet and all evidence bytes unchanged.
manifest=load(P/'MANIFEST.json');errors=[]
for f in manifest['files']:
 if sha(P/f['path'])!=f['sha256']:errors.append(f['path'])
for s in S:
 if sha(s['path'])!=s['sha256']:errors.append(s['path'])
assert not errors,errors
assert len(cr['case_reviews'])==61 and len(pr['payload_reviews'])==39
assert len({r['case_id'] for r in cr['case_reviews']})==61
assert len({r['proposal_id'] for r in pr['payload_reviews']})==39
assert sum(len(f['recipes']) for f in load(O/'frozen-contexts.json'))==191
save('end-integrity-receipt.json',{'at':now,'sealed_primary_manifest_sha256':sha(P/'MANIFEST.json'),'sealed_members_verified':len(manifest['files']),'evidence_bindings_verified':len(S),'baseline_owner_files_unchanged':len(base),'errors':errors,'no_primary_or_maintained_writes':True,'no_git_or_github_writes':True})
review={'reviewer':'Codex GPT-6 /root/media_research','primary_author':'Codex /root/materials_research','at':now,'status':'complete_supported_with_retained_limits','reviewed_inputs':{n:sha(P/n) for n in ['MANIFEST.json','decisions.json','evidence.json','proposals.json','payload-ancestry.json','integration-dependencies.json','scientific-read-ledger.json','payload-primary-assessments.json','finding-dispositions.json','mapping-evidence-dispositions.json']},'case_reviews':cr['case_reviews'],'payload_reviews':pr['payload_reviews'],'finding_dispositions':load(O/'finding-disposition-review.json')['dispositions'],'new_findings':[],'open_review_findings':0,'counts':{'cases':61,'payloads':39,'context_occurrences':191,'evidence_entries':451,'filed_findings_reviewed':7,'provenance_rows_reviewed':27,'changed_payloads':sum(bool(x['changes_from_selected_predecessor']) for x in A['field_reviews']),'cases_with_proposals':sum(bool(d['proposal_ids']) for d in D)},'lineage_result':'All 39 original selected proposals have exactly one successor. Additional older ancestor IDs in two replacement lists are provenance, not additional replacements. The two MATERIALS-P-* selected proposals remain represented. No proposal disappeared behind renaming.','validation_scope':{'closed_schema':'39 exact payloads independently passed unchanged closed-schema validator.','partonomy':A['partonomy_scope'],'partonomy_errors':A['partonomy_errors'],'whole_campaign_final_gate':'Not performed by this reviewer. Root must validate the actual final combined overlay and any subsequent union bytes.','scientific_acceptance':'This supports the bounded case-level scientific corrections and seven proposed remediations only. It is not approval of whole owners, inherited roles, all component references, source admission, exports, pending coordinator unions or record merges.'},'obligations':['Preserve all original negative decisions, raw labels, occurrence membership, source quantities, product forms, histories and substantive holds.','Keep the 18 historical Peptone inbound claims and current cross-shard component choices under source-specific reconciliation; do not retarget by identifier availability alone.','Phytone, generic soy, Difco Soytone and Catalase reuse is bounded. No other-worker counts, history or approval of pending 37 coordinator union candidates is imported.','Remaining historical duplicate groups are not newly introduced collisions; no arbitrary representative or merge is authorized.','Retain historical human MappingEvidence and the distinct ComponentEvidence enum. New scientific applicability judgments remain agent-attributed.','Canonical integration/native/source/export gates remain coordinator work. No issues were closed and no payload was applied.'],'supporting_artifacts':{n:sha(O/n) for n in ['case-reviews-v2.json','payload-reviews-v2.json','mapping-evidence-review.json','finding-disposition-review.json','scientific-read-ledger.json','proposal-lineage-audit.json','field-and-structural-audit.json','dependency-and-optional-policy-review.json','end-integrity-receipt.json']}}
save('final-scientific-review.json',review)
save('HANDOFF.json',{'reviewer':review['reviewer'],'status':review['status'],'at':now,'counts':review['counts'],'review_path':'final-correction-v1/review-materials/final-scientific-review.json','review_sha256':sha(O/'final-scientific-review.json'),'reviewed_inputs':review['reviewed_inputs'],'open_review_findings':0,'scope_limits':review['validation_scope'],'obligations':review['obligations']})
md='''The independent materials review is complete for all 61 assigned cases, 39 exact successor payloads, 191 frozen recipe contexts and seven filed MAT finding dispositions. All 39 selected original proposals have exactly one successor, including the two MATERIALS-P-* proposals; older ancestor IDs are retained separately.

The seven remediations are supported in the proposed bytes. The 27 mapping-provenance dispositions were checked claim by claim, including the single narrow Neopeptone DATABASE_MATCH and the three Phytone LLM_SUGGESTION assertions. Historical human evidence and the separate component-evidence enum were preserved. No new unresolved review finding was established.

This is bounded scientific acceptance, not whole-owner or release approval. Unknown product selections, inherited roles, source/export holds, the 18 historical Peptone component dependencies, remaining duplicate families and all pending coordinator unions remain unresolved as recorded. No other-worker counts, source memberships or historical review approval were imported.

Independent closed-schema checks passed for the 39 payloads. Partonomy passed for the original published 138-proposal overlay with these 39 material successors inserted by owner-path replacement. That is not the later final combined campaign overlay; root's actual final integration gate remains authoritative.

All 335 sealed primary members, 451 evidence bindings and 2,956 baseline owner files were rehashed unchanged. Long manufacturer catalogs were read at the relevant product sections, not every unrelated page. Original retrieval timestamps were preserved; no new network capture is claimed. Preliminary review files remain intact; the v2 case/payload views only refine per-record locators within the same archived aggregate bytes and add complete decision evidence bindings.

No primary packet, payload, maintained source, Git state or GitHub issue was modified. The final review binds every case and payload hash. Stop here for coordinator assembly.
'''
assert not (O/'HANDOFF.md').exists();(O/'HANDOFF.md').write_text(md)
files=[{'path':str(p.relative_to(O)),'sha256':sha(p),'bytes':p.stat().st_size} for p in sorted(O.rglob('*')) if p.is_file() and p.name!='MANIFEST.json']
save('MANIFEST.json',{'created_at':now,'reviewer':review['reviewer'],'status':'sealed independent materials review','files':files})
print(json.dumps({'final-scientific-review.json':sha(O/'final-scientific-review.json'),'HANDOFF.json':sha(O/'HANDOFF.json'),'MANIFEST.json':sha(O/'MANIFEST.json'),'files':len(files),'counts':review['counts']},indent=2))
