"""Independently verify the bounded applied data and every candidate input hash."""
from pathlib import Path
from collections import Counter
import csv,hashlib,io,json,subprocess,sys,yaml
ROOT=Path(sys.argv[1]).resolve();RUN=ROOT.parent;OUT=Path(__file__).resolve().parent
BASE='40b787d37d33d544551389ff019f2d64ad63d7cc'
OWNER='data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml';LEDGER='mappings/unified_mapping_rejections.tsv';SSSOM='mappings/ingredient_mappings.sssom.tsv'
SUBJECT='MIM:Na2hpo4_X_7_H2o';NAME='Na2HPO4 x 7 H2O';NEW='NCIT:C61946';OLD='kgmicrobe.compound:na2hpo4_x_7_h2o'
def shab(b):return hashlib.sha256(b).hexdigest()
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  while data:=f.read(8*1024*1024):h.update(data)
 return h.hexdigest()
def base(p):return subprocess.check_output(['git','show',BASE+':'+p],cwd=ROOT)
def table(b):return list(csv.DictReader((s for s in b.decode().splitlines() if not s.startswith('#')),delimiter='\t'))
checks={}
old=yaml.safe_load(base(OWNER));new=yaml.safe_load((ROOT/OWNER).read_bytes())
assert new['identifier']==new['ontology_mapping']['ontology_id']==NEW
assert {k:v for k,v in old.items() if k not in {'identifier','ontology_mapping','curation_history'}}=={k:v for k,v in new.items() if k not in {'identifier','ontology_mapping','curation_history'}}
assert new['curation_history'][:-1]==old['curation_history']
assert new['ontology_mapping']['evidence'][:-1]==old['ontology_mapping']['evidence']
assert set(new['ontology_mapping'])==set(old['ontology_mapping'])
assert len(new['ontology_mapping']['evidence'])==len(old['ontology_mapping']['evidence'])+1
checks['owner_scope']={'unrelated_fields_identical':True,'history_prefix_identical':True,'new_history_events':1,'old_mapping_evidence_preserved':True,'owner_sha256':sha(ROOT/OWNER)}
for name in ['mapped','unmapped']:
 path=f'data/curated/{name}_ingredients.yaml';a=yaml.safe_load(base(path));b=yaml.safe_load((ROOT/path).read_bytes())
 listkeys=[k for k,v in a.items() if isinstance(v,list)]
 assert len(listkeys)==1,listkeys
 key=listkeys[0]
 olditems=[i for i in a[key] if i.get('preferred_term')!=NAME];newitems=[i for i in b[key] if i.get('preferred_term')!=NAME]
 dump=lambda x:json.dumps(x,sort_keys=True,default=str,separators=(',',':'))
 assert Counter(map(dump,olditems))==Counter(map(dump,newitems))
 target=[i for i in b[key] if i.get('preferred_term')==NAME]
 assert target==([new] if name=='mapped' else [])
 changes=[k for k in a if k!=key and a[k]!=b[k]]
 assert changes==['generation_date'],changes
 checks['aggregate_'+name]={'non_target_records_identical':True,'metadata_changed':changes,'records':len(b[key])}
oldledger=table(base(LEDGER));newledger=table((ROOT/LEDGER).read_bytes());assert len(oldledger)==len(newledger)
ld=[(i,a,b) for i,(a,b) in enumerate(zip(oldledger,newledger),1) if a!=b]
assert len(ld)==1
_,a,b=ld[0];assert a['ingredient_name']==b['ingredient_name']==NAME and a['rejected_id']==b['rejected_id']=='CHEBI:34683' and a['mim_id']==OLD and b['mim_id']==NEW
assert set(k for k in a if a[k]!=b[k])=={'mim_id','reason'}
checks['ledger']={'rows':len(newledger),'changed_rows':1,'rejected_id_preserved':'CHEBI:34683','new_owner':NEW,'sha256':sha(ROOT/LEDGER)}
oldss=base(SSSOM);newss=(ROOT/SSSOM).read_bytes();orows=table(oldss);nrows=table(newss)
oldtarget=[r for r in orows if r['subject_id']==SUBJECT];target=[r for r in nrows if r['subject_id']==SUBJECT]
assert len(oldtarget)==2 and len(target)==1
strip=lambda b:[l for l in b.splitlines(keepends=True) if not l.startswith((SUBJECT+'\t').encode())]
assert strip(oldss)==strip(newss)
row=target[0];assert row['object_id']==NEW and row['predicate_id']=='skos:exactMatch' and row['validation_method']==''
assert row['other']=='Na2HPO4.7H2O|Na2HPO4•7H2O|CAS:7782-85-6'
oldtokens=set(oldtarget[0]['source'].split('|'));newtokens=set(row['source'].split('|'))
assert oldtokens<=newtokens
checks['canonical_sssom']={'before_rows':len(orows),'after_rows':len(nrows),'other_bytes_identical':True,'historical_sources_preserved':True,'target':row,'sha256':sha(ROOT/SSSOM)}
primary=ROOT/'reports/ncit_heptahydrate_875_20261101/sources/ncit-C61946.json';fetch=json.loads(primary.with_name('ncit-C61946-receipt.json').read_bytes());term=json.loads(primary.read_bytes())
assert sha(primary)==fetch['sha256']=='a112c3e91dd6aa46feb112621ba5d13673df69f1b20665e042e22b8aa05a1d83'
props={p['type']:p['value'] for p in term['properties']}
assert term['code']=='C61946' and term['active'] is True and term['name']==row['object_label']
assert props['CAS_Registry']==new['chemical_properties']['cas_rn']=='7782-85-6'
assert props['Chemical_Formula']=='2Na.HO4P.7H2O' and props['FDA_UNII_Code']=='70WT22SF4B'
checks['primary_evidence']={'sha256':sha(primary),'official_url':fetch['url'],'version':term['version'],'matches_exact_form':True,'live_web_recheck':'web tool unavailable; archived official response and fetch receipt inspected'}
cdir=ROOT/'output/step2-native-candidate';receipt=json.loads((cdir/'generation-receipt.json').read_bytes());manifest=json.loads((cdir/'inputs-before.json').read_bytes());after=json.loads((cdir/'inputs-after.json').read_bytes())
assert manifest==after and sha(cdir/'inputs-before.json')==receipt['input_manifest_sha256']
assert sha(cdir/'candidate.sssom.tsv')==receipt['candidate_sha256']
assert sha(RUN/'generate_candidate.py')==receipt['harness_sha256']
assert sha(RUN/'claw-source/scripts/build_mim_ingredient_sssom.py')==receipt['producer_sha256']
checked=[]
for path,meta in manifest.items():
 assert Path(path).stat().st_size==meta['bytes'] and sha(path)==meta['sha256'],path
 checked.append(path)
