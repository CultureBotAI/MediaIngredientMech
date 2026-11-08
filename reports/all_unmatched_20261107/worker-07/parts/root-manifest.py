"""Hash the finished worker bundle and retained native review pairs, excluding self."""
import datetime
import hashlib
import json
from pathlib import Path

ROOT = Path.cwd()
OUT = ROOT / "reports/all_unmatched_20261107/worker-07"
DEST = OUT / "MANIFEST.json"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    paths = sorted(p for p in OUT.rglob("*") if p.is_file() and p != DEST)
    assert not any(p.is_symlink() or p.suffix == ".pyc" or "__pycache__" in p.parts for p in paths)
    native = sorted(p for p in (ROOT / "reviews/structured").glob("*-worker07-source-owner-comparison/*") if p.name in {"review.yaml", "review.md"})
    assert len(native) == 4, "Retain both immutable native observations"
    evidence = json.loads((OUT / "evidence.json").read_text())["evidence"]
    source = {}
    for entry in evidence:
        capture = entry["capture"]
        if capture["root"] == "source":
            assert capture["path"] not in source or source[capture["path"]] == capture["sha256"]
            source[capture["path"]] = capture["sha256"]
    result = {"schema_version": 1, "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(), "artifact_root": str(OUT.relative_to(ROOT)), "excludes": ["MANIFEST.json itself", "private worker environment/state and post-commit handoff receipt"], "files": {str(p.relative_to(OUT)): sha(p) for p in paths}, "native_review_files": {str(p.relative_to(ROOT)): sha(p) for p in native}, "external_source_root": "/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5", "external_source_captures": dict(sorted(source.items())), "integrity_only": "Hashes establish exact bytes; scientific applicability remains in per-case and independent-review artifacts. No source, owner or export approval is conferred by this manifest."}
    DEST.write_text(json.dumps(result, indent=2) + "\n")
    for relative, digest in result["files"].items():
        assert sha(OUT / relative) == digest
    for relative, digest in result["native_review_files"].items():
        assert sha(ROOT / relative) == digest
    for relative, digest in result["external_source_captures"].items():
        assert sha(Path(result["external_source_root"]) / relative) == digest
    print(json.dumps({"manifest": str(DEST.relative_to(ROOT)), "sha256": sha(DEST), "artifact_file_count": len(paths), "native_review_file_count": len(native), "external_source_capture_count": len(source), "status": "PASS"}))


if __name__ == "__main__":
    main()
