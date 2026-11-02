"""Read-only integrity verification of the frozen Step7c source/publication packet.

Historical absolute identities are never opened. Supply a current repository
containing the exact maintained source evidence. This does not replay external
producers, grant scientific approval, or certify final PR closure.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import io
import json
import tarfile
from pathlib import Path

INDEX = "source-promotion-evidence.index.json"
STATE = "source_and_promotion_evidence_not_final_closure"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def encode(value):
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode()


def read(path):
    require(path.is_absolute() and path == path.resolve(), "Aliased evidence path")
    require(path.is_file() and not path.is_symlink(), "Nonregular evidence file")
    return path.read_bytes()


def relative(name):
    path = Path(name)
    require(
        not path.is_absolute() and path.parts and ".." not in path.parts,
        "Unsafe relative evidence path",
    )
    return path


def verify(index_path, repository):
    index = json.loads(read(index_path))
    require(index["kind"] == "step7c_source_and_promotion_evidence", "Wrong packet kind")
    selection = index["selection"]
    require(selection["state"] == STATE and selection["captured_at"], "Wrong stage state")
    require(
        selection["scientific_approval_added"] is False
        and selection["supervisor_binding"] is None
        and selection["closure_evidence_separate_from_this_frozen_stage"] is True,
        "Invalid authority/scope declaration",
    )
    require(sha(encode(selection)) == index["selection_sha256"], "Selection hash differs")
    transport = index["publication_transport"]
    require(
        transport["encoding"] == "base64-standard-with-one-final-newline",
        "Unknown archive transport",
    )
    encoded = read(index_path.parent / relative(transport["archive_file"]))
    require(sha(encoded) == transport["archive_text_sha256"], "Archive text hash differs")
    packed = base64.b64decode(encoded[:-1], validate=True)
    require(base64.b64encode(packed) + b"\n" == encoded, "Noncanonical archive encoding")
    require(
        sha(packed) == index["archive_sha256"] and len(packed) == index["archive_bytes"],
        "Decoded archive hash/size differs",
    )
    with tarfile.open(fileobj=io.BytesIO(packed), mode="r:gz") as archive:
        members = archive.getmembers()
        require(
            all(m.isfile() and m.name == Path(m.name).name for m in members),
            "Unsafe archive member",
        )
        require(len({m.name for m in members}) == len(members), "Duplicate archive member")
        payloads = {m.name: archive.extractfile(m).read() for m in members}
    files = selection["files"]
    require(set(payloads) == {item["sha256"] for item in files}, "Payload set differs")
    require(
        len({(item["identity"], item["sha256"]) for item in files}) == len(files),
        "Duplicate historical identity/version",
    )
    for item in files:
        data = payloads[item["sha256"]]
        require(sha(data) == item["sha256"] and len(data) == item["bytes"], "Payload changed")
    for command in selection["commands"]:
        receipt = json.loads(payloads[command["receipt"]["sha256"]])
        log = command["log"]
        require(
            receipt["log"] == log["identity"]
            and receipt["log_sha256"] == log["sha256"]
            and receipt["exit_code"] == command["exit_code"]
            and receipt.get("finished_at"),
            "Completed command/log binding differs",
        )
    for item in selection["maintained_references"]:
        data = read(repository / relative(item["repository_path"]))
        require(
            sha(data) == item["sha256"] and len(data) == item["bytes"],
            "Maintained reference differs: " + item["repository_path"],
        )
    return {
        "status": "PASS",
        "state": STATE,
        "captured_at": selection["captured_at"],
        "scope": selection["verification_scope"],
        "archived_identities": len(files),
        "maintained_references": len(selection["maintained_references"]),
        "commands": len(selection["commands"]),
        "scientific_approval_added": False,
        "supervisor_binding": None,
        "pending_at_capture": selection["pending_at_capture"],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--index", type=Path, default=Path(__file__).absolute().with_name(INDEX))
    parser.add_argument("--repository", type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(verify(args.index.absolute(), args.repository.absolute()), indent=2))