for path,h in receipt['label_maps'].items():assert sha(cdir/path)==h
comparisons=json.loads((cdir/'comparison-inputs.json').read_bytes())
for path,meta in comparisons.items():assert sha(path)==meta['sha256'] and Path(path).stat().st_size==meta['bytes']
crows=table((cdir/'candidate.sssom.tsv').read_bytes());candidates=[r for r in crows if r['subject_id']==SUBJECT]
assert len(candidates)==1
assert {k:v for k,v in candidates[0].items() if k!='source'}=={k:v for k,v in row.items() if k!='source'}
assert set(candidates[0]['source'].split('|'))|oldtokens==newtokens
checks['candidate']={'rows':len(crows),'all_generation_inputs_verified':len(checked),'input_bytes_verified':sum(v['bytes'] for v in manifest.values()),'comparison_inputs_verified':len(comparisons),'label_maps_verified':len(receipt['label_maps']),'target_equals_promoted_row_except_preserved_source_lineage':True,'sha256':receipt['candidate_sha256'],'input_paths':checked}
application=RUN/'step2-application';source=json.loads((application/'source-apply.json').read_bytes());promotion=json.loads((application/'mapping-promotion.json').read_bytes());publication=json.loads((application/'receipt-publication.json').read_bytes())
assert source['state']==promotion['state']=='complete' and source['applied'] is promotion['applied'] is True
assert source['records'][0]['before_yaml_sha256']==shab(base(OWNER))==sha(application/'source-apply.before.yaml')
assert source['records'][0]['after_yaml_sha256']==sha(ROOT/OWNER)
assert source['ledger_before_sha256']==shab(base(LEDGER))==sha(application/'source-apply.before-ledger.tsv')
assert source['ledger_after_sha256']==sha(ROOT/LEDGER)
assert source['sssom_before_sha256']==shab(oldss)==sha(application/'source-apply.before.sssom.tsv')
assert promotion['source_receipt_sha256']==sha(application/'source-apply.json')
assert promotion['candidate_sha256']==receipt['candidate_sha256'] and promotion['sssom_after_sha256']==sha(ROOT/SSSOM)
assert promotion['sssom_before_sha256']==sha(application/'mapping-promotion.before.tsv')
for phase in [source,promotion]:
 journal=json.loads(Path(phase['transaction']['journal']).read_bytes());assert journal['status']=='complete'
 for p,prior in journal['previous'].items():assert shab(prior.encode())==shab(base(str(Path(p).relative_to(ROOT))))
path=ROOT/'reports/sssom_completion_20260921/mapping_changes/issue875-ncit-exact-heptahydrate.json';native=json.loads(path.read_bytes())
assert sha(path)==publication['receipt_sha256'] and native['sequence']==16
assert native['before_sha256']==shab(oldss) and native['after_sha256']==shab(newss)
assert native['changed_rows']==native['removed_rows']==1 and native['added_rows']==0
assert native['records']==source['records']
for p,h in publication['previous_receipts_unchanged'].items():assert sha(p)==h==shab(base(str(Path(p).relative_to(ROOT))))
checks['receipts']={'source_apply_bound':True,'promotion_bound':True,'native_receipt_bound':True,'previous_receipts_unchanged':len(publication['previous_receipts_unchanged']),'journals_complete_and_before_images_verified':True,'receipt_sha256':sha(path)}
# Ensure the active row has no inherited positive mapping approval.
mreview=json.loads((ROOT/'reports/sssom_completion_20260921/review.json').read_bytes());ds=[d for d in mreview['decisions'] if d['owner_record']==OWNER]
assert len(ds)==1 and ds[0]['disposition']=='WITHHOLD'
checks['mapping_release']={'target_disposition':ds[0]['disposition'],'review_reason':ds[0]['review_reason']}
report={'baseline':BASE,'checks':checks,'source_hashes':{p:sha(ROOT/p) for p in [OWNER,LEDGER,SSSOM,'scripts/promote_heptahydrate_ncit.py','src/mediaingredientmech/ingredient_bundle_refresh.py']},'repository_mutations':False}
(OUT/'applied-verification.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:{a:b for a,b in v.items() if a not in {'target','input_paths','review_reason'}} for k,v in checks.items()},indent=2))
