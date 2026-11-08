from pathlib import Path
import datetime, hashlib, json, subprocess, re
import yaml

R = Path.cwd()
A = R / '.temp/peptone-consumer-independent-v1/ambiguous'
C = R.parents[2]
NOW = datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def put(name, value):
    with (A/name).open('x') as f:
        json.dump(value, f, indent=2, ensure_ascii=False); f.write('\n')

claims = json.loads((A/'selected-claims.json').read_text())
observations = json.loads((A/'original-source-observations.json').read_text())
pins = json.loads((A/'owner-beforeimage-pins.json').read_text())
assert len(claims) == len(pins) == 10
assert len(observations['rows']) == 124
for p in pins:
    assert sha(p['path']) == p['sha256'] == sha(A/p['copy'])

source_details = {
 'FAB_ORIGINAL': {
  'url':'https://www.academia.edu/145655855/Fastidiosipila_sanguinis_gen_nov_sp_nov_a_new_Gram_positive_coccus_shaped_organism_from_human_blood',
  'doi':'10.1099/ijs.0.63327-0',
  'files':['original-source-read-6.json','original-source-read-7.json','original-paper-pages-web.json'],
  'read_extent':'Original-paper mirror text: title/authors/DOI and methods/results/species-description passages, pp853–856; publisher abstract/title independently matched. Tables, sequence analysis and references not exhaustively reviewed. No raw publisher PDF obtained.',
  'claim':'Original paper associates the FAB preparation with Oxoid; its separate Anaerobe Systems PYG fermentation broth does not identify the FAB components.',
  'scope':'Fastidiosipila sanguinis original study. Supports source-attribution discrepancy only; historical catalogue formulation and meat-granule composition unresolved.'},
 'MOORE1976': {
  'url':'https://scispace.com/pdf/emendation-of-bacteroidaceae-and-butyrivibrio-and-3spebb4661.pdf',
  'doi':'10.1099/00207713-26-2-238',
  'files':['pdf-access-web-attempts.json','moore1976-find-web.json','original-source-read-6.json'],
  'read_extent':'Web-tool PDF text extraction of original-paper mirror: p238 methods, p239 medium context, p242 Butyrivibrio context, pp250–251 E.siraeum and C.leptum passages, pp251–252 references. Not every page/table read. Publisher metadata matched. Direct raw PDF request returned HTML403, retained as denial, not PDF evidence.',
  'claim':'Exact historical PY-cellobiose and PY-maltose use is confirmed for E.siraeum and C.leptum. E.siraeum text supports peptone as a basal-medium class at that occurrence; recipes refer to the 1975 Anaerobe Laboratory Manual, which was not inspected.',
  'scope':'Occurrence-bound evidence; neither supplier-specific identity nor one common formulation for all PY/PYG labels is established.'},
 'DSMZ104C_DSM753': {
  'url':'https://bacmedia.dsmz.de/medium/104c?ccno=DSM+753',
  'files':['captures/dsmz104c-dsm753.html','captures/dsmz104c-dsm753.html.capture.json'],
  'read_extent':'Captured original HTML inspected at strain selection/modification, Main sol.104c component table and named digest rows. No historical equivalence certificate.',
  'claim':'Current C.leptum DSM753 repository recipe contains separate Trypticase peptone (BD BBL) and pepsin-digested meat peptone, 5g each, and substitutes D-maltose for glucose.',
  'scope':'Current strain-specific comparator, not proof that the historic PY-maltose single peptone edge denotes either product.'},
 'ATCC1223': {
  'url':'https://www.atcc.org/~/media/8c253e70949144a6b7038ad5024f8f1d.ashx',
  'files':['captures/atcc1223.pdf','captures/atcc1223.pdf.capture.json','captures/atcc1223.extracted.txt'],
  'read_extent':'Entire one-page authentic ATCC PDF read via pdftotext, including composition and preparation.',
  'claim':'ATCC1223 for T.pectinovorum specifies Polypeptone Peptone (BD211910), 5g, alongside a distinct heart-infusion ingredient and other components.',
  'scope':'Current authentic repository recipe; no demonstrated identity with historic PY-pectin observation. Polypeptone must not be replaced by Bacto Peptone or Hipolypepton.'},
 'NEOGEN_NCM0199': {
  'url':'https://www.neogen.com/499687/globalassets/pim/assets/original/10007/ncm0199_ts_en-us.pdf',
  'files':['captures/w05-direct-151.body','captures/w05-direct-151.body.reuse.json','captures/w05-direct-151.extracted.txt'],
  'read_extent':'Entire two-page manufacturer PDF read via pdftotext; exact archived bytes and original access timestamp 2026-11-08T06:22:02.501887+00:00 reused.',
  'claim':'2019 manufacturer FAB sheet identifies a peptone mixture; it is a LabM/Neogen formulation.',
  'scope':'Comparator only. No bridge to original-paper Oxoid attribution; cannot approve original FAB ingredient or starch/glucose assertions.'},
 'ACUMEDIA7110': {
  'url':'https://biotrading.com/assets/productinformatie/acumedia/tds/7110.pdf',
  'files':['captures/w05-direct-155.body','captures/w05-direct-155.body.reuse.json','captures/w05-direct-155.extracted.txt'],
  'read_extent':'Entire three-page manufacturer PDF read via pdftotext; exact archived bytes and original access timestamp 2026-11-08T06:22:43.890414+00:00 reused.',
  'claim':'Manufacturer meat granules denote a formulated cooked-meat medium with multiple constituents.',
  'scope':'Negative comparator against treating meat granules automatically as pure food meat; does not establish Fastidiosipila granule product.'},
 'MORRIS1985': {
  'url':'https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/00207713-35-4-478',
  'doi':'10.1099/00207713-35-4-478',
  'files':['original-paper-pages-web.json','original-fulltext-web-attempts.json'],
  'read_extent':'Publisher title/abstract/references inspected; offered HTML full text unavailable. No original formula inspected.',
  'claim':'Matched original C.scindens study identified; no inspected recipe establishes PYEG ingredient identity.',
  'scope':'Bibliographic/source-access evidence only.'},
 'SMIBERT1983': {
  'url':'https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/00207713-33-4-852',
  'doi':'10.1099/00207713-33-4-852',
  'files':['original-paper-pages-web.json','original-fulltext-web-attempts.json'],
  'read_extent':'Publisher abstract/metadata/references read; original complete methods unavailable.',
  'claim':'Original T.pectinovorum description identified; abstract describes pectin and rumen-fluid/short-chain-fatty-acid requirement but does not supply peptone identity.',
  'scope':'No formula or historical bridge to ATCC1223 inspected.'},
 'SMIBERT1984': {
  'url':'https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/00207713-34-4-457',
  'doi':'10.1099/00207713-34-4-457',
  'files':['original-paper-pages-web.json','original-fulltext-web-attempts.json'],
  'read_extent':'Publisher abstract/metadata/references read; original complete methods unavailable.',
  'claim':'Original T.socranskii species/subspecies description identified; no inspected original peptone formulation.',
  'scope':'No resolution of inherited PY-glucose-rumen-fluid digest identity or clarified-rumen assertion.'},
 'ANDREESEN1970': {
  'url':'https://link.springer.com/article/10.1007/BF00409521','doi':'10.1007/BF00409521',
  'files':['original-primary-attempts-9.json','original-primary-read-10.json'],
  'read_extent':'Publisher abstract, article metadata and explicit subscription-preview boundary inspected. Full text not purchased or read.',
  'claim':'Original C.formicaceticum study and fructose phenotyping identified; abstract does not identify digest in PY-fructose.',
  'scope':'Bibliographic/source-access evidence only.'},
 'BERGEY_ORIGINAL': {
  'urls':['https://onlinelibrary.wiley.com/doi/abs/10.1002/9781118960608.gbm00619','https://onlinelibrary.wiley.com/doi/abs/10.1002/9781118960608.gbm00629','https://onlinelibrary.wiley.com/doi/abs/10.1002/9781118960608.gbm01249'],
  'files':['original-source-read-6.json','original-source-read-7.json'],
  'read_extent':'Clostridium and Treponema abstract/metadata and selected reference lists inspected; full-text links redirected to abstracts. Eubacterium chapter returned403.',
  'claim':'Direct source chapter references verified where accessible. These accesses did not expose complete source recipes.',
  'scope':'Raw-source observation lineage verified separately; unavailable chapter contents are not presented as inspected.'},
 'POLYSACCHAROLYTICUM1980': {
  'url':'https://www.microbiologyresearch.org/content/journal/micro/10.1099/00221287-116-1-157','doi':'10.1099/00221287-116-1-157',
  'files':['search-original-specific-8.json','original-primary-attempts-9.json'],
  'read_extent':'Exact citation verified from inspected Bergey reference list; search preview only, attempted original publisher page timed out. Full methods unread.',
  'claim':'Original species-paper lead retained without formulation claim.',
  'scope':'Does not extend E.siraeum occurrence support to C.polysaccharolyticum.'},
 'RUMINANTIUM1959': {
  'url':'https://pmc.ncbi.nlm.nih.gov/articles/PMC181027/','doi':'10.1128/br.23.3.125-153.1959',
  'files':['original-primary-attempts-9.json','original-primary-read-10.json'],
  'read_extent':'Bibliographic search discovery and PMC access attempt; PMC returned browser challenge. No original body inspected.',
  'claim':'Original taxonomic source located but its recipe remains unread.',
  'scope':'Current ATCC17233 alternative medium602 listing does not prove original PYG-rumen composition.'},
 'BIFORMIS_CURRENT': {
  'url':'https://www.atcc.org/products/27806',
  'files':['search-original-specific-8.json','original-primary-attempts-9.json'],
  'read_extent':'Current repository search preview offered different growth media; direct page timed out. No original 0.02%Tween80 recipe inspected.',
  'claim':'No source bridge from current growth-media listing to legacy PYG-0.02%Tween80 established.',
  'scope':'Discovery/access evidence only, not chemistry proof.'}
}
for k,d in source_details.items():
 d['source_id']=k
 d['files']=[{'path':f,'sha256':sha(A/f)} for f in d['files']]
 d['recorded_at']=NOW
