"""Bind the exact source-case scope and actual owner/proposal inputs for native review."""
import hashlib,json,subprocess,sys
from pathlib import Path
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'MAPPING_SEMANTICS.md').is_file())
OUT=ROOT/'reports/all_unmatched_20261107/worker-09'
rel=lambda p:str(p.relative_to(ROOT))
groups=('antibiotics','salts','materials')
decisions=[d for g in groups for d in json.loads((OUT/g/'decisions.json').read_text())['decisions']]
cases=json.loads((OUT/'common/frozen-shard-09.json').read_text())['cases']; byid={d['case_id']:d for d in decisions}
targets=[];inputs={'MAPPING_SEMANTICS.md','src/mediaingredientmech/schema/mediaingredientmech.yaml','mappings/ingredient_mappings.sssom.tsv','conf/record_review.yaml'}
for i,c in enumerate(cases):
 d=byid[c['case_id']]
 t={'target_id':c['case_id'],'path':rel(OUT/'common/frozen-shard-09.json'),'selector':f'cases[{i}] case_id={c["case_id"]}','label':c['source']+': '+c['source_label'],'kind':'snapshot_row','semantic_digest':{'algorithm':'SHA256','sha256':d['case_input_sha256'],'description':'Canonical sorted compact JSON of the complete unchanged frozen case, UTF-8 ensure_ascii=false allow_nan=false; no newline.'}}
 if d['owner_records']:
  t['owner_paths']=[{'repository':'CultureBotAI/MediaIngredientMech','path':o['path'],'role':'Referenced baseline owner context; not an assertion that every source case exactly denotes this owner'} for o in d['owner_records']]
  inputs.update(o['path'] for o in d['owner_records'])
 else:t['ownership_note']='Source-only case; no current MIM owner is invented. Any proposed new owner is an isolated candidate in proposals.json.'
 targets.append(t)
for g in groups:
 for n in ('decisions.json','evidence.json','proposals.json'):inputs.add(rel(OUT/g/n))
 for p in json.loads((OUT/g/'proposals.json').read_text())['proposals']:inputs.add(rel(OUT/p['after_capture']['path']))
 for e in json.loads((OUT/g/'evidence.json').read_text())['evidence']:
  if e['capture']['root']=='artifact':inputs.add(rel(OUT/e['capture']['path']))
for item in json.loads((OUT/'common/frozen-recipe-copies.json').read_text())['files']:inputs.add(rel(OUT/item['capture_path']))
for path in sys.argv[2:]:inputs.add(path)
targetfile=OUT/'common/native-targets-full.json';targetfile.write_text(json.dumps({'targets':targets},indent=2)+'\n')
cmd=[sys.executable,str(ROOT/'scripts/record_review.py'),'inspect','--targets',str(targetfile)]
for p in sorted(inputs):cmd.extend(['--input',p])
proc=subprocess.run(cmd,cwd=ROOT,capture_output=True,text=True)
(OUT/'validation'/sys.argv[1]).write_text(proc.stdout)
(OUT/'validation'/(sys.argv[1]+'.command.json')).write_text(json.dumps({'command':cmd,'exit_code':proc.returncode,'stderr':proc.stderr},indent=2)+'\n')
print(json.dumps({'returncode':proc.returncode,'source_cases':len(targets),'context_inputs':len(inputs),'stderr':proc.stderr}));sys.exit(proc.returncode)
