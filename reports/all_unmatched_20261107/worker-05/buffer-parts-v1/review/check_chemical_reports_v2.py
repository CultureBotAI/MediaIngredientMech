import json, hashlib, pathlib, subprocess, importlib.util, sys
from datetime import datetime, timezone
import yaml
R=pathlib.Path.cwd(); S=R/'.temp/w05-buffer-parts-v1'; B=R/'reports/all_unmatched_20261107/worker-05'
def h(p):return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def oh(x):return hashlib.sha256(json.dumps(x,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
def read(p):return json.loads(pathlib.Path(p).read_text())
base=read(B/'tellurium-polypeptone-v1/core/proposals.json')['proposals']; bp={p['proposal_id']:p for p in base}
ps=read(S/'chemical-reports/proposals.json')['proposals']; ds=read(S/'chemical-reports/decisions.json')['decisions']
bd={d['case_id']:d for d in read(B/'tellurium-polypeptone-v1/core/decisions.json')['decisions']}
checks=[]
for p in ps:
 f=B/p['after_capture']['path']; gh=subprocess.check_output(['git','show','0bac12cabfd1f67f212631d8eef9aa46379f6b41:'+str(f.relative_to(R))])
 checks.append({'proposal_id':p['proposal_id'],'proposal_object_sha256':oh(p),'unchanged_proposal':p==bp[p['proposal_id']],'after_capture':p['after_capture'],'current_hash_matches':h(f)==p['after_capture']['sha256'],'base_git_bytes_equal':gh==f.read_bytes()})
dc=[]
for d in ds:
 old=bd[d['case_id']]; delta={k:v for k,v in d.items() if old.get(k)!=v};assert set(delta)=={'evidence_ids','chemical_report_verification'}
 assert set(old['evidence_ids'])<=set(d['evidence_ids'])
 dc.append({'case_id':d['case_id'],'before_object_sha256':oh(old),'selected_decision_object_sha256':oh(d),'changed_fields':list(delta),'all_other_fields_including_holds_identical':True})
f=read(S/'chemical-reports/finding-verification-v1.json'); historical=[]
for row in f['rows']:
 original_file=S/'chemical-reports/inputs/triage'/('finding-'+row['finding_id'][-3:]+'-initial.json'); assert h(original_file)==row['original_finding_sha256']; assert read(original_file)==row['original_finding']
 for ref in row['corrected_historical_report_bindings']:
  q=B/ref['report']; v=read(q); assert h(q)==ref['report_sha256']; arr=v[ref['field']]; matches=[x for x in arr if oh(x)==ref['object_sha256']];assert len(matches)==1
  historical.append({'finding_id':row['finding_id'],'report':str(q.relative_to(R)),'sha256':h(q),'object_sha256':ref['object_sha256'],'exact_object_verified':True})
builder=pathlib.Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/kgm-unmapped-20261107/claw/scripts/build_mim_ingredient_sssom.py')
assert h(builder)==h(B/'final-correction-v1/inputs/pinned-native-row-builder.py')
sys.path.insert(0,str(builder.parent));spec=importlib.util.spec_from_file_location('w05review_native',builder);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
p=next(p for p in ps if p['proposal_id']=='CHEM-C1193-Tris-HCl-salt'); q=B/p['after_capture']['path'];record=yaml.safe_load(q.read_text());rows=m._row_from_yaml(q,{},{},{},{},record=record,owners={})
assert len(rows)==3
assert {x['predicate_id'] for x in rows}=={'skos:exactMatch','skos:broadMatch'}
assert {x['object_id'] for x in rows}=={'CHEBI:9754','cas:1185-53-1','kgmicrobe.compound:tris_hydrochloride_salt'}
shard=read(B/'contracts/shard-05.json'); caseindex={x['case_id']:x for x in shard['cases']}
eth=[d for d in ds if d['case_id'] in ['CM_NAME:e56f64c93c94d3ae719a19c4aed635437b7172cd38eb6e4099740780e0c8e2da','CM_NAME:fddd9315d7231b1b5a11f98a7424dbf1c27e78964249cd2240ed46d59eb3baac']]
ep=next(p for p in ps if p['proposal_id']=='CHEM-C1193-ethanol95-dsmz_78')
occ=[x for d in eth for x in d['occurrence_ids']]; assert len(set(occ))==12
source=[]
for x in read(S/'chemical-reports/primary-read-ledger-v1.json')['full_primary_sources']:
 q=S/'chemical-reports'/x['path'];assert h(q)==x['sha256'];source.append({'path':str(q.relative_to(R)),'sha256':h(q)})
out={'reviewer':'/root/final_skeptical','at':datetime.now(timezone.utc).isoformat(),'payload_checks':checks,'decision_checks':dc,'exact_historical_report_objects':historical,'native_builder_sha256':h(builder),'tris_complete_native_rows':rows,'ethanol_occurrences':occ,'ethanol_count':len(occ),'primary_capture_checks':source,'limitations':['These deterministic checks bind bytes, preservation and native semantics; source-scientific assessment is separate.','No maintained owner or export application is approved.']}
dest=S/'review/chemical-report-independent-checks-v1.json';assert not dest.exists();dest.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print(dest.relative_to(R),h(dest));print('payloads',len(checks),'cases',len(dc),'native rows',len(rows),'historical bound objects',len(historical))
