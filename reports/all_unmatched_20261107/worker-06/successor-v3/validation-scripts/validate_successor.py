"""Read-only full-shard gates; isolated collection overlay only.

No maintained payload, selector, generator, or historical report is written.
Each run requires a fresh log directory and preserves unsuccessful runs.
"""
from pathlib import Path
import argparse, collections, datetime, hashlib, json, os, subprocess, sys
import yaml

ROOT = Path.cwd()
R = ROOT / 'reports/all_unmatched_20261107/worker-06'
S = R / 'successor-v3'
Q = Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
BASE = '1b3641853c7105b9091f81b5a9b19c99e8ed351e'
FROZEN = 'e000d66dd26ab053e9b17ce7bf8d3c873c3dde99'
PY = sys.executable

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def digest(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False).encode()).hexdigest()

def dump(p, obj):
    Path(p).write_text(json.dumps(obj, indent=2, ensure_ascii=False) + '\n')

def read(p):
    return json.loads(Path(p).read_text())

parser = argparse.ArgumentParser()
parser.add_argument('--run', required=True)
args = parser.parse_args()
assert args.run.isalnum() or all(c.isalnum() or c in '-_' for c in args.run)
L = S / 'logs' / args.run
L.mkdir(parents=True, exist_ok=False)
T = ROOT / '.temp/all-unmatched-worker-06/successor-v3' / args.run
T.mkdir(parents=True, exist_ok=False)
D = read(S / 'decisions.json')['decisions']
E = read(S / 'evidence.json')['evidence']
P = read(S / 'proposals.json')['proposals']
OLD = R / 'successor-v2/final'
OD = read(OLD / 'decisions.json')['decisions']
OE = read(OLD / 'evidence.json')['evidence']
OP = read(OLD / 'proposals.json')['proposals']
C = read(Q / 'shards/shard-06.json')['cases']
H = read(S / 'source-holds.json')['cases']
errors = []

def check(ok, msg):
    if not ok:
        errors.append(msg)

check(len(D) == len(C) == len(H) == 188, '188 complete cases')
check([d['case_id'] for d in D] == [c['case_id'] for c in C], 'frozen case order')
check(sha(S/'source-holds.json') == sha(R/'source-holds.json') == sha(OLD/'source-holds.json'), 'all original hold bytes')
for i, (d, c, h) in enumerate(zip(D, C, H)):
    check(d['case_input_sha256'] == digest(c), f'case digest {i}')
    check(d['source'] == {k:c[k] for k in ['source','source_case_id','source_label','raw_source_label']}, f'raw source {i}')
    check(d['occurrence_ids'] == [o['occurrence_id'] for o in c.get('occurrences',[])], f'occurrences {i}')
    check(d['independent_review']['status'] == 'complete', f'independent review {i}')
    check(h['frozen_case_sha256'] == digest(c), f'hold case digest {i}')
    for k,v in h['frozen_source_state'].items():
        check(v == c.get(k,c.get('original_kg_entry',{}).get(k)), f'hold flags {i} {k}')
check(sum(len(d['occurrence_ids']) for d in D)==310, '310 CM occurrence IDs')
hold_count=sum(len(h['frozen_source_state'].get('downstream_holds',[])) for h in H)
check(hold_count==88,'88 downstream holds')
check(len({p['proposal_id'] for p in P})==len(P),'unique proposal IDs')
check(len({p['owner_path'] for p in P})==len(P),'unique proposed owner paths')
eids={e['evidence_id'] for e in E}
check(len(eids)==len(E),'unique evidence IDs')
for e in E:
    cap=e['capture']; check(sha((R if cap['root']=='artifact' else Q)/cap['path'])==cap['sha256'], 'capture '+e['evidence_id'])
old_e={e['evidence_id']:e for e in OE}
changed_e=[e['evidence_id'] for e in E if e['evidence_id'] in old_e and e!=old_e[e['evidence_id']]]
# Evidence ledger metadata may be corrected, while the captured source bytes and
# actual retrieval instant must remain historical facts.
for e in E:
    if e['evidence_id'] in old_e and old_e[e['evidence_id']].get('accessed_at'):
        check(e.get('accessed_at')==old_e[e['evidence_id']]['accessed_at'], 'original retrieval time '+e['evidence_id'])
preserved=[]
for manifest in [R/'SHA256SUMS',R/'successor-v2/SHA256SUMS']:
    count=0
    for line in manifest.read_text().splitlines():
        h,p=line.split('  ',1); check(sha(ROOT/p)==h,'historical manifest entry '+p); count+=1
    original=subprocess.check_output(['git','show',BASE+':'+str(manifest.relative_to(ROOT))])
    check(hashlib.sha256(original).hexdigest()==sha(manifest),'historical manifest bytes '+str(manifest))
    preserved.append({'path':str(manifest.relative_to(ROOT)),'sha256':sha(manifest),'entries':count})
