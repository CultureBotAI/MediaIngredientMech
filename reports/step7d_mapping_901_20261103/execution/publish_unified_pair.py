"""Publish only the native, fully traced Step7d pair under the user exception."""
from pathlib import Path
import argparse
import csv
import gzip
import hashlib
import io
import json
import subprocess
import sys

D = Path(__file__).resolve().parent
RUN = D.parent
W = RUN / 'step7d'
PAIR = D / 'unified-rebuild-v1/output'
TRACE = D / 'unified-trace-v1'
HEAD = '70b0991a821b7c9c0d4c43924b564384cabc54b9'
BASE = '467aa319a06ef992035f509f66fe251082b44ae1'
PRODUCER = '3022b8738dcc9e01c7464a8d5c95aa9be2eef141'
PLAN = 'a82bc6d32e750f16fc7ecfa4c0a5e172a5930c849d7dc3ec5a6ca106ed60fca4'
NAMES = ('UNIFIED_INGREDIENT_MAPPING.tsv', 'UNIFIED_INGREDIENT_MAPPING.provenance.json')
BEFORE = ('1edaba0f0f2d1afb84129a2ba185963a2cdf3e9b982690fdfd610df1fd78cc88', '172018698861b2161238ca72ad116269e213b72a111a5dbe4a265eb643399bc9')
AFTER = ('f6a8eb844e578d79da9538abf99c244fc25b2c928c50c64c0477b1218092a0f1', '075fcc6ef6eca25c1e63d65889df37d4893be2b1b9d3630df90704012dc2c831')
sys.path[:0] = [str(W), str(W/'src')]
from scripts import apply_owned_name_policy as policy
from scripts import step7a_guarded_publication as native
from scripts import promote_heptahydrate_ncit as guarded
from scripts import check_unified_freshness as freshness
from plugins.lock_manager import LockManager
from plugins.repository_settings import RepositorySettings


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def read(path):
    path = Path(path).absolute()
    require(path == path.resolve(), 'Aliased input: '+str(path))
    return policy.regular(path)


def git(root, *args):
    return subprocess.check_output(['git', *args], cwd=root).decode().strip()


def table(raw):
    stream = io.StringIO(raw.decode(), newline='')
    reader = csv.DictReader(stream, delimiter='\t')
    rows = list(reader)
    require(all(None not in r and None not in r.values() for r in rows), 'Malformed snapshot')
    return reader.fieldnames, rows


