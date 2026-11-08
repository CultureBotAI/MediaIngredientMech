"""Strict issue1203 binding, native closed schema and full-catalogue partonomy.

2026-11-08. Read-only on all maintained/source inputs. Output a new receipt.
Negative controls exercise lost occurrences, raw-source drift, wrong stock routing,
concentration drift and fabricated solvent; no validator can establish science.
"""
import argparse, copy, dataclasses, datetime, hashlib, json, subprocess
from collections import defaultdict
from pathlib import Path
import yaml
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
from mediaingredientmech.validation.write_validated import validate_ingredient
R=Path('reports/all_unmatched_20261107/worker-07');S=R/'successors/issue1203-v1'
Q=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
CM='CM_NAME:9dd78dd62f6762ad602b4126b067042b0cc68ba65bd212f9a10b07ec20b33e8e'
KG='KG_CASE:ac6686c0d61be7f652dcf0c2a495b463e1adf24fee613329fd02707bd19d759d'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
canonical=lambda v:json.dumps(v,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()

def strict_rows(case,rows,payloads):
    assert len(rows)==len(case['occurrences'])==17
    assert len({r['occurrence_id'] for r in rows})==17
    expected={r['occurrence_id']:r for r in case['occurrences']}
    groups=defaultdict(list)
    for row in rows:
        original=expected[row['occurrence_id']]
        assert all(row[k]==v for k,v in original.items()),'frozen field drift'
        strength=(row['stock_concentration'] or {}).get('value')
        expected_strength={'1592':'7.5','1593':'7.5','1593a':'7.5','1673':'350','1677':'350','1678':'350','1818':None,'1845':None,'1897':None}[row['primary_medium']]
        assert strength==expected_strength
        groups[strength].append(row['occurrence_id'])
        assert row['solute_identity']['identifier']=='CHEBI:31795'
        if strength:
            p=payloads[strength]
            assert row['resolved_material_identifier']==p['identifier']
            assert p['identifier'].startswith('kgmicrobe.ingredient:')
            assert p['ontology_mapping']['ontology_id']==p['identifier']
            assert p['ingredient_type']=='STOCK_SOLUTION'
            assert p['components']==[dict(p['components'][0])], 'unexpected inferred component'
            part=p['components'][0]
            assert part['component_id']=='CHEBI:31795' and part['reference_scope']=='MIM_CATALOG'
            assert part['concentration_value']==strength and part['concentration_unit']=='G_PER_L'
            assert p['component_assertion']['completeness']=='UNKNOWN'
            assert all(s['synonym_text']!='Mg(SO4) x 7 H2O' for s in p.get('synonyms',[]))
        else:
            assert row['resolved_material_identifier']=='CHEBI:31795' and row['proposal_ids']==[]
    assert {k:len(v) for k,v in groups.items()}=={None:5,'7.5':6,'350':6}
    return dict(groups)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args()
    dest=S/args.output;assert not dest.exists()
    cases=json.loads((Q/'shards/shard-07.json').read_text())['cases'];case=next(c for c in cases if c['case_id']==CM)
    ds=json.loads((S/'decisions.json').read_text())['decisions'];es=json.loads((S/'evidence.json').read_text())['evidence'];ps=json.loads((S/'proposals.json').read_text())['proposals']
    old={d['case_id']:d for d in json.loads((R/'decisions.json').read_text())['decisions']}
    unchanged=[d['case_id'] for d in ds if d==old[d['case_id']]]
    assert len(unchanged)==186
    assert {d['case_id'] for d in ds if d!=old[d['case_id']]}=={CM,KG}
    cm=next(d for d in ds if d['case_id']==CM)
    assert hashlib.sha256(canonical(case)).hexdigest()==cm['case_input_sha256']
    rows=json.loads((S/'occurrence-dispositions.json').read_text())['occurrences'];assert rows==cm['occurrence_dispositions']
    payloads={v:yaml.safe_load((S/'proposed_owners'/f).read_text()) for v,f in [('7.5','stock-7p5g-L-v2.yaml'),('350','stock-350g-L.yaml')]}
    groups=strict_rows(case,rows,payloads)
    by_e={e['evidence_id']:e for e in es}
    for row in rows:
        assert sha(Q/row['full_recipe_snapshot'])==row['source_file_sha256']
        source=yaml.safe_load((Q/row['full_recipe_snapshot']).read_text())
        for key in row['component_path'].split('/'):source=source[int(key)] if isinstance(source,list) else source[key]
        assert source==row['raw_component']
        for ev in row['primary_evidence']:
            item=by_e[ev['evidence_id']]
            assert all(ev[k]==item[k] for k in ['capture','url','accessed_at','locator'])
            assert sha(R/ev['capture']['path'])==ev['capture']['sha256']
    assert 'B-PROPOSAL-Mgso4_X_7_H2o' not in {p['proposal_id'] for p in ps}
    assert not any(p['owner_path']=='data/ingredients/mapped/Mgso4_X_7_H2o.yaml' for p in ps)
    negative=[]
    for kind in ['duplicate_occurrence','raw_drift','stock_to_solute','wrong_strength','fabricated_solvent']:
        rr=copy.deepcopy(rows);pp=copy.deepcopy(payloads)
        if kind=='duplicate_occurrence':rr[-1]=copy.deepcopy(rr[0])
        elif kind=='raw_drift':rr[0]['raw_component']['concentration']['value']='100'
        elif kind=='stock_to_solute':rr[1]['resolved_material_identifier']='CHEBI:31795'
        elif kind=='wrong_strength':pp['350']['components'][0]['concentration_value']='7.5'
        else:pp['7.5']['components'].append({'component_name':'water','component_id':'CHEBI:15377'})
        try:strict_rows(case,rr,pp)
        except AssertionError:negative.append({'control':kind,'result':'rejected'})
        else:raise AssertionError('Negative control escaped: '+kind)
    catalogue={str(p):yaml.safe_load(p.read_text()) for state in ['mapped','unmapped'] for p in Path('data/ingredients',state).glob('*.yaml')}
    native_owner_errors=[str(e) for e in validate_ingredient(catalogue['data/ingredients/mapped/Mgso4_X_7_H2o.yaml'])]
    baseline_violations={str(v) for v in validate_component_partonomy(catalogue.values())}
    original_ids=defaultdict(list)
    for path,record in catalogue.items():original_ids[record['identifier']].append(path)
    results=[]
    for p in ps:
        f=R/p['after_capture']['path'];assert sha(f)==p['after_capture']['sha256']
        r=yaml.safe_load(f.read_text());before=catalogue.get(p['owner_path'])
        errors=[str(v) for v in validate_ingredient(r)]
        if before is not None:
            assert sha(Path(p['owner_path']))==p['before_sha256']
            history=before.get('curation_history',[])
            assert r.get('curation_history',[])[:len(history)]==history and len(r['curation_history'])>len(history)
        else:assert p['kind']=='new_owner' and p['before_sha256'] is None
        collision=bool(original_ids.get(r['identifier']) and before is None)
        results.append(dict(proposal_id=p['proposal_id'],after_sha256=sha(f),identifier=r['identifier'],schema_errors=errors,introduced_collision=collision))
        catalogue[p['owner_path']]=r
    ids=defaultdict(list)
    for r in results:ids[r['identifier']].append(r['proposal_id'])
    collisions={k:v for k,v in ids.items() if len(v)>1}
    final=validate_component_partonomy(catalogue.values());proposed_ids=set(ids)
    violations=[dataclasses.asdict(v) for v in final if str(v) not in baseline_violations or v.record_id in proposed_ids]
    changes=subprocess.run(['git','diff','--name-status','be2f4c36d3d4ed79aabe29401c555ae3fd65d7b0','--'],capture_output=True,text=True,check=True).stdout.splitlines()
    old_changes=[line for line in changes if not line.startswith('A\t')]
    baseline=json.loads((R/'captures/root-maintained-baseline-hashes.json').read_text())['files']
    drift=[p for p,h in baseline.items() if sha(Path(p))!=h]
    passed=not(native_owner_errors or collisions or violations or old_changes or drift or any(r['schema_errors'] or r['introduced_collision'] for r in results))
    receipt=dict(at=datetime.datetime.now(datetime.timezone.utc).isoformat(),status='PASS' if passed else 'FAIL',method='Exact17 source-field binding and component traversal; native closed schema for100 proposedpayloads and existingpureowner; whole catalogue partonomy with in-memory proposals; published and maintained byte preservation.',scientific_approval=False,input_hashes={n:sha(S/n) for n in ['decisions.json','evidence.json','proposals.json','occurrence-dispositions.json']},unchanged_decision_count=len(unchanged),groups=groups,negative_controls=negative,native_owner_schema_errors=native_owner_errors,proposal_results=results,proposal_id_collisions=collisions,partonomy_violations=violations,published_predecessor_file_changes=old_changes,maintained_baseline_file_count=len(baseline),maintained_drift=drift)
    dest.write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps({k:receipt[k] for k in ['status','unchanged_decision_count','native_owner_schema_errors','partonomy_violations','published_predecessor_file_changes','maintained_drift']}))
    return 0 if passed else 1
if __name__=='__main__':raise SystemExit(main())