put('source-evidence-catalog.json',list(source_details.values()))

details={
 'Fastidious_Anaerobe_Broth_With_Meat_Granules':(['FAB_ORIGINAL','NEOGEN_NCM0199','ACUMEDIA7110'], 'Source-specific vendor discrepancy confirmed; a current LabM/Neogen formula cannot support original Oxoid-attributed FAB. Peptone composition and granule product remain unresolved.', 'Original FAB catalogue/formula and historical product identity; do not substitute the separate Anaerobe Systems PYG broth.', 'Compose with existing cooked-meat/granule withdrawal proposal; preserve its exact correction and all uncertainty. New finding PEPTONE-SOURCE-001 requires coordinator issue-first disposition.'),
 'PY-cellobiose':(['MOORE1976','POLYSACCHAROLYTICUM1980','BERGEY_ORIGINAL'], 'E.siraeum original paper supports occurrence-bound peptone basal-medium class; C.polysaccharolyticum is a separate source occurrence with unread formulation. No whole-owner generic or product identity established.', 'Resolve the C.polysaccharolyticum PY-cellobiose recipe or separate occurrence ownership; historical PY manual recipe remains unread.', 'No supplier detail is demanded for genuine generic peptone. One supported occurrence is insufficient for both observations.'),
 'PY-fructose':(['ANDREESEN1970','BERGEY_ORIGINAL'], 'Original C.formicaceticum paper abstract inspected; it does not spell out the inherited peptone component. PY abbreviation alone does not establish the material edge.', 'Original PY-fructose preparation/formulation for C.formicaceticum; subscription full text unavailable in this bounded free review.', 'Retain raw PY-fructose label, inherited expansion provenance and missing quantities.'),
 'PY-glucose-rumen_Fluid':(['SMIBERT1984','BERGEY_ORIGINAL'], 'Exact raw context is T.socranskii (source LPSN subspecies paredis). Inspected original-paper abstract lacks peptone specification; unrelated Prevotella research is not applicable.', 'Original PY base/digest in the stated Treponema preparation, or a primary recipe with a demonstrated source bridge.', 'Compose with literal rumen fluid UNMAPPED correction under #204/#1204; never restore clarified rumen fluid.'),
 'PY-maltose':(['MOORE1976','DSMZ104C_DSM753','BERGEY_ORIGINAL'], 'Original C.leptum PY-maltose experiment verified; referenced manual formulation unread. Current exact-strain repository recipe has two distinguishable peptones and cannot identify the inherited single edge.', 'Original manual recipe and which peptone constituent the historical single component was intended to represent.', 'Retain current recipe as comparator, not an instruction to inject quantities or collapse two digests.'),
 'PY-pectin':(['SMIBERT1983','ATCC1223','BERGEY_ORIGINAL'], 'Original T.pectinovorum source identified; full historical formula unread. Authentic ATCC1223 specifically uses Polypeptone BD211910, but no bridge to original PY-pectin is demonstrated.', 'Original PY-pectin ingredient list or historical identity linkage to ATCC1223.', 'Do not turn Polypeptone comparator into Bacto Peptone, Hipolypepton, or a broad product-family approval.'),
 'PYEG':(['MORRIS1985','BERGEY_ORIGINAL'], 'Exact raw taxon is C.scindens. Existing research citation leads concern other taxa (including Caulobacter); publisher original study abstract does not resolve PYEG ingredient identity.', 'C.scindens original PYEG preparation, including whether the abbreviation denotes the inherited three-component interpretation.', 'The retained peptone label remains an inherited interpretation, not a newly observed ingredient.'),
 'PYG-002_Tween_80':(['BIFORMIS_CURRENT','BERGEY_ORIGINAL'], 'Exact source observation is Holdemanella biformis (legacy Eubacterium biforme). No inspected original formulation establishes the inherited peptone edge; current alternative growth media are not the observed recipe.', 'Original E.biforme PYG-0.02%Tween80 base recipe and source applicability.', 'Preserve 0.02% as raw label information; no new quantitative component assertion inferred from it.'),
 'PYG':(['BERGEY_ORIGINAL','MOORE1976'], 'All114 raw observations were accounted for across multiple genera/chapters. Inspected occurrence-limited papers and a general DSMZ/VPI association do not establish one shared formula or digest identity for the aggregate owner.', 'Occurrence-specific recipe binding or supported disjoint formulation cohorts for114 observations; this bounded task does not claim exhaustive retrieval of114 papers.', 'Do not promote a single occurrence or comparator to all114 uses; no source-global Bacto assignment.'),
 'PYG_Rumen_Fluid':(['RUMINANTIUM1959','BERGEY_ORIGINAL'], 'Exact raw source taxon is E.ruminantium. Original source chapter inaccessible and original-paper body challenge-blocked; existing interpretation does not establish a digest material identity.', 'Original E.ruminantium PYG-rumen base formulation; later unrelated Prevotella cultures do not bind it.', 'Compose with literal rumen fluid UNMAPPED correction under #204/#1204; retain native scope/method uncertainty.')
}
ledger=[]; candidatepins=[]
for c in claims:
 path=Path(c['before_owner_path']); name=path.stem; owner=yaml.safe_load((R/path).read_text()); index=int(re.search(r'\[(\d+)\]',c['claim_key']).group(1)); src,summary,missing,composition=details[name]
 rows=[o for o in observations['rows'] if o['owner_path']==str(path)]
 assert rows
 assert owner['components'][index] == c['before_component']
 candidates=[]
 for version in c['existing_published_consumer_versions']:
  p=C/'preflight/final-intake-candidate-v1/snapshot/workers/w05'/version['git_path']; assert sha(p)==version['payload_sha256']; v=dict(version,path=str(p),independently_rehashed_sha256=sha(p),scientific_approval=False); candidates.append(v); candidatepins.append(v)
 for version in c['combined_consumer_candidates']:
  p=Path(version['source_path']);assert sha(p)==version['candidate_sha256'];v=dict(version,independently_rehashed_sha256=sha(p),scientific_approval=False);candidates.append(v);candidatepins.append(v)
 ledger.append({
  'claim_key':c['claim_key'],'owner_path':str(path),'owner_before_sha256':sha(R/path),'component_index':index,'before_component':owner['components'][index],
  'before_assertion':owner.get('component_assertion'),'original_source_observation_count':len(rows),'original_observations':rows,
  'source_evidence_ids':src,'assessment':summary,'scientific_disposition':'HOLD_EXACT_COMPONENT_IDENTITY_WITH_REVIEWED_MINIMAL_WITHDRAWAL',
  'whole_claim_generic_identity_supported':False,'specific_product_identity_supported':False,'occurrence_bound_generic_support':name=='PY-cellobiose',
  'supported_occurrence_limit':{'csv_row_including_header':5908,'taxon':'Eubacterium siraeum','support':'Peptone medium at that occurrence; no formulation/product/whole-owner approval.'} if name=='PY-cellobiose' else None,
  'precise_unresolved_fact':missing,'minimal_withdrawal_recommendation':{'component_name':'peptone','component_name_status':'Retain existing interpreted label, not newly asserted direct source observation.','component_id':'REMOVE_UNSUPPORTED_RESOLVING_ID','reference_scope':'UNMAPPED','quantities':'Preserve current absence; do not invent.','provenance':'Append narrow explanation preserving every historical assertion and original raw label. Preserve ABBREVIATION_EXPANSION/CURATED_INTERPRETATION method and UNKNOWN/PARTIAL completeness.'},
  'coupled_requirements':composition,'candidate_contexts_rehashed':candidates,
  'origin_constraint':'W05 causal generic-peptone source case may motivate a dependent child; it is not evidence that the child recipe occurred in that source case. Authentic child-origin and exact successor review remain required.',
  'source_case_accepted_for_integration':False,'whole_owner_approved':False,'role_approved':False,'supported_export_approved':False,
  'reviewer':'/root/peptone_ambiguous_sources','peer_review_required':'/root/peptone_skeptic (separate sibling agent; final assessment maintained separately by parent)',
  'author_related_to_previous_worker03_dependency_audit':True,'worker03_own_proposals_approved':False})
