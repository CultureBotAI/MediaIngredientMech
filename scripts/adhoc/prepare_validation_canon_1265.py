#!/usr/bin/env python3
"""Prepare an isolated exact-pin Claw source for MIM's offline QC (#1265).

2026-11-08. Inputs: MIM's existing governance pin and verified Claw origin.
Output: a detached, clean worktree under ~/agent-work/claw; no branch changes.
Run with Claw's environment and pass its root explicitly. No service/session input.
"""
from pathlib import Path
import argparse
import re
import subprocess
import sys

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--claw', required=True, type=Path)
parser.add_argument('--destination', required=True, type=Path, help='Explicit durable worktree path')
args = parser.parse_args()
claw = args.claw.resolve()
root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(claw))
from plugins.repository_settings import RepositoryTarget
from plugins.lock_manager import LockManager

RepositoryTarget('claw', claw, 'CultureBotAI/culturebotai-claw').open()
pin = (root / 'scripts/.vendored_canon_ref').read_text().strip()
if not re.fullmatch('[0-9a-f]{40}', pin):
    raise SystemExit('Invalid existing canonical pin')
if not args.destination.is_absolute():
    raise SystemExit('Destination must be an explicit absolute durable path')
destination = args.destination.resolve()
import tempfile
for temporary in (Path('/tmp').resolve(), Path('/private/tmp').resolve(), Path(tempfile.gettempdir()).resolve()):
    if destination.is_relative_to(temporary):
        raise SystemExit('Session worktrees must not be stored in temporary directories')
with LockManager().lock('claw', 'mim1265_prepare_pinned_validation_source'):
    RepositoryTarget('claw', claw, 'CultureBotAI/culturebotai-claw').open()
    if subprocess.run(['git', 'cat-file', '-e', pin + '^{commit}'], cwd=claw).returncode:
        subprocess.run(['git', 'fetch', '--no-tags', 'origin', pin], cwd=claw, check=True)
    if not destination.exists():
        subprocess.run(['git', 'worktree', 'add', '--detach', str(destination), pin], cwd=claw, check=True)
RepositoryTarget('claw', destination, 'CultureBotAI/culturebotai-claw').open()
if subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=destination, text=True).strip() != pin:
    raise SystemExit('Pinned validation source HEAD differs')
if subprocess.check_output(['git', 'status', '--porcelain'], cwd=destination):
    raise SystemExit('Pinned validation source is dirty')
print(destination)
