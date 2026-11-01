"""Verify the frozen report inventory without the original run directory."""

from pathlib import Path
import hashlib
import json


root = Path(__file__).resolve().parent.parent
manifest = json.loads((root / "execution/inventory.json").read_text())
for entry in manifest["files"]:
    path = root / entry["path"]
    assert path.resolve().is_relative_to(root.resolve()), entry["path"]
    data = path.read_bytes()
    assert len(data) == entry["bytes"], entry["path"]
    assert hashlib.sha256(data).hexdigest() == entry["sha256"], entry["path"]
print(f"Verified {len(manifest['files'])} archived files; no scientific approval asserted.")
