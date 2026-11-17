from pathlib import Path
import csv,collections,hashlib,json,shutil
D=Path(__file__).resolve().parent
KG=Path('/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe-mim-1788-20261107')
rules=json.loads((D/'queues/microbedecoder-current-material-holds.json').read_text())
by_ordinal=collections.defaultdict(list)
for r in rules:by_ordinal[int(r['source_record'].rsplit('=',1)[1])].append(r)
raw=KG/'data/raw/database.csv';rawhash=hashlib.sha256();selected={};before=raw.stat()
with raw.open('rb') as f:
 def lines():
  for line in f:rawhash.update(line);yield line.decode('utf-8',errors='surrogateescape')
 for ordinal,row in enumerate(csv.DictReader(lines()),1):
  if ordinal in by_ordinal:
   digest=hashlib.sha256(json.dumps(row,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode('utf-8',errors='surrogateescape')).hexdigest()
   assert all(digest==r['raw_record_sha256'] for r in by_ordinal[ordinal]);selected[str(ordinal)]={'source_record':by_ordinal[ordinal][0]['source_record'],'raw_record_sha256':digest,'raw_row':row,'bound_dispositions':by_ordinal[ordinal]}
assert set(map(int,selected))==set(by_ordinal)
assert rawhash.hexdigest()=='0c6ff730a108720a5d6972400f2bccf2eca8621713b62736abdf5df0fb188c95'
assert (raw.stat().st_size,raw.stat().st_mtime_ns)==(before.st_size,before.st_mtime_ns)
(D/'queues/microbedecoder-source-records.json').write_text(json.dumps(selected,indent=2,ensure_ascii=True)+'\n')
expected={tuple(r[k] for k in ['source_record','source_column','source_literal']):r for r in rules};assert len(expected)==len(rules)
ids={r['object_curie'] for r in rules};actual=[];edgehash=hashlib.sha256();p=KG/'data/transformed/microbedecoder/edges.tsv'
with p.open('rb') as f:
 def lines():
  for line in f:edgehash.update(line);yield line.decode('utf-8')
 for row in csv.DictReader(lines(),delimiter='\t'):
  if row['object'] not in ids:continue
  key=tuple(row[k] for k in ['source_record','source_column','value']);rule=expected[key]
  fieldmap={'subject':'subject','object':'object_curie','source_citation':'source_citation','predicate':'predicate','relation':'relation','primary_knowledge_source':'primary_knowledge_source','knowledge_level':'knowledge_level','agent_type':'agent_type','value_encoding':'value_encoding'}
  assert all(row[a]==rule[b] for a,b in fieldmap.items());actual.append(row)
marker=json.loads((D/'snapshots/data/transformed/microbedecoder/source_finalization.json').read_text());assert edgehash.hexdigest()==marker['members']['edges.tsv']['sha256'];assert len(actual)==len(expected)==225
with (D/'queues/microbedecoder-current-edges.tsv').open('x',newline='') as f:w=csv.DictWriter(f,fieldnames=list(actual[0]),delimiter='\t');w.writeheader();w.writerows(actual)
for rel in ['kg_microbe/transform_utils/microbedecoder/material_dispositions.py','kg_microbe/transform_utils/microbedecoder/chemical_curation.py']:
 p=KG/rel;out=D/'snapshots'/rel;out.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,out)
proof={'raw_path':str(raw),'raw_sha256':rawhash.hexdigest(),'raw_selected_records':len(selected),'material_disposition_rows':len(rules),'candidate_source_ids':len(ids),'graph_rows_matched':len(actual),'graph_sha256':edgehash.hexdigest(),'native_finalization_graph_hash_matches':True,'each_exact_material_source_key_and_predicate_preserved':True,'all_identity_statuses':dict(collections.Counter(r['identity_status'] for r in rules)),'all_identity_approved':dict(collections.Counter(r['identity_approved'] for r in rules)),'scientific_approval_added':False,'record_hash_algorithm_source':'kg_microbe/transform_utils/microbedecoder/chemical_curation.py:canonical_raw_row_sha256'}
(D/'microbedecoder-observation-proof.json').write_text(json.dumps(proof,indent=2)+'\n');print(json.dumps(proof))