put('per-claim-scientific-ledger.json',{'schema_version':'1.0.0','reviewer':'/root/peptone_ambiguous_sources','completed_at':NOW,'scope':'Exact ten ambiguous peptone component claims; full owner/recipe approval excluded.','coverage':{'claims':10,'owners':10,'source_observations':124,'pyg_observations':114,'original_full_papers_exhaustively_read':0},'claims':ledger})
put('candidate-context-pins.json',candidatepins)

finding={
 'finding_id':'PEPTONE-SOURCE-001','issue_key':'MediaIngredientMech:Fastidious_Anaerobe_Broth_With_Meat_Granules:FAB-source-applicability',
 'status':'CONFIRMED_REPORTED_TO_ROOT_BEFORE_ANY_FIX','severity':'major','native_rule':'MAPPING_SEMANTICS sections3 and6; record-review evidence scope',
 'affected_claims':[claims[0]['claim_key']], 'owner_before_sha256':claims[0]['before_owner_sha256'],
 'affected_fields':['component_assertion.evidence[0].notes','components[1].component_id','historical research/decomposition provenance (preserve)'],
 'title':'Fastidious source attribution uses LabM/Neogen without a bridge to the original Oxoid-attributed preparation',
 'description':'The inherited active assertion identifies a LabM/Neogen FAB basis. The matched original Fastidiosipila sanguinis paper instead attributes FAB to Oxoid. Its separate Anaerobe Systems PYG fermentation broth must not be substituted as FAB composition. Exact historical FAB formula remains unresolved; the comparator discrepancy does not itself prove that peptone is absent.',
 'evidence_ids':['FAB_ORIGINAL','NEOGEN_NCM0199'],
 'reproduction':[
  'Verify beforeimage SHA256 aa56347529508fd0c082571cfd39540c6ac3205ba587c992594015c1e881c6a5; inspect component_assertion and source-research notes for LabM/Neogen.',
  'Verify original-source-read-7.json hash against source-evidence-catalog.json; inspect archived original-paper mirror paragraph p854 (web extraction turn62view3 line26) for explicit Fastidious Anaerobe Broth (Oxoid).',
  'Check original-paper publisher DOI/title metadata in original-paper-pages-web.json; no publisher PDF is claimed read.',
  'Verify preserved NCM0199 original PDF hash3ca3efc02a4a025b34ecb3126924fdb8d6fdfe011ba5a1d543af01a344268354 and read named manufacturer scope. No equivalent historical Oxoid recipe bridge is established.'
 ],
 'bounded_proposed_fix':'Coordinator deduplicates against #1176/#1193 before author work. In an authentic separately reviewed dependent successor, withdraw unsupported resolving peptone ID to UNMAPPED while retaining inherited literal peptone/provenance; append source-applicability correction and explicitly mark Neogen comparator unselected. Preserve raw FAB-with-meat-granules observation and all historical research text. Do not invent an Oxoid catalogue number or replace all composition from a current comparator. Compose with existing meat-granule withdrawal, preserving all other unreviewed component assertions as holds.',
 'acceptance_checks':['Exact owner/candidate beforeimage binding; source explanation cites archived p854 text and access limits.','No promotion of comparator or of separate PYG medium to FAB ingredient proof.','Existing cooked-meat/granule UNMAPPED repair retained; no starch/glucose or quantity invention/deletion from this bounded fix.','No component_id remains under peptone if identity unresolved; native schema/partonomy and exact-successor independent review pass, without whole-owner approval.'],
 'dedup_context':['https://github.com/CultureBotAI/MediaIngredientMech/issues/1176#issuecomment-6719248666','https://github.com/CultureBotAI/MediaIngredientMech/issues/1193'],
 'github_mutation':False,'fix_applied':False,'reported_to_root_before_fix':True,
 'independent_confirmation':'/root/peptone_skeptic independently read exact archived Falsen passage and confirmed discrepancy by in-process message; its final review is separate.'}
