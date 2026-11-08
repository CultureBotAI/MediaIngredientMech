import pathlib,json,gzip,hashlib,datetime
O=pathlib.Path('.temp/w05-tellurium-polypeptone-v1/review/membership-child');S=pathlib.Path('.temp/w05-tellurium-polypeptone-v1/polypeptone');d=json.loads((S/'input/polypeptone-context-subset.json').read_text());p=pathlib.Path(d['original_capture']);sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();assert sha(p)==d['sha256'];full=json.loads(gzip.decompress(p.read_bytes()));own=next(x for x in full['owners'] if x['path']==d['owner']['path']);assert own==d['owner'];assert own['exact_resolving_label_occurrences']==d['owner']['exact_resolving_label_occurrences'];recs=[]
for key,r in d['complete_japanese_recipes'].items():
 assert full['current_complete_recipes'][key]==r
 recs.append({'source_path':key,'snapshot_path':r['source_path'],'snapshot_sha256':r['sha256'],'object_sha256':hashlib.sha256(json.dumps(r['complete_recipe'],sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()})
(O/'input-authentication-v1.json').write_text(json.dumps({'reviewer':'/root/final_skeptical/preservation_audit','started_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'original_capture':str(p),'original_sha256':sha(p),'original_capture_inspected_at':full['inspected_at'],'context_matching_method':full['matching_method'],'original_occurrence_table_path':full['occurrence_table_path'],'original_occurrence_table_sha256':full['occurrence_table_sha256'],'subset_path':str(S/'input/polypeptone-context-subset.json'),'subset_sha256':sha(S/'input/polypeptone-context-subset.json'),'owner_and_all150rows_exact_subset':True,'complete23recipes_exact_subset':True,'recipes':recs},indent=2)+'\n')
(O/'read/original150-context-rows.json').write_text(json.dumps(own['exact_resolving_label_occurrences'],indent=2,ensure_ascii=False)+'\n')
def semantic(x):
 if isinstance(x,dict):return {k:semantic(v) for k,v in x.items() if k not in ['evidence','curation_history']}
 if isinstance(x,list):return [semantic(v) for v in x]
 return x
for i,(key,r) in enumerate(d['complete_japanese_recipes'].items()):
 (O/'read'/f'recipe-{i:02d}.json').write_text(json.dumps({'source_path':key,'snapshot_sha256':r['sha256'],'complete_scientific_recipe_fields':semantic(r['complete_recipe'])},indent=2,ensure_ascii=False)+'\n')
print('Authenticated150owner rows and23complete recipe objects against originalgzip. Semantic read derivatives exclude evidence/curation metadata only; original bytes retained.')
