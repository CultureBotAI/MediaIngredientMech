"""Read-only derived-output/scope audit before final local checks finish."""
from pathlib import Path
import collections,csv,datetime,hashlib,io,json,subprocess,sys
HERE=Path(__file__).resolve().parent; RUN=HERE.parents[1]; W=RUN/'step8-aliases'; BASE='0ee56c11a2894ed50a476b331d56297be0a3ee12'
sys.path[:0]=[str(W),str(W/'src')]
from mediaingredientmech.ingredient_bundle_contract import reviewed_products

def sha(b):return hashlib.sha256(b).hexdigest()
def git(*args):return subprocess.check_output(['git','-C',str(W),*args])
def raw(name):return (W/name).read_bytes()
def old(name):return git('show',BASE+':'+name)
def doc(name):return json.loads(raw(name))
def table(b):return list(csv.DictReader([l for l in b.decode().splitlines() if not l.startswith('#')],delimiter='\t'))
CAN='mappings/ingredient_mappings.sssom.tsv'; REV='reports/sssom_completion_20260921/review.json'; EV='reports/sssom_completion_20260921/mapping-evidence.json'; P='reports/owned_name_deferred_669_20261103';prior_path='reports/step7d_mapping_901_20261103/refresh-v2/companion-review.json'
plan=doc(P+'/publication-plan.json');selected={p['source_position'] for p in plan['pairs']};rows=table(raw(CAN));before_rows=table(old(CAN));a=json.loads(old(REV));b=doc(REV);olddec={d['source_position']:d for d in a['decisions']};newdec={d['source_position']:d for d in b['decisions']};assert set(olddec)==set(newdec)==set(range(1,3015));assert a['record_inputs']==b['record_inputs'];assert b['source_sha256']==sha(raw(CAN));decision_changes=[]
for pos in olddec:
 assert olddec[pos]['disposition']==newdec[pos]['disposition']
 if pos in selected:assert newdec[pos]['disposition']=='WITHHOLD'
 else:assert olddec[pos]==newdec[pos]
 if olddec[pos]!=newdec[pos]:decision_changes.append({'position':pos,'fields':[k for k in olddec[pos] if olddec[pos][k]!=newdec[pos][k]]})
assert len(decision_changes)==23
supported=[rows[p-1] for p in newdec if newdec[p]['disposition']=='SUPPORTED'];withheld=[rows[p-1] for p in newdec if newdec[p]['disposition']=='WITHHOLD'];assert supported==[before_rows[p-1] for p in olddec if olddec[p]['disposition']=='SUPPORTED']
reviewed='output/mim-reviewed-sssom'; rm=doc(reviewed+'/manifest.json');assert rm['source_sha256']==sha(raw(CAN)) and rm['review_sha256']==sha(raw(REV));assert table(raw(reviewed+'/ingredient_mappings.sssom.tsv'))==supported;assert table(raw(reviewed+'/withheld_mappings.sssom.tsv'))==withheld
for name,value in rm['files'].items():assert sha(raw(reviewed+'/'+name))==value
prior=json.loads(old(prior_path));assert raw(prior_path)==old(prior_path)==raw(P+'/prior-companion-review.json');comp=doc(P+'/companion-review.json');assert comp['decisions']==prior['decisions'] and comp['record_inputs']==prior['record_inputs'];assert comp['claims_file']==prior['claims_file'] and comp['claims_sha256']==prior['claims_sha256']==sha(raw(comp['claims_file']));claims=doc(comp['claims_file'])['claims'];assert len(claims)==51 and len(comp['record_inputs'])==20
names={comp['claims_file'],comp['base_review'],*comp['inputs'],*comp['record_inputs']};products,proof=reviewed_products(comp,{name:raw(name) for name in names});product_checks={}
for name,content in products.items():
 assert raw('output/mim-reviewed-ingredient-bundle/'+name)==content,name
 product_checks[name]=sha(content)
refresh=doc(P+'/companion-refresh-receipt.json');assert refresh['scientific_approval_added'] is False;assert refresh['successor_review_sha256']==sha(raw(P+'/companion-review.json'));assert refresh['claim_counts']==dict(collections.Counter(c['kind'] for c in claims));assert refresh['historical_commit']==BASE
DIS='reports/semantic_review_20260921/resolution/assertion-dispositions.tsv';od=table(old(DIS));nd=table(raw(DIS));key=lambda x:(x['source_record'],x['assertion_type'],x['source_position']);oo={key(r):r for r in od};nn={key(r):r for r in nd};assert len(oo)==len(od)==len(nn)==len(nd)==4519 and oo.keys()==nn.keys();changed=collections.Counter();mapping_changed=[]
for k,v in oo.items():
 n=nn[k];assert v['resolution_status']==n['resolution_status']
 if v['assertion_type']!='mapping':assert v==n
 else:
  assert n['source_record_sha256']==sha(raw(CAN))
  fields=[f for f in v if v[f]!=n[f]]
  for f in fields:changed[f]+=1
  if v['review_reason']!=n['review_reason']:mapping_changed.append(int(v['source_position']))
