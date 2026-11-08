"""Seal the independent organic receipt after the recorded scientific reading."""
import collections, datetime, hashlib, json, pathlib
R=pathlib.Path('reports/all_unmatched_20261107/worker-08')
S=R/'successors/issue-1227-v1'; A=S/'research/organic_products'; O=S/'independent-review/organic_products'
Q=pathlib.Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(n,x):
 p=O/n;assert not p.exists(),p;p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
H=read(A/'PRIMARY-HANDOFF-v3.json');D=read(A/H['final_selection']['decisions'])['decisions'];P=read(A/H['final_selection']['proposals'])['proposals']
E={x['evidence_id']:x for x in read(R/'successors/issue-1201-v1/evidence.json')['evidence']+read(A/H['final_selection']['evidence_additions'])['evidence']}
used=sorted({i for x in D+P for i in x['evidence_ids']})
events=[json.loads(l) for l in (O/'read-events.jsonl').read_text().splitlines()]
scope_by_name={
 'web-ontology-1.json':'Captured ChEBI betaine, nalidixic-acid and methanethiol identity/structure sections; separate ECHA403 failure. This is the stored response scope, not every page on those sites.',
 'web-ontology-2.json':'Captured ethane, methane, isovaleric-acid and thymidine-monophosphate term definitions/properties and relations.',
 'web-ontology-3.json':'Captured valeric-acid, sodium-stearate, sodium-lactate, NAD(+), glycylglycine, ferric-pyrophosphate and trehalose identity/property/relationship sections, including their bounded page windows.',
 'web-additional-compounds.json':'Captured laminarin/PQQ/Asparagine supplier/ontology identity sections. Primocarcin abstract only; chlororaphin first-page/first65line material only. Cytovirin JavaScript-limited response is not structure verification. No full papers claimed.',
 'web-supplier-2.json':'Thermo Soytone product identity; Sigma HOMOPIPES identity; MES hydrate supplier identity; NIST sodium-nicotinate formula/CAS. Failed Se-acid request is negative retrieval evidence only.',
 'web-recipes-1.json':'Complete captured DSMZ672 alternatives, JCM1385 pointer, JCM906 formulation, CCAP NCL recipe. Failed initial FCGM request superseded by the separately read actual one-page PDF.',
 'web-recipes-2.json':'Complete captured JCM1130 VFA, JCM393 sodium-nicotinate, JCM600 toluene and DSMZ88 ore contexts. DSMZ60 is a comparison, not the assigned ore recipe.',
 'web-chemical-final.json':'ChEBI nicotinic-acid identity and Sigma B2629 betaine product/chemical sections. Site navigation and unrelated marketing do not provide chemical evidence.',
 'web-source-compounds.json':'MediaDive Se-acid and DL-asparagine raw label/automatic cross-reference disclaimer; specific S-lactone-anion comparator. Failed opens are not source identity proof.',
 'web-products-final.json':'HiMedia R2A-broth composition table and Sigma USP-thioglycollate comparator inspected as alternatives only. Denger search/abstract passage is superseded for scientific reliance by the actual institutional PDF Methods read recorded below.',
 'web-source-final2.json':'Actual NBRC1045 complete short recipe; exact NBRC957/MediaDive1465/DSMZ560 failure messages. Search discoveries and third-party catalogue prose are not relied on as assigned identity evidence.',
 'web-source-final3.json':'TCI M1893 methyl6-methylnicotinate product identity/formula/CAS section; contrast with the ambiguous automatic source cross-reference. Unrelated DSMZ production lists and failed flour request are not independent structure/formulation proof.',
 'primary-facts.json':'All bounded factual entries read, with underlying JCM906/JCM600/DSM88 actual recipes and Wako/TCI/ChEBI scope independently inspected. These paraphrases are not treated as primary authority by themselves.',
 'additional-primary-facts.json':'All bounded entries read. Actual ATCC474/177 PDFs, Denger/Roy Methods, FAO TSB table, official ontology terms and supplier identity sections were separately read; distinct product/scratch alternatives remain distinct.',
 'nalidixic-web-read.json':'Entire actual NBRC1301 captured recipe and the NBRC1314/M2023 inaccessible responses; only1301 is positive primary evidence.',
 'capture-retention.json':'Entire relocation/provenance receipt. Original URLs, original timestamps or explicitly date-only precision and exact private hashes are preserved, not assigned this review time.',
 'owner-search.json':'Search scope and relevant candidate paths/identity excerpts inspected. This is a candidate-finding aid, not approval of every match or a scientific absence proof.',
 'owner-lookup.json':'Ignored-inclusive search scope and relevant owners compared with the actual complete selected owners, frozen beforeimages and no-delta owners. Unrelated textual matches are not identity evidence.',
 'ontology-lookup.json':'Recorded SQL/query scope and relevant chemical candidates inspected; broad substring returns contain unrelated terms. No global ontology absence claim is made. NCIT exact CAS lookup was independently rerun read-only.',
 'peer-remediation-v2.json':'Original DL-asparagine parent-direction remediation and exact old/new binding read as historical lineage, not self-authorizing scientific evidence.',
 'category-correction-ledger.json':'All mapping assertion classifications read and compared with actual whole payloads. Human-supplied inherited entries and the distinct ComponentEvidence enum are excluded from blanket rewriting.',
 'correction-ledger.json':'All31 selected entries/actions and held boundaries read; final v3 R2A method successor takes precedence over this preserved v2 metadata.',
 'dependent-reference-inventory-v2.json':'Scope and relevant identity/dependency rows inspected; independent ignored-inclusive component scan confirms no old/new NCIT component dependents. Serialized historical/export references are integration obligations, not rewritten here.',
 'ncit-native-resolution.json':'Native function/result metadata read; independently queried same exact read-only ontology database and official OLS term. No claim that independent SQL is a native full-label gate.',
 'cas-lookup.json':'Exact CAS query/source metadata read and query independently rerun against the bound NCIT database.',
 'pyruvate-primary-binding.json':'Full binding read and exact original official MICRO0000541 definition examined; separate agar-source annotation excluded from liquid-medium inference.',
 'new-finding-referrals-v3.json':'All routed soy-grade, R2A-pyruvate and plain-flour corrections read against raw source and final owner. These preceded author execution.',
 'peer-remediation-v3.json':'Full author remediation binding read, entire v3 R2A YAML reread and exact semantic delta independently verified.'
}
entries=[]
for eid in used:
 e=E[eid];cap=e['capture'];p=(R if cap['root']=='artifact' else Q)/cap['path'];assert sha(p)==cap['sha256']
 status='scientific_scope_read';name=p.name
 if eid.startswith('op-case-'):
  scope='Entire assigned frozen case, complete original KG source record or every CM occurrence raw field, source label and occurrence identifiers read. Only assigned cases in this shard capture are claimed.'
 elif eid.startswith('op-context-'):
  scope='Complete recipe scientific context read: input names, quantities, nested solutions and preparation notes. Bookkeeping histories, unrelated target-organism annotations and imported ontology enrichments are not primary chemistry evidence.'
  if 'nldm_' in name:scope='All ingredient names/quantities in the first NLDM context, exact name/quantity differences across all ten variants, every complete Trimethylglycine occurrence and top-level preparation/source notes inspected. Unrelated other-ingredient imported mapping notes were not used.'
  if 'rs_medium_nutrient' in name:scope='Entire assigned L-Asparagine hydrate occurrence and all ancestor stages: MEM100X seven-input list,2.27mL per50mL Mix4,10.9mL per150mL final NM, top preparation notes. Other P5 stock fields were read in context; no approval of unrelated unresolved carbon-source conflicts is claimed.'
  if 'mtp4_' in name:scope='Entire assigned methanethiol occurrence, archived DSMZ560/195/193 source-expansion notes, all input names/quantities and relevant gas/preparation context; current DSMZ560 request unavailable.'
 elif '/owners/' in cap['path'] or cap['path'].endswith('.yaml'):
  scope='Entire relevant frozen owner/preimage and history inspected, either directly or as fields byte-identical to the whole selected payload plus rendered beforeimage differences. Hash equality is separately recorded and is not the scientific review.'
 elif eid in ['op-search-search-targeted-final','op-search-search-unresolved']:
  status='discovery_only_not_relied_on_as_primary';scope='Recorded discovery queries/leads considered, not promoted to primary identity proof. Relevant primary targets were read separately; a result snippet or absence of a hit is not a global absence claim. No claim that every unrelated search-result body was read.'
 elif eid=='op-jcm1120-failed':status='unavailable_primary';scope='Actual short HTTP200 page says Nothing found; no ethane preparation evidence is present.'
 elif eid=='op-shared-failed-retrievals':status='retrieval_failure_read';scope='Exact DSMZ560 PDF record inspected:2026-11-08T05:16:12.135437+00:00 HTTP404. No current PDF reading claimed; separate archived frozen MTP4 witness retained.'
 elif eid in ['op1227-failed-nbrc1314','op1227-failed-togo2023']:
  status='unavailable_primary';scope='Actual inaccessible response read. Exact occurrence remains source-held; readable1301 cannot substitute for this unavailable source.'
 elif name in scope_by_name:scope=scope_by_name[name]
 elif e['kind']=='ontology':scope='Complete captured term/search response scientific fields read: canonical label, synonyms, definition, identity cross-references, formula and obsolescence where present. Empty bounded query responses are only no-hits for those queries, not global absence.'
 elif name.endswith('.pdf'):scope='Complete captured short recipe PDF read, including ingredient quantities and preparation instructions.'
 elif name.endswith('.html'):scope='Actual captured provider HTML scientific content read, including original label, recipe/product context and automatic cross-reference disclaimer where present; navigation is not chemical evidence.'
 elif name.endswith('.json') and any(s in name.lower() for s in ['togo','1894','mediadive']):scope='Entire actual primary JSON response read, including all input rows, comments and source identifiers.'
 else:raise AssertionError(('Unclassified read scope',eid,cap['path']))
 entries.append({'evidence_id':eid,'kind':e['kind'],'capture':cap,'url':e.get('url'),'original_accessed_at':e.get('accessed_at'),'source_locator':e.get('locator'),'read_status':status,'actual_read_scope':scope,'capture_hash_verified':True})

