"""Append report-only corrections; never modify the sealed media packet."""
from pathlib import Path
import copy, hashlib, json
from datetime import datetime, timezone

W = Path.cwd()
S = W / '.temp/w05-final-correction-v1'
P = W / 'reports/all_unmatched_20261107/worker-05/final-correction-v1'
source = S / 'media'
out = S / 'remediation/media-report-v2'
out.mkdir(parents=True, exist_ok=False)
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
dump = lambda p, x: p.write_text(json.dumps(x, indent=2, ensure_ascii=False) + '\n')
changes = []

def amend(name, edits):
    original = json.loads((source / name).read_text())
    successor = copy.deepcopy(original)
    for pointer, expected, replacement, finding in edits:
        keys = pointer.strip('/').split('/')
        node = successor
        for k in keys[:-1]:
            node = node[int(k)] if isinstance(node, list) else node[k]
        key = int(keys[-1]) if isinstance(node, list) else keys[-1]
        assert expected in node[key], (name, pointer)
        before = node[key]
        node[key] = before.replace(expected, replacement)
        changes.append(dict(path=name, json_pointer=pointer, before=before,
                            after=node[key], finding_id=finding))
    dump(out / name, successor)

F1 = 'W05-FINAL-MEDIA-REVIEW-01'
F2 = 'W05-FINAL-MEDIA-REVIEW-02'
amend('decisions.json', [('/decisions/38/final_correction_reassessment/assessment',
    'complete historical human assertion',
    'complete historical MANUAL_CURATION assertion (original human/process supplier not established)', F1)])
amend('primary-read-ledger.json', [('/cases/38/assessment',
    'complete historical human assertion',
    'complete historical MANUAL_CURATION assertion (original human/process supplier not established)', F1)])
amend('finding-dispositions.json', [('/findings/0/correction',
    'complete former human assertion',
    'complete former MANUAL_CURATION assertion (original human/process supplier not established)', F1),
    ('/findings/1/source_locator', 'Manufacturer printed page301, approximate basal formula',
     'Manufacturer printed page302, approximate basal formula', F2)])
amend('mapping-evidence-typing.json', [('/additional_marine_f01_replacement',
    'Inherited human assertion',
    'Inherited MANUAL_CURATION assertion (original human/process supplier not established)', F1)])
handoff = (source / 'HANDOFF.md').read_text()
for old, new in [
    ('historical human assertion', 'historical MANUAL_CURATION assertion (original human/process supplier not established)'),
    ('prior human object', 'prior MANUAL_CURATION object'),
    ('Two inherited active human mapping assertions', 'Two inherited active MANUAL_CURATION mapping assertions with unverified original supplier')]:
    assert old in handoff
    handoff = handoff.replace(old, new)
(out / 'SUPERSEDING-MEDIA-REPORT.md').write_text(
    '# Report metadata correction only\n\n'
    'Author: /root. Independently reported by /root/final_skeptical before correction. '
    'This addendum supersedes the identified report prose and locator in the sealed media v1 packet. '
    'All 45 payloads, source captures, original timestamps, inherited evidence enums and historical objects remain unchanged. '
    'The original packet and scripts remain immutable evidence.\n\n' + handoff)
receipt = dict(at=datetime.now(timezone.utc).isoformat(), author='/root',
    reviewer='/root/final_skeptical', findings=[F1,F2],
    reported_to_coordinator_before_fix=True,
    report_receipt=dict(path=str((S/'review-media/new-findings-v1.json').relative_to(W)),
                        sha256=sha(S/'review-media/new-findings-v1.json')),
    changed_fields=changes,
    unchanged_payloads=True, unchanged_source_captures=True,
    originals=[dict(path=str((source/n).relative_to(W)),sha256=sha(source/n))
               for n in ['HANDOFF.md','decisions.json','primary-read-ledger.json','finding-dispositions.json','mapping-evidence-typing.json']],
    selected_reports=[dict(path=str(p.relative_to(out)),sha256=sha(p)) for p in sorted(out.iterdir())])
dump(out/'remediation-receipt.json',receipt)
dump(out/'MANIFEST.json',dict(files=[dict(path=str(p.relative_to(out)),sha256=sha(p))
                                  for p in sorted(out.iterdir())]))
import shutil
shutil.copytree(out,P/'remediation/media-report-v2')
print(json.dumps(dict(output=str(out), fields=len(changes), manifest_sha256=sha(out/'MANIFEST.json'))))