assert set(mapping_changed)<=selected
SEM='reports/semantic_review_20260921/resolution/current-review.json';sem=doc(SEM);oldsem=json.loads(old(SEM));assert sem['release_verdict']==oldsem['release_verdict']=='FAIL';assert sem['bundle']=='output/mim-kgx-710-full';assert len(sem['blocking_finding_ids'])==len(oldsem['blocking_finding_ids']);assert len(sem['blocking_assertion_ids'])==len(oldsem['blocking_assertion_ids']);assert sem['evidence_gaps']==oldsem['evidence_gaps'];assert sem['inputs']['output/mim-kgx-710-full/manifest.json']==sha(raw('output/mim-kgx-710-full/manifest.json'))
sm=doc('output/mim-kgx-710-supported/manifest.json');assert sm['release_verdict']=='PASS' and sm['full_release_verdict']=='FAIL';assert table(raw('output/mim-kgx-710-supported/ingredient_mappings.sssom.tsv'))==supported;assert sm['full_bundle_manifest_sha256']==sha(raw('output/mim-kgx-710-full/manifest.json'))
oldselector=prior_path.encode();newselector=(P+'/companion-review.json').encode()
for name in ['tests/test_ingredient_bundle.py','.github/workflows/qc-reviewed-sssom.yaml']:
 assert old(name).count(oldselector)==1 and raw(name)==old(name).replace(oldselector,newselector)
assert git('diff','--name-only',BASE,'--','.github/workflows').decode().splitlines()==['.github/workflows/qc-reviewed-sssom.yaml']
assembler='reports/sssom_completion_20260921/assemble_review.py';assert raw(assembler)==old(assembler).replace(b'REVIEWED_SOURCE = "'+sha(old(CAN)).encode()+b'"',b'REVIEWED_SOURCE = "'+sha(raw(CAN)).encode()+b'"')
allowed={'src/mediaingredientmech/ingredient_bundle_refresh.py','src/mediaingredientmech/owned_name_suppression_refresh.py','src/mediaingredientmech/profiles/owned_name_suppression_v1.schema.json','tests/test_ingredient_bundle.py','tests/test_owned_name_suppression_refresh.py','tests/test_sssom_other_cross_record.py','.github/workflows/qc-reviewed-sssom.yaml',assembler}
actual=set(git('diff','--name-only',BASE,'--','src','tests','.github','justfile','pyproject.toml','uv.lock','conf','scripts',assembler).decode().splitlines());assert actual==allowed,(actual-allowed,allowed-actual)
for name in ['UNIFIED_INGREDIENT_MAPPING.tsv','UNIFIED_INGREDIENT_MAPPING.provenance.json','.github/workflows/qc-evidence.yaml','src/mediaingredientmech/form_mapping_review.py','scripts/validate_sssom_invariants.py']:
 assert raw(name)==old(name)
report={'reviewer':'/root/step7d_independent_review','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'observed_head':git('rev-parse','HEAD').decode().strip(),'scope':'Actual complete derived outputs and allowed code/test/workflow scope; final local/CI checks pending','verdict':'PASS for this content audit','counts':{'canonical':len(rows),'supported_mapping_rows':len(supported),'withheld_mapping_rows':len(withheld),'selected_withheld':len(selected),'companion_owners':len(comp['record_inputs']),'companion_claims':len(claims),'semantic_assertions':len(nd),'semantic_statuses':dict(collections.Counter(r['resolution_status'] for r in nd)),'blocking_findings':len(sem['blocking_finding_ids']),'blocking_assertions':len(sem['blocking_assertion_ids']),'evidence_gap_groups':len(sem['evidence_gaps'])},'decision_changes':decision_changes,'semantic_changed_fields':dict(changed),'companion_products_sha256':product_checks,'semantic_release_verdict':sem['release_verdict'],'supported_subset_release_verdict':sm['release_verdict'],'allowed_source_test_workflow_paths':sorted(actual),'finding_ids_to_resolve_after_final_checks':['deferred23-immediate-completion-source-inventory','deferred23-publication-log-proof-role-alias','deferred23-native-evidence-continuation-refusal','deferred23-fixture-discards-history-prefix'],'findings':[],'limitations':['Full QC/test results were not assumed; exact published head and CI remain pending.','Default nested-worktree native B4 was skipped; no B4-active claim is made.','Subset support/typed review refresh does not make full corpus release ready or approve the23 suppressed rows.']}
p=HERE/'final-derived-audit-v1.json';assert not p.exists();p.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'output':str(p),'sha256':sha(p.read_bytes()),'counts':report['counts'],'semantic_changed_fields':dict(changed)},indent=2))
