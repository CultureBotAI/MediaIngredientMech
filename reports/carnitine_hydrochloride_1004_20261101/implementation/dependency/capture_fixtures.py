from pathlib import Path
import csv,gzip,hashlib,io,json,subprocess
import yaml
ROOT=Path.cwd()
BASE='99fe4b44d78126d78041a69eeb366c52bedf0caa'
OUT=ROOT/'tests/fixtures'
OUT.mkdir(exist_ok=True)
owner='data/ingredients/mapped/NLDM_metabolites.yaml'
sources={}
def read(name):
    raw=subprocess.check_output(['git','show',f'{BASE}:{name}'],cwd=ROOT)
    sources[name]={'kind':'committed git blob','revision':BASE,'sha256':hashlib.sha256(raw).hexdigest()}
    return raw

def rows(raw,kgx=False):
    return list(csv.DictReader(io.StringIO(raw.decode()),delimiter='\t',quoting=csv.QUOTE_NONE if kgx else csv.QUOTE_MINIMAL))

def doc(name):
    return json.loads(read(name))

slice_path=ROOT.parent/'step3-mim-entry-preflight/input-delta/current-carnitine-occurrences.tsv'
slice_bytes=slice_path.read_bytes()
assert hashlib.sha256(slice_bytes).hexdigest()=='e7fdbba52261189a462da2e4ada8f80f99c5b047dbb3d2627c29b545478f2c35'
(OUT/'issue1004-routing-occurrences.tsv').write_bytes(slice_bytes)
sources[str(slice_path)]={'kind':'frozen local source excerpt; source input was gitignored CultureMech output',
 'culturemech_checkout_context':'a74dd489','sha256':hashlib.sha256(slice_bytes).hexdigest(),
 'whole_source_sha256':'e04bc9c22ee753e8456cd6aa7a972b7e6d3c2f114427c87aad44c09e38be236a'}
nldm=yaml.safe_load(read(owner))
component_ids={c['component_id'] for c in nldm['components'] if c.get('reference_scope')=='MIM_CATALOG'}
# Immutable native partonomy context: exact dependency owners, no future live-corpus assumptions.
all_records=yaml.load(read('data/curated/mapped_ingredients.yaml'),Loader=yaml.CSafeLoader)['ingredients']
context=[r for r in all_records if r.get('mapping_status')!='REJECTED' and r.get('identifier') in component_ids and r['identifier']!='kgmicrobe.compound:carnitine_hydrochloride']
assert component_ids-{r['identifier'] for r in context}=={'kgmicrobe.compound:carnitine_hydrochloride'}
control_paths=['data/ingredients/mapped/'+n+'.yaml' for n in ('Dl-carnitine','L-Carnitine','L-Carnitine_Hydrochloride')]
controls={p:yaml.safe_load(read(p)) for p in control_paths}
base='reports/semantic_review_20260921'
original=next(r for r in rows(read(base+'/records.tsv')) if r['source_record']==owner)
historical=[r for r in rows(read(base+'/kgx_assertions.tsv')) if r['source_record']==owner]
archive=doc(base+'/resolution/historical-review-evidence.json')['reports'][original['review_report']]
roles=[r for r in doc(base+'/resolution/roles/inherited-role-review.json')['entries'] if r['source_record']==owner]
prior_dispositions=[r for r in rows(read(base+'/resolution/assertion-dispositions.tsv')) if r['source_record']==owner]
edge_path=ROOT.parent/'step2-mim/output/mim-kgx-710-full/mim_edges.tsv'
edge_raw=edge_path.read_bytes(); edges=[r for r in rows(edge_raw,True) if r['source_record']==owner]
sources[str(edge_path)]={'kind':'ignored generated local KGX input; not a committed source blob',
 'checkout_context':subprocess.check_output(['git','rev-parse','HEAD'],cwd=edge_path.parents[2],text=True).strip(),
 'sha256':hashlib.sha256(edge_raw).hexdigest()}
assert len(edges)==68
canonical=read('mappings/ingredient_mappings.sssom.tsv')
sssom_rows=rows(b'\n'.join(l for l in canonical.splitlines() if not l.startswith(b'#'))+b'\n')
position,mapping=next((i,r) for i,r in enumerate(sssom_rows,1) if r['subject_id']=='MIM:NLDM_metabolites')
mapping_review=doc('reports/sssom_completion_20260921/review.json')
decision=next(d for d in mapping_review['decisions'] if d['source_position']==position)
assert decision['disposition']=='SUPPORTED'
component_plan=doc(base+'/resolution/components/applied-changes.json')[0]
disposition=rows(read(base+'/resolution/components/dispositions.tsv'))[0]
plan_path=component_plan.get('after_path',component_plan['source_record'])
disposition_path=disposition['current_record']
plan_owner_bytes={p:read(p).decode() for p in {plan_path,disposition_path}}
fixture={'kind':'immutable exact owner/review dependency excerpts, not new approval', 'base_revision':BASE,
 'owner':owner,'partonomy_context':context,'distinct_controls':controls,'historical_original_record':original,
 'historical_assertions':historical,'historical_report':archive,'inherited_role_reviews':roles,
 'prior_assertion_dispositions':prior_dispositions,'graph_edges':edges,'mapping_row':mapping,
 'mapping_decision':decision,'component_plan':component_plan,'component_disposition':disposition,
 'explicit_plan_owner_bytes':plan_owner_bytes}
payload=(json.dumps(fixture,sort_keys=True,indent=2)+'\n').encode()
path=OUT/'issue1004-routing-dependencies.json.gz';path.write_bytes(gzip.compress(payload,mtime=0))
manifest={'base_revision':BASE,'inputs':sources,'fixtures':{
 'issue1004-routing-occurrences.tsv':{'sha256':hashlib.sha256(slice_bytes).hexdigest()},
 path.name:{'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'uncompressed_sha256':hashlib.sha256(payload).hexdigest()}}}
(OUT/'issue1004-routing-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'partonomy_dependency_records':len(context),'historical_claims':len(historical),
'graph_claims':len(edges),'role_reviews':len(roles),'fixture_bytes':len(path.read_bytes())}))
