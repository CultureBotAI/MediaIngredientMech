"""Read-only production review: private fixture demonstrates late output alias."""
from pathlib import Path
import datetime, hashlib, importlib.util, json
R=Path(__file__).resolve().parent
W=R.parents[1]/'worktree'
sp=importlib.util.spec_from_file_location('queue_tests',W/'tests/test_reconcile_kgm_chemical_queue.py')
t=importlib.util.module_from_spec(sp); sp.loader.exec_module(t)
m=t.reconciler
F=R/'parent-swap-fixture-v1'; F.mkdir(exist_ok=False)
snapshot,mim,consumed=t.runnable_fixture(F)
upstream=F/'upstream-read-only'; upstream.mkdir()
parent=F/'safe-parent'; parent.mkdir()
output=parent/'new-report'
original_load=m.load_review
triggered=[]
def swapped_load(*args,**kwargs):
    # All initial output guards have run; the replacement happens before the
    # potentially long native review and the final hash rechecks.
    parent.rmdir(); parent.symlink_to(upstream,target_is_directory=True)
    triggered.append(True)
    return original_load(*args,**kwargs)
m.load_review=swapped_load
try:
    summary=m.run(snapshot,mim,Path('review.json'),consumed,output)
    result={'returned_success':True,'candidate_count':summary['candidate_count']}
except Exception as e:
    result={'returned_success':False,'error_type':type(e).__name__,'error':str(e)}
result.update({'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
               'script_sha256':hashlib.sha256((W/'scripts/reconcile_kgm_chemical_queue.py').read_bytes()).hexdigest(),
               'private_fixture':str(F),'swap_after_initial_path_guards':bool(triggered),
               'upstream_written_files': sorted(str(p.relative_to(upstream)) for p in upstream.rglob('*') if p.is_file()),
               'no_real_upstream_or_scientific_inputs_changed':True})
(R/'parent-swap-result-v1.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
