from pathlib import Path
from collections import Counter
import csv,hashlib,json,re,shutil,subprocess,sys
import yaml
OUT=Path(__file__).resolve().parent;RUN=OUT.parent;MIM=RUN/'mim';CM=RUN.parent.parent.parent/'CultureMech'
sys.path.insert(0,str(MIM/'src'))
from mediaingredientmech.utils.culturemech_occurrences import mim_identifier_for_occurrence
TARGET='kgmicrobe.compound:na2hpo4_x_7_h2o';label='Na2HPO4 x 7 H2O';rel='data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for block in iter(lambda:f.read(1048576),b''):h.update(block)
 return h.hexdigest()
record=yaml.safe_load((MIM/rel).read_text())
aggregate=yaml.safe_load((MIM/'data/curated/mapped_ingredients.yaml').read_text())
if isinstance(aggregate,dict):aggregate=aggregate['ingredients']
matched=[r for r in aggregate if r['preferred_term']==label]
manifest=[]
for p in [MIM/rel,MIM/'MAPPING_SEMANTICS.md',MIM/'src/mediaingredientmech/schema/mediaingredientmech.yaml',MIM/'mappings/unified_mapping_rejections.tsv',MIM/'mappings/ingredient_mappings.sssom.tsv',MIM/'data/curated/mapped_ingredients.yaml',CM/'output/ingredient_occurrences.tsv',CM/'output/ingredients_list.tsv',RUN/'claw/scripts/build_unified_ingredient_mapping.py']:
 manifest.append({'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size})
(OUT/'input-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
(OUT/'target-input.yaml').write_bytes((MIM/rel).read_bytes())
with (CM/'output/ingredient_occurrences.tsv').open(newline='') as f:
 reader=csv.DictReader(f,delimiter='\t');fields=reader.fieldnames
 occurrences=[r for r in reader if r['resolved_identifier']==TARGET or r['mim_preferred_term']==label or re.fullmatch(r'na2hpo4\s*(?:x|[.·•])?\s*7\s*h2o',r['preferred_term'],re.I)]
with (OUT/'current-culturemech-occurrences.tsv').open('w',newline='') as f:
 writer=csv.DictWriter(f,fields,delimiter='\t');writer.writeheader();writer.writerows(occurrences)
identity_matches=[];label_matches=[]
for p in sorted((MIM/'data/ingredients').rglob('*.yaml')):
 d=yaml.safe_load(p.read_text());cp=d.get('chemical_properties') or {};ont=d.get('ontology_mapping') or {}
 if d.get('identifier') in {TARGET,'cas:7782-85-6','NCIT:C61946'} or cp.get('cas_rn')=='7782-85-6' or ont.get('ontology_id')=='NCIT:C61946':
  identity_matches.append({'path':str(p.relative_to(MIM)),'identifier':d.get('identifier'),'mapping_status':d.get('mapping_status'),'preferred_term':d.get('preferred_term'),'cas_rn':cp.get('cas_rn'),'ontology_id':ont.get('ontology_id')})
 names=[(d.get('preferred_term',''),'preferred_term')]+[(s.get('synonym_text',''),s.get('synonym_type','')) for s in d.get('synonyms',[])]
 hits=[{'text':n,'type':t} for n,t in names if re.fullmatch(r'na2hpo4\s*(?:x|[.·•])?\s*7\s*h2o',n,re.I) or 'phosphate heptahydrate' in n.casefold()]
 if hits:label_matches.append({'path':str(p.relative_to(MIM)),'identifier':d.get('identifier'),'mapping_status':d.get('mapping_status'),'hits':hits})
with (MIM/'mappings/unified_mapping_rejections.tsv').open() as f:rejections=[r for r in csv.DictReader(f,delimiter='\t') if TARGET in r.values()]
with (MIM/'mappings/ingredient_mappings.sssom.tsv').open() as f:sssom=[r for r in csv.DictReader((l for l in f if not l.startswith('#')),delimiter='\t') if r['subject_id']=='MIM:Na2hpo4_X_7_H2o']
summary={'record_matches_aggregate':len(matched)==1 and matched[0]==record,
 'current_culturemech_rows':len(occurrences),'distinct_recipes':len({r['recipe_id'] for r in occurrences}),
 'occurrence_labels':dict(Counter(r['preferred_term'] for r in occurrences)),
 'occurrence_raw_identifiers':dict(Counter(r['resolved_identifier'] for r in occurrences)),
 'occurrence_native_effective_identifiers':dict(Counter(mim_identifier_for_occurrence(r) for r in occurrences)),
 'identity_matches':identity_matches,'label_matches':label_matches,'rejections':rejections,'sssom_rows':sssom,
 'duplicate_search_scope':'All data/ingredients/**/*.yaml via pathlib.rglob including ignored files; independent rg --no-ignore --hidden CAS/NCIT/name scan also performed. Stock solution and REJECTED_LABEL hits are distinguished, not merged.',
 'revisions':{k:subprocess.check_output(['git','-C',str(p),'rev-parse','HEAD'],text=True).strip() for k,p in [('mim',MIM),('culturemech',CM)]}}
(OUT/'record-and-occurrence-audit.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k not in ['label_matches','sssom_rows','rejections']},indent=2))
