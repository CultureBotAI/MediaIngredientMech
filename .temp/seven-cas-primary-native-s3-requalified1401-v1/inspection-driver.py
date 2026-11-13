"""2026-11-12: inspect seven actual diagnostic CAS claims for primary review.

Inputs are the exact current claims, source endpoint and preserved evidence.
Outputs are a private frozen input map, factual readback and native inspect log.
No owner edits, generation, publication, source replay, tests or Git mutation.
"""
from datetime import datetime, timezone
import argparse
import csv
import hashlib
import io
import json
import os
from pathlib import Path
import re
import subprocess
import yaml

C = Path(__file__).resolve().parents[1]
ROOT = C / 'integration/stable-method-cumulative-source-canary-target'
PY = C / 'integration/stable-campaign-adoption-worktree/.venv/bin/python3'
OUT = ROOT / '.temp/seven-cas-primary-native-s3-requalified1401-v1'
CLAIMS = '.temp/seven-cas-dispositions-claims-s3-requalified1401-v1/CLAIMS.json'
TARGETS = '.temp/seven-cas-dispositions-claims-s3-requalified1401-v1/TARGETS.json'
HEAD = 'eeb586afd00af70997b0f46e76c08e8cfa074665'
parser=argparse.ArgumentParser(description=__doc__)
for name in ['claims','targets','required-inputs','verification-copy','verification-result','verification-stdout','verification-postcheck']:
    parser.add_argument('--'+name+'-sha256',required=True)
args=parser.parse_args()
assert all(re.fullmatch('[0-9a-f]{64}',v) for v in vars(args).values())
sha = lambda raw: hashlib.sha256(raw).hexdigest()
now = lambda: datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
pins = {}
def pin(name, expected=None):
    path = ROOT/name
    assert not Path(name).is_absolute() and '..' not in Path(name).parts
    assert not any(p.is_symlink() for p in (path, *path.parents))
    raw = path.read_bytes()
    digest = sha(raw)
    assert expected is None or digest == expected, name
    assert name not in pins or pins[name] == digest
    pins[name] = digest
    return raw
def doc(name, expected=None):
    return json.loads(pin(name, expected))
assert Path.cwd() == ROOT and not os.path.lexists(OUT)
assert subprocess.check_output(['git','--no-optional-locks','rev-parse','HEAD'],cwd=ROOT).decode().strip() == HEAD
started = now()
claims = doc(CLAIMS, args.claims_sha256)
targets = doc(TARGETS, args.targets_sha256)['targets']
for name,digest in doc('.temp/seven-cas-dispositions-claims-s3-requalified1401-v1/REQUIRED-REVIEW-INPUTS.json',args.required_inputs_sha256).items(): pin(name,digest)
for name,digest in doc('.temp/seven-cas-current-hold-context-v1/REVIEW-INPUTS.json','b90cde1ff8320d41063b36b1870fda147fd7b07d06d3a0ef43198b0eeb2aba8a').items(): pin(name,digest)
doc('.temp/seven-cas-current-hold-context-v1/COPY-RECEIPT.json','23bc856070b1c7cd325af21a498a4e95020a619baa673f364a9cb511cc01453b')
doc('.temp/cumulative-source-successor-committed-verification-s3-requalified1401-v1/COPY-RECEIPT.json',args.verification_copy_sha256)
verify_result = doc('.temp/cumulative-source-successor-committed-verification-s3-requalified1401-v1/RESULT.json',args.verification_result_sha256)
verified = doc('.temp/cumulative-source-successor-committed-verification-s3-requalified1401-v1/stdout.json',args.verification_stdout_sha256)
postcheck=doc('.temp/cumulative-source-successor-committed-verification-s3-requalified1401-v1/POSTCHECK.json',args.verification_postcheck_sha256)
assert verify_result['exit_code'] == 0 and verify_result['head'] == HEAD and verify_result['stdout_sha256'] == args.verification_stdout_sha256
assert postcheck['status'] == 'SOURCE_NATIVE_VERIFIED_AND_PROTECTED_BYTES_UNCHANGED' and postcheck['head'] == HEAD
assert postcheck['result_sha256'] == args.verification_result_sha256 and postcheck['native_stdout_sha256'] == args.verification_stdout_sha256
assert verified['status'] == 'COMPLETE_CURRENT_SOURCE_SUCCESSOR' and verified['current_identity']['head'] == HEAD
endpoint = doc(claims['source_correction']['path'], claims['source_correction']['sha256'])
manifest = doc(endpoint['manifest']['path'], endpoint['manifest']['sha256'])
app = doc(endpoint['receipt']['path'],endpoint['receipt']['sha256'])
assert app['state'] == 'COMPLETE' and app['recovery_required'] is False and app['release_approval_added'] is False
request = doc(manifest['request']['path'],manifest['request']['sha256'])
operations = {op['mim_id']:op for op in request['operations']}
for name,digest in manifest['ledger_sha256'].items():pin(name,digest)
for mid in ['MIM:0000862','MIM:0002227']:
    op=operations[mid]
    for role in ['primary','skeptic']:
        ref=op[role];pin(ref['path'],ref['sha256']);pin(str(Path(ref['path']).with_name('review.md')),ref['markdown_sha256'])
    before=app['beforeimages'][op['before']['path']];pin(before['path'],before['sha256'])
