"""Reproduce lost reserved evidence in external fixture copies only."""
from pathlib import Path
from contextlib import contextmanager
import importlib.util,json,sys
import pytest
from kg_microbe_write import ValidatedWriteTransaction
root=Path(sys.argv[1]).resolve();out=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('writer_tests',root/'tests/test_promote_heptahydrate_ncit.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
results=[]
for target in ['receipt','owner_backup','ledger_backup','sssom_backup']:
    fixture=out/('reservation-'+target);fixture.mkdir(exist_ok=False)
    with pytest.MonkeyPatch.context() as patch:
        work,log,before=module.case.__wrapped__(fixture,patch)
        writer=module.writer
        patch.setattr(writer,'new_transaction',lambda root,validator,journal:ValidatedWriteTransaction(root,validator=validator,journal_dir=journal))
        original=writer.reserve_receipt_outputs
        replaced={'receipt':log,'owner_backup':log.with_suffix('.before.yaml'),'ledger_backup':log.with_suffix('.before-ledger.tsv'),'sssom_backup':log.with_suffix('.before.sssom.tsv')}[target]
        @contextmanager
        def race(*args,**kwargs):
            with original(*args,**kwargs) as handles:
                replaced.unlink()
                replaced.write_bytes(b'concurrent replacement evidence\n')
                yield handles
        patch.setattr(writer,'reserve_receipt_outputs',race)
        result=writer.apply_sources(work,log,apply=True)
        record={'target':target,'applied':result['applied'],'changed':result['changed'],
          'owner_changed':(work/writer.OWNER).read_bytes()!=before[writer.OWNER],
          'ledger_changed':(work/writer.LEDGER).read_bytes()!=before[writer.LEDGER],
          'replaced_path':str(replaced),'replacement_preserved':replaced.read_bytes()==b'concurrent replacement evidence\n',
          'receipt_is_reported_complete':json.loads(log.read_text()).get('state')=='complete' if target!='receipt' else False,
          'journal_status':json.loads(Path(result['transaction']['journal']).read_text())['status']}
        assert record['applied'] and record['owner_changed'] and record['ledger_changed']
        assert record['replacement_preserved'] and record['journal_status']=='complete'
        results.append(record)
report={'writer_sha256':module.writer.digest((root/'scripts/promote_heptahydrate_ncit.py').read_bytes()),
  'reservation_helper_sha256':module.writer.digest((root/'src/mediaingredientmech/curate/apply_receipt.py').read_bytes()),
  'native_transaction':str(Path(sys.modules['kg_microbe_write.transaction'].__file__).resolve()),'cases':results}
(out/'reservation-race.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
