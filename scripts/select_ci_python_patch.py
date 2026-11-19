"""Select the installed maintained Python's actual patch for CI (#1450).

uv's explicit patch request selects fixed-version environment metadata. A file
path alone can still select its mutable minor alias in uv0.13.9. This helper
records the actual installed interpreter; it never edits environment metadata
or weakens MIM's runtime guards.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
from pathlib import Path

PROBE = "import json,sys; print(json.dumps({'version': list(sys.version_info[:3]), 'implementation': sys.implementation.name}))"


def select_patch(request):
    if re.fullmatch(r"[0-9]+\.[0-9]+", request) is None:
        raise ValueError("Expected the maintained Python major.minor request")
    result = subprocess.run(
        ["uv", "python", "find", "--managed-python", "--system", request],
        check=True,
        capture_output=True,
        text=True,
        timeout=30,
    )
    selected = Path(result.stdout.strip())
    if not selected.is_absolute():
        raise ValueError("Selected interpreter path must be absolute")
    resolved = selected.resolve(strict=True)
    if not resolved.is_file() or not os.access(resolved, os.X_OK):
        raise ValueError("Selected interpreter must be an executable file")
    digest = hashlib.sha256(resolved.read_bytes()).hexdigest()
    result = subprocess.run(
        [str(resolved), "-I", "-S", "-c", PROBE],
        check=True,
        capture_output=True,
        text=True,
        timeout=10,
    )
    actual = json.loads(result.stdout)
    version = actual["version"]
    if (
        actual["implementation"] != "cpython"
        or len(version) != 3
        or any(type(part) is not int or part < 0 for part in version)
        or version[:2] != [int(part) for part in request.split(".")]
    ):
        raise ValueError("Selected interpreter differs from the maintained Python request")
    if hashlib.sha256(resolved.read_bytes()).hexdigest() != digest:
        raise ValueError("Selected interpreter changed during inspection")
    return {
        "maintained_minor_request": request,
        "actual_patch_request": ".".join(map(str, version)),
        "selected_path": str(selected),
        "resolved_path": str(resolved),
        "executable_sha256": digest,
        "implementation": actual["implementation"],
    }


def main():
    request = os.environ["UV_PYTHON"]
    if request != Path(".python-version").read_text().strip():
        raise ValueError("CI request differs from maintained .python-version")
    record = select_patch(request)
    output = Path(".temp/runtime-ci-diagnostic-1450/python-selection.json")
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("x", encoding="utf-8") as handle:
        json.dump(record, handle, indent=2)
        handle.write("\n")
    with Path(os.environ["GITHUB_ENV"]).open("a", encoding="utf-8") as handle:
        handle.write("UV_PYTHON=" + record["actual_patch_request"] + "\n")
    print(json.dumps(record, indent=2))


if __name__ == "__main__":
    main()
