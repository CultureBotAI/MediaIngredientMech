import collections, datetime, gzip, hashlib, json, pathlib, re, subprocess

O=pathlib.Path('.temp/w05-tellurium-polypeptone-v1/review/membership-child')
S=pathlib.Path('.temp/w05-tellurium-polypeptone-v1/polypeptone')
REVIEWER='/root/final_skeptical/preservation_audit'
def sha(p): return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def objsha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
def save(name,x):
 p=O/name
 assert not p.exists(),p
 p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
d=json.loads((S/'input/polypeptone-context-subset.json').read_text())
f=json.loads(gzip.decompress(pathlib.Path(d['original_capture']).read_bytes()))
rows=d['owner']['exact_resolving_label_occurrences']
assert next(x for x in f['owners'] if x['path']==d['owner']['path'])==d['owner']
route={32:86,55:130,72:181,73:182,77:189,82:197,94:222,96:239,98:264,99:273,103:2,104:323,106:423,107:535,108:86,109:838,110:98,111:99,149:1467}
conflict={99,130,181,182}; unavailable={2,98}
ass=[]
for i,r in enumerate(rows):
 raw=r['preferred_term']; ing=json.loads(r['ingredient_json']); rec=f['current_complete_recipes'][r['source_path']]
 primary=[]
 if raw.startswith('Hipolypepton'):
  group='hipolypepton_raw_label';disposition='retain_distinct_Hipolypepton_source_boundary'
  conclusion='The supplied label is Hipolypepton, not evidence of the BD equal-parts casein/animal-tissue blend. Historical unsuffixed Nihon Hipolypepton is documented as casein-derived; current Shioya is a separately identified product. Preserve source qualifiers, asterisk, quantity and recipe context without assigning an unsupplied SKU.'
  missing='Recipe-specific product/version and any documented historical Nihon-to-current-Shioya continuity; common casein substrate does not prove equal preparation.'
  scope='Complete original occurrence row and ingredient object read. Manufacturer family comparison read; this row has no newly read originating NBRC/JCM recipe in this child scope.'
  primary=['wako.pdf','wako-japan.html','labology.html']
 elif 'BD' in raw or 'BBL' in raw:
  group='bd_bbl_raw_label';disposition='retain_brand_qualified_BD_candidate_scope'
  conclusion='Explicit BD/BBL qualifier is relevant positive brand-family context. The Thermo 2019 catalogue describes equal parts pancreatic casein digest and peptic animal-tissue digest. This is a candidate family link, not new primary approval of the source recipe or all generic labels.'
  missing='Recipe-version/procurement confirmation; '+('211910 is explicitly supplied and matches the manufacturer catalogue number, but no historical lot is established.' if '211910' in raw else 'no product catalogue number or lot supplied in this raw label.')
  scope='Complete original occurrence row and ingredient object read; direct manufacturer product page read, but no newly retrieved originating recipe for this row.'
  primary=['thermo.pdf','micro-polypeptone.json']
 elif i in route:
  group='nihon_polypepton_raw_label';n=route[i];primary=[f'jcm{n}.html','wako-2001.pdf','wako-2002.pdf','nihon-manufacturing-2007.pdf']
  if n in conflict:
   disposition='source_version_routing_conflict_preserved'
   conclusion=f'Frozen supplementary recipe says {raw}; current JCM{n} instead names Hipolypepton (FUJIFILM Wako). Historical conventional Nihon Polypepton is casein/porcine-enzyme based, distinct from the documented BD equal-parts blend. Preserve both source versions; the changed name is not evidence of the historical lot or an automatic synonym bridge.'
   missing='Historical recipe version/product record resolving the Polypepton-to-Hipolypepton substitution, and exact formulation/SKU continuity if an identity bridge is proposed.'
  elif n in unavailable:
   disposition='historical_named_route_retained_current_collection_unavailable'
   conclusion=f'Current JCM{n} says Nothing found. Captured MediaDive J{n} retains the Nihon Pharm. Co. attribute and original JCM URL. It corroborates the historical route; it is not a newly accessible originating JCM recipe. No redirect or substitute recipe is inferred.'
   missing=f'An accessible originating or archived JCM{n} recipe/version, and exact product specification if whole-owner equivalence is proposed.'
   primary += [f'mediadiveJ{n}.json',f'togoM{2 if n==2 else 90}.json',f'togoM{2 if n==2 else 90}-page.html']
  else:
   disposition='named_Nihon_route_confirmed_at_current_collection'
   conclusion=f'Current JCM{n} directly retains the Nihon Polypepton name and source batch quantity, supporting the named Japanese route. Historical manufacturer evidence identifies conventional Nihon Polypepton as casein/porcine-enzyme based. This supports separation from BD equal-parts casein/animal-tissue product, without proving every historical lot or exact equivalence to Hipolypepton.'
   missing='Exact product/version continuity if mapping a source-specific historical recipe to a specific maintained product owner; no SKU or lot is supplied by this recipe.'
  scope='Complete original occurrence/ingredient and complete scientific fields of the 23-recipe subset read; originating current JCM response independently read (including unsuccessful responses), with applicable manufacturer evidence.'
 else:
  group='generic_raw_label';disposition='retain_source_qualified_or_generic_unresolved_route'
  conclusion='Generic spelling alone does not establish BD or Japanese product identity. Preserve the original ingredient object, source qualifiers and quantity; do not map by a shared name or shared historical FOODON answer.'
  missing='Supplier/product/formulation version supported by the originating source; if that is known only through embedded historical evidence, preserve that attribution rather than erase it.'
  scope='Complete original occurrence row and ingredient object read. No newly read originating primary recipe is asserted for this row.'
  if i==20:
   conclusion='Although the raw label is generic Polypeptone, its exact ingredient evidence and notes explicitly state Nihon Pharm. Co. and 0.1 g per source batch. Current JCM197 independently confirms that qualifier and amount. It must not be treated as supplier-unspecified or assigned BD identity.'
   scope='Complete original occurrence/ingredient read; current originating JCM197 recipe independently read. Historical MediaDive excerpt retained with its original timestamp, not recaptured or reauthored.'
   primary=['jcm197.html','wako-2001.pdf','wako-2002.pdf']
  elif i==125:
   primary=['jcm2.html','mediadiveJ2.json'];scope+=' Current JCM2 unsuccessful response and MediaDive J2 crosscheck read: the latter independently carries Nihon Pharm. Co.; no supplier-free BD inference.'
  elif i==127:
   primary=['jcm98.html','mediadiveJ98.json'];scope+=' Current JCM98 unsuccessful response and MediaDive J98 crosscheck read: the latter independently carries Nihon Pharm. Co.; no supplier-free BD inference.'
 ass.append({'target_id':f'POLYPEPTONE-CONTEXT-{i:03d}','zero_based_original_row_index':i,'original_row_locator':f'owners[path=data/ingredients/mapped/Polypeptone.yaml].exact_resolving_label_occurrences[{i}]','row_sha256_canonical_json_utf8':objsha(r),'recipe_id':r['recipe_id'],'source_path':r['source_path'],'source_snapshot_path':rec['source_path'],'source_snapshot_sha256':rec['sha256'],'ingredient_locator':r['component_field']+'/'+r['component_index'],'raw_preferred_term':raw,'raw_concentration_value':r['concentration_value'],'raw_concentration_unit':r['concentration_unit'],'ingredient_object_sha256_canonical_json_utf8':objsha(ing),'original_row':r,'raw_label_partition':group,'disposition':disposition,'conclusion':conclusion,'precise_missing_fact':missing,'primary_read_scope':scope,'primary_capture_refs':[str(S/'captures'/x) for x in primary],'quantity_review_limit':'Preserved as supplied; no new concentration normalization or approval. Source-stock/batch quantities remain distinct from receiving-medium concentration.','whole_owner_or_export_approval':False})
