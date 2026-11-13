"""Pure exact original-root/path/hash acquisition checks shared by native consumers.

No file discovery, external dereference, executable loading or scientific votes.
The caller supplies its already verified input reader and strict JSON decoder.
"""

from __future__ import annotations

import re
from pathlib import PurePosixPath

CAPABILITY = "mim-semantic-transition-evidence/v1"


def require(value, message):
    if not value:
        raise ValueError("Semantic transition: " + message)


def relative(value):
    require(isinstance(value, str) and value, "relative path required")
    path = PurePosixPath(value)
    require(
        not path.is_absolute()
        and ".." not in path.parts
        and str(path) == value
        and "\\" not in value,
        "unsafe relative path",
    )
    return value


class Evidence:
    """Exact original (root, path, hash) acquisitions in separate copied members.

    A beforeimage and installed file can share a logical path only with distinct
    exact hashes. That is explicit phase history, never an ambient replacement.
    """

    def __init__(self, inputs, packet_ref, decode):
        require(set(packet_ref) == {"path", "sha256"}, "pinned packet required")
        self.inputs = inputs
        self.decode = decode
        self.packet = inputs.document(packet_ref["path"], packet_ref["sha256"])
        require(
            set(self.packet)
            == {
                "schema_version",
                "capability",
                "scope",
                "files",
                "publication",
                "sources",
                "history",
            }
            and self.packet["schema_version"] == 1
            and self.packet["capability"] == CAPABILITY
            and self.packet["scope"] == "semantic_reconstruction_not_transaction_reexecution",
            "unsupported evidence packet",
        )
        self.files: dict[tuple[str, str, str], dict] = {}
        physical = set()
        for item in self.packet["files"]:
            require(
                set(item) == {"root", "path", "sha256", "member", "acquired_from"},
                "invalid acquisition",
            )
            root = item["root"]
            require(
                isinstance(root, str)
                and root.startswith("/")
                and str(PurePosixPath(root)) == root
                and ".." not in PurePosixPath(root).parts,
                "invalid original root identity",
            )
            relative(item["path"])
            relative(item["member"])
            require(re.fullmatch(r"[a-f0-9]{64}", item["sha256"]), "invalid acquisition digest")
            key = (root, item["path"], item["sha256"])
            require(
                key not in self.files and item["member"] not in physical,
                "duplicate acquisition or member",
            )
            # acquired_from is exact original capture/archive provenance, not a
            # new storage path and never permission to dereference it in CI.
            require(
                isinstance(item["acquired_from"], str) and item["acquired_from"].startswith("/"),
                "capture provenance required",
            )
            self.files[key] = item
            physical.add(item["member"])
            inputs.read(item["member"], item["sha256"])

    def read(self, root, ref):
        require(set(ref) == {"path", "sha256"}, "exact native file reference required")
        relative(ref["path"])
        key = (root, ref["path"], ref["sha256"])
        require(key in self.files, "missing qualified native evidence: " + str(key))
        item = self.files[key]
        return self.inputs.read(item["member"], item["sha256"])

    def document(self, root, ref):
        return self.decode(self.read(root, ref))
