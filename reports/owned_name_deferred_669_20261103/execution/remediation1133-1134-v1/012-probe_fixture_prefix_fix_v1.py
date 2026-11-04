"""Independent private fixture-prefix regression; no maintained writes."""
from pathlib import Path
from copy import deepcopy
import datetime
import hashlib
import importlib.util
import json
import sys
from unittest.mock import patch

W = Path.cwd()
OUT = W.parent / 'next23-execution-20261103/independent-review/fixture-prefix-probes-v1'
assert not OUT.exists()
OUT.mkdir()
TEST = W/'tests/test_owned_name_suppression_refresh.py'
assert hashlib.sha256(TEST.read_bytes()).hexdigest() == 'dcd100dbf2cb3437ff3c5daaddc9e29ac178f8240dafddfc26e7fd6c2e9c3d3f'
spec=importlib.util.spec_from_file_location('independent_fixture_prefix',TEST)
m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m)
original=Path.read_bytes
source=W/m.policy.MANIFEST
actual=original(source)
results=[]
for populated in [False,True]:
    old=m.read_json(actual)
    if not populated: old[m.policy.UPDATE]=[]
    prefix=deepcopy(old[m.policy.UPDATE]); assert bool(prefix)==populated
    raw=m.encoded(old)
    with patch.object(Path,'read_bytes',lambda p: raw if p==source else original(p)):
        case=m.build_case(OUT/('populated' if populated else 'empty'))
    assert m.read_json(case['before'][m.policy.MANIFEST])[m.policy.UPDATE]==prefix
    assert case['manifest'][m.policy.UPDATE][:-1]==prefix
    assert len(case['manifest'][m.policy.UPDATE])==len(prefix)+1
    assert m.verify(case)['scientific_approval_added'] is False
    results.append({'case':'populated-prefix' if populated else 'empty-prefix','outcome':'passed','historical_entries':len(prefix)})
    if populated:
        exact=deepcopy(case['manifest'])
        for mutation in ['delete','alter']:
            case['manifest']=deepcopy(exact)
            if mutation=='delete': del case['manifest'][m.policy.UPDATE][0]
            else: case['manifest'][m.policy.UPDATE][0]['scope']='fabricated history'
            m.repin(case)
            try: m.verify(case)
            except ValueError as error:
                assert 'expected one manifest history append' in str(error)
                results.append({'case':mutation+'-existing-prefix','outcome':'rejected','error':str(error)})
            else: raise AssertionError('altered/deleted history accepted')
assert original(source)==actual
assert hashlib.sha256(original(TEST)).hexdigest()=='dcd100dbf2cb3437ff3c5daaddc9e29ac178f8240dafddfc26e7fd6c2e9c3d3f'
report={'reviewer':'/root/step7d_independent_review','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'issue':'https://github.com/CultureBotAI/MediaIngredientMech/issues/1134','test_sha256':hashlib.sha256(original(TEST)).hexdigest(),'results':results,'maintained_manifest_unchanged':True,'limitations':['Private fixture construction uses a temporary read override only for the source manifest; native verifier and private receipt chain are real.']}
(OUT/'result.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2));print(hashlib.sha256((OUT/'result.json').read_bytes()).hexdigest())
