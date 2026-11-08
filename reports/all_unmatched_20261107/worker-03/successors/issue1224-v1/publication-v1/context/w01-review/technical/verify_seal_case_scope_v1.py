import hashlib
import json
import os
from pathlib import Path

P=Path(__file__).resolve().parent
C=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107')
D=C/'integration/final-same-target-reconciliation-v2'
A=C/'assignments/w01-nine-scope-candidates-independent-v1.json'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(Path(p).read_text())
def bind(p):return {'path':str(Path(p).resolve()),'sha256':sha(p)}
def save(n,v):
    with (P/n).open('x') as f:json.dump(v,f,ensure_ascii=False,indent=2);f.write('\n')
assert sha(D/'HANDOFF.json')=='fb4cb8972c815667e925b056cdb7797d1635b291a9fb3ba936061bdcfa3dac96'
assert sha(D/'MANIFEST.json')=='6c89863e292bf1b4333be602bf4a355c0219766456d16e1f574bb5412d956df9'
manifest=read(D/'MANIFEST.json');handoff=read(D/'HANDOFF.json')
files={};links=[]
for root,dirs,names in os.walk(D,followlinks=False):
    for n in dirs+names:
        p=Path(root)/n
        if p.is_symlink():links.append(str(p.relative_to(D)))
    for n in names:
        p=Path(root)/n
        if p.is_file() and not p.is_symlink():files[str(p.relative_to(D))]={'sha256':sha(p),'size':p.stat().st_size}
assert not links
excluded=set(manifest['excluded_runtime_cache_files'])
assert set(files)==set(manifest['files'])|excluded|{'MANIFEST.json','HANDOFF.json'}
assert all(files[k]==v for k,v in manifest['files'].items())
assert len(manifest['files'])==393
assert all(k.startswith('private-black-cache/') and k.endswith('.pickle') for k in excluded)
assert not [x for x in files if x.startswith('publication-v2/')]
assert handoff['active_summary']['sha256']==sha(D/'publication-v4/candidate-summary-v4.json')
assert handoff['manifest']['sha256']==sha(D/'MANIFEST.json')
save('independent-author-seal-v1.json',{'handoff':bind(D/'HANDOFF.json'),'manifest':bind(D/'MANIFEST.json'),'active_summary':bind(D/'publication-v4/candidate-summary-v4.json'),'ignored_inclusive_method':'os.walk entire author packet, followlinks=False; every regular-file byte hashed, every symlink recorded. No gitignore filters.','manifest_members':len(manifest['files']),'all_regular_files':len(files),'exact_manifest_matches':True,'symlinks':links,'excluded_runtime_cache_files':sorted(excluded),'excluded_caches_not_review_evidence':True,'interrupted_publication_regular_files':0,'retained_failures':[bind(D/n) for n in ['publication-v2-interruption-v1.json','build-v2.stderr','pytest-v1.log','test_successor_contract_attempt1.py','format-metadata-v1.log','ruff-packet-final-v1.log']],'failure_limits':'SIGINT and KeyboardInterrupt are in retained bytes. Numeric exit130 was parent-reported; no literal numeric exit-status receipt was located in the sealed packet. Initial test failure concerned superseded versus supersedes wording; original test/source/log retained. UV cache permission failure is not hidden.'})

a=read(A);case_by_id={};case_files={}
for path in sorted((C/'queue/preliminary-v5/shards').glob('shard-*.json')):
    data=read(path)
    for c in data['cases']:
        case_by_id[c['case_id']]=c;case_files[c['case_id']]=path
rows=[];origins=set();case_ids=set();occurrence_ids=set();refs=0
for t in a['candidates']:
    grouped=[]
    for o in t['origins']:
        origins.add(o['entry_id'])
        for b in o['case_bindings']:
            refs+=1;cid=b['case_id'];case_ids.add(cid);case=case_by_id[cid]
            digest=hashlib.sha256(json.dumps(case,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
            assert digest==b['input_sha256'],(cid,digest,b['input_sha256'])
            actual={x['occurrence_id']:x for x in case.get('occurrences',[])}
            assert set(actual)==set(b['occurrence_ids']),(cid,'occurrence mismatch')
            occurrence_ids.update(actual)
            grouped.append({'origin':o['entry_id'],'case_id':cid,'complete_original_case_digest':digest,'case_file':bind(case_files[cid]),'source':{k:case.get(k) for k in ['source','source_case_id','source_label','raw_source_label']},'original_KG_count_definition':case.get('original_kg_entry',{}).get('occurrences_definition'),'original_KG_source_record':case.get('original_kg_entry',{}).get('source_record'),'case_binding':b,'occurrences':[{'occurrence_id':v['occurrence_id'],'recipe_id':v['recipe_id'],'component_path':v['component_path'],'raw_source_label':v.get('raw_preferred_term'),'full_recipe_snapshot':v['full_recipe_snapshot'],'raw_component':v['raw_component']} for v in actual.values()]})
    rows.append({'candidate_id':t['candidate_id'],'operation':t['operation'],'case_ids':t['case_ids'],'occurrence_ids':t['occurrence_ids'],'original_bindings':grouped,'applicability_note':'Trace membership is provenance coverage, not automatic candidate routing. TARGET-032 keeps the W03 Oxoid case as historical author/source lineage; NEW-OXOID scopes the catalog-qualified case. The three DEP rows share a triggering source case and add no new source observations.'})
save('raw-source-case-occurrence-bindings-v1.json',{'assignment':bind(A),'candidate_rows':len(rows),'distinct_origin_entry_ids':len(origins),'distinct_source_case_ids':len(case_ids),'distinct_CM_occurrence_ids':len(occurrence_ids),'origin_case_reference_rows':refs,'counts_not_additive':'The same case/occurrence may appear under both source authors or dependency candidates. KG helper constants are not recipe frequency.','entries':rows})
print(json.dumps({'seal_members':len(manifest['files']),'all_files':len(files),'candidates':len(rows),'distinct_origins':len(origins),'distinct_cases':len(case_ids),'distinct_CM_occurrences':len(occurrence_ids),'case_refs':refs,'seal':bind(P/'independent-author-seal-v1.json'),'coverage':bind(P/'raw-source-case-occurrence-bindings-v1.json')}))