private=pathlib.Path('.temp/all-unmatched-worker-08/issue-1201-v1')
supplement=[]
def add(p,scope,locator,url=None,accessed=None):
 supplement.append({'path':str(p),'sha256':sha(p),'read_scope':scope,'locator':locator,'url':url,'original_accessed_at':accessed})
ret=read(R/'successors/issue-1201-v1/research/organic_products/sources/capture-retention.json')['entries']
for fname,scope,loc in [
 ('atcc-474.pdf','Complete one-page ATCC474 recipe, commercial BD211260 and separate additions.','page1'),
 ('atcc-177.pdf','Complete one-page ATCC177 recipe; commercial option and independently printed scratch alternative.','page1'),
 ('wako-dl-asparagine-monohydrate.pdf','SDS identity/composition pages1–2 read,2026revision; exact DLhydrate CAS/form. Remaining hazard sections not used as identity evidence.','sections1 and3'),
 ('sulfolactate-author.pdf','Actual Denger2010 title/abstract, Methods/Chemicals and growth-substrate context read. No fullarticle-reading claim.','pages1–2, pp967–968'),
 ('roy-2003-sulfolactate.html','Actual Roy2003 Methods/Chemicals and culture-substrate paragraphs read. No claim of complete article inspection.','Methods, Chemicals'),
 ('ols-micro-0000541.json','Complete official term response, especially literal liquid definition and distinct agar-source annotation.','/_embedded/terms/0'),
 ('ols-micro-0000113.json','Complete official term response including exact synonym and standard formulation scope. Lengthy third-party prose not republished.','/_embedded/terms/0')]:
 p=private/'private-primary'/fname;rr=next(x for x in ret if x.get('capture',x.get('private_capture'))==str(p));assert sha(p)==rr['sha256'];add(p,scope,loc,rr['url'],rr.get('accessed_at'))