counts=dict(collections.Counter(x['raw_label_partition'] for x in ass));assert len(ass)==150 and sorted(counts.values())==[8,19,25,98]
save('rows-150-v1.json',{'reviewer':REVIEWER,'source_capture':d['original_capture'],'source_capture_sha256':sha(d['original_capture']),'source_capture_original_inspected_at':f['inspected_at'],'canonical_hash_algorithm':'SHA256 of UTF-8 json.dumps(sort_keys=True,separators=(comma,colon),ensure_ascii=False)','counts_are_raw_label_partitions_not_primary_approvals':counts,'historical135_statistic_unchanged':d['owner']['record']['occurrence_statistics'],'row_assessments':ass})
rr=[]
for i,(p,r) in enumerate(d['complete_japanese_recipes'].items()):
 assert r==f['current_complete_recipes'][p]
 rr.append({'target_id':f'JAPANESE-RECIPE-{i:02d}','source_path':p,'source_snapshot_path':r['source_path'],'source_snapshot_sha256':r['sha256'],'complete_recipe_canonical_object_sha256':objsha(r['complete_recipe']),'row_target_ids':[x['target_id'] for x in ass if x['source_path']==p],'review_read_derivative':str(O/'read'/f'recipe-{i:02d}.json'),'review_read_derivative_sha256':sha(O/'read'/f'recipe-{i:02d}.json'),'actual_read_scope':'Complete scientific recipe fields including all ingredients, quantities, solutions, processing, source references and notes read for membership context. The complete original JSON was parsed and hash-bound; repetitive inherited evidence/history metadata outside the target ingredient was not recertified. Target ingredient evidence, where present, was read as part of each complete row.','assessment':'Recipe context does not justify folding the named Nihon component into the BD product blend. Preserve all raw forms, stock/batch scope and source version. No review approval of unrelated ingredient chemistry or imported quantity conversions.'})
