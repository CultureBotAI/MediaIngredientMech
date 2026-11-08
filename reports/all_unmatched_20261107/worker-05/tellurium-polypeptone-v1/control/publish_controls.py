from pathlib import Path
from datetime import datetime, timezone
import json, hashlib, shutil

W=Path.cwd()
S=W/'.temp/w05-tellurium-polypeptone-v1'
P=W/'reports/all_unmatched_20261107/worker-05/tellurium-polypeptone-v1'
sha=lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
rows=[]
for name in ['tellurium','polypeptone','review','issues','inputs','control']:
    source=S/name
    dest=P/name
    source_files=[p for p in sorted(source.rglob('*')) if p.is_file()]
    for p in source_files:
        q=dest/p.relative_to(source)
        if q.exists():
            assert p.read_bytes()==q.read_bytes(), str(q)
        else:
            q.parent.mkdir(exist_ok=True,parents=True)
            shutil.copy2(p,q)
        rows.append(dict(private_path=str(p.relative_to(W)), published_path=str(q.relative_to(W)),sha256=sha(q),bytes=q.stat().st_size))
    assert {str(p.relative_to(dest)) for p in dest.rglob('*') if p.is_file()}=={str(p.relative_to(source)) for p in source_files},name
receipt=P/'validation/private-public-mirror.json'
assert not receipt.exists()
receipt.write_text(json.dumps(dict(at=datetime.now(timezone.utc).isoformat(),status='PASS',scope='Exact publication copies; no scientific reauthorship, capture bytes and original timestamps retained.',files=rows),indent=2)+'\n')
print(json.dumps(dict(status='PASS',files=len(rows),receipt_sha256=sha(receipt))))