for n,scope,loc in [
 ('d','TCI A0541 identity/formula/CAS contradiction and Wako2023 SDS identity sections read.','TCI product175–236; Wako sections1/3'),
 ('g','Complete captured DSMZ1003 two-page recipe read; Se-acid remains formula/oxidation-unspecified.','lines0–42'),
 ('l','ChEBI15245 parent/child relationship and BD211260 product identity/specification read; unrelated FAO tables not relied on.','ChEBI0–35; BD229–283'),
 ('m','Supplier DL-sodium-lactate identity/solid-versus60%solution contrast read.','relevant supplier identity sections'),
 ('n','Captured ChEBI sodium-lactate/ferric-pyrophosphate/PQQ properties and structure passages inspected.','relevant chemical term property sections'),
 ('o','Neutral dTMP term and exact FAO Trypticase Soy Broth formulation including glucose-free alternative read.','dTMP identity; FAO428–456')]:
 p=private/'organic_products/raw-web'/('web1201-'+n+'.json');add(p,scope,loc,accessed='2026-11-08 (date only retained by original capture; exact time unknown)')
for v in read(S/'root-primary/retrievals.json'):
 if v['id'] in ['MICRO:0000541','MICRO:0000543','MICRO:0000113']:
  add(pathlib.Path(v['path']),'Complete fresh official term capture read as supplemental identity/label evidence; this is official-primary fallback, not native MICRO adapter success.','/_embedded/terms/0',v['url'],v['accessed_at'])
