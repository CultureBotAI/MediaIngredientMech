"""Isolated actual pinned producer projection; no canonical generation or publication."""
from pathlib import Path
import json,hashlib,datetime,sys,types,os,yaml,copy,subprocess
R=Path.cwd(); W=R/'reports/all_unmatched_20261107/worker-01';O=W/'shard';V=O/'validation';V.mkdir(exist_ok=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
producer=R.parents[4]/'.temp/kgm-unmapped-20261107/claw/scripts/build_mim_ingredient_sssom.py'
assert sha(producer)=='38d59f42953305f6fc51e4fc24dfc59ee1919bfb961595b67a8afe9f8a46a1bc'
producer_root=producer.parent.parent
producer_revision=subprocess.check_output(['git','-C',str(producer_root),'rev-parse','HEAD'],text=True).strip()
assert producer_revision=='76c1ebeea3fc7f80bf1abe044688f298f390cfac'
assert not subprocess.check_output(['git','-C',str(producer_root),'status','--porcelain','--untracked-files=no'],text=True).strip()
captured=producer.read_bytes();os.environ['MEDIAINGREDIENTMECH_ROOT']=str(R)
mod=types.ModuleType('w01_captured_native_producer');mod.__file__=str(producer);sys.modules[mod.__name__]=mod
exec(compile(captured,str(producer),'exec'),mod.__dict__)
P=json.loads((O/'proposals.json').read_text())['proposals'];results=[];identities={};owner_paths={}
for p in P:
 cap=p.get('after_capture')
 if not cap:continue
 assert cap['root']=='artifact';ap=W/cap['path'];assert sha(ap)==cap['sha256'];r=yaml.safe_load(ap.read_text())
 target=p.get('integration_target_path') or p.get('new_owner_path') or p.get('destination_path') or p['owner_path']
 assert r['identifier'] not in identities,(p['proposal_id'],'duplicate proposed identity',identities.get(r['identifier']))
 assert target.casefold() not in owner_paths,(p['proposal_id'],'duplicate intended owner path',owner_paths.get(target.casefold()))
 identities[r['identifier']]=p['proposal_id'];owner_paths[target.casefold()]=p['proposal_id']
 rows=mod._row_from_yaml(R/target,residual={},kgm_sources={},kgm_labels={},canonical_labels={},record=r,owners={})
 if isinstance(rows,dict):rows=[rows]
 om=r.get('ontology_mapping') or {};oid=om.get('ontology_id');ident=r.get('identifier');grade=om.get('mapping_quality')
 expected='skos:exactMatch' if oid==ident else 'skos:broadMatch' if grade=='NARROW_MATCH' else None
 assert expected is not None,(p['proposal_id'],grade,ident,oid,'Unreviewed grade/identity relationship')
 matches=[x for x in rows if x['object_id']==oid];assert matches and all(x['predicate_id']==expected for x in matches),(p['proposal_id'],rows,expected)
 identity=[x for x in rows if x['object_id']==ident];assert identity and all(x['predicate_id']=='skos:exactMatch' for x in identity),(p['proposal_id'],'missing exact identity',rows)
 if expected=='skos:broadMatch':
  assert any(x['object_id'].startswith(('kgmicrobe.ingredient:','kgmicrobe.compound:')) and x['predicate_id']=='skos:exactMatch' for x in rows),(p['proposal_id'],'missing mandatory exact registry sibling',rows)
 assert len({(x['subject_id'],x['object_id']) for x in rows})==len(rows),(p['proposal_id'],'duplicate subject/object pair',rows)
 assert not any(x['predicate_id']=='skos:closeMatch' for x in rows),(p['proposal_id'],rows)
 rejected={s['synonym_text'] for s in r.get('synonyms',[]) if s.get('synonym_type')=='REJECTED_LABEL'}
 emitted={s for row in rows for s in row.get('other','').split('|') if s}
 assert not (rejected & emitted),(p['proposal_id'],'rejected label emitted',sorted(rejected & emitted))
 results.append({'proposal_id':p['proposal_id'],'payload_path':cap['path'],'payload_sha256':sha(ap),'intended_owner_path':target,'mapping_quality':grade,'expected_ontology_predicate':expected,'rejected_labels_not_emitted':sorted(rejected),'rows':rows,'result':'PASS'})
# Regression: old wrong grade reproduces closeMatch, corrected payload has broadMatch.
old=W/'shard/root_substances/proposed_owners/completeness-Filtered_Tomato_Juice_PH7-after.yaml';r=yaml.safe_load(old.read_text())
bad=mod._row_from_yaml(R/'data/ingredients/mapped/Filtered_Tomato_Juice_PH7.yaml',residual={},kgm_sources={},kgm_labels={},canonical_labels={},record=r,owners={})
assert any(x['object_id']=='MICRO:0000556' and x['predicate_id']=='skos:closeMatch' for x in bad)
assert not any(x['object_id']=='MICRO:0000556' and x['predicate_id']=='skos:broadMatch' for x in bad)
good=next(x for x in results if x['proposal_id']=='RS-COMPLETE-FILTERED_TOMATO_JUICE_PH7')
mod._check_producer_bindings()
binding={str(p.relative_to(producer_root)):hashlib.sha256(b).hexdigest() for p,b in mod._IMPORTED_PRODUCER_BYTES.items()}
out=V/(sys.argv[1] if len(sys.argv)>1 else 'native-generated-predicates-v1.json');assert not out.exists()
out.write_text(json.dumps({'at':datetime.datetime.now(datetime.UTC).isoformat(),'producer_path':str(producer),'producer_revision':producer_revision,'producer_tracked_worktree_clean':True,'producer_sha256':sha(producer),'producer_bound_source_sha256':binding,'method':'Compile captured pinned native producer bytes, invoke actual _row_from_yaml with empty ancillary dictionaries on isolated after payloads and intended owner filenames; no canonical generation/publication.','proposals_input_sha256':sha(O/'proposals.json'),'reviewed_proposal_count':len(results),'checks':results,'regression_1164':{'issue':'https://github.com/CultureBotAI/MediaIngredientMech/issues/1164','old_payload_sha256':sha(old),'old_native_rows':bad,'expected_broad_match_negative_control':'correctly rejected old BROAD_MATCH result','corrected_payload_sha256':good['payload_sha256'],'corrected_expected_parent_and_exact_registry':'PASS'},'result':'PASS'},indent=2)+'\n')
print(out,len(results),'PASS')
