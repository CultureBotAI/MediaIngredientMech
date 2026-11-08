import datetime,hashlib,json,pathlib
O=pathlib.Path('.temp/w05-tellurium-polypeptone-v1/review/membership-child');S=pathlib.Path('.temp/w05-tellurium-polypeptone-v1/polypeptone')
sha=lambda p:hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def save(n,d):
 p=O/n;assert not p.exists();p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
raw=json.loads((O/'rows-150-v1.json').read_text());entries=[]
for rc in json.loads((S/'togo-exact-retry-fetch-receipts.json').read_text()):
 p=S/'captures'/rc['path'];assert rc['exit_code']==0 and sha(p)==rc['sha256'];d=json.loads(p.read_text());matched=[]
 for ci,c in enumerate(d['components']):
  for ii,x in enumerate(c.get('items',[])):
   if 'polypept' in x.get('component_name','').casefold():matched.append({'json_pointer':f'/components/{ci}/items/{ii}','exact_object':x})
 assert len(matched)==1
 entries.append({'path':str(p),'sha256':sha(p),'capture_author':'/root/polypeptone_supplement','original_receipt':rc,'meta_exact':d['meta'],'polypepton_items':matched,'read_scope':'All component names, supplied amounts/units, GMO labels/IDs, complete preparation comments and top-level source metadata read for membership comparison; unrelated generic GMO property/role lists are not independently approved.','scientific_assessment':'Direct TOGO database evidence retains source Polypepton (Nihon Pharm. Co.) with GMO_001322 label Hipolypepton (Nihon seiyaku). This is positive source-qualified cross-label evidence for the Japanese casein-product family; it is not evidence of equivalence to BD equal-parts casein/animal-tissue blend or of exact Nihon-to-Shioya SKU continuity.'})
byM={x['meta_exact']['gm'].rsplit('/',1)[-1]:x for x in entries}
rowM={32:'M77',55:'M122',72:'M174',73:'M175',77:'M182',82:'M190',94:'M215',96:'M231',98:'M256',99:'M266',103:'M2',104:'M318',106:'M423',107:'M537',108:'M77',109:'M874',110:'M90',111:'M91'}
for r in raw['row_assessments']:
 i=r['zero_based_original_row_index']
 if i in rowM:
  e=byM[rowM[i]];r['primary_capture_refs'].append(e['path']);r['late_togo_assessment']='Exact TOGO response additionally preserves the raw Nihon Polypepton spelling and maps it to provider GMO_001322 / Hipolypepton (Nihon seiyaku). This narrows the Japanese family route; it does not establish exact formulation/SKU continuity or BD equivalence.'
  r['late_togo_read_scope']='Complete source/recipe composition and preparation fields read; relationship to this historical occurrence remains source-qualified. M77 also supplies corroborating JCM86 context for row032, without treating that current API response as its frozen bytes.'
  if i in [103,110]:
   r['precise_missing_fact']='No named-family fact is missing for retaining the Nihon source route: TOGO and MediaDive both explicitly support it. Original JCM endpoint is unavailable; only a stronger exact product/version or SKU-continuity claim would require additional originating/manufacturer evidence.'
 elif r['raw_label_partition']=='bd_bbl_raw_label':
  r['precise_missing_fact']='No missing named BD/BBL-family fact is identified from this raw-label comparison. '+('Supplied catalogue211910 matches the dated manufacturer catalogue. ' if '211910' in r['raw_preferred_term'] else 'A catalogue number is needed only if a particular SKU/version is claimed. ')+'No historical lot claim is made or required merely to retain the named product family. Whole-owner application remains separate because the owner still includes generic/source-qualified scope.'
 r['named_partial_preparation_rule']='A source-supported named preparation can be curated without determining every peptide species or lot. Unresolved stronger cross-product/version equivalence is distinct from the known named family and from coordinator release approval.'
raw['successor_of']={'path':str(O/'rows-150-v1.json'),'sha256':sha(O/'rows-150-v1.json')}
raw['successor_reason']='Append newly available successful TOGO primary responses; clarify that missing SKU/lot details are prerequisites only to stronger identity claims, not an invented barrier to a known named partial preparation.'
save('togo-late-primary-review-v1.json',{'reviewer':'/root/final_skeptical/preservation_audit','read_completed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'successful_capture_count':len(entries),'successful_captures':entries,'failed_initial_attempts':{'path':str(S/'togo-exact-fetch-receipts.json'),'sha256':sha(S/'togo-exact-fetch-receipts.json'),'assessment':'Initial DNS failures preserved. Successful retry bytes are separately named; initial failures are not negative scientific evidence.'}})
save('rows-150-v2.json',raw)
print(len(entries),'late captures read; all150 successor assessments retained')
