from pathlib import Path
import datetime, hashlib, json, os, subprocess, sys

RUN = Path(__file__).resolve().parent
ORIGINAL = RUN.parent.parent
CLAW_ORIGINAL = (ORIGINAL / '../../KG-Hub/KG-Microbe/culturebotai-claw').resolve()
OLD_RUN = ORIGINAL / 'output/sssom-generation-20261031T213407Z'
repo, name, *cmd = sys.argv[1:]
ci_environment = repo == 'claw-ci'
if ci_environment:
    repo = 'claw'
if cmd and cmd[0] == '--':
    cmd = cmd[1:]
root = RUN / repo
venv = (CLAW_ORIGINAL if repo == 'claw' else ORIGINAL) / '.venv'
env = dict(os.environ)
env.update(
    PYTHONDONTWRITEBYTECODE='1',
    PYTHONPATH=':'.join(map(str, [RUN/'claw/src', RUN/'claw', RUN/'mim/src', OLD_RUN/'test-deps'])),
    UV_PROJECT_ENVIRONMENT=str(venv), UV_NO_SYNC='1', UV_CACHE_DIR=str(RUN/'uv-cache'),
    UV_TOOL_DIR=str(RUN/'uv-tools'), UV_TOOL_BIN_DIR=str(RUN/'uv-tool-bin'),
    PYSTOW_HOME=str(OLD_RUN/'ontology-cache'),
    MEDIAINGREDIENTMECH_ROOT=str(RUN/'mim'), CULTUREMECH_ROOT=str((ORIGINAL/'../CultureMech').resolve()),
    KGMICROBE_ROOT=str((ORIGINAL/'../../KG-Hub/KG-Microbe/kg-microbe').resolve()),
    CLAW_ROOT=str(RUN/'claw'), CLAW_SRC=str(RUN/'claw/src'),
    OPENCLAW_ORCHESTRATION_ROOT=str(RUN/'claw'), OPENCLAW_WORKSPACE=str(RUN/'claw/workspace'),
    PATH=str(venv/'bin') + ':' + os.environ['PATH'],
)
if ci_environment:
    # Match the hermetic CI suite, which declares no live sibling checkouts.
    # Keep the real-root generation/QC profile separate and retain its failures.
    for key in (
        'MEDIAINGREDIENTMECH_ROOT', 'CULTUREMECH_ROOT', 'KGMICROBE_ROOT',
        'CLAW_ROOT', 'CLAW_SRC', 'OPENCLAW_ORCHESTRATION_ROOT', 'OPENCLAW_WORKSPACE',
        'COMMUNITYMECH_ROOT', 'TRAITMECH_ROOT', 'PROTEINTRAITSMECH_ROOT',
        'ANTIBIOTICMECH_ROOT', 'CELLSTRUCTUREMECH_ROOT', 'HABITATMECH_ROOT',
        'NATURALPRODUCTMECH_ROOT', 'TAXONMECH_ROOT', 'PATHWAYMECH_ROOT',
        'DUFMECH_ROOT', 'CMMMECH_ROOT', 'AIMECH_ROOT',
    ):
        env.pop(key, None)
    env['PYTHONPATH'] = ':'.join(map(str, [RUN/'claw/src', RUN/'claw', OLD_RUN/'test-deps']))
(RUN/'logs').mkdir(exist_ok=True)
log_path = RUN/'logs'/f'{name}.log'
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
with log_path.open('x') as log:
    proc = subprocess.run(cmd, cwd=root, env=env, stdout=log, stderr=subprocess.STDOUT)
receipt = {'name':name, 'argv':cmd, 'cwd':str(root), 'started_at':started,
           'environment_profile':'claw-ci-no-sibling-roots' if ci_environment else 'generation-and-native-qc',
           'finished_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
           'exit_code':proc.returncode, 'log':str(log_path),
           'log_sha256':hashlib.sha256(log_path.read_bytes()).hexdigest()}
(RUN/'logs'/f'{name}.json').write_text(json.dumps(receipt, indent=2)+'\n')
print(json.dumps(receipt, indent=2))
print(log_path.read_text()[-2500:])
raise SystemExit(proc.returncode)
