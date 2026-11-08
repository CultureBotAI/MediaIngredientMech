import hashlib
import importlib.util
import json
import sys
from pathlib import Path

import yaml

P=Path(__file__).resolve().parent
C=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107')
M=C/'integration/worktree'
D=C/'integration/final-same-target-reconciliation-v2'
PRODUCER=C.parent/'kgm-unmapped-20261107/claw/scripts/build_mim_ingredient_sssom.py'
sys.path.insert(0,str(M/'src'))
from mediaingredientmech.synonym_policy import is_resolving_synonym
from mediaingredientmech.export.reviewed_sssom import _safe_synonyms
def bind(p):return {'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
spec=importlib.util.spec_from_file_location('technical_native_sssom_probe',PRODUCER)
module=importlib.util.module_from_spec(spec);sys.modules[spec.name]=module;spec.loader.exec_module(module)
f=D/'publication-v4/candidates/TARGET-024/Soy_Peptone.yaml'
r=yaml.safe_load(f.read_bytes())
reject={'Phytone peptone','Phytone peptone (BD-BBL)','Soytone (BD-Difco) or Phytone peptone (BD-BBL)'}
checks=[]
for syn in r['synonyms']:
    if syn['synonym_text'] not in reject|{'Soybean peptone'}:continue
    positive=syn['synonym_text']=='Soybean peptone'
    resolves=is_resolving_synonym(syn);publishable=module._is_publishable_mim_synonym(syn)
    assert resolves==publishable==positive
    error=None
    try:_safe_synonyms({'subject_id':'MIM:Soy_Peptone','other':syn['synonym_text']},r)
    except ValueError as e:error=str(e)
    assert (error is None)==positive
    checks.append({'synonym':syn,'native_resolves':resolves,'native_producer_publishable':publishable,'supported_export_gate_error':error,'control':'known exact positive synonym' if positive else 'specified rejected product claim'})
rows=module._row_from_yaml(Path('Soy_Peptone.yaml'),{},{},{},{},record=r,owners={})
tokens={t for row in rows for t in row.get('other','').split('|') if t}
assert not reject.intersection(tokens)
# The fallback registry row need not carry every otherwise permissible alias;
# the positive policy/gate control above separately proves it is not all-reject.
result={'candidate':bind(f),'native_producer':bind(PRODUCER),'native_policy':bind(M/'src/mediaingredientmech/synonym_policy.py'),'native_supported_export_gate':bind(M/'src/mediaingredientmech/export/reviewed_sssom.py'),'checks':checks,'actual_in_memory_rows':rows,'rejected_tokens_absent':True,'method':'Import actual pinned native functions; call with complete exact candidate in memory and empty ancillary maps. No producer main, canonical output or file mutation.','limitations':'Other inherited Soytone/Bacto/peptic-soy resolving tokens are unchanged and remain subject to their separate source holds; this technical check gives them no scientific approval. No complete campaign alias or release admission is established.'}
with (P/'soy-native-alias-probe-v1.json').open('x') as out:json.dump(result,out,indent=2,ensure_ascii=False);out.write('\n')
print(json.dumps({'checks':len(checks),'rows':len(rows),'receipt':bind(P/'soy-native-alias-probe-v1.json')}))
