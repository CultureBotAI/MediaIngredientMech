"""Worker09 artifact assembly, 2026-11-08. No scientific decisions are generated.
Inputs: immutable shard and three independently authored group bundles.
Output: aggregate outcome-contract files and mechanical progress accounting.
"""
import collections, datetime, hashlib, json
from pathlib import Path
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'MAPPING_SEMANTICS.md').is_file())
OUT=ROOT/'reports/all_unmatched_20261107/worker-09'
SHARD=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5/shards/shard-09.json')
GROUPS=('antibiotics','salts','materials')
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
def check_cases(cases,decisions):
 original={c['case_id']:c for c in cases};counts=collections.Counter(d['case_id'] for d in decisions)
 if set(counts)!=set(original) or any(n!=1 for n in counts.values()):raise ValueError('Decisions must account for exactly every case once')
 for d in decisions:
  c=original[d['case_id']]
  if d['case_input_sha256']!=digest(c):raise ValueError('Changed case hash: '+c['case_id'])
  if d['source']!={k:c[k] for k in ('source','source_case_id','source_label','raw_source_label')}:raise ValueError('Changed source fields: '+c['case_id'])
  if sorted(d['occurrence_ids'])!=sorted(o['occurrence_id'] for o in c.get('occurrences',[])):raise ValueError('Changed occurrences: '+c['case_id'])
def write(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def main():
 shard=json.loads(SHARD.read_text()); combined={k:[] for k in ('decisions','evidence','proposals')}
 for g in GROUPS:
  for key in combined:
   x=json.loads((OUT/g/(key+'.json')).read_text());combined[key].extend(x[key])
 check_cases(shard['cases'],combined['decisions'])
 for key,idkey in [('evidence','evidence_id'),('proposals','proposal_id')]:
  counts=collections.Counter(x[idkey] for x in combined[key]);duplicates=[k for k,n in counts.items() if n!=1]
  if duplicates:raise ValueError(f'duplicate {key} identifiers: {duplicates}')
 byid={d['case_id']:d for d in combined['decisions']};ordered=[byid[c['case_id']] for c in shard['cases']]
 write(OUT/'decisions.json',dict(schema_version=1,worker_slot=9,shard_sha256=hashlib.sha256(SHARD.read_bytes()).hexdigest(),phase='shard',decisions=ordered))
 for key in ('evidence','proposals'):write(OUT/(key+'.json'),dict(schema_version=1,**{key:combined[key]}))
 reviewed=[d['case_id'] for d in ordered if d['independent_review']['status']=='complete'];pending=[d['case_id'] for d in ordered if d['case_id'] not in reviewed]
 write(OUT/'progress.json',dict(assigned_count=len(ordered),primary_decision_count=len(ordered),reviewed_count=len(reviewed),remaining_count=len(pending),assigned_case_ids=[c['case_id'] for c in shard['cases']],reviewed_case_ids=reviewed,remaining_case_ids=pending,current_task='Final validation and handoff' if not pending else 'Independent skeptical review and remediation',blockers=[],updated_at=datetime.datetime.now(datetime.timezone.utc).isoformat()))
 print(json.dumps({'cases':len(ordered),'reviewed':len(reviewed),'evidence':len(combined['evidence']),'proposals':len(combined['proposals'])}))
if __name__=='__main__':main()
