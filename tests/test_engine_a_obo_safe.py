"""Tests for scripts/_engine_a_obo_safe.sh — the Engine-A OBO-safety gate.

Exit 0 = SAFE (caller runs linkml-term-validator --labels); exit 1 = UNSAFE
(non-OBO prefix would crash OAK, so the caller skips Engine A). Regression focus:
prefix matching must be case-insensitive — the data carries lowercase `mesh:`
while the allowlist uses uppercase `MESH`, and a case-sensitive test previously
classed every mesh record as UNSAFE, so Engine A never validated a MeSH record.
"""

import subprocess
from pathlib import Path

SCRIPT = Path(__file__).parent.parent / "scripts" / "_engine_a_obo_safe.sh"
ALLOWED = "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"


def _rc(tmp_path, content):
    f = tmp_path / "r.yaml"
    f.write_text(content)
    return subprocess.run(["bash", str(SCRIPT), str(f), ALLOWED]).returncode


def test_lowercase_mesh_is_safe(tmp_path):
    # The bug: lowercase `mesh:` != uppercase `MESH` -> used to return 1 (skip).
    assert _rc(tmp_path, "ontology_id: mesh:C016600\n") == 0


def test_uppercase_obo_prefixes_are_safe(tmp_path):
    assert _rc(tmp_path, "ontology_id: CHEBI:15377\n") == 0
    assert _rc(tmp_path, "ontology_id: FOODON:03315720\n") == 0
    assert _rc(tmp_path, "environment_term: ENVO:00002149\n") == 0


def test_non_obo_prefixes_are_unsafe(tmp_path):
    assert _rc(tmp_path, "ontology_id: cas:50-00-0\n") == 1
    assert _rc(tmp_path, 'ontology_id: "kgmicrobe.compound:foo"\n') == 1
    # MICRO is deliberately omitted from obo_prefixes (0-byte stub, no remote db),
    # so a MICRO id is unsafe for Engine A -> deferred to Engine B.
    assert _rc(tmp_path, "ontology_id: MICRO:0000114\n") == 1


def test_mixed_obo_and_non_obo_is_unsafe(tmp_path):
    # any non-OBO prefix in the file makes the whole file unsafe for Engine A
    assert _rc(tmp_path, "ontology_id: mesh:C016600\nenvironment_term: cas:1-2-3\n") == 1


def test_no_ontology_ids_is_safe(tmp_path):
    assert _rc(tmp_path, "preferred_term: Foo ingredient\n") == 0
