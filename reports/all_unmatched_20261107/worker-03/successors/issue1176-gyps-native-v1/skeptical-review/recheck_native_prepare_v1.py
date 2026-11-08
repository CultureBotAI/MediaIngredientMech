from pathlib import Path
import json,hashlib,shutil,sys,datetime
R=Path.cwd(); C=R.parents[2]; O=R/'.temp/gyps-native-origin-v1'; S=O/'skeptical-review'; src=O/'technical-review/fixture-v2'; dst=S/'native-recheck-fixture-v1'
assert not dst.exists();shutil.copytree(src,dst,symlinks=True)
sys.path.insert(0,str(C/'integration/worktree/src'))
from mediaingredientmech.curate import campaign_owner_apply as native
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
before=sha(dst/'data/ingredients/mapped/GYPS.yaml')
prepared=native.prepare(dst,dst/'positive/plan.json',dst/'positive/acceptance.json');native._recheck(prepared)
after=sha(dst/'data/ingredients/mapped/GYPS.yaml');assert before==after=='36840ca128760eb0ac542753d24d155fd1ebb6ccd8229be130953a0d01f2cf6e'
assert len(prepared.operations)==1
result={'reviewer':'/root/gyps_native_skeptic','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS_BOUNDED_NATIVE_PREPARE_RECHECK_ONLY','native_calls':['campaign_owner_apply.prepare','campaign_owner_apply._recheck'],'native_apply_called':False,'source_fixture':str(src.relative_to(R)),'private_recheck_fixture':str(dst.relative_to(R)),'fixture_is_real_worker_publication':False,'full_campaign_prepared':False,'operator_sha256':sha(C/'integration/worktree/src/mediaingredientmech/curate/campaign_owner_apply.py'),'reviewed_ledger_sha256':sha(O/'proposals.json'),'native_ledger_sha256':sha(dst/'intake/proposals.json'),'operation_count':len(prepared.operations),'owner_inventory_count':len(prepared.before),'global_case_count':len(json.loads((dst/'intake/global-cases.json').read_bytes())),'prepared_original_origin':prepared.operations[0]['origins'],'payload_sha256':hashlib.sha256(next(iter(prepared.payloads.values()))).hexdigest(),'before_sha256':before,'after_owner_sha256':after,'own_file_input_count':len(prepared.inputs),'meaning':'The exact current prospective ledger bytes pass native constructor in a copied one-owner fixture. Synthetic empty mapping checkpoint and fixture Git head prove bounded contract compatibility, not full campaign or real publication acceptance.'}
assert result['reviewed_ledger_sha256']==result['native_ledger_sha256']=='582ea36dd479b8ecd244d996a6eb772569eb232b1631f87ef5f4aa143a20ce67'
(S/'native-prepare-independent-recheck-v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
