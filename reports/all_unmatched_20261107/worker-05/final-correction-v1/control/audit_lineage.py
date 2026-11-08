from pathlib import Path
from datetime import datetime,timezone
import argparse,collections,hashlib,json,re,yaml
W=Path.cwd();S=W/'.temp/w05-final-correction-v1';B=W/'reports/all_unmatched_20261107/worker-05';N=B/'correction-1193-v1'
ap=argparse.ArgumentParser();ap.add_argument('--core',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
objsha=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
def rows(p,k):
 x=json.loads(p.read_text());return x[k] if isinstance(x,dict) else x
def resolve(cap):
 p=B/cap['path']
 if not p.is_file():p=S/cap['path'].removeprefix('final-correction-v1/')
 assert sha(p)==cap['sha256'];return p
old={p['proposal_id']:p for p in rows(N/'proposals.json','proposals')}
new={p['proposal_id']:p for p in rows(a.core/'proposals.json','proposals')}
lineage=rows(a.core/'proposal-lineage.json','rows');changes=[];errors=[];records={};old_records={};pid_map={}
for lin in lineage:
 pid=lin['proposal_id'];p=new[pid];records[pid]=yaml.safe_load(resolve(p['after_capture']).read_text())
 if not lin['predecessor_proposal_id']:continue
 oldid=lin['predecessor_proposal_id'];pid_map[oldid]=pid;o=yaml.safe_load(resolve(old[oldid]['after_capture']).read_text());r=records[pid];old_records[oldid]=o
 fields=[k for k in sorted(set(o)|set(r)) if o.get(k)!=r.get(k)]
 history=o.get('curation_history',[]);history_ok=r.get('curation_history',[])[:len(history)]==history
 neg=[x for x in o.get('synonyms',[]) if x.get('synonym_type')=='REJECTED_LABEL'];neg_ok=all(x in r.get('synonyms',[]) for x in neg)
 preserve_fields=[k for k in set(o)|set(r) if 'occurrence' in k or k in ['roles','organism_roles','causal_graphs']]
 unchanged_scoped=all(o.get(k)==r.get(k) for k in preserve_fields)
 if not(history_ok and neg_ok and unchanged_scoped):errors.append(dict(proposal_id=pid,history_ok=history_ok,negative_ok=neg_ok,scope_fields_ok=unchanged_scoped))
 changes.append(dict(proposal_id=pid,predecessor=oldid,changed_top_level_fields=fields,changed_payload=bool(fields),
   history_prefix_preserved=history_ok,inherited_negative_objects_preserved=neg_ok,
   unchanged_scope_fields=preserve_fields,scope_fields_unchanged=unchanged_scoped,
   before_capture=old[oldid]['after_capture'],after_capture=p['after_capture']))
suggestions=json.loads((S/'control/w05-provenance-suggestions.json').read_text())['rows'];typing=[]
for suggestion in suggestions:
 oldid=suggestion['proposal_id'];pid=pid_map[oldid];i=int(re.search(r'\[(\d+)\]',suggestion['field']).group(1))
 o=old_records[oldid]['ontology_mapping']['evidence'][i];r=records[pid]['ontology_mapping']['evidence'][i]
 assert o['evidence_type']=='MANUAL_CURATION'
 expected=suggestion['suggested_native_type'];ok=r['evidence_type']==expected
 if not ok:errors.append(dict(proposal_id=pid,field=suggestion['field'],expected=expected,actual=r['evidence_type']))
 typing.append(dict(audit_row_id=suggestion['audit_row_id'],proposal_id=pid,predecessor_proposal_id=oldid,
  field=suggestion['field'],audit_expected_type=expected,before=o,after=r,
  before_value_sha256=objsha(o),after_value_sha256=objsha(r),type_pass=ok,
  changed_entry_fields=[k for k in sorted(set(o)|set(r)) if o.get(k)!=r.get(k)],
  audit_source_full_value_sha256=suggestion['full_value_sha256']))
receipt=dict(at=datetime.now(timezone.utc).isoformat(),auditor='/root',scope='Exact predecessor/successor and source-lineage validation, not chemical approval',
 original_proposals_accounted=len(pid_map),selected_proposals=len(new),changed_original_payloads=sum(x['changed_payload'] for x in changes),
 byte_identical_original_payloads=sum(x['before_capture']['sha256']==x['after_capture']['sha256'] for x in changes),
 original_payload_lineage=changes,mapping_type_entries=typing,mapping_type_totals=dict(collections.Counter(x['after']['evidence_type'] for x in typing)),
 errors=errors,status='PASS' if not errors else 'FAIL')
assert not a.out.exists();a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({k:receipt[k] for k in ['status','original_proposals_accounted','selected_proposals','changed_original_payloads','byte_identical_original_payloads','mapping_type_totals','errors']}))
raise SystemExit(bool(errors))