put('confirmed-findings.json',{'findings':[finding]})

inputs=[]
for p in [R/'MAPPING_SEMANTICS.md',R/'.claude/skills/review-yaml-category/SKILL.md',R/'docs/record-reviews.md',R/'docs/record-review-profile.md',R/'conf/record_review.yaml',C/'preflight/final-component-dependency-plan-v1/HANDOFF.json',C/'preflight/final-component-dependency-plan-v1/minimal-couplings-28.json',C/'preflight/final-component-dependency-plan-v1/source-evidence-refcheck-32.json',C/'preflight/final-component-dependency-plan-v1/source-bindings.json',C/'preflight/final-component-dependency-plan-v2/ROUTES.md']:
 inputs.append({'path':str(p),'sha256':sha(p)})
put('input-pins.json',inputs)
put('access-and-limitations.json',{
 'completed_at':NOW,'reviewer':'/root/peptone_ambiguous_sources',
 'bounded_local_search':'Ignored and hidden files included for named record/research artifacts in current W03 tree, prior W03 science-b dependency audit, W05 correction1193 snapshot, and main repository research/ingredients. No claim all private or historical files absent; no credentials searched.',
 'existing_research_status':'Main repository research citations and inherited record claims read as leads; multiple citations describe other taxa. Existing source text has not been promoted from LLM report to inspected publication.',
 'source_observation_verification':'124 selected observations independently rebound to original microbedecoder ZIP/member, Latin-1 decoded losslessly; original labels/taxa/DOI fields retained exactly. Original source chapters may remain unavailable.',
 'direct_attempts':[json.loads(p.read_text()) for p in sorted((A/'captures').glob('*.capture.json'))],
 'web_capture_semantics':'Archived JSON files contain exact returned web-tool text, including tool source identifiers and access errors. They are extracted-source representations, not raw publisher response bodies. Recording times are file-write times; publication dates and crawler dates are not access timestamps.',
 'web_files':[{'path':str(p.relative_to(A)),'sha256':sha(p),'recorded_file_at':datetime.datetime.fromtimestamp(p.stat().st_mtime,datetime.timezone.utc).isoformat()} for p in sorted(A.glob('*.json')) if p.name.startswith(('search-','original-source-read-','original-primary-','original-paper-','original-fulltext-','pdf-access-','moore1976-'))],
 'unread_materials':['Anaerobe Laboratory Manual3rd1975 and4th1977 full recipe text','Complete Clostridium/Treponema/Eubacterium Bergey chapter recipe bodies','Morris1985, Smibert1983, Smibert1984 original full methods','Andreesen1970 subscription full text','Bryant1959 original body (PMC challenge)','Original E.biforme PYG0.02%Tween80 recipe','C.polysaccharolyticum1980 full recipe'],
 'controls':'No raw HTML403 capture, publisher abstract, search preview, unrelated taxon recipe, current comparator, native schema PASS, or abbreviation expansion is accepted as exact legacy product proof.',
 'paid_or_provider_calls':0,'external_agent_sessions':0,'maintained_or_candidate_writes':0,'github_mutations':0,
 'native_validation':'Parent owns all20 native review/schema synthesis; this subagent did not rerun full-repository QC or claim its source ledger is native schema certification.'})
print(json.dumps({'claims':len(ledger),'observations':len(observations['rows']),'findings':1,'source_catalog_entries':len(source_details),'ledger_sha256':sha(A/'per-claim-scientific-ledger.json'),'finding_sha256':sha(A/'confirmed-findings.json')},indent=2))