for n in ['Soya_Pepton.yaml','Soya_Peptone.yaml','Bacto_Soytone.yaml','HOMOPIPES.yaml']:
 add(pathlib.Path('data/ingredients/mapped')/n,'Entire owner and full history read as sibling or component context; no new whole-owner or role approval.','entire YAML')
add(pathlib.Path('data/ingredients/unmapped/Amphotericin.yaml'),'Entire generic Amphotericin owner and history read; A/B/product ambiguity retained.','entire YAML')

ledger={'reviewer':'/root/inorganics','author':'/root/organics','scope':'All223 evidence entries referenced by the final51 cases/31 proposals, plus independently read original private sources and current ontology supplements. Scientific scope is explicit per entry; a verified SHA alone is never recorded as reading.','evidence_entries':entries,'supplementary_actual_reads':supplement,'limitations':['Unavailable NBRC1314/M2023 primary remains occurrence-held. Current DSMZ560 failed; archived frozen source witness is identified.','Primocarcin abstract and chlororaphin first-page capture were read only to their captured scope; full papers were not claimed.','Local lookup negatives are bounded queries, not global ontology absence. Historical author ledgers are contextual evidence and not independent approval.','Old R2A component-reference-assessment records LABEL_ENUMERATION as pre-v3 metadata. Exact v3 payload, peer-remediation-v3 and this review control the final assertion method.','Complete owner reading includes inherited concerns; bounded planning acceptance is not whole-owner, role or export approval.']}
write('source-read-ledger.json',ledger)

inputpaths=[A/'PRIMARY-HANDOFF-v3.json',A/'assignment.json']+[A/n for n in H['files']]
inputpaths += [S/'inputs/external-review/findings.json',S/'inputs/coordinator-triage/all113-payload-action-matrix.json',S/'inputs/coordinator-triage/completeness-adjudication-refinement.json',S/'inputs/coordinator-triage/complete-list-primary-proof.json',S/'inputs/issue1227-live-body.json',S/'inputs/issue1227-live-comments.json',S/'COORDINATOR-NEW-FINDINGS-v2.json',S/'root-primary/retrievals.json',R/'successors/issue-1201-v1/evidence.json',R/'provenance/shard-08.json']
input_hashes={str(p.relative_to(R)):sha(p) for p in inputpaths}
for e in entries:
 if e['capture']['root']=='artifact':input_hashes[e['capture']['path']]=e['capture']['sha256']