# Every pre-existing tracked path remains byte-identical, not merely old ledgers.
tracked_changes=subprocess.check_output(['git','diff','--name-status',BASE],text=True).splitlines()
check(all(x.startswith('A\t') for x in tracked_changes),'modified/deleted historical tracked path')
paths=subprocess.check_output(['rg','--files','--no-ignore','--hidden','data/ingredients'],text=True).splitlines()
records={p:yaml.safe_load(Path(p).read_text()) for p in paths if p.endswith('.yaml')}
catalog=collections.defaultdict(list)
for p,y in records.items():catalog[y['identifier']].append(p)
ownerhashes={o['path']:o['sha256'] for d in D for o in d['owner_records']}
proposed_ids=[]
for p in P:
    after=R/p['after_capture']['path']; check(sha(after)==p['after_capture']['sha256'],'payload hash '+p['proposal_id'])
    y=yaml.safe_load(after.read_text()); proposed_ids.append(y['identifier'])
    if p['kind']=='new_owner':
        check(not Path(p['owner_path']).exists() and y['identifier'] not in catalog,'new owner collision '+p['proposal_id'])
    else:ownerhashes[p['owner_path']]=p['before_sha256']
for p,h in ownerhashes.items():
    check(sha(p)==h,'current owner hash '+p)
    check(hashlib.sha256(subprocess.check_output(['git','show',FROZEN+':'+p])).hexdigest()==h,'frozen owner hash '+p)
check(len(set(proposed_ids))==len(P),'unique proposed identity identifiers')
maintained=subprocess.check_output(['git','diff','--name-only',BASE,'--','data','mappings','src','conf','docs','UNIFIED_INGREDIENT_MAPPING.tsv','MAPPING_SEMANTICS.md'],text=True).splitlines()
check(not maintained,'maintained paths changed')
old_p={p['proposal_id']:p for p in OP}
changed_p=[p['proposal_id'] for p in P if p['proposal_id'] not in old_p or p!=old_p[p['proposal_id']]]
changed_payloads=[p['proposal_id'] for p in P if p['proposal_id'] not in old_p or p['after_capture']['sha256']!=old_p[p['proposal_id']]['after_capture']['sha256']]
receipt={'status':'FAIL' if errors else 'PASS','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'case_count':len(D),'cm_occurrence_count':310,'hold_count':hold_count,'proposal_count':len(P),'proposal_kinds':dict(collections.Counter(p['kind'] for p in P)),'evidence_count':len(E),'changed_case_indices':[i for i,(a,b) in enumerate(zip(D,OD)) if a!=b],'changed_proposal_metadata_ids':changed_p,'changed_payload_ids':changed_payloads,'corrected_evidence_ids':changed_e,'preserved_historical_manifests':preserved,'maintained_records_enumerated_including_ignored':len(records),'actual_baseline_owner_count':len(ownerhashes),'maintained_changed_paths':maintained,'inputs':{str((S/f).relative_to(ROOT)):sha(S/f) for f in ['decisions.json','evidence.json','proposals.json','source-holds.json']},'errors':errors,'scientific_approval':False}
dump(L/'invariants.json',receipt)
if errors:raise SystemExit('\n'.join(errors))

def run(label,cmd,extra=None):
    out=subprocess.run(cmd,capture_output=True,text=True,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'})
    (L/(label+'.log')).write_text(out.stdout+out.stderr or 'No diagnostics emitted. Exact command and exit code retained in adjacent JSON.\n')
    dump(L/(label+'.json'),{'command':cmd,'exit_code':out.returncode,**(extra or {})})
    if out.returncode:raise SystemExit(out.stdout+out.stderr)

run('structural-command',[PY,str(Q.parent.parent/'scripts/audit_worker_outcomes_v1.py'),'--shard',str(Q/'shards/shard-06.json'),'--decisions',str(S/'decisions.json'),'--evidence',str(S/'evidence.json'),'--proposals',str(S/'proposals.json'),'--artifact-root',str(R),'--source-root',str(Q),'--mim-root',str(ROOT),'--output',str(L/'structural-audit.json')])
run('schema-command',[PY,'scripts/validate_strict.py',*[str(R/p['after_capture']['path']) for p in P],'--out',str(L/'schema.tsv'),'--workers','1'],{'payload_hashes':{p['proposal_id']:p['after_capture']['sha256'] for p in P},'payload_count':len(P)})
for name,rows in [('partonomy-baseline',records),('partonomy-successor',{**records,**{p['owner_path']:yaml.safe_load((R/p['after_capture']['path']).read_text()) for p in P}})]:
    folder=T/name;folder.mkdir()
    for mapped,f in [(True,'mapped_ingredients.yaml'),(False,'unmapped_ingredients.yaml')]:
        (folder/f).write_text(yaml.safe_dump({'ingredients':[y for y in rows.values() if (y.get('mapping_status')=='MAPPED')==mapped]},sort_keys=False,allow_unicode=True))
    run(name,[PY,'scripts/validate_component_partonomy.py','--curated-dir',str(folder)],{'record_count':len(rows),'input_hashes':{f:sha(folder/f) for f in ['mapped_ingredients.yaml','unmapped_ingredients.yaml']},'isolated_overlay_only':True,'maintained_write':False})
print(f'PASS {len(D)} cases, {len(P)} payloads, {len(E)} evidence bindings; complete schema and full-catalogue partonomy; historical bytes preserved')
