"""Native producer + actual test-function replay on external membership fixtures."""
from pathlib import Path
from datetime import datetime, timezone
import copy,csv,hashlib,importlib.util,json,subprocess,sys,traceback
import yaml
OUT=Path(__file__).resolve().parent
RUN=OUT.parents[1]
ROOT=RUN/'step2-mim'
sys.path[:0]=[str(ROOT/'src'),str(RUN/'claw-source/src')]
def load(name,rel):
    spec=importlib.util.spec_from_file_location(name,ROOT/rel)
    mod=importlib.util.module_from_spec(spec);sys.modules[name]=mod;spec.loader.exec_module(mod);return mod
producer=load('independent_membership_producer','scripts/build_culturemech_membership.py')
target=load('independent_membership_regression','tests/test_repair_heptahydrate_membership.py')
ordinary=load('independent_membership_invariants','tests/test_culturemech_membership.py')
from mediaingredientmech.utils.culturemech_occurrences import effective_occurrence_statistics,membership_counts,mim_identifier_for_occurrence
archive=ROOT/'reports/sssom_scientific_curation_20261101/audit875/current-culturemech-occurrences.tsv'
with archive.open(newline='') as f:
    reader=csv.DictReader(f,delimiter='\t');fields=reader.fieldnames;source=[r for r in reader if mim_identifier_for_occurrence(r)==target.guarded.NEW]
assert len(source)==32
with (ROOT/target.writer.MEMBERSHIP).open() as f:
    current=list(csv.DictReader((line for line in f if not line.startswith('#')),delimiter='\t'))
records=yaml.safe_load((ROOT/'data/curated/mapped_ingredients.yaml').read_text())['ingredients']
known=producer.mim_identifiers()
owner=yaml.safe_load((ROOT/target.guarded.OWNER).read_text())
source_paths=['scripts/build_culturemech_membership.py','src/mediaingredientmech/utils/culturemech_occurrences.py','tests/test_repair_heptahydrate_membership.py','tests/test_culturemech_membership.py','mappings/culturemech_recipe_membership.tsv']
hashes={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in source_paths}
results={'at':datetime.now(timezone.utc).isoformat(),'head':subprocess.check_output(['git','-C',str(ROOT),'rev-parse','HEAD'],text=True).strip(),'source_hashes':hashes,'synthetic_future_source_variants':True,'production_writes':False,'cases':[]}
for case in ['unchanged_archived_32','new_recipe_same_accepted_label','repeat_in_existing_recipe']:
    fixture=OUT/case;fixture.mkdir()
    rows=copy.deepcopy(source)
    if case!='unchanged_archived_32':
        new=copy.deepcopy(source[0])
        if case=='new_recipe_same_accepted_label':
            new['recipe_id']='CultureMech:999999';new['recipe_label']='future_review_fixture';new['source_path']='bacterial/future_review_fixture.yaml'
        else:new['component_index']='99'
        rows.append(new)
    source_path=fixture/'occurrences.tsv'
    with source_path.open('w',newline='') as f:
        w=csv.DictWriter(f,fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
    edges,unknown=producer.collect(source_path,known)
    assert not unknown and all(ident==target.guarded.NEW for ident,recipe in edges)
    all_edges={(r['mim_identifier'],r['recipe_id']):int(r['occurrences']) for r in current if r['mim_identifier']!=target.guarded.NEW}
    all_edges.update(edges)
    producer.OUTPUT=fixture/target.writer.MEMBERSHIP
    producer.write(all_edges,f'independent synthetic source evolution case={case}')
    with producer.OUTPUT.open() as f:published=list(csv.DictReader((l for l in f if not l.startswith('#')),delimiter='\t'))
    ordinary.test_every_published_identifier_is_held_by_active_record(published,records)
    ordinary.test_edges_are_unique_so_a_rebuild_cannot_duplicate_them(published)
    ordinary.test_the_artifact_is_sorted_so_rebuilds_diff_cleanly(published)
    ordinary.test_both_sides_are_stable_ids(published)
    target.ROOT=fixture
    try:
        target.test_committed_memberships_do_not_reuse_retired_identity()
        verdict='PASS';failure=None
    except AssertionError:
        verdict='FAIL';failure=traceback.format_exc()
    effective=effective_occurrence_statistics(owner,membership_counts(producer.OUTPUT))
    results['cases'].append({'case':case,'source_rows':len(rows),'native_selected_edges':len(edges),'native_occurrences':sum(edges.values()),'unknown':unknown,'published_edges':len(published),'ordinary_owner_unique_sorted_stable_id_invariants':'PASS','effective_counts':effective,'actual_live_test':verdict,'traceback':failure,'membership_sha256':hashlib.sha256(producer.OUTPUT.read_bytes()).hexdigest()})
assert [c['actual_live_test'] for c in results['cases']]==['PASS','PASS','PASS']
for p,h in hashes.items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,p
results['source_status']=subprocess.check_output(['git','-C',str(ROOT),'status','--short'],text=True).strip()
(OUT/'results.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