for n in ['source-read-ledger.json','findings.json','input-validation.json','case-appraisals.json','proposal-appraisals.json','independent-ncit-query.json','independent-dependent-reference-check.json','new-finding-referral-v1.json']:
 input_hashes[str((O/n).relative_to(R))]=sha(O/n)
for v in supplement:
 p=pathlib.Path(v['path'])
 if p.is_relative_to(R):input_hashes[str(p.relative_to(R))]=v['sha256']
review={'schema_version':'1','reviewer':'/root/inorganics','author':'/root/organics','reviewed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'authoritative_handoff':{'path':str((A/'PRIMARY-HANDOFF-v3.json').relative_to(R)),'sha256':sha(A/'PRIMARY-HANDOFF-v3.json')},'scope':'All51 assigned organic cases and all31 complete final selected owner payloads, not only changed fields. Authorship-separated from organic author. Inorganic scientific payloads and other cohorts are outside this receipt.','status':'complete_bounded_review_with_preserved_holds','case_ids':H['case_ids'],'proposal_ids':H['proposal_ids'],'case_hashes':H['case_hashes'],'payload_hashes':H['payload_hashes'],'input_hashes':input_hashes,'open_blocking_findings':[],'full_payload_review':True,'case_reviews':read(O/'case-appraisals.json')['case_reviews'],'proposal_reviews':read(O/'proposal-appraisals.json')['proposal_reviews'],'findings':read(O/'findings.json')['findings'],'inherited_concerns':read(O/'findings.json')['inherited_concerns'],'external_finding_lineage':read(O/'findings.json')['external_finding_lineage'],'source_read_ledger':{'path':str((O/'source-read-ledger.json').relative_to(R)),'sha256':sha(O/'source-read-ledger.json')},'validation':{'path':str((O/'input-validation.json').relative_to(R)),'sha256':sha(O/'input-validation.json'),'mechanical_checks_passed':len(read(O/'input-validation.json')['checks']),'scope':'Exact frozen input preservation, selected after/before/capture hashes, v3 semantic delta and independent read-only NCIT/dependency checks. Parent retains native assembly responsibility.'},'acceptance_boundary':['Accept only the source/identity/alias/provenance and component corrections individually appraised above for isolated planning.','All preserved source/role/WITHHOLD/REJECTED/export holds remain. Inherited pentanoate and soy-family concerns remain explicit.','No owner merge, corpus application, export approval, cross-shard winner selection or self-scientific approval is granted.','No failed or partially read primary source is presented as fully inspected.'],'whole_owner_role_supported_export_approved':False}
write('review.json',review)
summary={'review_sha256':sha(O/'review.json'),'source_read_ledger_sha256':sha(O/'source-read-ledger.json'),'findings_sha256':sha(O/'findings.json'),'input_validation_sha256':sha(O/'input-validation.json'),'cases':len(review['case_reviews']),'payloads':len(review['proposal_reviews']),'evidence_entries':len(entries),'supplementary_reads':len(supplement),'new_findings':1,'resolved_new_findings':1,'open_blocking_findings':0,'scientific_holds_preserved':True}
write('FINAL-HANDOFF.json',summary)
(O/'HANDOFF.md').write_text('Independent organic review complete: 51 source cases and 31 complete final payloads.\n\nAuthoritative author selection: PRIMARY-HANDOFF-v3.json. IF-OP1227-F1 was routed before author correction and resolved by exact v3 R2A re-review. All six parts and UNKNOWN closure are preserved.\n\nThe receipt accepts bounded planning claims with inherited source, role and export holds. It does not approve entire owners; pentanoate aliases and the soy-family identity remain explicitly held. Unavailable and partially read sources are identified in the source ledger.\n\nreview.json SHA256: '+summary['review_sha256']+'\nsource-read-ledger.json SHA256: '+summary['source_read_ledger_sha256']+'\nfindings.json SHA256: '+summary['findings_sha256']+'\n\nNo author artifact, maintained data, Git or GitHub state was changed. The coordinator owns native assembly and final integration.\n')
print(json.dumps(summary))
