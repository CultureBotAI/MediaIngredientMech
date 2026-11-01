"""Offline actual merged-producer replay of #1004 pure source proposal."""
from pathlib import Path
import copy,csv,gzip,hashlib,importlib.util,io,json,subprocess,sys
import yaml
ROOT=Path.cwd(); RUN=ROOT.parent; OUT=ROOT/'output/issue1004-dependency-tests/unified-replay'
OUT.mkdir(exist_ok=False)
CLAW=RUN/'claw-cas-guard'
commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=CLAW,text=True).strip()
assert commit.startswith('6a717258'),commit

def sha(content):return hashlib.sha256(content).hexdigest()
def load(name,path):
 spec=importlib.util.spec_from_file_location(name,path);module=importlib.util.module_from_spec(spec);sys.modules[name]=module;spec.loader.exec_module(module);return module
writer=load('issue1004_writer_probe',ROOT/'scripts/merge_carnitine_hydrochloride.py')
builder=load('issue1004_unified_probe',CLAW/'scripts/build_unified_ingredient_mapping.py')
lists=load('issue1004_lists_probe',ROOT/'scripts/export_lists.py')
gate=load('issue1004_gate_probe',ROOT/'scripts/check_unified_rejections.py')
before={p:writer.frozen_bytes(p) for p in writer.OWNERS}
after=writer.propose_sources(before,writer.frozen_bytes(writer.LEDGER),writer.frozen_bytes(writer.MEMBERSHIP),timestamp='2026-11-01T12:00:00+00:00')
fixture=json.loads(gzip.decompress((ROOT/'tests/fixtures/issue1004-routing-dependencies.json.gz').read_bytes()))
prior=RUN/'step3-preflight-new/unified-rejection-supplement-20261101T065627Z'
source=prior/'actual-source-slice-native-occurrences.json'
actual=json.loads(source.read_text())
assert actual['Carnitine Hydrochloride']['term_id']=='CHEBI:91318'
assert actual['DL-carnitine']['term_id']=='CHEBI:17126'
assert {k:v['count'] for k,v in actual.items()}=={'Carnitine Hydrochloride':14,'DL-carnitine':2}
ledger_rows=list(csv.DictReader(io.StringIO(after[writer.LEDGER].decode()),delimiter='\t'))
selected=[r for r in ledger_rows if r['mim_id']==writer.NEW]
assert {r['rejected_id'] for r in selected}=={'CHEBI:91318','CHEBI:48601'}
records={p:yaml.safe_load(after[p]) for p in writer.OWNERS if p!=writer.COMPONENT_OWNER}
records.update({Path(p):r for p,r in fixture['distinct_controls'].items()})
records[Path('data/ingredients/mapped/Synthetic_Amide_Control.yaml')]={
 'identifier':'CHEBI:48601','preferred_term':'carnitinamide chloride','mapping_status':'MAPPED',
 'ontology_mapping':{'ontology_id':'CHEBI:48601','ontology_label':'carnitinamide chloride','mapping_quality':'EXACT_MATCH'}}
names=['Carnitine Hydrochloride','Carnitine (Dl) Hydrochloride']
injected={name:{'term_id':'CHEBI:48601','count':1,'example_media':['SYNTHETIC_REENTRY_REGRESSION']} for name in names}
for r in fixture['distinct_controls'].values():
 injected[r['preferred_term']]={'term_id':r['identifier'],'count':1,'example_media':['SYNTHETIC_SIBLING_CONTROL']}
injected['carnitinamide chloride']={'term_id':'CHEBI:48601','count':1,'example_media':['SYNTHETIC_LEGITIMATE_AMIDE_CONTROL']}
results={}
for variant in ['complete_ledger','missing_amide_guard','wrong_owned_kg_node']:
 target=OUT/variant
 changed=copy.deepcopy(records)
 if variant=='wrong_owned_kg_node':changed[writer.SURVIVOR]['kg_microbe_node_id']='CHEBI:48601'
 for path,r in changed.items():
  output=target/path;output.parent.mkdir(parents=True,exist_ok=True);output.write_text(yaml.safe_dump(r,sort_keys=False))
 (target/'docs/data').mkdir(parents=True)
 lists.export_label_index(list(changed.values()),target/'docs/data/label_index.csv')
 rows=[r for r in selected if variant!='missing_amide_guard' or r['rejected_id']!='CHEBI:48601']
 ledger=target/writer.LEDGER;ledger.parent.mkdir(parents=True)
 with ledger.open('w') as stream:
  table=csv.DictWriter(stream,fieldnames=list(selected[0]),delimiter='\t',lineterminator='\n');table.writeheader();table.writerows(rows)
 indexes=builder.load_mim_index(target);labels=builder.load_mim_label_index(target)
 try:rejections=builder.load_mapping_rejections(target,indexes[0],label_index=labels,live=builder.live_records(*indexes))
 except ValueError as exc:
  assert variant=='wrong_owned_kg_node' and 'MIM still publishes the rejected ID' in str(exc)
  results[variant]={'refusal':str(exc)};continue
 assert variant!='wrong_owned_kg_node'
 current=builder.build_unified_rows(actual,*indexes,rejections,labels)
 regressions=builder.build_unified_rows(injected,*indexes,rejections,labels)
 for label,product in [('actual_source',current),('synthetic_reentry',regressions)]:
  builder.write_tsv(product,target/f'{label}.tsv')
  (target/f'{label}.json').write_text(json.dumps(product,indent=2)+'\n')
 by_name={r['ingredient_name']:r for r in regressions}
 for name in names:assert by_name[name]['mim_id']==writer.NEW
 if variant=='complete_ledger':
  for name in names:
   row=by_name[name]
   assert row['cas_rn']=='461-05-2'
   assert not ({row[c] for c in gate.IDENTITY_COLUMNS}&{'CHEBI:48601','CHEBI:91318','cas:461-06-3',writer.OLD})
  assert gate.check(target/'synthetic_reentry.tsv',ledger)==[]
  assert gate.check(target/'actual_source.tsv',ledger)==[]
  assert next(r for r in current if r['ingredient_name']=='DL-carnitine')['chebi_id']=='CHEBI:17126'
  for control in fixture['distinct_controls'].values():assert by_name[control['preferred_term']]['mim_id']==control['identifier']
  assert by_name['carnitinamide chloride']['mim_id']=='CHEBI:48601'
 else:
  assert any(by_name[name]['chebi_id']=='CHEBI:48601' or by_name[name]['culturemech_term_id']=='CHEBI:48601' for name in names)
 results[variant]={'actual_source':current,'synthetic_reentry':regressions}
manifest={'kind':'native offline proposal replay; synthetic amide re-entry is not a current published defect',
 'producer_commit':commit,'producer_sha256':sha((CLAW/'scripts/build_unified_ingredient_mapping.py').read_bytes()),
 'writer_sha256':sha((ROOT/'scripts/merge_carnitine_hydrochloride.py').read_bytes()),
 'source_excerpt':str(source),'source_excerpt_sha256':sha(source.read_bytes()),
 'source_precedence_note':'Frozen free DL occurrences aggregate to CHEBI:17126; underlying solution source is mediadive.compound:1351 and medium source CHEBI:17126, not two identical raw assertions.',
 'proposal_inputs':{str(p):sha(b) for p,b in before.items()},'proposal_outputs':{str(p):sha(b) for p,b in after.items()},'results':results}
(OUT/'receipt.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'variants':list(results),'producer':commit,'receipt_sha256':sha((OUT/'receipt.json').read_bytes())}))
