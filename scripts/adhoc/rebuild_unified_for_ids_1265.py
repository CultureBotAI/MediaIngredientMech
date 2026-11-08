#!/usr/bin/env python3
"""#1265, 2026-11-08: preview native unified snapshot from pinned local sources.

Run using Claw's environment; --claw identifies its validated control checkout.
Resolve both repositories natively; fetch CultureMech under a short metadata lock,
then archive only normalized YAML into durable MIM staging. No shared checkout
files change. The native builder writes only the proposed .temp output. Publication
and native freshness stamping are separate reviewed steps.
"""
from pathlib import Path
import argparse
import hashlib
import json
import os
import subprocess
import sys

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--claw', type=Path, required=True)
args = parser.parse_args()
claw = args.claw.resolve()
root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(claw))
from plugins.repository_settings import RepositorySettings, merged_repository_environment
from plugins.lock_manager import LockManager
from kg_microbe_fleet import load_fleet_manifest

env = merged_repository_environment(claw / '.env')
settings = RepositorySettings.from_environment(
    config={'repositories': {'mediaingredientmech': str(root)}},
    environ=env, manifest=load_fleet_manifest(),
)
mim = settings.get_target('mediaingredientmech'); mim.open()
cm = settings.get_target('culturemech'); cm.open()
with LockManager().lock('culturemech', 'mim1265_read_source_snapshot'):
    cm.open()
    subprocess.run(['git', 'fetch', '--no-tags', 'origin', 'main'], cwd=cm.path, check=True)
    revision = subprocess.check_output(['git', 'rev-parse', 'FETCH_HEAD'], cwd=cm.path, text=True).strip()
stage = root / '.temp/unified-id-rebuild'
stage.mkdir(parents=True, exist_ok=False)
source = stage / 'culturemech'
source.mkdir()
archive = subprocess.Popen(['git', 'archive', revision, 'data/normalized_yaml'], cwd=cm.path, stdout=subprocess.PIPE)
extraction = subprocess.run(['tar', '-x', '-C', str(source)], stdin=archive.stdout)
archive.stdout.close()
if archive.wait() or extraction.returncode:
    raise SystemExit('Pinned source archive failed')
output = stage / 'UNIFIED_INGREDIENT_MAPPING.tsv'
run_env = dict(os.environ, CULTUREMECH_ROOT=str(cm.path), MEDIAINGREDIENTMECH_ROOT=str(root))
command = [sys.executable, str(claw / 'scripts/build_unified_ingredient_mapping.py'),
           '--culturemech', str(source), '--mim', str(root), '--output', str(output), '--format', 'tsv']
with (stage / 'build.log').open('w') as log:
    result = subprocess.run(command, cwd=claw, env=run_env, stdout=log, stderr=subprocess.STDOUT)
if result.returncode:
    raise SystemExit(result.returncode)
receipt = {
    'issue': 1265, 'culturemech_source': {'repository': 'CultureBotAI/CultureMech', 'commit': revision},
    'claw_commit': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=claw, text=True).strip(),
    'builder_sha256': hashlib.sha256((claw / 'scripts/build_unified_ingredient_mapping.py').read_bytes()).hexdigest(),
    'mim_migration_sha256': hashlib.sha256((root / 'reports/stable_ids_1265_20261108/migration.json').read_bytes()).hexdigest(),
    'before_sha256': hashlib.sha256((root / 'UNIFIED_INGREDIENT_MAPPING.tsv').read_bytes()).hexdigest(),
    'after_sha256': hashlib.sha256(output.read_bytes()).hexdigest(),
    'rows': len(output.read_text().splitlines()) - 1,
    'published': False,
}
(stage / 'rebuild.json').write_text(json.dumps(receipt, indent=2)+'\n')
print(json.dumps(receipt, indent=2))