for name in ['AGENTS.md','.claude/skills/map-media-ingredients/SKILL.md','.claude/skills/review-sssom-output/SKILL.md','docs/record-reviews.md','docs/record-review-profile.md','docs/REVIEWED_INVALID_CAS_DIAGNOSTICS.md','src/mediaingredientmech/curate/stable_sssom_publication.py','src/mediaingredientmech/curie.py','src/mediaingredientmech/stable_ids.py']:
    pin(name)
canonical = pin(claims['canonical']['path'],claims['canonical']['sha256']).decode()
rows = list(csv.DictReader(io.StringIO(''.join(line for line in canonical.splitlines(keepends=True) if not line.startswith('#'))),delimiter='\t'))
historic_name=next(name for name in claims['evidence_inputs'] if name.endswith('/INPUTS.json') and claims['evidence_inputs'][name]=='36bd9830ae9fdfdf9b03346df11f4d9360e3595ed1049c4ace3f43623dc6e622')
historical=doc(historic_name)
history={e['mim_id']:e for e in historical['entries']}
assert claims['head']==HEAD and claims['scientific_approval'] is False and claims['scope']=='diagnostic_candidate_only'
assert len(claims['entries'])==len(targets)==7
facts=[]
for entry,target in zip(claims['entries'],targets,strict=True):
    mid=entry['owner']['mim_id'];owner=yaml.safe_load(pin(entry['owner']['path'],entry['owner']['sha256']))
    assert owner['mim_id']==mid and entry['row']==rows[entry['row_position']-1]==history[mid]['row']
    assert history[mid]['inherited_decision']['disposition']=='WITHHOLD'
    assert target['selector']==entry['entry_id'] and target['semantic_digest']['sha256']==sha(json.dumps(entry,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode())
    invalid=[];arithmetic=[]
    for field in ['object_id','other','xref']:
        for token in entry['row'].get(field,'').split('|'):
            if not token.strip().casefold().startswith('cas:'):continue
            rn=token.strip()[4:];assert re.fullmatch(r'[1-9][0-9]{1,6}-[0-9]{2}-[0-9]',rn)
            digits=rn.replace('-','');weighted=sum(i*int(d) for i,d in enumerate(reversed(digits[:-1]),1))
            if weighted%10 != int(digits[-1]):invalid.append({'field':field,'token':token})
            arithmetic.append({'field':field,'literal':token,'weighted_sum':weighted,'expected_digit':weighted%10,'actual_digit':int(digits[-1])})
    assert invalid==entry['invalid_tokens'] and invalid
    current_bytes=pin(entry['owner']['path'])
    assert sha(subprocess.check_output(['git','--no-optional-locks','show',HEAD+':'+entry['owner']['path']],cwd=ROOT))==sha(current_bytes)
    if entry['action']=='RETIRE_INVALID_CAS':
        assert mid in {'MIM:0000862','MIM:0002227'} and entry['hold'] is None
        op=operations[mid];assert op['after_path']==entry['owner']['path'] and manifest['outputs'][op['after_path']]==entry['owner']['sha256']
        assert yaml.safe_load(pin(op['proposal']['path'],op['proposal']['sha256']))==owner
        bad=entry['row']['object_id'];assert bad in op['rejected_identifiers']
        assert bad not in [owner['identifier'],owner['ontology_mapping']['ontology_id'],*owner['legacy_identifiers']]
        assert owner['chemical_properties']['cas_rn'] != bad[4:]
        before_ref=app['beforeimages'][op['before']['path']];before=yaml.safe_load(pin(before_ref['path'],before_ref['sha256']))
        assert before['mim_id']==owner['mim_id'] and owner['curation_history'][:len(before['curation_history'])]==before['curation_history']
        assert op['inherited_holds']==op['residual_holds']
    else:
        assert entry['action']=='RETAIN_INVALID_CAS_WITHHOLD' and mid not in operations
        assert manifest['before_inventory'][entry['owner']['path']]==entry['owner']['sha256']==manifest['after_inventory'][entry['owner']['path']]
        assert history[mid]['owner']['sha256']==entry['owner']['sha256']
        assert entry['hold']['issue'].endswith('/753' if mid=='MIM:0001639' else '/887')
        assert entry['row']['object_id'] in {owner['identifier'],owner['ontology_mapping']['ontology_id']}
    facts.append({'entry_id':entry['entry_id'],'mim_id':mid,'row_position':entry['row_position'],'full_row_exact':True,'current_and_committed_owner_sha256':sha(current_bytes),'permanent_id_preserved':True,'action':entry['action'],'inherited_disposition':'WITHHOLD','arithmetic':arithmetic,'active_owner_withdrawal_verified':entry['action']=='RETIRE_INVALID_CAS','unchanged_predecessor_owner_verified':entry['action']=='RETAIN_INVALID_CAS_WITHHOLD'})
OUT.mkdir()
def save(name,value):
    with (OUT/name).open('x') as stream:json.dump(value,stream,indent=2,ensure_ascii=False);stream.write('\n')
save('FACTS.json',{'at':now(),'kind':'READ_ONLY_TARGET_FACTS_NOT_SCIENTIFIC_APPROVAL','head':HEAD,'canonical_rows':len(rows),'target_count':7,'input_pins_checked':len(pins),'entries':facts,'tests_run':False,'native_source_replay_run':False,'new_scientific_approval':False})
pin((OUT/'FACTS.json').relative_to(ROOT).as_posix())
with (OUT/'inspection-driver.py').open('xb') as stream:stream.write(Path(__file__).read_bytes())
pin((OUT/'inspection-driver.py').relative_to(ROOT).as_posix())
save('INPUTS.json',pins)
argv=[str(PY),'-B','scripts/record_review.py','inspect','--targets',TARGETS]
for name in sorted(pins):argv.extend(['--input',name])
env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','PYTHONPATH':str(ROOT/'src')}
save('INSPECT-COMMAND.json',{'at':started,'argv':argv,'cwd':str(ROOT),'environment_overlay':{'PYTHONDONTWRITEBYTECODE':'1','PYTHONPATH':str(ROOT/'src')},'owner':'/root/s3_completed_source_audit'})
with (OUT/'INSPECT.json').open('xb') as out,(OUT/'INSPECT.stderr.txt').open('xb') as err:
    result=subprocess.run(argv,cwd=ROOT,env=env,stdout=out,stderr=err)
for name,digest in pins.items():assert sha((ROOT/name).read_bytes())==digest,name
save('INSPECT-RESULT.json',{'at':now(),'exit_code':result.returncode,'stdout_sha256':sha((OUT/'INSPECT.json').read_bytes()),'stderr_sha256':sha((OUT/'INSPECT.stderr.txt').read_bytes()),'inputs':len(pins),'claims_sha256':pins[CLAIMS]})
print(json.dumps({'result':str(OUT/'INSPECT-RESULT.json'),'sha256':sha((OUT/'INSPECT-RESULT.json').read_bytes()),'exit_code':result.returncode,'inputs':len(pins)}))
raise SystemExit(result.returncode)
