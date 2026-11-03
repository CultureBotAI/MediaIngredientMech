from pathlib import Path
import datetime
import hashlib
import json
import os
import subprocess
import sys
from plugins.repository_settings import RepositorySettings
from plugins.lock_manager import LockManager

HERE = Path(__file__).resolve().parent
RUN = HERE.parent
MIM = RUN / 'mim'
CLAW = RUN / 'claw'
OUTPUT = MIM / 'output/sssom-followup-684-686/ingredient_mappings.sssom.tsv'
GENERATOR = CLAW / 'scripts/build_mim_ingredient_sssom.py'
assert not OUTPUT.exists(), 'New candidate output must not overwrite prior artifacts'
target = RepositorySettings.from_environment().get_target('mediaingredientmech')
with target.open() as repository:
    assert target.path.resolve() == MIM.resolve()
    assert repository.working_tree_dir == str(MIM)
head = subprocess.check_output(['git', '-C', str(CLAW), 'rev-parse', 'HEAD'], text=True).strip()
assert head == '9294730aeb19d269899177678db87406f4251555', head
record = {
    'started_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'generator_head': head,
    'generator_path': str(GENERATOR),
    'generator_sha256': hashlib.sha256(GENERATOR.read_bytes()).hexdigest(),
    'mim_head': subprocess.check_output(['git', '-C', str(MIM), 'rev-parse', 'HEAD'], text=True).strip(),
    'output_path': str(OUTPUT),
    'source_baseline': {'path': str(HERE / 'source-baseline.json'), 'sha256': hashlib.sha256((HERE / 'source-baseline.json').read_bytes()).hexdigest()},
    'argv': [sys.executable, str(GENERATOR), '--output', str(OUTPUT),
             '--prior-stamps-from', str(MIM / 'mappings/ingredient_mappings.sssom.tsv')],
    'scope': 'Unmodified native builder under RepositorySettings verified target and LockManager. Fresh output only; canonical mapping and previous candidate remain unchanged. CultureMech outputs are comparison inputs only.',
}
(HERE / 'generation-start.json').write_text(json.dumps(record, indent=2) + '\n')
with LockManager({'my_id': 'codex-sssom-followup-684-686'}).lock('mediaingredientmech', 'Generate follow-up diagnostic SSSOM candidate'):
    result = subprocess.run(record['argv'], env=dict(os.environ))
record.update(finished_at=datetime.datetime.now(datetime.timezone.utc).isoformat(), exit_code=result.returncode,
              generator_sha256_after=hashlib.sha256(GENERATOR.read_bytes()).hexdigest())
if OUTPUT.exists():
    record.update(output_sha256=hashlib.sha256(OUTPUT.read_bytes()).hexdigest(), output_bytes=OUTPUT.stat().st_size)
(HERE / 'generation-result.json').write_text(json.dumps(record, indent=2) + '\n')
raise SystemExit(result.returncode)
