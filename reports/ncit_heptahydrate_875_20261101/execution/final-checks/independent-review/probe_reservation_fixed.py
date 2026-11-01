"""Independent #1029 regression against the real transaction in fresh fixtures."""
from pathlib import Path
from contextlib import contextmanager
import importlib.util,json,sys
import pytest
from kg_microbe_write import ValidatedWriteTransaction
root=Path(sys.argv[1]).resolve();out=Path(__file__).resolve().parent/'reservation-fixed';out.mkdir(exist_ok=False)
spec=importlib.util.spec_from_file_location('writer_tests_fixed',root/'tests/test_promote_heptahydrate_ncit.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
results=[]
for timing in ['reserved','after_commit']:
 for target in ['receipt','owner_backup','ledger_backup','sssom_backup']:
  for symlink in [False,True]:
   fixture=out/(timing+'-'+target+('-symlink' if symlink else '-regular'));fixture.mkdir()
   with pytest.MonkeyPatch.context() as patch:
    work,log,before=module.case.__wrapped__(fixture,patch);writer=module.writer
    replaced={'receipt':log,'owner_backup':log.with_suffix('.before.yaml'),'ledger_backup':log.with_suffix('.before-ledger.tsv'),'sssom_backup':log.with_suffix('.before.sssom.tsv')}[target]
    victim=fixture/'competitor-evidence';victim.write_bytes(b'competitor evidence\n')
    def replace():
     replaced.unlink()
     if symlink:replaced.symlink_to(victim)
     else:replaced.write_bytes(victim.read_bytes())
    original=writer.reserve_receipt_outputs
    @contextmanager
    def race(*args,**kwargs):
     with original(*args,**kwargs) as handles:
      if timing=='reserved':replace()
      yield handles
    class NativeRace(ValidatedWriteTransaction):
     def commit(self,*,apply=False):
      result=super().commit(apply=apply)
      if apply and timing=='after_commit':replace()
      return result
    patch.setattr(writer,'reserve_receipt_outputs',race)
    patch.setattr(writer,'new_transaction',lambda root,validator,journal:NativeRace(root,validator=validator,journal_dir=journal))
    try:writer.apply_sources(work,log,apply=True)
    except ValueError as error:message=str(error)
    else:raise AssertionError('Lost reservation incorrectly reported success')
    assert 'Reserved evidence output' in message
    changed=(work/writer.OWNER).read_bytes()!=before[writer.OWNER]
    assert changed==(timing=='after_commit')
    assert ((work/writer.LEDGER).read_bytes()!=before[writer.LEDGER])==changed
    assert replaced.read_bytes()==victim.read_bytes()==b'competitor evidence\n'
    assert replaced.is_symlink()==symlink
    journals=list((log.parent/(log.stem+'-journal')).glob('*.json'))
    assert len(journals)==int(changed)
    if changed:
     journal=json.loads(journals[0].read_text());assert journal['status']=='complete'
     for p in [writer.OWNER,writer.LEDGER]:assert journal['previous'][str(work/p)].encode()==before[p]
    if target!='receipt':assert json.loads(log.read_text())['state']=='failed'
    results.append({'timing':timing,'target':target,'symlink':symlink,'refused':True,'sources_changed':changed,'competitor_preserved':True,'recovery_journal_preserved':changed,'receipt_failed_if_present':True})
report={'writer_sha256':module.writer.digest((root/'scripts/promote_heptahydrate_ncit.py').read_bytes()),'tests_sha256':module.writer.digest((root/'tests/test_promote_heptahydrate_ncit.py').read_bytes()),'native_transaction':str(Path(sys.modules['kg_microbe_write.transaction'].__file__).resolve()),'cases':results}
(out/'results.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'writer_sha256':report['writer_sha256'],'tests_sha256':report['tests_sha256'],'cases':len(results),'all_refused_without_false_completion':True,'before_commit_no_source_writes':True,'after_commit_journals_preserved':True},indent=2))
