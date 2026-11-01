from pathlib import Path
import importlib.util,json,shutil,tempfile,hashlib
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent/'step3-mim'
spec=importlib.util.spec_from_file_location('probe_carnitine',ROOT/'scripts/merge_carnitine_hydrochloride.py');w=importlib.util.module_from_spec(spec);spec.loader.exec_module(w)
with tempfile.TemporaryDirectory(prefix='mim-1004-noop-receipt-') as directory:
 r=Path(directory)
 for p in w.BEFORE:
  target=r/p;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(w.frozen_bytes(p))
 evidence=r/w.EVIDENCE;shutil.copytree(ROOT/w.EVIDENCE,evidence)
 log=r/'receipts/apply.json'
 w.apply_sources(r,evidence,log,apply=True)
 original=json.loads(log.read_text())
 revised=w.propose_sources({p:w.frozen_bytes(p) for p in w.OWNERS},w.frozen_bytes(w.LEDGER),w.frozen_bytes(w.MEMBERSHIP),timestamp='2026-11-02T00:00:00+00:00')
 for p in w.OWNERS:(r/p).write_bytes(revised[p])
 outcome=w.apply_sources(r,evidence,log,apply=True)
 result={'producer_sha256':hashlib.sha256((ROOT/'scripts/merge_carnitine_hydrochloride.py').read_bytes()).hexdigest(),'prior_receipt_timestamp':original['timestamp'],'substituted_timestamp':'2026-11-02T00:00:00+00:00','current_owners_match_actual_receipt':all(original['output_sha256'][str(p)]==w.digest((r/p).read_bytes()) for p in w.OWNERS),'result':outcome,'production_changes':False}
 with (HERE/'completed-receipt-binding-probe.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
 print(json.dumps(result,indent=2))
