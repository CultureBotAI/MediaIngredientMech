import pathlib,json,hashlib,subprocess,datetime
R=pathlib.Path.cwd();O=R/'.temp/gyps-native-origin-v1';C=R.parents[2];OLD=R/'reports/all_unmatched_20261107/worker-03/successors/issue1176-dependencies-v1';HEAD='784ee2541506c914b4c34f091de688d39784d548'
def sha(b):return hashlib.sha256(b).hexdigest()
def canonical(d):return json.dumps(d,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()
def capture(src,rel,expected=None):
 b=src.read_bytes();assert expected is None or sha(b)==expected; p=O/rel;p.parent.mkdir(parents=True,exist_ok=True);assert not p.exists();p.write_bytes(b);return {'path':rel,'sha256':sha(b),'source_path':str(src),'bytes':len(b)}
assert subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()==HEAD
assert not subprocess.check_output(['git','status','--short'],text=True).strip()
rows=[]
for rel in ['HANDOFF.json','MANIFEST.json','dependency-selection.json','machine-ledger.json','lineage-review/verified-origin-inventory-v1.json','inputs/primary/gyps-publication-528.pdf','inputs/primary/gyps-publication-528.txt','inputs/primary-metadata/original-capture-metadata.json','inputs/primary-metadata/original-source-row-recheck.json','skeptical-review/native/review.yaml']:
 p=OLD/rel;b=p.read_bytes();assert subprocess.check_output(['git','show',HEAD+':'+str(p.relative_to(R))])==b;rows.append(capture(p,'inputs/prior-sidecar/'+rel))
rows.append(capture(OLD/'payloads-v2/GYPS.yaml','payloads/GYPS.yaml','fa98f361a39dcaf0bea1f4046829287581bc45e2813044696e5070de58708aa1'))
rows.append(capture(R/'data/ingredients/mapped/GYPS.yaml','inputs/before/GYPS.yaml','36840ca128760eb0ac542753d24d155fd1ebb6ccd8229be130953a0d01f2cf6e'))
review=C/'preflight/w03-peptone-final-head-independent-v1'
rows.append(capture(review/'HANDOFF.json','inputs/distinct-head-review/HANDOFF.json','2d97691f4c83391fcd0d83abc97e3139654b57606e9610ddb018131f6b5ea328'))
for rel in ['MANIFEST.json','review-v3.yaml','review-v3.md','ASSESSMENT-v3.json','prior-review-and-causal-case.json']:
 rows.append(capture(review/rel,'inputs/distinct-head-review/'+rel))
for rel in ['union-ledger.json','shards/shard-03.json','shards/shard-05.json']:
 rows.append(capture(C/'queue/preliminary-v5'/rel,'inputs/frozen/'+pathlib.Path(rel).name))
caseid='KG_CASE:ba039f9e4a33baf69eb111ceb979cf6c9ad8fe788c13488f256336508ce94151';ledger=json.loads((O/'inputs/frozen/union-ledger.json').read_text());case=next(x for x in ledger if x['case_id']==caseid);assert sha(canonical(case))=='d42806e437d2e4c72f3e148314c5ef72e8c21f08c78b7b70eebe3d32c83b67d6'
(O/'inputs/frozen/causal-case.json').write_text(json.dumps(case,indent=2)+'\n')
for src,dst in [(C/'integration/worktree/src/mediaingredientmech/curate/campaign_owner_apply.py','campaign_owner_apply.py'),(C/'integration/final-application-accounting-v3/crosswalk.py','crosswalk.py'),(C/'integration/final-application-accounting-v3/README.md','crosswalk-v3-README.md'),(C/'integration/final-application-accounting-v3/historical-v2/README.md','crosswalk-shape-contract.md'),(R/'MAPPING_SEMANTICS.md','MAPPING_SEMANTICS.md'),(R/'docs/record-reviews.md','record-reviews.md'),(R/'docs/record-review-profile.md','record-review-profile.md')]: rows.append(capture(src,'inputs/contracts/'+dst))
core=[]
for name in ['decisions','proposals','evidence']:
 p=R/f'reports/all_unmatched_20261107/worker-03/successors/issue1226-v1/{name}.json';b=p.read_bytes();assert subprocess.check_output(['git','show',HEAD+':'+str(p.relative_to(R))])==b;core.append({'path':str(p.relative_to(R)),'sha256':sha(b),'count':len(json.loads(b)[name])})
result={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'base_head':HEAD,'old_sidecar':str(OLD.relative_to(R)),'inputs':rows,'prior_core_unchanged':core,'global_case_count':len(ledger),'causal_case_id':caseid,'causal_case_sha256':sha(canonical(case)),'case_hash_method':'SHA256 of UTF8 JSON sort_keys=True,separators=(comma,colon),ensure_ascii=False,allow_nan=False','causal_only':True,'new_W03_assigned_cases':0,'new_GYPS_observations':0,'new_occurrences':0,'capture_policy':'Exact copied raw bytes except explicitly extracted whole causal object, whose native canonical hash is bound to full global frozen ledger. No payload/science/history edits.'}
(O/'input-freeze.json').write_text(json.dumps(result,indent=2)+'\n');print('frozen',len(rows),'casecount',len(ledger),'payloadunchanged')
