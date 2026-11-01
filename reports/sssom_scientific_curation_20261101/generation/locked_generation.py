from pathlib import Path
import os, subprocess, sys
from plugins.repository_settings import RepositorySettings
from plugins.lock_manager import LockManager

RUN = Path(__file__).resolve().parent
phase = sys.argv[1] if len(sys.argv) > 1 else 'baseline'
if phase not in {'baseline', 'final', 'ready'}:
    raise SystemExit('expected baseline, final (blocked proposal), or ready (safe scope)')
output = RUN/'mim/output/sssom-scientific-audit'/f'{phase}.sssom.tsv'
if output.exists():
    raise SystemExit(f'Refusing to overwrite {output}')
target = RepositorySettings.from_environment().get_target('mediaingredientmech')
with target.open() as repository:
    assert target.path.resolve() == (RUN/'mim').resolve()
    assert repository.working_tree_dir == str(RUN/'mim')
with LockManager({'my_id':'codex-scientific-audit'}).lock('mediaingredientmech', 'Generate diagnostic SSSOM candidate'):
    result = subprocess.run([
        sys.executable, str(RUN/'claw/scripts/build_mim_ingredient_sssom.py'),
        '--output', str(output),
        '--prior-stamps-from', str(RUN/'mim/mappings/ingredient_mappings.sssom.tsv'),
    ], env=dict(os.environ))
raise SystemExit(result.returncode)
