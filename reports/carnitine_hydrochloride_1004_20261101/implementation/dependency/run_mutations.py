"""Fresh-process negative controls; only isolated copies are changed."""
from pathlib import Path
import ast,datetime,hashlib,json,os,shutil,subprocess,sys
ROOT=Path.cwd();OUT=ROOT/'output/issue1004-dependency-tests/mutations';OUT.mkdir(exist_ok=False)
helper='src/mediaingredientmech/utils/culturemech_occurrences.py'
builder='reports/semantic_review_20260921/resolution/build_review.py'
assembler='reports/sssom_completion_20260921/assemble_review.py'
controls=[
 ('remove_salt_routing',helper,'routing','tests/test_carnitine_occurrence_routing.py','reviewed_source_labels or historical_slice or future_membership'),
 ('broaden_old_id_group',helper,'broad','tests/test_carnitine_occurrence_routing.py','other_source_routes'),
 ('count_rejected_tombstone',helper,'tombstone_count','tests/test_carnitine_occurrence_routing.py','future_membership'),
 ('allow_changed_owner_approval',builder,'owner_hash','tests/test_carnitine_merge_dependencies.py','all_68_nonmapping'),
 ('allow_mapping_approval_carry',assembler,'mapping_carry','tests/test_carnitine_merge_dependencies.py','owner_only_receipt'),
 ('skip_explicit_plan_validation',builder,'explicit_plans','tests/test_carnitine_merge_dependencies.py','explicit_plan_guard'),
]
reports=[builder,assembler,'reports/sssom_completion_20260921/mapping_changes/make_receipt.py']
stable=json.loads((OUT.parent/'source-stable.json').read_text())
results=[]
for label,relative,mutation,test,select in controls:
 dest=OUT/label;dest.mkdir()
 shutil.copytree(ROOT/'src',dest/'src',ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
 (dest/'scripts').mkdir()
 for src in (ROOT/'scripts').glob('*.py'):shutil.copyfile(src,dest/'scripts'/src.name)
 shutil.copytree(ROOT/'tests/fixtures/issue1004-before',dest/'tests/fixtures/issue1004-before')
 shutil.copyfile(ROOT/'MAPPING_SEMANTICS.md',dest/'MAPPING_SEMANTICS.md')
 for source in reports:
  target=dest/source;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/source,target)
 target=dest/relative;original=target.read_text();changed=original
 if mutation=='routing':
  for name in ('Carnitine Hydrochloride','Carnitine (Dl) Hydrochloride'):
   needle=f'    _source_label_key("{name}"): "NCIT:C216679",\n';assert needle in changed;changed=changed.replace(needle,'')
 elif mutation=='broad':
  needle='    source_label = _source_label_key(row.get("preferred_term") or "")'
  assert needle in changed;changed=changed.replace(needle,'    if row.get("resolved_identifier") == "kgmicrobe.compound:carnitine_hydrochloride":\n        return "NCIT:C216679"\n'+needle)
 elif mutation=='tombstone_count':
  needle='    if record.get("mapping_status") == "REJECTED":\n        return stored_media, stored_total\n'
  assert needle in changed;changed=changed.replace(needle,'')
 elif mutation=='owner_hash':
  needle='    return bool(name and current_hash and reviewed_hash and current_hash == reviewed_hash)'
  assert needle in changed;changed=changed.replace(needle,'    return bool(name and current_hash and reviewed_hash)')
 elif mutation=='mapping_carry':
  needle='            and refreshes.matches(owner, baseline["record_inputs"].get(owner))\n'
  assert needle in changed;changed=changed.replace(needle,'')
 else:
  module=ast.parse(changed);function=next(n for n in module.body if isinstance(n,ast.FunctionDef) and n.name=='validate_explicit_plans')
  lines=changed.splitlines(keepends=True)
  changed=''.join(lines[:function.lineno])+ '    return None  # isolated guard-removal control\n' + ''.join(lines[function.end_lineno:])
 assert original!=changed;target.write_text(changed);ast.parse(changed)
 env=dict(os.environ,MIM_DEPENDENCY_TEST_SOURCE_ROOT=str(dest),PYTHONPYCACHEPREFIX=str(dest/'fresh-bytecode'),
          PYTHONPATH=str(dest/'src')+os.pathsep+os.environ.get('PYTHONPATH',''))
 argv=[sys.executable,'-m','pytest','-q','--no-cov',test,'-k',select]
 started=datetime.datetime.now(datetime.timezone.utc).isoformat()
 proc=subprocess.run(argv,cwd=ROOT,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
 log=dest/'pytest.log';log.write_text(proc.stdout)
 killed=proc.returncode==1 and ' failed' in proc.stdout and 'ERROR collecting' not in proc.stdout and 'ERROR at setup' not in proc.stdout
 result={'name':label,'source':relative,'source_sha256':hashlib.sha256(original.encode()).hexdigest(),
         'mutation_sha256':hashlib.sha256(changed.encode()).hexdigest(),'argv':argv,'started_at':started,
         'exit_code':proc.returncode,'killed':killed,'log_sha256':hashlib.sha256(log.read_bytes()).hexdigest(),
         'summary':proc.stdout.splitlines()[-1]}
 results.append(result);print(label,result['summary'],'KILLED' if killed else 'NOT KILLED',flush=True)
unchanged={path:hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest for path,digest in stable['owned_files'].items()}
(OUT/'receipt.json').write_text(json.dumps({'controls':results,'owned_source_unchanged':unchanged},indent=2)+'\n')
assert all(r['killed'] for r in results)
assert all(unchanged.values())