save('recipes-23-v1.json',{'reviewer':REVIEWER,'complete_recipe_context_count':len(rr),'recipe_assessments':rr})
captures=[]
names=[f'jcm{x}.html' for x in [2,86,98,99,130,181,182,189,197,222,239,264,273,323,345,406,409,423,535,838,1028,1467]]+['thermo.pdf','wako.pdf','wako-2001.pdf','wako-2002.pdf','nihon-manufacturing-2007.pdf','wako-japan.html','labology.html','mediadive442.json','mediadive2060.json','mediadiveJ2.json','mediadiveJ98.json','togoM2.json','togoM90.json','togoM2-page.html','togoM90-page.html','micro-polypeptone.json','foodon.json','foodon-peptone-search.json','foodon-polypeptone-search.json','ontology-all-polypeptone-search.json']
pdfscope={'thermo.pdf':'Printed49 full product text/table/image; printed5 acquisition history and final96 copyright2019. No current2026 procurement claim.','wako.pdf':'Printed8 entire Hipolypepton description/table visually read; other page products only contextual.','wako-2001.pdf':'Printed15 manufacturer product comparison visually read. Conventional Polypepton milk-casein/porcine enzyme; NS enzyme is plant-derived in this version.','wako-2002.pdf':'Printed13 product comparison visually read. Conventional Polypepton milk-casein/porcine enzyme; NS enzyme is microbial-derived in this version.','nihon-manufacturing-2007.pdf':'Full extracted article117–121 read; Fig2 printed118 visually read: casein, enzyme, digestion, filtration, concentration, drying, packaging. No specified recipe lot or Hipolypepton SKU continuity.'}
for name in names:
 p=S/'captures'/name;rp=pathlib.Path(str(p)+'.receipt.json');receipt=json.loads(rp.read_text());assert sha(p)==receipt['sha256']
 captures.append({'path':str(p),'sha256':sha(p),'capture_receipt_path':str(rp),'capture_receipt_sha256':sha(rp),'capture_author':'/root/polypeptone_supplement','original_capture_url':receipt.get('url'),'original_accessed_at':receipt.get('accessed_at'),'original_completed_at':receipt.get('completed_at'),'original_http_status':receipt.get('http_status'),'independent_reviewer':REVIEWER,'read_scope':pdfscope.get(name,'Complete response text/data relevant to product/recipe identity read; no approval from hash matching.'),'original_bytes_and_timestamps_reused':True})
contracts=['MAPPING_SEMANTICS.md','.claude/skills/review-yaml-category/SKILL.md','docs/record-reviews.md','docs/record-review-profile.md']
issues=[pathlib.Path('.temp/w05-tellurium-polypeptone-v1/issues')/x for x in ['issue1202.json','issue1202-comments.json','issue1226.json','issue1226-comments.json','comment6718777428.json','comment6718777633.json']]
save('primary-read-ledger-v1.json',{'reviewer':REVIEWER,'author_of_captures':'/root/polypeptone_supplement','read_completed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'git_head_at_read':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),'captures':captures,'contracts':[{'path':x,'sha256':sha(x),'read_scope':'Sections3/6' if x=='MAPPING_SEMANTICS.md' else 'Complete current contract/skill'} for x in contracts],'issues':[{'path':str(x),'sha256':sha(x),'read_scope':'Complete body or all nested comment pages, including listed individual comments'} for x in issues],'scope_limit':'This is independent scientific membership/source comparison only. Parent compiles attributed findings into native review. No whole-owner, union, ingredient role, source-release or export approval.'})
print(counts,len(rr),len(captures))
