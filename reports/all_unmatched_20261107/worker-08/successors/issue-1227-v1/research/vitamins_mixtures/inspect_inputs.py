import datetime, hashlib, json, re, subprocess, sys
from html import unescape
from pathlib import Path
import yaml

R = Path('reports/all_unmatched_20261107/worker-08')
S = R / 'successors/issue-1227-v1'
M = S / 'research/vitamins_mixtures'
A = json.loads((M / 'assignment.json').read_text())
E = {e['evidence_id']: e for e in json.loads((R / 'successors/issue-1201-v1/evidence.json').read_text())['evidence']}

def log(path, purpose, locator='entire file displayed'):
    row = {'at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'path': str(path),
           'sha256': hashlib.sha256(path.read_bytes()).hexdigest(), 'purpose': purpose, 'locator': locator}
    with (M / 'inspection-log.jsonl').open('a') as f:
        f.write(json.dumps(row) + '\n')

mode = sys.argv[1]
if mode == 'payload':
    for index in map(int, sys.argv[2:]):
        p = A['proposals'][index]
        path = R / p['after_capture']['path']
        assert hashlib.sha256(path.read_bytes()).hexdigest() == p['after_capture']['sha256']
        print('\nPAYLOAD', index, p['proposal_id'], p['after_capture']['sha256'])
        print(path.read_text())
        log(path, 'Complete selected payload read')
elif mode == 'source':
    for key in sys.argv[2:]:
        e = E[key]
        path = R / e['capture']['path']
        raw = path.read_bytes()
        assert hashlib.sha256(raw).hexdigest() == e['capture']['sha256']
        if raw.startswith(b'%PDF'):
            q = subprocess.run(['pdftotext', '-layout', str(path), '-'], capture_output=True, text=True, check=True)
            text = q.stdout
            if q.stderr: print('PDF_EXTRACTION_WARNINGS', q.stderr)
        else:
            text = raw.decode()
            text = re.sub(r'<script\b[^>]*>.*?</script>|<style\b[^>]*>.*?</style>', '', text, flags=re.S|re.I)
            text = unescape(re.sub('<[^>]+>', ' ', text))
            text = re.sub(r'\s+', ' ', text)
        print('\nSOURCE', key, e.get('url', e.get('locator')), e['capture']['sha256'], '\n', text)
        log(path, 'Actual primary source content read', 'Entire captured body rendered as text; PDF text extraction where applicable')
elif mode == 'cases':
    lo, hi = map(int, sys.argv[2:])
    for i, d in list(enumerate(A['decisions']))[lo:hi]:
        print('\nCASE', i, d['case_id'], d['source'], '\nREASON', d['reasoning'], '\nAPPLICABILITY', d['applicability'], '\nMISSING', d['missing_requirement'], '\nPROPOSALS', d['proposal_ids'])
    log(M / 'assignment.json', 'All selected case outcome fields read', f'decisions[{lo}:{hi}], identity/source/occurrence applicability and missing requirements')
