"""Independent assembly/accounting inspection. Does not supply scientific conclusions."""
import argparse, collections, copy, hashlib, json, traceback
from pathlib import Path
from datetime import datetime, timezone
import yaml

W=Path.cwd(); S=W/'.temp/w05-final-correction-v1'; O=S/'review-assembly'
B=W/'reports/all_unmatched_20261107/worker-05'; N=B/'correction-1193-v1'
C=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107')
Q=C/'queue/preliminary-v5'
ap=argparse.ArgumentParser();ap.add_argument('--core',type=Path,required=True);ap.add_argument('--output',required=True);ap.add_argument('--require-public',action='store_true');a=ap.parse_args()
def load(p):return json.loads(p.read_text())
def rows(p,k):
    x=load(p);return x[k] if isinstance(x,dict) else x
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def objsha(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
def resolve(cap):
    root=B if cap['root']=='artifact' else Q
    p=(root/cap['path']).resolve(); assert p.is_relative_to(root.resolve()),p
    if not p.is_file() and not a.require_public and cap['root']=='artifact' and cap['path'].startswith('final-correction-v1/'):
        p=S/cap['path'].removeprefix('final-correction-v1/')
    assert p.is_file(),p
    assert sha(p)==cap['sha256'],p
    return p

out=O/a.output;assert not out.exists()
receipt=dict(reviewer='/root/final_skeptical',at=datetime.now(timezone.utc).isoformat(),scope='Independent exact assembly, accounting and attribution inspection; chemical applicability comes from separately attributed scientific reviews.',core=str(a.core),errors=[])
try:
    ds=rows(a.core/'decisions.json','decisions');ps=rows(a.core/'proposals.json','proposals');es=rows(a.core/'evidence.json','evidence')
    oldds=rows(N/'decisions.json','decisions');oldps=rows(N/'proposals.json','proposals');oldes=rows(N/'evidence.json','evidence')
    sd={x['case_id']:x for x in load(Q/'shards/shard-05.json')['cases']};od={x['case_id']:x for x in oldds};op={x['proposal_id']:x for x in oldps};oe={x['evidence_id']:x for x in oldes}
    dd={x['case_id']:x for x in ds};pp={x['proposal_id']:x for x in ps};ee={x['evidence_id']:x for x in es}
    assert len(dd)==len(ds) and set(dd)==set(sd)==set(od)
    assert len(pp)==len(ps) and len(ee)==len(es)
    assert set(oe)<=set(ee)
    assert sha(Q/'shards/shard-05.json')=='457c957af21271b120190093dd311bf4044b82a3ad26b54e2fc5b52083dec1c4'
    assignments={lane:load(S/f'control/{lane}-assignment.json') for lane in ['chemicals','materials','media']}
    case_lane={};finding_ids=[]
    for lane,r in assignments.items():
        for cid in r['case_ids']:assert cid not in case_lane;case_lane[cid]=lane
        finding_ids+=r['finding_ids']
    assert set(case_lane)==set(dd) and len(finding_ids)==len(set(finding_ids))
    fragment_cache={};case_checks=[]
    for d in ds:
        cid=d['case_id'];raw=sd[cid];prior=od[cid];prov=d['final_assembly_provenance']
        assert d['case_input_sha256']==objsha(raw)
        assert d['source']=={k:raw[k] for k in ['source','source_case_id','source_label','raw_source_label']}
        assert d['occurrence_ids']==[x['occurrence_id'] for x in raw.get('occurrences',[])]
        assert prov['primary_lane']==case_lane[cid] and prov['compiler']=='/root'
        fp=W/prov['selected_fragment_path'];assert sha(fp)==prov['selected_fragment_sha256']
        if fp not in fragment_cache:fragment_cache[fp]={x['case_id']:x for x in rows(fp,'decisions')}
        fd=fragment_cache[fp][cid]
        assert objsha(fd)==prov['selected_decision_object_sha256']
        assert objsha(prior)==prov['predecessor_decision_object_sha256']
        # Canonical compilation may add evidence/reviewer bindings and assembly provenance only.
        remove={'final_assembly_provenance','independent_review','evidence_ids'}
        assert {k:v for k,v in d.items() if k not in remove}=={k:v for k,v in fd.items() if k not in remove}
        assert set(fd['evidence_ids'])<=set(d['evidence_ids'])
        assert all(i in ee for i in d['evidence_ids']) and all(i in pp for i in d['proposal_ids'])
        oh=prior.get('preserved_source_holds',{});nh=d.get('preserved_source_holds',{})
        assert {k:v for k,v in oh.items() if k!='policy'}=={k:v for k,v in nh.items() if k!='policy'}
        assert prior.get('preserved_downstream_holds')==d.get('preserved_downstream_holds')
        assert prov['source_hold_policy_wording']['before']==oh.get('policy')
        assert prov['source_hold_policy_wording']['after']==nh.get('policy')
        case_checks.append(dict(case_id=cid,lane=case_lane[cid],source_case_sha256=objsha(raw),canonical_decision_sha256=objsha(d),reviewed_fragment_sha256=objsha(fd),occurrence_ids=d['occurrence_ids'],source_hold_policy_changed=oh.get('policy')!=nh.get('policy'),substantive_source_holds_unchanged=True,proposal_ids=d['proposal_ids']))
    line=rows(a.core/'proposal-lineage.json','rows');lm={x['proposal_id']:x for x in line};assert set(lm)==set(pp)
    covered=[];payloads=[];new_records={};old_records={};owners=set()
    for p in ps:
        pid=p['proposal_id'];assert p['owner_path'] not in owners;owners.add(p['owner_path'])
        assert all(c in dd and pid in dd[c]['proposal_ids'] for c in p['case_ids'])
        assert all(e in ee for e in p['evidence_ids'])
        path=resolve(p['after_capture']);new=yaml.safe_load(path.read_text());new_records[pid]=new;lin=lm[pid]
        assert lin['successor_after_capture']==p['after_capture'] and lin['owner_path']==p['owner_path']
        oldid=lin['predecessor_proposal_id'];fields=[]
        if oldid:
            covered.append(oldid);prior=op[oldid];before=yaml.safe_load(resolve(prior['after_capture']).read_text());old_records[oldid]=before
            assert prior['owner_path']==p['owner_path'] and prior['before_sha256']==p['before_sha256']
            assert lin['predecessor_proposal_sha256']==objsha(prior)
            assert lin['predecessor_after_capture']==prior['after_capture']
            assert new.get('curation_history',[])[:len(before.get('curation_history',[]))]==before.get('curation_history',[])
            assert all(s in new.get('synonyms',[]) for s in before.get('synonyms',[]) if s.get('synonym_type')=='REJECTED_LABEL')
            fields=[k for k in set(before)|set(new) if 'occurrence' in k or k in ['roles','organism_roles','causal_graphs']]
            assert all(before.get(k)==new.get(k) for k in fields)
        else:assert p['kind']=='edit_existing_owner' and p['before_sha256']
        if p['before_sha256']:assert sha(W/p['owner_path'])==p['before_sha256']
        payloads.append(dict(proposal_id=pid,predecessor=oldid,owner_path=p['owner_path'],case_ids=p['case_ids'],selected_capture=p['after_capture'],inherited_history_and_negatives_preserved=True,preserved_role_count_graph_fields=fields))
    assert len(covered)==len(set(covered))==len(op) and set(covered)==set(op)
    old_to_new={x['predecessor_proposal_id']:x['proposal_id'] for x in line if x['predecessor_proposal_id']}
    type_rows=rows(S/'control/w05-provenance-suggestions.json','rows');types=[]
    for suggestion in type_rows:
        oldid=suggestion['proposal_id'];pid=old_to_new[oldid];i=int(suggestion['field'].split('[')[1].split(']')[0])
        before=old_records[oldid]['ontology_mapping']['evidence'][i];after=new_records[pid]['ontology_mapping']['evidence'][i]
        assert objsha(before)==suggestion['full_value_sha256']
        assert after['evidence_type']==suggestion['suggested_native_type']
        types.append(dict(audit_row_id=suggestion['audit_row_id'],proposal_id=pid,field=suggestion['field'],before_sha256=objsha(before),after_sha256=objsha(after),type=after['evidence_type']))
    caps=[];changes=[]
    for e in es:
        ep=resolve(e['capture']);caps.append(dict(evidence_id=e['evidence_id'],capture=e['capture'],resolved_path=str(ep),original_accessed_at=e.get('accessed_at')))
        if e['evidence_id'] in oe:
            before=oe[e['evidence_id']]
            for k in ['capture','accessed_at','url']:assert before.get(k)==e.get(k),(e['evidence_id'],k)
            if before!=e:changes.append(dict(evidence_id=e['evidence_id'],changed_fields=[k for k in set(before)|set(e) if before.get(k)!=e.get(k)]))
    assert {r['evidence_id'] for r in changes}=={'MATERIALS-C1193-JCM117','M1193-WEB-web-more-2-131','M1193-FOLLOWON-153'}
    receipt.update(status='PASS',canonical_hashes={n:sha(a.core/n) for n in ['decisions.json','proposals.json','evidence.json','proposal-lineage.json','assembly-receipt.json']},counts=dict(cases=len(ds),proposals=len(ps),original_proposals=len(covered),additional_existing_owner_followons=len(ps)-len(covered),evidence=len(es),occurrences=sum(len(d['occurrence_ids']) for d in ds),mapping_types=dict(collections.Counter(x['type'] for x in types))),case_checks=case_checks,payload_checks=payloads,all_evidence_hash_checks=caps,mapping_evidence_checks=types,changed_old_evidence_metadata=changes,original_finding_ids=sorted(finding_ids),selected_fragment_hashes=[dict(path=str(p),sha256=sha(p)) for p in fragment_cache],limitations=['PASS is exact mechanical assembly, not a new independent chemical review.','Native final review and final canonical reviewer linkage remain separately checked.','No source case, owner application, export admission or conditional owner selection is granted.'])
except Exception:
    receipt['status']='FAIL';receipt['errors'].append(traceback.format_exc())
out.write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({k:receipt.get(k) for k in ['status','counts','errors']},indent=2))
raise SystemExit(receipt['status']!='PASS')
