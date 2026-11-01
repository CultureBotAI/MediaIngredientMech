"""Read-only independent namespace and predicate boundary probes."""
from pathlib import Path
import collections
import contextlib
import datetime
import hashlib
import importlib.util
import io
import itertools
import json
import subprocess
import sys
import types
import yaml

RUN = Path(__file__).resolve().parents[1]
CLAW = RUN/'claw'; MIM = RUN/'mim'; HERE = Path(__file__).resolve().parent
HEAD='9294730aeb19d269899177678db87406f4251555'
BASE='8f837d505b948a25965b0b2a001a4c7691c840fc'
def git(*args): return subprocess.check_output(['git','-C',str(CLAW),*args],text=True).strip()
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec); sys.modules[name]=mod; spec.loader.exec_module(mod)
    return mod
assert git('rev-parse','HEAD')==HEAD
assert not git('status','--porcelain')
sys.path.insert(0,str(CLAW/'scripts'))
new=module('review_registry_new',CLAW/'scripts/build_mim_ingredient_sssom.py')
old=types.ModuleType('review_registry_old'); old.__file__=str(CLAW/'scripts/build_mim_ingredient_sssom.py')
exec(compile(git('show',BASE+':scripts/build_mim_ingredient_sssom.py'),old.__file__,'exec'),old.__dict__)
native=module('review_registry_native',MIM/'scripts/validate_sssom_invariants.py')
fixtures=HERE/'adversarial-registry-fixtures'; fixtures.mkdir(exist_ok=True)
output=io.StringIO(); cases=[]; prior_failures=[]
parents=['CHEBI:17634','FOODON:00001234','ENVO:00001998','mesh:C017721','NCIT:C178908']
qualities=['NARROW_MATCH','CLOSE_MATCH','EXACT_MATCH']
with contextlib.redirect_stdout(output),contextlib.redirect_stderr(output):
    for namespace,stem,kind,parent,quality in itertools.product(
        ['kgmicrobe.ingredient:','kgmicrobe.compound:'],
        ['MES_Buffer','Buffer_(pH7)','Stock-é'],
        ['matching','mixed-case','different'], parents,qualities,
    ):
        subject=new._mim_curie(stem+'.yaml'); slug=subject[4:].lower()
        primary=namespace+{'matching':slug,'mixed-case':subject[4:],'different':'older_independent_slug'}[kind]
        rec={'identifier':primary,'preferred_term':'Prepared subject','mapping_status':'MAPPED',
             'ingredient_type':'STOCK_SOLUTION',
             'ontology_mapping':{'ontology_id':parent,'ontology_label':'Parent label','mapping_quality':quality},
             'curation_history':[{'timestamp':'2026-10-15T12:00:00Z'}],
             'synonyms':[{'synonym_text':'Subject alias','synonym_type':'RAW_TEXT'},
                         {'synonym_text':'Rejected alias','synonym_type':'REJECTED_LABEL'}]}
        p=fixtures/(stem+'.yaml'); p.write_text(yaml.safe_dump(rec))
        args=(p,{}, {},{parent:('Target name',['Target alias','Rejected alias'])},{parent:'Canonical parent'})
        a=old._row_from_yaml(*args); b=new._row_from_yaml(*args)
        assert not list(native.evaluate_rule_b1(b))
        assert not list(native.evaluate_rule_b5(b))
        identities=[r for r in b if r['object_id'].startswith('kgmicrobe.')]
        assert all(r['object_id'].startswith(namespace) and r['predicate_id']=='skos:exactMatch' for r in identities)
        assert any(r['object_id']==primary for r in identities)
        if quality=='NARROW_MATCH': assert any(r['object_id']==namespace+slug for r in identities)
        else: assert len(identities)==1
        parentrow=next(r for r in b if r['object_id']==parent)
        assert 'Subject alias' in parentrow['other'].split('|')
        assert 'Rejected alias' not in parentrow['other'].split('|')
        if quality!='EXACT_MATCH':
            assert 'Target alias' not in parentrow['other'].split('|')
            assert 'Parent label' not in parentrow['other'].split('|')
        if a!=b:
            oldnames={r['object_id'].split(':')[0] for r in a if r['object_id'].startswith('kgmicrobe.')}
            assert quality=='NARROW_MATCH' and len(oldnames)==2
            prior_failures.append({'namespace':namespace,'stem':stem,'kind':kind,'parent':parent,'quality':quality})
        cases.append({'namespace':namespace,'stem':stem,'kind':kind,'parent':parent,'quality':quality,'rows':len(b)})

    # A whole-source pass, with identical empty enrichment inputs, checks that
    # the delta stays inside namespace fixes instead of changing source identity.
    corpus=[]; total=0
    for p in sorted((MIM/'data/ingredients/mapped').glob('*.yaml')):
        a=old._row_from_yaml(p,{}, {}, {}, {}); b=new._row_from_yaml(p,{}, {}, {}, {})
        total+=1
        if a==b: continue
        rec=yaml.safe_load(p.read_text()); primary=rec.get('identifier')
        oldset={r['object_id']:r for r in a}; newset={r['object_id']:r for r in b}
        common=oldset.keys()&newset.keys()
        assert all(oldset[k]==newset[k] for k in common),p
        assert primary.startswith(('kgmicrobe.ingredient:','kgmicrobe.compound:')),p
        assert len(oldset.keys()-newset.keys())==len(newset.keys()-oldset.keys())==1,p
        replacement=newset[next(iter(newset.keys()-oldset.keys()))]
        assert replacement['object_id'].split(':')[0]==primary.split(':')[0]
        assert replacement['predicate_id']=='skos:exactMatch'
        assert not list(native.evaluate_rule_b1(b)) and not list(native.evaluate_rule_b5(b))
        assert newset[primary]['predicate_id']=='skos:exactMatch'
        corpus.append({'record':str(p.relative_to(MIM)),'record_sha256':sha(p),
                       'primary':primary,'removed':sorted(oldset.keys()-newset.keys()),
                       'added':sorted(newset.keys()-oldset.keys())})

assert any('Sodium_Nitrate_070_M_Stock' in d['record'] for d in corpus)
assert git('rev-parse','HEAD')==HEAD and not git('status','--porcelain')
result={'checked_at':datetime.datetime.now(datetime.UTC).isoformat(),'head':HEAD,'base':BASE,
        'builder_sha256':sha(CLAW/'scripts/build_mim_ingredient_sssom.py'),
        'synthetic_count':len(cases),'prior_namespace_failures_resolved':len(prior_failures),
        'synthetic_cases':cases,'native_B1_B5':'pass for every synthetic case and changed real record',
        'real_records_probed':total,'real_changed_records':corpus,
        'limitations':['Whole-source row comparison deliberately uses empty enrichment inputs; complete native regeneration and ontology validation are owned by the parent task.'],
        'findings':[],'source_unchanged':True}
(HERE/'adversarial-registry-result.json').write_text(json.dumps(result,indent=2)+'\n')
(HERE/'adversarial-registry-probe.log').write_text(output.getvalue())
print(json.dumps({k:v for k,v in result.items() if k!='synthetic_cases'},indent=2))
