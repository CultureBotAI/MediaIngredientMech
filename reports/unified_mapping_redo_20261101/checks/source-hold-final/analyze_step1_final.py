from pathlib import Path
from collections import Counter
import csv,hashlib,io,json,subprocess
r=Path(__file__).resolve().parent;m=r/'step1-mim';e=r/'step1-source-holds-evidence'
base='2add44fbfe37544218d2f4daeb322b35debc5dd4'
def read_tsv(text):
 rows=list(csv.DictReader(io.StringIO(text),delimiter='\t'))
 assert len(rows)==len({x['ingredient_name'] for x in rows})
 return {x['ingredient_name']:x for x in rows}
before=read_tsv(subprocess.check_output(['git','show',base+':UNIFIED_INGREDIENT_MAPPING.tsv'],cwd=m,text=True))
after=read_tsv((m/'UNIFIED_INGREDIENT_MAPPING.tsv').read_text())
original=read_tsv((r/'step1-evidence/unified-candidate.tsv').read_text())
holds=json.loads((r/'step1-independent/proposed-source-holds.json').read_text())['rows'];names={x['ingredient_name'] for x in holds}
assert before.keys()!=after.keys()
changed={name:{key:[before[name][key],after[name][key]] for key in before[name] if before[name][key]!=after[name][key]} for name in before.keys()&after.keys() if before[name]!=after[name]}
source_delta={name:{key:[original[name][key],after[name][key]] for key in after[name] if original[name][key]!=after[name][key]} for name in original if original[name]!=after[name]}
assert set(source_delta)==names
for name in names:
 assert after[name]['mapping_status']=='UNMAPPED'
 for key in ('mim_id','chebi_id','culturemech_term_id','cas_rn','kg_microbe_node_id','synonyms'):assert after[name][key]=='',(name,key)
 for key in ('ingredient_name','occurrence_count','example_media'):assert after[name][key]==original[name][key]
sssom=(m/'mappings/ingredient_mappings.sssom.tsv').read_bytes()
assert sssom==subprocess.check_output(['git','show',base+':mappings/ingredient_mappings.sssom.tsv'],cwd=m)
rows=list(csv.DictReader((x for x in sssom.decode().splitlines() if not x.startswith('#')),delimiter='\t'))
result={'base':base,'base_rows':len(before),'final_rows':len(after),'added':len(after.keys()-before.keys()),'removed':len(before.keys()-after.keys()),'changed':len(changed),'unchanged':sum(before[n]==after[n] for n in before.keys()&after.keys()),'changed_fields':dict(Counter(k for fields in changed.values() for k in fields)),'final_statuses':dict(Counter(x['mapping_status'] for x in after.values())),'occurrences':sum(int(x['occurrence_count']) for x in after.values()),'source_hold_rows_changed':len(source_delta),'nonheld_rows_unchanged_from_initial_generation':len(original)-len(source_delta),'sssom_rows':len(rows),'sssom_unchanged':True,'sssom_sha256':hashlib.sha256(sssom).hexdigest(),'rejected_empty_identity':sum(x['mapping_status']=='REJECTED' and not x['mim_id'] for x in after.values()),'compound_chebi_leaks':sum(x['mim_id'].startswith('kgmicrobe.compound:') and any(x[k].startswith('CHEBI:') for k in ('culturemech_term_id','chebi_id','kg_microbe_node_id')) for x in after.values())}
assert result['rejected_empty_identity']==result['compound_chebi_leaks']==0
for name,obj in [('final-comparison.json',result),('unified-main-delta.json',changed),('source-hold-row-delta.json',source_delta)]:
 with (e/name).open('x') as f:json.dump(obj,f,indent=2);f.write('\n')
print(json.dumps(result,indent=2))
