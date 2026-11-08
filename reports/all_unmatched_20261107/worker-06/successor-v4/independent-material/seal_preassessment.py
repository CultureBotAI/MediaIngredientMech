from pathlib import Path
import datetime,hashlib,json,subprocess
O=Path(__file__).resolve().parent;W=O.parents[2];C=W.parents[2]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(n,x):
 with (O/n).open('x') as f:json.dump(x,f,indent=2,ensure_ascii=False);f.write('\n')
current=json.loads((O/'current-selector-dedup.json').read_text());term_hits=[]
for row in current['selected_payloads']:
 b=subprocess.check_output(['git','show',f"{row['head']}:{row['published_path']}"],cwd=W)
 assert hashlib.sha256(b).hexdigest()==row['sha256']
 if any(s in b.decode().casefold() for s in ['c84042','o2zup321u8']):term_hits.append(row)
save('current-selector-term-reference-check.json',{'reviewer':'/root/residual_material_review','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'selector_receipt_sha256':sha(O/'current-selector-dedup.json'),'full_payload_count':len(current['selected_payloads']),'anywhere_ncit_or_unii_reference_matches':term_hits,'interpretation':'Checks full selected payload texts, including ontology mappings, evidence and histories, beyond resolving identity fields. No global ontology absence claim.'})
sources=json.loads((O/'primary-read-receipts.json').read_text())
ontology=json.loads((O/'live-specific-terms/receipts.json').read_text())
assessment={
 'schema':'w06-material-independent-science-preassessment-v1',
 'reviewer':'/root/residual_material_review',
 'author':'/root',
 'independence':'Reviewer did not author predecessor records, decisions, candidate YAML or candidate mapping. Reviewer independently inspected primary bodies, native contracts/catalogue, explicit coordinator selected payloads and official ontology responses. This receipt supplies constraints and does not approve a yet-unseen final payload.',
 'recorded_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'scope':['W06 case82 apple pectin identity/representation/source outcome','W06 case161 three YNB context outcomes'],
 'source_receipts':sources,
 'new_official_ontology_queries':ontology,
 'dedup':{'current_selector_sha256':current['selector_sha256'],'selected_payload_count':len(current['selected_payloads']),'selected_apple_identity_matches':len(current['apple_or_ncit_identity_matches']),'selected_ncit_anywhere_matches':len(term_hits),'catalogue_counts':[r['yaml_count'] for r in current['native_catalogue']],'catalogue_apple_or_ncit_matches':[len(r['apple_or_ncit_identity_matches']) for r in current['native_catalogue']],'ignored_files_included':True,'prior_and_coordinator_candidate_receipts':['proposal-duplicate-search.json','historical-intake-search-v2.json'],'acceptance_limit':'A source-publication selector identifies the duplicate-search scope; it grants no whole-owner/role/application/export approval. Later pending heads are not silently accepted.'},
 'apple':{
  'primary_assessment':'Complete M2313 captured body specifies apple pectin separately from citrus-peel pectin in the one-of carbon-substrate alternatives. The 0.2% amount belongs to an alternative, not to a simultaneous 19-component stock; the percent basis is unspecified. A source-qualified apple material is supported without supplier or exact esterification/grade.',
  'ontology_assessment':'Official NCI EVS 26.10d marks NCIT:C84042 Pectin, Apple active/default, under generic Pectin C63647, with NCI Apple Pectin synonym and FDA/UNII naming provenance. OLS confirms its label, nonobsolete state and exact synonym scope. This supports the bounded apple-origin material identity under MAPPING_SEMANTICS section3 first applicable exact-term rule. CHEBI:17309 remains generic; its apple-related synonyms and NCIT CHEBI annotation do not establish generic-pectin exact identity.',
  'safe_identity':'NCIT:C84042',
  'safe_ontology_label':'Pectin, Apple',
  'safe_mapping_predicate':'EXACT_MATCH',
  'mapping_method':'New mapping is an LLM-assisted evidence assessment; do not claim MANUAL_CURATION or automated exact label match.',
  'preserve':['Exact raw label pectin (apple)','Frozen source case and single CM occurrence binding','Original primary capture bytes, evidence ID and retrieval timestamp','New ontology captures retain their actual new query times','Genuine null-before record origin and independent review'],
  'do_not_infer':['Generic CHEBI exact identity','CAS 9000-69-5 as apple-specific registry identity','NCIT chemical formula as source sample formula','Malus pumila species assertion from an ontology synonym','supplier or catalogue','grade/purity/degree of esterification','physical dry form, solvent or component list','0.2% w/v, mass, final volume or simultaneous use of all alternatives','carbon-source role approval or whole-owner/export approval'],
  'further_hold':'Exact product/sample characterization remains unknown; this does not defeat the evidenced source-qualified material representation.'
 },
 'ynb':{
  'J240':{'known':'Yeast Nitrogen Base, BD-Difco, 1g in captured receiving recipe','primary_location':'/data/solutions/0/recipe/2','remaining_unknown':['exact formulation variant','catalogue','amino-acid inclusion','ammonium-sulfate inclusion']},
  'DSMZ1682':{'known':'Yeast Nitrogen Base,6.7g; supplier attribute absent','remaining_unknown':['supplier','exact formulation variant','catalogue']},
  'DSMZ1837':{'known':'Yeast Nitrogen Base,6.7g; supplier attribute absent','remaining_unknown':['supplier','exact formulation variant','catalogue']},
  'bounded_outcome':'Correct which facts are missing per receiving source. Preserve all three exact doses and do not collapse unspecified products into a common variant or transfer J240 manufacturer into the two other recipes. These are contexts of one frozen KG case, not new CM occurrences.'
 },
 'verdict':'PREAUTHOR_CONSTRAINTS_COMPLETE_FINAL_PAYLOAD_REVIEW_PENDING',
 'findings':[],
 'no_release_approval':True
}
save('preauthor-science-assessment.json',assessment)
files=[]
for p in sorted(O.rglob('*')):
 if p.is_file() and not p.name.startswith('preauthor-MANIFEST'):files.append({'path':str(p.relative_to(O)),'sha256':sha(p),'bytes':p.stat().st_size})
save('preauthor-MANIFEST.json',{'schema':'w06-independent-material-preauthor-manifest-v1','created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':files,'limit':'Immutable preauthor snapshot; final exact payload review will add separate successor files, not rewrite these files.'})
print(json.dumps({'assessment_sha256':sha(O/'preauthor-science-assessment.json'),'manifest_sha256':sha(O/'preauthor-MANIFEST.json'),'files':len(files),'selected_payloads':len(current['selected_payloads']),'ncit_reference_matches':len(term_hits)}))
