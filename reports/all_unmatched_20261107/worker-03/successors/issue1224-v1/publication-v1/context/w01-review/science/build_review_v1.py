from inspect_inputs import *
from datetime import datetime,timezone
from collections import Counter
now=datetime.now(timezone.utc).isoformat()
bind=json.loads((R/'input-bindings-v1.json').read_text())
resolved=json.loads((R/'resolved-complete-inputs-v1.json').read_text())
def out(name,data):
 with (R/name).open('x') as f:json.dump(data,f,indent=2,ensure_ascii=False);f.write('\n')
def ref(p):
 p=Path(p);return {'path':str(p.resolve()),'sha256':sha(p)}
def objsha(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
# Keep original capture timestamps and their exact authority; a review timestamp is not a retrieval date.
evidence=[]
for e in bind['source_evidence']:
 assert sha(e['path'])==e['sha256'],e['evidence_id']
 matches=[]
 for w in [2,3,4,5,8,10]:
  p=Path(B[w]['evidence']);d=json.loads(p.read_text())['evidence']
  for q in d:
   if q['evidence_id']==e['evidence_id']:
    matches.append({'worker':w,'evidence_file':ref(p),'original_record':q})
 evidence.append({**e,'capture_metadata_authorities':matches,'timestamp_policy':'Original accessed_at is retained in original_record where supplied. Null/absent is not replaced by this review time. No fresh network retrieval was performed.'})
S=C/'preflight/existing-owner-scope-decisions-v1'
fresh=[]
for p in sorted((S/'fresh-primary').glob('*.body')):
 mp=p.with_suffix('.meta.json');m=json.loads(mp.read_text()) if mp.exists() else {}
 fresh.append({'evidence_id':'SCOPE-'+p.stem,'body':ref(p),'metadata':ref(mp) if mp.exists() else None,'original_capture_metadata':m})
out('source-ledger-v1.json',{'created_at':now,'source':ref(R/'input-bindings-v1.json'),'original_capture_count':len(evidence),'original_captures':evidence,'scope_advice_fresh_primary_captures':fresh,'scope_primary_index':ref(S/'primary-source-index.json'),'inspection_scope':'Complete applicable primary source tables and preparation descriptions; supplier PDF applicable product/general-method sections, not unrelated languages or products. Ontology full term/parent responses. Validation/search/review artifacts are provenance/context, not primary science or transferred approval.'})
# Exact case/occurrence coverage, full original objects and raw recipe elements are already in the resolved input.
case_map={};occ_map={};originals={};case_bindings=[]
for c in resolved['candidates']:
 for o in c['originals']:
  originals[o['origin']['entry_id']]=o['origin']
  for x in o['cases']:
   case_map[x['case_id']]=x
   for z in x.get('occurrences',[]):occ_map[z['occurrence_id']]=z
 for cid in c['case_ids']:
  os=[o for o in c['originals'] if cid in o['origin']['case_ids']]
  x=next(x for o in os for x in o['cases'] if x['case_id']==cid)
  case_bindings.append({'candidate_id':c['candidate_id'],'case_id':cid,'raw_source_label':x['raw_source_label'],'source_case_id':x['source_case_id'],'case_object_sha256_canonical_json':objsha(x),'original_decision_bindings':[{'entry_id':o['origin']['entry_id'],'decisions_file':{'path':o['decisions_path'],'sha256':o['decisions_sha256']},'decision_locator':'case_id='+cid,'original_decision_sha256_canonical_json':objsha(next(q for q in o['decisions'] if q['case_id']==cid)),'declared_case_input_sha256':next(q for q in o['decisions'] if q['case_id']==cid)['case_input_sha256']} for o in os],'source_shard':{'path':os[0]['source_shard'],'sha256':os[0]['source_shard_sha256']},'occurrence_ids':[z['occurrence_id'] for z in x.get('occurrences',[])],'dependency_only_backlink':c['candidate_id'].startswith('DEP-'),'comparison_only_for_Difco':c['candidate_id']=='TARGET-032' and x['source_case_id']=='CM0149 Broth (OXOID)'})
occurrences=[]
for oid,z in occ_map.items():
 p=C/'queue/preliminary-v5'/z['full_recipe_snapshot'];r=yaml.safe_load(p.read_text());assert sha(p)==z['source_file_sha256']
 node=r
 for tok in z['component_path'].split('/'):node=node[int(tok)] if isinstance(node,list) else node[tok]
 assert node==z['raw_component'],oid
 occurrences.append({'occurrence_id':oid,'original_occurrence_object':z,'recipe':ref(p),'component_matches_full_recipe':True,'scientific_use':'Read full recipe composition, nested-stock context and applicable preparation. Existing unrelated chemistry, role, unit normalization and organism claims are not newly approved.'})
copy_equivalence=[]
for e in bind['source_evidence']:
 if e['kind']=='source_snapshot' and e['path'].endswith('.yaml') and '/hardlinked-' in e['path']:
  original=Path(e['path']);authority=Path(e['resolved_capture_path']);equal=yaml.safe_load(original.read_text())==yaml.safe_load(authority.read_text());assert equal
  copy_equivalence.append({'evidence_id':e['evidence_id'],'original_worker_capture':ref(original),'frozen_source_authority':ref(authority),'complete_parsed_yaml_equal':equal,'note':'Byte hashes can differ because of serialization. Both exact bytes are bound; no silent repinning.'})
coverage={'created_at':now,'assignment':ref(C/'assignments/w01-nine-scope-candidates-independent-v1.json'),'counts':{'candidates':len(resolved['candidates']),'authentic_beforeimages':sum(c['before'] is not None for c in resolved['candidates']),'unique_original_worker_proposals':len(originals),'unique_source_cases':len(case_map),'unique_cm_occurrences':len(occ_map),'candidate_case_backlinks':len(case_bindings),'candidate_occurrence_backlinks':sum(len(c['occurrence_ids']) for c in resolved['candidates'])},'case_bindings':case_bindings,'occurrences':occurrences,'original_snapshot_serialization_checks':copy_equivalence,'limitations':['Dependency candidates carry the causal JCM266 case backlink; they are not additional assigned MicrobeDecoder observations.','TARGET-032 retains Oxoid case as historical comparison/provenance; NEW-OXOID-CM0149 owns its proposed product scope.','KG occurrence helper fields are not measured frequencies. Empty CM occurrence arrays do not prove no source observations.','Coverage is inspection accounting, not positive mapping, membership transfer or release acceptance.']}
out('coverage-v1.json',coverage)
# Short source excerpts, locators and scientific interpretations. Full bodies are immutable external inputs.
judgments=[]
def J(eid,locator,excerpt,interpretation):
 z=next((x for x in evidence if x['evidence_id']==eid),None)
 if z: cap={'path':z['path'],'sha256':z['sha256'],'url':z.get('url')}
 else:
  x=next(x for x in fresh if x['evidence_id']==eid);cap={**x['body'],'url':x['original_capture_metadata'].get('url')}
 judgments.append({'evidence_id':eid,'capture':cap,'locator':locator,'short_extract':excerpt,'review_interpretation':interpretation})
J('MATERIALS-CAP-5c0a089f5206be3d','meta.original_media_id; components; comments','Catalase (Sigma C--10); 60 mg','TOGO M109 links JCM_M117 and filtration. It supplies the literal historical catalog, not independently verified historical species or C100 equivalence. GMO annotation is not manufacturer species proof.')
J('MATERIALS-C1193-JCM117','complete body','Nothing found','The direct JCM retrieval is a failure and cannot support an attribution of successful direct inspection.')
J('BIO-PRIMARY-supp-8bb907b6a644b834','COA page 1 product and specific activity','CATALASE FROM BOVINE LIVER','C9322 bovine-liver lyophilized powder and 2,000–5,000 units/mg protein are product specification; 3190 units/mg and 86% protein are this lot results only.')
J('I1201-BIO-mesh-catalase-v2','descriptor URI and label','D002374; Catalase','Species-neutral enzyme descriptor is compatible with broad classification; not evidence for a human CAT sequence or all supplier equivalence.')
J('BIO-PRIMARY-de6aeb89029c0b8a','term definition','human CAT gene','Human 527-aa CAT protein is not established by generic enzyme reagent labels. Retain #312 exclusion.')
J('ROOT-jcm-266','clarified rumen fluid preparation paragraph','120°C for 15 min','JCM preparation heats contents and centrifuges 25,000 x g for 15 min; collect supernatant. Species is not supplied.')
J('a-primary-primary-09719ef2226161b4','clarified rumen fluid stock section','Clarified rumen fluid from medium 1310','Cow or sheep, muslin, 121°C/15 min, 27,000 x g/20 min, N2 and frozen storage describe a distinct source preparation; do not overwrite JCM handling.')
J('SCOPE-micro520','full term definition','fluid extracted from the rumen of a cow','Cow-specific exact target cannot identify a source-spanning, species-unspecified processed material.')
J('SCOPE-micro1898','full term definition and recipe citation','clarified rumen fluid for DSMZ Medium 1310','Specific DSMZ1310 preparation is not the generic/JCM owner. Species/protocol distinctions remain in source forms.')
J('SCOPE-micro1795','term label, definition, definition_source','Phytone peptone','Specific trademark/papaic soybean digest term; supplier corroborates soy. Erroneous Hordeum vulgare parenthetical is not adopted or treated as origin evidence.')
J('bio-primary-9abc0083911c4faa','components[0].items[8]; comments[0]','phytone (BBL)','Source names BBL product, 0.3 g with 100 mL water. Supports product identity; frozen receiving G_PER_L transcription is not recertified.')
J('MATERIALS-CAP-a1d17581eca50e64','PDF page 7; pages 33 and 36','strong acids, bases, or proteolytic enzymes','General peptone manufacturing allows different digestion methods. Page33 describes this manufacturer\'s enzymatic soy products; page36 gives distinct product SKUs. Neither establishes all unspecified MediaDive soy inputs as a specific product.')
J('SCOPE-micro1795-parents','MICRO:0000181 parent term definition/source','soy peptone','Term specifies mixed enzymatic soybean flour digest and has papaic/brand synonyms. Same label does not prove all generic source75 material has this process/scope; taxonomy typo is not by itself a reason to reject identity.')
J('MATERIALS-C1193-MEDIADIVE75','data ingredient name, CAS and synonyms','Soy peptone','Generic source names and imported CAS91079-46-8 do not independently certify manufacturer, process, grade or structure. Some frozen recipe attributes name example Soytone products; those do not make every unqualified use that product.')
J('MATERIALS-C1193-MEDIADIVE1466','data ingredient name and CAS','Soya pepton','Sibling generic record and CAS annotation do not resolve product/process equivalence or authorize an owner merge.')
J('MATERIALS-C1193-DIFCO-SOYTONE','catalog212489 product description','an enzymatic digest of soy','Supports Difco Soytone product context. Does not establish equivalence to Bacto Soytone, Phytone or every generic source75 input.')
J('M1193-DIRECT-110','manufacturer manual excerpt pages1–2, Formula and preparation','Approximate Formula* Per Liter','Nine printed inputs are supported as that Difco formula: peptone10, beef extract10, yeast3, dextrose5, NaCl5, starch1, cysteineHCl0.5, sodiumacetate3, agar0.5g. Adjustments allowed by source. No Tryptose, hydrate or invariant-lot inference.')
J('MEDIA-P104','ingredient1769 used attributes','BD-Difco (3×)','Supports original owner continuity at captured source scope, independently corroborated by JCM481/482/612. This displayed count is not a new frequency claim for all owner memberships.')
J('SCOPE-jcm481','complete medium table','Reinforced clostridial medium (BD-Difco)','38g product plus water and 30g sea salt are separate receiving inputs.')
J('SCOPE-jcm482','complete medium table','Reinforced clostridial medium (BD-Difco)','38g product plus water and 40g sea salt are separate receiving inputs.')
J('SCOPE-jcm612','complete medium table','Reinforced clostridial medium (BD-Difco)','38g product plus additional agar and water are separate receiving inputs.')
J('b-primary-b80f9ee369','NBRC902 complete composition','CM0149 Broth (OXOID)','38g product, 1L water, optional15g additional agar; source explicitly identifies Oxoid product, not Difco.')
J('b-targeted-b087f0859f30','IFU0539 English pages1–4; CM0149B/T table','Yeast extract 13.0','CM0149 current table has yeast13g/L, peptone10 and agar0.5, no beef. Distinct CM0151 table cannot be substituted. Historical NBRC source revision remains unknown.')
J('M1193-WEB-web-b4-0-182','captured search result BT-SPEC-0099, date12/04/12','REINFORCED CLOSTRIDIAL MEDIUM CM0149','Archived indexed supplier text shows yeast3 plus Lab-Lemco10. This is a search-response capture, not successfully retrieved original PDF; adequate to preserve revision uncertainty, not assign a historical lot formula.')
J('M1193-DIRECT-21','DSMZ634 complete recipe','BD-BBL, OXOID or MERCK','Alternative suppliers in a receiving medium do not establish product identity equality or let generic RCM resolve to one selected product.')
out('primary-scientific-assessments-v1.json',{'created_at':now,'assessments':judgments,'evidence_ledger':ref(R/'source-ledger-v1.json'),'attribution':'New independent interpretation by OpenAI Codex /root/primary_context of the bound original bodies, with earlier author/scope-review conclusions treated as hypotheses rather than approval.'})
