from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess,collections,yaml,csv,io
OUT=Path(__file__).resolve().parent;RUN=OUT.parents[1];MIM=RUN/'step3-mim';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
receipt_path=RUN/'step3-application/source-apply.json';receipt=json.loads(receipt_path.read_bytes());assert receipt['state']=='complete' and receipt['applied'] is True and receipt['approval'].startswith('NONE:')
assert len(receipt['records'])==3 and len(receipt['output_sha256'])==5
assert all(sha(MIM/p)==h for p,h in receipt['output_sha256'].items())
backups={}
for p,h in receipt['input_sha256'].items():
 path=Path(p)
 if path.is_relative_to(MIM/'data/ingredients') or path.is_relative_to(MIM/'mappings'):
  backup=RUN/'step3-application'/('source-apply.before-'+path.name);assert sha(backup)==h;backups[str(backup)]=h
 else:assert sha(path)==h
assert len(backups)==7
tracked={}
for entry in subprocess.check_output(['git','ls-tree','-rz','HEAD','data/ingredients'],cwd=MIM).decode().rstrip('\0').split('\0'):
 meta,name=entry.split('\t');_,kind,blob=meta.split();
 if kind=='blob' and name.endswith('.yaml'):tracked[name]=blob
changed=[]
for name,blob in tracked.items():
 b=(MIM/name).read_bytes();current=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
 if current!=blob:changed.append(name)
assert set(changed)=={r['source_record'] for r in receipt['records']}
assert len(tracked)==2955
normalize=lambda x:json.dumps(x,sort_keys=True,default=str)
Loader=yaml.CSafeLoader
surfaces={}
inherited_divergences=[]
for category in ['mapped','unmapped']:
 individual=[yaml.load(p.read_text(),Loader=Loader) for p in (MIM/f'data/ingredients/{category}').glob('*.yaml')]
 agg=yaml.load((MIM/f'data/curated/{category}_ingredients.yaml').read_text(),Loader=Loader)
 oldagg=yaml.load(subprocess.check_output(['git','show',f'HEAD:data/curated/{category}_ingredients.yaml'],cwd=MIM),Loader=Loader)['ingredients']
 keyed=lambda rows:{r['preferred_term']:r for r in rows}
 current_index,old_index=keyed(agg['ingredients']),keyed(oldagg)
 assert len(current_index)==len(agg['ingredients']) and len(old_index)==len(oldagg)
 target_names={'Carnitine Hydrochloride','Carnitine (Dl) Hydrochloride','NLDM_metabolites'}
 changed_names=[name for name in current_index if current_index[name]!=old_index[name]]
 assert set(changed_names)==(target_names if category=='mapped' else set())
 for record in individual:
  projected=current_index[record['preferred_term']]
  if record!=projected:
   assert record['preferred_term'] not in target_names
   assert projected==old_index[record['preferred_term']]
   paths=[p for p in (MIM/f'data/ingredients/{category}').glob('*.yaml') if yaml.load(p.read_text(),Loader=Loader)['preferred_term']==record['preferred_term']]
   assert len(paths)==1
   assert paths[0].read_bytes()==subprocess.check_output(['git','show','HEAD:'+str(paths[0].relative_to(MIM))],cwd=MIM)
   keys=[k for k in set(record)|set(projected) if record.get(k)!=projected.get(k)]
   assert keys==['discussions']
   inherited_divergences.append({'path':str(paths[0].relative_to(MIM)),'fields':keys,'individual_and_aggregate_unchanged_from_base':True})
 surfaces[category]={'count':len(individual),'aggregate_sha256':sha(MIM/f'data/curated/{category}_ingredients.yaml'),'changed_record_names':changed_names,'target_records_equal_individual':True}
 assert len(individual)==len(agg['ingredients'])
for r in receipt['records']:
 before=yaml.load((RUN/'step3-application'/('source-apply.before-'+Path(r['source_record']).name)).read_text(),Loader=Loader)
 after=yaml.load((MIM/r['source_record']).read_text(),Loader=Loader)
 assert after['curation_history'][:-1]==before['curation_history']
 assert after['curation_history'][-1]['timestamp']==receipt['timestamp']
 assert after['occurrence_statistics']==before['occurrence_statistics']
 assert sha(MIM/r['source_record'])==r['after_yaml_sha256']
oldmembership=RUN/'step3-application/source-apply.before-culturemech_recipe_membership.tsv'
read=lambda p:list(csv.DictReader((line for line in p.read_text().splitlines() if not line.startswith('#')),delimiter='\t'))
old=read(oldmembership);new=read(MIM/'mappings/culturemech_recipe_membership.tsv');oldid='kgmicrobe.compound:carnitine_hydrochloride';newid='NCIT:C216679'
pairs_old=[(r['recipe_id'],r['occurrences']) for r in old if r['mim_identifier']==oldid];pairs_new=[(r['recipe_id'],r['occurrences']) for r in new if r['mim_identifier']==newid]
assert pairs_old==pairs_new and len(pairs_old)==14
assert [r for r in old if r['mim_identifier']!=oldid]==[r for r in new if r['mim_identifier']!=newid]
assert not any(r['mim_identifier']==oldid for r in new)
assert sha(MIM/'mappings/ingredient_mappings.sssom.tsv')==receipt['sssom_before_sha256']
assert sha(MIM/'mappings/other_cross_record_baseline.tsv')==receipt['baseline_before_sha256']
candidate=MIM/'output/step3-native-candidate';generation=json.loads((candidate/'generation-receipt.json').read_bytes());assert generation['candidate_sha256']==sha(candidate/'candidate.sssom.tsv')
assert generation['input_manifest_sha256']==sha(candidate/'inputs-before.json')
assert json.loads((candidate/'inputs-before.json').read_bytes())==json.loads((candidate/'inputs-after.json').read_bytes())
assert all(sha(candidate/name)==h for name,h in generation['label_maps'].items())
assert generation['producer_revision']=='6a7172585eb68da7f4fe01aee75a82458ddd470c'
assert generation['producer_sha256']==sha(RUN/'claw-cas-guard/scripts/build_mim_ingredient_sssom.py')
rows=read(candidate/'candidate.sssom.tsv');selected=[r for r in rows if r['subject_id'] in {'MIM:Carnitine_Hydrochloride','MIM:Carnitine_Dl_Hydrochloride','MIM:NLDM_metabolites'}];assert len(selected)==2
result={'checked_at':datetime.now(timezone.utc).isoformat(),'verdict':'PASS_ACTUAL_SOURCE_APPLICATION; PROMOTION_BLOCKED_BY_1038_PENDING_REPAIR','source_receipt_sha256':sha(receipt_path),'source_timestamp':receipt['timestamp'],'changed_owners':changed,'unchanged_owners':len(tracked)-len(changed),'source_outputs':receipt['output_sha256'],'backups':backups,'aggregate_surfaces':surfaces,'inherited_unrelated_surface_divergences':inherited_divergences,'preserved_14_recipe_occurrence_pairs':pairs_new,'canonical_and_baseline_unchanged':True,'full_native_candidate_sha256':sha(candidate/'candidate.sssom.tsv'),'full_native_candidate_rows':len(rows),'selected_rows':selected,'generation_receipt_sha256':sha(candidate/'generation-receipt.json'),'label_maps_verified':generation['label_maps'],'scientific_or_release_approval':False,'production_edits':False}
(OUT/'receipt.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
