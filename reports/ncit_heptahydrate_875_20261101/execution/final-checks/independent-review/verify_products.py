"""Read-only checks of actual refresh, unified and semantic boundaries."""
from pathlib import Path
from collections import Counter
import csv,io,json,subprocess,sys
from mediaingredientmech import ingredient_bundle_refresh as r
from mediaingredientmech.export.reviewed_sssom import load_review
from mediaingredientmech.ingredient_bundle_contract import read_json,content_sha256
ROOT=Path(sys.argv[1]).resolve();BASE='40b787d37d33d544551389ff019f2d64ad63d7cc';OUT=Path(__file__).resolve().parent
OWNER='data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml';SUBJECT='MIM:Na2hpo4_X_7_H2o'
def historical(p):return subprocess.check_output(['git','show',BASE+':'+p],cwd=ROOT)
def table(b):return list(csv.DictReader(io.StringIO(b.decode()),delimiter='\t'))
prior_path='reports/ingredient_bundle_20261101_followup/review.json';prefix=ROOT/'reports/ingredient_bundle_20261101_ncit875'
prior=read_json(historical(prior_path));before={p:historical(p) for p in r.source_names(prior)};current={p:(ROOT/p).read_bytes() for p in before};contracts={p:(ROOT/p).read_bytes() for p in r.CONTRACTS}
assert historical(prior_path)==(ROOT/prior_path).read_bytes()==(prefix/'prior-review.json').read_bytes()
load_review(ROOT,Path(prior['base_review']))
successor,audit=r.verify_unchanged_cohort(prior,before,current,contracts,contracts)
assert r.encode(successor)==(prefix/'review.json').read_bytes()
saved=read_json((prefix/'dependency-refresh.json').read_bytes())
assert all(saved[k]==v for k,v in audit.items())
assert saved['historical_commit']==BASE
assert saved['producer_sha256']==content_sha256((ROOT/'src/mediaingredientmech/ingredient_bundle_refresh.py').read_bytes())
assert saved['prior_review_sha256']==content_sha256(historical(prior_path))
assert saved['successor_review_sha256']==content_sha256(r.encode(successor))
checks={'companion':{'exact_native_successor_replay':True,'all_audit_fields_reproduced':True,'owners':len(successor['record_inputs']),'claims':saved['claim_counts'],'relocated_decisions':sum(x['base_decision_locations']['before']!=x['base_decision_locations']['after'] for x in audit['selected_mapping_evidence_unchanged']),'scientific_approval_added':audit['scientific_approval_added']}}
up='UNIFIED_INGREDIENT_MAPPING.tsv';old=table(historical(up));new=table((ROOT/up).read_bytes());a={x['ingredient_name']:x for x in old};b={x['ingredient_name']:x for x in new}
assert len(old)==len(a)==len(new)==len(b)==4170 and a.keys()==b.keys()
changed={k:{f:{'before':a[k][f],'after':b[k][f]} for f in a[k] if a[k][f]!=b[k][f]} for k in a if a[k]!=b[k]}
assert set(changed)=={'Na2HPO4 x 7 H2O','Na2HPO4.7H2O','Na2HPO4·7H2O'}
for label,delta in changed.items():
 assert set(delta)=={'mim_id','synonyms'},(label,delta)
 assert b[label]['mim_id']=='NCIT:C61946' and b[label]['mapping_status']=='MAPPED'
 assert b[label]['chebi_id']==b[label]['kg_microbe_node_id']=='' and b[label]['culturemech_term_id']!='CHEBI:34683'
 assert b[label]['cas_rn']=='7782-85-6'
 assert set(b[label]['synonyms'].split('|'))-set(a[label]['synonyms'].split('|'))=={'Sodium Phosphate, Dibasic, Heptahydrate'}
 assert set(a[label]['synonyms'].split('|'))<=set(b[label]['synonyms'].split('|'))
 assert a[label]['occurrence_count']==b[label]['occurrence_count'] and a[label]['example_media']==b[label]['example_media']
assert sum(int(x['occurrence_count']) for x in old)==sum(int(x['occurrence_count']) for x in new)==209330
assert not [x for x in new if x['mapping_status']=='REJECTED' and not x['mim_id']]
assert not [x for x in new if x['mim_id'].startswith('kgmicrobe.compound:') and any('CHEBI:' in x[k] for k in ['chebi_id','culturemech_term_id','kg_microbe_node_id'])]
checks['unified']={'rows':len(new),'occurrences':209330,'changed_rows':changed,'unchanged_rows':len(new)-len(changed),'rejected_empty_mim_id':0,'compound_chebi_leaks':0,'sha256':content_sha256((ROOT/up).read_bytes())}
# No semantic finding is retired and no nonmapping assertion approval changes.
fp='reports/semantic_review_20260921/resolution/finding-dispositions.tsv';fa=table(historical(fp));fb=table((ROOT/fp).read_bytes());assert len(fa)==len(fb)
fdelta=[]
for x,y in zip(fa,fb,strict=True):
 if x!=y:
  delta=[k for k in x if x[k]!=y[k]]
  assert delta==['current_record_sha256'] and x['source_record']==OWNER
  fdelta.append(x['finding_id'])
assert len(fdelta)==2
ap='reports/semantic_review_20260921/resolution/assertion-dispositions.tsv';aa=table(historical(ap));ab=table((ROOT/ap).read_bytes())
non_a={x['assertion_id']:x for x in aa if x['assertion_type']!='mapping'};non_b={x['assertion_id']:x for x in ab if x['assertion_type']!='mapping'};assert non_a.keys()==non_b.keys()
for ident,x in non_a.items():
 y=non_b[ident]
 if x!=y:assert [k for k in x if x[k]!=y[k]]==['source_record_sha256'] and x['source_record']==OWNER and x['resolution_status']==y['resolution_status']=='OPEN'
# Compare complete mapping decision semantics through the receipt's position map.
mp='reports/sssom_completion_20260921/review.json';ma=read_json(historical(mp));mb=read_json((ROOT/mp).read_bytes())
receipt=read_json((ROOT/'reports/sssom_completion_20260921/mapping_changes/issue875-ncit-exact-heptahydrate.json').read_bytes())
oldproof=read_json(historical('reports/sssom_completion_20260921/mapping-evidence.json'));newproof=read_json((ROOT/'reports/sssom_completion_20260921/mapping-evidence.json').read_bytes())
for x,pos in zip(ma['decisions'],receipt['position_map'],strict=True):
 if x['owner_record']==OWNER:continue
 assert pos is not None
 y=mb['decisions'][pos-1]
 assert {k:v for k,v in x.items() if k not in {'source_position','evidence_key'}}=={k:v for k,v in y.items() if k not in {'source_position','evidence_key'}}
 assert oldproof['entries'][x['evidence_key']]==newproof['entries'][y['evidence_key']]
assert [d['disposition'] for d in mb['decisions'] if d['owner_record']==OWNER]==['WITHHOLD']
checks['semantic_boundary']={'finding_hash_updates_only':fdelta,'nonmapping_assertions_approval_preserved':True,'all_non_target_mapping_decisions_and_evidence_preserved':True,'old_status_counts':dict(Counter(x['resolution_status'] for x in aa)),'new_status_counts':dict(Counter(x['resolution_status'] for x in ab)),'target_mapping':'WITHHOLD','target_buffer':'OPEN'}
(OUT/'products-verification.json').write_bytes(r.encode({'baseline':BASE,'checks':checks}))
print(json.dumps(checks,indent=2))
