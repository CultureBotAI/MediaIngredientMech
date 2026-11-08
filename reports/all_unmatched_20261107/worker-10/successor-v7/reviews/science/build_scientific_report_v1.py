"""Freeze this reviewer's scientific conclusions, without modifying author inputs."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,yaml
R=Path(__file__).resolve().parents[3];O=Path(__file__).resolve().parent
A=R/'reports/all_unmatched_20261107/worker-10';S=A/'successor-v7'
W=R.parents[1]/'w07/worktree/.temp/columbia-continuity-independent-v1'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def bind(p):return {'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size}
def load(p):return json.loads(p.read_text())
verification=load(O/'candidate-verification-v1.json');prereq=load(O/'prerequisite-science-v1.json')
targets=[]
conclusions={
'sv7-dependent-columbia-unmapped0118-partition':{
 'conclusion':'Supported genuine same-path generic-owner continuity correction. Both vendor strings remain as nonresolving provenance; the generic owner keeps its identifier, classification, unresolved scope, original generic label, statistics and all five original events.',
 'claim_assessment':[
  'The authentic maintained29ed63 owner is an extracted generic medium preparation, not agar itself and not an established vendor formula. No molecular formula, supplier, product catalogue, ontology grounding, role or composition is grafted onto it.',
  'The two vendor labels previously resolved to the generic residual despite differing positive nominal formulas and supplied-form contexts. REJECTED_LABEL is claim-specific rejection of global identity ownership on this generic record; it does not deny that either product exists.',
  'Only this existing-owner proposal receives maintained before29ed63. Preserved old history is not transplanted onto a vendor destination. The new event truthfully identifies root authoring and AI assistance.',
  'Historical Aug30 x4/x1 mentions and stored zero counts remain historical facts. The seven later context rows are a separate inventory; no retrospective recount or new assigned source case is implied.'
 ],'positive_sources':['authentic maintained owner and original5event history','native MAPPING_SEMANTICS section3 and synonym_policy','full7current source recipes','JCM1270','MediaDiveJ1270','TOGO7exact cached objects','BD2009','Oxoid CM0331 specification']},
'sv3-hm-difco-columbia1270':{
 'conclusion':'Supported exact vendor-qualified alias transfer onto the existing source-qualified nominal Difco dry-base candidate, coupled to the genuine0118 dependency. The entire final record remains consistent with its bounded nominal2009 and JCM1270 scope.',
 'claim_assessment':[
  'Full JCM1270 explicitly identifies BD-Difco44g before separate water and blood. Two vendor-labelled current rows and the positively attributed MediaDiveJ1270/compound2046 row support three dry routes. Generic compound2046 and the generic Columbia label do not become global Difco identities.',
  'The genuine2009 manufacturer page158 lists seven immediate names. CURATED_INTERPRETATION/COMPLETE remains limited to those nominal names; no structured component amounts, dry-mass fractions, exact historical lot or final-volume yield are asserted. Performance adjustments remain unknown. Water and blood remain outside dry components.',
  'The seven full component objects are unchanged: four unresolved named parts plus represented yeast extract, sodium chloride and agar. Catalog references denote only these constituents; no complete child-owner approval follows.',
  'Full OLS MICRO0000536 response defines the separate BBL recipe; genuine2009 BBL/EH columns differ positively from Difco. The older manufacturer PDF has different heart wording and BBL proportions, as the retained notes disclose. Failed source requests and search wrappers remain historical leads, not positive manufacturer support.',
  'The new CATALOG_VARIANT preserves exact old synonym text/source. Existing source-qualified identity, supplied form, LLM_SUGGESTION evidence, all four original events, version/lot limits and receiving-medium discrepancies are retained. Only synonyms, appended notes and one truthful history event change.',
  'The vendor destination keeps maintained before=null. Its previous e356 payload is proposal lineage; generic29ed63→0bbcb8 is a coupled dependency, not its own preimage.'
 ],'positive_sources':['JCM1270 full HTML','TOGO M1366 cached full object','MediaDiveJ1270 complete JSON plus generic ingredient2046','BD2009 title/copyright/Columbia section and printed158 raster','older BD manufacturer PDF version context','OLS MICRO0000536 full response','current component ID/name rows only']},
'sv1-buffers-tris_hcl_0_2m_ph7_5_dsmz273':{
 'conclusion':'UNKNOWN correctly replaces PARTIAL for this source-named0.2M Tris-HCl pH7.5 stock. The complete source-qualified record is retained with no chemistry or identity expansion.',
 'claim_assessment':[
  'Full DSM273 PDF explicitly adds250mL of this stock to receiving seawater and other inputs. It does not state a complete internal stock recipe and does not explicitly identify omitted constituents. UNKNOWN follows the native source-relative enum contract.',
  'One UNMAPPED Tris-HCl named buffer-system part is retained; no dry reagent form, salt ratio, carrier, titrant or seawater constituent is invented. LABEL_ENUMERATION and RECIPE_SOURCE evidence remain appropriate for the one name stated in the source.',
  'Registry-only preparation identity and nominal0.2M/pH7.5 boundary remain; no pure Tris exact mapping, global raw-label alias, inferred final-medium concentration or release approval is added.',
  'Every existing field except completeness is exact; original two history objects and all source/quantity holds survive. Historical PARTIAL wording is explicitly qualified in the v3 decision marker without rewriting the old completion_reassessment.'
 ],'positive_sources':['DSM273 full PDF and raster','frozen case80 and full CultureMech004701 recipe','native ComponentCompletenessEnum']},
'sv1-buffers-hepes_2m_ph7_jcm556_1200':{
 'conclusion':'UNKNOWN correctly replaces PARTIAL for the named2M HEPES pH7 stock. Full-record retention preserves bounded source associations and all unresolved composition/form details.',
 'claim_assessment':[
  'Both complete JCM556/1200 bodies name5mL of2M HEPES pH7 in separately sterilized-stock context. Neither provides the HEPES stock formula or explicitly states omitted constituents; receiving water, other stocks and gases do not establish its carrier or components.',
  'One UNMAPPED HEPES part remains; supplied acid/salt form, titrant and amount, solvent and full composition are not guessed. LABEL_ENUMERATION and existing RECIPE_SOURCE evidence remain unchanged.',
  'The local stock identity is distinct in nominal strength/pH from the retained50mM pH7.8 comparison and is not the pure HEPES acid owner. No exact full-formulation sameness between recipes is newly asserted.',
  'Three frozen assigned occurrences remain intact. Their normalized5G_PER_L entries are retained source records; the primary5mL reading is not silently converted into mass or used to repair source recipes.',
  'Every existing field except completeness is exact; two original history events and all source/role/export holds survive. v3 explicitly distinguishes historical PARTIAL wording from active UNKNOWN.'
 ],'positive_sources':['full JCM556 HTML','full JCM1200 HTML','frozen case135 and three complete enclosing recipes','native ComponentCompletenessEnum']},
'sv1-bio-columbia_blood_agar_oxoid_m2224':{
 'conclusion':'The unchanged complete37e8 source payload is a valid bounded nominal dry-base origin for the updated dependency/routing metadata. It is not a newly composed or approved combined Oxoid owner.',
 'claim_assessment':[
  'Actual TOGO M2224 supplies39g Oxoid dry product and separate23/5/1/10g nominal component list; water is an external input. No catalogue number is printed there, and no final-volume yield or dry-mass fraction is inferred.',
  'The complete unchanged record uses registry-only identity and four nominal constituents; special peptone stays UNMAPPED, while sodium chloride, starch and agar refs identify only those generic constituents. No blood or receiving water is introduced as a dry part.',
  'W04 current4a3d origin binds source300 with literal variable quantity and printedCM0331. Manufacturer nominal four-input formula provides product context, not an invented39g dose for source300 or historical catalogue for source921.',
  'W04 current origin retains PARTIAL and is not itself the final combined candidate. The existing coordinator5846 prototype is a read-only composition input. One coordinator-composed, separately reviewed final Oxoid family candidate remains required; these origins must not be installed as parallel owners.',
  'Four later CM3311L prepared-base contexts remain held with no dry39g conversion or broad prepared-base alias. Their vendor provenance is supported, while exact preparation identity/quantity remains unresolved.'
 ],'positive_sources':['full TOGO M2224 body','full frozen case118 and enclosing recipe','full W04 source300 case/current payload','cached TOGO M2935 object','genuine Oxoid4page specification and raster','seven later context recipes','read-only coordinator prototype']}
}
for r in verification['payload_matrix']:
 pid=r['proposal_id']
 if pid not in conclusions:continue
 p=Path(r['after']['path']);d=yaml.safe_load(p.read_text())
 targets.append({'proposal_id':pid,'before':r['before'],'after':r['after'],'full_record_read':True,'all_top_level_fields_reviewed':list(d),'field_changes':r['field_changes'],'original_history_events_retained':len(d.get('curation_history',[]))-(1 if r['changed'] else 0),'assessment':conclusions[pid]})
extra=[]
for h,scope in [
 ('c15b4419aecebb920b8b1a6dfc74cabef82cc45aff5c04cd198ec66c391ac924','All older Columbia manufacturer excerpt text; version context only. Beef Heart Digest vs2009 infusion and older BBL12/3 proportions directly checked.'),
 ('49f95e733559020dbafbd57baa6b4f0d973ab9fe72dbf5e662414930b5f99a00','Full OLS response: MICRO0000536 definition/source is BBL10/5/5/3/1/5/13.5 formulation; no whole-Difco exact identity inferred.')]:
 p=W/'inputs/blobs'/h;extra.append({**bind(p),'actual_scope':scope})
component_bindings=[]
for name in ['Yeast_Extract','Nacl','Agar','Starch']:
 p=R/'data/ingredients/mapped'/f'{name}.yaml';d=yaml.safe_load(p.read_text());component_bindings.append({**bind(p),'identifier':d['identifier'],'preferred_term':d['preferred_term'],'scope':'Current identity/name support for retained component reference only; full owner roles/exports not reviewed or approved.'})
primary_reads=prereq['primary_readings']
evidence=load(S/'author-core-v3/evidence.json')['evidence']
for row in primary_reads:
 for e in evidence:
  if e.get('capture',{}).get('sha256')==row['sha256'] and e.get('url'):
   row.setdefault('url',e['url'])
   row.setdefault('original_accessed_at',e.get('accessed_at'))
   row.setdefault('bound_evidence_id',e['evidence_id'])
   break
out={
 'review_id':'W10-SV7-COLUMBIA-CONTROLS-INDEPENDENT-SCIENCE-V1',
 'reviewer':'worker10:/root/preparation_skeptic (AI)',
 'earliest_recorded_review_milestone':load(O/'started.json')['at'],
 'timing_qualification':'Earliest saved prerequisite milestone, not a fabricated exact cognitive start; source observations and final script times are separately preserved.',
 'completed_at':datetime.now(timezone.utc).isoformat(),
 'status':'PASS_BOUNDED_CORRECTION','verdict':'pass_with_limitations','scientific_review':True,'author_independent':True,
 'authorship_and_independence':{
  'candidate_author':'Codex worker10 /root',
  'reviewer_prior_involvement':'Prior W10 preparation-family skeptical review and successor-v3/v6 Difco full-payload reviews; authored earlier skeptical findings/reports, including the current historical-enum metadata finding. This is fresh independent review of root candidate bytes, not a claim of historically uninvolved review or human review.',
  'original_payload_authorship':'Tris/HEPES original proposals: /root/buffers_research. Oxoid source proposal: /root/bio_research. Difco original KG proposal: root worker10 source author, later biological source-support correction by /root/bio_research, root provenance and v6 assertion corrections. Generic0118 original histories retain their actual mixed historical curator strings; authorship is not recertified as human.',
  'scope_separation':'This reviewer authored none of these target source payloads or root v7 candidates. W07 science/continuity reports and coordinator prototype are separately attributed input context, not copied acceptance.'},
 'active_author_freeze':bind(S/'author-freeze-v3.json'),
 'active_core':verification['core_bindings'],
 'contracts_read':[bind(R/p) for p in ['MAPPING_SEMANTICS.md','src/mediaingredientmech/schema/mediaingredientmech.yaml','src/mediaingredientmech/synonym_policy.py','docs/record-reviews.md','docs/record-review-profile.md','.claude/skills/review-yaml-category/SKILL.md']],
 'exact_candidate_reviews':targets,
 'coverage':{'fresh_changed_full_payloads':4,'unchanged_Oxoid_full_payload_and_changed_metadata':1,'changed_assigned_cases':[80,118,135,178],'assigned_occurrences_in_these_cases':5,'current_external_owner_context_rows':7,'supported_Difco_context_routes':3,'held_prepared_Oxoid_context_routes':4,'all_assigned_cases_retained':188,'all_assigned_occurrences_retained':304,'original_proposals':127,'new_genuine_dependency_proposals':1,'selected_proposals':128,'old_payloads_changed':3,'old_payloads_exact':124,'other_case_objects_exact':184,'old_evidence_objects_exact':1218,'new_author_evidence_objects':6,'mechanical_candidate_checks':verification['check_count'],'prerequisite_source_checks':prereq['check_count']},
 'source_evidence':{'prerequisite_report':bind(O/'prerequisite-science-v1.json'),'full_verified_prerequisite_manifests':bind(O/'prerequisite-manifest-check-v1.json'),'principal_primary_reads':primary_reads,'additional_primary_context_reads':extra,'derived_read_support':[bind(O/n) for n in ['oxoid-spec-primary.txt','bd2009-columbia-primary.txt','bd-older-columbia-primary.txt','dsmz273-primary.txt','bd2009-p170.png','oxoid-spec-p1.png','dsmz273-p1.png']],'full_TOGO_member_binding':prereq['source_corpus'],'seven_TOGO_objects':prereq['source_objects'],'full_assigned_recipe_bindings':verification['frozen_source_occurrences'],'current_component_identity_rows':component_bindings,'new_network_fetches':0,'positive_support_policy':'Actual captured primary bodies and visible PDF tables support claims. Issue comments/reviews are instruction or prior-review context. Failed responses/search wrappers are never promoted to positive primary evidence.'},
 'independent_verification':{'receipt':bind(O/'candidate-verification-v1.json'),'script':bind(O/'verify_candidates_v1.py'),'stdout':bind(O/'candidate-verifier-v1.stdout'),'stderr':bind(O/'candidate-verifier-v1.stderr'),'actual_exit_code':0,'claim':'975 exact source, complete-payload, rollback, retained-core, history, dependency and native synonym-policy checks passed; no broad native suite run is claimed by this reviewer.'},
 'findings':[{'finding_id':'W10-SV7-SKEPTIC-HISTORICAL-COMPLETENESS-001','severity':'minor','status':'resolved_in_exact_author_core_v3','reported_before_fix':bind(O/'historical-completeness-finding-v1.json'),'root_correction':bind(S/'historical-enum-correction.json'),'independent_verification':verification['historical_enum_fix_verification'],'scope':'Two metadata clarifications only. Exact old completion_reassessment objects, all source/payload/history and evidence/proposal bytes remain unchanged; no chemistry or GitHub closure.'}],
 'other_disclosed_root_draft_correction':{'finding':bind(S/'author-draft-binding-finding.json'),'scope':'Initial author-v1 overbroad new evidence case associations narrowed in v2. Original v1 preserved; all1218 old evidence objects and all4payloads remain exact. This reviewer verified v3 active applicability without claiming authorship of the root-discovered finding.'},
 'open_new_findings':[],
 'existing_finding_dispositions':[
  {'finding_ids':['CENTRAL-21','BIO-F06','BIO-F07'],'disposition':'Bounded source-worker generic dependency and Difco alias/routing correction supported. Genuine application, final single Oxoid composition/review and all prepared/global/role/export holds remain; no terminal closure of the entire finding family.'},
  {'finding_id':'CENTRAL24-COMPLETENESS-001','disposition':'Only controls941/955 corrected toUNKNOWN. Do not close the whole broader guidance finding, modify280/938, or downgrade complete nominal Wolfe/Hutner lists.'}],
 'limitations':prereq['source_limits']+[
  'Review is prepublication exact author-v3 candidate review; final assembled native pair, source-worker publication head and coordinator acceptance remain separate stages.',
  'All127old payloads/188case bindings were checked mechanically, but the other124 payloads and184cases receive no renewed scientific approval.',
  'Five frozen assigned recipe contexts and seven later current-owner contexts are distinct denominators. KGcase178 helper occurrence1 is not a measured CultureMech occurrence and contributes zero assigned CM occurrence IDs.',
  'This reviewer does not certify every primary producer field outside the named stock/product and continuity claims; retained recipe normalization defects and unrelated constituents remain source context, not new curation.',
  'No maintained edit, shared manifest edit, Git/GitHub mutation, role/export/whole-owner release approval, new paid call or external session was performed.'
 ],
 'review_attempt_disclosure':prereq['review_attempt_notes']+['A later initial frozen-source path assumed campaign root; lookup showed authoritative source_root=queue/preliminary-v5, then all five complete recipes/four original cases were read and hashes verified. No absence claim or evidence mutation followed.','Some broad proposal/route displays exceeded output size; all affected complete records and remaining metadata were subsequently read in targeted calls, and full nested previous objects were checked mechanically against their originals.'],
 'source_routing_binding':bind(S/'source-routing.json'),'cross_worker_binding':bind(S/'cross-worker-dependencies.json'),
 'approval_granted':{'bounded_proposal_science_supported':True,'maintained_application':False,'whole_owner_release':False,'roles':False,'exports':False,'final_combined_Oxoid_candidate':False,'future_published_head':False}
}
p=O/'scientific-review-v1.json';assert not p.exists();p.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
md='''The four exact v7 candidate records pass independent scientific review within their declared source scope. The unchanged W10 Oxoid record was also read in full as an authentic source origin. No maintained application, final Oxoid combination, whole-owner, role, export, or future published-head approval is granted.

The genuine UNMAPPED_0118 dependency preserves generic identity and all five original events, retains both vendor labels as REJECTED_LABEL, and transfers only the supported BD-Difco vendor label to the existing Difco dry-base candidate. Three current Difco routes are source-supported; four 1 L prepared Oxoid contexts stay held. W04 source300 keeps its variable dose/catalogue; W10 source921 keeps39g without a historical catalogue assertion. The coordinator still must compose and review one combined Oxoid candidate.

Tris941 and HEPES955 now use UNKNOWN because their primary recipes neither establish a full stock formula nor explicitly identify omitted constituents. Their complete payloads retain every other scientific field and append one truthful event. Difco retains its seven-name nominal2009 COMPLETE/CURATED_INTERPRETATION scope, separate blood/water and unresolved lot/performance details.

One minor metadata finding was reported before correction: cases80/135 retained old PARTIAL wording without an explicit historical/current distinction. Author-core-v3 adds that clarification and preserves the old objects and all payloads exactly. The immutable finding and independently verified correction are bound in the JSON report. No new open finding remains in this bounded review.

Independent verification passed975 candidate checks and42 prerequisite source checks. It retains188 assigned cases/304occurrences,128 selected proposals comprising127 original IDs plus the genuine dependency,124 unchanged old payloads,184 unchanged case objects and1218 unchanged evidence objects. These mechanical totals do not renew science for unaffected records.

Reviewer: worker10:/root/preparation_skeptic, an AI separate from root candidate authorship. Prior W10 preparation and Difco successor review participation is explicitly disclosed. Genuine manufacturer PDF tables, primary recipe bodies and complete source contexts were reread; no fresh network research was required. Final native assembly/publication remains a separate review stage.
'''
m=O/'scientific-review-v1.md';assert not m.exists();m.write_text(md)
print(json.dumps({'status':out['status'],'verdict':out['verdict'],'report':bind(p),'markdown':bind(m)}))