def run(trace_hash, log, apply):
    require(RepositorySettings.from_environment().get_target('mediaingredientmech').path.resolve() == W, 'Wrong MIM root')
    require(git(W, 'rev-parse', 'HEAD') == HEAD and not git(W, 'status', '--porcelain', '--untracked-files=all'), 'Clean reviewed checkpoint required')
    require(git(RUN/'step7c-claw', 'rev-parse', 'HEAD') == PRODUCER, 'Producer moved')
    inputs = {}
    def bind(path, expected=None):
        path=Path(path).absolute(); raw=read(path)
        require(expected is None or sha(raw)==expected, 'Pinned input changed: '+str(path))
        inputs[path]=raw
        return raw
    trace_raw=bind(TRACE/'trace-receipt.json',trace_hash);trace=json.loads(trace_raw)
    require(trace['status']=='PASS' and trace['untraced_cells']==0 and trace['changed_cells']==6 and trace['changed_rows']==4, 'Trace is incomplete')
    require(all(trace[k] is True for k in ('after_pair_processed','baseline_native_replay_exact','after_native_replay_exact','native_provenance_verified','all_changed_inputs_accounted_for')), 'Native trace not verified')
    require((trace['base_revision'],trace['mim_checkpoint'],trace['producer_revision'],trace['plan_sha256'],trace['after_tsv_sha256'],trace['after_provenance_sha256'])==(BASE,HEAD,PRODUCER,PLAN,*AFTER), 'Trace bindings differ')
    plan=json.loads(bind(D/'owner-plan.json',PLAN))
    for path in TRACE.iterdir():
        require(path.is_file(), 'Unexpected trace directory member');bind(path)
    inventory=json.loads(gzip.decompress(bind(TRACE/'native-input-inventory.json.gz')))
    for path,info in inventory.items():bind(path,info['sha256'])
    for path,digest in json.loads(bind(TRACE/'executed-code-inputs.json')).items():bind(path,digest)
    for module in (policy,native,guarded,freshness):
        path=Path(module.__file__).resolve();raw=bind(path)
        require(raw==subprocess.check_output(['git','show',BASE+':'+str(path.relative_to(W))],cwd=W),'Native helper changed')
    bind(Path(__file__))
    bind(D/'user-authorization.txt','bd325cc48b99b5e78ac1a9f8e487ac4ff725629352622ab9d8f1097d03e29703')
    bind(D/'user-selector-clarification.txt','2da6cb41d2dc04d5f9571042fd3ad5712114fa200c9a0fe4031563c3f41cbf4f')
    for name,item in plan['owners'].items():bind(W/name,item['after_sha256'])
    old=[bind(W/name,h) for name,h in zip(NAMES,BEFORE,strict=True)]
    new=[bind(PAIR/name,h) for name,h in zip(NAMES,AFTER,strict=True)]
    columns,prior=table(old[0]);fields,after=table(new[0]);require(columns==fields and len(prior)==len(after)==4170,'Snapshot shape changed')
    actual=[]
    for position,(a,b) in enumerate(zip(prior,after,strict=True),1):
        require(all(a[k]==b[k] for k in ('ingredient_name','occurrence_count','mapping_status','example_media')),'Protected snapshot cell changed')
        actual.extend((position,a['ingredient_name'],k,a[k],b[k]) for k in columns if a[k]!=b[k])
    cells=json.loads(inputs[TRACE/'cell-traces.json'])
    require(not cells['untraced_cells'] and len(cells['cells'])==6,'Untraced cell present')
    declared=[(c['row_position'],c['ingredient_name'],c['column'],c['before'],c['after']) for c in cells['cells']]
    require(actual==declared and all(c['status']=='TRACED' and c['owner_path'] in plan['owners'] for c in cells['cells']),'Exact trace cells differ')
    provenance=json.loads(new[1]);digest,count=freshness.inputs_digest(W/'data/ingredients')
    require(provenance['artifact_sha256']==AFTER[0] and provenance['mim_inputs_digest']==digest and provenance['mim_record_count']==count and provenance['mim_rev']==freshness._git_rev(W),'Native sidecar binding differs')
    original_paths=policy.ingredient_paths(W)
    culture=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/CultureMech')
    recipes=culture/'data/normalized_yaml'
    expected_recipes={Path(p) for p in inventory if Path(p).is_relative_to(recipes)}
    def scope():
        require(policy.ingredient_paths(W)==original_paths,'Owner inventory moved')
        require(set(recipes.rglob('*.yaml'))==expected_recipes,'CultureMech input membership moved')
        require(git(culture,'rev-parse','HEAD')=='a74dd489720c9df96cc073ffd11568d407d3c06c','CultureMech revision moved')
        require(git(W,'rev-parse','HEAD')==HEAD,'Reviewed checkpoint moved')
    scope()
    result={'exception':'User-authorized Step7d option(a) native snapshot rebuild only; every other plan step remains prohibited.', 'base_revision':BASE,'mim_checkpoint':HEAD,'producer_revision':PRODUCER,'plan_sha256':PLAN,'trace_receipt_sha256':trace_hash,'changed_cells':6,'changed_rows':4,'untraced_cells':0,'before_sha256':dict(zip(NAMES,BEFORE)),'after_sha256':dict(zip(NAMES,AFTER)),'scientific_approval_added':False,'supervisor_binding':None,'input_sha256':{str(p):sha(b) for p,b in inputs.items()}}
    backups={log.with_name(log.stem+'.before-'+name):raw for name,raw in zip(NAMES,old,strict=True)}
    return native.publish(W,dict(zip(map(Path,NAMES),new)),inputs,log,backups,result,apply=apply,validate_scope=scope)


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--trace-sha256',required=True);parser.add_argument('--log',type=Path,required=True);parser.add_argument('--apply',action='store_true');args=parser.parse_args()
    with LockManager().lock('mediaingredientmech','User-authorized Step7d traced snapshot pair'):
        result=run(args.trace_sha256,args.log,args.apply)
    print(json.dumps({k:v for k,v in result.items() if k!='input_sha256'},indent=2))
